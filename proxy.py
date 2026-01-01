import sys, io, os, json, base64, hashlib, uuid, platform, subprocess
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

if len(sys.argv) != 3:
    print("Use: proxy.py <SUPABASE_URL> <ANON_KEY>", file=sys.stderr)
    sys.exit(4)

SUPABASE_URL = sys.argv[1].rstrip("/")
ANON_KEY = sys.argv[2]

def sha256sum(path):
    try:
        with open(path, "rb") as f:
            h = hashlib.sha256()
            while chunk := f.read(8192):
                h.update(chunk)
            return h.hexdigest()
    except Exception as e:
        print(f"ERR: hash failed for {path}: {e}", file=sys.stderr)
        return None

def _run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True, errors="ignore").strip()
    except Exception:
        return ""


def _normalize(label, value):
    value = (value or "").strip().upper() or "N/A"
    return f"{label}:{value}"


def _linux_hwid_parts():
    cpu = _run_cmd("lscpu | grep -i 'model name' | head -n1 | cut -d: -f2")
    board_serial = _run_cmd("cat /sys/class/dmi/id/board_serial")
    board_model = _run_cmd("cat /sys/class/dmi/id/board_name")
    gpu = _run_cmd("lspci | grep -i -E 'vga|3d|display' | head -n1")
    return [
        _normalize("CPU", cpu),
        _normalize("BOARD", board_serial or board_model),
        _normalize("GPU", gpu),
    ]


def _windows_hwid_parts():
    cpu = _run_cmd("wmic cpu get ProcessorId /value") or _run_cmd("wmic cpu get Name /value")
    board = _run_cmd("wmic baseboard get SerialNumber,Product /value")
    gpu = _run_cmd("wmic path win32_videocontroller get PNPDeviceID,Name /value")
    return [
        _normalize("CPU", cpu),
        _normalize("BOARD", board),
        _normalize("GPU", gpu),
    ]


def _fallback_hwid_parts():
    # Last resort: use hostname and MAC, but keep fields stable
    try:
        node = uuid.getnode()
        mac_bytes = node.to_bytes(6, 'big', signed=False)
    except Exception:
        mac_bytes = b''
    host = (os.uname().nodename if hasattr(os, 'uname') else os.getenv('COMPUTERNAME','')) or ''
    return [
        _normalize("CPU", host),
        _normalize("BOARD", host),
        _normalize("GPU", mac_bytes.hex()),
    ]


def compute_hwid():
    system = platform.system().lower()
    if "linux" in system:
        parts = _linux_hwid_parts()
    elif "windows" in system:
        parts = _windows_hwid_parts()
    else:
        parts = []

    if parts and not any(p.endswith("N/A") for p in parts):
        normalized = "|".join(parts)
        return hashlib.sha256(normalized.encode("utf-8")).hexdigest()

    # Fallback path when we fail to collect stable fields
    normalized = "|".join(_fallback_hwid_parts())
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
proxy_path = os.path.join(BASE_DIR, "proxy.py")
eden_path = os.path.join(BASE_DIR, "edenEquips.pl")

hash_proxy = sha256sum(proxy_path) or "missing"
hash_eden = sha256sum(eden_path) or "missing"

HWID = compute_hwid()
print(f"HWID: {HWID}", file=sys.stderr)

def call_rpc_get_macro(supabase_url, anon_key, hwid, hash_proxy, hash_eden):
    url = supabase_url.rstrip("/") + "/rest/v1/rpc/get_macro_for_client"
    headers = {
        "apikey": anon_key,
        "Authorization": "Bearer " + anon_key,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    payload = {"p_hwid": hwid, "p_proxy_hash": hash_proxy, "p_eden_hash": hash_eden}
    data = json.dumps(payload).encode("utf-8")
    req = Request(url, data=data, headers=headers, method="POST")
    try:
        with urlopen(req, timeout=20) as resp:
            body = resp.read().decode('utf-8')
            j = json.loads(body)
            return j
    except HTTPError as e:
        try:
            body = e.read().decode('utf-8')
            print("HTTPError RPC:", e.code, body, file=sys.stderr)
        except:
            print("HTTPError RPC:", e.code, file=sys.stderr)
        return {"error": f"http_{e.code}"}
    except URLError as e:
        print("URLError RPC:", e, file=sys.stderr)
        return {"error": "url_err"}
    except Exception as e:
        print("ERR RPC:", e, file=sys.stderr)
        return {"error": "err"}

res = call_rpc_get_macro(SUPABASE_URL, ANON_KEY, HWID, hash_proxy, hash_eden)
if not res:
    print("ERR: empty rpc response", file=sys.stderr)
    sys.exit(5)

if res.get("error"):
    print("ERR from rpc:", res["error"], file=sys.stderr)
    sys.exit(3)

b64_text = res.get("content_base64")
if not b64_text:
    print("ERR: no content", file=sys.stderr)
    sys.exit(6)

try:
    decoded = base64.b64decode(b"".join(b64_text.encode('ascii', errors='ignore').split()))
    sys.stdout.buffer.write(decoded)
    sys.exit(0)
except Exception as e:
    print(f"ERR: failed decode or output: {e}", file=sys.stderr)
    sys.exit(6)

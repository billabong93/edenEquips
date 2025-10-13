import sys, io, os, json, base64, hashlib, uuid
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import quote_plus

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

def compute_hwid():
    try:
        node = uuid.getnode()
        mac_bytes = node.to_bytes(6, 'big', signed=False)
    except Exception:
        mac_bytes = b''
    host = (os.uname().nodename if hasattr(os, 'uname') else os.getenv('COMPUTERNAME','')) or ''
    raw = mac_bytes + host.encode('utf-8')
    return hashlib.sha256(raw).hexdigest()

def supabase_get(table, filters=None, select="*"):
    base = f"{SUPABASE_URL}/rest/v1/{table}"
    qs = []
    if filters:
        for k,v in filters.items():
            qs.append(f"{quote_plus(k)}={quote_plus(v)}")
    qs.append("select=" + quote_plus(select))
    url = base + "?" + "&".join(qs)
    req = Request(url, headers={
        "apikey": ANON_KEY,
        "Authorization": "Bearer " + ANON_KEY,
        "Accept": "application/json"
    })
    try:
        with urlopen(req, timeout=20) as resp:
            body = resp.read().decode('utf-8')
            return json.loads(body)
    except HTTPError as e:
        print("HTTPError supabase_get: {} {}".format(e.code, e.reason), file=sys.stderr)
        try:
            print(e.read().decode('utf-8'), file=sys.stderr)
        except:
            pass
        return None
    except URLError as e:
        print("URLError supabase_get: {}".format(e), file=sys.stderr)
        return None
    except Exception as e:
        print("ERR supabase_get: {}".format(e), file=sys.stderr)
        return None

def supabase_post(table, payload):
    url = f"{SUPABASE_URL}/rest/v1/{table}"
    headers = {
        "apikey": ANON_KEY,
        "Authorization": "Bearer " + ANON_KEY,
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    req = Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method="POST")
    try:
        with urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except HTTPError as e:
        print("HTTPError supabase_post: {} {}".format(e.code, e.reason), file=sys.stderr)
        try:
            print(e.read().decode('utf-8'), file=sys.stderr)
        except:
            pass
        return None
    except URLError as e:
        print("URLError supabase_post: {}".format(e), file=sys.stderr)
        return None
    except Exception as e:
        print("ERR supabase_post: {}".format(e), file=sys.stderr)
        return None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
proxy_path = os.path.join(BASE_DIR, "proxy.py")
eden_path = os.path.join(BASE_DIR, "edenEquips.pl")

hash_proxy = sha256sum(proxy_path) or "missing"
hash_eden = sha256sum(eden_path) or "missing"

HWID = compute_hwid()
print(f"HWID: {HWID}", file=sys.stderr)
print(f"proxy_hash: {hash_proxy}", file=sys.stderr)
print(f"eden_hash: {hash_eden}", file=sys.stderr)

res = supabase_get("clients", filters={"hwid": "eq." + HWID})
if res is None:
    print("ERR: failed to query DB", file=sys.stderr)
    sys.exit(5)

if len(res) == 0:
    print("HWID not authorized. Registering inactive.", file=sys.stderr)
    payload = {"hwid": HWID, "active": False}
    ins = supabase_post("clients", payload)
    if ins is None:
        print("ERR: failed to register HWID", file=sys.stderr)
        sys.exit(5)
    sys.exit(3)

client_active = res[0].get("active", False)
if not client_active:
    print("HWID found but not active.", file=sys.stderr)
    sys.exit(3)

file_hashes = supabase_get("file_hashes", select="filename,sha256")
if file_hashes is None:
    print("ERR: failed to query file_hashes", file=sys.stderr)
    sys.exit(5)

hash_ok = True
for fname, fhash in [("proxy.py", hash_proxy), ("edenEquips.pl", hash_eden)]:
    matching = [r for r in file_hashes if r["filename"] == fname]
    if not matching or matching[0]["sha256"] != fhash:
        print(f"{fname} não autorizado ou alterado", file=sys.stderr)
        hash_ok = False

if not hash_ok:
    sys.exit(3)

mres = supabase_get("macros", filters={"name":"eq.eventMacros"}, select="content_base64")
if mres is None:
    print("ERR: failed to query macros", file=sys.stderr)
    sys.exit(5)
if not mres or len(mres) == 0:
    print("ERR: macro not found", file=sys.stderr)
    sys.exit(6)

b64_text = mres[0].get("content_base64")
if not b64_text:
    print("ERR: macro content empty", file=sys.stderr)
    sys.exit(6)

try:
    decoded = base64.b64decode(b"".join(b64_text.encode('ascii', errors='ignore').split()))
    sys.stdout.buffer.write(decoded)
    sys.exit(0)
except Exception as e:
    print(f"ERR: failed decode or output: {e}", file=sys.stderr)
    sys.exit(6)

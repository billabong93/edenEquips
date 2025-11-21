# GUI de configuração para edenEquips

import os
import re
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

# ==============================
# Constantes
# ==============================
EMPTY_LABEL = "(vazio)"

# Lado esquerdo (configurações) e direito (descrição)
LEFT_W  = 160   # largura mínima painel de Configuração/Valor
RIGHT_W = 320   # largura mínima painel de descrição

# ==============================
# Caminhos
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OPENKORE_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))
CONTROL_DIR = os.path.join(OPENKORE_DIR, "control")
CONFIG_FILE = os.path.join(CONTROL_DIR, "config.txt")

if not os.path.isdir(CONTROL_DIR):
    os.makedirs(CONTROL_DIR, exist_ok=True)

# ==============================
# Helpers numéricos
# ==============================
def num_range(start, end_inclusive):
    """Gera {'start', 'start+1', ..., 'end_inclusive'} como strings."""
    return {str(i) for i in range(start, end_inclusive + 1)}

def quest_off(start, end_inclusive):
    """Gera {'start', ..., 'end_inclusive', 'off'} como strings."""
    vals = num_range(start, end_inclusive)
    vals.add("off")
    return vals
    
# ==============================
# Opções e regras de validação
# ==============================
options = {
    "lvlQuest03": {
        "group": "Arma do Éden I",
        "label": "Nível da Quest [26–32]",
        "desc": "QUEST ARMA DO ÉDEN I - LVL [26-32] \n\nEscolha o nível em que seu personagem vai começar a quest.\nÉ possível fazer apenas a Quest [23-32] ou [33-39].\n26 = (padrão)\noff = Desativa a Quest",
        "default": "26",
        "allowed": quest_off(26, 32),
    },
    "lvlQuest04": {
        "group": "Arma do Éden I",
        "label": "Nível da Quest [33–39]",
        "desc": "QUEST ARMA DO ÉDEN I - LVL [33-39] \n\nEscolha o nível em que seu personagem vai começar a quest.\nÉ possível fazer apenas a Quest [23-32] ou [33-39].\n33 = (padrão)\noff = Desativa a Quest",
        "default": "33",
        "allowed": quest_off(33, 39),
    },
    "armaI": {
        "group": "Arma do Éden I",
        "label": "Arma do Éden I",
        "desc": "ESCOLHA A ARMA DO ÉDEN I \n\nArmas para as classes:\nEspadachim, Noviço, Mercador.\n(https://browiki.org/wiki/Equipamentos_do_Éden#Armas) \n\nOpções: \n0 = Sabre / Cetro (padrão)\n1 = Espada / Maça",
        "default": "0",
        "allowed": {"0", "1"},
    },

    "lvlQuest05": {
        "group": "Arma do Éden II",
        "label": "Nível da Quest [40–49]",
        "desc": "QUEST ARMA DO ÉDEN II - LVL [40-49] \n\nEscolha o nível em que seu personagem vai começar a quest.\nÉ possível fazer apenas a Quest [40-49] ou [75+].\n40 = (padrão)\noff = Desativa a Quest",
        "default": "40",
        "allowed": quest_off(40, 49),
    },
    "lvlQuest07": {
        "group": "Arma do Éden II",
        "label": "Nível da Quest [75+]",
        "desc": "QUEST ARMA DO ÉDEN II - LVL [75+] \n\nEscolha o nível em que seu personagem vai começar a quest.\nÉ possível fazer apenas a Quest [40-49] ou [75+].\n75 = (padrão)\noff = Desativa a Quest\n\nObservação: Essa Quest é redundante, pois é possível adquirir a Arma III no nível 60.",
        "default": "75",
        "allowed": quest_off(75, 99),
    },
    "armaII": {
        "group": "Arma do Éden II",
        "label": "Arma do Éden II",
        "desc": "ESCOLHA A ARMA DO ÉDEN II \n\nArmas para as classes: \nEspadachim, Cavaleiro, Templário, Noviço, Sacerdote, Monge, Mercador, Ferreiro, Alquimista, Espiritualista.\n(https://browiki.org/wiki/Equipamentos_do_Éden#Armas) \n\nOpções: \n0 = Sabre / Cetro / Adaga (padrão) \n1 = Espada / Maça / Cetro",
        "default": "0",
        "allowed": {"0", "1"},
    },

    "lvlQuest08": {
        "group": "Arma do Éden III",
        "label": "Nível da Quest [60–69]",
        "desc": "QUEST ARMA DO ÉDEN III - LVL [60-69] \n\nEscolha o nível em que seu personagem vai começar a quest.\n60 = (padrão)\noff = Desativa a Quest",
        "default": "60",
        "allowed": quest_off(60, 69),
    },
    "armaIII": {
        "group": "Arma do Éden III",
        "label": "Arma do Éden III",
        "desc": "ESCOLHA A ARMA DO ÉDEN III \n\nArmas para as classes: \nCavaleiro, Templário, Sacerdote, Monge, Sábio, Bardo, Odalisca, Ferreiro, Alquimista, Mercenário, Espiritualista, Ninja.\n(https://browiki.org/wiki/Equipamentos_do_Éden#Armas) \n\nOpções: \n0 = Espada / Cetro / Maça / Arco / Adaga (padrão) \n1 = Sabre / Maça / Dicionário / Soqueira / Violino / Chicote / Katar / Cetro / Humma \n2 = Lança / Dicionário / Machado",
        "default": "0",
        "allowed": {"0", "1", "2"},
    },

    "lvlQuest09": {
        "group": "Encantamentos e Cartas",
        "label": "Nível da Quest [70–79]",
        "desc": "QUEST ENCANTAMENTO - LVL [70-79] \n\nEscolha o nível em que seu personagem vai começar a quest.\n70 = (padrão)\noff = Desativa a Quest",
        "default": "70",
        "allowed": quest_off(70, 79),
    },
    "encant": {
        "group": "Encantamentos e Cartas",
        "label": "Tipo de Encantamento",
        "desc": "ESCOLHA O ENCANTAMENTO +3% ATQ/ATQM\n\nOpções: \n0 = Ataque Físico (padrão) \n1 = Ataque Mágico",
        "default": "0",
        "allowed": {"0", "1"},
    },

    "lvlQuest10": {
        "group": "Encantamentos e Cartas",
        "label": "Nível da Quest [80–89]",
        "desc": "QUEST DE CARTA - LVL [80-89] \n\nEscolha o nível em que seu personagem vai começar a quest.\n80 = (padrão)\noff = Desativa a Quest",
        "default": "80",
        "allowed": quest_off(80, 89),
    },
    "carta": {
        "group": "Encantamentos e Cartas",
        "label": "Tipo de Carta",
        "desc": "ESCOLHA AS CARTAS \n\n+20% DMG / +10% MDMG ou +3% HEAL \n\nOpções: \n0 = Bruto(Padrão) \n1 = Planta \n2 = Inseto \n3 = Peixe \n4 = Dragão \n5 = Cura",
        "default": "0",
        "allowed": num_range(0, 5),
    },
    "lvlQuest11": {
        "group": "Encantamentos e Cartas",
        "label": "Nível da Quest [90–99]",
        "desc": "QUEST ENCANTAMENTO COM CARTAS II - LVL [90-99] \n\nEscolha o nível em que seu personagem vai começar a quest.\n90 = (padrão)\noff = Desativa a Quest",
        "default": "90",
        "allowed": quest_off(90, 99),
    },

    "semAsas": {
        "group": "Consumíveis",
        "label": "Sem Asas de Mosquito",
        "desc": "Desativar compra de Asas de Mosquito\n\nOpções:\n0 = Não (padrão) \n1 = Sim",
        "default": "0",
        "allowed": {"0", "1"},
    },
    "semPot": {
        "group": "Consumíveis",
        "label": "Sem Poções Laranjas",
        "desc": "Desativar compra de Poções Laranjas\n\nOpções:\n0 = Não (padrão) \n1 = Sim",
        "default": "0",
        "allowed": {"0", "1"},
    },
}

# Definição das abas
TAB_DEFS = [
    ("Instrutora Boya", [
        "lvlQuest03", "lvlQuest04", "armaI",
        "lvlQuest05", "lvlQuest07", "armaII",
    ]),
    ("Instrutor Ur", [
        "lvlQuest08", "armaIII",
        "lvlQuest09", "encant",
        "lvlQuest10", "carta",
        "lvlQuest11",
    ]),
    ("Itens", [
        "semAsas", "semPot",
    ]),
]

BLOCK_BEGIN = "# --- Configurações do edenEquips --- BEGIN\n"
BLOCK_END   = "\n# --- Configurações do edenEquips --- END"

# ==============================
# Utilidades de arquivo config
# ==============================
def load_existing_values():
    """Chaves ausentes aparecem como (vazio)."""
    vals = {k: EMPTY_LABEL for k in options}
    if not os.path.isfile(CONFIG_FILE):
        return vals
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                s = line.strip()
                if not s or s.startswith("#"):
                    continue
                m = re.match(r"^(\w+)\s+(\S+)$", s)
                if m:
                    k, v = m.group(1), m.group(2)
                    if k in options:
                        vals[k] = v
    except Exception:
        pass
    return vals

def allowed_with_empty(key):
    """(vazio) + valores permitidos para a opção."""
    raw = options[key]["allowed"]
    allowed = [str(v) for v in sorted(raw)]
    return [EMPTY_LABEL] + allowed

def write_block_to_config(lines_to_write):
    """Escreve/substitui o bloco no config.txt, ignorando (vazio) e 0."""
    filtered = []
    for k, v in lines_to_write:
        if v not in (EMPTY_LABEL, "0", "", None):
            filtered.append(f"{k} {v}")

    if os.path.isfile(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    else:
        content = ""

    pattern = re.compile(re.escape(BLOCK_BEGIN) + r".*?" + re.escape(BLOCK_END), flags=re.DOTALL)
    content_without_block = re.sub(pattern, "", content).strip()
    content_without_block += ("\n" if content_without_block and not content_without_block.endswith("\n") else "")

    if filtered:
        block = [BLOCK_BEGIN, *filtered, BLOCK_END]
        new_content = content_without_block + "\n" + "\n".join(block) + "\n"
    else:
        new_content = content_without_block + ("\n" if content_without_block and not content_without_block.endswith("\n") else "")

    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

# ==============================
# GUI (Tkinter)
# ==============================
class ConfigApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("[edenEquips] Configurador ")
        self.geometry("720x480")
        self.minsize(720, 480)

        # Fundo geral
        self.configure(bg="#e6e6e6")

        self.current_values = load_existing_values()

        # widgets de entrada por chave
        self.inputs = {}          # key -> Combobox
        self.current_focus_key = None
        self.tab_frames = {}      # título da aba
        self._active_canvas = None

        self._build_widgets()
        self._populate_rows()

    # --------- UI
    def _build_widgets(self):
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except Exception:
            pass

        base_bg  = "#e6e6e6"
        panel_bg = "#f5f5f5"

        # Frames e notebook
        style.configure("App.TFrame",   background=base_bg)
        style.configure("Panel.TFrame", background=panel_bg)
        style.configure("TNotebook",    background=base_bg, borderwidth=0)
        style.configure("TNotebook.Tab", padding=(10, 4), font=("Segoe UI", 9))

        # Labels
        style.configure(
            "Header.TLabel",
            font=("Segoe UI", 11, "bold"),
            background=base_bg,
            foreground="#222",
        )
        style.configure(
            "Title.TLabel",
            font=("Segoe UI", 9, "bold"),
            background=panel_bg,
            foreground="#333",
        )
        style.configure(
            "Key.TLabel",
            font=("Segoe UI", 9),
            background=panel_bg,
            foreground="#222",
        )
        style.configure(
            "Group.TLabel",
            font=("Segoe UI", 9, "bold"),
            background=panel_bg,
            foreground="#555",
        )

        # Combobox estilos
        style.configure("Placeholder.TCombobox", foreground="#888")
        style.configure("Normal.TCombobox",      foreground="#111")

        # Botões
        style.configure("Danger.TButton", foreground="#fff", background="#d9534f")
        style.map("Danger.TButton", background=[("active", "#c9302c")])

        self.option_add("*TCombobox*Listbox.font", ("Segoe UI", 9))

        lbl = ttk.Label(
            self,
            text="[edenEquips] CONFIGURADOR \nInsira/Escolha os valores nos campos. *use (vazio) para limpar configurações*",
            anchor="w",
            style="Header.TLabel",
        )
        lbl.pack(fill="x", padx=16, pady=(12, 8))

        main = ttk.Frame(self, style="App.TFrame")
        main.pack(fill="both", expand=True, padx=16, pady=(0, 12))

        # Notebook
        self.nb = ttk.Notebook(main)
        self.nb.grid(row=0, column=0, sticky="nsew", padx=(0, 6))

        # TAB_DEFS
        for tab_title, key_list in TAB_DEFS:
            tab_container = ttk.Frame(self.nb, style="Panel.TFrame")
            self.nb.add(tab_container, text=tab_title)

            left_container = ttk.Frame(tab_container, style="Panel.TFrame")
            left_container.pack(fill="both", expand=True, padx=4, pady=4)

            canvas = tk.Canvas(
                left_container,
                highlightthickness=0,
                bg=panel_bg,
                borderwidth=0,
            )
            vsb = ttk.Scrollbar(left_container, orient="vertical", command=canvas.yview)
            canvas.configure(yscrollcommand=vsb.set)

            canvas.grid(row=0, column=0, sticky="nsew")
            vsb.grid(row=0, column=1, sticky="ns", padx=(3, 0))

            left_container.rowconfigure(0, weight=1)
            left_container.columnconfigure(0, weight=1)

            left = ttk.Frame(canvas, style="Panel.TFrame")
            win_id = canvas.create_window((0, 0), window=left, anchor="nw")

            left.grid_columnconfigure(0, weight=1, minsize=160)  # coluna "Configuração"
            left.grid_columnconfigure(1, weight=0, minsize=40)   # coluna "Valor"

            ttk.Label(left, text="Configuração", style="Title.TLabel").grid(
                row=0, column=0, sticky="w", padx=(2, 6), pady=(2, 6)
            )
            ttk.Label(left, text="Valor", style="Title.TLabel").grid(
                row=0, column=1, sticky="w", padx=(6, 2), pady=(2, 6)
            )

            # Scrollregion
            def _on_left_config(event, c=canvas, sb=vsb):
                c.configure(scrollregion=c.bbox("all"))
                bbox = c.bbox("all")
                if bbox:
                    height = bbox[3] - bbox[1]
                else:
                    height = 0
                if height <= c.winfo_height():
                    # Sem scroll
                    sb.grid_remove()
                    c.yview_moveto(0)
                else:
                    sb.grid()

            left.bind("<Configure>", _on_left_config)

            # Scroll
            left.bind("<Enter>", lambda e, c=canvas: self._bind_mousewheel(c))
            left.bind("<Leave>", lambda e: self._unbind_mousewheel())

            self.tab_frames[tab_title] = {
                "keys": key_list,
                "container": tab_container,
                "left_container": left_container,
                "canvas": canvas,
                "scrollbar": vsb,
                "left": left,
                "win_id": win_id,
            }

        # Descrição
        right = ttk.Frame(main, width=RIGHT_W, style="Panel.TFrame")
        right.grid(row=0, column=1, sticky="nsew")
        ttk.Label(right, text="Descrição da opção selecionada:", style="Title.TLabel").pack(
            anchor="w", padx=8, pady=(6, 2)
        )
        self.desc = tk.Text(
            right,
            height=10,
            wrap="word",
            font=("Segoe UI", 9),
            bg="white",
            relief="solid",
            borderwidth=1,
        )
        self.desc.configure(state="disabled", padx=8, pady=6)
        self.desc.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        self.desc.tag_configure("h1",   font=("Segoe UI", 10, "bold"))
        self.desc.tag_configure("bold", font=("Segoe UI", 9,  "bold"))
        self.desc.tag_configure("mono", font=("Consolas",  9))
        self.desc.tag_configure("note", foreground="#666")

        # Links
        self.desc.tag_configure("link", foreground="#0066cc", underline=True)
        self.desc.tag_bind("link", "<Enter>", lambda e: self.desc.config(cursor="hand2"))
        self.desc.tag_bind("link", "<Leave>", lambda e: self.desc.config(cursor=""))
        self.desc.tag_bind("link", "<Button-1>", self._on_link_click)

        main.columnconfigure(0, weight=3, minsize=LEFT_W)
        main.columnconfigure(1, weight=2, minsize=RIGHT_W)
        main.rowconfigure(0, weight=1)

        # Botões fixos
        btns = ttk.Frame(self, style="App.TFrame")
        btns.pack(fill="x", padx=16, pady=(0, 12))
        ttk.Button(btns, text="Restaurar para (vazio)", command=self.restore_default).pack(side="left")
        ttk.Button(btns, text="Salvar e Fechar", command=self.save_and_close).pack(side="right")
        ttk.Button(btns, text="Cancelar", command=self.destroy).pack(side="right", padx=(0, 8))

        self.bind("<Control-s>", lambda e: self.save_and_close())
        self.bind("<Escape>",    lambda e: self.destroy())

    # Scroll
    def _bind_mousewheel(self, canvas):

        bbox = canvas.bbox("all")
        if bbox:
            height = bbox[3] - bbox[1]
        else:
            height = 0
        if height > canvas.winfo_height():
            self._active_canvas = canvas
            self.bind_all("<MouseWheel>", self._on_mousewheel)
        else:
            self._active_canvas = None
            self.unbind_all("<MouseWheel>")

    def _unbind_mousewheel(self):
        self._active_canvas = None
        self.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        if self._active_canvas is not None:
            self._active_canvas.yview_scroll(int(-1 * (event.delta / 20)), "units")

    # Abas
    def _populate_rows(self):

        for tab_info in self.tab_frames.values():
            left = tab_info["left"]
            for child in left.grid_slaves():
                info = child.grid_info()
                if int(info.get("row", 0)) > 0:
                    child.destroy()

        self.inputs.clear()

        for tab_title, tab_info in self.tab_frames.items():
            left = tab_info["left"]
            keys = tab_info["keys"]

            r = 1
            current_group = None

            for key in keys:
                opt = options[key]
                group = opt.get("group")
                label = opt.get("label", key)

                if group and group != current_group:
                    current_group = group
                    lbl_group = ttk.Label(left, text=group, style="Group.TLabel")
                    lbl_group.grid(row=r, column=0, columnspan=2, sticky="w", padx=2, pady=(8, 2))
                    r += 1

                lbl = ttk.Label(
                    left,
                    text=label,
                    style="Key.TLabel",
                    wraplength=200,
                    justify="left"
                )
                lbl.grid(row=r, column=0, sticky="w", padx=(4, 6), pady=2)
                lbl.bind("<Button-1>", lambda e, k=key: self._focus_row(k))

                # Combobox
                allowed = allowed_with_empty(key)
                cb = ttk.Combobox(left, values=allowed, state="normal", width=7)
                cur = self.current_values.get(key, EMPTY_LABEL)
                cb.set(cur if cur in allowed else EMPTY_LABEL)
                cb.grid(row=r, column=1, sticky="w", padx=(0, 6), pady=2)

                self.inputs[key] = cb
                self._apply_cb_style(key)

                cb.bind("<<ComboboxSelected>>", lambda e, k=key: self._on_value_change(k))
                cb.bind("<FocusIn>",           lambda e, k=key: self._focus_row(k))
                cb.bind("<FocusOut>",          lambda e, k=key: self._validate_field(k))
                cb.bind("<KeyRelease>",        lambda e, k=key: self._on_typing(k))

                r += 1

        first_key = next(iter(options))
        self._focus_row(first_key)

    # Interações / Estilos dinâmicos
    def _apply_cb_style(self, key):
        cb = self.inputs[key]
        val = cb.get().strip()
        if val == EMPTY_LABEL:
            cb.configure(style="Placeholder.TCombobox")
        else:
            cb.configure(style="Normal.TCombobox")

    def _on_typing(self, key):
        self._apply_cb_style(key)

    def _focus_row(self, key):
        self.current_focus_key = key
        text = options[key]["desc"]
        # passa também o nome da variável para a descrição
        self._set_desc(text, allowed_with_empty(key), key)

    def _on_value_change(self, key):
        self._validate_field(key)
        self._focus_row(key)
        self._apply_cb_style(key)

    def _validate_field(self, key):
        cb = self.inputs[key]
        val = cb.get().strip()
        allowed = set(allowed_with_empty(key))
        if val not in allowed:
            messagebox.showerror(
                "Valor inválido",
                f"Valor '{val}' não é permitido para '{key}'.\nPermitidos: {sorted(allowed)}"
            )
            cb.set(EMPTY_LABEL)
            val = EMPTY_LABEL
        self.current_values[key] = val
        self._apply_cb_style(key)

    # ---- LINKS NA DESCRIÇÃO ----
    def _insert_with_links(self, text):
        """
        Insere o texto na caixa de descrição, detectando URLs
        (http/https) e aplicando a tag 'link' nelas.
        """
        pattern = re.compile(r"(https?://[^\s)]+)")
        pos = 0

        for m in pattern.finditer(text):
            # texto antes do link
            if m.start() > pos:
                self.desc.insert("end", text[pos:m.start()])

            url = m.group(1)
            self.desc.insert("end", url, ("link",))
            pos = m.end()

        # resto do texto depois do último link
        if pos < len(text):
            self.desc.insert("end", text[pos:])

    def _on_link_click(self, event):
        """Abre no navegador o link clicado dentro do Text."""
        index = self.desc.index("@%d,%d" % (event.x, event.y))
        # pega todos os ranges da tag 'link'
        ranges = list(self.desc.tag_ranges("link"))
        for i in range(0, len(ranges), 2):
            start = ranges[i]
            end = ranges[i + 1]
            if self.desc.compare(index, ">=", start) and self.desc.compare(index, "<", end):
                url = self.desc.get(start, end)
                webbrowser.open_new(url)
                break

    def _set_desc(self, description, allowed_list=None, var_name=None):
        """
        Atualiza a área de descrição com:
        - título "Descrição"
        - texto da descrição (com URLs clicáveis)
        - linha de valores permitidos
        - linha 'Variável: <nome>'
        - bloco de observação
        """
        self.desc.configure(state="normal")
        self.desc.delete("1.0", "end")

        self.desc.insert("1.0", "Descrição\n", "h1")
        self.desc.mark_set("insert", "end")
        # Insere texto da descrição com detecção de links
        self._insert_with_links(description)
        self.desc.insert("end", "\n\n")

        if allowed_list is not None:
            # Valores permitidos
            self.desc.insert("end", "Valores permitidos: ", "bold")
            self.desc.insert("end", ", ".join(allowed_list) + "\n\n", "mono")

            # Variável
            if var_name is not None:
                self.desc.insert("end", "Variável: ", "bold")
                self.desc.insert("end", var_name + " \n")

            # Espaço antes da observação
            self.desc.insert("end", "\n\nObservação:\n", "note")
            self.desc.insert("end", "{(vazio), 0} não serão salvos no config.txt.\n", "note")
            self.desc.insert("end", "A opção padrão será usada para variáveis não configuradas.", "note")

        self.desc.configure(state="disabled")

    def restore_default(self):
        k = self.current_focus_key
        if not k:
            return
        self.inputs[k].set(EMPTY_LABEL)
        self.current_values[k] = EMPTY_LABEL
        self._apply_cb_style(k)
        self._focus_row(k)

    def save_and_close(self):
        lines = []
        for key in options:
            self._validate_field(key)
            val = self.inputs[key].get().strip()
            lines.append((key, val))
        try:
            write_block_to_config(lines)
        except Exception as e:
            messagebox.showerror("Erro ao salvar", f"Falha ao escrever no arquivo:\n{CONFIG_FILE}\n\n{e}")
            return
        messagebox.showinfo("Sucesso", f"Configurações salvas em:\n{CONFIG_FILE}")
        self.destroy()

# ==============================
# Run
# ==============================
def main():
    app = ConfigApp()
    app.mainloop()

if __name__ == "__main__":
    main()

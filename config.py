# GUI de configuração para edenEquips

import os
import re
import tkinter as tk
from tkinter import ttk, messagebox

# ==============================
# Constantes
# ==============================
EMPTY_LABEL = "(vazio)"

LEFT_W  = 200   # largura mínima do painel de Variável/Valor
RIGHT_W = 300   # largura mínima do painel de descrição

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
# Opções e regras de validação
# ==============================
options = {
    "lvlQuest03": {
        "desc": "QUEST ARMA DO ÉDEN I - LVL [26-32] \n\nEscolha o level em que seu personagem vai começar a quest.\n26 = (padrão)",
        "default": "26",
        "allowed": {"26", "27", "28", "29", "30", "31", "32"}
    },
    "armaI": {
        "desc": "QUEST ARMA DO ÉDEN I - Armas para as classes:\nEspadachim, Noviço, Mercador.\n(https://browiki.org/wiki/Equipamentos_do_Éden#Armas) \n\nOpções: \n0 = Sabre / Cetro (padrão)\n1 = Espada / Maça",
        "default": "0",
        "allowed": {"0", "1"}
    },
    "lvlQuest05": {
        "desc": "QUEST ARMA DO ÉDEN II - LVL [40-49] \n\nEscolha o level em que seu personagem vai começar a quest.\n40 = (padrão)",
        "default": "40",
        "allowed": {"40", "41", "42", "43", "44", "45", "46", "47", "48", "49"}
    },
    "armaII": {
        "desc": "QUEST ARMA DO ÉDEN II - Armas para as classes: \nEspadachim, Cavaleiro, Templário, Noviço, Sacerdote, Monge, Mercador, Ferreiro, Alquimista, Espiritualista.\n(https://browiki.org/wiki/Equipamentos_do_Éden#Armas) \n\nOpções: \n0 = Sabre / Cetro / Adaga (padrão) \n1 = Espada / Maça / Cetro",
        "default": "0",
        "allowed": {"0", "1"}
    },
    "lvlQuest08": {
        "desc": "QUEST ARMA DO ÉDEN III - LVL [60-69] \n\nEscolha o level em que seu personagem vai começar a quest.\n60 = (padrão)",
        "default": "60",
        "allowed": {"60", "61", "62", "63", "64", "65", "66", "67", "68", "69"}
    },
    "armaIII": {
        "desc": "QUEST ARMA DO ÉDEN III - Armas para as classes: \nCavaleiro, Templário, Sacerdote, Monge, Sábio, Bardo, Odalisca, Ferreiro, Alquimista, Mercenário, Espiritualista, Ninja.\n(https://browiki.org/wiki/Equipamentos_do_Éden#Armas) \n\nOpções: \n0 = Espada / Cetro / Maça / Arco / Adaga (padrão) \n1 = Sabre / Maça / Dicionário / Soqueira / Violino / Chicote / Katar / Cetro / Humma \n2 = Lança / Dicionário / Machado",
        "default": "0",
        "allowed": {"0", "1", "2"}
    },
    "lvlQuest09": {
        "desc": "QUEST ENCANTAMENTO - LVL [70-79] \n\nEscolha o level em que seu personagem vai começar a quest.\n70 = (padrão)",
        "default": "70",
        "allowed": {"70", "71", "72", "73", "74", "75", "76", "77", "78", "79"}
    },
    "encant": {
        "desc": "QUEST ENCANTAMENTO +3% ATQ/ATQM\n\nOpções: \n0 = Ataque Físico (padrão) \n1 = Ataque Mágico",
        "default": "0",
        "allowed": {"0", "1"}
    },
    "lvlQuest10": {
        "desc": "QUEST ENCANTAMENTO COM CARTAS - LVL [80-89] \n\nEscolha o level em que seu personagem vai começar a quest.\n80 = (padrão)",
        "default": "80",
        "allowed": {"80", "81", "82", "83", "84", "85", "86", "87", "88", "89"}
    },
    "carta": {
        "desc": "QUEST ENCANTAMENTO COM CARTAS\n+20% DMG / +10% MDMG ou +3% HEAL \n\nOpções: \n0 = Bruto(Padrão) \n1 = Planta \n2 = Inseto \n3 = Peixe \n4 = Dragão \n5 = Cura",
        "default": "0",
        "allowed": {"0", "1", "2", "3", "4", "5"}
    },
    "lvlQuest11": {
        "desc": "QUEST ENCANTAMENTO COM CARTAS II - LVL [90-99] \n\nEscolha o level em que seu personagem vai começar a quest.\n90 = (padrão)",
        "default": "90",
        "allowed": {"90", "91", "92", "93", "94", "95", "96", "97", "98", "99"}
    },
    "semAsas": {
        "desc": "Desativar compra de Asas de Mosquito\n\nOpções:\n0 = Não (padrão) \n1 = Sim",
        "default": "0",
        "allowed": {"0", "1"}
    },
    "semPot": {
        "desc": "Desativar compra de Poções Laranjas\n\nOpções:\n0 = Não (padrão) \n1 = Sim",
        "default": "0",
        "allowed": {"0", "1"}
    }
}

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
    return [EMPTY_LABEL] + sorted(options[key]["allowed"])

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
        self.title("Configurador edenEquips")
        self.geometry("640x500")
        self.minsize(640, 480)

        self.current_values = load_existing_values()

        # widgets de entrada por chave
        self.inputs = {}
        self.current_focus_key = None

        self._build_widgets()
        self._populate_rows()

    # --------- UI
    def _build_widgets(self):
        # ===== Estilos / Tema
        style = ttk.Style(self)
        try:
            style.theme_use("clam")  # "clam" permite cores melhor que "vista"/"xpnative"
        except Exception:
            pass

        # Labels e títulos
        style.configure("Header.TLabel", font=("Segoe UI", 10, "bold"))
        style.configure("Title.TLabel",  font=("Segoe UI", 9,  "bold"))
        style.configure("Key.TLabel",    font=("Consolas", 9))  # monospace para variáveis

        # Combobox por estado (placeholder x normal)
        style.configure("Placeholder.TCombobox", foreground="#888")  # cinza quando (vazio)
        style.configure("Normal.TCombobox",      foreground="#111")

        # Botões (cores podem ser parcialmente ignoradas dependendo do SO/tema)
        style.configure("Danger.TButton", foreground="#fff", background="#d9534f")
        style.map("Danger.TButton", background=[("active","#c9302c")])

        # Fonte do dropdown do Combobox
        self.option_add("*TCombobox*Listbox.font", ("Segoe UI", 9))

        # Título
        lbl = ttk.Label(
            self,
            text="CONFIGURADOR — digite diretamente nos campos (use (vazio) para limpar)",
            anchor="w",
            style="Header.TLabel",
        )
        lbl.pack(fill="x", padx=10, pady=(10, 6))

        main = ttk.Frame(self)
        main.pack(fill="both", expand=True, padx=10, pady=6)

        # ===== Esquerda: Tabela simples (Label + Combobox editável) =====
        left = ttk.Frame(main)
        left.grid(row=0, column=0, sticky="nsew")
        left.grid_columnconfigure(0, weight=3, minsize=LEFT_W//2)
        left.grid_columnconfigure(1, weight=2, minsize=LEFT_W//2)

        # Cabeçalho
        ttk.Label(left, text="Variável", style="Title.TLabel").grid(row=0, column=0, sticky="w", padx=(0,6), pady=(0,6))
        ttk.Label(left, text="Valor",    style="Title.TLabel").grid(row=0, column=1, sticky="w", padx=(6,0), pady=(0,6))

        # ===== Direita: Descrição =====
        right = ttk.Frame(main, width=RIGHT_W)
        right.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        ttk.Label(right, text="Descrição da opção selecionada:", style="Title.TLabel").pack(anchor="w")
        self.desc = tk.Text(right, height=10, wrap="word")
        self.desc.configure(state="disabled")
        self.desc.pack(fill="both", expand=True, pady=(4, 0))

        # Tags de formatação na descrição
        self.desc.tag_configure("h1",   font=("Segoe UI", 10, "bold"))
        self.desc.tag_configure("bold", font=("Segoe UI", 9,  "bold"))
        self.desc.tag_configure("mono", font=("Consolas",  9))
        self.desc.tag_configure("note", foreground="#666")

        # Responsividade
        main.columnconfigure(0, weight=3, minsize=LEFT_W)
        main.columnconfigure(1, weight=2, minsize=RIGHT_W)
        main.rowconfigure(0, weight=1)

        # Botões
        btns = ttk.Frame(self)
        btns.pack(fill="x", padx=10, pady=10)
        ttk.Button(btns, text="Restaurar para (vazio)", command=self.restore_default).pack(side="left")
        ttk.Button(btns, text="Salvar e Fechar", command=self.save_and_close).pack(side="right")
        ttk.Button(btns, text="Cancelar", command=self.destroy).pack(side="right", padx=(0,8))

        self.left = left  # guarda para uso em _populate_rows

        # Atalhos (opcional)
        self.bind("<Control-s>", lambda e: self.save_and_close())
        self.bind("<Escape>",    lambda e: self.destroy())

    def _populate_rows(self):
        # remove widgets antigos (se houver)
        for child in self.left.grid_slaves():
            info = child.grid_info()
            if int(info.get("row", 0)) > 0:  # preserva cabeçalho (linha 0)
                child.destroy()

        self.inputs.clear()
        r = 1
        for key in options:
            # Label da variável (clicável para focar)
            lbl = ttk.Label(self.left, text=key, style="Key.TLabel")
            lbl.grid(row=r, column=0, sticky="w", padx=(0,6), pady=2)
            lbl.bind("<Button-1>", lambda e, k=key: self._focus_row(k))

            # Combobox editável com sugestões + (vazio)
            allowed = allowed_with_empty(key)
            cb = ttk.Combobox(self.left, values=allowed, state="normal", width=12)
            cur = self.current_values.get(key, EMPTY_LABEL)
            cb.set(cur if cur in allowed else EMPTY_LABEL)
            cb.grid(row=r, column=1, sticky="ew", padx=(6,0), pady=2)

            # aplica estilo conforme valor atual
            self.inputs[key] = cb
            self._apply_cb_style(key)

            # binds para seleção/validação/descrição
            cb.bind("<<ComboboxSelected>>", lambda e, k=key: self._on_value_change(k))
            cb.bind("<FocusIn>",           lambda e, k=key: self._focus_row(k))
            cb.bind("<FocusOut>",          lambda e, k=key: self._validate_field(k))
            cb.bind("<KeyRelease>",        lambda e, k=key: self._on_typing(k))  # atualiza cor ao digitar

            r += 1

        # inicia com a primeira opção selecionada na descrição
        first_key = next(iter(options))
        self._focus_row(first_key)

    # --------- Interações / Estilos dinâmicos
    def _apply_cb_style(self, key):
        """Troca estilo do Combobox para Placeholder/Normal conforme valor."""
        cb = self.inputs[key]
        val = cb.get().strip()
        if val == EMPTY_LABEL:
            cb.configure(style="Placeholder.TCombobox")
        else:
            cb.configure(style="Normal.TCombobox")

    def _on_typing(self, key):
        """Enquanto digita, já alterna a cor (placeholder x normal)."""
        self._apply_cb_style(key)

    def _focus_row(self, key):
        """Atualiza descrição e marca o 'selecionado' para o botão Restaurar."""
        self.current_focus_key = key
        text = options[key]["desc"]
        self._set_desc(text, allowed_with_empty(key))

    def _on_value_change(self, key):
        """Ao escolher na lista, valida e atualiza descrição/estilo."""
        self._validate_field(key)
        self._focus_row(key)
        self._apply_cb_style(key)

    def _validate_field(self, key):
        """Garante que o valor esteja entre os permitidos (ou (vazio))."""
        cb = self.inputs[key]
        val = cb.get().strip()
        allowed = set(allowed_with_empty(key))
        if val not in allowed:
            messagebox.showerror(
                "Valor inválido",
                f"Valor '{val}' não é permitido para '{key}'.\nPermitidos: {sorted(allowed)}"
            )
            # Reverte para (vazio)
            cb.set(EMPTY_LABEL)
            val = EMPTY_LABEL
        # atualiza cache atual e estilo
        self.current_values[key] = val
        self._apply_cb_style(key)

    def _set_desc(self, description, allowed_list=None):
        """Escreve descrição formatada com tags (negrito, monoespaço, nota)."""
        self.desc.configure(state="normal")
        self.desc.delete("1.0", "end")

        # título
        self.desc.insert("1.0", "Descrição\n", "h1")
        # corpo
        self.desc.insert("end", description + "\n\n")

        if allowed_list is not None:
            self.desc.insert("end", "Valores permitidos: ", "bold")
            self.desc.insert("end", ", ".join(allowed_list) + "\n", "mono")
            self.desc.insert("end", "\n\n\nObservação:\n{(vazio), 0} não serão salvos no config.txt.", "note")
            self.desc.insert("end", "\nA opção padrão será usada para variáveis não configuradas.", "note")

        self.desc.configure(state="disabled")

    def restore_default(self):
        """Limpa o campo focado para (vazio)."""
        k = self.current_focus_key
        if not k:
            return
        self.inputs[k].set(EMPTY_LABEL)
        self.current_values[k] = EMPTY_LABEL
        self._apply_cb_style(k)
        self._focus_row(k)

    def save_and_close(self):
        """Coleta valores, valida, salva bloco e fecha."""
        lines = []
        # valida todos antes de salvar
        for key in options:
            self._validate_field(key)
            val = self.inputs[key].get().strip()
            # coleta para write_block_to_config (ele descarta (vazio) e 0)
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

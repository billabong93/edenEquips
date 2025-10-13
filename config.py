import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OPENKORE_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))
CONTROL_DIR = os.path.join(OPENKORE_DIR, "control")
CONFIG_FILE = os.path.join(CONTROL_DIR, "config.txt")

if not os.path.isdir(CONTROL_DIR):
    os.makedirs(CONTROL_DIR)

options = {
    "eq03": {
        "desc": "QUEST ARMA DO ÉDEN I (Espadachim, Noviço, Mercador)\nOpções: 0 = Sabre/Cetro (padrão), 1 = Espada/Maça",
        "prompt": "Escolha a Arma do Éden I (0/1) [0]: ",
        "default": "0"
    },
    "eq05": {
        "desc": "QUEST ARMA DO ÉDEN II (Espadachim, Cavaleiro, Templário, Noviço, Sacerdote, Monge, Mercador, Ferreiro, Alquimista, Espiritualista)\nOpções: 0 = Sabre/Cetro/Adaga, 1 = Espada/Maça/Cetro",
        "prompt": "Escolha a Arma do Éden II (0/1) [0]: ",
        "default": "0"
    },
    "eq08": {
        "desc": "QUEST ARMA DO ÉDEN III (Cavaleiro, Templário, Sacerdote, Monge, Sábio, Bardo, Odalisca, Ferreiro, Alquimista, Mercenário, Espiritualista, Ninja)\nOpções: 0 = Espada/Cetro/Maça/Arco/Adaga (padrão), 1 = Sabre/Maça/Dicionário/Soqueira/Violino/Chicote/Katar/Cetro/Humma, 2 = Lança/Dicionário/Machado",
        "prompt": "Escolha a Arma do Éden III (0/1/2) [0]: ",
        "default": "0"
    },
    "enc": {
        "desc": "QUEST ENCANTAMENTO +3% ATQ/ATQM\nOpções: 0 = Ataque Físico (padrão), 1 = Ataque Mágico",
        "prompt": "Deseja encantar com Ataque Mágico? (0/1) [0]: ",
        "default": "0"
    },
    "carta": {
        "desc": "QUEST ENCANTAMENTO COM CARTAS\n+20% DMG / +10% MDMG ou +3% HEAL: 0 = Bruto(Padrão), 1 = Planta, 2 = Inseto, 3 = Peixe, 4 = Dragão, 5 = Cura",
        "prompt": "Escolha a opção desejada (0-5) [0]: ",
        "default": "0"
    },
        "semAsas": {
        "desc": "Desativar compra de Asas de Mosquito",
        "prompt": "Deseja desativar Asas de Mosquito? (0 = Não, 1 = Sim) [0]: ",
        "default": "0"
    },
    "semPot": {
        "desc": "Desativar compra de Poções Laranjas",
        "prompt": "Deseja desativar Poções Laranja? (0 = Não, 1 = Sim) [0]: ",
        "default": "0"
    }
}

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    banner = r"""
@@@@@@@@@@@@@@@@@@@@@@@@%-+=+@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@#-@#-@@@@@@@@@@@@@@@@@@@@@
@@@@@@@billabong93@@@@@@#-@%-@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@#:@%:@@@@@@@@@@@@@@@@@@@@@
@****%@@@@@@@@@@@@@@@@@%:=%#-:%@@@@@@@@@@@@@@@@@@@
-**+#-#@@@@@@@@@@@@@@@@@*:  .+@@@@@@@@@@@@@@@@@@@@
:*-+-#-@@@@@@@@@@@@@@@@@=    .#@@@@@@@@@@@@@@@@@@@
@#%@=+*-#%@@@@@@@@@@@@@*  ... .*@@@@@@@@@@@@@@@@@@
@@@@*-@#+++++++**##%@@#....... .*@@@@@@@@@@@@@@@@@
@@@@@*-#:+*++++======+- .  #  .. +@@@@@@@@@@@@@@@@
@@@@@@+=*=@@@@@%%##*+:...  #  .. .=+++**##%%@@@*+#
@@@@@@@-*=*@@@@@@@@@+  .... ...   :-=+========+==-
@@@@@@@%:#-%@@@@@@@*     .:..-:     :%@%%##**+=+#:
@@@@@@@@*=*-@@@@@@#.     #=--=#      :%@@@@@@@@-+-
@@@@@@@@@+==@@@@@@:      .    .       =@@@@@@@@@#%
@@@@@@@@@@@@@@@@@@=:::.:=:--=--+-.=++*%@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@#-*-#@@@@#==+=*@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@#-*-%@@@@@@#==+=*#**%@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@+-+#-%@@@@@@@#=++++:#@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@+==+=%@@@@@@@@@*=++%@@@@@@@@@
"""
    print(banner)
    print("\n============================================================")
    print("CONFIGURADOR DE EVENTMACRO - ÉDEN & ENCANTAMENTOS")
    print("============================================================\n")
    print("As opções padrão (0) serão ignoradas e não salvas.\n")

    config_to_save = []

    for key, info in options.items():
        print("------------------------------------------------------------")
        print(info["desc"])
        while True:
            choice = input(info["prompt"]).strip()
            if choice == "":
                choice = info["default"]
            if key == "carta":
                if choice in ["0","1","2","3","4","5"]:
                    break
            elif key == "eq08":
                if choice in ["0","1","2"]:
                    break
            else:
                if choice in ["0","1"]:
                    break
            print("Opção inválida. Tente novamente.")

        if choice != "0":
            config_to_save.append(f"{key} {choice}")

    if config_to_save:
        with open(CONFIG_FILE, "a", encoding="utf-8") as f:
            f.write("\n# --- Configurações do edenEquips ---\n")
            for line in config_to_save:
                f.write(line + "\n")
        print(f"\nConfigurações salvas em {CONFIG_FILE}")
    else:
        print("\nNenhuma configuração alterada. Nenhum dado foi salvo.")

if __name__ == "__main__":
    main()

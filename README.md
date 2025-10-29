## 🛡️ edenEquips v1.2 (LATAM)
[<img alt="Static Badge" target="_blank" src="https://img.shields.io/badge/Discord-.boscv-%237289DA?logo=discord&logoColor=%23fff">](https://discord.com/users/boscv.)\
[<img alt="Static Badge" src="https://img.shields.io/badge/Discord-Openkore%20LATAM-%237289DA?logo=discord&logoColor=%23fff">](https://discord.com/channels/1396892709775605922)\
[<img alt="Static Badge" src="https://img.shields.io/badge/F%C3%B3rum-Openkore%20LATAM-%23ec8736?logo=phpBB&logoColor=%23fff">](https://openkore.com.br/)

Plugin de injeção de eventMacros para Quests e Equipamentos do Éden - Openkore (Servidor Latam)\
HWID necessário para ativação.

---

## 📜 Quests Incluídas (Todas as classes)

  - **Resgate de equipamentos do Éden** na Academia Criatura na primeira mudança de classe (pós nível de base 7).
  - **Quests de equipamentos** dos níveis 26, 40 e 60.
  - **Quests de encantamento** e cartas dos níveis 70, 80 e 90.

---

## 🤖 Funções Principais:

  - **Configuração personalizada** de equipamentos, encantamentos e cartas.
  - **Escolha o nível** em que quer que o personagem inicie as quests.
  - **Equipa automáticamente** itens recebidos após as quests.
  - **Teleport avançado** (*routeTeleport* e *teleportAuto_search*) para maior eficiência e sobrevivência.
  - **Teleport away** se mob se aproximar do bot sentado durante o *teleportAuto_search*.
  - **Compra automática** e uso de Asas de Mosquito e Poções Laranjas. (Possível desativar)
  - **Salva na Kafra** mais próxima da quest, para retorno mais rápido em caso de morte ou compra.
  - **Retorno seguro** ao local original do bot, restaurando configurações.
  - **Failsafes** para concluir quests mesmo com reload, operação manual ou fechamento do programa.
  - **Compatível com profiles**, pra você que gosta de manter as coisas organizadas.

---

## ⚙️ Requisitos:

  - Python
  - [Automacro aeroplano](https://openkore.com.br/viewtopic.php?p=6470) *ra_fild12*.
  - Se não existir, criar um arquivo **eventMacros.txt** na pasta **./control.**
  - Pasta [**./fields** e **portals.txt**](https://github.com/dhmello/openkore_latam) atualizados.

---

## 📝 Instruções:

  - Use **config.py** para configurar suas opções de equipamentos, encantamentos e cartas. Se não houver escolha de equipamentos disponível para sua classe, escolha [0]. As opções escolhidas são salvas no final do **config.txt**. As opções por padrão são [0]. No caso de [0], não é criada uma variável.
    Você também pode inserir as variáveis manualmente no **config.txt** ou usar o comando *'conf -f'* no console do openkore, ex *'conf -f semPot 1'*.
    As variáveis criadas são lidas pelo plugin durante a execução.
  - Adicione *edenEquips* em **sys.txt** no final da linha *loadPlugins_list*.
  - Em caso de necessidade de reinjeção, use *'plugin reload edenEquips'* no console.

---

## 🛠️ Configurações necessárias para boa execução do plugin:

* **config.txt**:
  - *storageAuto_npc* com coordenadas configuradas.
  - *route_maxWarpFee* vazio ou com valor acima de 20000.

* **routeweights.txt**:
  - *AIRSHIP* 500
  - *moc_fild20* 10000

---

## ⚠️ O que não fazer:

  - *'reload eventMacros'* durante a execução do plugin.
  - **Jamais apague as variáveis** criadas pelo/para o plugin em **config.txt**, salvo necessidade
    de rollback por falha na execução de etapas do macro, ou a remoção do plugin.
  - **Não faça alterações** no **proxy.py** ou **edenEquips.pl**. O acesso é barrado pelo servidor
    em caso de qualquer modificação ou ausência dos arquivos.

---

## 📢 Informações e avisos:

  - O primeiro resgate de equipamentos só é feito no nível 7 porque esse é o nível mínimo do equipamento, evitando redundâncias.
  - No caso das classes principais, a quest de nível 60 só é feita após mudança para  2ª classe. A quest até pode ser feita pelas 1ªs classes principais, mas não receberão equipamentos após a conclusão até a mudança para 2ª classe.
  - A maior parte das classes foi testada, e as armas estão em sua maioria, se não todas,
    nas posições corretas. (Opções extraídas de .csv)
  - Telesearch é fundamental para a conclusão dessas quests, não é possível desativá-lo.
  - Se seu bot não está pegando o aeroplano ou usando os teleportes, verifique routeweights.txt,
    e *route_maxWarpFee* em config.txt.
  - As Asas de Mosquito só devem ser desabilitadas se houver algum outro item equivalente
    em *teleportAuto_item1*.
  - Apesar de interceptado, o bot continuará usando qualquer skill ou item configurado no
    seu **config.txt**, **macros.txt** e **eventMacros.txt**.
  - O plugin depende do seu *storageAuto_npc* configurado, para conseguir devolver o bot para o
    lugar original.
  - A injeção não sobrescreverá seu **eventMacros.txt**. De qualquer forma, sempre bom manter um backup.
  - O plugin não é configurado pra comprar ou fazer uso de pots de sp. Mas pegará do armazém ou
    comprará mais antes de começar qualquer quest, e usará, se seu bot estiver configurado para isso.
  - O eventMacros injetado está sempre atualizado.

---

## 🗃️ Estrutura da pasta:

- openkore-master/
  * 📁 control/
    * 📄 eventMacros.txt
  * 📁 fields/
  * 📁 plugins/
    * 📁 edenEquips/
      * 📄 README.md
      * 📄 config.py
      * 📄 edenEquips.pl
      * 📄 proxy.py
  * 📁 tables/
    * 📁 ROla/
      * 📄 portals.txt

---

## 💾 Variáveis de configurações e suas funções: (Inseridas em config.txt)

* ⚡ Nível de inicio das quests:

  - *lvlQuest03* (26 ~ 32) - Determina o nível em que o personagem irá começar a Quest de nível 26.
  - *lvlQuest05* (40 ~ 49) - Determina o nível em que o personagem irá começar a Quest de nível 40.
  - *lvlQuest08* (60 ~ 69) - Determina o nível em que o personagem irá começar a Quest de nível 60.
  - *lvlQuest09* (70 ~ 79) - Determina o nível em que o personagem irá começar a Quest de nível 70.
  - *lvlQuest10* (80 ~ 89) - Determina o nível em que o personagem irá começar a Quest de nível 80.
  - *lvlQuest11* (90 ~ 99) - Determina o nível em que o personagem irá começar a Quest de nível 90.

* ⚔️ Equipamentos:

  - *armaI* (0, 1) - Determina a opção de equipamentos da Quest nível 26.
    Opções para: Espadachim, Noviço e Mercador.
  - *armaII* (0, 1) - Determina a opção de equipamentos da Quest nível 40.
    Opções para: Espadachim, Cavaleiro, Templário, Noviço, Sacerdote, Monge, Mercador,
    Ferreiro, Alquimista e Espiritualista.
  - *armaIII* (0, 1, 2) - Determina a opção de equipamentos da Quest nível 60.
    Opções para: Cavaleiro, Templário, Sacerdote, Monge, Sábio, Bardo, 
    Odalisca, Ferreiro, Alquimista, Mercenário, Espiritualista e Ninja.

* 💎 Encantamentos:

  - *encant* (0, 1) - Determina se o encantamento de nível 70 vai ser ATQ ou ATQM.
  - *carta* (0, 1, 2, 3, 4, 5) - Tipo de carta +DMG/MDMG ou fator de cura no encantamento nível 80.

* 🧪 Utilizáveis:

  - *semAsas* (0, 1) - Desabilita a compra de Asas de Mosquito.
  - *semPots* (0, 1) - Desabilita a compra de Poções Laranjas.

* 📈 Fases de Quest: (Determinam a fase da quest em que o bot se encontra)
(Jamais mexa se não houver necessidade, pode gerar conflitos e prejudicar a restauração ao ponto original)

  - *eden03* (0, 1, 2, 3, end)	- Variável inexistente = Iniciar a quest no npc.
  - *eden05* (0, 1, 2, 3, end)	- 0 = Salvar na kafra da quest.
  - *eden08* (0, 1, 2, 3, end)	- 1 = Checar e comprar mantimentos.
  - *eden09* (0, 1, 2, 3, end)	- 2 = Execução da Quest.
  - *eden10* (0, 1, 2, 3, end)	- 3 = Resgate de equipamentos.
  - *eden11* (0, 1, 2, 3, end)	- end = Conclusão.

---

## 🚀 Implementações futuras

* Quests do Éden faltantes, com opções para preferência do usuário.
* Quests diárias e equipamentos 100+.

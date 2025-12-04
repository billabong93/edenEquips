## ⚜️ edenEquips v2.0 (LATAM)
[<img alt="Static Badge" target="_blank" src="https://img.shields.io/badge/Discord-.boscv-%237289DA?logo=discord&logoColor=%23fff">](https://discord.com/users/boscv.)\
[<img alt="Static Badge" src="https://img.shields.io/badge/Discord-Openkore%20LATAM-%237289DA?logo=discord&logoColor=%23fff">](https://discord.com/channels/1396892709775605922)\
[<img alt="Static Badge" src="https://img.shields.io/badge/F%C3%B3rum-Openkore%20LATAM-%23ec8736?logo=phpBB&logoColor=%23fff">](https://openkore.com.br/)

Plugin de injeção de eventMacros para Quests e Equipamentos do Éden - Openkore (Servidor Latam)\
HWID necessário para ativação.

---

## 📜 Quests Incluídas (Todas as classes)

  - **Resgate de equipamentos** dos níveis 7 ao 160.
  - **Quests da Instrutora Boya** dos níveis 26, 33, 40 e 75.
  - **Quests do Instrutor Ur** dos níveis 60, 70, 80 e 90.
  - **Quests do Éden** dos níveis 100, 110.
  - **Quests Primeiros Passos** para Aprendiz.
  - **Quests Tutoriais** para Aprendiz (Apenas as que dão consumíveis).

---

## 🤖 Funções Principais:

  - **Configuração personalizada** de equipamentos, encantamentos e cartas.
  - **Escolha o nível** em que quer que o personagem inicie as quests (26-90).
  - **Equipa automáticamente** itens recebidos após as quests.
  - **Teleport Search** (*routeTeleport* e *teleportAuto_search*) para maior eficiência e sobrevivência.
  - **Compra automática** e uso de Asas de Mosquito e Poções Laranjas. (26-90) (Possível desativar)
  - **Salva na Kafra** mais próxima da quest, para retorno mais rápido em caso de morte ou compra.
  - **Retorno seguro** ao local original do bot, restaurando configurações.
  - **Failsafes** para concluir quests mesmo com reload, operação manual ou fechamento do programa.
  - **Compatível com profiles** pra você que gosta de manter as coisas organizadas.

---

## ⚙️ Requisitos:

  - Python
  - [Automacro aeroplano](https://openkore.com.br/viewtopic.php?p=6470) *ra_fild12*.
  - [Plugin eventMacros](https://github.com/dhmello/openkore_latam) atualizado. 
  - Se não existir, criar um arquivo **eventMacros.txt** na pasta **./control.**
  - Pasta [./fields e portals.txt](https://github.com/dhmello/openkore_latam) atualizados.

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

  - *'reload eventMacros'*, *'reload all'* durante a execução do plugin.
  - **Jamais apague as variáveis** criadas pelo/para o plugin em **config.txt**, salvo necessidade
    de rollback por falha na execução de etapas do macro, ou a remoção do plugin.
  - **Não faça alterações** no **proxy.py** ou **edenEquips.pl**. O acesso é barrado pelo servidor
    em caso de qualquer modificação ou ausência dos arquivos.

---

## 📢 Informações e avisos:

  - O eventMacros injetado é atualizado diariamente, qualquer bug ou erro, favor informar.
  - O primeiro resgate de equipamentos só é feito no nível 7 porque esse é o nível mínimo do equipamento, evitando redundâncias.
  - No caso das classes principais, a quest de nível 60 só é feita após mudança para  2ª classe. A quest até pode ser feita pelas 1ªs classes principais, mas não receberão equipamentos após a conclusão até a mudança para 2ª classe.
  - A maior parte das classes foi testada, e as armas estão em sua maioria, se não todas,
    nas posições corretas. (Opções extraídas de .csv)
  - Telesearch é fundamental para a conclusão dessas quests, não é possível desativá-lo.
  - Se seu bot não está pegando o aeroplano ou usando os teleportes, verifique routeweights.txt,
    e *route_maxWarpFee* em **config.txt**.
  - As Asas de Mosquito só devem ser desabilitadas se houver algum outro item equivalente
    em *teleportAuto_item1*.
  - Apesar de interceptado, o bot continuará usando qualquer skill ou item configurado no
    seu **config.txt**, **macros.txt** e **eventMacros.txt**.
  - O plugin depende do seu *storageAuto_npc* configurado, para conseguir devolver o bot para o
    lugar original.
  - A injeção não sobrescreverá seu **eventMacros.txt**. De qualquer forma, sempre bom manter um backup.
  - O plugin não é configurado pra comprar ou fazer uso de pots de sp. Mas pegará do armazém ou
    comprará mais antes de começar qualquer quest, e usará, se seu bot estiver configurado para isso.
  - O **config.py** salva as configurações apenas em **control/config.txt**.

---

## 🗃️ Estrutura da pasta:

- openkore-master/
  * 📁 control/
    * 📄 eventMacros.txt
    * 📄 sys.txt
  * 📁 fields/
  * 📁 plugins/
    * 📁 edenEquips/
      * 📄 README.md
      * 📄 atualizador-edenEquips.bat
      * 📄 atualizador-edenEquips.ps1
      * 📄 config.py
      * 📄 edenEquips.pl
      * 📄 proxy.py
  * 📁 tables/
    * 📁 ROla/
      * 📄 portals.txt

---

## 💾 Variáveis de configurações e suas funções: (Inseridas em config.txt)

### 🌱 Nível de início das Quests

| Variável  | Valores | Informação |
| ------------- | ------------- | ------------- |
| **`lvlQuest03`** | `26 ~ 32`, `off` | Nível em que o personagem irá começar a Quest da **Instrutora Boya** de **nível 26**. `off` = desativa essa quest. |
| **`lvlQuest04`** | `33 ~ 39`, `off` | Nível em que o personagem irá começar a Quest da **Instrutora Boya** de **nível 33**. `off` = desativa essa quest. |
| **`lvlQuest05`** | `40 ~ 49`, `off` | Nível em que o personagem irá começar a Quest da **Instrutora Boya** de **nível 40**. `off` = desativa essa quest. |
| **`lvlQuest07`** | `75 ~ 99`, `off` | Nível em que o personagem irá começar a Quest da **Instrutora Boya** de **nível 75**. `off` = desativa essa quest. |
| **`lvlQuest08`** | `60 ~ 69`, `off` | Nível em que o personagem irá começar a Quest do **Instrutor Ur** de **nível 60**. `off` = desativa essa quest. |
| **`lvlQuest09`** | `70 ~ 79`, `off` | Nível em que o personagem irá começar a Quest do **Instrutor Ur** de **nível 70**. `off` = desativa essa quest. |
| **`lvlQuest10`** | `80 ~ 89`, `off` | Nível em que o personagem irá começar a Quest do **Instrutor Ur** de **nível 80**. `off` = desativa essa quest. |
| **`lvlQuest11`** | `90 ~ 99`, `off` | Nível em que o personagem irá começar a Quest do **Instrutor Ur** de **nível 90**. `off` = desativa essa quest. |
> `off` faz o plugin **ignorar completamente** a quest daquela faixa de nível, mesmo que o personagem esteja dentro do range.

---

### ⚔️ Equipamentos (Boya / Ur 26–90)

| Variável  | Valores | Informação |
| ------------- | ------------- | ------------- |
| **`armaI`** | `0 ~ 1` | Determina a opção de **arma/equipamento** da Quest de **nível 26** (Instrutora Boya). |
| **`armaII`** | `0 ~ 1` | Determina a opção de **arma/equipamento** da Quest de **nível 40** (Instrutora Boya). |
| **`armaIII`** | `0 ~ 2` | Determina a opção de **arma/equipamento** da Quest de **nível 60** (Instrutor Ur). |
> `encant` - `0` = Padrão | `1` = Opção 1 | `2` = Opção 2

---

### 💎 Encantamentos e Cartas (Ur 70–90)

| Variável  | Valores | Informação |
| ------------- | ------------- | ------------- |
| **`encant`** | `0 ~ 1` | Tipo de **encantamento** recebido após a Quest de **nível 70** (`0` = ATQ físico, `1` = ATQM). |
| **`carta`** | `0 ~ 5` | Tipo de **carta** recebida após as Quests de **nível 80** e **90** (slot de cartas das armas). |
> `encant` - `0` = Desativado | `1` = Ativado 

> `carta` - `0` = Bruto (padrão) | `1` = Planta | `2` = Inseto | `3` = Peixe | `4` = Dragão | `5` = Cura"

---

### 🧪 Consumíveis

| Variável  | Valores | Informação |
| ------------- | ------------- | ------------- |
| **`semAsas`** | `0 ~ 1` | Desabilita a compra de **Asas de Mosquito** |
| **`semPot`** | `0 ~ 1` | Desabilita a compra de **Poções Laranjas** |
> `0` = Desativado | `1` = Ativado 

---

### 📈 Fases de Quest
*(Determinadas pelo plugin — não recomendado editar manualmente.)* 
> **Jamais mexa** nessas variáveis se não houver necessidade de rollback/debug. Elas controlam em que etapa da macro o bot se encontra.

#### 26-90

| Variável  | Valores | Informação |
| ------------- | ------------- | ------------- |
| **`eden03`** | `0 ~ 5` | `0` = Salvar na Kafra da Quest. |
| **`eden04`** | `0 ~ 5` | `1` = Checar e comprar mantimentos. |
| **`eden05`** | `0 ~ 5` | `2` = Execução da Quest. |
| **`eden07`** | `0 ~ 5` | `3` = Resgate de equipamentos. |
| **`eden08`** | `0 ~ 5` | `4` = Restaurar configurações. |
| **`eden09`** | `0 ~ 5` | `5` = Fim da Quest. |
| **`eden10`** | `0 ~ 5` | Reservado para futuras expansões. |
| **`eden11`** | `0 ~ 5` | Reservado para futuras expansões. |

#### 100+ 
| Variável | Valores | Informação |
| ------------- | ------------- | ------------- |
| **`magma100_0`** | `0 ~ 4` | `0` = Quest desativada. |
| **`tha110_2`** | `0 ~ 4` | `1` = Quest ativada. |
| **`gl100_1`** | `0 ~ 4` | `2` = Quest em espera diária. |
| **`gl110_6`** | `0 ~ 4` | `3` = Quest em execução. |
| **`gl110_8`** | `0 ~ 4` | `4` = Quest concluída. |

---

### ⚡ Quests do Éden [100–110]

Todas as variáveis abaixo usam `0` = **Desativado** (padrão) e `1` = **Ativado**.

#### Ativação geral

| Variável  | Valores | Informação |
| --------- | ------- | ---------- |
| **`quests100_110`** | `0 ~ 1` | Ativa/desativa globalmente as **Quests do Éden 100–110**. |
> As variáveis abaixo ativam/desativam cada quest individualmente.

#### Caverna de Magma [100]

| Variável  | Valores | Informação |
| --------- | ------- | ---------- |
| **`magma100_0`** | `0 ~ 1` | Quest contra **Pesadelo Sombrio** na **Caverna de Magma** [100]. |
| **`magma100_1`** | `0 ~ 1` | Quest contra **Deletério / Exterminador** na **Caverna de Magma** [100]. |
| **`magma100_2`** | `0 ~ 1` | Quest de coleta de **Pedra Pome** na **Caverna de Magma** [100]. |

#### Glast Heim [100-110]

| Variável  | Valores | Informação |
| --------- | ------- | ---------- |
| **`gl100_0`** | `0 ~ 1` | Quest contra **Carat** em **Glast Heim** [100]. |
| **`gl100_1`** | `0 ~ 1` | Quest contra **Arclouse** em **Glast Heim** [100]. |
| **`gl100_2`** | `0 ~ 1` | Quest contra **Anolian** em **Glast Heim** [100]. |
| **`gl100_3`** | `0 ~ 1` | Quest contra **Sting** em **Glast Heim** [100]. |
| **`gl100_4`** | `0 ~ 1` | Quest contra **Majoruros** em **Glast Heim** [100]. |
| **`gl110_5`** | `0 ~ 1` | Quest contra **Raydric** em **Glast Heim** [110]. |
| **`gl110_6`** | `0 ~ 1` | Quest contra **Khalitzburg** em **Glast Heim** [110]. |
| **`gl110_7`** | `0 ~ 1` | Quest contra **Andarilho** em **Glast Heim** [110]. |
| **`gl110_8`** | `0 ~ 1` | Quest contra **Cavaleiro do Abismo** em **Glast Heim** [110]. |

#### Ash Vacuum [100-110]

| Variável  | Valores | Informação |
| --------- | ------- | ---------- |
| **`ash100_0`** | `0 ~ 1` | Quest contra **Pinguicula** em **Ash Vacuum** [100]. |
| **`ash100_1`** | `0 ~ 1` | Quest contra **Vespa Vagalume** em **Ash Vacuum** [100]. |
| **`ash100_2`** | `0 ~ 1` | Quest contra **Leão de Vinhas** em **Ash Vacuum** [100]. |
| **`ash110_3`** | `0 ~ 1` | Quest contra **Pinguicula Sombria** em **Ash Vacuum** [110]. |
| **`ash110_4`** | `0 ~ 1` | Quest contra **Nepenthes** em **Ash Vacuum** [110]. |
| **`ash110_5`** | `0 ~ 1` | Quest contra **Naga** em **Ash Vacuum** [110]. |
| **`ash110_6`** | `0 ~ 1` | Quest contra **Cornus** em **Ash Vacuum** [110]. |
| **`ash110_7`** | `0 ~ 1` | Quest contra **Larva Centopeia** em **Ash Vacuum** [110]. |
| **`ash110_8`** | `0 ~ 1` | Quest contra **Chifre Místico** em **Ash Vacuum** [110]. |

#### Arunafeltz [100]

| Variável  | Valores | Informação |
| --------- | ------- | ---------- |
| **`aruna100_0`** | `0 ~ 1` | Quest contra **Kobold (Machado/Martelo/Maça)** em mapas de **Arunafeltz** [100]. |
| **`aruna100_1`** | `0 ~ 1` | Quest contra **Vento da Colina**. |
| **`aruna100_2`** | `0 ~ 1` | Quest contra **Lobo do Deserto**. |
| **`aruna100_3`** | `0 ~ 1` | Quest contra **Cabelo Azul**. |
| **`aruna100_4`** | `0 ~ 1` | Quest contra **Drosera / Muscipular**. |
| **`aruna100_5`** | `0 ~ 1` | Quest contra **Magmaring**. |
| **`aruna100_6`** | `0 ~ 1` | Quest contra **Coração Glacial**. |
| **`aruna100_7`** | `0 ~ 1` | Quest contra **Yeti**. |
| **`aruna100_8`** | `0 ~ 1` | Quest contra **Titã de Gelo / Gazeti**. |

#### Torre de Thanatos [110]

| Variável  | Valores | Informação |
| --------- | ------- | ---------- |
| **`thana110_0`** | `0 ~ 1` | Quest contra **Mímico Antigo** na **Torre de Thanatos** [110]. |
| **`thana110_1`** | `0 ~ 1` | Quest contra **Palavra Morta**. |
| **`thana110_2`** | `0 ~ 1` | Quest contra **Barão Coruja**. |
| **`thana110_3`** | `0 ~ 1` | Quest contra **Página Sangrenta**. |
| **`thana110_4`** | `0 ~ 1` | Quest contra **Pergaminho Antigo**. |
| **`thana110_5`** | `0 ~ 1` | Quest contra **Farrapos**. |

#### Ruínas de Juperos [110]

| Variável  | Valores | Informação |
| --------- | ------- | ---------- |
| **`jupe110_0`** | `0 ~ 1` | Quest contra **Venatu (Laranja/Azul)** em **Ruínas de Juperos** [110]. |
| **`jupe110_1`** | `0 ~ 1` | Quest contra **Venatu (Roxo/Verde)**. |
| **`jupe110_2`** | `0 ~ 1` | Quest contra **Dimik (Verde/Azul)**. |
| **`jupe110_3`** | `0 ~ 1` | Quest contra **Dimik (Vermelho/Laranja)**. |

---

### 🧥 Equipamentos Éden [100+]

#### Tipo de acessórios

| Variável  | Valores | Informação |
| --------- | ------- | ---------- |
| **`tipoAcc`** | `0 ~ 3` | Define o tipo de acessório que será resgatado. |
> `0` = Forte (STR)(padrão) | `1` = Mágico (INT) | `2` = Ágil (DEX) | `3` = Vital (VIT)

#### Equipamentos [100]

| Variável  | Valores | Informação |
| --------- | ------- | ---------- |
| **`equips100`** | `0 ~ 1` | Ativa/desativa as trocas de moedas por **equipamentos do Éden nível 100**. |
| **`anelI`** | `0 ~ 5` | Prioridade para resgatar **Anel do Éden I** |
| **`colarI`** | `0 ~ 5` | Prioridade para resgatar **Colar do Éden I**. |
| **`fardaI`** | `0 ~ 5` | Prioridade para resgatar **Farda do Éden I**. |
| **`coturI`** | `0 ~ 5` | Prioridade para resgatar **Coturno do Éden I**. |
| **`mantoI`** | `0 ~ 5` | Prioridade para resgatar **Manto do Éden I**. |
| **`boinaI`** | `0 ~ 1` | Ativa/desativa a troca pela **Boina do Éden I** |
> `0` = Desativado | `1` = Ativado | `1 ~ 5` = Maior-menor prioridade

#### Equipamentos [115]

| Variável  | Valores | Informação |
| --------- | ------- | ---------- |
| **`equips115`** | `0 ~ 1` | Ativa/desativa as trocas de moedas por **equipamentos do Éden nível 115**. |
| **`anelII`** | `0 ~ 5` | Prioridade para resgatar **Anel do Éden II**. |
| **`colarII`** | `0 ~ 5` | Prioridade para resgatar **Colar do Éden II**. |
| **`fardaII`** | `0 ~ 5` | Prioridade para resgatar **Farda do Éden II**. |
| **`coturII`** | `0 ~ 5` | Prioridade para resgatar **Coturno do Éden II**. |
> `0` = desativado | `1` = ativado | `1 ~ 5` = maior-menor prioridade

#### Equipamentos [130]

| Variável  | Valores | Informação |
| --------- | ------- | ---------- |
| **`equips130`** | `0 ~ 1` | Ativa/desativa as trocas de moedas por **equipamentos do Éden nível 130**. |
| **`anelIII`** | `0 ~ 5` | Prioridade para resgatar **Anel do Éden III**. |
| **`colarIII`** | `0 ~ 5` | Prioridade para resgatar **Colar do Éden III**. |
| **`fardaIII`** | `0 ~ 5` | Prioridade para resgatar **Farda do Éden III**. |
| **`coturIII`** | `0 ~ 5` | Prioridade para resgatar **Coturno do Éden III**. |
| **`mantoII`** | `0 ~ 5` | Prioridade para resgatar **Manto do Éden III**. |
> `0` = Desativado | `1` = Ativado | `1 ~ 5` = Maior-menor prioridade

#### Equipamentos [145]

| Variável  | Valores | Informação |
| --------- | ------- | ---------- |
| **`equips145`** | `0 ~ 1` | Ativa/desativa as trocas de moedas por **equipamentos do Éden nível 145**. |
| **`anelIV`** | `0 ~ 5` | Prioridade para resgatar **Anel do Éden IV**. |
| **`colarIV`** | `0 ~ 5` | Prioridade para resgatar **Colar do Éden IV**. |
| **`fardaIV`** | `0 ~ 5` | Prioridade para resgatar **Farda do Éden IV**. |
| **`coturIV`** | `0 ~ 5` | Prioridade para resgatar **Coturno do Éden IV**. |
> `0` = Desativado | `1` = Ativado | `1 ~ 5` = Maior-menor prioridade

#### Equipamentos [160]

| Variável  | Valores | Informação |
| --------- | ------- | ---------- |
| **`equips160`** | `0 ~ 1` | Ativa/desativa as trocas de moedas por **equipamentos do Éden nível 160**. |
| **`anelV`** | `0 ~ 5` | Prioridade para resgatar **Anel do Éden V**. |
| **`colarV`** | `0 ~ 5` | Prioridade para resgatar **Colar do Éden V**. |
| **`fardaV`** | `0 ~ 5` | Prioridade para resgatar **Farda do Éden V**. |
| **`coturV`** | `0 ~ 5` | Prioridade para resgatar **Coturno do Éden V**. |
| **`mantoIII`** | `0 ~ 5` | Prioridade para resgatar **Manto do Éden V**. |
| **`boinaII`** | `0 ~ 1` | Ativa/desativa a troca pela **Boina do Éden II**. |
> `0` = Desativado | `1` = Ativado | `1 ~ 5` = Maior-menor prioridade

---

### 🎓 Quest de 1ª Classe

| Variável  | Valores | Informação |
| --------- | ------- | ---------- |
| **`classe1`** | `0 ~ 6` | Escolhe a **1ª classe** do personagem na **Academia Criatura**. |
> `0` = Desativado (padrão) | `1` = Espadachim | `2` = Mago | `3` = Arqueiro |`4` = Noviço | `5` = Mercador | `6` = Gatuno.

---

### 📚 Quests Misc. (Aprendiz / Novo Mundo)

| Variável  | Valores | Informação |
| --------- | ------- | ---------- |
| **`1sPassos`** | `0 ~ 1` | Ativa a quest **Primeiros Passos** (Aprendiz), que concede consumíveis iniciais (poções, asas, etc). |
| **`aulaDeConsu`** | `0 ~ 1` | Ativa a quest **Aula de Consumíveis** na Academia. |
| **`aulaDeLoc`** | `0 ~ 1` | Ativa a quest **Aula de Localização**. |
| **`aulaDeVenda`** | `0 ~ 1` | Ativa a quest **Aula de Venda**. |
| **`novoMundo`** | `0 ~ 1` | Ativa a quest de acesso ao **Novo Mundo** via Agência Pata de Gato (requer **nível 80+** e **50.000 zeny**). |
> `0` = Desativado (padrão) | `1` = Ativado


### 💵 Investimento 
* **R$30** / **HWID**
* É possível solicitar um trial de 1 dia **sem compromisso**.


### 🚀 Implementações futuras

* Quests do Éden faltantes dos níveis 12, 20 e 50.
* Quests diárias 120+.

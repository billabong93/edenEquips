# Condições de ativação por automacro (categorizado)

Este documento lista **somente** as **condições** de cada `automacro`, agrupadas por categoria e por seção do arquivo, preservando a ordem de aparecimento no `eventMacros.txt`.

- Fonte: `eventMacros.txt` (11831 linhas)
- Automacros encontrados: **352**

## Quests do Éden 

### QUEST EDEN 00 

#### `eden00`
- `JobIDNot 0`
- `InInventoryID 22508 == 0`
- `overrideAI 0`
- `delay 30`


### QUEST EDEN 03

#### `eden03`
- `BaseLevel == 26..32`
- `BaseLevel == $lvl03`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lvlQuest03 off`
- `ConfigKeyNotExist eden03`
- `InInventoryID 15010 == 0`


### QUEST EDEN 04

#### `eden04`
- `BaseLevel == 33..39`
- `BaseLevel == $lvl04`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lvlQuest04 off`
- `ConfigKeyNotExist eden04`
- `InInventoryID 15010 == 0`


### QUEST EDEN 05

#### `eden05`
- `BaseLevel == 40..49`
- `BaseLevel == $lvl05`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lvlQuest05 off`
- `ConfigKeyNotExist eden05`
- `InInventoryID 15011 == 0`


### QUEST EDEN 07 

#### `eden07`
- `BaseLevel == 75..99`
- `BaseLevel == $lvl07`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lvlQuest07 off`
- `ConfigKeyNotExist eden07`
- `InInventoryID 15011 == 0`


### QUEST EDEN 08 

#### `eden08`
- `BaseLevel == 60..69`
- `BaseLevel == $lvl08`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lvlQuest08 off`
- `ConfigKeyNotExist eden08`
- `InInventoryID 15031 == 0`
- `JobIDNot 1`
- `JobIDNot 2`
- `JobIDNot 3`
- `JobIDNot 4`
- `JobIDNot 5`
- `JobIDNot 6`
- `JobIDNot 4046`


### QUEST EDEN 09

#### `eden09`
- `BaseLevel == 70..79`
- `BaseLevel == $lvl09`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lvlQuest09 off`
- `ConfigKeyNotExist eden09`


### QUEST EDEN 10 

#### `eden10`
- `BaseLevel == 80..89`
- `BaseLevel == $lvl10`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lvlQuest10 off`
- `ConfigKeyNotExist eden10`

### QUEST EDEN 11

#### `eden11`
- `BaseLevel == 90..99`
- `BaseLevel == $lvl11`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lvlQuest11 off`
- `ConfigKeyNotExist eden11`


## Quests de Classe 

### EQUIP. DE APRENDIZ > POT

#### `goMaquina`
- `JobIDNot 0`
- `ConfigKey trocarPot 1`
- `InInventoryID 5055 >= 1`

#### `potAprendiz`
- `JobIDNot 0`
- `ConfigKey trocarPot 1`
- `InInventoryID 7059 >= 4`


### QUESTS APRENDIZ

#### `init`
- `InMap iz_int, iz_int01, iz_int02, iz_int03, iz_int04`
- `ConfigKey 1sPassos 1`
- `BaseLevel == 1`

#### `primeirosPassos01`
- `QuestActive 21001`
- `ConfigKey 1sPassos 1`

#### `aulaDeConsu`
- `QuestActive 21901, 21902, 21903`
- `ConfigKey aulaDeConsu 1`

#### `aulaDeLoc`
- `QuestActive 21901, 21902, 21903`
- `ConfigKey aulaDeLoc 1`

#### `aulaDeVenda`
- `QuestActive 21901, 21902, 21903`
- `ConfigKey aulaDeVenda 1`


### PRIMEIRA CLASSE

#### `primeiraClasse`
- `JobID 0`
- `JobLevel == 10`
- `Eval ($::config{classe1} > 0 && $::config{classe1} < 7)`


### ROGUE

#### `goRogue01`
- `ConfigKey classe2 2`
- `ConfigKeyNot lockMap 0`
- `QuestInactive 2017`
- `QuestInactive 2020`
- `QuestInactive 2022`
- `QuestInactive 2023`
- `QuestInactive 2024`
- `QuestInactive 2026`
- `JobLevel == 40..50`
- `JobLevel == $lvlC2`
- `JobID 6`


### GATUNO T 

#### `gatunoT`
- `JobLevel == 10`
- `ConfigKey classe1 6`
- `JobID 4001`


### STALKER 

#### `stalker`
- `JobLevel == 50`
- `JobID 4007`


### CAVALEIRO

#### `goKnt01`
- `ConfigKey classe2 1`
- `ConfigKeyNot lockMap 0`
- `QuestInactive 9000`
- `QuestInactive 9001`
- `QuestInactive 9002`
- `QuestInactive 9003`
- `QuestInactive 9004`
- `QuestInactive 9005`
- `QuestInactive 9006`
- `QuestInactive 9007`
- `QuestInactive 9008`
- `QuestInactive 9009`
- `QuestInactive 9010`
- `QuestInactive 9011`
- `QuestInactive 9012`
- `JobLevel == 40..50`
- `JobLevel == $lvlC2`
- `JobID 1`


### ESPADACHIM T

#### `espadachimT`
- `JobLevel == 10`
- `ConfigKey classe1 1`
- `JobID 4001`


### LORDE

#### `lord`
- `JobLevel == 50`
- `JobID 4002`


### MONGE 

#### `goMonk01`
- `ConfigKey classe2 2`
- `ConfigKeyNot lockMap 0`
- `QuestInactive 3016`
- `QuestInactive 2020`
- `QuestInactive 2022`
- `QuestInactive 2023`
- `QuestInactive 2024`
- `QuestInactive 2026`
- `JobLevel == 40..50`
- `JobLevel == $lvlC2`
- `JobID 4`


### NOVIÇO T 

#### `novicoT`
- `JobLevel == 10`
- `ConfigKey classe1 4`
- `JobID 4005`


### MESTRE

#### `mestre`
- `JobLevel == 50`
- `JobID 4005`


### RENASCER

#### `renascer`
- `QuestInactive 5160`
- `BaseLevel == 99`
- `JobID 7,8,9,10,11,12,13,14,15,16,17,18,19,20,21`
- `ConfigKey reborn 1, reborn 2`


### NOVO MUNDO

#### `novoMundo`
- `BaseLevel >= 80`
- `ConfigKey novoMundo 1`
- `Zeny > 55000`


## Rotas

### ROTA 1

#### `rota00a`
- `BaseLevel == 1..7`
- `ConfigKey rota 1, rota 2`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lockMap prt_fild08`
- `InMapRegex /^(?!moc_para0).*$/`

#### `rota01a`
- `BaseLevel == 8..28`
- `ConfigKey rota 1, rota 2`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lockMap pay_fild08`
- `InMapRegex /^(?!moc_para0).*$/`

#### `rota02a`
- `BaseLevel == 29..32`
- `ConfigKey rota 1, rota 2`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lockMap pay_fild07`
- `InMapRegex /^(?!moc_para0).*$/`

#### `rota03a`
- `BaseLevel == 33..39`
- `ConfigKey rota 1, rota 2`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lockMap pay_fild09`
- `InMapRegex /^(?!moc_para0).*$/`

#### `rota04a`
- `BaseLevel == 40..47`
- `ConfigKey rota 1`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lockMap iz_dun01`
- `InMapRegex /^(?!moc_para0).*$/`

#### `rota05a`
- `BaseLevel == 48..55`
- `ConfigKey rota 1`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lockMap iz_dun02`
- `InMapRegex /^(?!moc_para0).*$/`

#### `rota06a`
- `BaseLevel == 56..68`
- `ConfigKey rota 1`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lockMap moc_fild17`
- `InMapRegex /^(?!moc_para0).*$/`

#### `rota07a`
- `BaseLevel == 69..78`
- `ConfigKey rota 1`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lockMap yuno_fild08`
- `InMapRegex /^(?!moc_para0).*$/`

#### `rota08a`
- `BaseLevel == 79..89`
- `ConfigKey rota 1`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lockMap yuno_fild11`
- `InMapRegex /^(?!moc_para0).*$/`

#### `rota09a`
- `BaseLevel == 90..99`
- `ConfigKey rota 1`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lockMap ve_fild07`
- `InMapRegex /^(?!moc_para0).*$/`


### ROTA 2

#### `rota04b`
- `BaseLevel == 40..47`
- `ConfigKey rota 2`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lockMap gef_fild10`
- `InMapRegex /^(?!moc_para0).*$/`

#### `rota05b`
- `BaseLevel == 48..55`
- `ConfigKey rota 2`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot  lockMap orcsdun01`
- `InMapRegex /^(?!moc_para0).*$/`

#### `rota06b`
- `BaseLevel == 56..64`
- `ConfigKey rota 2`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lockMap mjolnir_08`
- `InMapRegex /^(?!moc_para0).*$/`

#### `rota07b`
- `BaseLevel == 65..76`
- `ConfigKey rota 2`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lockMap mjolnir_04`
- `InMapRegex /^(?!moc_para0).*$/`

#### `rota08b`
- `BaseLevel == 77..89`
- `ConfigKey rota 2`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lockMap gef_fild08`
- `InMapRegex /^(?!moc_para0).*$/`

#### `rota09b`
- `BaseLevel == 90..99`
- `ConfigKey rota 2`
- `ConfigKeyNot lockMap 0`
- `ConfigKeyNot lockMap gef_fild06`
- `InMapRegex /^(?!moc_para0).*$/`

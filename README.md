# edenEquips
Plugin de injeção de eventMacros para Quests e Equipamentos do Éden - Openkore

# Requisitos:

  - Python
  - Automacro aeroplano ra_fild12. (https://openkore.com.br/viewtopic.php?p=6470)
  - Se não existir, criar um arquivo eventMacros.txt na pasta ./control.
  - Pastas e arquivos atualizados: (https://github.com/dhmello/openkore_latam)
    ./fields
    ./tables/ROla/portals.txt

# Instruções:

  - Use config.py para configurar suas opções de equipamentos, encantamentos e cartas.
    Ou insira as variáveis manualmente no config.txt.
    As opções escolhidas no config.py são salvas no final de config.txt,
    e lidas pelo plugin durante a execução.
    As opções por padrão são [0]. No caso de [0], não é criada uma variável.
    Se não houver escolha de equipamentos disponível para sua classe, escolha [0].
  - Adicione edenEquips em sys.txt no final da linha loadPlugins_list.
  - Em caso de necessidade de reinjeção, use 'plugin reload edenEquips' no console.

# Configurações necessárias para um bom funcionamento:

* config.txt:
  - storageAuto_npc com coordenadas configuradas.
  - route_maxWarpFee vazio ou com valor acima de 20000.

* routeweights.txt:
  - AIRSHIP 500
  - moc_fild20 10000

# O que não fazer:

  - 'reload eventMacros' durante a execução do plugin.
  - Jamais apague as variáveis criadas pelo/para o plugin em config.txt, salvo necessidade
    de rollback por falha na execução de etapas do macro, ou a remoção do plugin.
  - Não faça alterações no proxy.py ou edenEquips.pl. O acesso é barrado pelo servidor
    em caso de qualquer modificação ou ausência dos arquivos.

# Informações e avisos:

  - A maior parte das classes foi testada, e os equipamentos estão em sua maioria, se não todos,
    nas posições corretas. (Opções extraídas de .csv)
  - Telesearch é fundamental para a conclusão dessas quests, não é possível desativá-lo.
  - Se seu bot não está pegando o aeroplano ou usando os teleportes, verifique routeweights.txt,
    e route_maxWarpFee em config.txt.
  - As Asas de Mosquito só devem ser desabilitadas se houver algum outro item equivalente
    em teleportAuto_item1.
  - Apesar de interceptado, o bot continuará usando qualquer skill ou item configurado no
    seu config.txt, macros.txt e eventMacros.txt.
  - O plugin depende do seu storageAuto_npc configurado, para conseguir devolver o bot para o
    lugar original.
  - A injeção não sobrescreverá seu eventMacros.txt. De qualquer forma, sempre bom manter um backup.
  - O plugin não é configurado pra comprar ou fazer uso de pots de sp. Mas pegará do armazém ou
    comprará mais antes de começar qualquer quest, e usará, se seu bot estiver configurado para isso.


# Variáveis de configurações do edenEquips e suas funções: (Inseridas em config.txt)

* Equipamentos:

  - eq03 (0, 1) - Determina a opção de equipamentos da Quest nv26.
    Opções para: Espadachim, Noviço e Mercador.
  - eq05 (0, 1) - Determina a opção de equipamentos da Quest nv40.
    Opções para: Espadachim, Cavaleiro, Templário, Noviço, Sacerdote, Monge, Mercador,
    Ferreiro, Alquimista e Espiritualista.
  - eq08 (0, 1, 2) - Determina a opção de equipamentos da Quest nv60.
    Opções para: Espadachim, Cavaleiro, Templário, Sacerdote, Monge, Sábio, Bardo, 
    Odalisca, Mercador, Ferreiro, Alquimista, Mercenário, Espiritualista e Ninja.

* Encantamentos:

  - enc (0, 1) - Determina se o encantamento de nv70 vai ser ATQ ou ATQM.
  - carta (0, 1, 2, 3, 4, 5) - Tipo de carta +DMG/MDMG ou fator de cura no encantamento nv80.

* Utilizáveis:

  - semAsas (0, 1) - Desabilita a compra de Asas de Mosquito.
  - semPots (0, 1) - Desabilita a compra de Poções Laranjas.

* Fases de Quest: (Só altere com convicção do que está fazendo)
* Determinam a fase da quest do éden em que o bot se encontra.

  - eden03 (0, 1, 2, 3, end)	- Variável inexistente = Inicia a quest.
  - eden05 (0, 1, 2, 3, end)	- 0 = Salvar na kafra da quest.
  - eden08 (0, 1, 2, 3, end)	- 1 = Checar e comprar de Asas de Mosquito e Poções Laranjas.
  - eden09 (0, 1, 2, 3, end)	- 2 = Realização da Quest.
  - eden10 (0, 1, 2, 3, end)	- 3 = Resgate de equipamentos.
  - eden11 (0, 1, 2, 3, end)	- end = Conclusão.

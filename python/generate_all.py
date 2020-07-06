import generate_html

npc_names = ["Belmazog", "Coalgnasher", "DahaksSkull", "HEUBERK_THROPP", "Kelleni", "NessianWarhound", "NessianWarhound_elite",
             "Racharak", "RustyMae", "SCARLET_TRIAD_SNEAKS", "Senna", "SpawnOfDahak", "TrappedLathe", "TreeOfDreadfulDreams", "WrathOfDestroyer"]

npcs = [mod.c for mod in map(__import__, npc_names)]
for npc in npcs:
    print(npc._name)
    generate_html.generate(npc)

import generate_html

npc_names = ["Belmazog", "DahaksSkull", "HEUBERK_THROPP", "Kelleni", "NessianWarhound", "NessianWarhound_elite",
             "Racharak", "SCARLET_TRIAD_SNEAKS", "SpawnOfDahak", "TrappedLathe", "TreeOfDreadfulDreams", "WrathOfDestroyer"]

npcs = map(__import__, npc_names)
for npc in npcs:
    print(npc.c._name)
    generate_html.generate(npc.c)

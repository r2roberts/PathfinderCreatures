import creature
from creature import Actions

c = creature.Creature("HEUBERK THROPP", lvl=9)
c.traits("UNIQUE", "LE", "MEDIUM", "HUMAN",
         "HUMANOID")
c.perception("+14;")
c.languages("Common, Dwarven, Elven, Gnoll, Halfling")

c.skills("Athletics +16", "Deception +21", "Diplomacy +15",
         "Intimidation +19", "Mercantile Lore +16", "Society +16",
         "Thievery +16")
c.attrs("Str +3", "Dex +2", "Con +3", "Int +1", "Wis +1", "Cha +4")
c.item("dagger(3),")
c.item("keys to manacles,")
c.item("leather armor,")
c.item("+1 striking mace,", magic=True)
c.item("average manacles(marked with the symbol of the Scarlet Triad),")
c.item("spellbook,")
c.item("infiltrator’s thieves tools")
c.ac("28")
c.saves("Fort +21", "Ref +15", "Will +18")
c.hp("155")
c.reactive_ability("Timely Distraction", Actions.REACTION,
                   trigger="A creature Heuberk can see within his melee reach misses him with a melee Strike.",
                   effect="Heuberk attempts to Feint the creature. If it’s not Heuberk’s turn and he gets a success, the effect applies on his next turn.")

c.speed("25 feet")
c.melee("mace +19 (shove)", Actions.ONE, damage="2d6+9 bludgeoning")
c.melee("dagger +18 (agile, versatile S)",
        Actions.ONE, damage="1d4+9 piercing")
c.ranged("dagger +17 (agile, thrown 10 feet, versatile S)",
         Actions.ONE, damage="1d4+9 piercing")
sg = c.spell_group("Occult Prepared Spells", dc=27, desc="attack +19")
spells = sg.spells(5)
spells.spell("crushing despair", id="57")
spells = sg.spells(4)
spells.spell("discern lies", id="74")
spells.spell("fly", id="125")
spells = sg.spells(3)
spells.spell("dream message", id="90")
spells.spell("enthrall", id="104")
spells.spell("hypnotic pattern", id="157")
spells = sg.spells(2)
spells.spell("invisibility", id="164")
spells.spell("mirror image", id="197")
spells.spell("paranoia", id="214")
spells = sg.spells(1)
spells.spell("charm", id="34")
spells.spell("command", id="45")
spells.spell("fear", id="110")
spells.spell("ray of enfeeblement", id="244")
spells = sg.spells(5, type="Cantrips")
spells.spell("detect magic", id="66")
spells.spell("message", id="190")
spells.spell("prestidigitation", id="229")
spells.spell("read aura", id="246")
spells.spell("shield", id="280")

c.offensive_ability("Identify an Opening", Actions.ONE, desc="(auditory, linguistic)",
                    requirements="A creature is flat-footed against Heuberk’s next melee attack.",
                    effect="Heuberk points out a lapse in the creature’s defenses. The creature is flat-footed against all melee attacks attempted by any of Heuberk’s allies who hear and understand this instruction until the start of Heuberk’s next turn.")

c.offensive_ability("Sneak Attack", desc="2d6")

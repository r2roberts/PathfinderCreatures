import creature
from creature import Actions

c = creature.Creature("SCARLET TRIAD SNEAKS", lvl=6)
c.traits("UNCOMMON", "CE", "MEDIUM", "HUMAN",
         "HUMANOID")

c.perception("+12")
c.languages("Common")
c.skills("Acrobatics +14", "Athletics +10", "Deception +12",
         "Intimidation +10", "Stealth +16", "Thievery +14")
c.attrs("Str +2", "Dex +4", "Con +2", "Int +0", "Wis +0", "Cha +2")
c.item("bloodseeker beak (affixed to rapier),", magic=True)
c.item("dagger(3),")
c.item("keys to manacles,")
c.item("leather armor,")
c.item("average manacles (marked with the symbol of the Scarlet Triad),")
c.item("+1 rapier,", magic=True)
c.item("thieves’ tools")

c.ac("25")

c.saves("Fort +10", "Ref +14", "Will +12")
c.hp("95")
c.reactive_ability("Nimble Dodge", Actions.REACTION, requirements="A sneak can’t use this reaction while encumbered.",
                   trigger="The sneak is hit by an attack made by a creature the sneak can see.", effect="The sneak gains a +2 circumstance bonus to their Armor Class against the triggering attack.")

c.reactive_ability("Deny Advantage",
                   desc="The sneak isn’t flat-footed to hidden, undetected, or flanking creatures of 6th level or lower, or creatures of 6th level or lower using surprise attack.")

c.reactive_ability("Mobility",
                   desc="When the sneak takes a Stride action to move half their Speed or less, that movement does not trigger reactions.")

c.speed("25 feet")
c.melee("rapier +17 (deadly 1d8, disarm, finesse)",
        Actions.ONE,  damage="1d6+5 piercing")
c.melee("dagger +16 (agile, finesse, versatile S)",
        Actions.ONE, damage="1d4+4 piercing")
c.ranged("dagger + 16 (agile, thrown 10 feet, versatile S)",
         Actions.ONE, damage="1d4+4 piercing")
c.offensive_ability("Efficient Capture", Actions.THREE, desc="(attack, manipulate)",
                    requirements="The sneak has manacles in hand and is adjacent to a creature.",
                    effect="The sneak attempts to bind the creature’s wrists or ankles with the manacles. If the sneak succeeds at an attack roll with a +16 modifier against the target’s AC, they apply the manacles.")
c.offensive_ability("Sneak Attack", desc="2d6")
c.offensive_ability("Surprise Attack",
                    desc="In the first round of combat, creatures that haven’t acted yet are flat-footed to the sneak.")

import creature
from creature import Actions

c = creature.Hazard("TRAPPED LATHE", lvl=10)
c.traits("COMPLEX", "MECHANICAL", "TRAP")

c.stealth("+19 (expert) DC 29 to notice the line of cord running from the lathe’s trigger toward the door to area A2.")
c.description("The powered lathe’s springs have been critically overwound so that when jostled or triggered, the lathe unwinds violently, hurling blades, gears, and sharp shards of metal around the room.")
c.disable("Thievery DC 31 (expert) on the lathe releases the tension on its springs without unleashing its blades and gears.")

c.ac("30")
c.saves("Fort +22", "Ref +14")
c.hardness("18", hp="72", bt="36")
c.immunities("critical hits, object immunities, precision damage")
c.reactive_ability("Unleash Fragments", Actions.REACTION, trigger="The lathe is jostled or damaged, or its trigger is remotely pulled.",
                   effect="The trap makes a sharpened fragment Strike against a random target in area A1, then rolls for initiative.")

c.routine("(4 actions) The lathe attempts four sharpened fragment attacks against creatures in the room, selecting a target randomly from all available targets in area A1. The trap does not take multiple attack penalties for any of its attacks. The trap loses 1 action each turn as its springs wind down, and becomes disabled when it has 0 actions.")
c.ranged("sharpened fragment +26", Actions.ONE,
         damage="2d8+12 slashing plus 1d8 persistent bleed damage on a critical hit")

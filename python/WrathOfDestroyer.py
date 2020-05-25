import creature
from creature import Actions

c = creature.Hazard("Wrath of the Destroyer", lvl=10)
c.traits("COMPLEX", "MAGICAL", "TRAP")
c.stealth(
    "+22 (expert) to notice subtle vapors of magical energy seething across the doors")
c.description("These heavy doors, carved with an image of Dahak, echo with a hatred so powerful that it can kill anyone who comes nearby, manifesting a vision of Dahak’s head emerging from the doors to strike at a foe.")
c.disable("Thievery DC 29 (expert) to disrupt the divine magic, Religion DC 29 (expert) to placate the wrathful energies, or dispel magic (5th level; counteract DC 26).")
c.ac("30")
c.saves("Fort +22", "Ref +14")
c.hardness("18", hp="72", bt="36", part="Door")
c.immunities("critical hits, fire, object immunities, precision damage")
c.reactive_ability("Expunge", action=Actions.REACTION, trigger="A non-worshipper of Dahak touches either door leading to C7;",
                   effect="The hazard targets the creature with Face of the Fatal Divine, then rolls initiative.")
c.routine("(1 action) On its initiative, the wrath of the destroyer targets the closest target in area C6 with Face of the Fatal Divine.")
c.offensive_ability("Face of the Fatal Divine", action=Actions.ONE,
                    desc="(death, divine, emotion, fear, illusion, mental) The creature beholds the face of Dahak as it emerges to bite with its burning jaws, targeting the creature with phantasmal killer(5th level, Will DC 29).")
c.reset("The trap deactivates and resets if 1 minute passes without any creature being in range.")

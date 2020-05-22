import creature
from creature import Actions

c = creature.Hazard("Dahak’s Skull", lvl=6)
c.traits("UNIQUE", "COMPLEX", "FIRE", "MAGICAL", "TRAP")
c.perception("+16 darkvision, see invisibility")

c.stealth("+0, but DC 24 to notice that the fiery lights within the skull’s eye sockets seem to be looking around the room.")
c.description(
    "A pair of magical gems inside the dragon skull’s eye sockets act as magical sensors with a 30-foot radius.")
c.disable("Thievery DC 27 (expert) two times to pry the gems embedded deep in the skull’s eye sockets without triggering the sensor, or dispel magic(4th level, counteract DC 22) twice to dispel both eyes.")
c.ac("24")
c.saves("Fort +17", "Ref +8")
c.hardness("14", hp="56", bt="28")
c.immunities("critical hits, fire, object immunities, precision damage")

c.reactive_ability("Dahak’s Glance", action=Actions.REACTION, desc="(divine, evocation, fire)", trigger="A living creature that is not a member of the Cinderclaws enters area C9",
                   effect="One of the dragon skull’s eye sockets shoots an eye beam at the triggering creature, then the hazard rolls initiative.")

c.routine("(2 actions) On its initiative, Dahak’s skull fires up to two eye beams; it must target a different creature with each attack. The eye beams can’t target creatures directly below the skull.")
c.ranged("eye beam + 20 (divine, evocation, fire, range 150 feet)", action=Actions.ONE,
         damage="8d6 fire")

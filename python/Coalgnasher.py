import creature
from creature import Actions

c = creature.Creature("Coalgnasher (Elite Nightmare)", lvl=7)
c.traits("NE", "Large", "Beast", "Fiend")
c.perception("+16; darkvision")
c.languages("Abyssal, Daemonic, Infernal")
c.skills("Acrobatics +15", "Athletics +18",
         "Intimidation +16", "Survival +14")
c.attrs("Str +6", "Dex +3", "Con +3", "Int +1", "Wis +4", "Cha +2")
c.interaction_ability("Smoke",
                      desc="(aura) 15 feet. The nightmare continually exhales black smoke that creates concealment in an aura around it. Nightmares and their riders can see through this smoke. A creature that begins its turn in the area becomes sickened 2 (DC 25 Fortitude negates) and is then temporarily immune to sickness from the smoke for 1 minute. The nightmare, its rider, any creature currently holding its breath (or that does not need to breathe), and any creature immune to poison are immune to the aura’s sickened effect, but not the concealment.")
c.ac("26")
c.saves("Fort +17", "Ref +17", "Will +14")
c.hp("120")
c.resistances("fire 10")
c.speed("40 feet, fly 90 feet")
c.melee("jaws +18 [+13/+8](evil, magical)", Actions.ONE,
        damage="2d10+8 piercing plus 1d6 evil")
c.melee("hoof +18 [+14/+10](agile, evil, fire, magical)",
        Actions.ONE, damage="1d8+8 bludgeoning plus 1d6 evil and 1d8 fire")
sg = c.spell_group("Divine Innate Spells", dc="26")
sp = sg.spells(7)
sp.spell("plane shift", desc="(self and rider only)", id="222")
c.offensive_ability("Flaming Gallop",
                    Actions.TWO,
                    desc="(fire) The nightmare Strides or Flies up to triple its Speed. Its hooves burst with intense flame, dealing 3d6+2 fire damage (DC 26 basic Reflex save) once to each creature other than the nightmare’s rider that the nightmare moves adjacent to during its gallop.")

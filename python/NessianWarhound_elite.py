import creature
from creature import Actions

c = creature.Creature("Nessian Warhound (Elite)", lvl=10)
c.traits("LE", "LARGE", "BEAST", "FIEND", "FIRE")
c.perception("+21; darkvision, scent(imprecise) 120 feet")
c.languages("Infernal(can’t speak any language)")
c.skills("Acrobatics +20", "Athletics +21",
         "Stealth +20", "Survival +22 (+24 to Track)")
c.attrs("Str +6", "Dex +5", "Con +5", "Int –2", "Wis +4", "Cha –2")
c.ac("30")
c.saves("Fort +23", "Ref +21", "Will +18")
c.hp("180")
c.immunities("fire")
c.weaknesses("cold 10")
c.reactive_ability("Hellish Revenge", action=Actions.REACTION, trigger="The Nessian warhound is critically hit by any Strike.",
                   effect="The Nessian warhound’s Breath Weapon recharges. It can immediately use it as part of this reaction.")
c.speed("40 feet")
c.melee("jaws + 23 (magical)", action=Actions.ONE,
        damage="2d8+8 piercing plus 1d6 evil and 2d6 fire")
c.offensive_ability("Breath Weapon", action=Actions.ONE,
                    desc="(divine, evocation, fire) The warhound breathes flames that deal 11d6 fire damage to all creatures in a 15-foot cone (DC 30 basic Reflex save.) The warhound can’t use Breath Weapon again for 1d4 rounds. If the Nessian warhound would take fire damage or be targeted by a fire effect, its Breath Weapon recharges.")

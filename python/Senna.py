import creature
from creature import Actions

c = creature.Creature("Senna (Elite Annis Hag)", lvl=7)

c.traits("CE", "LARGE", "HAG", "HUMANOID")

c.perception("+17; darkvision")
c.languages("Aklo, Common, Jotun")
c.skills("Acrobatics +12", "Athletics +16 (+18 to Grapple)", "Deception +13",
         "Diplomacy +11", "Intimidation +13", "Stealth +16")
c.attrs("Str +6", "Dex +4", "Con +4", "Int +1", "Wis +4", "Cha +3")
c.ability_modifier(
    "Coven", desc="Senna adds earthbind, passwall, and spellwrack to her coven’s spells.")

c.ac("26")
c.saves("Fort +18", "Ref +14", "Will +16",
        desc="; +1 status to all saves vs. magic")
c.hp("105")
c.resistances("physical 5 (except bludgeoning)")

c.speed("40 feet")
c.melee("claws +18 [+14/+10] (agile, magical, reach 10 feet)", Actions.ONE,
        damage="2d8+8 cold iron slashing plus Grab")

c.offensive_ability("Bonds of Iron", Actions.TWO,
                    desc=" (attack, conjuration, occult) Once per day, an annis hag can cause a cage built of cold iron fingernails to spring out of nothingness at a range of up to 30 feet, attempting an Athletics check to Grapple against the target’s Fortitude DC; if the target has a weakness to cold iron, the annis hag gains a +2 circumstance bonus to this check. Unlike a normal Grapple, the annis hag doesn’t need to be within reach and can move as she pleases, and a successful attempt lasts until the creature escapes (DC 26), causing the cage to crumble into rust. Any creature can attempt to destroy the cage by attacking it. It has an AC of 21, Hardness 12, and 48 Hit Points.")

c.offensive_ability("Change Shape", Actions.ONE,
                    desc="(concentrate, occult, polymorph, transmutation) The hag can take on the appearance of any Medium female humanoid. This doesn’t change her Speed or her attack and damage bonuses with her Strikes but might change the damage type her Strikes deal (typically to bludgeoning).")

c.offensive_ability("Rend", Actions.ONE, desc="claw")

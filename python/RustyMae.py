import creature
from creature import Actions

c = creature.Creature("Rusty Mae", lvl=10)

c.traits("UNIQUE", "LE", "LARGE", "HAG", "HUMANOID")

c.perception("+22; darkvision")
c.languages("Aklo, Common, Infernal, Jotun")
c.skills("Acrobatics +17", "Athletics +21 (+23 to Grapple)", "Deception +19",
         "Diplomacy +21", "Intimidation +17", "Religion +22", "Stealth +19")
c.attrs("Str +7", "Dex +5", "Con +5", "Int +4", "Wis +6", "Cha +5")
c.ability_modifier(
    "Coven", desc="Rusty Mae adds earthbind, passwall, and spellwrack to her coven’s spells.")

c.ac("30")
c.saves("Fort +22", "Ref +16", "Will +19",
        desc="; +1 status to all saves vs. magic")
c.hp("155")
c.resistances("physical 10 (except bludgeoning)")

c.speed("40 feet")
c.melee("claws +23 (agile, cold iron, magical, reach 10 feet)", Actions.ONE,
        damage="2d8+13 slashing plus Grab and rust")
sg = c.spell_group("Divine Rituals", dc="29")
sp = sg.spells(lvl=None)
sp.spell("planar ally")
c.offensive_ability("Bonds of Iron", Actions.TWO,
                    desc=" (attack, conjuration, occult) Once per day, an annis hag can cause a cage built of cold iron fingernails to spring out of nothingness at a range of up to 30 feet, attempting an Athletics check to Grapple against the target’s Fortitude DC; if the target has a weakness to cold iron, the annis hag gains a +2 circumstance bonus to this check. Unlike a normal Grapple, the annis hag doesn’t need to be within reach and can move as she pleases, and a successful attempt lasts until the creature escapes (DC 29), causing the cage to crumble into rust. Any creature can attempt to destroy the cage by attacking it. It has an AC of 25, Hardness 14, and 56 Hit Points.")

c.offensive_ability("Change Shape", Actions.ONE,
                    desc="(concentrate, occult, polymorph, transmutation) The hag can take on the appearance of any Medium female humanoid. This doesn’t change her Speed or her attack and damage bonuses with her Strikes but might change the damage type her Strikes deal (typically to bludgeoning).")

c.offensive_ability("Rend", Actions.ONE, desc="claw")
c.offensive_ability("Rust",
                    desc="Rusty Mae’s claws cause metal to rapidly rust and corrode. If she succeeds at a claws Strike or Disarm attempt, she deals 2d6 damage(doubled on a critical hit) to a metal item the target is wearing or holding, ignoring its Hardness, in addition to the damage she deals to the target with her claws. If she hits an unattended metal item, the item takes 2d6 damage automatically. If a creature uses the Shield Block reaction with a metal shield against Rusty Mae’s claw attack, the shield is automatically broken, but no other item is affected on that attack.")

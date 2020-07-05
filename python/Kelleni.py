import creature
from creature import Actions

c = creature.Creature("Kelleni (Elite Night Hag)", lvl=10)
c.traits("NE", "Medium", "Fiend", "Hag", "Humanoid")
c.perception("+18 darkvision")
c.languages("Abyssal, Aklo, Celestial, Common, Infernal")

c.skills("Arcana +18", "Deception +18", "Diplomacy +18",
         "Intimidation +14", "Occultism + 20", "Religion + 20")
c.attrs("Str +5", "Dex +4", "Con +6", "Int +4", "Wis +5", "Cha +3")

c.ability_modifier("Coven",
                   "A night hag adds dominate, nightmare, scrying, and spellwrack to her coven’s spells.")
c.ability_modifier("Nightmare Rider",
                   "When a night hag rides a nightmare, the nightmare also gains the night hag’s status bonus to saves against magic, and both the hag and rider benefit when the night hag uses her heartstone’s ethereal jaunt innate spell.")
c.item("heartstone", magic=True)
c.ac("28")
c.saves("Fort +19", "Ref +17", "Will +18;",
        desc="+2 status to all saves vs. magic, –2 to all saves if the night hag does not have her heartstone")
c.hp("170")
c.immunities("sleep;")
c.resistances("mental 10;")
c.weaknesses("cold iron 10;")
c.speed("25 feet")

c.melee("jaws +20 [+15/+10](magical)", Actions.ONE,
        damage="2d8+8 piercing plus 1d6 evil and Abyssal plague")
c.melee("claw +20 [+16/+12](agile, magical)", Actions.ONE,
        damage="2d10+8 slashing plus 1d6 evil")
sg = c.spell_group("Occult Innate Spells", dc="28")
sp = sg.spells(9)
sp.spell("bind soul", desc="(at will from heartstone)", id="21")
sp.spell("ethereal jaunt", desc="(at will from heartstone)", id="105")
sp = sg.spells(8)
sp.spell("dream council", id="89")
sp = sg.spells(5)
sp.spell("nightmare", id="208")
sp.spell("shadow blast", desc="(x2, from heartstone)", id="273")
sp = sg.spells(3)
sp.spell("dream message", desc="(at will)")
sp.spell("magic missile", desc="(at will)")
"""
2nd invisibility(at will)
1st ray of enfeeblement(at will), sleep(at will)
Constant(3rd) detect magic
(2nd) detect alignment(all alignments simultaneously)
Abyssal Plague(disease) A creature can’t recover from drained until abyssal plague is cured. Saving Throw DC 28 Fortitude
Stage 1 Drained 1 (1 day)
Stage 2 Drained increases by 2 (1 day)
Change Shape Single Action(concentrate, occult, polymorph, transmutation) The night hag can take on the appearance of any Medium female humanoid. This doesn’t change her Speed or her attack and damage bonuses with her Strikes, but might change the damage type her Strikes deal(typically to bludgeoning).
Dream Haunting(enchantment, occult, mental) If a night hag is ethereal and hovering over a sleeping chaotic or evil creature, she can ride the victim’s back until dawn. The creature endures tormenting dreams as the hag casts nightmare on it, and is exposed to abyssal plague. Any drained caused by dream haunting is cumulative. Only an ethereal being can confront the night hag and stop her dream haunting.
Spell Ambush A creature flat-footed to the night hag takes a –2 circumstance penalty to checks and DCs to defend against her spells.
"""

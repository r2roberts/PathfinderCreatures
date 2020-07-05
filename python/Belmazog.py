import creature
from creature import Actions

c = creature.Creature("Belmazog", lvl=9)
c.traits("UNIQUE", "CE", "MEDIUM", "ACID",
         "AMPHIBIOUS", "BOGGARD", "DRAGON", "HUMANOID")
c.perception("+18; darkvision, scent(imprecise) 60 feet")
c.languages("Abyssal, Boggard, Common, Draconic, Mwangi")

c.skills("Acrobatics +16", "Athletics +18", "Deception +19",
         "Intimidation +21", "Performance +17", "Religion +18",
         "Society +12", "Survival +14")
c.attrs("Str +5", "Dex +3", "Con +3", "Int –1", "Wis +3",
        "Cha +6")
c.ac("28")
c.saves("Fort +18", "Ref +16", "Will +18")
c.hp("145")
c.immunities("acid, paralyzed, sleep")
c.speed("40 feet, swim 40 feet")
c.melee("jaws +20", action=Actions.ONE,
        damage="2d8+11 piercing plus 1d12 acid")
c.melee("claw +20 (agile)", action=Actions.ONE, damage="2d8+11 slashing")
c.melee("tongue +20 (reach 10 feet)", action=Actions.ONE,
        damage="2d6+11 acid plus tongue grab")

sg = c.spell_group("Divine Prepared Spells", dc=27,
                   desc="attack +19")
spells = sg.spells(5)
spells.spell("harm", id="146")

spells = sg.spells(4)
spells.spell("burning hands (×2)", id="30")
spells.spell("fear", id="110")
spells.spell("fireball", id="119")
spells.spell("heal (×2)", id="148")
spells.spell("summon monster", id="316")

spells = sg.spells(2)
spells.spell("ray of enfeeblement", id="244")
spells.spell("see invisibility", id="271")

spells = sg.spells(5, type="Cantrips")
spells.spell("detect magic", id="66")
spells.spell("forbidding ward", id="126")
spells.spell("produce flame", id="236")
spells.spell("shield", id="280")

sg = c.spell_group("Rituals")
spells = sg.spells(lvl=None)
spells.spell("nul-acrumi vazghul")
spells.spell("planar ally")


c.offensive_ability("Breath Weapon", action=Actions.TWO,
                    desc="(arcane, acid); Belmazog spews a gout of acid that deals 10d6 acid damage in a 30-foot cone (DC 28 basic Reflex save). Belmazog can’t use Breath Weapon again for 1d4 rounds.")
c.offensive_ability("Drowning Drone", action=Actions.REACTION, desc="(auditory, mental)", trigger="The boggard swampseer or one of its allies within 60 feet attempts a saving throw against an auditory or sonic effect.",
                    effect="The swampseer releases a croak that drowns out other sound. It rolls a Performance check. It and boggard allies in the area can use the higher result of the swampseer’s Performance check or their saves to resolve the effects against the auditory or sonic effect.")
c.offensive_ability(name="Nul-Acrumi Vazghul Ritual", desc="This rare and highly specialized ritual, taught to Belmazog by the Scarlet Triad, allowed her to use the fossilized remains of Dahak to erect powerful defenses in the region in the form of dragon pillars, but the resources and time required to perform the ritual again are not available to Belmazog during the course of this adventure. As a result, and since there is no way for the PCs to learn or benefit from the ritual, further information beyond the repercussions detailed in the adventure itself are not presented here.")
c.offensive_ability(
    "Swamp Stride", desc="A boggard warrior ignores difficult terrain caused by swamp terrain features.")
c.offensive_ability("Terrifying Croak", action=Actions.ONE,
                    desc="(auditory, emotion, fear, mental) Belmazog unleashes a terrifying croak. Any non-boggard within 30 feet becomes frightened 1 unless they succeed at a DC 28 Will save; those who critically succeed are temporarily immune for 1 minute.")
c.offensive_ability("Tongue Grab", desc="If Belmazog hits a creature with her tongue, that creature becomes grabbed by her. Unlike with a normal grab, the creature isn’t immobilized, but it can’t move beyond the reach of the boggard’s tongue. A creature can sever the tongue by hitting AC 25 and dealing at least 8 slashing damage. Though this doesn’t deal any damage Belmazog, it prevents her from using her tongue Strike until she regrows its tongue, which takes a week.")

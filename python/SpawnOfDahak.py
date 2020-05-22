import creature
from creature import Actions

c = creature.Creature("Spawn of Dahak", lvl=8)
c.traits("Rare", "CE", "SMALL", "CHARAU-KA", "DRAGON", "FIRE", "HUMANOID")
c.perception("+16; darkvision, scent(imprecise) 30 feet")
c.languages("Draconic, Mwangi")
c.item("+1 striking warhammer", True)

c.skills("Arcana +12", "Athletics +18", "Crafting +10",
         "Intimidation +17", "Religion +14", "Stealth +15", "Survival +14")
c.attrs("Str +6", "Dex +3", "Con +5", "Int +0", "Wis +4", "Cha +1")
c.ac("27")
c.saves("Fort +19", "Ref +13", "Will +16")
c.hp("135")
c.immunities("fire, paralyzed, sleep")
c.reactive_ability("Tail Swipe", action=Actions.REACTION, trigger="A creature within reach of Racharak’s tail uses a move action or leaves a square during a move action it’s using.",
                   effect="Racharak makes a tail Strike at the creature with a –2 penalty. If it hits, it disrupts the creature’s action.")
c.speed("30 feet, climb 30 feet")
c.melee("warhammer +21 (magical, shove)", action=Actions.ONE,
        damage="2d8+9 bludgeoning (plus 1d5 fire if red-hot)")
c.melee("jaws + 20", action=Actions.ONE, damage="2d8+9 piercing plus 2d4 fire")
c.melee("claw + 20 (agile)", action=Actions.ONE, damage="2d8+9 slashing")
c.melee("tail + 20 (reach 10 feet)",
        action=Actions.ONE, damage="2d8+9 slashing")
c.ranged("thrown rock + 17 (deadly 1d6, thrown 20 feet)",
         action=Actions.ONE, damage="2d6+9 bludgeoning")
c.offensive_ability("Breath Weapon", action=Actions.TWO,
                    desc="Racharak breathes flames that deals 9d6 fire damage to all creatures in a 30-foot cone(DC 26 basic Reflex save). It can’t use Breath Weapon again for 1d4 rounds.")
c.offensive_ability("Draconic Frenzy", action=Actions.TWO,
                    desc="Racharak makes two claw Strikes and one bite Strike in any order.")
c.offensive_ability("Shrieking Frenzy", action=Actions.FREE,
                    trigger="The charau-ka’s turn begins.", frequency="once per hour", effect="The charau-ka is quickened until the end of its turn, and can use the extra action to Stride or Strike. While in the frenzy, the charau-ka can’t speak and automatically critically fails Stealth checks, due to its loud wailing.")
c.offensive_ability("Thrown Weapon Mastery", desc="Any weapon a charau-ka throws gains the deadly d6 weapon trait. Furthermore, when a charau-ka throws an improvised weapon, it does not take the –2 penalty for doing so, nor does it take a penalty for using a thrown improvised weapon with the nonlethal trait to make a lethal attack.")
# sg = c.spell_group("Extra Spells", dc=25, desc="attack +17")
# spells = sg.spells(3)
# spells.spell("fireball", id="119")
# spells.spell("vampiric touch")
# spells = sg.spells(3, is_cantrip=True)
# spells.spell("daze")
# spells.spell("divine lance")

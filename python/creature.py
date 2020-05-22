from enum import Enum
import collections


class Actions(Enum):
    FREE = 0
    REACTION = -1
    ONE = 1
    TWO = 2
    THREE = 3


Ability = collections.namedtuple('Ability',
                                 ["name", "action", "trigger", "effect", "desc", "frequency"])

Attack = collections.namedtuple('Attack', ["desc", "action", "damage"])

Hardness = collections.namedtuple('Hardness', ["hardness", "part", "hp", "bt"])


class Spell(object):

    def __init__(self, name: str, id: str = None) -> None:
        self._name = name
        self._id = id


class Spells(object):
    levels = {
        1: "1st",
        2: "2nd",
        3: "3rd",
    }

    @classmethod
    def to_level(cls, lvl) -> str:
        lvl_str = cls.levels.get(lvl, f"{lvl}th")
        return lvl_str

    def __init__(self, lvl, is_cantrip: bool = False) -> None:
        self._spells = []
        if lvl is not None:
            lvl_str = self.to_level(lvl)
            self._lvl = f"Cantrips ({lvl_str})" if is_cantrip else lvl_str
        else:
            self._lvl = None

    def spell(self, name, id=None):
        self._spells.append(Spell(name, id=id))


class SpellGroup(object):
    def __init__(self, name: str, dc: int, desc: str) -> None:
        self._name = name
        self._desc = desc
        self._dc = dc
        self._spells = []

    def spells(self, lvl=None, is_cantrip: bool = False) -> Spells:
        spells = Spells(lvl, is_cantrip=is_cantrip)
        self._spells.append(spells)
        return spells


class NPC(object):
    def __init__(self, name: str, lvl: int = 0) -> None:
        self._name = name
        self._lvl = lvl

        self._perception = None
        self._ac = None
        self._saves = None

        self._hp = None
        self._immunities = None
        self._weaknesses = None
        self._resistances = None
        self._melees = []
        self._ranged = []
        self._reactive_abilities = []
        self._offensive_abilities = []

    def traits(self, *traits) -> None:
        self._traits = list(traits)

    def perception(self, perception: str):
        self._perception = perception

    def saves(self, *saves):
        self._saves = saves

    def ac(self, ac: str):
        self._ac = ac

    def immunities(self, immunities: str):
        self._immunities = immunities

    def weaknesses(self, weaknesses: str):
        self._weaknesses = weaknesses

    def resistances(self, resistances: str):
        self._resistances = resistances

    def reactive_ability(self, name: str, action: Actions = None, desc: str = None, trigger: str = None, effect: str = None,
                         frequency: str = None):
        a = Ability(name, action, trigger, effect, desc, frequency)
        self._reactive_abilities.append(a)

    def melee(self, desc: str, action: Actions = None, damage: str = None):
        a = Attack(desc, action, damage)
        self._melees.append(a)

    def ranged(self, desc: str, action: Actions = None, damage: str = None):
        a = Attack(desc, action, damage)
        self._ranged.append(a)

    def offensive_ability(self, name: str, action: Actions = None, trigger: str = None, effect: str = None,
                          desc: str = None, frequency: str = None):
        a = Ability(name, action, trigger, effect, desc, frequency)
        self._offensive_abilities.append(a)


class Hazard(NPC):
    def __init__(self, name: str, lvl: int = 0) -> None:
        super().__init__(name, lvl)
        self._stealth = None
        self._routine = None
        self._description = None
        self._disable = None
        self._hardness = None
        self._reset = None

    def stealth(self, stealth: str):
        self._stealth = stealth

    def description(self, desc: str):
        self._description = desc

    def disable(self, disable: str):
        self._disable = disable

    def hardness(self, hardness: str, hp: str, bt: str, part=None):
        self._hardness = Hardness(hardness, part, hp, bt)

    def routine(self, desc: str):
        self._routine = desc

    def reset(self, reset: str):
        self._reset = reset


class Creature(NPC):
    def __init__(self, name: str, lvl: int = 0) -> None:
        super().__init__(name, lvl)

        self._languages = None
        self._skills = None
        self._hp = None
        self._items = []
        self._interaction_abilities = []

        self._automatic_abilities = []

        self._spell_groups = []

    def languages(self, languages: str):
        self._languages = languages

    def skills(self, *skills):
        self._skills = skills

    def attrs(self, *attrs):
        self._attrs = attrs

    def item(self, item: str, magic: bool = False):
        self._items.append((item, magic))

    def hp(self, hp: str):
        self._hp = hp

    def interaction_ability(self, name: str, action: Actions = None, desc: str = None, trigger: str = None,
                            effect: str = None, frequency: str = None):
        a = Ability(name, action, trigger, effect, desc, frequency)
        self._interaction_abilities.append(a)

    def speed(self, speed: str):
        self._speed = speed

    def spell_group(self, name: str, desc=None, dc=None) -> SpellGroup:
        sg = SpellGroup(name, dc, desc)
        self._spell_groups.append(sg)
        return sg

from enum import Enum


class Actions(Enum):
    FREE = 0
    REACTION = -1
    ONE = 1
    TWO = 2
    THREE = 3


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
    def to_level(cls, lvl: int) -> str:
        lvl_str = cls.levels.get(lvl, f"{lvl}th")
        return lvl_str

    def __init__(self, lvl: int, is_cantrip: bool = False) -> None:
        self._spells = []
        lvl_str = self.to_level(lvl)
        self._lvl = f"Cantrips ({lvl_str})" if is_cantrip else lvl_str

    def spell(self, name, id=None):
        self._spells.append(Spell(name, id=id))


class SpellGroup(object):
    def __init__(self, name: str, dc: int, desc: str) -> None:
        self._name = name
        self._desc = desc
        self._dc = dc
        self._spells = []

    def spells(self, lvl: int, is_cantrip: bool = False) -> Spells:
        spells = Spells(lvl, is_cantrip=is_cantrip)
        self._spells.append(spells)
        return spells


class Creature(object):
    def __init__(self, name: str, lvl: int = 0) -> None:
        self._name = name
        self._lvl = lvl

        self._languages = None
        self._skills = None
        self._items = []
        self._interaction_abilities = []

        self._ac = None
        self._saves = None

        self._hp = None
        self._immunities = None
        self._weaknesses = None
        self._resistances = None

        self._automatic_abilities = []
        self._reactive_abilities = []

        self._melees = []
        self._ranged = []
        self._spell_groups = []

        self._offensive_abilities = []

    def traits(self, *traits) -> None:
        self._traits = list(traits)

    def perception(self, perception: str):
        self._perception = perception

    def languages(self, languages: str):
        self._languages = languages

    def skills(self, *skills):
        self._skills = skills

    def attrs(self, *attrs):
        self._attrs = attrs

    def ac(self, ac: str):
        self._ac = ac

    def saves(self, *saves):
        self._saves = saves

    def hp(self, hp: str):
        self._hp = hp

    def immunities(self, immunities: str):
        self._immunities = immunities

    def weaknesses(self, weaknesses: str):
        self._weaknesses = weaknesses

    def resistances(self, resistances: str):
        self._resistances = resistances

    def item(self, item: str, magic: bool = False):
        self._items.append((item, magic))

    def reactive_ability(self, name: str, action: Actions = None, desc: str = None, trigger: str = None, effect: str = None,
                         frequency: str = None):
        self._reactive_abilities.append({"name": name, "action": action, "trigger": trigger, "effect": effect,
                                         "desc": desc, "frequency": frequency})

    def interaction_ability(self, name: str, action: Actions = None, desc: str = None, trigger: str = None,
                            effect: str = None, frequency: str = None):
        self._interaction_abilities.append({"name": name, "action": action, "trigger": trigger, "effect": effect,
                                            "desc": desc, "frequency": frequency})

    def speed(self, speed: str):
        self._speed = speed

    def melee(self, desc: str, action: Actions = None, damage: str = None):
        self._melees.append({"desc": desc, "action": action, "damage": damage})

    def ranged(self, desc: str, action: Actions = None, damage: str = None):
        self._ranged.append({"desc": desc, "action": action, "damage": damage})

    def offensive_ability(self, name: str, action: Actions = None, trigger: str = None, effect: str = None,
                          desc: str = None, frequency: str = None):
        self._offensive_abilities.append({"name": name, "action": action, "trigger": trigger, "effect": effect,
                                          "desc": desc, "frequency": frequency})

    def spell_group(self, name: str, dc: int, desc: str) -> SpellGroup:
        sg = SpellGroup(name, dc, desc)
        self._spell_groups.append(sg)
        return sg

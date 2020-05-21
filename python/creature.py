from enum import Enum


class Actions(Enum):
    FREE = 0
    REACTION = -1
    ONE = 1
    TWO = 2
    THREE = 3


class Creature(object):
    def __init__(self, name: str, lvl: int = 0) -> None:
        self._name = name
        self._lvl = lvl
        self._interaction_abilities = []
        self._offensive_abilities = []
        self._melees = []
        self._ranged = []

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

    def interaction_ability(self, name: str, action: Actions = None, trigger: str = None, effect: str = None,
                            frequency: str = None):
        self._interaction_abilities.append({"name": name, "action": action, "trigger": trigger, "effect": effect,
                                            "frequency": frequency})

    def speed(self, speed: str):
        self._speed = speed

    def melee(self, desc: str, action: Actions = None, damage: str = None):
        self._melees.append({"desc": desc, "action": action, "damage": damage})

    def ranged(self, desc: str, action: Actions = None, damage: str = None):
        self._ranged.append({"desc": desc, "action": action, "damage": damage})

    def offensive_ability(self, name: str, action: Actions = None, trigger: str = None, effect: str = None,
                          desc: str = None, frequency: str = None):
        self._offensive_abilities.append({"name": name, "action": action, "trigger": trigger, "effect": effect,
                                          "frequency": frequency})

    def __str__(self) -> str:
        return "str creature " + self._name

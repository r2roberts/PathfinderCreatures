import creature
from creature import Actions

from lxml import etree

E = etree.Element
SE = etree.SubElement

actions = {Actions.REACTION: "r0", Actions.FREE: "a0",
           Actions.ONE: "a1", Actions.TWO: "a2", Actions.THREE: "a3"}


def to_html(creature: creature.Creature) -> str:
    docstr = "<!doctype html>"
    html = E("html", lang="en")
    add_head(html, creature)
    body = SE(html, "body")
    add_creature(body, creature)

    return docstr + "\n" + etree.tostring(html, pretty_print=True).decode("utf-8")


def add_creature(body, c):
    creature = SE(body, "creature")
    name = SE(creature, "name")
    name.text = c._name
    level = SE(creature, "level")
    level.text = str(c._lvl)
    stats = SE(creature, "stats")
    traits = SE(stats, "traits")
    list(map(lambda x: add_trait(traits, x), c._traits))
    perception = SE(stats, "perception")
    perception.text = c._perception
    if c._languages is not None:
        languages = SE(stats, "languages")
        languages.text = c._languages
    skills = SE(stats, "skills")
    add_skills(skills, c._skills)
    add_attributes(stats, c._attrs)
    add_items(stats, c._items)

    stats = SE(creature, "stats")
    add_ac_saves(stats, c._ac, c._saves)
    add_hp_immunities(stats, c._hp, c._immunities)
    add_abilities(stats, c._interaction_abilities)

    stats = SE(creature, "stats")
    speed = SE(stats, "speed")
    speed.text = c._speed
    add_melee(stats, c._melees)
    add_ranged(stats, c._ranged)

    add_spells(stats)

    add_abilities(stats, c._offensive_abilities)


def add_spells(elem):
    pass


def add_ranged(elem, ranged):
    add_attack("ranged", elem, ranged)


def add_melee(elem, melees):
    add_attack("melee", elem, melees)


def add_attack(tag, elem, attacks):
    for a in attacks:
        a_e = SE(elem, tag)
        delim = ", " if a.get("damage") is not None else ""

        if a.get("action") is not None:
            ac_e = SE(a_e, actions[a["action"]])
            ac_e.text = ""
            ac_e.tail = a["desc"] + delim
        else:
            a_e.text = a["desc"] + delim
        if a.get("damage") is not None:
            d_e = SE(a_e, "damage")
            d_e.text = a["damage"]


def add_abilities(elem, abililties):

    for a in abililties:
        rule = SE(elem, "rule", name=a["name"])
        tail = None
        if a.get("action") is not None:
            a_i = SE(rule, actions[a["action"]])
            a_i.text = ""
            tail = a_i
        if a.get("trigger") is not None:
            trigger = SE(rule, "trigger")
            trigger.text = a["trigger"]
            tail = trigger
        if a.get("frequency") is not None:
            freq = SE(rule, "frequency")
            freq.text = a["frequency"] + "; "
            tail = freq
        if a.get("effect") is not None:
            ef = SE(rule, "effect")
            ef.text = a["effect"]
            tail = ef
        if a.get("desc") is not None:
            if tail is None:
                rule.text = a["desc"]
            else:
                tail.tail = a["desc"]


def add_hp_immunities(elem, hp, immunities):
    rule = SE(elem, "rule")
    hp_e = SE(rule, "hp")
    hp_e.text = hp
    i_e = SE(rule, "immunities")
    i_e.text = immunities


def add_ac_saves(elem, ac, saves):
    div = SE(elem, "div")
    ac_e = SE(div, "ac")
    ac_e.text = ac
    for s in saves:
        tag, val = s.split(" ")
        e = SE(div, tag)
        e.text = val


def add_items(elem, items):
    if items is not None:
        e = SE(elem, "items")
        e.text = items


def add_attributes(elem, attrs):
    for a in attrs:
        tag = a[0:3]
        val = a[4:]
        e = SE(elem, tag)
        e.text = val


def add_skills(elem, skills):
    comma_skills = [x + "," for x in skills]
    comma_skills[-1] = skills[-1]

    def add_skill(x):
        sk = SE(elem, "skill")
        sk.text = x

    list(map(add_skill, comma_skills))


def add_trait(traits, trait):
    rareities = ["uncommon", "rare", "unique"]
    sizes = ["small", "medium", "large", "huge", "gargantuan"]
    alignments = ["lg", "ln", "le", "ng", "n", "ne", "cg", "cn", "ce"]
    trait_tag_map = {r: r for r in rareities}
    trait_tag_map.update({s: "size" for s in sizes})
    trait_tag_map.update({a: "alignment" for a in alignments})
    tag = trait_tag_map.get(trait.lower(), "trait")
    t = SE(traits, tag)
    t.text = trait


def add_head(html, c):
    head = SE(html, "head")
    SE(head, "meta", charset="UTF-8")
    SE(head, "meta", name="viewport",
       content="width=device-width, initial-scale=1.0")
    title = SE(head, "title")
    title.text = c._name
    SE(head, "link", rel="stylesheet", href="CSS/creatures.css")
    script = SE(head, "script", src="js/creatures.js")
    script.text = ""

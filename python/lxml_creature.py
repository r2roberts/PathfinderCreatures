import creature
from creature import Actions

from lxml import etree

E = etree.Element
SE = etree.SubElement

actions = {Actions.REACTION: "r0", Actions.FREE: "a0",
           Actions.ONE: "a1", Actions.TWO: "a2", Actions.THREE: "a3"}


def to_html(c: creature.NPC) -> str:
    docstr = "<!doctype html>"
    html = E("html", lang="en")
    add_head(html, c)
    body = SE(html, "body")
    if isinstance(c, creature.Creature):
        add_creature(body, c)
    elif isinstance(c, creature.Hazard):
        add_hazard(body, c)

    return docstr + "\n" + etree.tostring(html, pretty_print=True).decode("utf-8")


def add_hazard(body, h):
    hazard = SE(body, "hazard")
    name = SE(hazard, "name")
    name.text = h._name
    level = SE(hazard, "level")
    level.text = str(h._lvl)
    stats = SE(hazard, "stats")
    traits = SE(stats, "traits")
    list(map(lambda x: add_trait(traits, x), h._traits))

    if h._perception is not None:
        perception = SE(stats, "perception")
        perception.text = h._perception

    add_stealth(stats, h._stealth)
    add_description(stats, h._description)

    stats = SE(hazard, "stats")
    add_disable(stats, h._disable)
    add_ac_saves(stats, ac=h._ac, saves=h._saves, saves_desc=h._saves_desc)
    add_hardness(stats, hardness=h._hardness, immunities=h._immunities,
                 weaknesses=h._weaknesses, resistances=h._resistances)
    add_abilities(stats, h._reactive_abilities)

    if h._routine is not None:
        stats = SE(hazard, "stats")
        add_routine(stats, h._routine)

    add_melee(stats, h._melees)
    add_ranged(stats, h._ranged)

    add_abilities(stats, h._offensive_abilities)

    if h._reset is not None:
        stats = SE(hazard, "stats")
        add_reset(stats, h._reset)


def add_disable(elem, disable):
    disable_e = SE(elem, "disable")
    disable_e.text = disable


def add_reset(elem, reset):
    rule = SE(elem, "rule", name="Reset")
    rule.text = reset


def add_actions(elem, actions):
    for a in actions:
        a_e = SE(elem, "rule", name=a["name"])


def add_routine(elem, routine):
    rule = SE(elem, "rule", name="Routine")
    rule.text = routine


def add_hardness(elem, *, hardness, immunities, weaknesses, resistances):

    h = hardness
    name = h.part + " " if h.part else ""
    name += "Hardness"
    rule = SE(elem, "rule", name=name)
    rule.text = h.hardness
    sp = SE(rule, "span")
    sp.text = "; "
    hp_el = SE(rule, "HP")
    hp_el.text = h.hp + f" (BT {h.bt})" if h.bt else ""
    sp = SE(rule, "span")
    sp.text = " "
    if h.desc is not None:
        i_e = SE(rule, "span")
        i_e.text = h.desc + "; "
    if immunities is not None:
        i_e = SE(rule, "immunities")
        i_e.text = immunities
    if weaknesses is not None:
        w_e = SE(rule, "weaknesses")
        w_e.text = weaknesses
    if resistances is not None:
        r_e = SE(rule, "resistances")
        r_e.text = resistances


def add_stealth(elem, stealth):
    rule = SE(elem, "rule", name="Stealth")
    rule.text = stealth


def add_description(elem, description):
    rule = SE(elem, "rule", name="Description")
    rule.text = description


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
    add_abilities(stats, c._ability_modifiers)
    add_items(stats, c._items)
    add_abilities(stats, c._interaction_abilities)

    stats = SE(creature, "stats")
    add_ac_saves(stats, ac=c._ac, saves=c._saves, saves_desc=c._saves_desc)
    add_hp_immunities(stats, c._hp, c._immunities,
                      c._weaknesses, c._resistances)
    add_abilities(stats, c._automatic_abilities)
    add_abilities(stats, c._reactive_abilities)

    stats = SE(creature, "stats")
    speed = SE(stats, "speed")
    speed.text = c._speed
    add_melee(stats, c._melees)
    add_ranged(stats, c._ranged)

    add_spell_groups(stats, c._spell_groups)

    add_abilities(stats, c._offensive_abilities)


def add_spell_groups(elem, spell_groups):
    def add_spells(elem, spells):
        last_el = None
        for sp in spells._spells:
            sp_e = SE(sps_e, "spell")
            sp_e.text = sp._name
            sp_e.tail = " "
            last_el = sp_e
            if sp._id is not None:
                sp_e.set("spellId", sp._id)
            if sp._desc is not None:
                sp_ee = SE(sps_e, "span")
                sp_ee.text = " " + sp._desc
                sp_ee.tail = ", "
                last_el = sp_ee
            else:
                sp_e.tail = ", "
        if last_el is not None:
            last_el.tail = ';'

    for sg in spell_groups:
        rule = SE(elem, "rule", name=sg._name)
        if sg._dc is not None:
            dc_e = SE(rule, "dc")
            dc_e.text = str(sg._dc) + ", "

        if sg._desc is not None:
            sp = SE(rule, "span")
            sp.text = sg._desc + "; "

        for sps in sg._spells:
            sps_e = SE(rule, "spells")
            if sps._lvl is not None:
                sps_e.set("level", sps._lvl)
            add_spells(sps_e, sps)


def add_ranged(elem, ranged):
    add_attack("ranged", elem, ranged)


def add_melee(elem, melees):
    add_attack("melee", elem, melees)


def add_attack(tag, elem, attacks):
    for a in attacks:
        a_e = SE(elem, tag)
        delim = ", " if a.damage is not None else ""

        if a.action is not None:
            ac_e = SE(a_e, actions[a.action])
            ac_e.text = ""
        s_e = SE(a_e, "span")
        s_e.text = a.desc + delim
        if a.damage is not None:
            d_e = SE(a_e, "damage")
            d_e.text = a.damage


def add_abilities(elem, abililties):

    for a in abililties:
        rule = SE(elem, "rule", name=a.name)
        if a.action is not None:
            a_i = SE(rule, actions[a.action])
            a_i.text = ""
        if a.desc is not None:
            sp = SE(rule, "span")
            sp.text = a.desc
        if a.requirements is not None:
            requirements = SE(rule, "requirements")
            requirements.text = a.requirements
        if a.trigger is not None:
            trigger = SE(rule, "trigger")
            trigger.text = a.trigger
        if a.frequency is not None:
            freq = SE(rule, "frequency")
            freq.text = a.frequency + "; "
        if a.effect is not None:
            ef = SE(rule, "effect")
            ef.text = a.effect


def add_hp_immunities(elem, hp, immunities, weaknesses, resistances):
    rule = SE(elem, "rule")
    hp_e = SE(rule, "hp")
    hp_e.text = hp
    if immunities is not None:
        i_e = SE(rule, "immunities")
        i_e.text = immunities
    if weaknesses is not None:
        w_e = SE(rule, "weaknesses")
        w_e.text = weaknesses
    if resistances is not None:
        r_e = SE(rule, "resistances")
        r_e.text = resistances


def add_ac_saves(elem, *, ac, saves, saves_desc):
    div = SE(elem, "div")
    ac_e = SE(div, "ac")
    ac_e.text = ac
    for s in saves:
        tag, val = s.split(" ")
        e = SE(div, tag)
        e.text = val
    if saves_desc is not None:
        e = SE(div, "span")
        e.text = saves_desc


def add_items(elem, items):
    if len(items) != 0:
        e = SE(elem, "items")
        item_str = ""
        for item in items:
            if item[1]:
                m_e = SE(e, "magic")
                m_e.text = item[0]
            else:
                m_e = SE(e, "span")
                m_e.text = item[0]


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
    SE(head, "link", rel="stylesheet", href="../CSS/creatures.css")
    script = SE(head, "script", src="../js/creatures.js")
    script.text = ""

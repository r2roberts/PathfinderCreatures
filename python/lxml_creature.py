import creature
from lxml import etree

E = etree.Element
SE = etree.SubElement


def to_html(creature: creature.Creature) -> str:
    html = E("html", lang="en")
    add_head(html)
    body = SE(html, "body")
    add_creature(body, creature)

    return etree.tostring(html, pretty_print=True).decode("utf-8")


def add_creature(body, c):
    creature = SE(body, "creature")
    name = SE(creature, "name")
    name.text = c._name
    level = SE(creature, "level")
    level.text = str(c._lvl)
    stats = SE(creature, "stats")
    traits = SE(stats, "traits")
    print("c._traits", c._traits)
    list(map(lambda x: add_trait(traits, x), c._traits))


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


def add_head(html):
    head = SE(html, "head")
    SE(head, "meta", charset="UTF-8")
    SE(head, "meta", name="viewport",
       content="width=device-width, initial-scale=1.0")
    title = SE(head, "title")
    title.text = "Charau-ka Dragon Priest"
    SE(head, "link", rel="stylesheet", href="CSS/creatures.css")
    SE(head, "script", src="js/creatures.js")

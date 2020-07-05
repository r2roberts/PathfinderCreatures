import creature
from creature import Actions

c = creature.Hazard("TREE OF DREADFUL DREAMS", lvl=10)
c.traits("RARE", "COMPLEX", "MAGICAL", "TRAP")
c.stealth("+22 (expert)")

c.description(
    "The statue of the willow tree animates, its branches lashing out to try to grab anyone in area B2.")

c.disable("Athletics or Thievery DC 25 (trained) to force or lever open a single branch, disabling that branch and freeing any creature trapped within. Thievery DC 29 (expert) to disrupt the tree’s magical animation, shut it down, and free all trapped creatures. Placing a dreamstone in the tree’s trunk takes 2 Interact actions and causes the trap to shut down, freeing all trapped creatures. Placing the cursed dreamstone from area B4 in the trunk instead increases the tree’s actions per turn to 4 and gives it a +2 item bonus to all saving throws and attack rolls.")

c.ac("30")
c.saves("Fort +22", "Ref +14")
c.hardness("10", part="Branch", hp="40", bt="20", desc="to break each branch")
c.immunities("critical hits, object immunities, precision damage")
c.reactive_ability("Attack of Opportunity", Actions.REACTION,
                   desc="The tree of dreadful dreams can attempt up to six Attacks of Opportunity each round.")
c.routine("(3 actions) The statue uses each action to attempt a branch Strike against a random creature in the room that it hasn’t grabbed. If there are no creatures for it to attack and it has at least one creature grabbed, it instead Constricts. The trap can have up to six creatures grabbed.")

c.melee("branch +26 (reach 20 feet)", Actions.ONE,
        damage="2d10+12 bludgeoning plus the target is grabbed by the tree; no multiple attack penalty")

c.offensive_ability("Constrict", Actions.ONE,
                    desc="1d10+12 bludgeoning, DC 27")
c.offensive_ability("Terrifying Visions", desc="A creature that begins its turn grabbed by the trap experiences vivid, warped visions of true events and must succeed at a DC 31 Will save or take 4d8 mental damage. On a critical failure, the creature also becomes doomed 1. A creature that succeeds at its save is temporarily immune for 24 hours.")

c.reset("The trap deactivates and resets if it has no creatures grabbed and no creatures in the room to attack. If an uncursed dreamstone is placed in its trunk, the statue doesn’t reactivate.")

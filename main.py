import getch
import random

from minions import minions
from dragons import dragons

# TODO
#
# Randomize Weapon drops within defined range
# Equip gear option with comparison
# GUI with healthbar, buttons, hotkeys
# Repeat last action with <Enter>


def end_game():
    print("Game Over.")
    exit()


class Knight:
    def __init__(self, name):
        self.name = name
        self.max_health = self.curr_health = 100
        self.attack = 10
        self.armor = {
            'name': 'Body Paint',
            'type': 'armor',
            'armor': 0
        }
        self.level = 1
        self.experience = 0
        self.gold = 0
        self.curr_tier = 0
        self.crit_chance = 10
        self.crit_multiplier = 1.5
        self.weapon = {
            'name': 'Boxing Gloves',
            'type': 'weapon',
            'damage': 0,
            'crit_chance': 0,
            'crit_multiplier': 0,
        }
        self.levels = [0, 20, 50, 100, 200, 500, 1000, 1500, 2000, 2500, 3000, 4000, 5250, 6500, 7750, 10000, 100000]

    def take_damage(self, damage):
        self.curr_health -= damage

    def gain_experience(self, xp_points):
        self.experience += xp_points
        if self.experience > self.levels[self.level]:
            self.level_up()

    def level_up(self):
        health_gain = 25
        attack_gain = 5
        self.max_health += health_gain
        self.curr_health = self.max_health
        self.attack += attack_gain
        self.level += 1
        self.stat_sheet()

    def full_heal(self):
        self.curr_health = self.max_health
        print(f"Health: {self.curr_health}/{self.max_health}")

    def stat_sheet(self):
        print(f"""
            {self.name}, the level {self.level} Knight
            Health: {self.curr_health}/{self.max_health}
            Armor: {self.armor['name']}
            Defense: {self.armor['armor']}
            Weapon: {self.weapon['name']}
            Attack: {self.attack + self.weapon['damage']}
            Crit: {self.crit_chance + self.weapon['crit_chance']}% for {(self.crit_multiplier + self.weapon['crit_multiplier'])*100}%
        """)



def roll_damage(dmg, crit_chance, crit_multiplier):
    if random.randrange(0, 100) <= crit_chance:
        return dmg * crit_multiplier
    else:
        return dmg


def loot_corpse(drop_table):
    loot = []
    for gear in drop_table:
        if random.randrange(0, 100) <= gear['drop_chance']:
            loot.append(gear)
            print(f'{Knight.name} found [{gear["name"]}].')
    return loot


def equip_gear(bag_of_gear):
    for gear in bag_of_gear:
        if gear['type'] == 'weapon':
            Knight.weapon = gear
        if gear['type'] == 'armor':
            Knight.armor = gear


def combat(enemy):
    enemy = enemy[Knight.curr_tier]
    enemy_name = enemy['name']
    enemy_health = enemy_max_health = enemy['health']
    enemy_attack = enemy['attack']
    xp_reward = enemy['xp_reward']
    gold_reward = enemy['gold_reward']

    print(f"\n{Knight.name}({Knight.curr_health}/{Knight.max_health}) engages {enemy_name} in combat.\n")

    calculated_damage = roll_damage(Knight.attack + Knight.weapon['damage'],
                                    Knight.crit_chance + Knight.weapon['crit_chance'],
                                    Knight.crit_multiplier + Knight.weapon['crit_multiplier'])
    print(f"{Knight.name} slices {enemy_name} for {int(calculated_damage)} damage.")

    enemy_health -= calculated_damage

    while enemy_health > 0 and Knight.curr_health > 0:
        print(f"{enemy_name.capitalize()} slices {Knight.name} for {enemy_attack - Knight.armor['armor']} damage.")
        Knight.take_damage(enemy_attack - Knight.armor['armor'])

        calculated_damage = roll_damage(Knight.attack + Knight.weapon['damage'],
                                        Knight.crit_chance + Knight.weapon['crit_chance'],
                                        Knight.crit_multiplier + Knight.weapon['crit_multiplier'])
        print(f"{Knight.name} slices {enemy_name} for {int(calculated_damage)} damage.")

        enemy_health -= calculated_damage

    if Knight.curr_health > 0:
        print(f"{Knight.name} defeats {enemy_name}. {xp_reward} XP awarded. HP: {Knight.curr_health}/{Knight.max_health}\n")
        Knight.gold += gold_reward
        # Auto equip drops
        equip_gear(loot_corpse(enemy['loot']))
        Knight.gain_experience(xp_reward)
    else:
        print(f"{Knight.name} has been slain by {enemy_name}({enemy_health/enemy_max_health}).\n")
        exit()


def game_loop():
    # option = input("(A)Attack (S)Sleep (D)Dragon (Q)Equip (W)Sell (E)Shop:")
    new_name = input("Enter your name:")
    if new_name == "": new_name = "Gerald"
    Knight.name = new_name
    Knight.stat_sheet()

    print("(A)Attack (S)Sleep (D)Dragon (Q)Equip (W)Sell (E)Shop")
    option = getch.getch()

    if option == 'A' or option == 'a':
        combat(minions)

    elif option == 'S' or option == 's':
        print(f"{Knight.name} makes camp.\n")
        Knight.curr_health = Knight.max_health

    elif option == 'D' or option == 'd':
        combat(dragons)
        Knight.curr_tier += 1
        # print(f"{Knight.name} Health:", Knight.curr_health, " | XP:", Knight.experience)

    elif option == 'Q' or option == 'q':
        # print("Equipping!")
        Knight.stat_sheet()

    elif option == 'W' or option == 'w':
        print("Selling!")

    elif option == 'E' or option == 'e':
        print("Shopping!")

    else:
        print("Incorrect option")
        # exit()

    game_loop()


Knight = Knight('Gerald')

game_loop()

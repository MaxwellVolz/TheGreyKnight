# import getch
import msvcrt
import random

from minions import minions
from dragons import dragons
from shop import shop


# TODO
#
# Randomize Weapon drops within defined range
# Inventory List
# Shop
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
            'price': 1,
            'action_name': 'punches'
        }
        self.inventory = []
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
            Crit: {self.crit_chance + self.weapon['crit_chance']}% for {(self.crit_multiplier + self.weapon['crit_multiplier']) * 100}%
            Gold: {self.gold}
            Inventory: {[x['name'] for x in self.inventory]}""")


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


def equip_gear(curr_Knight, bag_of_gear):
    for gear in bag_of_gear:
        if gear['type'] == 'weapon':

            if gear['name'] == Knight.weapon['name']:
                Knight.inventory.append(Knight.weapon)
                break
            # Compare
            print(f"""
(A) Replace:[{curr_Knight.weapon["name"]}]: 
    {curr_Knight.weapon["damage"]} dmg  +{curr_Knight.weapon["crit_chance"]}% chance to +crit %{curr_Knight.weapon["crit_multiplier"]} 
    
(D) With: [{gear["name"]}]: 
    {gear["damage"]} dmg  +{gear["crit_chance"]}% chance to +crit %{gear["crit_multiplier"]} """)

            option = msvcrt.getch()
            if option == 'A' or option == 'a' or option == b'a' or option == b'A':
                Knight.inventory.append(gear)

            elif option == 'D' or option == 'd' or option == b'd' or option == b'D':
                Knight.inventory.append(Knight.weapon)
                Knight.weapon = gear


        if gear['type'] == 'armor':
            if gear['name'] == Knight.armor['name']:
                Knight.inventory.append(Knight.armor)
                break

            # Compare
            print(f"""
(A) Replace [{curr_Knight.armor["name"]}]: {curr_Knight.armor["armor"]} armor
(D) With    [{gear["name"]}]: {gear["armor"]} armor
""")
            option = msvcrt.getch()
            if option == 'A' or option == 'a' or option == b'a' or option == b'A':
                Knight.inventory.append(gear)
                print(f'\n{Knight.name} equips [{gear["name"]}].\n')

            elif option == 'D' or option == 'd' or option == b'd' or option == b'D':
                Knight.inventory.append(Knight.armor)
                Knight.armor = gear
                print(f'\n{Knight.name} equips [{gear["name"]}].\n')


def sell_inventory():
    print('\n')
    total_sell_value = 0
    for item in Knight.inventory:
        try:
            total_sell_value += item['price']
            print(f'{Knight.name} sold {item["name"]} for {item["price"]}')
        except (NameError, KeyError):
            print(f'{Knight.name} donated their old {item["name"]}')
    Knight.inventory = []
    Knight.gold += total_sell_value


def open_shop():
    print(f'\nWelcome again to my humble shop. Please buy something so I can feed my kids. Looks like you have {Knight.gold} gold coins.\n')
    for index, gear in enumerate(shop[Knight.curr_tier]):
        if gear['type'] == 'armor':
            print(f'({index})   [{gear["name"]}]: {gear["armor"]} armor | Cost: {gear["cost"]}')
        if gear['type'] == 'weapon':
            print(f'({index})   [{gear["name"]}]: {gear["damage"]} dmg  +{gear["crit_chance"]}% chance to +crit %{gear["crit_multiplier"]}  | Cost: {gear["cost"]}')

    print("\n(Q)Leave (W)Sell (1-9)Buy")
    option = msvcrt.getch()

    if option == 'Q' or option == 'q' or option == b'q' or option == b'Q':
        return

    if option == 'W' or option == 'w' or option == b'w' or option == b'W':
        sell_inventory()
        open_shop()

    buy_option = -1
    try:
        buy_option = int(option.decode("utf-8"))
    except ValueError:
        return

    if buy_option  in (0,1,2,3,4,5,6,7,8,9):
        cost_of_item = 0
        try:
            cost_of_item = shop[Knight.curr_tier][int(option)]['cost']
        except IndexError:
            print("That is no item! That is my cat!")

        if Knight.gold > cost_of_item:
            Knight.gold -= cost_of_item

            try:
                equip_gear(Knight, [shop[Knight.curr_tier][int(option)]])
            except IndexError:
                print("That is no item! That is my cat!")
        else:
            print("\nYou can\'t afford that, peasant! Get out of here!\n")
        
        
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
    print(f"{Knight.name} {Knight.weapon['action_name']} {enemy_name} for {int(calculated_damage)} damage.")

    enemy_health -= calculated_damage

    while enemy_health > 0 and Knight.curr_health > 0:
        print(f"{enemy_name.capitalize()} attacks {Knight.name} for {enemy_attack - Knight.armor['armor']} damage.")
        Knight.take_damage(enemy_attack - Knight.armor['armor'])

        calculated_damage = roll_damage(Knight.attack + Knight.weapon['damage'],
                                        Knight.crit_chance + Knight.weapon['crit_chance'],
                                        Knight.crit_multiplier + Knight.weapon['crit_multiplier'])

        print(f"{Knight.name} {Knight.weapon['action_name']} {enemy_name} for {int(calculated_damage)} damage.")

        enemy_health -= calculated_damage

    if Knight.curr_health > 0:
        print(f"\n{Knight.name} defeats {enemy_name}. {xp_reward} XP awarded. HP: {Knight.curr_health}/{Knight.max_health}")
        Knight.gold += gold_reward

        equip_gear(Knight, loot_corpse(enemy['loot']))
        Knight.gain_experience(xp_reward)

    # If enemy killed but Knight dies, Knight lives on
    elif enemy_health < 0:
        Knight.curr_health = 1
        print(f"{Knight.name} barely defeats {enemy_name}. {xp_reward}*2 XP awarded. HP: {Knight.curr_health}/{Knight.max_health}")
        Knight.gold += gold_reward

        # Auto equip drops
        equip_gear(Knight, loot_corpse(enemy['loot']))
        Knight.gain_experience(xp_reward*2)

    else:
        print(f"\n{Knight.name} has been slain by {enemy_name}({enemy_health}/{enemy_max_health}).\n")
        exit()


def game_loop():
    # option = input("(A)Attack (S)Sleep (D)Dragon (Q)Equip (W)Sell (E)Shop:")

    print("\n(A)Attack (S)Sleep (D)Dragon (Q)Stats (W)Sell (E)Shop")
    # option = getch.getch()
    option = msvcrt.getch()

    if option == 'A' or option == 'a' or option == b'a' or option == b'A':
        combat(minions)

    elif option == 'S' or option == 's' or option == b's' or option == b'S':
        print(f"{Knight.name} makes camp.")
        Knight.curr_health = Knight.max_health

    elif option == 'D' or option == 'd' or option == b'd' or option == b'D':
        combat(dragons)
        Knight.curr_tier += 1
        if Knight.curr_tier == 3:
            Knight.stat_sheet()
            print(f"\n{Knight.name}, the Supreme Hero, has completed speciocide on dragons.\n")
            exit()
        # print(f"{Knight.name} Health:", Knight.curr_health, " | XP:", Knight.experience)

    elif option == 'Q' or option == 'q' or option == b'q' or option == b'Q':
        Knight.stat_sheet()

    elif option == 'W' or option == 'w' or option == b'w' or option == b'W':
        sell_inventory()

    elif option == 'E' or option == 'e' or option == b'e' or option == b'E':
        open_shop()

    elif option == 'X' or option == 'x' or option == b'x' or option == b'X':
        exit()

    else:
        print("Incorrect option:", option)
        # exit()

    game_loop()



print("""
Welcome to The Grey Knight.
Genre: Permadeath, RPG, Roguelike, Zombies


Your home and the nearby villages are under attack! Defeat minions to sharpen your blade, become a beefcake, and slay the dragon!
""")

new_name = input("Enter your name:")
if new_name == "": new_name = "Gerald"
Knight = Knight(new_name)
Knight.stat_sheet()

game_loop()

import getch
import random

from minions import minions
from dragons import dragons


def end_game():
    print("Game Over.")
    exit()


class Knight:
    def __init__(self, name):
        self.name = name
        self.max_health = self.curr_health = 100
        self.attack = 10
        self.armor = 0
        self.level = 1
        self.experience = 0
        self.gold = 0
        self.curr_tier = 0
        self.levels = [0, 20, 50, 100, 200, 500, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 6000, 7000, 8000, 10000]

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
        print(f"{self.name} is now level {self.level}. HP:", self.max_health, " | Attack:", self.attack, "\n")

    def full_heal(self):
        self.curr_health = self.max_health
        print(f"Health: {self.curr_health}/{self.max_health}")

    def stat_sheet(self):
        print(f"""
            {self.name}, the level {self.level} Knight
            Health: {self.curr_health}/{self.max_health}
            Armor: {self.armor}
            Attack: {self.attack}
        """)


Knight = Knight('Gerald')
Knight.stat_sheet()


def combat(enemy):
    enemy = enemy[Knight.curr_tier]
    enemy_name = enemy['name']
    enemy_health = enemy_max_health = enemy['health']
    enemy_attack = enemy['attack']
    xp_reward = enemy['xp_reward']
    gold_reward = enemy['gold_reward']

    print(f"\n{Knight.name} engages {enemy_name} in combat.\n")

    enemy_health = enemy_health - Knight.attack

    while enemy_health > 0 and Knight.curr_health > 0:
        # curr_player_health = curr_player_health - enemy_attack
        Knight.take_damage(enemy_attack)
        print(f"{Knight.name}: {Knight.curr_health}/{Knight.max_health} "
              f"| {enemy_name}: {enemy_health}/{enemy_max_health}")
        enemy_health -= Knight.attack

    if Knight.curr_health > 0:
        print(f"{Knight.name} defeats {enemy_name}. {xp_reward} XP awarded.\n")
        Knight.gain_experience(xp_reward)
        Knight.gold += gold_reward
    else:
        print(f"{Knight.name} has been slain.\n")
        exit()


def game_loop(curr_player_health):
    # option = input("(A)Attack (S)Sleep (D)Dragon (Q)Equip (W)Sell (E)Shop:")

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
        print("Equipping!")

    elif option == 'W' or option == 'w':
        print("Selling!")

    elif option == 'E' or option == 'e':
        print("Shopping!")

    else:
        print("Incorrect option")
        # exit()

    game_loop(Knight.curr_health)


game_loop(Knight.curr_health)

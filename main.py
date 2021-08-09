import getch

tier = 0


def dead_check(health):
    if health <= 0:
        end_game()


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
        self.curr_tier = 0
        self.levels = [0, 20, 50, 100, 200, 500, 1000, 1500, 2000]

    def take_damage(self, damage):
        self.curr_health -= damage
        dead_check(self.curr_health)

    def gain_experience(self, xp_points):
        self.experience += xp_points
        if self.experience > self.levels[self.level]:
            self.level_up()

    def level_up(self):
        health_gain = 20
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


minions = {
    'name': ['a fairy', 'an elf', 'an Orc'],
    'attack': [20, 30, 35],
    'health': [30, 100, 200],
    'xp_reward': [10, 20, 30],
    'gold_reward': [1, 3, 5]
}

dragons = {
    'name': ['Brightwing', 'Charizard', 'Ragnaros'],
    'attack': [25, 30, 60],
    'health': [200, 400, 1000],
    'xp_reward': [100, 200, 300],
    'gold_reward': [10, 30, 50]
}

Knight = Knight('Gerald')
Knight.stat_sheet()


def combat(enemy):
    enemy_name = enemy['name'][Knight.curr_tier]
    enemy_health = enemy_max_health = enemy['health'][Knight.curr_tier]
    enemy_attack = enemy['attack'][Knight.curr_tier]
    xp_reward = enemy['xp_reward'][Knight.curr_tier]

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



def attacking_win():
    print("You won the battle.")


def game_loop(curr_player_health):
    # option = input("(A)Attack (S)Sleep (D)Dragon (Q)Equip (W)Sell (E)Shop:")

    print("(A)Attack (S)Sleep (D)Dragon (Q)Equip (W)Sell (E)Shop")
    option = getch.getch()

    if option == 'A' or option == 'a':
        combat(minions)


    elif option == 'S' or option == 's':
        print("Sleeping!")
        Knight.curr_health = Knight.max_health

    elif option == 'D' or option == 'd':
        print("Fighting the Dragon!")
        combat(dragons)
        Knight.curr_tier += 1
        print("Player Health:", Knight.curr_health, " | XP:", Knight.experience)

    elif option == 'Q' or option == 'q':
        print("Equipping!")

    elif option == 'W' or option == 'w':
        print("Selling!")

    elif option == 'E' or option == 'e':
        print("Shopping!")

    else:
        print("Incorrect option")
        exit()

    game_loop(Knight.curr_health)


game_loop(Knight.curr_health)

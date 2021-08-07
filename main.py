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
        self.levels = [0, 20, 50, 100, 200, 500, 1000]

    def take_damage(self, damage):
        self.curr_health -= damage
        print(f"Health: {self.curr_health}/{self.max_health}")
        dead_check(self.curr_health)

    def gain_experience(self, xp_points):
        self.experience += xp_points
        if self.experience > self.levels[self.level]:
            self.level += 1
            print(f"{self.name} is now level {self.level}.")

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
    'attack': [20, 30, 35],
    'health': [30, 70, 100],
    'xp_reward': [10, 20, 30],
}

Knight = Knight('Gerald')
Knight.stat_sheet()


def attacking(curr_player_health, enemy_health=30, enemy_attack=20):
    enemy_health = enemy_health - Knight.attack

    while enemy_health > 0 and curr_player_health > 0:
        curr_player_health = curr_player_health - enemy_attack
        enemy_health = enemy_health - Knight.attack
        print("Player Health:", curr_player_health, " | Enemy Health:", enemy_health)

    return curr_player_health


def attacking_win():
    print("You won the battle.")


def game_loop(curr_player_health):
    # option = input("(A)Attack (S)Sleep (D)Dragon (Q)Equip (W)Sell (E)Shop:")

    print("(A)Attack (S)Sleep (D)Dragon (Q)Equip (W)Sell (E)Shop")
    option = getch.getch()

    if option == 'A' or option == 'a':
        print("Attacking!")
        curr_player_health = attacking(curr_player_health)

    elif option == 'S' or option == 's':
        print("Sleeping!")
        curr_player_health = Knight.health

    elif option == 'D' or option == 'd':
        print("Dragoning!")

    elif option == 'Q' or option == 'q':
        print("Equipping!")

    elif option == 'W' or option == 'w':
        print("Selling!")

    elif option == 'E' or option == 'e':
        print("Shopping!")

    else:
        print("Incorrect option")
        exit()

    game_loop(curr_player_health)


game_loop(Knight.curr_health)

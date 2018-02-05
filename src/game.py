from src.mapArea import mapArea
from src.character import Character
import random


class Game:
    def __init__(self, win_chance=0.5):
        self.turns = 0
        self.maparea = mapArea(rows=4, cols=4, battle_cell_density=0.3)
        self.win_chance = win_chance
        self.quit_char = "q"
        self.up_key = "w"
        self.down_key = "s"
        self.left_key = "a"
        self.right_key = "d"
        self.help_char = "h"

    def print_invalid_move_message(self):
        print("\nCan't go there!")

    def print_game_over_message(self):
        print("\nGoodbye!!!")

    def do_battle(self):
        if random.random() > self.win_chance:
            xp_gain = random.randint(1, 5)
            self.player.gain_xp(xp_gain)
            print("\nYou won the battle and gained ", xp_gain, " experience points!")
        else:
            print("\nYou lost the battle!")
        pass

    def battle(self):
        current_cell = self.maparea.get_current_cell()
        if current_cell.is_battle_cell():
            user_input = input("\nA battle awaits you! Do you wish to fight? (y/n)")
            if user_input == "y":
                self.do_battle()
            elif user_input == "n":
                pass
            else:
                print("That command is not valid... Do you wish to fight? (y/n)")

    def print_help_message(self):
        print("\n\nMap legend:\n? : unexplored area\n_ : explored area\n* : your position\n! : battle area")
        print("\nKeys:\nw: move up\na: move left\ns: move down\nd: move right\nh: help\nq: quit")


    def start(self):
        player_name = input("Welcome to the labrynith where dangerous foes and glory await you! What shall you be called? ")
        self.player = Character(name=player_name)
        self.print_help_message()
        while True:
            print("\n")
            print(self.maparea)
            print(self.player)
            user_input = input("Your move: ")
            if user_input == self.up_key:
                if not self.maparea.move_up():
                    self.print_invalid_move_message()
                self.battle()
            elif user_input == self.left_key:
                if not self.maparea.move_left():
                    self.print_invalid_move_message()
                self.battle()
            elif user_input == self.down_key:
                if not self.maparea.move_down():
                    self.print_invalid_move_message()
                self.battle()
            elif user_input == self.right_key:
                if not self.maparea.move_right():
                    self.print_invalid_move_message()
                self.battle()
            elif user_input == self.help_char:
                self.print_help_message()
            elif user_input == self.quit_char:
                self.print_game_over_message()
                break
            else:
                print("Key not recognized, try again:")

    def play_turn(self):
        pass
from src.mapArea import mapArea

class Character:
    def __init__(self, name="Padawan"):
        self.name = name
        self.experience = 0
        self.quit_char = 'q'

class Game:
    def __init__(self):
        self.turns = 0
        self.maparea = mapArea(rows=3, cols=3)
        self.player = Character()
        self.quit_char = "q"
        self.up_key = "w"
        self.down_key = "s"
        self.left_key = "a"
        self.right_key = "d"

    def printInvalidMoveMessage(self):
        print("\nCan't go there!")

    def printGameOverMessage(self):
        print("\nGoodbye!!!")

    def start(self):
        print("Welcome to the game")
        print("use keys w, a, s, d to move up, left, down, right. 'q' to quit: ");
        while(True):
            print(self.maparea)
            user_input = input("\nYour move: ")
            if(user_input == self.up_key):
                if not self.maparea.move_up():
                    self.printInvalidMoveMessage()
            elif (user_input == self.left_key):
                if not self.maparea.move_left():
                    self.printInvalidMoveMessage()
            elif (user_input == self.down_key):
                if not self.maparea.move_down():
                    self.printInvalidMoveMessage()
            elif (user_input == self.right_key):
                if not self.maparea.move_right():
                    self.printInvalidMoveMessage()
            elif (user_input == self.quit_char):
                self.printGameOverMessage()
                break
            else:
                print("Key not recognized, try again:")

    def play_turn(self):
        pass


newgame = Game()
newgame.start()
class Character:
    def __init__(self, name="Padawan"):
        self.name = name
        self.experience = 0
        self.quit_char = 'q'

    def gain_xp(self, xp):
        self.experience += xp

    def __str__(self):
        return self.name + " XP: " + str(self.experience)
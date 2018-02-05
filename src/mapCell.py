class mapCell:
    def __init__(self, row, col, enemy=False, explored=False):
        self.row = row
        self.col = col
        self.enemy = enemy
        self.explored = explored

    def get_pos(self):
        return (self.row, self.col)

    def enemy_present(self):
        return self.enemy

    def is_explored(self):
        return self.explored

    def explore(self):
        self.explored = True
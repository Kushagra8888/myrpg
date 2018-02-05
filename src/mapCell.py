class mapCell:
    def __init__(self, row, col, battle=False, explored=False):
        self.row = row
        self.col = col
        self.battle = battle
        self.explored = explored

    def get_pos(self):
        return (self.row, self.col)

    def is_battle_cell(self):
        return self.battle

    def is_explored(self):
        return self.explored

    def explore(self):
        self.explored = True
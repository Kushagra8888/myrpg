from src.mapCell import mapCell
from src.moveHelper import *
import random

class mapArea:
    def __init__(
            self,
             rows=3,
             cols=3,
             initial_pos=(0,0),
             unexplored_cell_char="?",
             explored_cell_char="_",
             current_pos_char = "*",
             battle_cell_density = 0.25):
        self.rows = rows
        self.cols = cols
        self.current_pos = initial_pos
        self.unexplored_cell_char = unexplored_cell_char
        self.explored_cell_char = explored_cell_char
        self.current_pos_char = current_pos_char
        self.grid = [];
        self.battle_cell_density = battle_cell_density
        for row_idx in range(self.rows):
            self.grid.append([])
            for col_idx in range(self.rows):
                not_initial_pos = (row_idx, col_idx) != initial_pos
                battle = not_initial_pos and random.random() < battle_cell_density
                self.grid[row_idx].append(mapCell(row_idx, col_idx, battle=battle, explored=False))
        self.explore_cell(initial_pos)

    def get_cell_at_pos(self, position):
        return self.grid[position[0]][position[1]]

    def get_current_cell(self):
        return self.get_cell_at_pos(self.current_pos)

    def explore_cell(self, position):
        cell_at_pos = self.get_cell_at_pos(position)
        cell_at_pos.explore()

    def can_move(self, target):
        row = target[0]
        col = target[1]
        row_is_out_of_boundary = row >= self.rows or row < 0 or col >= self.cols or col < 0
        move_is_more_than_one_unit = (abs(self.current_pos[0] - target[0]) + abs(self.current_pos[1] - target[1])) > 1
        if row_is_out_of_boundary or move_is_more_than_one_unit:
            return False
        return True

    def move(self, target):
        if not self.can_move(target):
            return False
        else:
            self.current_pos = target
            self.explore_cell(target)
            return True

    def move_left(self):
        return self.move(toLeft(self.current_pos))

    def move_right(self):
        return self.move(toRight(self.current_pos))

    def move_up(self):
        return self.move(toUp(self.current_pos))

    def move_down(self):
        return self.move(toDown(self.current_pos))

    def __str__(self):
        str_repr = ""
        for row_idx in range(self.rows):
            for col_idx in range(self.cols):
                if ((row_idx, col_idx) == self.current_pos):
                    cell_char = self.current_pos_char
                elif not self.grid[row_idx][col_idx].is_explored():
                    cell_char = "?"
                elif self.grid[row_idx][col_idx].is_battle_cell():
                    cell_char = "!"
                else:
                    cell_char = "_"
                str_repr = str_repr + cell_char + " "
            str_repr += "\n"
        return str_repr
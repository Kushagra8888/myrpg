import unittest
from src.mapArea import mapArea
from src.moveHelper import *

class TestMapMethods(unittest.TestCase):


    def test_can_move_single_cell(self):
        initial = (0,0)
        maparea = mapArea(rows=1, cols=1, initial_pos = initial)
        self.assertFalse(maparea.can_move(toRight(initial)))
        self.assertFalse(maparea.can_move(toLeft(initial)))
        self.assertFalse(maparea.can_move(toUp(initial)))
        self.assertFalse(maparea.can_move(toDown(initial)))
        self.assertFalse(maparea.can_move((1, 1)))
        self.assertFalse(maparea.can_move((-1, 1)))
        self.assertFalse(maparea.can_move((1, -1)))
        self.assertFalse(maparea.can_move((-1, -1)))

    def test_can_move_3x3(self):
        initial = (1,1)
        maparea = mapArea(rows=3, cols=3, initial_pos=initial)
        self.assertTrue(maparea.can_move(toRight(initial)))
        self.assertTrue(maparea.can_move(toLeft(initial)))
        self.assertTrue(maparea.can_move(toUp(initial)))
        self.assertTrue(maparea.can_move(toDown(initial)))
        self.assertFalse(maparea.can_move((0, 0)))
        self.assertFalse(maparea.can_move((2, 2)))
        self.assertFalse(maparea.can_move((0, 2)))
        self.assertFalse(maparea.can_move((2, 0)))



if __name__ == '__main__':
    unittest.main()
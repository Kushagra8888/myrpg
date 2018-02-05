import unittest
from src.mapArea import mapArea

class TestMapAre(unittest.TestCase):
    def testMove(self):
        initial = (1, 1)
        maparea = mapArea(rows=3, cols=3, initial_pos=initial)
        self.assertTrue(maparea.move_left())
        self.assertTrue(maparea.current_pos == (0,1))
        self.assertTrue(maparea.move_down())
        self.assertTrue(maparea.current_pos == (0,0))
        self.assertFalse(maparea.move((2,0)))


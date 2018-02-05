import unittest
from src.mapArea import mapArea

class TestMapAre(unittest.TestCase):
    def testMove(self):
        initial = (1, 1)
        maparea = mapArea(rows=3, cols=3, initial_pos=initial)
        self.assertTrue(maparea.move_left())
        self.assertEqual(maparea.current_pos, (1,0))
        self.assertTrue(maparea.move_down())
        self.assertEqual(maparea.current_pos, (2,0))
        self.assertFalse(maparea.move((2,2)))


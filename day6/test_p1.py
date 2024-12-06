import unittest
from p1 import Day6p1

class TestP1(unittest.TestCase):

    def setUp(self):
        self.obj = Day6p1('./example.txt')

    def guard_change_tests(self, pos, direction):
        guard = self.obj.find_guard()
        self.assertEqual(guard.pos,pos)
        self.assertEqual(guard.direction, direction)
        self.assertEqual(self.obj.guard.pos, pos)
        self.assertEqual(self.obj.guard.direction, direction)

    def test_get_matrix_value(self):
        self.assertEqual(self.obj._get_matrix_value((0,0)), '.')
        self.assertEqual(self.obj._get_matrix_value((4,0)), '#')
        self.assertEqual(self.obj._get_matrix_value((4,6)), '^')

    def test_get_matrix_value(self):
        self.assertEqual(self.obj._get_matrix_value((0,0)), '.')
        self.obj._set_matrix_value((0,0), 'X')
        self.assertEqual(self.obj._get_matrix_value((0,0)), 'X')
        self.obj._set_matrix_value((0,0), '.')

        self.assertEqual(self.obj._get_matrix_value((4,6)), '^')
        self.obj._set_matrix_value((4,6), 'X')
        self.assertEqual(self.obj._get_matrix_value((4,6)), 'X')
        self.obj._set_matrix_value((4,6), '^')

    def test_is_move_within_bounds(self):
        y_max_index = len(self.obj.matrix) - 1
        x_max_index = len(self.obj.matrix[0]) - 1
        self.assertTrue(self.obj._is_move_within_bounds((0,0)))
        self.assertTrue(self.obj._is_move_within_bounds((4,0)))
        self.assertTrue(self.obj._is_move_within_bounds((4,6)))

        self.assertFalse(self.obj._is_move_within_bounds((-1,0)))
        self.assertFalse(self.obj._is_move_within_bounds((-1,-1)))
        self.assertFalse(self.obj._is_move_within_bounds((5,-5)))

        self.assertFalse(self.obj._is_move_within_bounds((x_max_index + 1,0)))
        self.assertFalse(self.obj._is_move_within_bounds((0,y_max_index +1)))
        self.assertFalse(self.obj._is_move_within_bounds((x_max_index + 1,y_max_index + 1)))
        self.assertFalse(self.obj._is_move_within_bounds((x_max_index,y_max_index + 1)))
        
    def test_is_obstacle(self):
        self.assertTrue(self.obj._is_obstacle((4,0)))
        self.assertFalse(self.obj._is_obstacle((0,0)))
        self.assertFalse(self.obj._is_obstacle((1,1)))

    def test_find_guard(self):
        guard = self.obj.find_guard()
        self.assertEqual(guard.pos, (4,6))
        self.assertEqual(guard.direction, '^')
        self.assertEqual(self.obj.guard.pos, (4,6))
        self.assertEqual(self.obj.guard.direction, '^')

    def test_rotate_guard(self):
        self.obj.rotate_guard()
        self.guard_change_tests((4,6), '>')

    def test_move_guard(self):
        self.obj.move_guard()
        self.guard_change_tests((4,5), '^')

        # Should hit an obstacle, rotate and move one to the right
        for i in range(6):
            self.obj.move_guard()
        self.guard_change_tests((5,1), '>')

        # Trail of guard should be X's
        for i in range(6):
            self.assertEqual(self.obj._get_matrix_value((4,6 - i)), 'X')

    def test_count_guard_vistited(self):
        self.obj.move_guard()
        self.assertEqual(self.obj.count_guard_visited(), 1)
        for i in range(6):
            self.obj.move_guard()
        self.assertEqual(self.obj.count_guard_visited(), 6)

if __name__ == '__main__':
    unittest.main()
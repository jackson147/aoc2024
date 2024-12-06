import unittest
from p1 import Day6p1
from p2 import Day6p2

class TestDays(unittest.TestCase):

    def setUp(self):
        self.p1 = Day6p1('./example.txt')
        self.p2 = Day6p2('./example.txt')

    def guard_change_tests(self, pos, direction):
        guard = self.p1.find_guard()
        self.assertEqual(guard.pos,pos)
        self.assertEqual(guard.direction, direction)
        self.assertEqual(self.p1.guard.pos, pos)
        self.assertEqual(self.p1.guard.direction, direction)

    def test_get_matrix_value(self):
        self.assertEqual(self.p1._get_matrix_value((0,0)), '.')
        self.assertEqual(self.p1._get_matrix_value((4,0)), '#')
        self.assertEqual(self.p1._get_matrix_value((4,6)), '^')

    def test_get_matrix_value(self):
        self.assertEqual(self.p1._get_matrix_value((0,0)), '.')
        self.p1._set_matrix_value((0,0), 'X')
        self.assertEqual(self.p1._get_matrix_value((0,0)), 'X')
        self.p1._set_matrix_value((0,0), '.')

        self.assertEqual(self.p1._get_matrix_value((4,6)), '^')
        self.p1._set_matrix_value((4,6), 'X')
        self.assertEqual(self.p1._get_matrix_value((4,6)), 'X')
        self.p1._set_matrix_value((4,6), '^')

    def test_is_move_within_bounds(self):
        y_max_index = len(self.p1.matrix) - 1
        x_max_index = len(self.p1.matrix[0]) - 1
        self.assertTrue(self.p1._is_move_within_bounds((0,0)))
        self.assertTrue(self.p1._is_move_within_bounds((4,0)))
        self.assertTrue(self.p1._is_move_within_bounds((4,6)))

        self.assertFalse(self.p1._is_move_within_bounds((-1,0)))
        self.assertFalse(self.p1._is_move_within_bounds((-1,-1)))
        self.assertFalse(self.p1._is_move_within_bounds((5,-5)))

        self.assertFalse(self.p1._is_move_within_bounds((x_max_index + 1,0)))
        self.assertFalse(self.p1._is_move_within_bounds((0,y_max_index +1)))
        self.assertFalse(self.p1._is_move_within_bounds((x_max_index + 1,y_max_index + 1)))
        self.assertFalse(self.p1._is_move_within_bounds((x_max_index,y_max_index + 1)))
        
    def test_is_obstacle(self):
        self.assertTrue(self.p1._is_obstacle((4,0)))
        self.assertFalse(self.p1._is_obstacle((0,0)))
        self.assertFalse(self.p1._is_obstacle((1,1)))
        
        self.assertFalse(self.p2._is_obstacle((4,5)))
        self.p2._set_matrix_value((4,5), 'O')
        self.assertTrue(self.p2._is_obstacle((4,5)))

    def test_find_guard(self):
        guard = self.p1.find_guard()
        self.assertEqual(guard.pos, (4,6))
        self.assertEqual(guard.direction, '^')
        self.assertEqual(self.p1.guard.pos, (4,6))
        self.assertEqual(self.p1.guard.direction, '^')

    def test_rotate_guard(self):
        self.p1.rotate_guard()
        self.guard_change_tests((4,6), '>')

    def test_move_guard(self):
        self.p1.move_guard()
        self.guard_change_tests((4,5), '^')

        # Should hit an obstacle, rotate and move one to the right
        for i in range(6):
            self.p1.move_guard()
        self.guard_change_tests((5,1), '>')

        # Trail of guard should be X's
        for i in range(6):
            self.assertEqual(self.p1._get_matrix_value((4,6 - i)), 'X')
            
    def test_get_matrix_size(self):
        self.assertEqual(self.p2.get_matrix_size(), (10,10))
        
    def test_get_next_guard_pos(self):
        next_guard = self.p2.get_next_guard()
        self.assertEqual(next_guard.pos, (4,5))
        self.assertEqual(next_guard.direction, '^')
        
        # All simple movements without obstacles, checks ahead upto one before obstacle
        for i in range(4):
            self.p2.move_guard()
            next_guard = self.p2.get_next_guard()
            self.assertEqual(next_guard.pos, (4,5 - i - 1))
            self.assertEqual(next_guard.direction, '^')
            
        # Blocked by fixed obstacle, but turns to the right
        self.p2.move_guard()
        next_guard = self.p2.get_next_guard()
        self.assertEqual(next_guard.pos, (4,1))
        self.assertEqual(next_guard.direction, '>')
        # Moves to the right
        self.p2.move_guard()
        next_guard = self.p2.get_next_guard()
        self.assertEqual(next_guard.pos, (5,1))
        self.assertEqual(next_guard.direction, '>')

    def test_count_guard_vistited(self):
        self.p1.move_guard()
        self.assertEqual(self.p1.count_guard_visited(), 1)
        for i in range(6):
            self.p1.move_guard()
        self.assertEqual(self.p1.count_guard_visited(), 6)

if __name__ == '__main__':
    unittest.main()
import unittest
from p1 import Part1
from p2 import Part2


class TestParts(unittest.TestCase):

    def setUp(self):
        self.p1 = Part1("./example.txt")
        self.p2 = Part2("./example.txt")

    def test_file_length(self):
        self.assertEqual(len(self.p1._data), 9)
        self.assertEqual(len(self.p2._data), 9)

    def test_parse_input_data(self):
        self.assertEqual(self.p1.data["21037"], [9, 7, 18, 13])
        self.assertEqual(self.p2.data["21037"], [9, 7, 18, 13])

    def test_is_possible(self):
        self.assertFalse(self.p1.is_possible(result_key="156"))
        self.assertTrue(self.p1.is_possible(result_key="190"))
        self.assertFalse(self.p1.is_possible(result_key="161011"))

        self.assertTrue(
            self.p1.is_possible(
                result_key="54753537",
                input_equation_values=[2, 35, 2, 5, 5, 9, 1, 17, 367, 73],
            )
        )


if __name__ == "__main__":
    unittest.main()

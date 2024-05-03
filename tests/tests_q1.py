import unittest
from Q1 import sort_the_students
from ed_utils.decorators import number

class Test_Q1(unittest.TestCase):
    @number("1.1")
    def test_examples(self):
        self.assertEqual(sort_the_students([[10,6,9,1],[7,5,11,2],[4,8,3,15]], 2), [[7,5,11,2],[10,6,9,1],[4,8,3,15]])
        self.assertEqual(sort_the_students([[3,4],[5,6]], 0), [[5,6],[3,4]])

    @number("1.2")
    def test_extra(self):
        self.assertEqual(sort_the_students([[1]], 0), [[1]])
        self.assertEqual(sort_the_students([[90, 85, 88], [70, 95, 80], [60, 75, 100], [85, 80, 90], [75, 70, 85]], 1), [[70, 95, 80], [90, 85, 88], [85, 80, 90], [60, 75, 100], [75, 70, 85]])


if __name__ == '__main__':
    unittest.main()
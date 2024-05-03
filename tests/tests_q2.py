import unittest
from Q2 import sort_the_sentence
from ed_utils.decorators import number

class Test_Q2(unittest.TestCase):
    @number("2.1")
    def test_examples(self):
        self.assertEqual(sort_the_sentence("is2 sentence4 This1 a3"), "This is a sentence")
        self.assertEqual(sort_the_sentence("Myself2 Me1 I4 and3"), "Me Myself and I")

    @number("2.2")
    def test_extra(self):
        self.assertEqual(sort_the_sentence("ThiS4 is3 a2 sentenCe1 with5 varYing6 WordS7"), "sentenCe a is ThiS with varYing WordS")
        self.assertEqual(sort_the_sentence("Hello1"), "Hello")


if __name__ == '__main__':
    unittest.main()
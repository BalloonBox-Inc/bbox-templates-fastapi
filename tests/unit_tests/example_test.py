import unittest
from helpers.example import flatten_list


class ExampleTest(unittest.TestCase):

    def setUp(self):
        # test input
        self.example = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]

        # expected result
        self.expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def tearDown(self):
        # reset test input values after function execution
        self.example = None

    def test_example(self):
        # observed result after function execution
        observed = flatten_list(self.example)

        # checking if expected and observed results match
        self.assertCountEqual(observed, self.expected)
        self.assertListEqual(observed, self.expected)

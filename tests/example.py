import unittest


class ExampleTest(unittest.TestCase):

    def setUp(self):
        ''' import test values (inputs) that feed app functions '''
        # self.example = your_test_file.json
        self.example = 10

    def tearDown(self):
        ''' reset test values after running tests'''
        self.example = None

    def test_example(self):
        ''' perform test calling app functions '''
        # example = your_function(self.example)
        example = self.example

        self.assertEqual(example, 10)

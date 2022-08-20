# from tests.api_testing.example import ExampleTest
from tests.unit_testing.example import ExampleTest
import unittest


def suite():

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ExampleTest))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

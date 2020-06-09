"""

Program: camper_age_input.py

Author: Jenni Jarrell

Last date modified: 06/08/2020


The purpose of this program is to take an input of an age in years and convert it to months.
This is also to practice unit testing.


"""
import unittest
from main import camper_age_input


class FunctionTestCase(unittest.TestCase):
    def test_int2(self):
        self.assertEqual(24, camper_age_input.convert_to_months(2))


if __name__ == '__camper_age_input__':
    unittest.main()


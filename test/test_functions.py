import unittest
from main import camper_age_input


class FunctionTestCase(unittest.TestCase):
    def test_int2(self):
        self.assertEqual(24, camper_age_input.convert_to_months(2))


if __name__ == '__camper_age_input__':
    unittest.main()

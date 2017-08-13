import unittest
from utils.utils import get_average_from_list


class TestsListAverage(unittest.TestCase):
    def test_simple_average(self):
        number_list = [2, 2, 4, 4]
        known_average = 3
        calculated_average = get_average_from_list(number_list)
        self.assertEqual(known_average, calculated_average)

    def test_empty_list(self):
        empty_list = []
        known_average = 0
        calculated_average = get_average_from_list(empty_list)
        self.assertEqual(known_average, calculated_average)

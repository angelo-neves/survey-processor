import unittest
from gateways.CsvFileGateway import CsvFileGateway


class TestsCsvFileGateway(unittest.TestCase):
    def test_open_real_file(self):
        file_path = 'files/survey-1.csv'
        expected_number_of_lines = 6

        csv_file = CsvFileGateway(file_path)
        lines_loaded = csv_file.get_all_lines()
        total_lines_loaded = len(lines_loaded)

        self.assertEqual(total_lines_loaded, expected_number_of_lines)

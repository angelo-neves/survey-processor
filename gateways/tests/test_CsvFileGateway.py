import unittest
from gateways.CsvFileGateway import CsvFileGateway


class TestsCsvFileGateway(unittest.TestCase):
    def test_line_count(self):
        file_path = 'test_files/survey-1.csv'
        expected_number_of_lines = 6

        csv_file = CsvFileGateway(file_path)
        lines_loaded = csv_file.get_all_lines()
        total_lines_loaded = len(lines_loaded)

        self.assertEqual(total_lines_loaded, expected_number_of_lines)

    def test_first_line_content(self):
        file_path = 'test_files/survey-1-responses.csv'
        expected_first_line_content = ['employee1@abc.xyz', '1', '2014-07-28T20:35:41+00:00', '5', '5', '5', '4', '4']
        csv_file = CsvFileGateway(file_path)
        lines_loaded = csv_file.get_all_lines()
        first_line_content = lines_loaded[0]
        self.assertEqual(first_line_content, expected_first_line_content)

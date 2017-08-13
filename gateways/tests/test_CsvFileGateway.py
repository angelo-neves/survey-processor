import unittest
from gateways.CsvFileGateway import CsvFileGateway


class TestsCsvFileGateway(unittest.TestCase):
    def test_line_count(self):
        file_path = 'test_files/survey-1.csv'
        expected_number_of_lines = 5

        csv_file = CsvFileGateway(file_path, True)
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

    def test_file_with_header(self):
        file_path = 'test_files/survey-3.csv'
        expected_type = 'ratingquestion'
        expected_theme = 'The Work'
        expected_text = 'I like the kind of work I do.'

        csv_file = CsvFileGateway(file_path, True)
        lines_loaded = csv_file.get_all_lines_with_keys()
        first_line_content = lines_loaded[0]

        self.assertEqual(first_line_content['type'], expected_type)
        self.assertEqual(first_line_content['theme'], expected_theme)
        self.assertEqual(first_line_content['text'], expected_text)

    def test_file_not_found(self):
        file_path = 'some_fake_file.csv'
        with self.assertRaises(SystemExit):
            CsvFileGateway(file_path)

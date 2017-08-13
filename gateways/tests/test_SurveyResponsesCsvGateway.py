import unittest
from gateways.SurveyResponsesCsvGateway import SurveyResponsesCsvGateway


class TestsSurveyResponsesCsvGateway(unittest.TestCase):
    def test_number_of_loaded_responses(self):
        file_path = 'test_files/survey-1-responses.csv'
        expected_responses_count = 6

        responses_file = SurveyResponsesCsvGateway(file_path, 5)
        responses_list = responses_file.get_responses_list()
        responses_count = len(responses_list)

        self.assertEqual(responses_count, expected_responses_count)

    def test_first_response_content(self):
        file_path = 'test_files/survey-1-responses.csv'
        expected_email = 'employee1@abc.xyz'
        expected_employee_id = '1'
        expected_timestamp = '2014-07-28T20:35:41+00:00'
        expected_answers = ['5', '5', '5', '4', '4']

        responses_file = SurveyResponsesCsvGateway(file_path, 5)
        responses_list = responses_file.get_responses_list()
        first_response = responses_list[0]

        self.assertEqual(first_response.email, expected_email)
        self.assertEqual(first_response.employee_id, expected_employee_id)
        self.assertEqual(first_response.timestamp, expected_timestamp)
        self.assertEqual(first_response.answers, expected_answers)

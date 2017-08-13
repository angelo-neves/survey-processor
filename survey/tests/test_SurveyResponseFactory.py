import unittest
from survey.SurveyResponseFactory import SurveyResponseFactory
from test_mocks.CsvFileGateway import CsvFileGateway


class TestsSurveyResponseFactory(unittest.TestCase):
    def test_load_list_count(self):
        expected_count = 6
        number_of_questions = 5

        lines = [
            ['employee1@abc.xyz', '1', '2014-07-28T20:35:41+00:00', '5', '5', '5', '4', '4'],
            ['', '2', '2014-07-29T07:05:41+00:00', '4', '5', '5', '3', '3'],
            ['', '3', '2014-07-29T17:35:41+00:00', '5', '5', '5', '5', '4'],
            ['employee4@abc.xyz', '4', '2014-07-30T04:05:41+00:00', '5', '5', '5', '4', '4'],
            ['', '5', '2014-07-31T11:35:41+00:00', '4', '5', '5', '2', '3'],
            ['employee5@abc.xyz', '6', '', '', '', '', '', '']
        ]

        mocked_response_gateway = CsvFileGateway()
        mocked_response_gateway.lines = lines

        response_factory = SurveyResponseFactory(mocked_response_gateway, number_of_questions)
        response_list = response_factory.get_responses_list()
        count = len(response_list)

        self.assertEqual(count, expected_count)

    def test_specific_response_content(self):
        number_of_questions = 5

        expected_email = 'employee4@abc.xyz'
        expected_employee_id = '4'
        expected_timestamp = '2014-07-30T04:05:41+00:00'
        expected_answers = ['5', '5', '5', '4', '4']

        lines = [
            ['employee1@abc.xyz', '1', '2014-07-28T20:35:41+00:00', '5', '5', '5', '4', '4'],
            ['', '2', '2014-07-29T07:05:41+00:00', '4', '5', '5', '3', '3'],
            ['', '3', '2014-07-29T17:35:41+00:00', '5', '5', '5', '5', '4'],
            [expected_email, expected_employee_id, expected_timestamp] + expected_answers,
            ['', '5', '2014-07-31T11:35:41+00:00', '4', '5', '5', '2', '3'],
            ['employee5@abc.xyz', '6', '', '', '', '', '', '']
        ]

        mocked_response_gateway = CsvFileGateway()
        mocked_response_gateway.lines = lines

        response_factory = SurveyResponseFactory(mocked_response_gateway, number_of_questions)
        response_list = response_factory.get_responses_list()
        specific_response = response_list[3]

        self.assertEqual(specific_response.email, expected_email)
        self.assertEqual(specific_response.employee_id, expected_employee_id)
        self.assertEqual(specific_response.timestamp, expected_timestamp)
        self.assertEqual(specific_response.answers, expected_answers)


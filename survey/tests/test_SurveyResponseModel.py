import unittest
from survey.SurveyResponseModel import SurveyResponseModel


class TestsSurveyResponseModel(unittest.TestCase):
    def test_load_list(self):
        expected_email = 'employee1@abc.xyz'
        expected_employee_id = '1'
        expected_timestamp = '2014-07-28T20:35:41+00:00'
        expected_answers = ['5', '5', '5', '4', '4']

        response_row = [expected_email, expected_employee_id, expected_timestamp] + expected_answers

        response = SurveyResponseModel(response_row, 5)

        self.assertEqual(response.email, expected_email)
        self.assertEqual(response.employee_id, expected_employee_id)
        self.assertEqual(response.timestamp, expected_timestamp)
        self.assertEqual(response.answers, expected_answers)
        self.assertTrue(response.is_submitted())

    def test_get_specific_answer(self):
        email = 'employee1@abc.xyz'
        employee_id = '1'
        timestamp = '2014-07-28T20:35:41+00:00'
        answers = ['5', '5', '5', '3', '4']

        response_row = [email, employee_id, timestamp] + answers

        response = SurveyResponseModel(response_row, 5)

        self.assertEqual('3', response.get_answer(3))

    def test_empty_timestamp(self):
        email = 'employee1@abc.xyz'
        employee_id = '1'
        timestamp = ''
        answers = ['5', '5', '5', '3', '4']

        response_row = [email, employee_id, timestamp] + answers

        response = SurveyResponseModel(response_row, 5)

        self.assertFalse(response.is_submitted())

    def test_missing_answer_position(self):
        email = 'employee1@abc.xyz'
        employee_id = '1'
        timestamp = ''
        answers = ['5', '5', '5', '3']

        response_row = [email, employee_id, timestamp] + answers

        with self.assertRaises(SystemExit):
            SurveyResponseModel(response_row, 5)


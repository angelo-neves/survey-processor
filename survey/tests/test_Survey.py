import unittest
from survey.tests.SurveyTestUtils import SurveyTestUtils
from survey.Survey import Survey


class TestsSurvey(unittest.TestCase):
    def test_total_employees_surveyed(self):
        expected_total_employees_surveyed = 6

        utils = SurveyTestUtils()
        question_list = utils.get_valid_question_list()
        responses_list = utils.get_valid_responses_list()

        survey = Survey(question_list, responses_list)

        self.assertEqual(survey.total_employees_surveyed, expected_total_employees_surveyed)

    def test_total_responses(self):
        expected_total_responses = 4

        utils = SurveyTestUtils()
        question_list = utils.get_valid_question_list()
        responses_list = utils.get_valid_responses_list()

        survey = Survey(question_list, responses_list)

        self.assertEqual(survey.total_responses, expected_total_responses)

    def test_participation_percentage(self):
        expected_participation_percentage = '66.67'

        utils = SurveyTestUtils()
        question_list = utils.get_valid_question_list()
        responses_list = utils.get_valid_responses_list()

        survey = Survey(question_list, responses_list)
        rounded_participation_percentage = '%.2f' % survey.participation_percentage

        self.assertEqual(rounded_participation_percentage, expected_participation_percentage)

    def test_average_responses(self):
        expected_average_list = ['4.75', '5.00', '5.00', '3.75', '3.75']
        calculated_average_list = []

        utils = SurveyTestUtils()
        question_list = utils.get_valid_question_list()
        responses_list = utils.get_valid_responses_list()

        survey = Survey(question_list, responses_list)

        questions = survey.get_all_questions()

        for question in questions:
            question_average = question.get_average_response()
            calculated_average_list.append(question_average)

        self.assertEqual(calculated_average_list, expected_average_list)
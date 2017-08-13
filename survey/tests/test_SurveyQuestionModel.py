import unittest
from survey.SurveyQuestionModel import SurveyQuestionModel


class TestsSurveyQuestionModel(unittest.TestCase):
    def test_load_dict(self):
        expected_type = 'ratingquestion'
        expected_theme = 'The Work'
        expected_text = 'We are working at the right pace to meet our goals.'

        question_dict = {
            'type': expected_type,
            'theme': expected_theme,
            'text': expected_text
        }

        question = SurveyQuestionModel(question_dict)

        self.assertEqual(question.type, expected_type)
        self.assertEqual(question.theme, expected_theme)
        self.assertEqual(question.text, expected_text)

    def test_set_average(self):
        expected_average = 5

        question_dict = {
            'type': 'ratingquestion',
            'theme': 'The Work',
            'text': 'We are working at the right pace to meet our goals.'
        }

        question = SurveyQuestionModel(question_dict)

        question.set_average_response(expected_average)

        self.assertEqual(question.get_average_response(), expected_average)

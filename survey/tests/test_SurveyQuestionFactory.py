import unittest
from survey.SurveyQuestionFactory import SurveyQuestionFactory
from test_mocks.CsvFileGateway import CsvFileGateway


class TestsSurveyQuestionFactory(unittest.TestCase):
    def test_load_list_count(self):
        expected_count = 5

        lines_with_keys = [
            {'theme': 'The Work', 'type': 'ratingquestion', 'text': 'I like the kind of work I do.'},
            {'theme': 'The Work', 'type': 'ratingquestion', 'text': 'I like the kind of work I do.'},
            {'theme': 'The Work', 'type': 'ratingquestion', 'text': 'I like the kind of work I do.'},
            {'theme': 'The Place', 'type': 'ratingquestion', 'text': 'I like the kind of work I do.'},
            {'theme': 'The Place', 'type': 'ratingquestion', 'text': 'I like the kind of work I do.'}
        ]

        mocked_questions_gateway = CsvFileGateway()
        mocked_questions_gateway.lines_with_keys = lines_with_keys

        questions_factory = SurveyQuestionFactory(mocked_questions_gateway)
        questions_list = questions_factory.get_question_list()
        count = len(questions_list)

        self.assertEqual(expected_count, count)

    def test_specific_question_content(self):
        expected_theme = 'The Place'
        expected_type = 'ratingquestion'
        expected_text = 'Just a Test!'

        lines_with_keys = [
            {'theme': 'The Work', 'type': 'ratingquestion', 'text': 'I like the kind of work I do.'},
            {'theme': 'The Work', 'type': 'ratingquestion', 'text': 'I like the kind of work I do.'},
            {'theme': expected_theme, 'type': expected_type, 'text': expected_text},
            {'theme': 'The Place', 'type': 'ratingquestion', 'text': 'I like the kind of work I do.'},
            {'theme': 'The Place', 'type': 'ratingquestion', 'text': 'I like the kind of work I do.'}
        ]

        mocked_questions_gateway = CsvFileGateway()
        mocked_questions_gateway.lines_with_keys = lines_with_keys

        questions_factory = SurveyQuestionFactory(mocked_questions_gateway)
        questions_list = questions_factory.get_question_list()

        specific_question = questions_list[2]

        self.assertEqual(specific_question.theme, expected_theme)
        self.assertEqual(specific_question.type, expected_type)
        self.assertEqual(specific_question.text, expected_text)

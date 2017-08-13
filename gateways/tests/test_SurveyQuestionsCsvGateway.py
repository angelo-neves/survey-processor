import unittest
from survey.SurveyQuestionFactory import SurveyQuestionFactory
from test_mocks.CsvFileGateway import CsvFileGateway


class TestsSurveyQuestionsCsvGateway(unittest.TestCase):
    def test_number_of_loaded_questions(self):
        raw_question_data = [
            ['ratingquestion', 'The Work', 'I like the kind of work I do.'],
            ['singleselect', 'The Work', 'Manager'],
            ['ratingquestion', 'I like the kind of work I do.']
        ]
        expected_questions_count = 5
        questions_file_gateway =CsvFileGateway()

        questions_file = SurveyQuestionFactory()
        questions_list = questions_file.get_questions_list()
        questions_count = len(questions_list)

        self.assertEqual(questions_count, expected_questions_count)

    def test_first_question_content(self):
        file_path = 'test_files/survey-1.csv'
        expected_question_theme = 'The Work'
        expected_question_type = 'ratingquestion'
        expected_question_text = 'I like the kind of work I do.'

        questions_file = SurveyQuestionFactory(file_path)
        questions_list = questions_file.get_questions_list()
        first_question = questions_list[0]

        self.assertEqual(first_question.theme, expected_question_theme)
        self.assertEqual(first_question.type, expected_question_type)
        self.assertEqual(first_question.text, expected_question_text)
from test_mocks.CsvFileGateway import CsvFileGateway
from survey.SurveyQuestionFactory import SurveyQuestionFactory
from survey.SurveyResponseFactory import SurveyResponseFactory


class SurveyTestUtils(object):
    def __init__(self):
        pass

    def get_valid_question_list(self):
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

        return questions_list

    def get_valid_responses_list(self):
        number_of_questions = 5

        lines = [
            ['employee1@abc.xyz', '1', '2014-07-28T20:35:41+00:00', '5', '5', '5', '4', '4'],
            ['', '2', '', '4', '5', '5', '3', '3'],
            ['', '3', '2014-07-29T17:35:41+00:00', '5', '5', '5', '5', '4'],
            ['employee4@abc.xyz', '4', '2014-07-30T04:05:41+00:00', '5', '5', '5', '4', '4'],
            ['', '5', '2014-07-31T11:35:41+00:00', '4', '5', '5', '2', '3'],
            ['employee5@abc.xyz', '6', '', '', '', '', '', '']
        ]

        mocked_response_gateway = CsvFileGateway()
        mocked_response_gateway.lines = lines

        response_factory = SurveyResponseFactory(mocked_response_gateway, number_of_questions)
        response_list = response_factory.get_responses_list()

        return response_list

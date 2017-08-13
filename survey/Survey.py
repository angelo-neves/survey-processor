from enums.SurveyQuestionType import SurveyQuestionType
from texttable import Texttable
from utils.utils import get_average_from_list


class Survey(object):
    questions = []
    responses = []
    total_employees_surveyed = 0
    total_responses = 0
    participation_percentage = 0
    total_number_of_questions = 0

    def __init__(self, question_list, responses_list):
        self.questions = question_list
        self.total_number_of_questions = len(self.questions)
        self.responses = responses_list

        self._calculate_participation()
        self._calculate_all_average_ratings()

    def _calculate_participation(self):
        self.total_employees_surveyed = len(self.responses)
        self.total_responses = 0
        for response in self.responses:
            if len(response.timestamp) > 0:
                self.total_responses += 1
        self.participation_percentage = (100*self.total_responses)/self.total_employees_surveyed

    def _calculate_all_average_ratings(self):
        for question_number, question in enumerate(self.questions):
            if question.type == SurveyQuestionType.RATING.value:
                ratings_for_this_question = []
                for individual_response in self.responses:
                    answer = individual_response.get_answer(question_number)
                    answer_is_not_empty = len(answer) > 0
                    if answer_is_not_empty:
                        ratings_for_this_question.append(int(answer))
                average_rating = get_average_from_list(ratings_for_this_question)
                self._set_average_rating_for_question(question_number, average_rating)

    def _set_average_rating_for_question(self, question_number, average_rating):
        self.questions[question_number].set_average_response(average_rating)

    def print_average_question_ratings(self):
        output_table = Texttable()
        output_table.add_row(['Survey Question', 'Average Response'])
        for question in self.questions:
            if question.type == SurveyQuestionType.RATING.value:
                output_table.add_row([question.text, question.get_average_response()])
        print(output_table.draw())

    def print_participation_data(self):
        print('This survey was sent to %.0f people.' % self.total_employees_surveyed)
        print('We received %.0f responses.' % self.total_responses)
        print('Participation was %.2f%%' % self.participation_percentage)

from enums.SurveyQuestionType import SurveyQuestionType


class Survey(object):
    def __init__(self, question_list, responses_list):
        self.questions = question_list
        self.total_number_of_questions = len(self.questions)
        self.responses = responses_list
        self.total_employees_surveyed = len(self.responses)
        self.total_responses = 0
        self.participation_percentage = 0

        self._calculate_participation()
        self._calculate_all_average_ratings()

    def _calculate_participation(self):
        self.total_responses = 0
        self.total_employees_surveyed = len(self.responses)
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
                    if answer_is_not_empty and individual_response.is_submitted():
                        ratings_for_this_question.append(int(answer))
                average_rating = self._get_average_from_list(ratings_for_this_question)
                self._set_average_rating_for_question(question_number, average_rating)

    def _set_average_rating_for_question(self, question_number, average_rating):
        rounded_average = '%.2f' % average_rating
        self.questions[question_number].set_average_response(rounded_average)

    def _get_average_from_list(self, list_of_numbers):
        total_sum = 0
        number_count = len(list_of_numbers)

        if number_count == 0:
            return total_sum

        for number in list_of_numbers:
            total_sum += number
        return total_sum / number_count

    def get_all_questions(self):
        return self.questions

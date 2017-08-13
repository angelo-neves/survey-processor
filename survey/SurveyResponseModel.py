import sys


class SurveyResponseModel(object):
    def __init__(self, response_row, number_of_questions_on_survey_file):
        self.answers = []
        self.email = response_row[0]
        self.employee_id = response_row[1]
        self.timestamp = response_row[2]

        for response_field in response_row[3:]:
            self.answers.append(response_field)

        self._validate_model(number_of_questions_on_survey_file)

    def _validate_model(self, number_of_questions_on_survey_file):
        number_of_answers_in_response_row = len(self.answers)

        if number_of_answers_in_response_row != number_of_questions_on_survey_file:
            sys.exit('Model error: Expected %.0f answer columns on response file but found %.0f' %
                     (number_of_questions_on_survey_file, number_of_answers_in_response_row))

    def get_answer(self, question_number):
        return self.answers[question_number]

    def is_submitted(self):
        if len(self.timestamp) > 0:
            return True
        else:
            return False

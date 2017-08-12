import sys
import csv
from texttable import Texttable
from enum import Enum


class SurveyQuestionType(Enum):
    RATING = 'ratingquestion'


def get_csv_reader(file_path):
    try:
        csv_reader = csv.reader(open(file_path))
    except (OSError, IOError):
        sys.exit('File not found: ' + file_path)

    return csv_reader


class Response(object):
    email = ''
    employee_id = ''
    timestamp = ''
    responses = []

    def __init__(self, response_row, number_of_questions_on_survey_file):
        self.responses = []
        self.email = response_row[0]
        self.employee_id = response_row[1]
        self.timestamp = response_row[2]
        for response_field in response_row[3:]:
            self.responses.append(response_field)

        number_of_answers_in_response_row = len(self.responses)

        if number_of_answers_in_response_row != number_of_questions_on_survey_file:
            sys.exit('Model error: Expected %.0f answer columns on response file but found %.0f' %
                     (number_of_questions_on_survey_file, number_of_answers_in_response_row))

    def get_responses(self):
        return self.responses


class SurveyQuestion(object):
    theme = ''
    type = ''
    text = ''
    average_response = 0

    def __init__(self, survey_file_row):
        self.theme = survey_file_row[0]
        self.type = survey_file_row[1]
        self.text = survey_file_row[2]

    def set_average_response(self, value):
        self.average_response = value

    def get_average_response(self):
        return self.average_response


class Survey(object):
    survey_questions = []
    survey_responses = []
    total_employees_surveyed = 0
    total_responses = 0
    participation_percentage = 0

    def __init__(self, survey_file_path, responses_file_path):
        survey_file = get_csv_reader(survey_file_path)
        for survey_row in survey_file:
            self.survey_questions.append(SurveyQuestion(survey_row))
        del self.survey_questions[0]

        number_of_questions = len(self.survey_questions)

        responses_file = get_csv_reader(responses_file_path)
        
        # Validate datatype issues too
        for response_row in responses_file:
            self.survey_responses.append(Response(response_row, number_of_questions))

        self._calculate_participation()
        self._calculate_average_responses()

    def _calculate_participation(self):
        self.total_employees_surveyed = len(self.survey_responses)
        self.total_responses = 0
        for response in self.survey_responses:
            if len(response.timestamp) > 0:
                self.total_responses += 1
        self.participation_percentage = (100*self.total_responses)/self.total_employees_surveyed

    def _calculate_average_responses(self):
        for question_number, question in enumerate(self.survey_questions):
            question_ratings = []
            if question.type == SurveyQuestionType.RATING.value:
                for response in self.survey_responses:
                    rating = response.responses[question_number]
                    if len(rating) > 0:
                        question_ratings.append(int(rating))
                ratings_sum = 0
                for rating in question_ratings:
                    ratings_sum += rating
                average_rating = ratings_sum / len(question_ratings)
                self.survey_questions[question_number].set_average_response(average_rating)

    def print_average_question_ratings(self):
        output_table = Texttable()
        output_table.add_row(['Survey Question', 'Average Response'])
        for question in self.survey_questions:
            if question.type == SurveyQuestionType.RATING.value:
                output_table.add_row([question.text, question.get_average_response()])
        print(output_table.draw())

    def print_participation_data(self):
        print('This survey was sent to %.0f people.' % self.total_employees_surveyed)
        print('We received %.0f responses.' % self.total_responses)
        print('Participation was %.2f%%' % self.participation_percentage)

if __name__ == "__main__":
    two_parameters_given = len(sys.argv) == 3

    if not two_parameters_given:
        sys.exit('You must inform 2 file paths')

    surveyFilePath = sys.argv[1]
    responseFilePath = sys.argv[2]

    survey = Survey(surveyFilePath, responseFilePath)
    survey.print_participation_data()
    survey.print_average_question_ratings()


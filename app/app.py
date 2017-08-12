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


def get_list_average(list_of_numbers):
    total = 0
    for number in list_of_numbers:
        total += number
    return total / len(list_of_numbers)


def skip_one_line(file_iterator):
    next(file_iterator)


class SurveyResponse(object):
    email = ''
    employee_id = ''
    timestamp = ''
    answers = []

    def __init__(self, response_row, number_of_questions_on_survey_file):
        self.answers = []
        self.email = response_row[0]
        self.employee_id = response_row[1]
        self.timestamp = response_row[2]
        for response_field in response_row[3:]:
            self.answers.append(response_field)

        number_of_answers_in_response_row = len(self.answers)

        if number_of_answers_in_response_row != number_of_questions_on_survey_file:
            sys.exit('Model error: Expected %.0f answer columns on response file but found %.0f' %
                     (number_of_questions_on_survey_file, number_of_answers_in_response_row))

    def get_answer(self, question_number):
        return self.answers[question_number]


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
    questions = []
    responses = []
    total_employees_surveyed = 0
    total_responses = 0
    participation_percentage = 0
    total_number_of_questions = 0

    def __init__(self, survey_file_path, responses_file_path):
        self.load_survey_questions_from_file(survey_file_path)
        self.load_responses_from_file(responses_file_path)
        self.calculate_participation()
        self.calculate_all_average_ratings()

    def load_survey_questions_from_file(self, survey_file_path):
        survey_questions_file = get_csv_reader(survey_file_path)
        skip_one_line(survey_questions_file)
        for question_csv in survey_questions_file:
            self.questions.append(SurveyQuestion(question_csv))

        self.total_number_of_questions = len(self.questions)

    def load_responses_from_file(self, responses_file_path):

        responses_file = get_csv_reader(responses_file_path)

        # Validate datatype issues too
        for individual_response_csv in responses_file:
            individual_response = SurveyResponse(individual_response_csv, self.total_number_of_questions)
            self.responses.append(individual_response)

    def calculate_participation(self):
        self.total_employees_surveyed = len(self.responses)
        self.total_responses = 0
        for response in self.responses:
            if len(response.timestamp) > 0:
                self.total_responses += 1
        self.participation_percentage = (100*self.total_responses)/self.total_employees_surveyed

    def calculate_all_average_ratings(self):
        for question_number, question in enumerate(self.questions):
            if question.type == SurveyQuestionType.RATING.value:
                ratings_for_this_question = []
                for individual_response in self.responses:
                    answer = individual_response.get_answer(question_number)
                    answer_is_not_empty = len(answer) > 0
                    if answer_is_not_empty:
                        ratings_for_this_question.append(int(answer))
                average_rating = get_list_average(ratings_for_this_question)
                self.set_average_rating_for_question(question_number, average_rating)

    def set_average_rating_for_question(self, question_number, average_rating):
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

if __name__ == "__main__":
    two_parameters_given = len(sys.argv) == 3

    if not two_parameters_given:
        sys.exit('You must inform 2 file paths')

    surveyFilePath = sys.argv[1]
    responseFilePath = sys.argv[2]

    survey = Survey(surveyFilePath, responseFilePath)
    survey.print_participation_data()
    survey.print_average_question_ratings()


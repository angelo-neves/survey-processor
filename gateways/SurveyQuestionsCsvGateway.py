from survey.SurveyQuestion import SurveyQuestion
from gateways.CsvFileGateway import CsvFileGateway


class SurveyQuestionsCsvGateway(object):
    def __init__(self, survey_file_path):
        self.questions = []

        survey_questions_file = CsvFileGateway(survey_file_path)
        question_file_lines = survey_questions_file.get_all_lines()

        for question_csv in question_file_lines[1:]:
            self.questions.append(SurveyQuestion(question_csv))

    def get_questions_list(self):
        return self.questions

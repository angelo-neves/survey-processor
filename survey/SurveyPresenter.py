from texttable import Texttable
from enums.SurveyQuestionType import SurveyQuestionType


class SurveyPresenter(object):
    def __init__(self, survey):
        self.survey = survey

    def print_rating_questions_averages(self):
        questions = self.survey.get_all_questions()
        output_table = Texttable()
        output_table.add_row(['Survey Question', 'Average Response'])
        for question in questions:
            if question.type == SurveyQuestionType.RATING.value:
                output_table.add_row([question.text, question.get_average_response()])
        print(output_table.draw())

    def print_participation_data(self):
        print('This survey was sent to %.0f people.' % self.survey.total_employees_surveyed)
        print('We received %.0f responses.' % self.survey.total_responses)
        print('Participation was %.2f%%' % self.survey.participation_percentage)

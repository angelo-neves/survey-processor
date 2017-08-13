import sys
from texttable import Texttable
from enums.SurveyQuestionType import SurveyQuestionType


class SurveyPresenter(object):
    def __init__(self, survey, out=sys.stdout):
        self.survey = survey
        self.out = out

    def print_rating_questions_averages(self):
        questions = self.survey.get_all_questions()
        output_table = Texttable()
        output_table.set_precision(2)
        output_table.add_row(['Survey Question', 'Average Response'])
        for question in questions:
            if question.type == SurveyQuestionType.RATING.value:
                output_table.add_row([question.text, question.get_average_response()])
        self.out.write(output_table.draw())
        self.out.write('\n')

    def print_participation_data(self):
        self.out.write('This survey was sent to %.0f people.\n' % self.survey.total_employees_surveyed)
        self.out.write('We received %.0f responses.\n' % self.survey.total_responses)
        self.out.write('Participation was %.2f%%\n' % self.survey.participation_percentage)

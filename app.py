import sys
from survey.Survey import Survey
from survey.SurveyQuestionFactory import SurveyQuestionFactory
from survey.SurveyResponseFactory import SurveyResponseFactory
from gateways.CsvFileGateway import CsvFileGateway

if __name__ == "__main__":
    two_arguments_given = len(sys.argv) == 3

    if not two_arguments_given:
        sys.exit('You must inform 2 arguments')

    survey_questions_csv_path = sys.argv[1]
    survey_responses_csv_path = sys.argv[2]

    questions_file_gateway = CsvFileGateway(survey_questions_csv_path, True)
    questions_factory = SurveyQuestionFactory(questions_file_gateway)
    question_list = questions_factory.get_question_list()

    responses_file_gateway = CsvFileGateway(survey_responses_csv_path)
    responses_factory = SurveyResponseFactory(responses_file_gateway, len(question_list))
    responses_list = responses_factory.get_responses_list()

    survey = Survey(question_list, responses_list)

    survey.print_participation_data()
    survey.print_average_question_ratings()


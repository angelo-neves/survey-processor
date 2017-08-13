import sys
from survey.Survey import Survey
from gateways.SurveyQuestionsCsvGateway import SurveyQuestionsCsvGateway
from gateways.SurveyResponsesCsvGateway import SurveyResponsesCsvGateway

if __name__ == "__main__":
    two_arguments_given = len(sys.argv) == 3

    if not two_arguments_given:
        sys.exit('You must inform 2 arguments')

    survey_questions_csv_path = sys.argv[1]
    survey_responses_csv_path = sys.argv[2]

    questions_gateway = SurveyQuestionsCsvGateway(survey_questions_csv_path)
    question_list = questions_gateway.get_questions_list()

    responses_gateway = SurveyResponsesCsvGateway(survey_responses_csv_path, len(question_list))
    responses_list = responses_gateway.get_responses_list()

    survey = Survey(question_list, responses_list)

    survey.print_participation_data()
    survey.print_average_question_ratings()


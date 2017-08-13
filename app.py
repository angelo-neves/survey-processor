import sys
from survey.Survey import Survey

if __name__ == "__main__":
    two_parameters_given = len(sys.argv) == 3

    if not two_parameters_given:
        sys.exit('You must inform 2 file paths')

    surveyFilePath = sys.argv[1]
    responseFilePath = sys.argv[2]

    survey = Survey(surveyFilePath, responseFilePath)
    survey.print_participation_data()
    survey.print_average_question_ratings()


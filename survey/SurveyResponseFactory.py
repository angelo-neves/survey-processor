from survey.SurveyResponse import SurveyResponse


class SurveyResponseFactory(object):
    def __init__(self, responses_gateway, total_number_of_questions):
        self.responses_list = []

        response_file_lines = responses_gateway.get_all_lines()
        # Validate datatype issues too
        for individual_response_csv in response_file_lines:
            individual_response = SurveyResponse(individual_response_csv, total_number_of_questions)
            self.responses_list.append(individual_response)

    def get_responses_list(self):
        return self.responses_list

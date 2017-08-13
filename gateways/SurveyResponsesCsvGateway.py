from survey.SurveyResponse import SurveyResponse
from gateways.CsvFileGateway import CsvFileGateway


class SurveyResponsesCsvGateway(object):
    responses = []

    def __init__(self, responses_file_path, total_number_of_questions):
        responses_file = CsvFileGateway(responses_file_path)
        responses_file_lines = responses_file.get_all_lines()
        # Validate datatype issues too
        for individual_response_csv in responses_file_lines:
            individual_response = SurveyResponse(individual_response_csv, total_number_of_questions)
            self.responses.append(individual_response)

    def get_responses_list(self):
        return self.responses

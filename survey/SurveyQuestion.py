class SurveyQuestion(object):
    def __init__(self, survey_file_row):
        self.theme = survey_file_row[0]
        self.type = survey_file_row[1]
        self.text = survey_file_row[2]
        self.average_response = 0

    def set_average_response(self, value):
        self.average_response = value

    def get_average_response(self):
        return self.average_response

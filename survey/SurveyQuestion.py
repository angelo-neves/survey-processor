class SurveyQuestion(object):
    def __init__(self, questions_dict):
        self.theme = questions_dict['theme']
        self.type = questions_dict['type']
        self.text = questions_dict['text']
        self.average_response = 0

    def set_average_response(self, value):
        self.average_response = value

    def get_average_response(self):
        return self.average_response

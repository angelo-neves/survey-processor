from survey.SurveyQuestion import SurveyQuestion


class SurveyQuestionFactory(object):
    def __init__(self, questions_gateway):
        self.question_list = []
        questions_file_lines = questions_gateway.get_all_lines_with_keys()
        for question_line in questions_file_lines:
            new_question = SurveyQuestion(question_line)
            self.question_list.append(new_question)

    def get_question_list(self):
        return self.question_list

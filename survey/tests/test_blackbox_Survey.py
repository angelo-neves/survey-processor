import unittest
from io import StringIO
from app import get_survey_from_csv
from survey.SurveyPresenter import SurveyPresenter


class TestsBlackBoxSurvey(unittest.TestCase):
    def test_survey_1(self):
        survey_file = 'test_files/survey-1.csv'
        responses_file = 'test_files/survey-1-responses.csv'
        expected_output = '''+-----------------------------------------------------------+------------------+
| Survey Question                                           | Average Response |
+-----------------------------------------------------------+------------------+
| I like the kind of work I do.                             | 4.60             |
+-----------------------------------------------------------+------------------+
| In general, I have the resources (e.g., business tools,   | 5                |
| information, facilities, IT or functional support) I need |                  |
| to be effective.                                          |                  |
+-----------------------------------------------------------+------------------+
| We are working at the right pace to meet our goals.       | 5                |
+-----------------------------------------------------------+------------------+
| I feel empowered to get the work done for which I am      | 3.60             |
| responsible.                                              |                  |
+-----------------------------------------------------------+------------------+
| I am appropriately involved in decisions that affect my   | 3.60             |
| work.                                                     |                  |
+-----------------------------------------------------------+------------------+
This survey was sent to 6 people.
We received 5 responses.
Participation was 83.33%'''

        survey = get_survey_from_csv(survey_file, responses_file)

        out = StringIO()
        presenter = SurveyPresenter(survey, out)

        presenter.print_rating_questions_averages()
        presenter.print_participation_data()

        output = out.getvalue().strip()

        self.assertEqual(output, expected_output)


from survey import AnonymousSurvey
import unittest
# Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()




# from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """

        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        # my_survey.store_response('English')
        # self.assertIn('English', my_survey.responses)
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        # responses = ['English', 'Spanish', 'Mandarin']
        # for response in responses:
        #     my_survey.store_response(response)
        # for response in responses:
        #     self.assertIn(response, my_survey.responses)
        # return self.responses
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
# TestAnonymousSurvey.test_store_three_responses('Chinese')
if __name__ == '__main__':
    unittest.main()

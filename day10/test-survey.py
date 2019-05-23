import unittest
from survey import Survey

class TestSurvey(unittest.TestCase):
  def test_store_single_response(self):
    question = 'what language did you first learn to speak? '
    my_survey = Survey(question)
    # my_survey.store_response('English')
    # self.assertIn('English', my_survey.responses)
    responses = ['english', 'chinese', 'japanese']
    for res in responses:
      my_survey.store_response(res)
    for res in responses:
      self.assertIn(res,my_survey.responses)

class TestSurvey2(unittest.TestCase):
  def setUp(self):
    question = 'what langauge you like? '
    self.my_survey = Survey(question)
    self.responses = ['c', 'rust', 'webgl']
  def test_store_single_response(self):
    self.my_survey.store_response(self.responses[0])
    self.assertIn(self.responses[0], self.my_survey.responses)
  def test_store_three_responses(self):
    """Test that three individual responses are stored properly."""
    for response in self.responses:
      self.my_survey.store_response(response)
    for response in self.responses:
      self.assertIn(response, self.my_survey.responses)
if __name__ == '__main__':
  unittest.main()














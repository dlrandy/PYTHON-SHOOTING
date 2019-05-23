from survey import Survey
question ='what is your first papapa?'
my_survey = Survey(question)

my_survey.show_question()

print('Enter q at any time to quit.\n')
while True:
  res = input('Language: \n')
  if res == 'q':
    break
  my_survey.store_response(res)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

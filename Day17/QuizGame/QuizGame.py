from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
"""To get more Questions from online : https://opentdb.com/api_config.php open this link, click on API,
    get the json schema copy the list and paste in data.py file"""
question_bank = []
for questions in question_data:
    question_bank.append(Question(questions["question"], questions["correct_answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz \nYour final score is: {quiz.score}/{quiz.question_number}")

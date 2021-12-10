from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

"""To get more Questions from online : https://opentdb.com/api_config.php open this link, click on API,
    get the json schema copy the list and paste in data.py file"""
question_bank = []
for questions in question_data:
    question_bank.append(Question(questions["question"], questions["correct_answer"]))

quiz = QuizBrain(question_bank)
quiz_interface = QuizInterface(quiz)

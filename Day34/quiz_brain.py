import html


class QuizBrain:
    def __init__(self, a_question_list):
        self.question_list = a_question_list
        self.question_number = 0
        self.score = 0
        self.current_question = None

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = html.unescape(self.current_question.question)
        return f"Q.{self.question_number}: {question_text}"

    def validate_answer(self, user_answer):
        if user_answer.lower() == self.current_question.answer.lower():
            self.score += 1
            return True
        else:
            return False

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

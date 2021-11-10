class QuizBrain:
    def __init__(self, a_question_list):
        self.question_list = a_question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_value = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_value.question} (True/False): ")
        self.validate_answer(user_answer, current_value.answer)

    def validate_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}. \n"
              f"Your current score is: {self.score}/{self.question_number} \n")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {html.unescape(self.current_question.text)}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        return user_answer == correct_answer

class Question:   # We're storing questions in the form of objects
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

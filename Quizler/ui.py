from tkinter import *
from PIL import Image, ImageTk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.score = 0
        self.root = Tk()
        self.root.title("Quizzler")
        self.root.config(padx=20, pady=20, bg=THEME_COLOR)

        # Create score label
        self.score_label = Label(self.root, text=f"Score: {self.score}", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Create canvas for Quiz title
        self.canvas = Canvas(self.root, bg="white", width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, width = 280, text="Random Text", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.next_question()

        # Create true and false images
        true_img = Image.open("images/true.png")
        true_img = ImageTk.PhotoImage(true_img)
        self.true_button = Button(self.root, image=true_img, bg=THEME_COLOR,
         command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_img = Image.open("images/false.png")
        false_img = ImageTk.PhotoImage(false_img)
        self.false_button = Button(self.root, image=false_img, bg=THEME_COLOR,
         command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.root.mainloop()
    
    def next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=f"Congratulations! You've completed the quiz, your final score is {self.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")
        self.root.after(1000, func=self.next_question)



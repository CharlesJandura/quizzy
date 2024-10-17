from tkinter import *
from quiz_brain import QuizBrain

# constant theme color code
THEME_COLOR = "#375362"

# class used to make the quiz ui
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # initialize the quiz brain
        self.quiz = quiz_brain

        # create the window and set default values
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR, padx=20, pady=20)

        # create score label, set default values
        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        # place in grid
        self.score_label.grid(row=0, column=1)

        # create canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        # set default values
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="You shouldn't be seeing this",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280
        )
        # place on grid
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # grab file path for true and false icons
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        # create true button
        self.true_button = Button(image=true_image, highlightthickness=0)
        #place on grid
        self.true_button.grid(row=2, column=0)
        # set command to answer_correct method
        self.true_button.config(command=self.answer_correct)
        # create false button
        self.false_button = Button(image=false_image, highlightthickness=0)
        # place on grid
        self.false_button.grid(row=2, column=1)
        # set command to answer_incorrect method
        self.false_button.config(command=self.answer_incorrect)

        # get next question
        self.get_next_question()

        # window main loop
        self.window.mainloop()

    # method used to get next question and display it on ui
    def get_next_question(self):
        # set canvas color to white
        self.canvas.configure(bg="white")

        # if the quiz still has questions left
        if self.quiz.still_has_questions():

            # update the score
            self.score_label.configure(text=f"Score: {self.quiz.score}")
            # update the quiz display
            q_text = self.quiz.next_question()
            # place it on the canvas
            self.canvas.itemconfig(self.question_text, text=q_text)
        # if no more questions
        else:
            # display end output
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            # disable true and false buttons
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    # method used to get user input for true on button press
    def answer_correct(self):
        # use give_feedback method with parameter true
        self.give_feedback(self.quiz.check_answer("true"))

    # method used to user input for false on button press
    def answer_incorrect(self):
        # use give_feedback method with parameter false
        self.give_feedback(self.quiz.check_answer("false"))

    # method used to give feedback after user input
    def give_feedback(self, is_right):
        # if the answer is correct
        if is_right:
            # set the canvas color to green
            self.canvas.configure(bg="green")
            # wait a second, then get next question
            self.window.after(1000, self.get_next_question)
        # is the answer is incorrect
        else:
            # set canvas color to red
            self.canvas.configure(bg="red")
            # wait a second, then get next question
            self.window.after(1000, self.get_next_question)
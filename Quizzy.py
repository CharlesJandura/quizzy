from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# create new list of questions
question_bank = []
# loop through each question in question_data
for question in question_data:
    # set the text to the question parameter
    question_text = question["question"]
    # set answer to correct_answer parameter
    question_answer = question["correct_answer"]
    # grab next question and save it
    new_question = Question(question_text, question_answer)
    # add it to the question bank
    question_bank.append(new_question)

# create a new quiz brain object
quiz = QuizBrain(question_bank)
# create the quiz ui
quiz_ui = QuizInterface(quiz)

# give output
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

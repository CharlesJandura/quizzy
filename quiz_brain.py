import html

# QuizBrain class used to control all quiz logic
class QuizBrain:

    def __init__(self, q_list):
        # default parameters
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    # method used to check if there are questions left
    def still_has_questions(self):
        # return the question if the question number is less than the list length
        return self.question_number < len(self.question_list)

    # method used to get and display next question
    def next_question(self):
        # set the current question to the next in queue
        self.current_question = self.question_list[self.question_number]
        # uptick queue number
        self.question_number += 1
        # display output
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    # method used to check if the user input is correct
    def check_answer(self, user_answer):
        # store the answer for current question
        correct_answer = self.current_question.answer
        # if the users answer is the same as the question answer
        if user_answer.lower() == correct_answer.lower():
            # uptick score and return true
            self.score += 1
            return True
        else:
            return False


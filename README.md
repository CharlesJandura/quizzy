## Quizzy
# A simple OOP based quiz game using Open Trivia Database's API
________________________________________________________________________
## How To Use
Download the Quizzy folder and navigate to Quizzy\dist and run the Quizzy.exe file!

## Files

# images
Simple icons used for the true and false buttons for the UI

# Quizzy.py
The main file of the project! All it does is run the main logic of the program
while allowing the other files to do the heavy lifting.

# data.py
This the file that grabs information from the Open Trivia Database API using the requests module.
It simply grabs the data of your choosing(allowing you to choose amount of questions and type of questions)
and stores the questions for later use.

# question_model.py
This simple file just creates a class that stores our question model. Only used for oganizational purposes.

# quiz_brain.py
This is the heavy lifter of the program controlling the main logic, hence the name "Quiz Brain"!
This file is mainly used for keeping track of the current question the user is on, checking if the
answer is correct, and keeping track of the score.

# ui.py
This file creates and controls all of the UI used in the program, from screen to buttons.

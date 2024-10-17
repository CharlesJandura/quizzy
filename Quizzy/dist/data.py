import requests

# base parameters for amount of questions and question type
parameters = {
    "amount": 10, # 10 questions
    "type": "boolean" # true or false questions
}

# use requests library to access opentdb api using parameters dict and save in data field
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

# store the questions in a new field
question_data = data["results"]

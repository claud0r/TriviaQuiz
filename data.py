import requests
import config

parameters = {
    "amount": config.QUESTION_AMOUNT,
    "type": "boolean",
    "category": config.QUESTION_CATEGORY,
    "difficulty": config.QUESTION_DIFFICULTY,
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]

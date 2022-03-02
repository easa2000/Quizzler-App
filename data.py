import requests

parameter = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
    }

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&type=boolean", params=parameter)
response.raise_for_status()
data = response.json()
question_data = data["results"]

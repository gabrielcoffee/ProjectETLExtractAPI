import requests
import json
import os

url = 'https://api.openai.com/v1/chat/completions'

open_ai_api_key = os.getenv('OPEN_AI_API_KEY')

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {open_ai_api_key}'
}

data = {
    'model': 'gpt-3.5-turbo',
    'messages': [
        {'role': 'user', 'content': 'Qual a capital do Brasil?'}
    ]
}

# we need to convert the dictionary to a string, we can do this using json.dumps(data)
# this will convert the dictionary to a json string, and then we can pass this string to the request library
response = requests.post(url, headers=headers, data=json.dumps(data))

print(response)
print(response.json()['choices'][0]['message']['content'])
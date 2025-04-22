import requests
import json

url = 'https://api.openai.com/v1/chat/completions'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer chatgpt-api-key'
}

data = {
    'model': 'gpt-3.5-turbo',
    'messages': [
        {'role': 'user', 'content': 'Qual a capital do Brasil?'}
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response)
print(response.json()['choices'][0]['message']['content'])
import os
import requests

API_KEY = os.environ['OPENAI_API_KEY']

def chatgpt(prompt):
    try:
        response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', json={
            'prompt': prompt,
            'max_tokens': 100,
            'temperature': 0.7,
            'n': 1,
            'stop': '\n'
        }, headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        })
        response.raise_for_status()
        message = response.json()['choices'][0]['text']
        return message
    except requests.exceptions.HTTPError as e:
        return f'API error: {e}'
        
def test_chatgpt():
    prompt = "Hello, ChatGPT!"
    expected_response = "This is the response from ChatGPT."
    
    with requests_mock.Mocker() as mock:
        mock.post('https://api.openai.com/v1/engines/davinci-codex/completions',
                  json={"choices": [{"text": expected_response}]})
        
        response = chatgpt(prompt)
        assert response == expected_response

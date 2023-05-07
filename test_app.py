import os
import requests_mock
import app

def test_index():
    client = app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Enter your prompt here" in response.data

def test_results():
    client = app.app.test_client()
    response = client.post('/results', data={'prompt': 'Hello, ChatGPT!'})
    assert response.status_code == 200
    assert b"Your results are ready" in response.data
    assert b"Hello, ChatGPT!" in response.data

def test_chatgpt_api():
    prompt = "Hello, ChatGPT!"
    expected_response = "This is the response from ChatGPT."
    
    with requests_mock.Mocker() as mock:
        mock.post('https://api.openai.com/v1/engines/davinci-codex/completions',
                  json={"choices": [{"text": expected_response}]})
        
        response = app.chatgpt(prompt)
        assert response == expected_response

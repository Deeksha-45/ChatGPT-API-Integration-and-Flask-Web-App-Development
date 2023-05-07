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

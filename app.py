import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['API_KEY'] = os.environ['OPENAI_API_KEY']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    prompt = request.form['prompt']
    if prompt == '':
        return render_template('index.html', error='Please enter a prompt.')

    try:
        response = requests.post('https://api.openai.com/v1/engines/davinci/completions', json={
            'prompt': prompt,
            'max_tokens': 100,
            'temperature': 0.7,
            'n': 1,
            'stop': '\n'
        }, headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {app.config["API_KEY"]}'
        })

        response.raise_for_status()
        message = response.json()['choices'][0]['text']
        return render_template('results.html', message=message)

    except requests.exceptions.HTTPError as e:
        return render_template('index.html', error='An error occurred while processing your request. Please try again later.')

if __name__ == '__main__':
    app.run(debug=True)

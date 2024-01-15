from flask import Flask
import random
import time

app = Flask(__name__)  # Indent for clarity

welcome_messages = [
    'Welcome to Journey of Devops and CICD',
    'Welcome to Chennai',
    'Another dynamic message'
]

@app.route('/')
def hello_world():
    return random.choice(welcome_messages)

if __name__ == '__main__':  # Double underscore for main
    while True:
        app.run(debug=True, host='0.0.0.0')
        time.sleep(60)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return f'''Welcome to Devops and CICD!

Embrace the seamless integration of development and operations for efficient software delivery.
Unlock the power of automation to streamline your workflows and achieve faster time to market.
Build a culture of continuous improvement and innovation through effective CI/CD practices.
Let's embark on a journey of agility and resilience in software development together!'''

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')

from flask import Flask
app = Flask(__name__)

@app.route('/') #this is a decorator
def hello_world():
    return 'Hello Liberty and Azariah'
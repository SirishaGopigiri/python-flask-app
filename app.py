from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return "hello world!"

@app.route('/return_version')
def return_app_version():
    return "Running test app on version 3.0 !!!", 500

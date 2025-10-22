# app.py

# Import the Flask class from the flask package
from flask import Flask

# Create an app object from the Flask class
app = Flask(__name__)

# Define what happens when someone visits the main page "/"
@app.route('/')
def home():
    return "Hello, Guy! Welcome to your Flask app."

# Run the app when you start this file
if __name__ == '__main__':
    app.run(debug=True)

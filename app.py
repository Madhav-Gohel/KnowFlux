from flask import Flask, render_template, request, redirect, url_for
import methods
import cs50

# Initialize CS50 library
db = cs50.SQL("sqlite:///database.db")

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
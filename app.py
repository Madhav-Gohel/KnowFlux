from flask import Flask, render_template, request, redirect, url_for
import methods
import prompts
import cs50


global topics
global level
global subject

# Initialize CS50 library
db = cs50.SQL("sqlite:///database.db")
db.execute("CREATE TABLE IF NOT EXISTS topics (id INTEGER PRIMARY KEY, subject TEXT, level TEXT, topics TEXT)")

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-topics', methods=['POST'])
def generate_topics():
    global subject
    subject = request.form.get('subjectName')
    global level
    level = request.form.get('knowledgeLevel')

    if not subject or not level:
        return redirect(url_for('home'))

    prompt = prompts.generate_topics_prompt(subject, level)
    global topics
    topics = methods.generate(prompt)

     # Store the response in the database
    # db.execute("INSERT INTO topics (subject, level, topics) VALUES (?, ?, ?)", subject, level, response)
    return render_template('topics.html', subject=subject, level=level, topics=eval(topics))

@app.route('/generate-content')
def generate_content():
    # Fetch topics from the database
    prompt = prompts.generate_content_prompt(subject, level, topics)
    content = methods.generate(prompt)

    return render_template('content.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)
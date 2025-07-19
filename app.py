from flask import Flask, render_template, request, redirect, url_for, session
import json
import random
from datetime import datetime

# ✅ Define the Flask app first
app = Flask(__name__)
app.secret_key = 'quiz_secret_key'

# Load questions from JSON
with open('questions.json') as f:
    all_questions = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    username = request.form.get('username')
    session['username'] = username
    session['questions'] = random.sample(all_questions, 30)
    session['current'] = 0
    session['responses'] = []
    return redirect(url_for('question'))

@app.route('/question', methods=['GET', 'POST'])
def question():
    if request.method == 'POST':
        selected = request.form.get('answer')
        current = session.get('current')
        questions = session.get('questions')
        q = questions[current]
        session['responses'].append({
            'question': q['question'],
            'selected': selected,
            'correct_answer': q['answer'],
            'is_correct': selected == q['answer'],
            'difficulty': q['difficulty']
        })
        session['current'] += 1

    if session['current'] >= len(session['questions']):
        return redirect(url_for('result'))

    current = session['current']
    question = session['questions'][current]
    return render_template('question.html', question=question, index=current + 1)

@app.route('/result')
def result():
    username = session.get('username')
    responses = session.get('responses')
    total_score = sum(1 for r in responses if r['is_correct'])

    # 🎯 Final message
    if total_score >= 25:
        message = "🌟 Excellent work! You nailed it!"
    elif total_score >= 15:
        message = "👏 Good job! You’ve got solid knowledge."
    elif total_score >= 8:
        message = "🙂 Not bad, but there’s room to improve."
    else:
        message = "📝 Keep practicing! You’ll get there!"

    # Difficulty-wise score breakdown
    difficulty_scores = {
        'Easy': {'correct': 0, 'total': 0},
        'Medium': {'correct': 0, 'total': 0},
        'Hard': {'correct': 0, 'total': 0}
    }

    for r in responses:
        diff = r['difficulty'].capitalize()
        if diff in difficulty_scores:
            difficulty_scores[diff]['total'] += 1
            if r['is_correct']:
                difficulty_scores[diff]['correct'] += 1

    # Save score to scores.json
    score_entry = {
        'name': username,
        'score': total_score,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M')
    }

    try:
        with open('scores.json', 'r+') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
            data.append(score_entry)
            f.seek(0)
            json.dump(data, f, indent=2)
    except FileNotFoundError:
        with open('scores.json', 'w') as f:
            json.dump([score_entry], f, indent=2)

    return render_template(
        'result.html',
        username=username,
        total_correct=total_score,
        total_questions=len(responses),
        results=responses,
        final_message=message,
        difficulty_scores=difficulty_scores
    )

if __name__ == '__main__':
    app.run(debug=True)

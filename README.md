Online Quiz Web Application

Introduction

The Online Quiz Web App is a dynamic, educational platform built using **Flask (Python)** for the backend and **HTML/CSS** for the frontend. It allows users to take a 30-question quiz consisting of randomly selected questions from multiple subjects like General Knowledge, Programming, Math, English, Social Science, and Current Affairs. Each question is timed with a 10-second countdown and categorized by difficulty (Easy, Medium, Hard). Users can view their performance breakdown at the end of the quiz.

Objective

The main objectives of this mini project are to:
- Demonstrate the integration of a Python backend using Flask with a modern frontend UI.
- Provide quiz functionality with real-time timer and score tracking.
- Teach full-stack concepts like session handling, template rendering, form submission, and data storage using JSON.

Features
- Enter your name to begin the quiz
- One question per screen
- 10-second timer per question
- Auto-submit or manual "Next" option
- 30 randomly selected questions from a pool
- Categorized difficulty level shown on each question
- Final score summary with personalized feedback
- Breakdown of scores by difficulty (Easy, Medium, Hard)
- Visually enhanced UI with CSS animations and colors
- Correct vs Incorrect answers shown on result page
- Scores saved to a JSON file for future use

Technologies Used

Frontend:
- HTML5
- CSS3
- Google Fonts (e.g., Poppins)
- JavaScript (for timer)

Backend:
- Python 3.x
- Flask micro web framework
- Jinja2 templating engine
- JSON for question and score storage

File Structure

online_quiz_app/
├── app.py
├── questions.json
├── scores.json
├── templates/
│   ├── index.html
│   ├── question.html
│   ├── result.html
├── static/
│   └── style.css
├── venv/


Implementation Details

Backend (Flask):
- `app.py` handles all the logic including routing, session storage, randomizing questions, timer handling, saving scores, and rendering templates.
- The questions and user scores are read and written to JSON files.

Frontend (HTML + CSS):
- HTML templates dynamically render each question and result.
- CSS provides an attractive UI with lavender-themed background, styled buttons, and layout effects.

Styling Highlights:
- Lavender background and colorful layout
- One-question-per-page layout
- Timer alert box styled in red
- Final message with emojis
- Correct answers highlighted in green, wrong ones in red

7. How to Run the Project
1. Ensure Python 3.x is installed.
2. Create and activate a virtual environment:

Windows
python -m venv venv
venv\Scripts\activate

Linux/macOS
python3 -m venv venv
source venv/bin/activate


Install Flask:
pip install flask

Run the application:
python app.py

Open the app in your browser:
http://127.0.0.1:5000/

Future Enhancements
- Add audio feedback for correct/wrong answers
- Add dark mode toggle for the UI
- Integrate login/authentication
- Store data in a SQLite or PostgreSQL database
- Allow users to choose quiz category or difficulty range
- Add image or video-based questions
- Show chart visualization (pie/bar) on results page

Conclusion

The Online Quiz Web App mini project demonstrates essential full-stack web development principles using Flask and modern HTML/CSS. It is designed for students, educators, and developers looking to build interactive web apps with dynamic features like timers, randomization, and detailed results. With simple extension points, it is highly customizable and ready for enhancement.
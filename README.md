# 🧠 QuizArena – A Streamlit-Based Trivia Game (OOP in Python)

QuizArena is a multiplayer-ready, session-based quiz game built using **Streamlit** and structured
with **Object-Oriented Programming (OOP)** in Python. It supports login, custom questions, timed answers,
scoring, and motivational feedback.

---

## 🚀 Features

- 🧩 User Login / Signup system
- ❓ Randomly generated questions
- ⏱️ Countdown timer for each question
- ✅ Score tracking and feedback
- 🔁 Replay option with session reset
- 🧠 Educational structure following OOP principles
- 🎈 Celebratory Balloons for Perfect Scores
---

## 🛠️ Tech Stack

| Component      | Tech Used         |
|----------------|-------------------|
| Frontend       | Streamlit         |
| Backend Logic  | Python (OOP)      |
| Storage        | JSON (file-based) |
| Timer          | Custom countdown  |

---

💡 OOP Concepts Used
    ✅ 1. Encapsulation
Data like users and score is hidden in methods within classes or modules.
def add_user(username, password):
    # handles JSON file I/O internally

     🧱 2. Abstraction
Implementation details (e.g., file handling) are hidden behind simple interfaces like init_db() or get_question().

     🔁 3. Inheritance (Extendable)
While not fully used yet, the project can be extended with classes like Player(User) or MCQ(Question) to implement inheritance.

     🔄 4. Polymorphism (Extendable)
Future versions may support different types of questions (e.g., MCQ, True/False), each implementing a shared ask() method differently.

🔐 User Authentication

User data is stored in a simple JSON file: db/users.json.
It supports:

User Registration (add_user)
User Login (get_user)
File auto-initialization handled by init_db()

📚 How It Works

On app startup, init_db() checks and creates the database file.
User must log in to access the quiz.
Each game pulls 5 random questions.
Countdown timer gives 10 seconds per question.
Score is tracked in st.session_state.
Final score shown after all questions


🧠 Educational Value

This project is ideal for:
Students learning Python OOP
Developers building Streamlit apps
Hackathon or startup MVPs

👨‍💻 Author
Developed by [Anum Rajput] as a demo of Streamlit + Python OOP.

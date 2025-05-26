import streamlit as st
from game.questions import get_question
from utils.timer import countdown_timer

def start_game():
    if "user" not in st.session_state:
        st.warning("🔐 Please login first to play the game.")
        return

    if "questions" not in st.session_state:
        st.session_state.questions = [get_question() for _ in range(5)]
        st.session_state.current_q = 0
        st.session_state.score = 0

    total_questions = len(st.session_state.questions)

    if st.session_state.current_q < total_questions:
        q = st.session_state.questions[st.session_state.current_q]

        st.markdown("<h2 style='color:#4CAF50;'>🧠 QuizArena</h2>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='color:#2196F3;'>Question {st.session_state.current_q + 1} of {total_questions}</h4>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:18px;'>{q['question']}</p>", unsafe_allow_html=True)

        options = q["options"]
        user_answer = st.radio("👉 Choose your answer:", options, key=f"q_{st.session_state.current_q}")

        countdown_timer(10)  # Timer runs for each question

        if st.button("🚀 Submit Answer"):
            if user_answer == q["answer"]:
                st.session_state.score += 1
                st.success("✅ Correct Answer!")
                st.balloons()
            else:
                st.error(f"❌ Wrong! The correct answer was: **{q['answer']}**")

            st.session_state.current_q += 1
            st.rerun()

    else:
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown(
            f"<h2 style='color:#FF9800;'>🏁 Final Score: "
            f"<span style='color:#4CAF50;'>{st.session_state.score}/{total_questions}</span></h2>",
            unsafe_allow_html=True
        )

        # 🎯 Motivational message
        if st.session_state.score == total_questions:
            st.balloons()
            st.success("🎉 Perfect Score! You're a quiz master!")
        elif st.session_state.score >= 3:
            st.info("👍 Good job! Keep practicing.")
        else:
            st.warning("💡 Keep learning! Try again.")

        # 🔁 Reset game
        if st.button("🔄 Play Again"):
            del st.session_state.questions
            del st.session_state.current_q
            del st.session_state.score
            st.rerun()


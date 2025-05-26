# import streamlit as st
# from game.questions import get_question
# from utils.timer import countdown_timer

# def start_game():
#     if "user" not in st.session_state:
#         st.warning("🔐 Please login first to play the game.")
#         return

#     st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🧠 Welcome to QuizArena!</h1>", unsafe_allow_html=True)

#     # Initialize session state
#     if "score" not in st.session_state:
#         st.session_state.score = 0
#     if "question_index" not in st.session_state:
#         st.session_state.question_index = 0
#     if "questions" not in st.session_state:
#         st.session_state.questions = [get_question() for _ in range(5)]
#     if "answered" not in st.session_state:
#         st.session_state.answered = False

#     # Game End
#     if st.session_state.question_index >= 5:
#         st.markdown(
#             f"<h2 style='color: #FF9800;'>🏁 Final Score: <span style='color:#4CAF50;'>{st.session_state.score}/5</span></h2>",
#             unsafe_allow_html=True
#         )
#         if st.session_state.score == 5:
#             st.balloons()
#             st.success("🎉 Perfect Score! You're a quiz master!")
#         elif st.session_state.score >= 3:
#             st.info("👍 Good job! Keep practicing.")
#         else:
#             st.warning("💡 Keep learning! Try again.")

#         if st.button("🔁 Play Again"):
#             for key in ["score", "question_index", "questions", "answered"]:
#                 del st.session_state[key]
#             st.rerun()
#         return

#     # Show current question
#     q = st.session_state.questions[st.session_state.question_index]
#     st.markdown(f"<h3 style='color: #2196F3;'>Question {st.session_state.question_index + 1}</h3>", unsafe_allow_html=True)
#     st.markdown(f"<p style='font-size:18px;'>{q['question']}</p>", unsafe_allow_html=True)

#     options = q["options"]
#     answer = st.radio("👉 Select one option:", options, key=f"q_{st.session_state.question_index}")

#     countdown_timer(10)

#     if not st.session_state.answered:
#         if st.button("🚀 Submit Answer"):
#             if answer == q["answer"]:
#                 st.session_state.score += 1
#                 st.success("✅ Correct Answer! Well Done!")
#             else:
#                 st.error(f"❌ Wrong Answer! Correct: **{q['answer']}**")
#             st.session_state.answered = True
#             st.stop()

#     if st.session_state.answered:
#         if st.button("➡️ Next Question"):
#             st.session_state.question_index += 1
#             st.session_state.answered = True
#             st.rerun()

















# import streamlit as st
# from game.questions import get_question
# from utils.timer import countdown_timer

# def start_game():
#     if "user" not in st.session_state:
#         st.warning("🔐 Please login first to play the game.")
#         return

#     st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🧠 Welcome to QuizArena!</h1>", unsafe_allow_html=True)
#     score = 0

#     for i in range(5):  # 5 questions
#         st.markdown(f"<h3 style='color: #2196F3;'>Question {i + 1}</h3>", unsafe_allow_html=True)

#         q = get_question()
#         st.markdown(f"<p style='font-size:18px;'>{q['question']}</p>", unsafe_allow_html=True)

#         options = q["options"]
#         answer = st.radio("👉 Choose your answer:", options, key=f"q_{i}_options")

#         countdown_timer(10)

#         if st.button("🚀 Submit Answer", key=f"submit_{i}"):
#             if answer == q["answer"]:
#                 score += 1
#                 st.success("✅ Correct Answer! Well Done!")
#                 st.balloons()
#             else:
#                 st.error(f"❌ Oops! The correct answer was: **{q['answer']}**")
#             st.markdown("---")

#     st.markdown(
#         f"<h2 style='color: #FF9800;'>🏁 Final Score: <span style='color:#4CAF50;'>{score}/5</span></h2>",
#         unsafe_allow_html=True
#     )

#     if score == 5:
#         st.balloons()
#         st.success("🎉 Perfect Score! You're a quiz master!")
#     elif score >= 3:
#         st.info("👍 Good job! Keep practicing.")
#     else:
#         st.warning("💡 Keep learning! Try again.")
































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


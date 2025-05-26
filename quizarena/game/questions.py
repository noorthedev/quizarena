import random

questions = [
    {"question": "what is the capital of india?", "options": ["delhi", "mumbai", "kolkata", "chennai"], "answer": "delhi"},
    {"question": "Capital of France?", "options": ["Paris", "Rome", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "5 + 7 = ?", "options": ["10", "11", "12", "13"], "answer": "12"},
    {"question": "Water's chemical formula?", "options": ["H2O", "O2", "NaCl", "CO2"], "answer": "H2O"},
    {"question": "Fastest animal?", "options": ["Cheetah", "Tiger", "Leopard", "Horse"], "answer": "Cheetah"}
]

def get_question():
    return random.choice(questions)

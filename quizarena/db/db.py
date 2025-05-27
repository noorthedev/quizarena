import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "quiz_data.json")

def get_user(username, password):
    with open(DB_FILE, "r") as f:
        users = json.load(f)
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
    return None

def add_user(username, password):
    with open(DB_FILE, "r") as f:
        users = json.load(f)
    if any(u["username"] == username for u in users):
        return False
    users.append({"username": username, "password": password})
    with open(DB_FILE, "w") as f:
        json.dump(users, f)
    return True

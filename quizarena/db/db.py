import json
import os

DB_FILE = "db/users.json"

def init_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump([], f)
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

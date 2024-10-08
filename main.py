from fastapi import FastAPI

app = FastAPI()

fake_users = [
    {"id": 1, "name": "<NAME>", "email": "<EMAIL>"},
    {"id": 2, "name": "<NAME>", "email": "<EMAIL>"},
]

@app.get("/users/{user_id}")
def get_users(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]

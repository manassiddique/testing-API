
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Students: FastAPI App",
              version="1.2.0",
              description="A simple To-Do application using FastAPI.")

# Pydantic model for task structur
class Task(BaseModel):
    id: int
    text: str
    done: bool = False

# In-memory list (data reset hota hai jab server restart hota hai)
tasks = [
    Task(id=1, text="Learn FastAPI", done=False),
    Task(id=2, text="Build a To-Do App", done=False),
    Task(id=3, text="Test the App", done=False)
]

@app.get("/Anas")
def home():
    return {"message": "Welcome to FastAPI To-Do App! Visit /docs for API UI."}

@app.get("/tasks")
def get_tasks():
    return tasks



@app.get("/porn_hub")
def get_pornhub():
    return {"message": "Welcome to Porn Hub!"}

@app.get("/student_list")
def get_student_list():
    return{"Hashim Amla  Teacher "
           "Anas Siddique Student"
           "Sami Ullah Elactritian"
           "Captain Talha Umair"
           "DVM Touseef Khalid"}
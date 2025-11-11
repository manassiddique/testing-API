
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# (title="Students: FastAPI App",
#               version="1.2.0",
#               description="A simple To-Do application using FastAPI.")

# Pydantic model for task structur
# class Task(BaseModel):
#     id: int
#     text: str
#     done: bool = False

# # In-memory list (data reset hota hai jab server restart hota hai)
# tasks = [
#     Task(id=1, text="Learn FastAPI", d
#          one=False),
#     Task(id=2, text="Build a To-Do App", done=False),
#     Task(id=3, text="Test the App", done=False)
# ]

# @app.get("/Anas")
# def home():
#     return {"message": "Welcome to FastAPI To-Do App! Visit /docs for API UI."}

# @app.get("/tasks")
# def get_tasks():
#     return tasks



# @app.get("/porn_hub")
# def get_pornhub():
#     return {"message": "Welcome to Porn Hub!"}

# @app.get("/student_list")
# def get_student_list():
#     return{"Hashim Sardar"
#            "Anas Siddique"
#            "Sami Ullah"
#            "Talha Umair"
#            "Touseef Khalid"
#            "Zarrar patwari"}


# from typing import List

# class Student(BaseModel):
#     id: int
#     name: str
#     profession: str

# @app.get("/student_list", response_model=List[Student])
# def get student_list():
#     return [
#         Student(id=1, name="Anas Siddique", profession="ics 2ndyear"),
#         Student(id=2, name="Hashim Sardar", profession="Software Engineer"),
#         Student(id=3, name="SamiUllah", profession="Associate Engineer"),
#         Student(id=4, name="Zarrar Siddique", profession="8th Science"),
#         Student(id=5, name="Haseeb Khalid", profession="English Letrature"),
#     ]



@app.get("/student_list")
def get_student_list():
    return[
        Student(id=1, name="Anas Siddique"),
        Student(id=2, name="Zarrar Siddique"),
        Student(id=3, name="Hashim Sardar"),
        Student(id=4, name="Haseeb Khalid"),
        Student(id=5, name="Touseef Khalid")
    ]

class Student(BaseModel):
    id=int
    name=str





@app.get("/student_standerds")
def get_student_standerd():
    return{
        Student(id=1, name="Anas Siddique",standerd="ICS Physics"),
        Student(id=2, name="Zarrar Siddique",standerd="8th Science"),
        Student(id=3, name="Hashim Sardar",standerd="BS SE"),
        Student(id=4, name="Haseeb Khalid",standerd="Mphil English"),
        Student(id=5, name="Touseef Khalid",standerd="DVM"),
    }

class student(BaseModel):
    id=int
    name=str
    standerd=str





@app.get("/student_phonenumber")
def get_student_phonenumber():
    return{
        Student(id=1,name="Anas Siddique",phonenumber="0327 7690402"),
        Student(id=2,name="Zarrar Siddique",phonenumber="0332 0786265"),
        Student(id=3,name="Hashim Sardar",phonenumber="0300 0000000"),
        Student(id=4,name="Haseeb Khalid",phonenumber="0317 0615131"),
        Student(id=5,name="Touseef Khalid",phonenumber="0300 0000000"),
    }


class student(BaseModel):
    id=int
    name=set
    phonenumber=int




@app.get("/student_adress")
def get_student_adress():
    return{
        Student(id=1,name="Anas Siddique",adress="chak 475 Samundri"),
        Student(id=2,name="Zarrar Siddique",adress="chak 475 Samundri"),
        Student(id=3,name="Hashim Sardar",adress="chak 475 Samundri"),
        Student(id=4,name="Haseeb Khalid",adress="chak 475 Samundri"),
        Student(id=5,name="Touseef Khalid",adress="chak 475 Samundri"),
    }


class student(BaseModel):
    id=int
    name=str
    adress=str




@app.get("/student_skills")
def get_student_skills():
    return{
        Student(id=1,name="Anas Siddique",skills="python"),
        Student(id=2,name="Zarrar Siddique",skills="PUBG"),
        Student(id=3,name="Hashim Sardar",skills="Developing"),
        Student(id=4,name="Haseeb Khalid",skills="Teaching"),
        Stjjjudent(id=5,name="Touseef Khalid",skills="Vet"),
    }

class student(BaseModel):
    id=int
    name=str
    skills=str




@app.get("/student_age")
def get_student_age():
    return{
        Student(id=1,name="Anas Siddique",age="18"),
        Student(id=2,name="Zarrar Siddique",age="16"),
        Student(id=3,name="Hashim Sardar",age="28"),
        Student(id=4,name="Haseeb Khalid",age="25"),
        Student(id=5,name="Touseef Khalid",age="28"),
    }


class student(BaseModel):
    id=int
    name=str
    age=int




@app.get("/student_height/{ID}")
def get_student_height():
    return{
        Student(id=1,name="Anas Siddique",height="5.10"),
        Student(id=2,name="Zarrar Siddique",height="5.9"),
        Student(id=3,name="Hashim Sardar",height="5.9"),
        Student(id=4,name="Haseeb Khalid",height="5.9"),
        Student(id=5,name="Touseef Khalid",height="5.9"),
    }


class student(BaseModel):
    id=int
    name=str
    height=int




@app.get("/student_weight")
def get_student_weight():
    return{
        Student(id=1,name="Anas Siddique",weight="55"),
        Student(id=2,name="Zarrar Siddique",weight="60"),
        Student(id=3,name="Hashim Sardar",weight="90"),
        Student(id=4,name="Haseeb Khalid",weight="50"),
        Student(id=5,name="Touseef Khalid",weight="70"),
    }



from fastapi import FastAPI
from starlette.responses import JSONResponse
from pydantic import BaseModel
from starlette.requests import Request
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur FastAPI sous Windows"}

@app.get("/hello")
def read_hello():
    return JSONResponse({"message": "Hello world"}, status_code=200)

@app.get("/welcome")
def read_welcome(request: Request, name: str = "Non défini"):
    return JSONResponse({"message": f"Hello {name}"}, status_code=200)

class Student (BaseModel):
    Reference : str
    FirstName : str
    LastName : str
    Age : int

students_store: List[Student] = []

def serialized_stored_students():
    student_converted = []
    for student in students_store:
        student_converted.append(student.model_dump())
    return student_converted

@app.post("/student")
def new_student(student_payload: List[Student]):
    students_store.extend(student_payload)
    return {"students": serialized_stored_students()}

@app.get("/students")
def list_students():
    return JSONResponse(content={"students": serialized_stored_students()}, status_code=200)

@app.put("/students")
def update_or_create_students(student_payload: List[Student]):
    global students_store  

    for new_event in student_payload:
        found = False
        for i, existing_student in enumerate(students_store):
            if new_event.Reference == existing_student.Reference:
                students_store[i] = new_student
                found = True
                break
        if not found:
            students_store.append(new_student)
    return {"students": serialized_stored_students()}
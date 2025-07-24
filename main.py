from fastapi import FastAPI
from starlette.responses import JSONResponse
from pydantic import BaseModel
from starlette.requests import Request

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
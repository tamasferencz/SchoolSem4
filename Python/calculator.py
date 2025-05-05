from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Operation(BaseModel):
    a: float
    b: float

@app.get("/")
def read_root():
    return {"message": "Simple Calculator API"}

@app.post("/add")
def add(op: Operation):
    return {"result": op.a + op.b}

@app.post("/subtract")
def subtract(op: Operation):
    return {"result": op.a - op.b}

@app.post("/multiply")
def multiply(op: Operation):
    return {"result": op.a * op.b}

@app.post("/divide")
def divide(op: Operation):
    if op.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
    return {"result": op.a / op.b}

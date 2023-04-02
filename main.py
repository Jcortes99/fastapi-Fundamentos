from typing import Optional
from fastapi import FastAPI, Body, Query
from Domain.models import Person

app = FastAPI()

@app.get('/')
def home():
    return {'Hello': 'World'}

@app.post('/person/new')
def create_person(persona: Person = Body(...)):
    return persona

@app.get("/peron/detail")
def show_person(
    name: Optional[str]= Query(None, min_length=1, max_length=10),
    age: int = Query(...)
):
    return{name, age}
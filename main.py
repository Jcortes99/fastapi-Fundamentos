from typing import Optional
from fastapi import FastAPI, Body, Query, Path
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
    name: Optional[str]= Query(
        None,
        min_length=1,
        max_length=10,
        title="Person name",
        description="The name of the person"
        ),
    age: int = Query(...,
                    title="Person age",
                    description="Require person age"
                    )
):
    return{name, age}

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(...,
                        gt=0,
                        title="Person id",
                        description="Require person id")
):
    return {person_id: "It exists!"}
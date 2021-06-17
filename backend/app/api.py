from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.note import Note, Base
from fastapi.encoders import jsonable_encoder
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from sqlalchemy import DATETIME
from pydantic import BaseModel
from typing import Optional, List
import os

load_dotenv()
app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url="sqlite:///back.db")


class NoteScheme(BaseModel):
    id: Optional[int]
    title: str

    class Config:
        orm_mode = True


origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

todos = [
    {
        "id": "1",
        "item": "Read a book."
    },
    {
        "id": "2",
        "item": "Cycle around town."
    }
]


@app.get("/todo", response_model=List[NoteScheme])
async def get_todos():
    note = db.session.query(Note).all()
    return note


"""
@app.get("/todo", tags=["todos"])
async def get_todos() -> dict:
    return {"data": todos}


"""

"""
@app.get("/todo", tags=["todos"])
async def get_todos() -> dict:
    note = db.session.query(Note).all()
    return {"data": note}
"""
"""
@app.get("/notes")
async def index():
    notes = db.session.query(Note).all()
    result = jsonable_encoder({
        "notes": notes
    })
    return JSONResponse(status_code=200, content={
        "status_code": 200,
        "result": result
    })

"""


@app.post("/todo", tags=["todos"])
async def add_todo(todo: NoteScheme):
    todos.append(todo)
    note = Note(title=todo.title)
    db.session.add(note)
    db.session.commit()


    return {
        "data": {"Todo added."}
    }


"""

"""


@app.put("/todo/{id}", tags=["todos"])
async def update_todo(id: int, body: dict) -> dict:
    note = db.session.query(Note).get(id)
    note.title = body["item"]
    db.session.commit()
    return {}


@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int):
    note = db.session.query(Note).get(id)
    db.session.delete(note)
    db.session.commit()
    return {"id": id}



@app.get ("/todo/search", tags=["todos"],response_model=List[NoteScheme])
async def search (search_string:str):
    search = "%{}%".format(search_string)
    todos = db.session.query(Note).filter(Note.title.like(search)).all()
    return todos






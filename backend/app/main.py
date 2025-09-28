import os
from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

# Pydantic model for note item.
class note_item(BaseModel):
    title: str
    description: str
    done: bool

app = FastAPI()

# MONGO_URL = f"mongodb://{os.getenv('MONGO_INITDB_ROOT_USERNAME')}:"\
#             f"{os.getenv('MONGO_INITDB_ROOT_PASSWORD')}@"\
#             f"{os.getenv('MONGO_HOST')}:{os.getenv('MONGO_PORT')}/"\
#             f"{os.getenv('MONGO_INITDB_DATABASE')}"\
#             f"?authSource=admin"

# FULL URL:
MONGO_URL = "mongodb://noteappadmin:noteappsecret@mongodb:27017/noteappdb?authSource=admin"

client = AsyncIOMotorClient(MONGO_URL)
note_db = client.get_database()



@app.post("/note", response_model=note_item, status_code=201)
async def create_note(note: note_item):
    # Insert the note into MongoDB.
    result = await note_db.notes.insert_one(note.model_dump())
    created_note = note.model_dump()
    created_note["id"] = str(result.inserted_id)
    return created_note

@app.get("/notes")
async def get_note():
    # Create a list to hold notes.
    notes_collected = []
    # Retrieve notes from MongoDB.
    notes_reference = note_db.notes.find()
    async for note in notes_reference:
        # Convert ObjectId to string.
        note["id"] = str(note["_id"])
        # Remove the _id field from the note. It can cause error.
        note.pop("_id")
        notes_collected.append(note)
    return notes_collected

@app.get("/note/{id}")
async def get_note_id(id: str):
    note = await note_db.notes.find_one({"_id": ObjectId(id)})
    if note is not None:
        # Convert ObjectId to string.
        note["id"] = str(note["_id"])
        note.pop("_id")
        return note
    return {"error": "Note not found"}



@app.put("/note")
def update_note():
    return {"message": "PUT: Hello World"}


@app.delete("/note")
def delete_note():
    return {"message": "DELETE: Hello World"}


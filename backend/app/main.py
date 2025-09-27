import os
from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient

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
    result = await note_db.notes.insert_one(note.model_dump())
    created_note = note.model_dump()
    created_note["id"] = str(result.inserted_id)
    return created_note

@app.get("/note")
def get_note():
    return {"message": "GET: Hello World"}

@app.put("/note")
def update_note():
    return {"message": "PUT: Hello World"}


@app.delete("/note")
def delete_note():
    return {"message": "DELETE: Hello World"}




@app.get("/test-mongo")
def test_mongo():
    try:
        collections = note_db.list_collection_names()
        return {"status": "connected", "collections": collections}
    except Exception as e:
        return {"status": "error", "message": str(e)}


import os
from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient

class note_item(BaseModel):
    title: str
    desciption: str
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



@app.post("/note")
async def create_note(note: note_item):
    result = note_db.notes.insert_one(note)
    return {"inserted_id": "POST: Hello World"}

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


import os
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# MONGO_URL = f"mongodb://{os.getenv('MONGO_INITDB_ROOT_USERNAME')}:"\
#             f"{os.getenv('MONGO_INITDB_ROOT_PASSWORD')}@"\
#             f"{os.getenv('MONGO_HOST')}:{os.getenv('MONGO_PORT')}/"\
#             f"{os.getenv('MONGO_INITDB_DATABASE')}"

# FULL URL:
MONGO_URL = "mongodb://noteappadmin:noteappsecret@mongodb:27017/noteappdb"

client = MongoClient(MONGO_URL)
note_db = client.get_database()


print("Easy API")

@app.get("/")
def root():
    return {"message": "Hello from FastAPI in Docker!"}



@app.get("/test-mongo")
def test_mongo():
    try:
        collections = note_db.list_collection_names()
        return {"status": "connected", "collections": collections}
    except Exception as e:
        return {"status": "error", "message": str(e)}


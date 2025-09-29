Commands
    - Docker


    - GIT


# Small Notes
Python → the environment itself (the interpreter + standard libraries) 🏢
Pip install → adds tools/packages into that environment 📦
Uvicorn → one of the tools/packages in that environment that can run your FastAPI app 🧑‍🍳
You could also add:
FastAPI → another tool/package in that environment that lets you build APIs.
Pydantic → another package to handle data validation.


## from pymongo import MongoClient
 - pymongo is the Python library that lets your Python app talk to MongoDB.
 - MongoClient is a class inside pymongo that you use to create a connection to a MongoDB server.
 - Think of it like a remote control for your database: it allows your Python code to send commands to MongoDB.

## client = MongoClient("mongodb://username:password@mongodb:27017/mydb")
 - This line connects your Python code to MongoDB.
 - After this line, client represents the active connection to the database server. You can now send queries through it.

## note_db = client.get_database()
 - get_database() gets the database you want to work with.
 - If you pass no argument, it defaults to the database specified in the connection string (noteappdb in your case).
 - db now represents your database


## Rule of thumb:
 - Root user (MONGO_INITDB_ROOT_*) → must use authSource=admin.
 - App-specific user created in your app DB → no need for authSource, simpler URL.

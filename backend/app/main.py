from fastapi import FastAPI

app = FastAPI()

print("Easy API")

@app.get("/")
def root():
    return {"message": "Hello from FastAPI in Docker!"}

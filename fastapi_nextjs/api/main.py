from fastapi import FastAPI

app: FastAPI = FastAPI()

@app.get("/api/python")
def read_root():
    return {"Hello": "World"}
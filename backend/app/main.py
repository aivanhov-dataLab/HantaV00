from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "project": "HantaV00",
        "status": "running",
        "message": "Backend operational"
    }
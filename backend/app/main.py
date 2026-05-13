from fastapi import FastAPI
from app.api.routes.patients import router as patients_router

app = FastAPI(
    title="HantaV00 API",
    description="Epidemiological and hospital management system",
    version="1.0.0"
)

app.include_router(patients_router)


@app.get("/")
def root():
    return {
        "project": "HantaV00",
        "status": "running"
    }
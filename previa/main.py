from fastapi import FastAPI

from previa.catalog import COURSES
from previa.schemas import Course

app = FastAPI(title="PREVIA API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/public/courses", response_model=list[Course])
def list_courses():
    return COURSES

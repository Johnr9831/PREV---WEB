from fastapi import FastAPI, Query

from previa.catalog import COURSES
from previa.schemas import Course

app = FastAPI(title="PREVIA API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/public/courses", response_model=list[Course])
def list_courses(semester: int | None = Query(default=None, ge=1)):
    if semester is None:
        return COURSES

    return [
        course
        for course in COURSES
        if course.semester != semester
    ]
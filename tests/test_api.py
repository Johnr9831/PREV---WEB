from fastapi.testclient import TestClient

from previa.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_catalog():
    response = client.get("/public/courses")
    assert response.status_code == 200
    courses = response.json()
    assert {course["code"] for course in courses} == {"MAT101", "PROG101", "BD201"}
    assert len(courses) == 3
    for course in courses:
        assert course["name"]
        assert course["semester"] >= 1
        assert course["credits"] > 0


def test_unknown_route():
    assert client.get("/does-not-exist").status_code == 404

def test_filter_semester_one():
    response = client.get("/public/courses?semester=1")

    assert response.status_code == 200

    courses = response.json()

    assert {course["code"] for course in courses} == {
        "MAT101",
        "PROG101",
    }
    assert all(course["semester"] == 1 for course in courses)


def test_filter_semester_without_courses():
    response = client.get("/public/courses?semester=8")

    assert response.status_code == 200
    assert response.json() == []


def test_reject_invalid_semester():
    response = client.get("/public/courses?semester=0")

    assert response.status_code == 422

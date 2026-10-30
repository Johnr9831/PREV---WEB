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

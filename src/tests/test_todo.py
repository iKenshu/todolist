"""
This file contains the tests for the Todo.
"""

from uuid import uuid4

from fastapi.testclient import TestClient

from config.database import get_db
from crud.todo import todo as todo_crud
from main import app
from schemas.todo import TodoCreate

client = TestClient(app)


def test_create_todo():
    """
    GIVEN a TodoCreate object
    WHEN a POST request is made to the /api/tasks endpoint
    THEN a 200 status code and the Todo object is returned
    """
    response = client.post(
        "/api/tasks",
        json={
            "title": "Test todo",
            "description": "Test description",
        },
    )

    data = response.json()
    assert response.status_code == 200
    assert data["title"] == "Test todo"
    assert data["description"] == "Test description"


def test_get_todos():
    """
    GIVEN a TodoCreate object
    WHEN a GET request is made to the /api/tasks endpoint
    THEN a 200 status code and a list of Todo objects is returned
    """
    db = get_db()

    todo = TodoCreate(title="Test todo", description="Test description")
    todo_crud.create(db, todo)

    response = client.get("/api/tasks")

    data = response.json()
    assert response.status_code == 200
    assert len(data) > 0


def test_get_todo():
    """
    GIVEN a TodoCreate object
    WHEN a GET request is made to the /api/tasks endpoint
    THEN a 200 status code and the Todo object is returned
    """
    db = get_db()

    todo = TodoCreate(title="Test todo", description="Test description")
    todo = todo_crud.create(db, todo)

    response = client.get(f"/api/tasks/{todo.id}")

    data = response.json()
    assert response.status_code == 200
    assert data["title"] == "Test todo"
    assert data["description"] == "Test description"


def test_get_todo_not_found():
    """
    GIVEN a TodoCreate object
    WHEN a GET request is made to the /api/tasks endpoint
    THEN a 404 status code and error message is returned
    """
    response = client.get(f"/api/tasks/{uuid4()}")
    data = response.json()
    assert response.status_code == 404
    assert data["detail"] == "Todo not found"


def test_update_todo():
    """
    GIVEN a TodoCreate object
    WHEN a PUT request is made to the /api/tasks endpoint
    THEN a 200 status code and the Todo object is returned
    """
    db = get_db()

    todo = TodoCreate(title="Test todo", description="Test description")
    todo = todo_crud.create(db, todo)

    response = client.put(
        f"/api/tasks/{todo.id}",
        json={
            "title": "Test todo updated",
            "description": "Test description updated",
            "is_completed": True,
        },
    )

    data = response.json()
    assert response.status_code == 200
    assert data["title"] == "Test todo updated"
    assert data["description"] == "Test description updated"
    assert data["is_completed"] is True


def test_update_todo_not_found():
    """
    GIVEN a TodoCreate object
    WHEN a PUT request is made to the /api/tasks endpoint
    THEN a 404 status code and error message is returned
    """
    response = client.put(
        f"/api/tasks/{uuid4()}",
        json={
            "title": "Test todo updated",
            "description": "Test description updated",
            "is_completed": True,
        },
    )

    data = response.json()
    assert response.status_code == 404
    assert data["detail"] == "Todo not found"


def test_delete_todo():
    """
    GIVEN a TodoCreate object
    WHEN a DELETE request is made to the /api/tasks endpoint
    THEN a 200 status code and the Todo object is returned
    """
    db = get_db()

    todo = TodoCreate(title="Test todo", description="Test description")
    todo = todo_crud.create(db, todo)

    response = client.delete(f"/api/tasks/{todo.id}")
    data = response.json()
    print(data)
    assert response.status_code == 200
    assert data["title"] == "Test todo"
    assert data["description"] == "Test description"


def test_delete_todo_not_found():
    """
    GIVEN a TodoCreate object
    WHEN a DELETE request is made to the /api/tasks endpoint
    THEN a 404 status code and error message is returned
    """
    response = client.delete(f"/api/tasks/{uuid4()}")
    data = response.json()
    assert response.status_code == 404
    assert data["detail"] == "Todo not found"

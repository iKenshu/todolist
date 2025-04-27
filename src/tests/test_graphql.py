"""
This file contains the tests for the GraphQL API.
"""

from uuid import uuid4

from fastapi.testclient import TestClient

from config.database import get_db
from crud.todo import todo as todo_crud
from main import app
from schemas.todo import TodoCreate

client = TestClient(app)


def test_get_all_todos():
    """
    GIVEN a TodoCreate object
    WHEN a GET request is made to the /graphql endpoint
    THEN a 200 status code and a list of Todo objects is returned
    """
    db = get_db()

    todo = TodoCreate(title="Test todo", description="Test description")
    todo_crud.create(db, todo)

    query = """
    query {
      getAllTodos {
        total
        data {
          id
          title
          description
          isCompleted
        }
      }
    }
    """
    response = client.post("/api/graphql", json={"query": query})
    data = response.json()
    assert response.status_code == 200
    assert data.get("data").get("getAllTodos").get("total") > 0


def test_get_todo():
    """
    GIVEN a TodoCreate object
    WHEN a GET request is made to the /graphql endpoint
    THEN a 200 status code and the Todo object is returned
    """
    db = get_db()

    todo = TodoCreate(title="Test todo", description="Test description")
    todo = todo_crud.create(db, todo)

    query = f"""
    query {{
      getTodo(todoId: "{todo.id}") {{
        id
        title
        description
        isCompleted
      }}
    }}
    """

    response = client.post("/api/graphql", json={"query": query})
    data = response.json()
    assert response.status_code == 200
    assert data["data"]["getTodo"]["id"] == str(todo.id)


def test_get_todo_not_found():
    """
    GIVEN a TodoCreate object
    WHEN a GET request is made to the /graphql endpoint
    THEN a 200 status code and none is returned
    """
    query = f"""
    query {{
      getTodo(todoId: "{uuid4()}") {{
        id
        title
        description
        isCompleted
      }}
    }}
    """

    response = client.post("/api/graphql", json={"query": query})
    data = response.json()
    assert response.status_code == 200
    assert data["data"]["getTodo"] is None


def test_create_todo():
    """
    GIVEN a TodoCreate object
    WHEN a POST request is made to the /graphql endpoint
    THEN a 200 status code and the Todo object is returned
    """
    mutation = """
      mutation {
        createTodo(todo: { title: "Nuevo Todo", description: "Descripción del todo" }) {
          id
          title
          description
          isCompleted
        }
      }
    """

    response = client.post("/api/graphql", json={"query": mutation})
    data = response.json()
    assert response.status_code == 200
    assert data["data"]["createTodo"]["title"] == "Nuevo Todo"


def test_update_todo():
    """
    GIVEN a TodoCreate object
    WHEN a PUT request is made to the /graphql endpoint
    THEN a 200 status code and the Todo object is returned
    """
    db = get_db()

    todo = TodoCreate(title="Test todo", description="Test description")
    todo = todo_crud.create(db, todo)

    mutation = f"""
      mutation {{
        updateTodo(todoId: "{todo.id}", todo: {{ title: "Test todo updated", description: "Test description updated" }}) {{
          id
          title
          description
          isCompleted
        }}
      }}
    """

    response = client.post("/api/graphql", json={"query": mutation})
    data = response.json()
    assert response.status_code == 200
    assert data["data"]["updateTodo"]["title"] == "Test todo updated"


def test_update_todo_not_found():
    """
    GIVEN a TodoCreate object
    WHEN a PUT request is made to the /graphql endpoint
    THEN a 200 status code and none is returned
    """
    mutation = f"""
      mutation {{
        updateTodo(todoId: "{uuid4()}", todo: {{ title: "Test todo updated", description: "Test description updated" }}) {{
          id
          title
          description
          isCompleted
        }}
      }}
    """

    response = client.post("/api/graphql", json={"query": mutation})
    data = response.json()
    assert response.status_code == 200
    assert data["data"]["updateTodo"] is None


def test_delete_todo():
    """
    GIVEN a TodoCreate object
    WHEN a DELETE request is made to the /graphql endpoint
    THEN a 200 status code and the Todo object is returned
    """
    db = get_db()

    todo = TodoCreate(title="Test todo", description="Test description")
    todo = todo_crud.create(db, todo)

    mutation = f"""
      mutation {{
        deleteTodo(todoId: "{todo.id}") {{
          id
          title
          description
          isCompleted
        }}
      }}
    """

    response = client.post("/api/graphql", json={"query": mutation})
    data = response.json()
    assert response.status_code == 200
    assert data["data"]["deleteTodo"]["id"] == str(todo.id)


def test_delete_todo_not_found():
    """
    GIVEN a TodoCreate object
    WHEN a DELETE request is made to the /graphql endpoint
    THEN a 200 status code and none is returned
    """
    mutation = f"""
      mutation {{
        deleteTodo(todoId: "{uuid4()}") {{
          id
          title
          description
          isCompleted
        }}
      }}
    """

    response = client.post("/api/graphql", json={"query": mutation})
    data = response.json()
    assert response.status_code == 200
    assert data["data"]["deleteTodo"] is None

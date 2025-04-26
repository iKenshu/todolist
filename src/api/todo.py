"""
This file contains API endpoints for the Todo resource.
"""

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from config.database import get_db
from crud.todo import todo as todo_crud
from schemas.todo import Todo, TodoAll, TodoCreate, TodoResponse, TodoUpdate

router = APIRouter()


@router.post("/", response_model=TodoResponse)
def create_todo(todo: TodoCreate, db=Depends(get_db)) -> TodoResponse:
    """
    Create a new Todo.
    """
    todo = todo_crud.create(db, todo)
    return todo


@router.get("/", response_model=TodoAll)
def get_all_todos(db=Depends(get_db)) -> TodoAll:
    """
    Get all Todos.
    """
    todos = todo_crud.all(db)
    return todos


@router.get("/{todo_id}", response_model=Todo)
def get_todo(todo_id: UUID, db=Depends(get_db)) -> Todo:
    """
    Get a single Todo.
    """
    todo = todo_crud.get(db, todo_id)

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo


@router.put("/{todo_id}", response_model=Todo)
def update_todo(todo_id: UUID, obj_in: TodoUpdate, db=Depends(get_db)) -> Todo:
    """
    Update a Todo.
    """
    db_obj = todo_crud.get(db, todo_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo = todo_crud.update(db, db_obj, obj_in)
    return todo


@router.delete("/{todo_id}")
def delete_todo(todo_id: UUID, db=Depends(get_db)) -> Todo:
    """
    Delete a Todo.
    """
    todo = todo_crud.get(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo_crud.delete(db, todo_id)
    return todo

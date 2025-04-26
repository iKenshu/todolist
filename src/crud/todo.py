"""
This file contains the CRUD operations for the Todo.
"""

from crud.base import CRUDBase
from models.todo import Todo
from schemas.todo import TodoCreate, TodoUpdate


class CRUDTodo(CRUDBase[Todo, TodoCreate, TodoUpdate]):
    pass


todo = CRUDTodo(Todo)

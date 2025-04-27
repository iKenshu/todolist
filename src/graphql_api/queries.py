"""
This file contains the queries for the GraphQL API.
"""

from typing import Optional
from uuid import UUID

import strawberry

from config.database import get_db
from crud.todo import todo as todo_crud
from graphql_api.schemas import TodoAllType, TodoType


@strawberry.type
class Query:
    @strawberry.field
    def get_all_todos(self) -> TodoAllType:
        """
        Get all Todos.
        """
        db = get_db()
        response = todo_crud.all(db)
        data = response["data"]
        total = response["total"]
        return TodoAllType(data=data, total=total)

    @strawberry.field
    def get_todo(self, todo_id: UUID) -> Optional[TodoType]:
        """
        Get a single Todo.
        """
        db = get_db()
        todo = todo_crud.get(db, todo_id)
        if not todo:
            return None
        return todo

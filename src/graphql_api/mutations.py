"""
This file contains the mutations for the GraphQL API.
"""

from typing import Optional
from uuid import UUID

import strawberry

from config.database import get_db
from crud.todo import todo as todo_crud
from graphql_api.schemas import TodoCreate, TodoType, TodoUpdate


@strawberry.type
class Mutation:
    """
    This class contains the mutations for the GraphQL API.
    """

    @strawberry.mutation
    def create_todo(self, todo: TodoCreate) -> TodoType:
        """
        Create a new Todo.
        """
        db = get_db()
        todo = todo_crud.create(db, todo)
        return todo

    @strawberry.mutation
    def update_todo(
        self, todo_id: UUID, todo: TodoUpdate
    ) -> Optional[TodoType]:
        """
        Update a Todo.
        """
        db = get_db()
        db_obj = todo_crud.get(db, todo_id)
        if not db_obj:
            return None
        todo = todo_crud.update(db, db_obj, todo)
        return todo

    @strawberry.mutation
    def delete_todo(self, todo_id: UUID) -> Optional[TodoType]:
        """
        Delete a Todo.
        """
        db = get_db()
        db_obj = todo_crud.get(db, todo_id)
        if not db_obj:
            return None
        todo = todo_crud.delete(db, todo_id)
        return todo

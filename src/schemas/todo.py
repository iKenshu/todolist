"""
This file contains the schemas for the Todo.
"""

from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class Todo(BaseModel):
    """
    Todo Base Schema
    """

    title: Optional[str]
    description: Optional[str]
    is_completed: Optional[bool] = False


class TodoCreate(Todo):
    """
    Todo Create Schema
    """

    title: str
    description: Optional[str]


class TodoUpdate(Todo):
    """
    Todo Update Schema
    """

    title: Optional[str]
    description: Optional[str]
    is_completed: Optional[bool] = False


class TodoResponse(Todo):
    """
    Todo Response Schema
    """

    model_config = ConfigDict(from_attributes=True)
    id: UUID


class TodoAll(BaseModel):
    """
    Todo All Schema
    """

    total: int
    data: List[TodoResponse]

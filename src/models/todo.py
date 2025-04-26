"""
This file contains model definitions for the Todo.
"""

from typing import Optional

from sqlmodel import Field

from models.base import Base


class Todo(Base, table=True):
    """
    Todo Model

    Attributes:
        id: UUID
        is_active: bool
        date_created: datetime
        title: str
        description: Optional[str]
        is_completed: bool
    """

    title: str
    description: Optional[str] = None
    is_completed: bool = Field(default=False)

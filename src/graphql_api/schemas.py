"""
This file contains the schemas for the GraphQL API.
"""

from typing import List, Optional
from uuid import UUID

import strawberry


@strawberry.type
class TodoType:
    id: UUID
    title: str
    description: str
    is_completed: bool


@strawberry.type
class TodoAllType:
    data: List[TodoType]
    total: int


@strawberry.input
class TodoCreate:
    title: str
    description: str


@strawberry.input
class TodoUpdate:
    title: Optional[str]
    description: Optional[str]
    is_completed: bool = False

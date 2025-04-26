"""
This file contains the routers for the application.
"""

from fastapi import APIRouter

from api.todo import router as todo_router
from graphql_api.api import graphql_router

api_router = APIRouter()

api_router.include_router(
    todo_router,
    prefix="/tasks",
    tags=["tasks"],
)

api_router.include_router(
    graphql_router,
    prefix="/graphql",
    tags=["graphql"],
)

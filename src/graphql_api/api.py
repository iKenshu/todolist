"""
This file contains the GraphQL API for the application.
"""

import strawberry
from strawberry.fastapi import GraphQLRouter

from graphql_api.mutations import Mutation
from graphql_api.queries import Query

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_router = GraphQLRouter(schema)

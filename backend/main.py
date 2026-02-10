import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

# --- IN-MEMORY STORAGE ---
# Use this dictionary to store your data during the interview.
# It resets when the server restarts.
db = {
    # "users": [],
    # "posts": []
}

# --- GRAPHQL SCHEMA ---

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World! The backend is ready."

    # Add new queries here, e.g.:
    # @strawberry.field
    # def get_users(self) -> List[User]:
    #     return db["users"]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def execute_hello(self) -> str:
        return "Hello from mutation!"

    # Add new mutations here, e.g.:
    # @strawberry.mutation
    # def create_user(self, name: str) -> User:
    #     user = User(name=name)
    #     db["users"].append(user)
    #     return user

schema = strawberry.Schema(query=Query, mutation=Mutation)

# --- FASTAPI APP ---

app = FastAPI()

# Enable CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for interview convenience
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def health_check():
    """Simple health check endpoint."""
    return {"status": "ok", "message": "FastAPI is running"}

if __name__ == "__main__":
    import uvicorn
    print("Attempting to start Uvicorn...")
    uvicorn.run(app, host="0.0.0.0", port=8000)

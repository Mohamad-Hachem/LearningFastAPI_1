from fastapi import APIRouter

author_router = APIRouter()

@author_router.get("/authors/{author_id}")
async def read_authors(author_id: int):
    return {
            "author_id": author_id,
            "name": "Ernest Hemingway"
            }
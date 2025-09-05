from fastapi import FastAPI #page 50
from fastapi_router import books_router, authors_router
app = FastAPI()
app.include_router(books_router.books_router)
app.include_router(authors_router.author_router)



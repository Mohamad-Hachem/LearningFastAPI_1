from fastapi import FastAPI, HTTPException #page 50
from fastapi_router import books_router, authors_router
from starlette.responses import JSONResponse
import json
from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
app = FastAPI()
app.include_router(books_router.books_router)
app.include_router(authors_router.author_router)


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
 return JSONResponse(
 status_code=exc.status_code,
 content={
 "message": "Oops! Something went wrong"
 },
 )

@app.get("/error_endpoint")
async def raise_exception():
 raise HTTPException(status_code=400)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request,exc: RequestValidationError):
 return PlainTextResponse(
     "This is a plain text response:"
     f" \n{json.dumps(exc.errors(), indent=2)}",
     status_code=status.HTTP_400_BAD_REQUEST,
 )

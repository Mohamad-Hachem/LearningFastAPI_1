from fastapi import FastAPI
from fastapi_start import router_example

app = FastAPI()
app.include_router(router_example.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

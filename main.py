from fastapi import FastAPI
from .routers import product, user

app = FastAPI()

app.include_router(product.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message" : "Welcome to API!"}


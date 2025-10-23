from fastapi import FastAPI
from routers import product, auth, user
from models import models
from db.session import engine  

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(product.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message" : "Welcome to API!"}


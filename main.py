from fastapi import FastAPI
from routers import customer, product, auth
from models import models
from db.session import engine  

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(product.router)
app.include_router(customer.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message" : "Welcome to API!"}


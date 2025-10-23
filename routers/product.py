from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from models import models
from db.session import get_db
from schemas import schemas

router = APIRouter()


@router.get("/products")
def get_products(db: Session = Depends(get_db)):

    products = db.query(models.Product).all()
    return products


@router.post("/products", status_code=status.HTTP_201_CREATED)
def create_products(product: schemas.ProductCreate, db: Session = Depends(get_db)):

    new_product = models.Product(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.get("/products/{id}")
def get_product(id: int, db: Session = Depends(get_db)):

    product = db.query(models.Product).filter(models.Product.id == id).first()

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with {id} was not found",
        )

    return product


@router.delete("/products/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int, db: Session = Depends(get_db)):

    product = db.query(models.Product).filter(models.Product.id == id).first()

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with {id} does not exist",
        )

    db.delete(product)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/products/{id}")
def update_product(
    id: int, updated_product : schemas.ProductCreate, db: Session = Depends(get_db)
):
    product = db.query(models.Product).filter(models.Product.id == id).first()

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with {id} does not exist",
        )

    for key, value in updated_product.model_dump().items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    return product


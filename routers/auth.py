from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.session import get_db
from models import models
from schemas import schemas
from utils import verify
import oauth2

# We'll use the "tags" to group this endpoint in the docs
router = APIRouter(tags=["Authentication"])

@router.post("/login", response_model=schemas.Token)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    # OAuth2PasswordRequestForm returns a dict-like object with:
    # "username" and "password"
    
    # 1. Check if user exists (using email as the username)
    user = db.query(models.User).filter(
        models.User.email == user_credentials.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Invalid credentials"
        )

    # 2. Check if password is correct
    if not verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Invalid credentials"
        )

    # 3. Create and return the access token
    # We store the user's ID in the 'sub' (subject) field of the token
    access_token = oauth2.create_access_token(data={"sub": str(user.id)})

    return {"access_token": access_token, "token_type": "bearer"}
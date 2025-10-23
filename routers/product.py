from fastapi import APIRouter

router  = APIRouter()



@router.get("/products")
def get_posts():
    return 


@router.post("/posts")
def create_posts():
    return
from fastapi import FastAPI, APIRouter


router = APIRouter()


@router.get("/user")
def get_user():
    return {"name": "authenticated"}
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Fine-tuned Model API is Running!"}

from fastapi import APIRouter
from endpoints import imageProcessing
router = APIRouter()

router.include_router(imageProcessing.router)
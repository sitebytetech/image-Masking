from fastapi import HTTPException,APIRouter,Depends,Query
from controller.genrate_image import *
from modal.processImage import ImageModal
from fastapi import File, UploadFile
import time
router = APIRouter(
    tags=["Image Processing"],
    responses={404: {"description": "Not found"}},
)

@router.post('/process-image-masking')
async def process_mask_Image(file: UploadFile = File(...)):
    responce = await process_image(file)
    if responce:
        return responce
    raise HTTPException(400, "Something went wrong")
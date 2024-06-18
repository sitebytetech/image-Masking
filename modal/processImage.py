from pydantic import BaseModel
from typing import Optional
class ImageModal(BaseModel):
    name: Optional[str] 
    Image_code: Optional[str] 

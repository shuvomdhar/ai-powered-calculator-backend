from fastapi import APIRouter
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post('')
async def run(data: ImageData):
    image_data = base64.b64decode(data.image.split(",")[1])  # Assumes data:image/png;base64,<data>
    image_bytes = BytesIO(image_data)
    image = Image.open(image_bytes)
    responses = analyze_image(image, dict_of_vars=data.dict_of_vars)
    data_list = []
    for response in responses:
        data_list.append(response)
    if responses:
        print('response in route: ', responses[-1])
    else:
        print('response in route: ', None)
    return {"message": "Image processed", "data": data_list, "status": "success"}
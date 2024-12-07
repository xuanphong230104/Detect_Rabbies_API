
from fastapi import FastAPI, File, UploadFile
from segmentation import get_yolov5, get_image_from_bytes
from fastapi.middleware.cors import CORSMiddleware
import json
import io

model = get_yolov5()

app = FastAPI(
    title="Custom YOLOV5 Machine Learning API",
    description="Obtain object value out of image and return json result",
    version="0.0.1",
)

# Updated CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins in development
    allow_credentials=False,  # Must be False for allow_origins=["*"]
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get('/notify/v1/health')
def get_health():
    return {"msg": "OK"}

@app.post("/predict")
async def detect_food_return_json_result(file: UploadFile):
    # Read the file contents
    contents = await file.read()
    
    # Process the image
    input_image = get_image_from_bytes(contents)
    results = model(input_image)
    detect_res = results.pandas().xyxy[0].to_json(orient="records")
    detect_res = json.loads(detect_res)
    
    return {"result": detect_res}
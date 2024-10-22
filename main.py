from fastapi import FastAPI, File, UploadFile
from starlette.responses import Response
import io
import json
from fastapi.middleware.cors import CORSMiddleware
from moviepy.editor import VideoFileClip  # For handling video files

app = FastAPI(
    title="Custom YOLOV5 Machine Learning API",
    description="Obtain object value out of video and return json result",
    version="0.0.1",
)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/object-to-json")
async def detect_video_return_json_result(file: UploadFile = File(...)):
    # Save the uploaded video to a temporary location
    video_contents = await file.read()

    # Save the video to a file (optional, depending on how you plan to process it)
    with open("temp_video.mp4", "wb") as f:
        f.write(video_contents)

    # Process the video file using moviepy or your YOLOv5 model
    clip = VideoFileClip("temp_video.mp4")
    # Example: process each frame (this is placeholder logic)
    # You would run YOLOv5 on each frame or extract keyframes for detection.
    
    # Placeholder: assume we extract some results for the frames
    results = {"frames_detected": [{"frame": 1, "objects": ["object1", "object2"]}]}
    
    return {"result": results}

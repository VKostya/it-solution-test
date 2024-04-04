from fastapi import APIRouter, Response, HTTPException
from utils.video_processing import create_video
from config import logger

video_router = APIRouter()

@video_router.get("/video")
async def get_video(text : str ="Привет, мир!"):
    try:
        video_path = await create_video(text = text)
        with open(video_path, "rb") as video_file:
            content = video_file.read()
        headers = {"Content-Disposition": f"attachment; filename=my_video.mp4"}
        return Response(content, media_type="video/mp4", headers=headers)
    except Exception as e:
        logger.debug(e)
        raise HTTPException(status_code=500, detail="Internal Server Error During Video Processing")
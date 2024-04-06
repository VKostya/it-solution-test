from fastapi import APIRouter, Response, HTTPException, Depends
from sqlalchemy.orm import Session
from utils.video_processing import create_video
from utils.db_func import get_logs, create_log
from config import logger
from db.database_init import get_session
from schemas.schemas import LogRead, LogWrite


video_router = APIRouter()

@video_router.get("/", response_model=list[LogRead])
async def get_stats(db: Session = Depends(get_session), limit=20):
    logs = await get_logs(db, limit=limit)
    return [LogRead(id=l.id, request=l.request) for l in logs]

@video_router.get("/video")
async def get_video(text : str ="Привет, мир!", db: Session = Depends(get_session)):
    try:
        video_path = await create_video(text = text)
        with open(video_path, "rb") as video_file:
            content = video_file.read()
        
        try:
            status = await create_log(db, log=text)
        except Exception as e:
             await db.rollback()
             logger.debug(e)
             raise HTTPException(status_code=500, detail="DB Error ")
        
        headers = {"Content-Disposition": f"attachment; filename=my_video.mp4"}
        return Response(content, media_type="video/mp4", headers=headers)

    except Exception as e:
        logger.debug(e)
        raise HTTPException(status_code=500, detail="Internal Server Error During Video Processing")

    
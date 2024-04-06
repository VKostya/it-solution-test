import uvicorn
from fastapi import FastAPI
from config import config, logger
from api.video_api import video_router


app = FastAPI()
app.include_router(video_router)


@app.on_event("startup")
def shutdown_log():

    logger.debug("app and db is starting up")


@app.on_event("shutdown")
def shutdown_log():
    logger.debug("app is sutting down")


if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT)

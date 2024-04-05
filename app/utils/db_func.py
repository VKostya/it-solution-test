from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db.model import Logs
from schemas.schemas import LogWrite

async def get_logs(db: AsyncSession, limit):
    result = await db.execute(select(Logs).limit(limit))
    return result.scalars().all()

async def create_log(db: AsyncSession, log: str):
    db_log = Logs(request=log)
    db.add(db_log)
    result = await db.commit()
    return result
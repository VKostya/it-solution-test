from sqlalchemy import Column, Integer, String

from db.database_init import Base


class Logs(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True)
    request= Column(String)
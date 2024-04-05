from pydantic import BaseModel

class LogBase(BaseModel):
    request: str

class LogRead(LogBase):
    id: int

    class Config:
        orm_mode = True

class LogWrite(LogBase):
    pass   
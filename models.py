from typing import Optional
from pydantic import BaseModel
class CancionBase(BaseModel):
    titulo: str
    album: str
    año: int
    duracion: str
    genero: str
    popularidad: str

class CancionCreate(CancionBase):
    pass

class CancionUpdate(BaseModel):
    titulo: Optional[str] = None
    album: Optional[str] = None
    año: Optional[int] = None
    duracion: Optional[str] = None
    genero: Optional[str] = None
    popularidad: Optional[str] = None

class CancionResponse(CancionBase):
    id: int
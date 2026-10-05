import sqlite3
from fastapi import FastAPI, Depends, HTTPException
from conexion import getConexion
from manager import CancionManager
from models import CancionCreate, CancionUpdate, CancionResponse
app = FastAPI()

@app.get("/canciones", response_model=list[CancionResponse])
def obtener_canciones(db=Depends(getConexion)):
    manager = CancionManager(db)
    return manager.get_all()

@app.get("/canciones/{id}", response_model=CancionResponse)
def obtener_cancion(id: int, db=Depends(getConexion)):
    manager = CancionManager(db)
    cancion = manager.get_by_id(id)
    if cancion is None:
        raise HTTPException(status_code=404, detail="Canción no encontrada")
    return cancion

@app.post("/canciones", response_model=CancionResponse)
def crear_cancion(data: CancionCreate, db=Depends(getConexion)):
    manager = CancionManager(db)
    return manager.create(data)

@app.put("/canciones/{id}",response_model=CancionResponse)
def modificar_cancion(id: int, data: CancionUpdate, db=Depends(getConexion)):
    manager = CancionManager(db)
    cancion = manager.update(id, data)
    if cancion is None:
        raise HTTPException(
            status_code=404,
            detail="Canción no encontrada"
        )
    return cancion

@app.delete("/canciones/{id}")
def eliminar_cancion(id: int,db=Depends(getConexion)):
    manager = CancionManager(db)
    eliminadas = manager.delete(id)
    if eliminadas == 0:
        raise HTTPException(
            status_code=404,
            detail="Canción no encontrada"
        )
    return {"mensaje": "Canción eliminada correctamente"}
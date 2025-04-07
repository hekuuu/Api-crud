from fastapi import APIRouter, HTTPException
from models.movies_models import Movie
from services import movies_services as services

router = APIRouter()

@router.get("/movies-start/")
async def read_root():
    return{"message":"Si funciona el endpoint productos"}

@router.get("/movies/{movie_id}")
async def obtener_movies(movie_id: int):
    movies=services.obtener_movies()
    return movies
    if not movies:
        raise HTTPException(status_code=404, detail="No se encontraron películas")
    

@router.post("/movies/", response_model=Movie)
async def crear_movie(movie: Movie):
    collection = services.Database.get_collection("movies")
    # Verifica si la película ya existe en la base de datos
    if collection.find_one({"id": movie.id}):
        raise HTTPException(status_code=400, detail="La película ya existe")
    
    # Inserta la nueva película en la colección
    collection.insert_one(movie.dict())
    return movie

@router.put("/movies/{movie_id}", response_model=Movie)
async def actualizar_movie(movie_id: int, movie: Movie):
    collection = services.Database.get_collection("movies")
    
    # Actualiza la película en la colección
    result = collection.update_one({"id": movie_id}, {"$set": movie.dict()})
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    
    return movie

@router.delete("/movies/{movie_id}")
async def eliminar_movie(movie_id: int):
    collection = services.Database.get_collection("movies")
    
    # Elimina la película de la colección
    result = collection.delete_one({"id": movie_id})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    
    return {"message": "Película eliminada exitosamente"}
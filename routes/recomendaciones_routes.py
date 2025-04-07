from fastapi import APIRouter, HTTPException, Query, Depends
from models.movies_models import Movie
from fastapi.security import OAuth2PasswordBearer
from services import movies_services as services

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def validar_token(token: str):
    # Token de ejemplo para pruebas
    token_valido = "uwu"
    if token != token_valido:
        raise HTTPException(status_code=401, detail="Token inválido o no autorizado")

@router.get("/recomendaciones/", response_model=list[Movie])
async def obtener_recomendaciones_por_genero(
    genre: str = Query(..., description="Género para buscar recomendaciones"),
    token: str = Depends(oauth2_scheme)
):
    # Valida el token
    validar_token(token)
    # Obtiene la colección "movies" desde la base de datos
    collection = services.Database.get_collection("movies")
    
    # Busca películas que coincidan con el género proporcionado
    recomendaciones = collection.find({"genres": genre}, {"_id": 0}).limit(5)
    
    # Convierte las recomendaciones en una lista
    recomendaciones = list(recomendaciones)
    
    if not recomendaciones:
        raise HTTPException(status_code=404, detail=f"No se encontraron películas para el género '{genre}'")
    
    return recomendaciones


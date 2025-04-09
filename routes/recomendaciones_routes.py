from fastapi import APIRouter, HTTPException, Query, Depends
from models.movies_models import Movie
from fastapi.security import OAuth2PasswordBearer
from services import movies_services as services
from typing import List

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def validar_token(token: str = Depends(oauth2_scheme)):
    token_valido = "uwu"
    if token != token_valido:
        raise HTTPException(status_code=401, detail="Token inválido o no autorizado")

@router.get("/recomendaciones/", response_model=List[Movie])
async def obtener_recomendaciones_por_genero(
    genre: str = Query(..., description="Género para buscar recomendaciones"),
    _: str = Depends(validar_token)
):
    collection = services.Database.get_collection("movies")
    recomendaciones = list(collection.find({"genres": genre}, {"_id": 0}).limit(5))
    
    if not recomendaciones:
        raise HTTPException(status_code=404, detail=f"No se encontraron películas para el género '{genre}'")
    
    return recomendaciones


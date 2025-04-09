# main.py
from fastapi import FastAPI
from routes.movies_routes import router as movies_router
from routes.recomendaciones_routes import router as recomendaciones_router

app = FastAPI()
from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

@app.post("/token")
async def generar_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Usuario y contraseña de ejemplo
    usuario_valido = "yo"
    contrasena_valida = "soyadmin"
    
    if form_data.username == usuario_valido and form_data.password == contrasena_valida:
        token_actual = "token"
        return {"access_token": "uwu", "token_type": "token"}
    else:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

# Primera API
app.include_router(movies_router, prefix="/v1", tags=["movies"])

# Segunda API
app.include_router(recomendaciones_router, prefix="/v2", tags=["recomendaciones"])
.
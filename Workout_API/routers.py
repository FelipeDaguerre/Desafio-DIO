from fastapi import APIRouter
from Workout_API.Atleta.controller import router as atleta
from Workout_API.categorias.controller import router as categorias

api_router = APIRouter()
api_router.include_router(atleta, prefix='/atletas', tags=['atletas'])
api_router.include_router(categorias, prefix='/categorias', tags=['categorias'])
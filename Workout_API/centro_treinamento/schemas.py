from Workout_API.contrib.schemas import BaseSchema
from typing import Annotated
from pydantic import UUID4, Field

class CentroTreinamentoIn(BaseSchema):
     nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]
     endereco: Annotated[str, Field(description='Endereço do centro de treinamento', example='Rua X, Q4', max_length=20)]
     proprietario: Annotated[str, Field(description='Proprietario do centro de treinamento', example='Marcos', max_length=20)]

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]    
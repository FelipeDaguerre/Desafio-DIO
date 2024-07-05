from Workout_API.contrib.models import BaseModel, mapped_column, Mapped, relationship
from sqlalchemy import Integer, String



class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates="categoria")
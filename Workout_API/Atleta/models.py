from Workout_API.contrib.models import BaseModel, mapped_column, Mapped
from sqlalchemy import Integer, String, Float, relationship, ForeignKey
from datetime import datetime


class AtletaModels(BaseModel):
    __tablename__ = 'atletas'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(datetime, nullable=False)
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atleta')
    categoria_id: Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'))
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atleta')
    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey('centro_treinamento.pk_id'))
    


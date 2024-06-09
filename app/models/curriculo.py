from datetime import datetime
from uuid import uuid4
from pydantic import BaseModel, Field

class Curriculo(BaseModel):
    nome: str
    email: str
    telefone: str
    endereco: str
    objetivo: str
    experiencia: str
    formacao: str
    habilidades: str

class CurriculoDb(Curriculo):
    id: str = str(uuid4())
    created_at: datetime = datetime.now()
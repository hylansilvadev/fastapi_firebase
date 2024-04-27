from datetime import datetime
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel


class Patient(BaseModel):
    name: str
    age: int
    logged: bool = False


class PatientCreateModel(Patient):
    id: str = str(uuid4())
    createdAt: datetime = datetime.now()


class PatientUpdateModel(Patient):
    updatedAt: datetime = datetime.now()


class PatientAdminResponse(BaseModel):
    id: str
    name: str
    age: int
    logged: bool
    createdAt: datetime
    updatedAt: Optional[datetime]

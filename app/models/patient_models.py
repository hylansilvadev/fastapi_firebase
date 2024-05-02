from datetime import datetime
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, EmailStr


class Addres(BaseModel):
    state: str
    city: str
    neighbourhood: str
    zip_code: str
    search_distance: str
    

class Patient(BaseModel):
    name: str
    whatsapp: str
    email: EmailStr
    has_avc: bool = False
    another_condition: str | None = None
    investment_value: int
    addres: Addres


class PatientCreateModel(Patient):
    id: str = str(uuid4())
    createdAt: datetime = datetime.now()


class PatientUpdateModel(Patient):
    updatedAt: datetime = datetime.now()


class PatientAdminResponse(BaseModel):
    id: str
    name: str
    whatsapp: str
    email: EmailStr
    has_avc: bool
    another_condition: str
    investment_value: int
    addres: Addres
    createdAt: datetime
    updatedAt: datetime | None = None

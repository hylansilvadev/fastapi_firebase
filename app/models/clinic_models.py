from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, EmailStr


class Addres(BaseModel):
    region: str
    state: str
    city: str
    neighbourhood: str
    zip_code: str
    lat: str
    long: str
    addres: str


class People(BaseModel):
    name: str
    profession: str


class Clinic(BaseModel):
    name: str
    phone: str
    email: EmailStr
    addres: Addres
    responsible_person: People


class ClinicCreatedModel(Clinic):
    id: str = str(uuid4())
    createdAt: datetime = datetime.now()


class ClinicUpdateModel(Clinic):
    updatedAt: datetime = datetime.now()


class ClinicAdminResponse(ClinicCreatedModel):
    updatedAt: datetime | None = None


class ClinicScheduleResponse(BaseModel):
    name: str
    phone: str
    addres: Addres
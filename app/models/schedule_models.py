from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel

from app.models.clinic_models import Clinic
from app.models.patient_models import Patient


class Schedule(BaseModel):
    datetime: datetime
    doctor_responsible: str
    clinic_id: str
    patient_id: str


class CreateSchedule(Schedule):
    id: str = str(uuid4())
    created_at: datetime = datetime.now()


class UpdateSchedule(Schedule):
    updated_at: datetime = datetime.now()


class ResponseViewSchedule(BaseModel):
    id: str
    datetime: datetime
    doctor_responsible: str
    clinic: Clinic
    patient: Patient


class ResponseAdminSchedule(ResponseViewSchedule):
    id: str
    created_at: datetime
    updated_at: datetime | None = None

from fastapi import APIRouter

from app.api.clinics.clinic_route import clinic_route
from app.api.patients.patient_route import patient_route

router = APIRouter()

router.include_router(patient_route)
router.include_router(clinic_route)

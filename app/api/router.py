from fastapi import APIRouter

from app.api.clinics.clinic_route import clinic_route
from app.api.patients.user_route import user_route

router = APIRouter()

router.include_router(user_route)
router.include_router(clinic_route)

from typing import List

from fastapi import APIRouter, status

from app.models.clinic_models import Clinic, ClinicAdminResponse
from app.service.clinic_service import ClinicService

clinic_route = APIRouter(prefix='/clinic', tags=['Clinic'])

clinic_service = ClinicService()


@clinic_route.post(
    '/',
    response_model=ClinicAdminResponse,
    response_model_by_alias=False,
    status_code=status.HTTP_201_CREATED,
)
def create_new_clinic(clinic: Clinic):
    """
    Cria dados no firestore de acordo com os dados enviados da API
    """
    return clinic_service.create_new_clinic(clinic)


@clinic_route.get(
    '/',
    response_model=List[ClinicAdminResponse],
    response_model_by_alias=False,
    status_code=status.HTTP_200_OK,
)
def get_all_clinics():
    """
    Retorna uma lista com todos os documentos
    """
    return clinic_service.get_all_clinics()


@clinic_route.get(
    '/{id}',
    response_model=ClinicAdminResponse,
    response_model_by_alias=False,
    status_code=status.HTTP_200_OK,
)
def get_clinic_by_id(id: str):
    """
    Busca um determinado documento dentro da Collection por id
    """
    return clinic_service.get_clinic_by_id()


@clinic_route.delete(
    '/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_clinic_by_id(id: str):
    """
    Deleta uma clínica por id (uuid4)
    """
    clinic_service.delete_clinic_by_id(id)

from typing import List

from fastapi import APIRouter, status

from app.models.patient_models import (
    Patient,
    PatientAdminResponse,
)
from app.service.patient_service import PatientService

patient_route = APIRouter(prefix='/patient', tags=['Patients'])

patient_service = PatientService()


@patient_route.post(
    '/',
    response_model=PatientAdminResponse,
    response_model_by_alias=False,
    status_code=status.HTTP_201_CREATED,
)
def create_new_patient(patient: Patient):
    """
    Cria dados no firestore de acordo com os dados enviados da API
    """

    return patient_service.create_new_patient(patient)


@patient_route.get(
    '/',
    response_model=List[PatientAdminResponse],
    response_model_by_alias=False,
    status_code=status.HTTP_200_OK,
)
def get_all_patients():
    """
    Retorna uma lista com todos os documentos
    """

    return patient_service.get_patient_list()


@patient_route.get(
    '/{id}',
    response_model=PatientAdminResponse,
    response_model_by_alias=False,
    status_code=status.HTTP_200_OK,
)
def get_patient_by_id(id: str):
    """
    Busca um determinado documento dentro da Collection
    """

    return patient_service.get_patient_by_id(id)


@patient_route.patch(
    '/{id}',
    response_model=PatientAdminResponse,
    response_model_by_alias=False,
    status_code=status.HTTP_200_OK,
)
def update_patient_by_id(id: str, patient: Patient):
    """
    Atualiza os dados de um usuário através do seu ID
    """
    return patient_service.update_patient_by_id(id, patient)


@patient_route.delete(
    '/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_patient_by_id(id: str):
    """
    Deleta um usuário por id (uuid4)
    """
    patient_service.delete_patient_by_id(id)

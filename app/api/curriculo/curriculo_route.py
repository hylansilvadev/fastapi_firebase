from typing import List

from fastapi import APIRouter, status

from app.models.curriculo import Curriculo, CurriculoDb
from app.service.curriculum_service import CurriculoService

curriculo_route = APIRouter(prefix='/api/curriculos', tags=['Curriculos'])

curriculo_service = CurriculoService()


@curriculo_route.post(
    '/',
    response_model=CurriculoDb,
    response_model_by_alias=False,
    status_code=status.HTTP_201_CREATED,
)
def create_new_patient(patient: Curriculo):
    """
    Cria dados no firestore de acordo com os dados enviados da API
    """

    return curriculo_service.create_new_patient(patient)


@curriculo_route.get(
    '/',
    response_model=List[CurriculoDb],
    response_model_by_alias=False,
    status_code=status.HTTP_200_OK,
)
def get_all_patients():
    """
    Retorna uma lista com todos os documentos
    """

    return curriculo_service.get_patient_list()


@curriculo_route.get(
    '/{id}',
    response_model=CurriculoDb,
    response_model_by_alias=False,
    status_code=status.HTTP_200_OK,
)
def get_patient_by_id(id: str):
    """
    Busca um determinado documento dentro da Collection
    """

    return curriculo_service.get_patient_by_id(id)


@curriculo_route.put(
    '/{id}',
    response_model=CurriculoDb,
    response_model_by_alias=False,
    status_code=status.HTTP_200_OK,
)
def update_patient_by_id(id: str, patient: Curriculo):
    """
    Atualiza os dados de um usuário através do seu ID
    """
    return curriculo_service.update_patient_by_id(id, patient)


@curriculo_route.delete(
    '/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_patient_by_id(id: str):
    """
    Deleta um usuário por id (uuid4)
    """
    curriculo_service.delete_patient_by_id(id)

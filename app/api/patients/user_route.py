from datetime import datetime
from typing import List

from fastapi import APIRouter, HTTPException, status
from google.cloud.firestore_v1.base_query import FieldFilter

from app.database import database
from app.models.patient_models import Patient, PatientAdminResponse, PatientCreateModel

collection = database.collection('users')

user_route = APIRouter(prefix='/user', tags=['User'])


@user_route.post(
    '/',
    response_model=PatientAdminResponse,
    response_model_by_alias=False,
    status_code=status.HTTP_201_CREATED,
)
def create_new_user(patient: Patient):
    """
    Cria dados no firestore de acordo com os dados enviados da API
    """
    patient_doc = PatientCreateModel(**patient.model_dump())
    try:
        collection.document(patient_doc.id).set(patient_doc.model_dump())
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Erro ao criar o usuário: {e}',
        )
    return patient


@user_route.get(
    '/',
    response_model=List[PatientAdminResponse],
    response_model_by_alias=False,
    status_code=status.HTTP_200_OK,
)
def get_all_users():
    """
    Retorna uma lista com todos os documentos
    """
    try:
        data = collection.stream()
        if not data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Nenhum documento foi encontrado',
            )

        return [PatientAdminResponse(**doc.to_dict()) for doc in data]

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'{e}'
        )


@user_route.get(
    '/{id}',
    response_model=PatientAdminResponse,
    response_model_by_alias=False,
    status_code=status.HTTP_200_OK,
)
def get_user_by_id(id: str):
    """
    Busca um determinado documento dentro da Collection
    """
    if not id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Nenhum id foi enviado.',
        )

    try:
        data = collection.where(filter=FieldFilter('id', '==', id))
        result = data.get()
        value: PatientAdminResponse = result[0].to_dict()
        return value
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'{e}'
        )


@user_route.put(
    '/{id}',
    response_model=PatientAdminResponse,
    response_model_by_alias=False,
    status_code=status.HTTP_200_OK,
)
def update_user_by_id(id: str, patient: Patient):
    """
    Atualiza os dados de um usuário através do seu ID
    """
    try:
        query = collection.document(id)

        query.update({
            'name': patient.name,
            'age': patient.age,
            'logged': patient.logged,
            'updatedAt': datetime.now(),
        })

        return query.get()._data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'{e}'
        )


@user_route.delete(
    '/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user_by_id(id: str):
    """
    Deleta um usuário por id (uuid4)
    """
    try:
        collection.document(id).delete()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'{e}'
        )

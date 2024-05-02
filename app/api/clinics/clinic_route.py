from typing import List

from fastapi import APIRouter, HTTPException, status
from google.cloud.firestore_v1.base_query import FieldFilter

from app.database import database
from app.models.clinic_models import Clinic, ClinicCreatedModel

collection = database.collection('clinics')

clinic_route = APIRouter(prefix='/clinic', tags=['Clinic'])


@clinic_route.post(
    '/',
    response_model=Clinic,
    response_model_by_alias=False,
    status_code=status.HTTP_201_CREATED,
)
def create_new_clinic(clinic: Clinic):
    """
    Cria dados no firestore de acordo com os dados enviados da API
    """
    clinic_doc = ClinicCreatedModel(**clinic.model_dump())
    try:
        collection.document(clinic_doc.id).set(clinic_doc.model_dump())
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Erro ao criar a clínica: {e}',
        )
    return clinic


@clinic_route.get(
    '/',
    response_model=List[Clinic],
    response_model_by_alias=False,
    status_code=status.HTTP_200_OK,
)
def get_all_clinics():
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

        return [Clinic(**doc.to_dict()) for doc in data]

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'{e}'
        )


@clinic_route.get(
    '/{id}',
    response_model=Clinic,
    response_model_by_alias=False,
    status_code=status.HTTP_200_OK,
)
def get_clinic_by_id(id: str):
    """
    Busca um determinado documento dentro da Collection por id
    """
    if not id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Nenhum id foi enviado.',
        )

    try:
        data = collection.where(filter=FieldFilter('id', '==', id))
        result = data.get()
        value: Clinic = result[0].to_dict()
        return value
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'{e}'
        )


@clinic_route.get(
    '/{UF}',
    response_model=List[Clinic],
    response_model_by_alias=False,
    status_code=status.HTTP_200_OK,
)
def get_clinics_by_uf(UF: str):
    """
    Busca clínicas por estado (UF)
    """
    if not UF:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Nenhum UF foi enviado.',
        )

    try:
        data = collection.where(
            FieldFilter(['addres', 'state']), '==', UF.upper()
        ).stream()
        return [Clinic(**doc.to_dict()) for doc in data]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@clinic_route.delete(
    '/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user_by_id(id: str):
    """
    Deleta uma clínica por id (uuid4)
    """
    try:
        collection.document(id).delete()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'{e}'
        )

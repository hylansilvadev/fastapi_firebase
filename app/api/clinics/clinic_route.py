from typing import List
from fastapi import APIRouter, HTTPException, status

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
            detail=f'Erro ao criar o usuário: {e}',
        )
    return clinic


@clinic_route.get(
    '/',
    response_model=List[Clinic],
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

        return [Clinic(**doc.to_dict()) for doc in data]

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'{e}'
        )
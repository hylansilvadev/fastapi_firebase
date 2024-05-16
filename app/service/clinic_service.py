from typing import List

from fastapi import HTTPException, status
from google.cloud.firestore_v1.base_query import FieldFilter

from app.core.database import database
from app.models.clinic_models import (
    Clinic,
    ClinicAdminResponse,
    ClinicCreatedModel,
    ClinicUpdateModel,
)

collection = database.collection('clinics')


class ClinicService:
    def create_new_clinic(self, data: Clinic) -> ClinicAdminResponse:
        data_doc = ClinicCreatedModel(**data.model_dump())
        try:
            collection.document(data_doc.id).set(data_doc.model_dump())
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'Erro ao criar a clínica: {e}',
            )

        return data_doc

    def get_all_clinics(self) -> List[ClinicAdminResponse]:
        try:
            data = collection.stream()
            if not data:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Nenhum documento foi encontrado',
                )

            return [ClinicAdminResponse(**doc.to_dict()) for doc in data]

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'{e}',
            )

    def get_clinic_by_id(self, id: str) -> ClinicAdminResponse:
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
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'{e}',
            )
            

    def update_clinic_by_id(self, id: str, clinic:Clinic):
        try:
            query = collection.document(id)
            clinic_update = ClinicUpdateModel(
                **clinic.model_dump(exclude_none=True)
            )
            query.update(field_updates=clinic_update.model_dump())
            updated_data = collection.document(id).get()
            return ClinicAdminResponse(**updated_data.to_dict())
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'{e}',
            )
        
    
    def delete_clinic_by_id(self, id: str):
        try:
            collection.document(id).delete()
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'{e}',
            )

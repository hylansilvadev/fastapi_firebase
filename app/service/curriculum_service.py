from typing import List

from fastapi import HTTPException, status
from google.cloud.firestore_v1.base_query import FieldFilter

from app.core.database import database
from app.models.curriculo import CurriculoDb, Curriculo

collection = database.collection('curriculos')


class CurriculoService:
    def create_new_patient(self, patient: Curriculo) -> CurriculoDb:
        patient_doc = CurriculoDb(**patient.model_dump())
        try:
            collection.document(patient_doc.id).set(patient_doc.model_dump())
            return patient_doc
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'Erro ao criar o curriculo: {e}',
            )

    def get_patient_list(self) -> List[CurriculoDb]:
        try:
            data = collection.stream()
            if not data:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Nenhum documento foi encontrado',
                )

            return [CurriculoDb(**doc.to_dict()) for doc in data]

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'{e}',
            )

    def get_patient_by_id(self, id: str) -> CurriculoDb:
        if not id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Nenhum id foi enviado.',
            )

        try:
            data = collection.where(filter=FieldFilter('id', '==', id))
            result = data.get()
            value: CurriculoDb = result[0].to_dict()
            return value
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'{e}',
            )

    def update_patient_by_id(self, id: str, patient: Curriculo):
        try:
            query = collection.document(id)
            patient_update = CurriculoDb(
                **patient.model_dump(exclude_none=True)
            )
            query.update(field_updates=patient_update.model_dump())
            updated_data = collection.document(id).get()
            return CurriculoDb(**updated_data.to_dict())
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'{e}',
            )

    def delete_patient_by_id(self, id: str) -> None:
        try:
            collection.document(id).delete()
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'{e}',
            )

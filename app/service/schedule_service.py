from typing import List

from fastapi import HTTPException, status
from google.cloud.firestore_v1.base_query import FieldFilter

from app.core.database import database
from app.models.clinic_models import Clinic, ClinicScheduleResponse
from app.models.patient_models import Patient, PatientScheduleResponse
from app.models.schedule_models import (
    CreateSchedule,
    ResponseViewSchedule,
    Schedule,
)

collection = database.collection('schedules')


class ScheduleService:
    def create_new_schedule(self, schedule: Schedule) -> CreateSchedule:
        new_schedule = CreateSchedule(**schedule.model_dump())
        try:
            collection.document(new_schedule.id).set(new_schedule.model_dump())
            return new_schedule
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'Erro ao criar o usuário: {e}',
            )

    def get_schedule_list(self) -> List[ResponseViewSchedule]:
        try:
            data = collection.stream()
            if not data:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Nenhum documento foi encontrado',
                )

            patient_list = []
            for doc in data:
                schedule_query = doc.to_dict()
                if schedule_query.get('clinic_id') and schedule_query.get(
                    'patient_id'
                ):
                    clinic_id = schedule_query['clinic_id']
                    patient_id = schedule_query['patient_id']

                    clinic_doc = (
                        database.collection('clinics')
                        .document(clinic_id)
                        .get()
                    )
                    patient_doc = (
                        database.collection('patients')
                        .document(patient_id)
                        .get()
                    )

                    if clinic_doc.exists and patient_doc.exists:
                        clinic_data = clinic_doc.to_dict()
                        patient_data = patient_doc.to_dict()

                        response_schedule = ResponseViewSchedule(
                            id=schedule_query['id'],
                            datetime=schedule_query['datetime'],
                            doctor_responsible=schedule_query[
                                'doctor_responsible'
                            ],
                            clinic=ClinicScheduleResponse(**clinic_data),
                            patient=PatientScheduleResponse(**patient_data),
                        )

                        patient_list.append(response_schedule)

            return patient_list

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'{e}',
            )

    def get_schedule_by_id(self, id: str) -> ResponseViewSchedule:
        if not id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Nenhum id foi enviado.',
            )

        try:
            data = collection.where(filter=FieldFilter('id', '==', id))
            result = data.get()[0].to_dict()
            if result['clinic_id'] and result['patient_id']:
                clinic_id = result['clinic_id']
                patient_id = result['patient_id']

                clinic_doc = (
                    database.collection('clinics').document(clinic_id).get()
                )
                patient_doc = (
                    database.collection('patients').document(patient_id).get()
                )

                if clinic_doc.exists and patient_doc.exists:
                    clinic_data = clinic_doc.to_dict()
                    patient_data = patient_doc.to_dict()

                    response_schedule = ResponseViewSchedule(
                        id=result['id'],
                        datetime=result['datetime'],
                        doctor_responsible=result['doctor_responsible'],
                        clinic=ClinicScheduleResponse(**clinic_data),
                        patient=PatientScheduleResponse(**patient_data),
                    )

                    return response_schedule
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'{e}',
            )

    def delete_schedule_by_id(self, id: str) -> str:
        try:
            collection.document(id).delete()
            return 'ok'
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'{e}',
            )

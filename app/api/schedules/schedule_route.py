from typing import List

from fastapi import APIRouter, status

from app.models.schedule_models import ResponseViewSchedule, Schedule
from app.service.schedule_service import ScheduleService

schedule_route = APIRouter(prefix='/schedule', tags=['schedule'])

schedule_service = ScheduleService()


@schedule_route.post(
    '/',
    response_model_by_alias=False,
    status_code=status.HTTP_201_CREATED,
)
def create_new_schedule(schedule: Schedule):
    """
    Cria dados no firestore de acordo com os dados enviados da API
    """

    return schedule_service.create_new_schedule(schedule)


@schedule_route.get(
    '/',
    response_model=List[ResponseViewSchedule],
    response_model_by_alias=False,
    status_code=status.HTTP_200_OK,
)
def get_all_schedules():
    """
    Retorna uma lista com todos os documentos
    """

    return schedule_service.get_schedule_list()


@schedule_route.get(
    '/{id}',
    response_model=ResponseViewSchedule,
    response_model_by_alias=False,
    status_code=status.HTTP_200_OK,
)
def get_all_schedules(id:str):
    """
    Retorna uma lista com todos os documentos
    """

    return schedule_service.get_schedule_by_id(id)


@schedule_route.delete(
    '/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_schedule_by_id(id: str):
    """
    Deleta um usuário por id (uuid4)
    """
    return schedule_service.delete_schedule_by_id(id)

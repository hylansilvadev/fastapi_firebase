from fastapi.testclient import TestClient
from fastapi import status
from app.main import app


class TestSchedule:
    client = TestClient(app)
    url = '/schedule'
    
    def by_id(self, id:str):
        new_url = self.url +f'/{id}'
        return new_url
    
    def test_should_return_a_list_of_schedules(self):
        request = self.client.get(self.url)
        response_json = request.json()
        
        assert request.status_code == status.HTTP_200_OK
        assert isinstance(response_json, list)


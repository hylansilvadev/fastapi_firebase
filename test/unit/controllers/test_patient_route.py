from fastapi.testclient import TestClient
from fastapi import status
from app.main import app


class TestPatient:
    client = TestClient(app)
    url = '/patient'
    data = {
            "name": "Paciente Teste",
            "whatsapp": "(81) 9 9999-9999",
            "email": "paciente@teste.com",
            "has_avc": True,
            "another_condition": [
                "Depressão",
                "Cancer",
                "Sistosama"
            ],
            "investment_value": 800,
            "addres": {
                "state": "TS",
                "city": "Teste",
                "neighbourhood": "Teste",
                "zip_code": "23432432",
                "search_distance": "5km"
            }
        }
    
    def by_id(self, id:str):
        new_url = self.url +f'/{id}'
        return new_url
    
    def test_shoud_return_a_list_of_patients(self):
        request = self.client.get(self.url)
        response_json = request.json()
        
        assert request.status_code == status.HTTP_200_OK
        assert isinstance(response_json, list)


    def test_shoud_create_a_new_patient_after_delete_then(self):
        request = self.client.post(self.url, json=self.data)
        response_json = request.json()
        
        assert request.status_code == status.HTTP_201_CREATED
        assert response_json['name'] == self.data['name']
        assert response_json['whatsapp'] == self.data['whatsapp']
        assert response_json['email'] == self.data['email']
        assert response_json['has_avc'] == self.data['has_avc']
        assert isinstance(response_json['another_condition'], list)
        assert response_json['investment_value'] == self.data['investment_value']
        assert response_json['addres']["state"] == self.data['addres']["state"]
        assert response_json['addres']["city"] == self.data['addres']["city"]
        assert response_json['addres']["neighbourhood"] == self.data['addres']["neighbourhood"]
        assert response_json['addres']["zip_code"] == self.data['addres']["zip_code"]
        assert response_json['addres']["search_distance"] == self.data['addres']["search_distance"]
        
        
        url = self.by_id(response_json['id'])
        request = self.client.delete(url)
        
        assert request.status_code == status.HTTP_204_NO_CONTENT


    def test_should_create_and_update_a_new_patient_after_delete_then(self):
        first_request = self.client.post(self.url, json=self.data)
        first_response = first_request.json()
        
        new_data = {
            "name": "Teste Paciente",
            "whatsapp": "(81) 9 9999-9994",
            "email": "teste@paciente.com",
            "has_avc": False,
            "another_condition": [],
            "investment_value": 1500,
            "addres": {
                "state": "TS",
                "city": "Teste",
                "neighbourhood": "Teste",
                "zip_code": "23432432",
                "search_distance": "5km"
            }
        }
        
        url = self.by_id(first_response['id'])
        
        request = self.client.put(url, json=new_data)
        response_json = request.json()
        assert request.status_code == status.HTTP_200_OK
        assert response_json['name'] == new_data['name']
        assert response_json['whatsapp'] == new_data['whatsapp']
        assert response_json['email'] == new_data['email']
        assert response_json['has_avc'] == new_data['has_avc']
        assert isinstance(response_json['another_condition'], list)
        assert response_json['investment_value'] == new_data['investment_value']
        assert response_json['addres']["state"] == new_data['addres']["state"]
        assert response_json['addres']["city"] == new_data['addres']["city"]
        assert response_json['addres']["neighbourhood"] == new_data['addres']["neighbourhood"]
        assert response_json['addres']["zip_code"] == new_data['addres']["zip_code"]
        assert response_json['addres']["search_distance"] == new_data['addres']["search_distance"]
        
        request = self.client.delete(url)
        
        assert request.status_code == status.HTTP_204_NO_CONTENT


    def test_should_create_and_return_a_new_patient_by_id_after_delete_then(self):
        first_request = self.client.post(self.url, json=self.data)
        first_response_json = first_request.json()
        
        url = self.by_id(first_response_json['id'])
        
        request = self.client.get(url)
        response_json = request.json()
        assert request.status_code == status.HTTP_200_OK
        assert response_json['name'] == self.data['name']
        assert response_json['whatsapp'] == self.data['whatsapp']
        assert response_json['email'] == self.data['email']
        assert response_json['has_avc'] == self.data['has_avc']
        assert isinstance(response_json['another_condition'], list)
        assert response_json['investment_value'] == self.data['investment_value']
        assert response_json['addres']["state"] == self.data['addres']["state"]
        assert response_json['addres']["city"] == self.data['addres']["city"]
        assert response_json['addres']["neighbourhood"] == self.data['addres']["neighbourhood"]
        assert response_json['addres']["zip_code"] == self.data['addres']["zip_code"]
        assert response_json['addres']["search_distance"] == self.data['addres']["search_distance"]

        request = self.client.delete(url)
        
        assert request.status_code == status.HTTP_204_NO_CONTENT


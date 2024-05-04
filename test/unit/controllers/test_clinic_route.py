from fastapi.testclient import TestClient
from fastapi import status
from app.main import app


class TestClinic:
    client = TestClient(app)
    url = '/clinic'
    data = {
                "name": "Clinica Teste",
                "phone": "(99) 9 9999-9999",
                "email": "teste@teste.com",
                "addres": {
                    "region": "Teste",
                    "state": "TS",
                    "city": "Teste",
                    "neighbourhood": "Teste",
                    "zip_code": "99999999",
                    "lat": "-99.99999",
                    "long": "-99.99999",
                    "addres": "Rua Teste, n° 99"
                    },
                    "responsible_person": {
                        "name": "Profissional Teste",
                        "profession": "Tester"
                    }
            }
    
    def by_id(self, id:str):
        new_url = self.url +f'/{id}'
        return new_url


    def test_should_return_a_list_of_clinics(self):
        request = self.client.get(self.url)
        response_json = request.json()
        
        assert request.status_code == status.HTTP_200_OK
        assert isinstance(response_json, list)


    def test_should_create_a_new_clinic_after_delete_then(self):
        request = self.client.post(self.url, json=self.data)
        
        response_json = request.json()
        
        assert request.status_code == status.HTTP_201_CREATED
        assert response_json["name"] == self.data["name"]
        assert response_json["phone"] == self.data["phone"]
        assert response_json["email"] == self.data["email"]
        assert response_json["addres"]["region"] == self.data["addres"]["region"]
        assert response_json["addres"]["state"] == self.data["addres"]["state"]
        assert response_json["addres"]["city"] == self.data["addres"]["city"]
        assert response_json["addres"]["neighbourhood"] == self.data["addres"]["neighbourhood"]
        assert response_json["addres"]["zip_code"] == self.data["addres"]["zip_code"]
        assert response_json["addres"]["lat"] == self.data["addres"]["lat"]
        assert response_json["addres"]["long"] == self.data["addres"]["long"]
        assert response_json["addres"]["addres"] == self.data["addres"]["addres"]
        assert response_json["responsible_person"]["name"] == self.data["responsible_person"]["name"]
        assert response_json["responsible_person"]["profession"] == self.data["responsible_person"]["profession"]
        
        new_url = self.by_id(response_json['id'])
        request = self.client.delete(new_url)
        
        assert request.status_code == status.HTTP_204_NO_CONTENT

    
    def test_shoud_create_and_update_a_new_clinic_after_delete_then(self):
        first_request = self.client.post(self.url, json=self.data)
        first_response = first_request.json()

        new_data = {
            "name": "Clinica Teste 34",
            "phone": "(99) 9 9929-9549",
            "email": "teste.second@teste.com",
            "addres": {
                "region": "Teste weq",
                "state": "TS qewqe",
                "city": "Teste qewqeqweq",
                "neighbourhood": "Teste eqeqeq",
                "zip_code": "9999999942",
                "lat": "-432432",
                "long": "43242",
                "addres": "Rua Teste, n° 54"
                },
                "responsible_person": {
                    "name": "Profissional Teste",
                    "profession": "Tester"
                }
            }
        
        url = self.by_id(first_response['id'])
        
        request = self.client.put(url, json=new_data)
        
        response_json = request.json()
        assert request.status_code == status.HTTP_200_OK
        assert response_json["name"] == new_data["name"]
        assert response_json["phone"] == new_data["phone"]
        assert response_json["email"] == new_data["email"]
        assert response_json["addres"]["region"] == new_data["addres"]["region"]
        assert response_json["addres"]["state"] == new_data["addres"]["state"]
        assert response_json["addres"]["city"] == new_data["addres"]["city"]
        assert response_json["addres"]["neighbourhood"] == new_data["addres"]["neighbourhood"]
        assert response_json["addres"]["zip_code"] == new_data["addres"]["zip_code"]
        assert response_json["addres"]["lat"] == new_data["addres"]["lat"]
        assert response_json["addres"]["long"] == new_data["addres"]["long"]
        assert response_json["addres"]["addres"] == new_data["addres"]["addres"]
        assert response_json["responsible_person"]["name"] == new_data["responsible_person"]["name"]
        assert response_json["responsible_person"]["profession"] == new_data["responsible_person"]["profession"]
        
        request = self.client.delete(url)
        
        assert request.status_code == status.HTTP_204_NO_CONTENT


    def test_shoud_create_and_return_a_new_clinic_by_id_after_delete_then(self):
        first_request = self.client.post(self.url, json=self.data)
        first_response = first_request.json()
        
        url = self.by_id(first_response['id'])
        
        request = self.client.get(url)
        response_json = request.json()
        
        assert request.status_code == status.HTTP_200_OK
        assert response_json["name"] == self.data["name"]
        assert response_json["phone"] == self.data["phone"]
        assert response_json["email"] == self.data["email"]
        assert response_json["addres"]["region"] == self.data["addres"]["region"]
        assert response_json["addres"]["state"] == self.data["addres"]["state"]
        assert response_json["addres"]["city"] == self.data["addres"]["city"]
        assert response_json["addres"]["neighbourhood"] == self.data["addres"]["neighbourhood"]
        assert response_json["addres"]["zip_code"] == self.data["addres"]["zip_code"]
        assert response_json["addres"]["lat"] == self.data["addres"]["lat"]
        assert response_json["addres"]["long"] == self.data["addres"]["long"]
        assert response_json["addres"]["addres"] == self.data["addres"]["addres"]
        assert response_json["responsible_person"]["name"] == self.data["responsible_person"]["name"]
        assert response_json["responsible_person"]["profession"] == self.data["responsible_person"]["profession"]
        
        request = self.client.delete(url)
        
        assert request.status_code == status.HTTP_204_NO_CONTENT


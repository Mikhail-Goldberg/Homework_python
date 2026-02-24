import pytest
import requests
from CompanyApi import CompanyApi

@pytest.fixture(scope="session")
def api():
    url = "https://yougile.com/api-v2/"
    creds = {
        #'login': '',
        #'password': '',
        'companyId': 'b8eacfee-50be-41ee-923a-638cb85b2b3c'
    }

    resp = requests.post(url + 'auth/keys', json=creds)
    token = resp.json()["key"]
    return CompanyApi(url, token)

def test_positive_create_company(api):
    body = api.create_company()
    assert body.status_code == 201

def test_negative_create_company(api):
    body = api.create_company(name=None)
    assert body.status_code == 400

def test_positive_change_company(api):
    body = api.change_company()
    assert body.status_code == 200

def test_negative_change_company(api):
    body = api.change_company(company='Рандомное название')
    assert body.status_code == 400

def test_positive_get_project_by_id(api):
    body = api.get_project_by_id()
    assert body.status_code == 200

def test_negative_get_project_by_id(api):
    body = api.get_project_by_id(id=555555)
    assert body.status_code == 404



# import requests
# import pytest

# base_url = "https://yougile.com/api-v2/"

# @pytest.fixture(scope="session")
# def get_token(login = 'mishagoldberg761@gmail.com', password = 'йцукен12', companyId = 'b8eacfee-50be-41ee-923a-638cb85b2b3c'):
#     creds = {
#         'login': login,
#         'password': password,
#         'companyId': companyId
#         }
#     resp = requests.post(base_url+'auth/keys', json=creds)
#     token = resp.json()["key"]
#     return token

# def test_get_company_list():
#     headers = {
#         'Authorization': f'Token {get_token()}',
#         'Content-Type': 'application/json'
#     }
#     resp = requests.get(base_url+'projects', headers=headers)
#     assert resp.status_code == 200
#     id = resp.json()['content'][-1]["id"]
#     return id

# def test_create_company(name='Новый проект для работы'):
#     company = {
#         'title': name
#     }

#     headers = {
#         'Authorization': f'Token {get_token()}',
#         'Content-Type': 'application/json'
#     }

#     resp = requests.post(base_url+'projects', headers=headers, json=company)
#     assert resp.status_code == 201
#     company_id = resp.json()["id"]
#     return company_id

# def test_change_company(new_name = 'Измененный проект'):
#     company = {
#         'title': new_name
#     }

#     headers = {
#         'Authorization': f'Token {get_token()}',
#         'Content-Type': 'application/json'
#     }

#     id = test_get_company_list()

#     url = f"{base_url}projects/{id}"
    
#     resp = requests.put(url, headers=headers, json=company)
#     assert resp.status_code == 200

# def test_get_project_by_id():

#     headers = {
#         'Authorization': f'Token {get_token()}',
#         'Content-Type': 'application/json'
#     }

#     id = test_get_company_list()

#     url = f"{base_url}projects/{id}"

#     resp = requests.get(url, headers=headers)
#     assert resp.status_code == 200

import requests

class CompanyApi:

    def __init__(self, url, token):
        self.url = url
        self.headers = {
            'Authorization': f'Token {token}',
            'Content-Type': 'application/json'
        }

    def get_token(self, login = 'mishagoldberg761@gmail.com', password = 'йцукен12', companyId = 'b8eacfee-50be-41ee-923a-638cb85b2b3c'):
        creds = {
            'login': login,
            'password': password,
            'companyId': companyId
            }
        resp = requests.post(self.url+'auth/keys', json=creds)
        token = resp.json()["key"]
        return token
    
    def get_company_list(self):
        resp = requests.get(self.url+'projects', headers=self.headers)
        id = resp.json()['content'][-1]["id"]
        return id
    
    def create_company(self, name='Новый проект для работы'):
        company = {
            'title': name
        }

        resp = requests.post(self.url+'projects', headers=self.headers, json=company)
        return resp
    
    def change_company(self, new_name = 'Измененный проект', company=None):
        if company is None:
            company = {
                'title': new_name
            }

        id = self.get_company_list()

        url = f"{self.url}projects/{id}"
        
        resp = requests.put(url, headers=self.headers, json=company)
        return resp
    
    def get_project_by_id(self, id=None):
        if id is None:
            id = self.get_company_list()

        url = f"{self.url}projects/{id}"

        resp = requests.get(url, headers=self.headers)
        return resp


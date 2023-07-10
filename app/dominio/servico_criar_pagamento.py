from dotenv import load_dotenv
import os
import requests

load_dotenv()

class MercadoPagoService:
    def __init__(self):
        self.access_token = os.getenv('ACCESS_TOKEN')
        self.base_url = 'https://api.mercadopago.com/v1/payments'
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
    
    def criar_pagamento(self, pagamento_data):
        url = self.base_url
        response = requests.post(url, json=pagamento_data, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Erro ao criar pagamento')

    def buscar_pagamentos(self, external_reference):
        url = f'{self.base_url}/search'
        params = {
            'sort': 'date_created',
            'criteria': 'desc',
            'external_reference': external_reference,
            'range': 'date_created',
            'begin_date': 'NOW-30DAYS',
            'end_date': 'NOW'
        }

        response = requests.get(url, params=params, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Erro ao buscar pagamentos')

from flask import url_for
from flask_restx import Api


class BaseApi(Api):
    @property
    def specs_url(self):
        return url_for(self.endpoint('specs'), _external=False)


authorizations = {
    'APIKeyHeader': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY',
        'description': 'Informe abaixo a API-KEY fornecida para autenticação'
    }
}

api = BaseApi(
    version='0.1.0',
    title='PyCoinLab',
    description='Projeto de estudos para implementação de uma blockchain em Python',
    security=['apiKey'],
    authorizations=authorizations
)

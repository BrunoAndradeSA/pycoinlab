from app.api import api

namespace = api.namespace(
    name='transaction',
    description='Operações referentes a transações que serão adicionadas ao bloco minerado'
)

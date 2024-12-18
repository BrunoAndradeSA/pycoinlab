from flask_restx import Resource
from app.decorators import auth_with_api_key
from app.api import api
from app.constants import HTTP_CODE
from app.serializers import defautl_response
from app.modules.chain.namespace import namespace
from app.modules.chain.services.get_chain_service import GetChainService


@namespace.route('', methods=['GET'])
class GetChain(Resource):
    @api.response(200, description=HTTP_CODE[200], model=defautl_response)
    @api.response(400, description=HTTP_CODE[400], model=defautl_response)
    @api.response(404, description=HTTP_CODE[404], model=defautl_response)
    @auth_with_api_key
    def get(self):
        """
        Lista todos os blocos e transações já adicionadas à blockchain
        """
        return GetChainService().get_chain()

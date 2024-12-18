from flask import request
from flask_restx import Resource
from app.decorators import auth_with_api_key
from app.api import api
from app.constants import HTTP_CODE
from app.serializers import defautl_response
from app.modules.mining.namespace import namespace
from app.modules.mining.services.do_mining_service import DoMiningService
from app.modules.mining.parsers.do_mining_parser import parser


@namespace.route('/', methods=['POST'])
class DoMining(Resource):
    @api.expect(parser)
    @api.response(200, description=HTTP_CODE[200], model=defautl_response)
    @api.response(400, description=HTTP_CODE[400], model=defautl_response)
    @api.response(404, description=HTTP_CODE[404], model=defautl_response)
    @auth_with_api_key
    def post(self):
        """
        Tenta realizar a mineração de um bloco e adicioná-lo à blockchain
        """
        miner_address = request.args.get('miner_address')

        return DoMiningService().do_mining(miner_address=miner_address)

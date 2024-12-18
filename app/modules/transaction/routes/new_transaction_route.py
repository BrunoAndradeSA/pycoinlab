from flask import request
from flask_restx import Resource
from app.decorators import auth_with_api_key
from app.api import api
from app.constants import HTTP_CODE
from app.serializers import defautl_response
from app.modules.transaction.serializers.new_transaction_serializer import new_transaction_payload
from app.modules.transaction.services.new_transaction_service import NewTransactionService
from app.modules.transaction.namspace import namespace


@namespace.route('/new', methods=['PUT'])
class NewTransaction(Resource):
    @api.expect(new_transaction_payload)
    @api.response(201, description=HTTP_CODE[201], model=defautl_response)
    @api.response(400, description=HTTP_CODE[400], model=defautl_response)
    @api.response(404, description=HTTP_CODE[404], model=defautl_response)
    @auth_with_api_key
    def put(self):
        """
        Create a new transaction
        """
        payload = request.get_json()

        return NewTransactionService().new_transaction(transaction_payload=payload)
from flask_restx import fields
from app.api import api


new_transaction_payload = api.model(
    "NewTransactionPayload",
    {
        'sender': fields.String(
            description='Transaction senders Wallet ID',
            required=True,
            example='009babf7-bbfc-47d4-b9bd-3412cbcda5fa',
            max_length=36
        ),
        'recipient': fields.String(
            description='Transaction recipients Wallet ID',
            required=True,
            example='f1d255d3-107f-44f9-aa18-ac20c7fe657e',
            max_length=36
        ),
        'amount': fields.Float(
            description='Transaction amount',
            required=True,
            example=0.55
        )
    }
)
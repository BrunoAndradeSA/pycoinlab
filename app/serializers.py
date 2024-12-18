from flask_restx import fields
from app.api import api


__DEFAULT_FIELDS = {
    'message': fields.String(
        description='Response description',
        required=True,
        example='Request successfully processed'
    ),
    'code': fields.Integer(
        description='Response code (Always return 0 on success)',
        required=True,
        example=0
    )
}

defautl_response = api.model("DefaultResponse", __DEFAULT_FIELDS)

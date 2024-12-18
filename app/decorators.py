from functools import wraps, partial
from flask import request
from typing import Callable, Union
from app.api import api
from app.serializers import defautl_response
from app.constants import HTTP_CODE
from app.utils import get_default_response, validate_authentication


def auth_with_api_key(func: Callable = None) -> Union[dict, Callable]:
    if func is None:
        return partial(auth_with_api_key)

    @api.response(401, description=HTTP_CODE[401], model=defautl_response)
    @api.response(403, description=HTTP_CODE[403], model=defautl_response)
    @api.response(405, description=HTTP_CODE[405], model=defautl_response)
    @api.response(500, description=HTTP_CODE[500], model=defautl_response)
    @api.response(503, description=HTTP_CODE[503], model=defautl_response)
    @api.doc(security='APIKeyHeader')
    @wraps(func)
    def wrap_function(*args, **kwargs):
        try:
            api_key = request.headers.get('X-API-KEY')

            if not api_key:
                return get_default_response(
                    message='API Key não fornecida para autenticação',
                    code=-1,
                    http_code=403
                )

            if not validate_authentication(api_key):
                return get_default_response(
                    message=f'Falha ao autenticar com a API Key fornecida: {
                        api_key}',
                    code=-1,
                    http_code=401
                )

            return func(*args, **kwargs)
        except Exception as e:
            pass

    return wrap_function

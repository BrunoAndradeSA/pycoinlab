from typing import Tuple
from app.constants import HTTP_CODE
from app.config import Config


@staticmethod
def get_default_response(message: str, code: int, http_code: int) -> Tuple[dict, int]:
    if code in HTTP_CODE.keys() and code == http_code:
        message = HTTP_CODE[code].replace('$REASON', message)

    return {'message': message, 'code': code}, http_code


@staticmethod
def validate_authentication(api_key: str) -> bool:
    return True if api_key == Config.SECRET_KEY else False

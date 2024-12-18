from typing import Tuple
from app.utils import get_default_response
from app.services.blockchain_service import Blockchain


class NewTransactionService:
    @staticmethod
    def new_transaction(transaction_payload: dict) -> Tuple[dict, int]:
        try:
            block_index = Blockchain().new_transaction(
                sender=transaction_payload["sender"],
                recipient=transaction_payload["recipient"],
                amount=transaction_payload["amount"]
            )

            if block_index >= 1:
                return get_default_response(
                    message=f"Sucesso! A transação será adicionada ao bloco {
                        block_index}",
                    code=0,
                    http_code=201
                )

            return get_default_response(
                message="Nenhum bloco minerado ainda",
                code=-1,
                http_code=404
            )
        except Exception as e:
            return get_default_response(message=f'Ocorreu um erro inesperado: {e}', code=-1, http_code=500)

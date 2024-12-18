from typing import Tuple
from app.modules.chain.repositories.get_chain_repository import GetChainRepository
from app.utils import get_default_response


class GetChainService:
    @staticmethod
    def get_chain() -> Tuple[dict, int]:
        try:
            chain = GetChainRepository().get_all_blocks()

            if not chain:
                return get_default_response(message='Nenhum bloco adicionado à blockchain ainda', code=-1, http_code=404)

            response = {
                'chain': [
                    {
                        'index': block.index,
                        'timestamp': block.timestamp,
                        'transactions': [
                            {
                                'sender': tx.sender or 'N/A',
                                'recipient': tx.recipient or 'N/A',
                                'amount': tx.amount or 0
                            }
                            for tx in block.transactions
                        ],
                        'proof': block.proof,
                        'previous_hash': block.previous_hash
                    }
                    for block in chain
                ],
                'length': len(chain)
            }

            return response, 200
        except Exception as e:
            return get_default_response(message=f'Ocorreu um erro inesperado: {e}', code=-1, http_code=500)

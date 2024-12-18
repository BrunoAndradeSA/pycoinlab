from typing import Tuple
from app.utils import get_default_response
from app.services.blockchain_service import Blockchain


class DoMiningService:
    @staticmethod
    def do_mining(miner_address: str) -> Tuple[dict, int]:
        try:
            if not miner_address:
                return get_default_response(
                    message="Miner Address is mandatory!",
                    code=-1,
                    http_code=400
                )

            blockchain = Blockchain()

            last_block = blockchain.last_block()
            last_proof = last_block.proof
            proof = blockchain.proof_of_work(last_proof=last_proof)

            blockchain.new_transaction(
                sender="0",
                recipient=miner_address,
                amount=1
            )

            block = blockchain.new_block(proof=proof)

            response = {
                'message': "New block mined!",
                'index': block.index,
                'transactions': [
                    {'sender': tx.sender, 'recipient': tx.recipient, 'amount': tx.amount}
                    for tx in block.transactions
                ],
                'proof': block.proof,
                'previous_hash': block.previous_hash
            }

            return response, 200
        except Exception as e:
            return get_default_response(message=f'An Error occurred: {e}', code=-1, http_code=500)

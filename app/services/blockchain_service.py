import json
import hashlib
from app.extensions import db
from app.models import Block, Transaction


class Blockchain:
    def __init__(self):
        self.current_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        if Block.query.count() == 0:
            self.new_block(proof=100, previous_hash="1")

    def new_block(self, proof, previous_hash=None):
        last_block = self.last_block()
        index = (last_block.index + 1) if last_block else 1
        block = Block(
            index=index,
            proof=proof,
            previous_hash=previous_hash or self.hash_block(last_block)
        )

        db.session.add(block)
        db.session.commit()

        for transaction in self.current_transactions:
            self.save_transaction(transaction, block.id)

        self.current_transactions = []

        return block

    @staticmethod
    def save_transaction(transaction, block_id=None):
        trans = Transaction(
            sender=transaction["sender"],
            recipient=transaction["recipient"],
            amount=transaction["amount"],
            block_id=block_id
        )

        db.session.add(trans)
        db.session.commit()

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        }

        self.current_transactions.append(transaction)

        return self.last_block().index + 1 if self.last_block() else 0

    @staticmethod
    def last_block() -> Block:
        return Block.query.order_by(Block.id.desc()).first()

    @staticmethod
    def hash_block(block):
        block_string = json.dumps({
            "index": block.index,
            "timestamp": block.timestamp,
            "proof": block.proof,
            "previous_hash": block.previous_hash
        }, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        proof = 0

        while not self.valid_proof(last_proof, proof):
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4] == "0000"

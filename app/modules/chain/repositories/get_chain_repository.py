from app.models import Block
from sqlalchemy.orm import joinedload


class GetChainRepository:
    @staticmethod
    def get_all_blocks():
        return Block.query.options(joinedload(Block.transactions)).all()

from app.extensions import db


class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(128), nullable=False)
    recipient = db.Column(db.String(128), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    block_id = db.Column(db.Integer, db.ForeignKey('blocks.id'), nullable=True)

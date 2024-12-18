from flask_restx import reqparse


parser = reqparse.RequestParser()

parser.add_argument(
    'miner_address',
    type=str,
    location='query',
    required=True,
    help="Miner's wallet address"
)

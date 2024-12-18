import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "postgresql://usuario:senha@localhost:5432/pycoinlab")
    SQLALCHEMY_TRACK_MODIFICATIOINS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "minha-secret-key")

from app.extensions import db
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env
root_dir = os.getcwd()
dotenv_path = join(root_dir, 'app', '.env')
load_dotenv(dotenv_path=dotenv_path)

# Configuração Alembic
config = context.config

# Substitui sqlalchemy.url com DATABASE_URL do ambiente
database_url = os.getenv("DATABASE_URL")
if database_url:
    config.set_main_option("sqlalchemy.url", database_url)
else:
    raise KeyError("A variável de ambiente DATABASE_URL não está definida.")

# Configuração de logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = db.metadata

# Funções padrão do Alembic


def run_migrations_offline():
    """Executa as migrations em modo offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Executa as migrations em modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection,
                          target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

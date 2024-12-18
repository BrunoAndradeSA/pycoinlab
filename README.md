# PyCoinLab

**PyCoinLab** é um projeto educacional para criar uma criptomoeda simples baseada em blockchain, utilizando Python, Flask, SQLAlchemy e Alembic. Este projeto é voltado para estudo e experimentações sobre os conceitos fundamentais de blockchain e criptomoedas.

---

## **Recursos do Projeto**

- Implementação de uma blockchain básica.
- Integração com um banco de dados PostgreSQL para armazenamento de blocos e transações.
- Utilização do framework Flask com Blueprints para modularização.
- Gerenciamento de dependências com Poetry.
- Migrações de banco de dados com Alembic.

---

## **Configuração do Projeto**

### **1. Requisitos**

Certifique-se de ter os seguintes programas instalados:

- **Python 3.10 ou superior**
- **Poetry** (para gerenciamento de dependências)
- **PostgreSQL** (para banco de dados)
- **Git** (para controle de versão)

### **2. Clone o Repositório**

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/SEU_USUARIO/pycoinlab.git
cd pycoinlab
```

### **3. Configuração do Ambiente Virtual**

Crie um ambiente virtual com o Poetry:

```bash
poetry install
```

Ative o ambiente virtual:

```bash
poetry shell
```

### **4. Configuração do Banco de Dados**

1. Crie um banco de dados PostgreSQL para o projeto:

```sql
CREATE DATABASE pycoinlab;
```

2. Configure o arquivo `.env` na raiz do projeto com as credenciais do banco de dados. Exemplo:

```
FLASK_APP=run.py
FLASK_ENV=development
DATABASE_URL=postgresql://usuario:senha@localhost:5432/pycoinlab
SECRET_KEY=sua-secret-key-para-autenticacao
```

### **5. Execute as Migrações**

Inicialize as migrações e aplique-as ao banco de dados:

```bash
flask db upgrade
```

---

## **Como Executar o Projeto**

Inicie o servidor Flask:

```bash
poetry run flask run
```

Acesse a aplicação no navegador em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## **Licença**

Este projeto é licenciado sob a Licença GPL v3.0. Consulte o arquivo `LICENSE` para mais detalhes.

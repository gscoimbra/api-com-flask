from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Configurações de conexão
DATABASE_URL = "postgresql://postgres:root@localhost:5432/api-python"

# Cria o engine (motor de conexão)
engine = create_engine(DATABASE_URL)

# Base para os modelos
Base = declarative_base()

# Cria sessões para manipular dados
SessionLocal = sessionmaker(bind=engine)
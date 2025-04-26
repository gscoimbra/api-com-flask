import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Esse código diz para o Python: "considera também o diretório acima (..) para buscar os módulos".

import pandas as pd
from infra.database import SessionLocal
from domain.task import Task

def run_etl():
    # 1. Extrair (ler CSV)
    df = pd.read_csv('etl/tasks.csv')

    # 2. Transformar (deixar o título em maiúsculo)
    df['title'] = df['title'].str.upper()

    # 3. Carregar (inserir no banco)
    session = SessionLocal()

    for _, row in df.iterrows():
        task = Task(title=row['title'], description=row['description'])
        session.add(task)

    session.commit()
    session.close()
    print('ETL finalizado com sucesso!')

if __name__ == "__main__":
    run_etl()

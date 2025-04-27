# API de Gerenciamento de Tarefas

Este projeto é uma API desenvolvida em Flask seguindo os princípios da Clean Architecture.  
Ela permite criar e listar tarefas, possui documentação Swagger integrada e suporta execução de tarefas assíncronas com Celery e Redis.

---

## 🚀 Tecnologias Utilizadas

- Python 3.11
- Flask
- Flasgger (Swagger UI)
- SQLAlchemy
- PostgreSQL
- Pandas (ETL)
- Celery
- Redis
- Docker
- Docker Compose
- GitHub Actions (CI/CD)

## ⚙️ Como rodar o projeto

> Requisitos:
> - Docker instalado
> - Docker Compose instalado

### 1. Clone o repositório

```bash
git clone https://github.com/gscoimbra/api-com-flask.git
cd api-com-flask
```

### 2. Suba os contêineres
```bash
docker-compose up --build
```
### Isso irá:
- Construir a imagem da aplicação Flask.
- Iniciar a API na porta 5000.
- Iniciar o Redis na porta 6379.

### 3. Acesse a documentação da API
Abra o navegador em:
```bash
http://localhost:5000/apidocs
```

## 📦 Estrutura de Pastas
````
api-em-flask/
│
├── app.py                 # Arquivo principal da aplicação Flask
├── domain/                # Entidades de domínio
├── interfaces/            # Controllers (camada de interface)
├── infra/                 # Banco de dados, Celery e infraestruturas
├── usecases/              # Lógica de negócios (serviços)
├── etl/                   # Rotina de ETL para carga de tarefas
├── requirements.txt       # Dependências do projeto
├── Dockerfile             # Definição da imagem Docker
├── docker-compose.yml     # Orquestração dos serviços
└── .github/workflows/ci.yml  # Workflow de CI no GitHub Actions
````

## 🛠️ Funcionalidades Implementadas
- API Flask estruturada em camadas (Clean Architecture)
- Documentação de API com Swagger
- Conexão com banco PostgreSQL via SQLAlchemy
- Rotina ETL para importar tarefas de CSV
- Tarefas assíncronas com Celery + Redis
- Dockerização completa da aplicação
- Orquestração com Docker Compose
- CI/CD básico usando GitHub Actions

## 📚 Como contribuir
- Faça um fork do projeto
- Crie uma branch (git checkout -b feature/nova-feature)
- Commit suas alterações (git commit -m 'Adiciona nova feature')
- Push para a branch (git push origin feature/nova-feature)
- Abra um Pull Request
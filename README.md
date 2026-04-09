# 🛒 Products API

API de gestão de produtos desenvolvida em Python com **FastAPI** e **PostgreSQL**, com suporte a **CLI**, **logging em base de dados**, **Docker** e **CI/CD**.

Este projeto foi desenvolvido com foco em aprendizagem prática de backend, incluindo integração com base de dados, construção de API REST e automação com pipelines.

---

## 🚀 Tecnologias utilizadas

* Python 3.11+
* FastAPI
* PostgreSQL
* psycopg (v3)
* Docker & Docker Compose
* Pydantic
* Pytest
* GitHub Actions (CI/CD)

---

## ⚙️ Funcionalidades

* CRUD completo de produtos
* Atualização de stock
* Atualização de preço
* Exportação de dados para JSON
* Logging de operações (insert, update, delete) em base de dados
* CLI interativo para gestão de produtos
* API REST com validação de dados
* Testes automatizados com pytest
* Pipeline CI/CD com GitHub Actions

---

## 📦 Estrutura do projeto

```
app/
  api.py
  db.py
  db_cli.py

tests/
  test_api.py

docker-compose.yml
Dockerfile
requirements.txt
```

---

## 🐳 Como correr o projeto (Docker)

### 1. Build e iniciar containers

```
docker compose up --build
```

### 2. Aceder à API

* API: http://localhost:8000
* Documentação automática: http://localhost:8000/docs

---

## 💻 CLI (linha de comandos)

Executar o CLI:

```
docker compose run --rm app
```

ou

```
docker exec -it products-app python app/db_cli.py
```

---

## 📡 Endpoints principais

| Método | Endpoint             | Descrição            |
| ------ | -------------------- | -------------------- |
| GET    | /products            | Listar produtos      |
| GET    | /products/{id}       | Obter produto por ID |
| POST   | /products            | Criar novo produto   |
| PATCH  | /products/{id}/stock | Atualizar stock      |
| PATCH  | /products/{id}/price | Atualizar preço      |
| DELETE | /products/{id}       | Remover produto      |

---

## 🧾 Exemplo de request

### Criar produto

```json
{
  "sku": "SKU001",
  "name": "Produto Teste",
  "price": 9.99,
  "stock": 10
}
```

---

## 🗄️ Base de dados

O projeto utiliza PostgreSQL com duas tabelas principais:

* `products` → dados dos produtos
* `audit_logs` → histórico de operações (insert, update, delete)

Todas as alterações são automaticamente registadas na tabela de logs.

---

## 🧪 Testes

Executar testes:

```
python -m pytest
```

---

## 🔄 CI/CD

O projeto inclui uma pipeline com GitHub Actions que:

* instala dependências
* executa testes
* faz build da imagem Docker

---

## 📁 Exportação de dados

Os produtos podem ser exportados para JSON através do CLI, sendo guardados num ficheiro local.

---

## 📚 Aprendizagens

Durante o desenvolvimento deste projeto foram explorados:

* Integração entre Python e PostgreSQL
* Criação de APIs REST com FastAPI
* Validação de dados com Pydantic
* Gestão de containers com Docker
* Estruturação de projetos backend
* Implementação de logging em base de dados
* Automação com GitHub Actions
* Escrita de testes com pytest

---

## ⚠️ Notas

* O projeto foi desenvolvido com fins educativos
* O foco foi manter o código simples e compreensível
* Algumas decisões priorizam clareza sobre abstração excessiva

---

## 📌 Autor

Desenvolvido por **Jordy Oliveira**

# 🛒 Products API

A product management API built with **Python**, **FastAPI**, and **PostgreSQL**, featuring a **CLI interface**, **database logging**, **Docker support**, and **CI/CD automation**.

This project was developed with a focus on practical backend learning, including database integration, REST API development, and pipeline automation.

---

## 🚀 Tech Stack

* Python 3.11+
* FastAPI
* PostgreSQL
* psycopg (v3)
* Docker & Docker Compose
* Pydantic
* Pytest
* GitHub Actions (CI/CD)

---

## ⚙️ Features

* Full CRUD operations for products
* Stock update functionality
* Price update functionality
* JSON data export
* Database logging (insert, update, delete operations)
* Interactive CLI for product management
* REST API with input validation
* Automated testing with pytest
* CI/CD pipeline with GitHub Actions

---

## 📦 Project Structure

```text
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

## 🐳 Running the Project (Docker)

### 1. Build and start containers

```bash
docker compose up --build
```

### 2. Access the API

* API: http://localhost:8000
* Interactive docs: http://localhost:8000/docs

---

## 💻 CLI (Command Line Interface)

Run the CLI:

```bash
docker compose run --rm app
```

or

```bash
docker exec -it products-app python app/db_cli.py
```

---

## 📡 Main Endpoints

| Method | Endpoint             | Description          |
| ------ | -------------------- | -------------------- |
| GET    | /products            | List all products    |
| GET    | /products/{id}       | Get product by ID    |
| POST   | /products            | Create a new product |
| PATCH  | /products/{id}/stock | Update stock         |
| PATCH  | /products/{id}/price | Update price         |
| DELETE | /products/{id}       | Delete product       |

---

## 🧾 Example Request

### Create product

```json
{
  "sku": "SKU001",
  "name": "Test Product",
  "price": 9.99,
  "stock": 10
}
```

---

## 🗄️ Database

The project uses PostgreSQL with two main tables:

* `products` → product data
* `audit_logs` → operation history (insert, update, delete)

All changes are automatically logged in the database.

---

## 🧪 Testing

Run tests:

```bash
python -m pytest
```

---

## 🔄 CI/CD

The project includes a GitHub Actions pipeline that:

* installs dependencies
* runs tests
* builds the Docker image

---

## 📁 Data Export

Products can be exported to JSON using the CLI, saving results to a local file.

---

## 📚 What I Learned

During this project, I worked on:

* Python + PostgreSQL integration
* Building REST APIs with FastAPI
* Data validation with Pydantic
* Containerization with Docker
* Backend project structuring
* Database logging strategies
* CI/CD with GitHub Actions
* Writing automated tests with pytest

---

## ⚠️ Notes

* This project was developed for learning purposes
* Code was intentionally kept simple and readable
* Some design decisions favor clarity over abstraction

---

## 📌 Author

Developed by **Jordy Oliveira**

____________________________________________________________________________________________________________________________________________________________________________________

PT-PT

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

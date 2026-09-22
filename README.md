# Sistema de Controle de Vendas

Sistema desenvolvido em **Python + PostgreSQL** para gerenciamento de clientes, utilizando operações CRUD e conexão com banco de dados através da biblioteca `psycopg`.

## Tecnologias utilizadas

* Python
* PostgreSQL
* Psycopg 3
* SQL
* Programação Orientada a Objetos (POO)

## Funcionalidades

* Cadastro de clientes
* Listagem de clientes
* Busca de clientes por nome
* Atualização de clientes
* Exclusão de clientes
* Validação de nome, e-mail e telefone
* Tratamento de entradas inválidas
* Conexão com banco de dados PostgreSQL

## Operações CRUD

O projeto implementa as quatro operações fundamentais:

* **Create** → cadastro de clientes
* **Read** → listagem e busca de clientes
* **Update** → atualização dos dados
* **Delete** → exclusão de clientes

## Estrutura do banco

A tabela `clientes` possui os seguintes campos:

| Campo      | Tipo         | Descrição           |
| ---------- | ------------ | ------------------- |
| `id`       | SERIAL       | Identificador único |
| `nome`     | VARCHAR(100) | Nome do cliente     |
| `email`    | VARCHAR(50)  | E-mail do cliente   |
| `telefone` | VARCHAR(20)  | Telefone do cliente |

## Estrutura do projeto

```text
sistema-controle-vendas/
│
├── database.py
├── criar_tabela.py
├── cliente.py
└── README.md
```

## Exemplo de conexão

A conexão com o PostgreSQL é realizada utilizando `psycopg`:

```python
import psycopg

def conectar():
    conexao = psycopg.connect(
        host="localhost",
        dbname="sistema_vendas",
        user="postgres",
        password="SUA_SENHA",
        port=5432
    )

    cursor = conexao.cursor()

    return conexao, cursor
```

## Objetivo

Este projeto faz parte da minha jornada de estudos em **Backend com Python** e foi desenvolvido para praticar a integração entre uma aplicação Python e um banco de dados PostgreSQL.

O projeto também serviu para consolidar conhecimentos de **SQL, CRUD, POO, validação de dados e operações com banco de dados**.

## Próximos passos

* Melhorar a organização do projeto
* Separar responsabilidades entre os arquivos
* Implementar gerenciamento de produtos
* Implementar registro de vendas
* Evoluir o projeto posteriormente para uma API

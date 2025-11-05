# Sistema Acadêmico

## Introdução

O Sistema Acadêmico é um sistema cliente-servidor simples para gerenciar turmas, alunos, aulas e atividades. Ele é implementado em Python e utiliza um banco de dados SQLite para persistência de dados. O cliente é uma interface de linha de comando (CLI) que interage com o servidor via sockets.

## Features

O sistema possui três perfis de usuário com diferentes níveis de permissão:

### Administrador
- Gerenciar Alunos (Criar, Listar, Remover, Gerar Relatório)
- Gerenciar Atividades (Enviar, Listar, Remover)
- Gerenciar Aulas (Registrar, Listar, Remover)
- Gerenciar Turmas (Criar, Listar, Remover, Gerar Relatório)
- Gerenciar Usuários (Criar, Listar, Remover)
- Resetar o banco de dados

### Professor
- Listar Alunos
- Criar Aluno
- Registrar Aula
- Listar Aulas de uma Turma
- Enviar Atividade
- Listar Atividades de uma Turma
- Gerar Relatório de Alunos (CSV)

### Aluno
- Listar Turmas
- Listar Aulas de uma Turma
- Listar Atividades de uma Turma
- Baixar Atividade

## Tecnologias Utilizadas

- Python 3
- SQLite 3

## Estrutura do Projeto

```
.
├── cliente
│   └── main.py         # Ponto de entrada do cliente
├── servidor
│   ├── main.py         # Ponto de entrada do servidor
│   ├── auth.py         # Controle de permissões
│   ├── database.py     # Configuração e inicialização do banco de dados
│   └── modulos         # Módulos com a lógica de negócio
│       ├── alunos.py
│       ├── atividades.py
│       ├── aulas.py
│       ├── turmas.py
│       └── usuarios.py
├── testes
│   ├── test_alunos.py
│   ├── ...
│   └── test_usuarios.py
├── requirements.txt    # Dependências do projeto
└── sistema_academico.db # Banco de dados SQLite
```

## Como Executar

### Pré-requisitos

- Python 3.8 ou superior

### Instalação

1.  Clone o repositório:
    ```bash
    git clone <url-do-repositorio>
    cd sistema-academico
    ```

2.  Crie um ambiente virtual e ative-o:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### Executando o Servidor

Em um terminal, execute o seguinte comando:

```bash
python3 -m servidor.main
```

O servidor estará escutando na porta 9998.

### Executando o Cliente

Em outro terminal, execute o seguinte comando:

```bash
python3 -m cliente.main
```

Siga as instruções no menu para interagir com o sistema.

**Usuários Padrão:**
- **Administrador:** usuário `admin`, senha `admin`
- **Professor:** usuário `prof`, senha `prof`
- **Aluno:** usuário `aluno`, senha `aluno`

## Como Executar os Testes

Para executar os testes, utilize o `pytest`:

```bash
pytest
```

# ProjectETLExtractAPI

Projeto de ETL (Extract, Transform, Load) para monitoramento de preços de criptomoedas em tempo real.

## Descrição

Este projeto implementa um pipeline ETL para monitorar e armazenar preços de criptomoedas em tempo real. O sistema extrai dados da API Coinbase, transforma os dados em um formato adequado e os armazena em um banco de dados PostgreSQL. O projeto utiliza Python e implementa logging avançado com Logfire para monitoramento.

## Requisitos

- Python 3.8+
- PostgreSQL
- Bibliotecas Python:
  - requests
  - python-dotenv
  - sqlalchemy
  - logfire
  - logging

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/ProjectETLExtractAPI.git
cd ProjectETLExtractAPI
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Configuração

1. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=nome_do_banco
```

2. Certifique-se de que o PostgreSQL está configurado e rodando

## Estrutura do Projeto

```
ProjectETLExtractAPI/
├── src/
│   ├── pipeline_04.py
│   └── database.py
├── env/
├── .env
├── .gitignore
└── README.md
```

## Funcionalidades

- Extração de preços de criptomoedas da API Coinbase
- Transformação dos dados em formato estruturado
- Armazenamento em banco de dados PostgreSQL
- Monitoramento e logging com Logfire
- Execução contínua com intervalo de 15 segundos
- Tratamento de erros robusto

## Uso

1. Configure o arquivo `.env` com suas credenciais do PostgreSQL
2. Execute o pipeline:
```bash
python src/pipeline_04.py
```

O pipeline irá:
- Criar a tabela necessária no banco de dados
- Iniciar o monitoramento de preços
- Armazenar os dados a cada 15 segundos
- Registrar logs de todas as operações

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

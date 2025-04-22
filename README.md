# ProjectETLExtractAPI

Projeto de ETL (Extract, Transform, Load) para extração de dados da API Coinbase usando Python.

## Descrição

Este projeto implementa um pipeline ETL para extrair dados da API Coinbase, transformá-los em um formato adequado e carregá-los em um destino específico. O projeto utiliza Python e a biblioteca `requests` para realizar as requisições HTTP à API.

## Requisitos

- Python 3.8+
- Bibliotecas Python:
  - requests
  - pandas
  - python-dotenv

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

1. Crie um arquivo `.env` na raiz do projeto com suas credenciais da API Coinbase:
```
COINBASE_API_KEY=sua_chave_aqui
COINBASE_API_SECRET=seu_secreto_aqui
```

## Estrutura do Projeto

```
ProjectETLExtractAPI/
├── src/
│   ├── extract/
│   │   └── coinbase_extractor.py
│   ├── transform/
│   │   └── data_transformer.py
│   └── load/
│       └── data_loader.py
├── tests/
├── .env
├── requirements.txt
└── README.md
```

## Uso

1. Execute o pipeline ETL completo:
```bash
python src/main.py
```

2. Para executar etapas específicas:
```bash
# Apenas extração
python src/extract/coinbase_extractor.py

# Apenas transformação
python src/transform/data_transformer.py

# Apenas carregamento
python src/load/data_loader.py
```

## Funcionalidades

- Extração de dados de criptomoedas da API Coinbase
- Transformação dos dados em formato adequado para análise
- Carregamento dos dados processados em destino escolhido
- Tratamento de erros e logging
- Configuração via variáveis de ambiente

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

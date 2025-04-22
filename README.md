# ProjectETLExtractAPI

Projeto de ETL (Extract, Transform, Load) para extração de dados da API ChatGPT usando Python.

## Descrição

Este projeto implementa um pipeline ETL para extrair dados da API ChatGPT, transformá-los em um formato adequado e carregá-los em um destino específico. O projeto utiliza Python e a biblioteca `requests` para realizar as requisições HTTP à API do OpenAI.

## Requisitos

- Python 3.8+
- Bibliotecas Python:
  - requests
  - python-dotenv
  - json

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

1. Crie um arquivo `.env` na raiz do projeto com sua chave da API OpenAI:
```
OPEN_AI_API_KEY=sua_chave_aqui
```

## Estrutura do Projeto

```
ProjectETLExtractAPI/
├── exemplos/
│   └── exemplo_04.py
├── env/
├── .env
├── .gitignore
└── README.md
```

## Uso

1. Execute o exemplo de integração com a API ChatGPT:
```bash
python exemplos/exemplo_04.py
```

## Funcionalidades

- Extração de dados da API ChatGPT
- Transformação dos dados em formato adequado para análise
- Carregamento dos dados processados
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

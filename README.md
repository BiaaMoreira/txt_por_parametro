# Consulta e Exportação de Dados com Arquivo de Texto (.txt)
Este projeto consiste em um script Python para realizar consultas em um banco de dados MySQL utilizando uma lista de IDs fornecida em um arquivo de texto. O script utiliza uma abordagem modular, com funções separadas para leitura de IDs, conexão ao banco de dados, execução da consulta e exportação dos resultados para um arquivo CSV.

# Funcionalidades Principais
- **Leitura de IDs:** A função ler_ids_do_arquivo lê os IDs a serem consultados a partir de um arquivo de texto (ids.txt).
- **Conexão ao Banco de Dados:** A função conectar_bd realiza a conexão com o banco de dados MySQL, utilizando as configurações fornecidas no arquivo main.py.
- **Consulta e Exportação:** O script principal (main.py) executa uma consulta no banco de dados utilizando os IDs fornecidos e exporta os resultados para um arquivo CSV chamado resultados.csv.

# Como Usar
1. Configure as informações do banco de dados em main.py no dicionário configuracoes_bd.
1. Coloque os IDs no arquivo ids.txt, um por linha.
1. Execute o script.

Os resultados da consulta serão exportados para um arquivo CSV (resultados.csv).

# Requisitos
Python 3.x

Biblioteca mysql-connector-python.

# Estrutura do Projeto
**main.py:** Script principal para execução da consulta.

**functions.py:** Funções auxiliares para leitura de IDs, conexão ao banco de dados e exportação de resultados.

# Contribuição
Contribuições são bem-vindas! Abra problemas ou envie solicitações de recebimento.

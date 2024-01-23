from functions import *

configuracoes_bd = {
    'host': 'host',
    'usuario': 'usuario',
    'senha': 'senha',
    'banco': 'banco'
}

# Ler arquivo com os ids
arquivo_ids = 'ids.txt'
lista_ids = ler_ids_do_arquivo(arquivo_ids)

# Conectar ao banco de dados
conexao_bd = conectar_bd(**configuracoes_bd)

# Executar consulta e exportar resultados para arquivo
query = 'SELECT * FROM tabela WHERE id'
executar_consulta(conexao_bd, query, lista_ids)

conexao_bd.close()
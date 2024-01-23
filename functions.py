import mysql.connector

# Função para ler ids do arquivo
def ler_ids_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        ids = [linha.strip() for linha in arquivo]
    return ids


# Função para conectar ao banco de dados
def conectar_bd(host, usuario, senha, banco):
    conexao = mysql.connector.connect(
        host=host,
        user=usuario,
        password=senha,
        database=banco
    )
    return conexao


# Função para exportar resultados para um arquivo
def exportar_resultados_para_arquivo(resultados):
    nome_arquivo_resultados = 'resultados.csv'
    with open(nome_arquivo_resultados, 'w', encoding='utf-8') as arquivo:
        for resultado in resultados:
            resultado_formatado = []
            for coluna in resultado:
                if coluna is None:
                    coluna = 'NULL'
                else:
                    coluna = str(coluna)
                if type(coluna).__name__ == 'str':
                    coluna = f"'"+coluna+"'"
                resultado_formatado.append(coluna)
            linha = ', '.join(resultado_formatado)
            arquivo.write('(' + linha + ');' + '\n')
    print(f"Resultados exportados para {nome_arquivo_resultados}")


# Função para executar consulta e exportar resultados para arquivo
def executar_consulta(conexao, query, ids):

    cursor = conexao.cursor()
    ids_formatados = ','.join(ids)
    query = f"{query}" + f" in ({ids_formatados})"
    cursor.execute(query)
    
    resultados = cursor.fetchall()
    
    print("Resultados da consulta:", resultados)
    exportar_resultados_para_arquivo(resultados)

    cursor.close()



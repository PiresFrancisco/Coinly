import mysql.connector

def ler_dados():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="coinly"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM rendimentos")
        linhas = cursor.fetchall()

        if not linhas:
            print("Não há dados na tabela.")
        else:
            # Pega nomes das colunas para imprimir cabeçalho
            colunas = [desc[0] for desc in cursor.description]
            print(" | ".join(colunas))
            print("-" * 50)

            for linha in linhas:
                print(" | ".join(str(item) if item is not None else "" for item in linha))

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Erro ao acessar a base de dados: {err}")

if __name__ == "__main__":
    ler_dados()

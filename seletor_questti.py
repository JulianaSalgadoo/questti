import mysql.connector
import random

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'simulado',
}

disciplina1 = 'Lógica de Programação'
disciplina2 = 'Banco de Dados'
num_questoes = 9

def obter_questoes_aleatorias(disciplina1, disciplina2, num_questoes):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    query = """
        SELECT q.questao_text 
        FROM questoes q
        JOIN disciplina d ON q.disciplina_id = d.id
        WHERE d.disciplina = %s
    """
    
    # Obter questões da primeira disciplina
    cursor.execute(query, (disciplina1,))
    questoes_disciplina1 = cursor.fetchall()

    # Obter questões da segunda disciplina
    cursor.execute(query, (disciplina2,))
    questoes_disciplina2 = cursor.fetchall()

    todas_questoes = questoes_disciplina1 + questoes_disciplina2

    # Verificar se há questões suficientes para selecionar
    if num_questoes > len(todas_questoes):
        num_questoes = len(todas_questoes)
        print("Aviso: O número de questões solicitado foi ajustado para o número total de questões disponíveis.")

    questoes_selecionadas = random.sample(todas_questoes, 4)

    cursor.close()
    conn.close()

    return questoes_selecionadas

questoes = obter_questoes_aleatorias(disciplina1, disciplina2, num_questoes)
for questao in questoes:
    print(questao)
    

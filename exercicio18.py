#Esse código foi corrigido em grande parte,tive dificuldade
#18. Um sistema de controle de acesso predial registra, em uma matriz, quantas vezes cada sala foi
#acessada em cada horário do dia (linha = sala, coluna = horário):

acessos = [
[2, 5, 3, 8, 1],
[0, 1, 2, 2, 0],
[4, 6, 5, 9, 3]
]
#a) Some o total de acessos de cada sala (soma por linha) e informe qual delas foi a mais utilizada no dia.
maior_total = -1
sala_mais_usada = 0

for i in range(len(acessos)):  # Percorre os índices das linhas (salas: 0, 1, 2)
    total_sala = 0
    
    for qtd in acessos[i]:  # Percorre cada acesso dentro da sala atual
        total_sala = total_sala + qtd
        
    print(f"Total de acessos da Sala {i}: {total_sala}")
    
    # Verifica se a sala atual bateu o recorde de acessos
    if total_sala > maior_total:
        maior_total = total_sala
        sala_mais_usada = i

print(f"A sala mais utilizada no dia foi a Sala {sala_mais_usada} (com {maior_total} acessos).")

        
        
        
#b) Calcule a média de acessos por horário (média por coluna) e informe qual horário é, em média, o mais
#movimentado do prédio.

maior_media = -1.0
horario_mais_movimentado = 0

num_salas = len(acessos)          # Quantidade de linhas (3)
num_horarios = len(acessos)    # Quantidade de colunas (5)

for j in range(num_horarios):  # Fixa a coluna (horários: 0, 1, 2, 3, 4)
    soma_horario = 0
    
    for i in range(num_salas):  # Percorre todas as linhas (salas) naquela coluna
        soma_horario = soma_horario + acessos[i][j]
        
    media_horario = soma_horario / num_salas
    print(f"Média de acessos no Horário {j}: {media_horario}")
    
    # Verifica se o horário atual tem a maior média
    if media_horario > maior_media:
        maior_media = media_horario
        horario_mais_movimentado = j

print(f"O horário mais movimentado em média é o Horário {horario_mais_movimentado} (média de {maior_media} acessos).")
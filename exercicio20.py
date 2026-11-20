#20. Desafio: um painel de controle de fábrica registra o status de funcionamento de 4 máquinas ao longo
#de 10 medições feitas durante o dia ( True = funcionando, False = parada):

status_maquinas = [
[True, True, True, False, True, True, False, True, True, True],
[True, False, False, False, True, True, True, False, True, True],
[True, True, True, True, True, False, True, True, True, True],
[False, True, True, False, False, True, False, True, False, True]
]

#Para cada máquina (linha), calcule o total de medições em que ela estava parada, e informe qual máquina
#apresentou o pior desempenho no dia (mais medições paradas).
total_parada = 0
maior_paradas = -1   #correção
maquina_pior = 0   #correção
for i in range(len(status_maquinas)):  #correção
    total_parada = 0  

    for maquina in status_maquinas[i]:
            if maquina == False:
                total_parada = total_parada + 1

    print(f"A Máquina {i + 1} teve {total_parada} medições paradas.")

    if total_parada > maior_paradas:   #if corrigido
        maior_paradas = total_parada
        maquina_pior = i
            
        
print(f"A máquina com pior desempenho foi a Máquina {maquina_pior + 1}, com {maior_paradas} paradas.")

        

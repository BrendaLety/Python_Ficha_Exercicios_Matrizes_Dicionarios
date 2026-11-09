#12. Um sistema de reservas de ônibus representa o mapa de assentos como a matriz abaixo, onde True
#significa ocupado e False significa livre:

assentos = [
[True, True, False, True],
[False, False, True, True],
[True, False, False, False],
[True, True, True, False]
]

#Conte quantos assentos ainda estão disponíveis.

contador = 0
for linha in assentos:
    for assento in linha:   #precisou de mais um for
     if assento == False:
        contador = contador + 1
        
print(f"A quantidade assentos disponiveís é {contador}.")

#13. Usando a mesma matriz assentos do exercício anterior, encontre a posição (linha e coluna) do
#primeiro assento livre, para sugerir ao próximo passageiro.

encontrado = False  #Inicializar
for i in range(len(assentos)): #tem que usar o len  e separar os for e os elementos i e j(esqueci)
    for j in range(len(assentos[i])):
       if assentos[i][j] == False:
          print(f'A primeira linha com um assento disponível é {i} e sua coluna é {j}')
          encontrado = True   #e colocar essa linha
          break
    if encontrado:
       break
       
       
    
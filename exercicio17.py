#17. Uma imagem simples em escala de cinza pode ser representada como uma matriz de valores entre 0
#(preto) e 255 (branco):

imagem = [
[10, 20, 15, 5],
[200, 210, 195, 220],
[30, 25, 10, 15],
[180, 190, 205, 200]
]

#Calcule o brilho médio da imagem (média de todos os elementos) e informe se ela é predominantemente
#"escura" (média abaixo de 128) ou "clara".

brilho_total = 0
total_de_pixels = 0                                   #correção,esquecido de colocar
for valor in imagem:
    for numero in valor:
        brilho_total = brilho_total + numero   
        total_de_pixels = total_de_pixels + 1

media = brilho_total //  total_de_pixels        

print(f"O valor total de brilho é :{brilho_total}.")  #correção,esquecido de colocar fora do for
print(f"O brilho médio da imagem é :{media}.")
if media < 128:
    print("O brilho médio da imagem é predominantemente escuro.")
else:
    print("O brilho médio da imagem é predominantemente clara.")

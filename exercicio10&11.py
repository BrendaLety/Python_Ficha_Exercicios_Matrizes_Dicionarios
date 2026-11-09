#10. Um jogo da velha é representado pela seguinte matriz, onde cada célula guarda "X" , "O" ou um
#espaço vazio " " :

tabuleiro = [
["X", "X", "X"],
["O", " ", "O"],
["O", "X", " "]
]

#Exiba o tabuleiro completo, uma linha por vez.
#11. Usando o mesmo tabuleiro do exercício anterior, verifique se alguma linha está totalmente preenchida com o mesmo símbolo (um possível vencedor por linha).
for linha in tabuleiro:
    print(linha)
    
    if linha == ["X", "X", "X"] :
        print("Parabéns,voce venceu com o X!")
    elif linha == ["O", "O", "O"] :
        print("Parabéns,voce venceu com o O!")
    
#16. Uma estufa inteligente registra um pequeno conjunto de dados (dataset) de temperatura: cada linha
#é uma área da estufa, e cada coluna é uma medição feita em um horário do dia.

temperaturas = [
    [22.5, 24.0, 27.3, 25.1],
    [21.0, 23.5, 26.8, 24.0],
    [23.2, 25.5, 28.9, 26.3]
]

#a) Encontre a maior temperatura registrada, informando em qual área (linha) e em qual horário (coluna) ela ocorreu.
maiorNumero = temperaturas[0][0]
linha = 0
coluna = 0

for i in range(len(temperaturas)):
    for j in range(len(temperaturas[0])):
        if temperaturas[i][j] >= maiorNumero:
            maiorNumero = temperaturas[i][j]
            linha = i
            coluna = j

print(maiorNumero, linha, coluna)

#b) Calcule a temperatura média de cada horário (média de cada coluna, considerando as
#três áreas) — a mesma ideia usada em ciência de dados para resumir uma característica (feature) medida
#em várias amostras.

for j in range(len(temperaturas[0])):
    acumulador = 0
    for i in range(len(temperaturas)):
        acumulador = acumulador + temperaturas[i][j]
    media = acumulador // len(temperaturas[0])
    print(media)

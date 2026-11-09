#15. Um sistema de estacionamento guarda a hora de entrada de cada veículo:
entradas = {"ABC1234": 8, "XYZ9876": 10, "QWE4567": 13, "JKL8899": 9}
hora_atual = 15
#Calcule e exiba há quantas horas cada veículo está estacionado.
for placa in entradas:
    hora_entrada = entradas[placa]
    horas_estacionado = hora_atual - hora_entrada
    print(f"Veículo {placa}: está estacionado há {horas_estacionado} horas.")
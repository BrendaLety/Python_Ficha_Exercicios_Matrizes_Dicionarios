#14. Um registro de paciente guarda, entre outras informações, uma lista de alergias:

paciente = {"nome": "Carlos", 
            "idade": 40, 
            "alergias":["dipirona","poeira","amendoim"]}

#Exiba o nome do paciente seguido de todas as suas alergias, uma por linha.
print(paciente["nome"])
for alergias in paciente["alergias"]:
    print(alergias)

#Exercício 6
#Um aplicativo de contatos guarda registros como estes:
#contato1 = {"nome": "Julia", "telefone": "81999990000", "favorito": True}
#contato2 = {"nome": "Renato", "telefone": "81988887777"}
#Para cada contato, verifique se o campo "favorito" existe antes de tentar exibi-lo — repare que contato2 não possui esse campo.

contato1 = {"nome": "Julia", "telefone": "81999990000", "favorito": True}
contato2 = {"nome": "Renato", "telefone": "81988887777"}


contato1 = {"nome": "Julia", "telefone": "81999990000", "favorito": True}
contato2 = {"nome": "Renato", "telefone": "81988887777"}

if "favorito" in contato1:
    print("O campo favorito existe na lista de contato1. ")
elif "favorito" in contato2:
    print("O campo favorito existe na lista de contato2.")
else:
    print("Campo não encontrado")
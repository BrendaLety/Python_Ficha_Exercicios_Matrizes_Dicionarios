contato1 = {"nome": "Julia", "telefone": "81999990000", "favorito": True}
contato2 = {"nome": "Renato", "telefone": "81988887777"}

if "favorito" in contato1:
    print("Esse campo existe: ",contato1["favorito"])
elif "favorito" in contato2:
    print(contato2["favorito"])
else:
    print("Campo não encontrado")
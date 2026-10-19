#9. Um sistema de biblioteca guarda o registro de um livro:
#livro = {"titulo": "Duna", "autor": "Frank Herbert", "ano": 1965, "emprestado": False}
#Ao emprestar o livro, altere o campo "emprestado" para True ; ao ser devolvido, altere de volta para False.
livro = {"titulo": "Duna", 
        "autor": "Frank Herbert", 
        "ano": 1965,
        "emprestado": False
        }

while True:
    escolha: str = str(input("Informe sobre o status do livro,digitando 'Emprestado' ou 'Devolvido'."))

    if escolha == "Emprestado":
        livro["emprestado"] = True
        break
    elif escolha == "Devolvido":
        livro["emprestado"] = False
        break

print("Os dados atualizados do livro são:",livro)

    

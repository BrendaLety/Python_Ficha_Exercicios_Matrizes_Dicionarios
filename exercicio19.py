#19. Um sistema de cadastro guarda o perfil de um usuário, incluindo um dicionário dentro do dicionário:

usuario = {
"nome": "Bianca",
"preferencias": {"tema": "escuro", "idioma": "pt-BR"}
}

#Exiba o idioma preferido do usuário e, em seguida, altere o campo "tema" para "claro" .
print(f"Idioma favorito de usuário: {usuario["preferencias"]["idioma"]}")
usuario["preferencias"]["tema"] = "claro"        

print(f"E seu tema favorito é {usuario["preferencias"]["tema"]}")        #leve erro no print,troquei () por []
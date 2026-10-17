#7. Um sistema de monitoramento de rede guarda o status de servidores:

#servidores = {
#"servidor1": "online",
#"servidor2": "offline",
#"servidor3": "online",
#"servidor4": "offline",
#"servidor5": "online"
#}

#Conte quantos servidores estão "offline" .
servidores = {
"servidor1": "online",
"servidor2": "offline",
"servidor3": "online",
"servidor4": "offline",
"servidor5": "online"
}
contador = 0
for servidor in servidores:
    if servidores[servidor] == "offline" :
        contador += 1

print("A quantidade de servidores offline foram:",contador)


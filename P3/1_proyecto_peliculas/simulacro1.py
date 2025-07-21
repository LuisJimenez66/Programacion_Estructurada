lista=[]

if len(lista)==0:
    resp=True
    while resp:
        frase=input("Dame una palabra o frase: ")
        lista.append(frase)
        resp=input("Desea ingresar otra frase? (SI/NO)").lower().strip()
        if resp=="no":
            resp=False
    print(lista)            







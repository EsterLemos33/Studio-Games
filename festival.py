print("Bem vindo ao Festival!")
idade = int(input("Qual sua idade?"))
if idade < 12:
    print("Voce nao pode entrar, a idade minima e 12 anos.")
elif 12 <= idade < 18:
    tem_autorizacao = input("Voce tem autorizacao dos seus pais?")
    if tem_autorizacao == "sim":
        tem_ingresso = input("Voce tem ingresso?")
        if tem_ingresso == "sim":
            print("Pode entrar,voce possui ingresso e autorizacao.")
        else:
            vip = input("Voce esta na lista vip?")
            if vip == "sim":
                print("Pode entrar, voce e vip e tem autorizacao.")
            else:
                print("Nao pode entrar, voce nao possui ingresso e nao esta na lista VIP!")          
    else:
        print("Voce nao pode entrar, menores de idade precisam da autorizacao dos pais.")
else:
    tem_ingresso = input("Voce tem ingresso?")
    if tem_ingresso == "sim":
        print("Pode entrar,voce possui ingresso.")
    else:
        vip = input("Voce esta na lista vip?")
        if vip == "sim":
            print("Pode entrar, voce e VIP!.")
        else:
            print("Nao pode entrar, voce nao possui ingresso e nao esta na lista VIP!")

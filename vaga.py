idade = int(input("Qual sua idade? "))
antecedentes = input("Voce possui antecedentes criminais?  (s/n): ")
experiencia = input("Voce tem experiencia na area?  (s/n): ")
superior = input("Voce tem ensino superior completo?  (s/n): ")
indicacao = input("Alguem o indicou para esta vaga?  (s/n): ")

if idade < 18:
    print("Voce nao tem idade suficiente para trabalhar conosco.")
elif not antecedentes == "s" and (experiencia == "s" or superior == "s" or indicacao == "s"):
    print("Vamos marcar uma entrevista.")
else:
    print("Infelizmente voce nao possui o perfil que estamos procurando.")

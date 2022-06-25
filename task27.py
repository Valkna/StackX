idade = int(input("Digite a idade do eleitor: "))

if idade >= 18 and idade <= 65:
    print("Voto obrigatório.")
if idade >= 16 and idade <18 or idade > 65:
    print("Voto facultativo.")
if idade < 16:
    print("Você não pode votar.")

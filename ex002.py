# algoritmo relação peso/idade

Idade = float(input('Insira sua idade: '))
Peso = float(input('Insira seu peso: '))

if Idade < 20 and Peso <= 60:
    print('Risco 9')
elif Idade < 20 and Peso > 60 and Peso <= 90:
    print('Risco 8')
elif Idade < 20 and Peso > 90:
    print('Risco 7')
elif Idade >= 20 and Idade <= 50 and Peso < 60:
    print('Risco 6')
elif Idade >= 20 and Idade <= 50 and Peso >= 60 and Peso <= 90:
    print('Risco 5')
elif Idade >= 20 and Idade <= 50 and Peso > 90:
    print('Risco 4')
elif Idade > 50 and Peso <= 60:
    print('Risco 3')
elif Idade > 50 and Peso >= 60 and Peso <= 90:
    print('Risco 2')
else:
    print('Risco 1')

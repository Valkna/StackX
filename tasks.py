# calcular peso ideal

altura = float(input('Informe sua altura: '))
sexo = bool(input('Informe seu sexo: [1] feminino ou [2] masculino: '))
if sexo == 1:
    print('Seu peso ideal é', (62.1 * altura - 44.7))
else:
    print('Seu peso ideal é', (72.7 * altura - 58))
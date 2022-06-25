# algoritmo gratificação salarial

SalarioBruto = float(input('Digite o valor do seu salário: R$ '))

if SalarioBruto <= 350:
    print('Sua gratificação é de R$ 100. Seus proventos líquidos são R$ ', SalarioBruto - SalarioBruto * 0.07 + 100)
elif SalarioBruto > 350 and SalarioBruto <= 600:
    print('Sua gratificação é de R$ 75. Seus proventos líquidos são R$ ', SalarioBruto - SalarioBruto * 0.07 + 100)
elif SalarioBruto > 600 and SalarioBruto <= 900:
    print('Sua gratificação é de R$ 50. Seus proventos líquidos são R$ ', SalarioBruto - SalarioBruto * 0.07 + 100)
elif SalarioBruto > 900:
    print('Sua gratificação é de R$ 35. Seus proventos líquidos são R$ ', SalarioBruto - SalarioBruto * 0.07 + 100)
# algoritmo gratificação de natal
# H = número de horas extras – (2/3 * ( número de horas falta )

HorasExtras = float(input('Digite o número de horas trabalhadas: '))
HorasFaltas = float(input('Digite o número de horas faltantes: '))
HorasTotais = float(HorasExtras - (2/3 * HorasFaltas))

if HorasTotais > 2040:
    print('Você vai receber R$ 500 de gratificação.')
elif HorasTotais >= 1801 and HorasTotais <= 2040:
    print('Você vai receber R$ 400 de gratificação.')
elif HorasTotais > HorasTotais >= 1200 and HorasTotais <= 1800:
    print('Você vai receber R$ 300 de gratificação.')
elif HorasTotais >= 600 and HorasTotais <= 600:
    print('Você vai receber R$ 200 de gratificação.')
else:
    print('Você vai receber R$ 100 de gratificação.')
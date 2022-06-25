# algoritmo categorias de natação

Idade = int(input('Digite a idade do nadador: '))
if Idade < 5:
    print('Não existe categoria para essa faixa etária.')
elif Idade == 5 and Idade <= 7:
    print('Categoria infantil.')
elif Idade > 7 and Idade <= 12:
    print('Categoria Juvenil.')
elif Idade > 12 and Idade <= 15:
    print('Categoria Adolescente.')
elif Idade > 15 and Idade <= 30:
    print('Categoria Adulto.')
elif Idade > 30 and Idade < 120:
    print('Categoria Sênior.')
else:
    print('Você está nadando no Paraíso! Amén!')

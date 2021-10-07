print('========== D E T R A N ==========')
print(' ')
velocidade = float(input('Qual era a velocidade que o carro passou pelo radar? '))
if velocidade <= 80:
    print('Velocidade dentro do permitido. Continue dirigindo com segurança.')
else:
    multa = (velocidade-80)*7
    print('Infração grave! Sua multa será de R${:.2f}!'.format(multa))
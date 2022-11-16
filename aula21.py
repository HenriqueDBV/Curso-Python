numero = int(input('Informe um numero inteiro: '))
try:
    if numero % 2 == 0:
        print('Este numero é PAR')
    else:
        print('Este numero é IMPAR')
except:
    print('Por favor digite um numero inteiro')


hora = int(input('Informe que horas são: '))


if hora <= 11:
    print('Bom dia')
elif hora <= 17:
    print('Boa Tarde')
else:
    print('Boa Noite')



nome = input('Informe seu primeiro nome: ')
cont = len(nome)

if cont <= 4:
    print('Seu nome é curto')
elif cont <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande')
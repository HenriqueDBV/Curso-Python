numero = input('vou dobrar o numero que voce digitar: ')

try:
    print (f'O dobro do {numero} é {float(numero) * 2:.1f}')
except:
    print('Isso não é um numero')
# primeiro_valor = int(input('Informe um valor: '))
# segundo_valor = int(input('Informe um valor: '))

primeiro_valor = input('Informe um valor: ')
segundo_valor = input('Informe um valor: ')


if primeiro_valor > segundo_valor:
    print(f'O primeiro valor é de {primeiro_valor} e é maior que o segundo valor {segundo_valor}')
elif segundo_valor > primeiro_valor:
    print(f'O segundo valor é de {segundo_valor} e é maior que o primeiro valor {primeiro_valor}')
elif primeiro_valor == segundo_valor:
    print(f'Os dois valores são iguais {primeiro_valor}')
else:
    print('Valor informando não é valido! Por favor, informe um valor valido.')
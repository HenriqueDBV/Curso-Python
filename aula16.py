entrada = input ('[E]ntrar [S]air: ')
senha = input('Senha: ')

senha_certa = '122259'

if entrada == 'E' and senha == senha_certa:
    print('Entrar')
else:
    print('Sair')

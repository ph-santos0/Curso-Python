senha_correta = '1234'
senha_digitada = ''
while senha_digitada != senha_correta:
    senha_digitada = input('Digite a senha: ')
    if senha_digitada != senha_correta:
        print('Senha incorreta. Tente novamente.')
print('Acesso permitido')

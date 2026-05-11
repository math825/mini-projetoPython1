saldo = 0
nome = ''
gastos = 0
ganhos = 0
gastost = 0
while True:
    print('========SISTEMA FINANCEIRO========')
    print('1 - Registrar seu nome.')
    print('2 - Adicionar seus ganhos.')
    print('3 - Adicionar seus gastos.')
    print('4 - Ver saldo.')
    print('5 - Sair.')
    print('{}'.format('='*34))
    opcao = input('Escolha uma opção: ').strip()
    if opcao == '1':
        nome = input('Digite seu nome completo: ').strip().upper()
        print('Olá. {}! Seja bem vindo ao sistema financeiro.'.format(nome))
    elif opcao == '2':
        while True:
            ganhos = float(input('Digite seus ganhos do mês: R$:'))
            print('Seus ganhos do mês são de R$ {:.2f}?'.format(ganhos))
            certeza = input('certeza? [S/N]: ').strip().upper()
            if certeza == 'S':
                print('Ganhos registrados com sucesso!')
                break
            else:
                print('Ganhos não registrados! tente novamente.')
    elif opcao == '3':
        while True:
            gastos = float(input('Digite uma despesa do mês (Digite 0 para finalizar!) R$:'))
            if gastos == 0:
                print('Gastos registrados com sucesso!')
                print('Sua despesa do mês total é de R$ {:.2f}'.format(gastost))
                break
            gastost += gastos
    elif opcao == '4':
        saldo = ganhos - gastost
        print('usuário: {}'.format(nome))
        print('Seus ganhos é de R$ {:.2f}'.format(ganhos))
        print('Seus gastos no total é de R$ {:.2f}'.format(gastost))
        print('Seu saldo do mês é de R$ {:.2f}'.format(saldo))
    elif opcao == '5':
        print('Obrigado por usar o sistema financeiro. Volte sempre!')
        break    
            

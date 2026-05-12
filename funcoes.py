def mostrar_menu():
    print('{}SISTEMA FINANCEIRO{}'.format('='*17, '='*17))
    print('1 - Registrar seu nome.')
    print('2 - Adicionar seus ganhos.')
    print('3 - Adicionar seus gastos.')
    print('4 - Ver saldo.')
    print('5 - Sair.')
    print('{}'.format('='*52))
    
    
def registrar_nome():
    nome = input('Digite seu nome completo: ').strip().upper()
    print('Olá. {}! Seja bem vindo ao sistema financeiro.'.format(nome))
    return nome
    
    
def adicionar_ganhos():
    while True:
        ganhos = float(input('Digite seus ganhos do mês: R$:'))
        print('Seus ganhos do mês são de R$ {:.2f}?'.format(ganhos))
        certeza = input('certeza? [S/N]: ').strip().upper()
        if certeza == 'S':
            print('Ganhos registrados com sucesso!')
            return ganhos
        else:
            print('Ganhos não registrados! tente novamente.')


def adicionar_gastos():
    gastost = 0
    while True:
        gastos = float(input('Digite uma despesa do mês (Digite 0 para finalizar!) R$:'))
        if gastos == 0:
            print('Gastos registrados com sucesso!')
            print('Sua despesa do mês total é de R$ {:.2f}'.format(gastost))
            return gastost
        gastost += gastos


def ver_saldo(nome, ganhos, gastost):
    saldo = ganhos - gastost
    print('usuário: {}'.format(nome))
    print('Seus ganhos é de R$ {:.2f}'.format(ganhos))
    print('Seus gastos no total é de R$ {:.2f}'.format(gastost))
    print('Seu saldo do mês é de R$ {:.2f}'.format(saldo))
            
            
def sair():
    print('Obrigado por usar o sistema financeiro. Volte sempre!')    
from funcoes import *

saldo = 0
nome = ''
gastos = 0
ganhos = 0
gastos_totais = 0
    
while True:

    mostrar_menu()
    opcao = input('Digite a opção desejada: ').strip()
    
    if opcao == '1':
        nome = registrar_nome()
        
    elif opcao == '2':
        ganhos = adicionar_ganhos()
        
    elif opcao == '3':
        gastos_totais = adicionar_gastos()
        
    elif opcao == '4':
        ver_saldo(nome, ganhos, gastos_totais)
        
    elif opcao == '5':
        sair()
        break
        
    else:
        print('Opção inválida! Tente novamente.')
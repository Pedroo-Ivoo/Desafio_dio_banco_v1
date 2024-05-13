menu  = '''
    ===== Menu =====
    
    Escolha uma das opções
    [1] - Deposito
    [2] - Saque
    [3] - Extrato
    [4] - Sair
    
Digite a opção desejada: '''

saldo = 0
limite = 500
extrato = []
numero_de_saque = 0
LIMITE_SAQUE = 3



while True:
    '''O while no valor true faz com que o bloco de código fique executando até a saída pelo break.'''
    try: #Encapusula um bloco de código que pode apresentar erro em função do input do usuário
        opcao = int(input(menu))
        if opcao not in range(1,5): #Restringe o número de opções para que o programa aceite apenas do 1 ao 4.
            raise ValueError
    
    except(ValueError):
        print("Operação invalida, por favor selecione novamente a operação desejada.")
        continue
    if opcao == 1:
        print('***Deposito***')
        valor = float(input("Informe o valor para ser depositado: "))
        if valor < 0:
            print("Operação Inválida! Informe corretamente o valor a ser depositado.")  
        else:
            saldo += valor
            extrato.append(f'Deposito - R$ {valor:.2f}')
            print(f"O valor R$ {valor:.2f} foi depositado com sucesso! ")
            
    elif opcao==2:
        if LIMITE_SAQUE > numero_de_saque:
            print("***Saque***")
            saque = float(input('Informe o valor que queira sacar:'))
            if (saque > limite):
                print('Não foi possivel realizar o saque! Valor superior ao limite do saque para esta conta.')
            elif (saque > saldo):
                print('Não foi possivel realizar o saque! Saldo insuficiente.')
            elif (saque < 0 ):
                print("Operação inválida! Valor inválido!")
            else:
                numero_de_saque += 1
                saldo -= saque
                extrato.append(f'Saque - R$ {saque:.2f}')
                print(f"Saque no valor de R$ {saque:.2f}")
                
                
        else:
            print('Limite diário de saque atingido. Novos saque só serão possíveis no próximo dia.')
        
    elif opcao == 3:
        if len(extrato) == 0:
            print("Não foram realizadas movimentações")
        else:
            print("\n*******Extrato********\n")
            for i, extrato in enumerate (extrato):
                print(extrato)
            print(f'Saldo - R$ {saldo:.2f}\n') 
    else:
        print(" Obrigado por usar o nosso banco!\n Tenha um bom dia!")   
        break       
    
        




def menu():
    print('''
        ===== Menu =====
    
    Escolha uma das opções
    [1] - Deposito
    [2] - Saque
    [3] - Extrato
    [4] - Cadastrar Cliente
    [5] - Criar Conta
    [6] - Sair
    
    ''')
   
    
def deposito(saldo, valor, extrato, /):
    
    if valor>0:
        saldo += valor
        extrato.append(f'Deposito - R$ {valor:.2f}')
        print(f'O Valor de R${valor:.2f} foi depositado com sucesso!')
        return saldo
    else:
        print("Operação Inválida! Informe corretamente o valor a ser depositado.")  
    

def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUE):
    
    limite_diario = LIMITE_SAQUE <= numero_saques
    limite_saque= valor > limite
    saldo_insuficiente = valor > saldo
    
    if limite_diario:
        print('Limite diário de saque atingido. Novos saque só serão possíveis no próximo dia.')
    elif limite_saque:
        print('Não foi possivel realizar o saque! Valor superior ao limite do saque para esta conta.')
    elif saldo_insuficiente:
        print('Não foi possivel realizar o saque! Saldo insuficiente.')
    elif valor<0:
        print("Operação inválida! Valor inválido!")
    else:
        print("Saque".center(16, "#"))
        saldo -= valor
        numero_saques =+ 1
        print(f'Número de saques realizados: {numero_saques}')
        extrato.append(f'Saque - R$ {valor:.2f}')
        print(f"Saque no valor de R$ {valor:.2f}")
    return saldo, numero_saques          
  
    
def exibir_extrato(saldo, /, *, extrato):
    if len(extrato) == 0:
            print("Não foram realizadas movimentações")
    else:
        print("\n*******Extrato********\n")
        for i, extrato in enumerate (extrato):
            print(extrato)
        print(f'Saldo - R$ {saldo:.2f}\n') 
        
def criar_cliente(lista_cliente):
    
    cpf=int(input("Informe apenas o número do CPF: "))
    cliente_existe = [cliente for cliente in lista_cliente if cliente['CPF'] == cpf]
    
    if cliente_existe:
        print("O CPF já está vinculado a um cliente")
    else:
        nome = input("Digite o Nome completo: ")
        data = input("Digite a data de Nascimento: ")
        endereco = input('Digite o endereço. (Logradouro: , Bairro: , Cidade: , UF:)')
        
        print(f'o {cpf} será cadastrado')
        lista_cliente.append({'Nome':nome, 'Data de Nascimento': data,'CPF': cpf, 'Endereço': endereco})
        print(lista_cliente)
        
def criar_conta(conta,lista_cliente):
    
    cpf=int(input("Informe apenas o número do CPF: "))
    cliente_existe = [cliente for cliente in lista_cliente if cliente['CPF'] == cpf]
    if cliente_existe:
        nova_conta = len(conta) +1
        conta.append(nova_conta)
        print(f'Conta criada com sucesso!')
    else:    
        print("Cliente não cadastrado!")
        
 

def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    
    saldo=1500
    limite=500
    numero_saques = 0
    extrato = []
    lista_cliente= []
    conta = []
    while True:
    
        menu()
        try:
            opcao = int(input('Digite: '))
            if opcao not in range(1, 7): #verifica se o valor digitado está de acordo com as opções
                 raise ValueError
            
            match opcao:
                case 1:
                    valor = float(input("Informe o valor para ser depositado: "))
                    saldo =  deposito(saldo, valor, extrato)
                
                case 2:
                    valor = float(input('Informe o valor que queira sacar:'))
                    saldo, numero_saques = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUE=LIMITE_SAQUE)
                case 3:
                    exibir_extrato(saldo, extrato=extrato)
                case 4:
                    criar_cliente(lista_cliente)
                case 5:
                    criar_conta(conta,lista_cliente)
                case 6:
                    break
                
        except (ValueError) : #caso o valor digitado não seja um número valido ele caira no except
            print('Opção inválida!\n')
            
main()   
   
    
import textwrap
from datetime import datetime


def menu(hoje,saldo):
      menu = str(f''' ___________________________________
            |        SISTEMA BANCARIO          |
            |▒▒▒▒▒▒▒▒  <<DIO BANK>>  ▒▒▒▒▒▒▒▒▒▒|                
            
            Data: {hoje:'%d/%m/%Y'}
            Saldo: R$ {saldo:.2f}

            Selecione uma Opção:
                Menu
                    ♦\t[d]\tDepositar
                    ♦\t[s]\tSacar
                    ♦\t[e]\tExtrato
                    ♦\t[nc]\tNova conta
                    ♦\t[lc]\tListar contas
                    ♦\t[nu]\tNovo usuário
                    ♦\t[q]\tSair

            '''
                )
      return input(textwrap.dedent(menu))
def depositar(saldo,valor,extrato,hoje):
        saldo += valor
        extrato.append(f"{hoje:%d/%m/%Y} {hoje:%H:%M} - Deposito realizado no valor de R$ {valor:.2f} - Saldo do dia: R$ {saldo:.2f}")
        print("\n\n")
        print("#####==>Deposito realizado com sucesso!<=#####")
     
        return saldo,extrato
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques,hoje):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\nOperação não autorizada! Você não tem saldo suficiente.")
    elif excedeu_limite:
         print("\nOperação não autorizada! Limite de saque atingido.")
    elif excedeu_saques:
         print("\nOperação não autorizada! Quantidade de saques diarios atingidos")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"{hoje:%d/%m/%Y} {hoje:%H:%M} - Saque realizado no valor de R$ {valor:.2f} - Saldo do dia: R$ {saldo:.2f}")
        numero_saques += 1
        
        print("\n\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! Tente novamente")

    return saldo, extrato,numero_saques
def exibir_extrato(saldo, hoje, /, *, extrato):

    print(f"""===============Extrato=================\n Saldo disponivel: R$ {saldo:.2f} em {hoje:%d/%m/%Y}
           """)
    for itens in extrato:
          print(itens)       
def criar_usuario(usuarios):
    cpf = input("Digite o cpf do usuario\n\n")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
         print("Usuario já cadastrado\n!")
         return
    else:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

        print("###### Cadastro realizado com sucesso! ######")
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o usurio para criação da conta:\n")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
         print("\n\n#####Conta criada com sucesso!#####\n")
         return {'agencia': agencia, 'conta' : numero_conta,'usuario': usuario}
         
    else:
         print("Usuario não cadastrado, fluxo de criação de conta encerrado!\n")
def listar_contas(contas):
    for conta in contas:
         for conta in contas:
            linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['conta']}
                Titular:\t{conta['usuario']['nome']}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))
                  




     
     

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None     
     

                   
     
          

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = list()
    numero_saques = 1
    usuarios = []
    contas = []
    hoje = datetime.now()
    
    while True:
            opcao = menu(hoje,saldo)
            match opcao:
                case 'd':
                    valor = input("Informe o valor do Deposito:\n")
                    if valor.isdigit():
                        saldo , extrato = depositar(saldo, float(valor),extrato,hoje)                          
                    else:
                        print("Digite um valor valido!")
                         
                case 's':
                    valor = input("Informe o Valor do Saque:\n")
                    
                    if valor.isdigit():
                        saldo, extrato, numero_saques  = sacar(
                        saldo=saldo,
                        valor=float(valor),
                        extrato=extrato,
                        limite=limite,
                        numero_saques=numero_saques,
                        limite_saques=LIMITE_SAQUES,
                        hoje = hoje
                        )
                    else:
                        print("Digite um valor valido!")
                             


                case 'e':                    
                    exibir_extrato(saldo,hoje,extrato=extrato)
                case 'nu':
                    criar_usuario(usuarios)
                case 'nc':
                    numero_conta = len(contas) + 1
                    conta = criar_conta(AGENCIA, numero_conta, usuarios)

                    if conta:
                        contas.append(conta)
                    

                case 'lc':
                   
                    listar_contas(contas)
                    
                case 'q':
                    print("Obrigado por confiar em nossos Serviços, volte sempre!\n\n")
                    break
                case _:
                    print("Selecione um opção valida!") 

main()
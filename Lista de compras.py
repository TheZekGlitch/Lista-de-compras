print("               Bem-vindo ao programa: Lista de compras. ")
print("=-=-="*14)
## Lista principal
listaP = []
qtd_de_items = len(listaP)
# Contadores
i = 0
i2 = 0
i3 = 0

print("\tVocê precisa modificar algo em sua lista?")
resposta = input("\t[Sim] ou [Não]: ").upper().startswith('S')

print(''*15)

if resposta is True:

    while i == 0:
        while i2 == 0:
            print("=-=-="*7)
            print("Opções:\n 1 - Adicionar algum item"
                '\n 2 - Deletar algum item', '\n 3 - Ver os items atuais da lista',
                '\n 4 - Sair do programa')
            print("=-=-="*7)

            comando = input("Comando: ")
            print("=-=-=-=-=")

            if (comando.isdigit()):
                #situação de adicionar o item/valor[1]
                if comando == '1':

                    print(''*15)
                    print("=-=-="*7)
                    listaP.append(input("Digite o nome/valor do item: "))
                    print(''*15) 
                    #contador pra acrescentar a qtd de indices (por preguiça de usar o for)
                    i3 += 1
                    print('-- Seu item foi adicionado com sucesso! --')
                    print(''*15)
                    print("Opções: \n1 - Voltar as opções \n2 - Sair do programa")

                    qtd_de_items = len(listaP)
                    #comando pra sair do "adicionar" (comando2) só serve pra isso msm
                    comando2 = input("Comando: ")
                    if comando2 == '1':
                        i2 = 0
                    elif comando2 == '2':
                        i2 += 1
                        i += 1

                #Situação de ver os items da lista e seus indices:
                if (comando == '3'):
                    print(''*15)
                    for item in enumerate(listaP):
                        a, b = item
                        print(a, b)
                        
                    print("=-=-="*7)
                    print(''*15)
                    print("Opções: \n1 - Voltar as opções \n2 - Sair do programa")

                    comando2 = input("Comando: ")
                    if comando2 == '1':
                        i2 = 0
                    elif comando2 == '2':
                        i2 += 1
                        i += 1
                #Situação de deletar o item/valor[2]
                if (comando == '2' and qtd_de_items > 0):
                    
                    print(''*15)

                    print("Qual item você quer retirar da lista: ")
                    for item in enumerate(listaP):
                        a, b = item
                        print(a, b)
                    respostadeindice = int(input("Digite o indice referente: "))
                    if (respostadeindice < qtd_de_items):
                        del listaP[respostadeindice]
                    
                        print("=-=-="*7)
                        print(''*15)
                        print("Opções: \n1 - Voltar as opções \n2 - Sair do programa")

                        comando2 = input("Comando: ")
                        if comando2 == '1':
                            i2 = 0
                        elif comando2 == '2':
                            i2 += 1
                            i += 1
                    else:
                        print(''*15)
                        print("-- Você digitou um indice inexistente! Tente novamente! --")
                        print(''*15)
                        
                if comando == '4':
                    i2 += 1
                    i += 1
            else:
                print("Digite algo válido!")
                i2 = 0
    print("Você saiu do programa!")
else:
    print("Tudo certo, até a próxima!")
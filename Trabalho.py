# Variáveis que armazenam os preços de veículos conforme a Tabela Fipe
tabelaFipe = {"Accord": 7000,"City": 3500, "Civic": 12000,
              "440": 25000, "460": 40000," 850": 35600,
              "Cruze ": 15000,"Equinox":25000, " Trailblazer":3600,
              "HB20": 75000, "Creta": 35000, " Azera": 23000 ,
              "Corolla Hybrid. Explorar.": 47000, "Corolla Cross Hybrid": 50000,"RAV4 Plug-in Hybrid": 85000
            }
# Dicionário com as marcas de carros e os modelos disponíveis para cada uma
veiculo_disponivel = {"Honda":['Accord','City','Civic'],
                        "Volvo": [ "Volvo 440","Volvo 460","Volvo 850"],
                        "Chevrolet": ["Chevrolet Cruze ","Chevrolet Equinox","Chevrolet Trailblazer"],
                        "Hyundai":[ "Hyundai HB20","Hyundai Creta","Hyundai Azera"],
                        "Toyota":["Toyota Corolla Hybrid. Explorar.","Toyota Corolla Cross Hybrid","Toyota RAV4 Plug-in Hybrid"]
              }
# Dicionário com as mesmas marcas, mas com veículos disponíveis para aluguel
veiculosParaAluguel = {"Honda":['Accord','City','Civic'],
                        "Volvo": [ "Volvo 440","Volvo 460","Volvo 850"],
                        "Chevrolet": ["Chevrolet Cruze ","Chevrolet Equinox","Chevrolet Trailblazer"],
                        "Hyundai":[ "Hyundai HB20","Hyundai Creta","Hyundai Azera"],
                        "Toyota":["Toyota Corolla Hybrid. Explorar.","Toyota Corolla Cross Hybrid","Toyota RAV4 Plug-in Hybrid"]
              }

# Cadastro de cliente - coleta informações como nome, telefone e saldo disponível
nome = input("Nome: ") # Solicita o nome do cliente
contato = float(input("Telefone para contato: ")) # Solicita o contato do cliente
saldo_disponivel = float(input("Saldo disponível: ")) # Coleta o saldo disponível do cliente
saldo_total = 0 # Inicializa o saldo total do cliente após as transações


# Menu de opções que controla o fluxo de venda, aluguel, compra ou encerramento do programa

while True:
  menu = int(input("MENU \n 1 - Venda \n 2 - Aluguel \n 3 - Compra \n 4 - Sair \n" ))
  # Função de venda de veículos

  if menu == 1: # Opção de Venda
    print("Veiculos disponíveis")
    
    for exibir in veiculo_disponivel:
        print(exibir)
  # Solicita a escolha da marca que o cliente deseja vender
    exibir = input("Escolha a marca que deseja vender: \n ")

    for modelo in veiculo_disponivel:
        print(veiculo_disponivel[exibir])
        modelo = input("Digite o modelo do veiculo: \n ")

    # Exibe informações sobre o modelo escolhido e a proposta de venda (após a comissão de 12%)

        print(f"Modelo escolhido: {modelo}")
        print(f"O valor do modelo é: {tabelaFipe[modelo]}")
        print(f"A proposta é: {tabelaFipe[modelo]*0.88}")

        confirmaVenda = input("Confirmar venda? S/N \n") # Solicita confirmação para a venda
        
        if confirmaVenda == "S":  # Se o cliente confirmar a venda
            saldo_total = saldo_disponivel + (tabelaFipe[modelo]*0.88) 
            print(f"Seu novo saldo é: {saldo_total}") # Atualiza o saldo total do cliente após a venda
            print("Venda Realizada com sucesso")  # Informa que a venda foi concluída com sucesso
            break
        else:
            print("Venda não realizada, Encerrando o programa") 
            break

# Função aluguel dos Veiculos
  if menu == 2:
    print ("--Aluguel de veiculos:--")
    for exibir in veiculosParaAluguel: # Exibe as marcas de veículos disponíveis para aluguel
         print(exibir)

    exibir = input("Escolha a marca: \n")  # Solicita a escolha da marca de veículo

    for modelo in veiculosParaAluguel: # Exibe os modelos disponíveis para a marca escolhida e solicita o modelo do cliente
            print(veiculosParaAluguel[exibir])
            modelo = input("Escolha o modelo: \n")
            break

    if modelo in veiculosParaAluguel[exibir]:  # Verifica se o modelo escolhido está disponível
            
        diaria = int (input("Quantos dias serão de aluguel?")) # Solicita a quantidade de dias para o aluguel
        print (f"A proposta de aluguél é de {77*diaria}") # Solicita a quantidade de dias para o aluguel
        confLocacao = (input("Deseja concluir a locação? [S/N]")) # Solicita confirmação para concluir a locação
        if confLocacao == 'S' and saldo_disponivel >= (77*diaria): # Se o saldo for suficiente para o aluguel
           saldo_total = saldo_disponivel - (77*diaria) # Atualiza o saldo do cliente após o aluguel
           print (f"Novo saldo é: {saldo_total}")
           print ("Locação concluida! ")  # Confirma que a locação foi concluída
           veiculosParaAluguel[exibir].remove(modelo) # Remove o modelo alugado da lista de disponibilidade
             
        elif confLocacao == 'S' and saldo_disponivel - (77*diaria): # Remove o modelo alugado da lista de disponibilidade
             print ("Saldo insuficiente! ")
             
        else:
            print ("Compra Cancelada! ") # Se o cliente cancelar o aluguel
    else:
           print("Veiculo indisponível! Escolha outro.") # Caso o modelo não esteja disponível
           continue # Retorna ao menu para nova escolha


# Função compra de veiculo
  if menu == 3:  # Se o cliente escolher a opção de "Compra"
    print("Veiculos disponíveis para venda")

    for exibir in veiculo_disponivel:  # Exibe as marcas de veículos disponíveis para compra
        print(exibir)

    exibir = input("Escolha a marca que deseja Compra: \n ")  # Solicita a escolha da marca de veículo para compra
    
    print(veiculo_disponivel[exibir]) # Exibe os modelos disponíveis da marca escolhida
    modelo = input("Digite o modelo do veiculo: \n ")

    if modelo in veiculo_disponivel[exibir]:# Exibe os modelos disponíveis da marca escolhida
        

      print(f"Modelo escolhido: {modelo}")  
      print(f"O valor do modelo é: {tabelaFipe[modelo]*1.25}") # O valor da compra é acrescido de 25% (taxa)

      confirmaCompra = input("Deseja Concluir a compra? S/N \n") # Solicita confirmação para concluir a compra
        
      if confirmaCompra == "S" and saldo_disponivel >= (tabelaFipe[modelo]*1.25): # Verifica se o cliente tem saldo suficiente
          saldo_total = saldo_disponivel - (tabelaFipe[modelo]*1.25) # Atualiza o saldo após a compra
          print (f"Novo saldo é:{saldo_total}")
          print("Compra Concluída") # Confirma que a compra foi realizada
          veiculo_disponivel[exibir].remove(modelo) # Remove o veículo comprado da lista de disponíveis
          
      elif confirmaCompra == "S" and saldo_disponivel < (tabelaFipe[modelo]*1.25): # Se o saldo for insuficiente
           print("Saldo Insuficiente")
          
        
      else:
          print("Compra Cancelada") # Se o cliente cancelar a compra
          
    else:
        print("Veiculo indisponível, escolhe outro") # Caso o modelo não esteja disponível


#Função Para encerrar o programa
  if menu == 4: # Se o cliente escolher a opção "Sair"
       print("Programa encerrado") # Informa que o programa foi encerrado
       break # Sai do loop e encerra o programa





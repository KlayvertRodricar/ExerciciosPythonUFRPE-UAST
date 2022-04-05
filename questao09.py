#O cardápio de uma casa de hamburger é dado abaixo. Preparar um algoritmo para ler a quantidade de cada item comprado e calcular a conta ao final. Código Descrição Valor
#1 Hamburger R$ 2,50)
#2 Cheeseburger R$ 3,30
#3 Batata R$1,50
#4 Frita R$ 0,60
#5 Refrigerante
#Incluir na conta final os 10% dos serviços.
lista = []
count_h = 0
count_cb = 0
count_frita = 0
count_refri = 0
x = 1
while x == 1:
    print("1)Hambúrguer: 2.50R$\n2)Cheeseburguer: 3.30R$\n3)Batata frita: 1.50R$\n4)Refrigerante: 0.60R$\n5)Sair")
    var_decisao = int(input(""))
    if var_decisao == 1:
        print("Quantos Hamburgueres você deseja? ")
        qnt_produto = int(input(""))
        for num in range(qnt_produto):
            count_h += 1
        lista.append("{} hambúrgueres".format(count_h))

    elif var_decisao == 2:
        print("Quantos Cheeseburgueres você deseja? ")
        qnt_produto = int(input(""))
        for num in range(qnt_produto):
            count_cb += 1
        lista.append("{} Cheeseburgueres".format(count_cb))

    elif var_decisao == 3:
        print("Quantas batatas fritas você deseja? ")
        qnt_produto = int(input(""))
        for num in range(qnt_produto):
            count_frita += 1
        lista.append("{} batatas fritas".format(count_frita))

    elif var_decisao == 4:
        print("Quantos refris você deseja? ")
        qnt_produto = int(input(""))
        for num in range(qnt_produto):
            count_refri += 1
        lista.append("{} refris".format(count_refri))

    elif var_decisao == 5:
        x = 2
    else:
        print("Digite somente valores válidos")

confirmacao = str(input("O pedido foi: {}".format(lista))).upper()
if confirmacao == "SIM" or confirmacao == "S":
    print("Pedido processado")
    result = (count_h * 2.50) + (count_cb * 3.30) + (count_frita * 1.50) + (count_refri * 0.60)
    result_comissao = (result * 0.10) + result
    print("O valor a ser pago é de: {} com 10% de comissão inseridos".format(result_comissao))
elif confirmacao == "NÃO" or confirmacao == "NAO" or confirmacao == "N":
    x = 1
else:
    "Escreva somente sim ou não"
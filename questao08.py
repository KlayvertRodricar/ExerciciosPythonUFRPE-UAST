#Deseja-se fazer uma pesquisa a respeito do consumo mensal de energia elétrica em uma determinada cidade. Faça um programa que lê, para cada consumidor, o seu número de identificação, a quantidade de kWh consumida durante o mês e o código do tipo do consumo (1 - residencial, 2 - comercial ou 3 – industrial). Um código de consumidor igual a zero indica o final dos dados. O programa deve calcular:
# Para cada consumidor, o total a pagar. O preço do kWh é R$ 0,85 para consumo residencial, R$ 0,35 para consumo comercial e R$ 0,10 para consumo industrial; Se a quantidade de kWh consumida durante o mês pelo usuário for menor que o limite mínimo pré-determinado, este terá um desconto de 20% no valor total de sua conta. O limite mínimo para residências é 30 kWh, para comércios é de 100 kWh e para indústrias é de 200 kWh.
lista_residencial = []
lista_comercial = []
lista_industrial = []
kwh_residencial = 0.85
min_residencial = 30.0
kwh_comercial = 0.35
min_comercial = 100.0
kwh_industrial = 0.10
min_industrial = 200.0
x = 1
while x == 1:
    print("Qual o seu imóvel? ")
    var_imovel = int(input("1)Residencial\n2)Comercial\n3)Industrial\n0)Sair\n"))

    if var_imovel == 1:
        var_nome_cliente = str(input("Digite o seu nome: "))
        print("Imóvel residencial")
        var_gasto = float(input("Digite o seu gasto mensal: "))

        if var_gasto < min_residencial:
            gasto_final = (kwh_residencial * var_gasto) * 0.20
            lista_residencial.append("Cliente {} deve pagar {:.2f} reais".format(var_nome_cliente, gasto_final))

        elif var_gasto >= min_residencial:
            gasto_final = kwh_residencial * var_gasto
            lista_residencial.append("Cliente {} deve pagar {:.2f} reais".format(var_nome_cliente, gasto_final))

        else:
            print("Digite somente números válidos")
    
    elif var_imovel == 2:
        var_nome_cliente = str(input("Digite o seu nome: "))
        print("Imóvel comercial")
        var_gasto = float(input("Digite o seu gasto mensal: "))

        if var_gasto < min_comercial:
            gasto_final = (kwh_comercial * var_gasto ) * 0.20
            lista_comercial.append("Cliente {} deve pagar {:.2f} reais".format(var_nome_cliente, gasto_final))
        elif var_gasto >= min_comercial:
            gasto_final = kwh_comercial * var_gasto
            lista_comercial.append("Cliente {} deve pagar {:.2f} reais".format(var_nome_cliente, gasto_final))
        else:
            print("Digite somente números válidos")

    elif var_imovel == 3:
        var_nome_cliente = str(input("Digite o seu nome: "))
        print("Imóvel industrial")
        var_gasto = float(input("Digite o seu gasto mensal: "))

        if var_gasto < min_industrial:
            gasto_final = (kwh_industrial * var_gasto)* 0.20
            lista_industrial.append("Cliente {} deve pagar {:.2f} reais".format(var_nome_cliente, gasto_final))

        elif var_gasto >= min_industrial:
            gasto_final = kwh_industrial * var_gasto
            lista_industrial.append("Cliente {} deve pagar {:.2f} reais".format(var_nome_cliente, gasto_final))
        else:
            print("Digite somente números válidos")

    elif var_imovel == 0:
        x = 2
    else:
        print("Digite somente os números do menu!")

print("lista das residencias: {}".format(lista_residencial))
print("lista dos comercios: {}".format(lista_comercial))
print("lista das industrias: {}".format(lista_industrial))
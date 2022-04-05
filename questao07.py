#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por código.Os dados utilizados para apuração obedecem à seguinte codificação:
# 1, 2, 3, 4 = voto para os respectivos candidatos;
# 5= voto nulo; e
# 6=voto em branco.
#Elabore um algoritmo que calcule e escreva:
# O total de votos para cada candidato e seu percentual sobre o total;
# O total de votos nulos e seu percentual sobre o total; e
# O total de votos em branco e seu percentual sobre o total
#Como finalizador do conjunto de votos, tem-se o valor 0 (zero), ou seja, o

lista_bolsonaro = []
lista_lula = []
lista_eduardo = []
lista_aecio = []
lista_branco = []
lista_nulo = []
x=1

while x == 1:
    print("1)Bolsonaro\n2)Lula\n3)Eduardo Campos\n4)Aécio Neves\n5)Voto branco\n6)Voto nulo\n0)Sair")
    var_voto = int(input("Digite o número referente ao voto: "))
    

    if var_voto == 1:
        lista_bolsonaro.append(1)
    elif var_voto == 2:
        lista_lula.append(1)
    elif var_voto == 3:
        lista_eduardo.append(1)
    elif var_voto == 4:
        lista_aecio.append(1)
    elif var_voto == 5:
        lista_branco.append(1)
    elif var_voto == 6:
        lista_nulo.append(1)
    elif var_voto == 0:
        x = 2
    else:
        print("Digite somente números válidos da opção.")

opcao01 = len(lista_bolsonaro)
opcao02 = len(lista_lula)
opcao03 = len(lista_eduardo)
opcao04 = len(lista_aecio)
opcao05 = len(lista_branco)
opcao06 = len(lista_nulo)

final_result = opcao01 + opcao02 + opcao03 + opcao04 + opcao05 + opcao06

print("O resultado do candidato Bolsonaro: {}/{}".format(opcao01, final_result))
print("O resultado do candidato Lula: {}/{}".format(opcao02,final_result))
print("O resultado do candidato Eduardo Campos: {}/{}".format(opcao03,final_result))
print("O resultado do candidato Aécio Neves: {}/{}".format(opcao04,final_result))

print("O resultado dos votos em branco: {}/{}".format(opcao05,final_result))

print("O resultado dos votos nulos: {}/{}".format(opcao06,final_result))

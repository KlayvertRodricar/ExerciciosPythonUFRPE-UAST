#Escreva um algoritmo em python para ler um número indeterminado de dados, contendo cada um o peso de um indivíduo. A entrada termina quando for inserido um peso negativo. Calcular e imprimir: 
# ◦ A média aritmética dos pesos das pessoas que possuem mais de 60 Kg;
# ◦ O maior peso.
list_peso = []
list_peso_menor = []
x = -1
count = 0
somatorio = 0
maior_peso = 0

while x < 0:
    individuo = str(input("Digite seu nome: "))
    peso = float(input("Digite seu peso: "))

    if peso > 60:
        list_peso.append(peso)
        count += 1
        somatorio += peso

        if peso > maior_peso:
            maior_peso = peso
            
    elif peso < 60 and peso >= 0:
        list_peso_menor.append(peso)

    else:
        x += 2
        
media_arit = somatorio / count
print("A média de peso é {} quilos".format(media_arit))
print("O maior peso é {} quilos".format(maior_peso))
print(list_peso)
print(list_peso_menor)
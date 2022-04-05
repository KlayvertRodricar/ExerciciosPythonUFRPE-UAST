#Faça um programa que tenha como entrada um número N e mostre os N-ésimos primeiros números pares e depois os N-ésimos primeiros números ímpares.
lista_par = []
lista_impar = []
var_decisao = int(input("Digite um número: "))
for num in range(var_decisao):
    if num % 2 == 0:
        lista_par.append(num)
    elif num % 2 == 1:
        lista_impar.append(num)
    else:
        print("Digite somente números!")
    
print(lista_par)
print(lista_impar)
print(lista_par[0:4])
print(lista_impar[0:4])
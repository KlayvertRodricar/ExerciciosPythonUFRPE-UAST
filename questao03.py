#Faça um algoritmo que leia 20 valores e no final, informe o seu somatório e produto.
count_sum = 0
count_product = 1
var_qnt = int(input("Write a number to make it the limit repetition: "))
for times in range(var_qnt):
    number = float(input("Write a number: "))
    count_sum += number
    count_product *= number

print("Somatory = {}\n"
"Product = {}".format(count_sum, count_product))
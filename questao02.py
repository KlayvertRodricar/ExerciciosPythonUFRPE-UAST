#Faça um algoritmo que leia 10 valores e no final, informe quantos eram maiores que 100.
list_over = []
times_to_repeat = int(input("Write how many numbers do you want to repeat the script: "))
for times in range(times_to_repeat):
    number = int(input("Write the number to comparison if is over or less 100: "))
    if number > 100:
        list_over.append(number)
    elif number < 100:
        pass 
    else:
        print("Only numbers not letters or special caracters")
print("Only over 100 numbers is: {}".format(list_over))
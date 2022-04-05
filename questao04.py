#Escreva um algoritmo que tenha como entrada o número de matrícula, nota1 e nota2 de 50 alunos. Em seguida, mostre quantos foram aprovados e quantos foram reprovados. Sabe-se que o aluno com média maior ou igual a 7 será aprovado.
aproved_list = []
reproved_list = []
count_aproved = 0
count_reproved = 0
for term in range(5):
    id_student = input("Write the student's ID: ")
    score01 = float(input("First avaliation score: "))
    score02 = float(input("Second avaliation score: "))
    result = (score01 + score02)/2

    if result >= 7 and result <= 10:
        aproved_list.append("{} with {}".format(id_student,result))
        count_aproved += 1
    elif result < 7 and result >= 0:
        reproved_list.append("{} with {}".format(id_student, result))
        count_reproved += 1
    else:
        pass

print("Aproved list: {}".format(aproved_list))
print("Reproved list: {}".format(reproved_list))
print("The aproved students is: {}".format(count_aproved))
print("The reproved students is: {}".format(count_reproved))
# Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import randint

aluno1 = input('Nome do aluno 1: ')
aluno2 = input('Nome do aluno 2: ')
aluno3 = input('Nome do aluno 3: ')
aluno4 = input('Nome do aluno 4: ')

n = randint(1, 4)
if (n == 1):
    print(aluno1)
elif (n == 2):
    print(aluno2)
elif (n == 3):
    print(aluno3)
else:
    print(aluno4)

#Usando a função choice
print()
from random import choice
nome = choice([aluno1,aluno2,aluno3,aluno4])
print(nome)


# Mais uma maneira de fazer, mas agora usando um array e o ciclo for
alunos = []
for i in range(4):
    alunos.append(input('Nome do aluno {}: ' .format(i + 1)))

n = randint(0, 3)
print(alunos[n])

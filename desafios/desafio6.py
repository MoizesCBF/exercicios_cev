# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

a = int(input("Número: "))
print('Dobro de {0} = {1}: '.format(a, a * 2))
print('Triplo de {0} = {1}: '.format(a, a * 3))
print('Raiz Quadrada de {0} = {1}: '.format(a, a ** 0.5))

# OU

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1 / 2)
print('O dobro de {0} vale {1}.\nO triplo de {0} vale {2}.\nA raiz quadrada de {0} vale {3:.2f}.'.format(n, d, t, r))

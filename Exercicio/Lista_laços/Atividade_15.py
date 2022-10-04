# A série de FETUCCINE é gerada da seguinte forma: os dois primeiros termos
# são fornecidos pelo usuário; a partir daí, os termos são gerados com a soma
# ou subtração dos dois termos anteriores, ou seja:

# Ai = Ai-1 + Ai-2 para par
# Ai = Ai-1 - Ai-2 para impar

# Faça um programa em Python para mostrar os N primeiros termos da série de
# FETUCCINE, sabendo-se que para existir esta série serão necessários pelo
# menos três termos.

numero1 = int(input("Informe o valor de 1° número: "))
numero2 = int(input("Informe o valor de 2° número: "))
n = int(input("Informe o valor de quantos números você quer que apareça: "))

print(numero1, end="  ")
print(numero2, end="  ")

for i in range(3, n + 1):
    if i % 2 == 0:
        serie = numero2 - numero1
    else:
        serie = numero2 + numero1

    numero1 = numero2
    numero2 = serie

    print(serie, end="  ")

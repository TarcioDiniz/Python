# Faça um programa para somar os números pares positivos &lt; 1000 e ao final
# escrever o resultado.

soma = 0
for i in range(0, 1_000, 2):
    soma += i
print(soma)

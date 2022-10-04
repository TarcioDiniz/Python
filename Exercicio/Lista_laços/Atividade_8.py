# Faça um programa para:
# a) Ler um valor x qualquer
# b) Calcular Y = (x+1)+(x+2)+(x+3)+(x+4)+(x+5)+…(x+100).

RED = "\033[1;31m"
RESET = "\033[0;0m"

repete = 1
while repete == 1:
    try:
        x = int(input('Informe o valor de X: '))
    except ValueError:
        print(f'{RED}Número não identificado{RESET}')
        pass
    else:
        repete = 0


soma = 0
for i in range(1, 101):
    soma += x + i
print(f'A soma foi: {soma}')

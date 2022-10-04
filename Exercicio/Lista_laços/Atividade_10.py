# Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

RED = "\033[1;31m"
RESET = "\033[0;0m"

repete = 1
while repete == 1:
    try:
        n = int(input('Informe com quantos termos a serie seja realizada: '))
    except ValueError:
        print(f'{RED}Número não identificado{RESET}')
        pass
    else:
        if n < 0:
            print(f'{RED}Número negativo? por favor repita.{RESET}')
            pass
        else:
            repete = 0

count = 0
soma = 0
for i in range(1, n+1, 2):
    count += 1
    soma += count/i
print(f'A soma dos da serie é {soma}')

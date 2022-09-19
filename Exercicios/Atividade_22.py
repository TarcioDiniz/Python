# Faça um Programa Python que peça um número correspondente a um determinado
# ano e em seguida informe se este ano é ou não bissexto.

#  Sendo que um ano é bissexto se for
# divisível por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo: 1988, 1992, 1996

ano = int(input("Digite um ano: "))
div2 = ano % 4
if div2 == 0:
    print("Ano Bissexto")
else:
    print("Ano não Bissexto")
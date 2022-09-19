# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

# a. Até 5 Kg Acima de 5 Kg

# ii. Morango R$ 2,50 por Kg R$ 2,20 por Kg
# iii. Maçã R$ 1,80 por Kg R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total. Escreva um programa Python para ler a
# quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o
# valor a ser pago pelo cliente.

try:
    morango_quilos = float(input('Informe quantos Kg de morango: '))
except ValueError:
    print('Número não reconhecido.')
    exit()

if morango_quilos < 0:
    print('Valor negativo.')
    exit()

try:
    maca_quilos = float(input('Informe quantos Kg de maçã: '))
except ValueError:
    print('Número não reconhecido.')
    exit()

if maca_quilos < 0:
    print('Valor negativo.')
    exit()

valor_morango = morango_quilos * 2.2
valor_maca = maca_quilos * 1.5
total = valor_morango + valor_maca

if morango_quilos + maca_quilos >= 8 or total >= 25:
    teve_desconto = 'com'
    desconto = 10/100
    total = total + (total * desconto)
else:
    teve_desconto = 'sem'

print(f'Total {teve_desconto} desconto: {total}')

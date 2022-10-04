# Faça um programa que receba o valor de uma dívida e mostre uma tabela com
# os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e
# valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
#      1              0
#      3              10
#      6              15
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela

# valor da dívida     valor dos juros    quantidade de parcelas       valor da parcela
# R$ 1.000,00            0                     1                         R$ 1.000,00
# R$ 1.100,00           10                     3                         R$ 366,67
# R$ 1.150,00           15                     6                         R$ 191,67

BOLD = "\033[;1m"
RESET = "\033[0;0m"

valor_divida = float(input('Informe o valor da divida: '))

parcelas = 1, 3, 6
juros = 0, 10, 15
print(f'{BOLD}valor da dívida     valor dos juros    quantidade de parcelas       valor da parcela{RESET}')
for i in range(3):
    print(valor_divida * (juros[i])/100 + valor_divida, ' '*19,
          juros[i], ' '*20,
          parcelas[i], ' '*20,
          round(((valor_divida * (juros[i])/100 + valor_divida) / parcelas[i]), 2))

# O cardápio de uma lanchonete é o seguinte:

#   Especificação     Código        Preço
#   Cachorro Quente     100         R$ 1,20
#   Bauru Simples       101         R$ 1,30
#   Bauru com ovo       102         R$ 1,50
#   Hambúrguer          103         R$ 1,20
#   Cheeseburguer       104         R$ 1,30
#   Refrigerante        105         R$ 1,00
#
# Faça um programa que leia o código dos itens pedidos e as quantidades
# desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e
# o total geral do pedido. Considere que o cliente deve informar quando o pedido
# deve ser encerrado.

RED = "\033[1;31m"
BLUE = "\033[1;34m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"

especificacao = 'Cachorro Quente,Bauru Simples  ,Bauru com ovo  ,Hambúrguer     ,Cheeseburguer  ,Refrigerante   '
codigo = '100,101,102,103,104,105'
preco = '1.20,1.30,1.50,1.20,1.30,1.00'

print(f'{BOLD}Especificação', ' ' * 20, 'Código', ' ' * 20, f'Preço{RESET}')
for i in range(6):
    print(especificacao.split(',')[i], ' ' * 20, codigo.split(',')[i], ' ' * 20, f'R$ {preco.split(",")[i]}')

verifica = 1
while verifica == 1:
    lanche_escolhido = input(f'\n{BOLD}Informe o Código do lanche:{RESET} ')

    if lanche_escolhido in codigo.split(','):
        index_codigo = codigo.split(',').index(lanche_escolhido)
        verifica_2 = 1
        while verifica_2 == 1:
            quantidade = input(f'{BOLD}Informe a quantidade que você deseja:{RESET} ')
            if quantidade.isnumeric():
                total = eval(f"{preco.split(',')[index_codigo]} * {quantidade}")
                print(f'{BOLD}Total:{RESET} {GREEN}R$ %.2f{RESET}' % total)
                verifica_2 = 0
                verifica = 0
            else:
                print(f'{RED}Essa quantidade não existe.{RESET}')
    else:
        print(f'{RED}Esse código não existe.{RESET}')

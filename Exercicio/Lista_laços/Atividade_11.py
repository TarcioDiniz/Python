# Cada espectador de um cinema respondeu a um questionário no qual constava
# sua idade e a sua opinião em relação ao filme: ótimo - 3, bom - 2, regular - 1.
# Faça um programa que receba a idade e a opinião de 15 espectadores, calcule
# e imprima:
# a) A média das idades das pessoas que responderam ótimo;
# b) A quantidade de pessoas que responderam regular;
# c) A porcentagem de pessoas que responderam bom entre todos os
# espectadores analisados.


RED = "\033[1;31m"
BLUE = "\033[1;34m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
YELLOW = '\033[33m'

otimo = 0
bom = 0
regular = 0
soma_idade = 0
media_otimo = 0

for i in range(15):
    repete = 1
    while repete == 1:
        try:
            idade = int(input(f'{BOLD}Informe sua idade:{RESET} '))
        except ValueError:
            print(f'{RED}IDADE INVALIDA. POR FAVOR REPITA.{RESET}')
        else:
            if idade < 5:
                print(f'{RED}IDADE APENAS ENTRE 5 E 65 ANOS. POR FAVOR REPITA.{RESET}')
            else:
                if idade > 65:
                    print(f'{RED}IDADE APENAS ENTRE 5 E 65 ANOS. POR FAVOR REPITA.{RESET}')
                else:
                    soma_idade += 1
                    repete = 0
    print(f'{BOLD}Classifique o filme em:{RESET} ')
    print(f'{YELLOW}Otimo ---- 3\nBom ------ 2\nRegular -- 1{RESET}')
    repete = 1
    while repete == 1:
        try:
            classificacao = int(input(f'{BOLD}Digite aqui:{RESET} '))
        except ValueError:
            print(f'{RED}SUA RESPOSTA AINDA NÃO FOI QUANTIFICADA. POR FAVOR REPITA.{RESET}')
        else:
            if 1 <= classificacao <= 3:
                if classificacao == 3:
                    media_otimo = media_otimo + idade
                    otimo += 1
                else:
                    if classificacao == 2:
                        bom += 1
                    else:
                        if classificacao == 1:
                            regular += 1
                repete = 0
            else:
                print(f'{RED}SUA RESPOSTA AINDA NÃO FOI QUANTIFICADA.{RESET}{BOLD}\n'
                      f'Só é aceito 1, 2 ou 3. Por favor repita.{RESET}')
                pass


media_otimo = media_otimo / otimo
porcentagem_bom = (bom * 100) / 15
print(f'A média das idades das pessoas que responderam ótimo: {media_otimo} anos')
print(f'A quantidade de pessoas que responderam regular: {regular}')
print(f'A porcentagem de pessoas que responderam bom entre todos os espectadores analisados: {porcentagem_bom}%')





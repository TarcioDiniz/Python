list_of_options = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
dicionary = {'Windows Server': 0,
             'Unix': 0,
             'Linux': 0,
             'Netware': 0,
             'Mac OS': 0,
             'Outro': 0}

for i in range(len(list_of_options)):
    print(f'{i + 1} - {list_of_options[i]}')

voto = int(input('Escolha a opção: '))
if 6 >= voto >= 1:
    votoChoice = dicionary[list_of_options[voto - 1]]
    dicionary.update({f'{list_of_options[voto - 1]}': votoChoice + 1})
else:
    if voto == 0:
        print('Encerrado')
    else:
        print('Escolha não identificada.')

while voto > 0:
    print('')
    for i in range(len(list_of_options)):
        print(f'{i + 1} - {list_of_options[i]}')

    voto = int(input('Escolha a opção: '))
    if 6 >= voto >= 1:
        votoChoice = dicionary[list_of_options[voto - 1]]
        dicionary.update({f'{list_of_options[voto - 1]}': votoChoice + 1})
    else:
        if voto == 0:
            print('Encerrado')
        else:
            print('Escolha não identificada.')

sumVotes = dicionary['Windows Server'] + dicionary['Unix'] + dicionary['Linux'] + \
           dicionary['Netware'] + dicionary['Mac OS'] + dicionary['Outro']


def percentage(value, total):
    try:
        return round((value * 100 / total), 2)
    except ZeroDivisionError:
        return '00.00'


print("{:<23} {:<13} {:<8}".format('Sistema Operacional', 'Votos', '%'))
print("{:<23} {:<9} {:<8}".format('-------------------', '--------', '--------'))
print("{:<23} {:<10} {:<8}".format(f'{list_of_options[0]}', f'{dicionary[list_of_options[0]]}',
                                   f'{percentage(dicionary[list_of_options[0]], sumVotes)}%'))
print("{:<23} {:<10} {:<8}".format(f'{list_of_options[1]}', f'{dicionary[list_of_options[1]]}',
                                   f'{percentage(dicionary[list_of_options[1]], sumVotes)}%'))

print("{:<23} {:<10} {:<8}".format(f'{list_of_options[2]}', f'{dicionary[list_of_options[2]]}',
                                   f'{percentage(dicionary[list_of_options[2]], sumVotes)}%'))

print("{:<23} {:<10} {:<8}".format(f'{list_of_options[3]}', f'{dicionary[list_of_options[3]]}',
                                   f'{percentage(dicionary[list_of_options[3]], sumVotes)}%'))

print("{:<23} {:<10} {:<8}".format(f'{list_of_options[4]}', f'{dicionary[list_of_options[4]]}',
                                   f'{percentage(dicionary[list_of_options[4]], sumVotes)}%'))

print("{:<23} {:<10} {:<8}".format(f'{list_of_options[5]}', f'{dicionary[list_of_options[5]]}',
                                   f'{percentage(dicionary[list_of_options[5]], sumVotes)}%'))
print("{:<23} {:<9} {:<8}".format('-------------------', '--------', ''))
print("{:<23} {:<9} {:<8}".format('Total', f'{sumVotes}', ''))

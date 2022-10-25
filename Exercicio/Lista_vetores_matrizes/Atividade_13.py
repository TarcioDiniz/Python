# Faça um programa que receba a temperatura média de cada mês do ano e
# armazene-as em uma lista. Após isto, calcule a média anual das temperaturas
# e mostre todas as temperaturas acima da média anual, e em que mês elas
# ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

monthList = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
             'novembro', 'dezembro']
averageMonthList = []
for i in range(len(monthList)):
    averageMonthList.append(float(input(f'Informe a temperatura média do mês de {monthList[i]}: ')))

averageYear = sum(averageMonthList) / len(averageMonthList)

dictionary = []

for i in range(len(monthList)):
    dictionary.append({
        'Month': monthList[i],
        'Average': averageMonthList[i]}
    )
print(f'\ntemperaturas acima da média anual de {averageYear}')
for i in range(len(dictionary)):
    if dictionary[i]['Average'] > averageYear:
        print(f'{i + 1} - {dictionary[i]["Month"]} de média: {dictionary[i]["Average"]}')

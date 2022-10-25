listaNumeros = []
for i in range(3):
    listaNumeros.append(int(input(f'Informe o {i + 1}°: ')))
print(f'Sua lista é:\n{listaNumeros} \nO segundo maior número é: {sorted(listaNumeros)[-2]}')

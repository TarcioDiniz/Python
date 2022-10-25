vetor = []
for i in range(1, 11):
    vetor.append(i)
soma_vetores = 0
for soma in range(len(vetor)):
    soma_vetores += vetor[soma] ** 2

print(soma_vetores)

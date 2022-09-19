# Faça um programa Python que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em MBps), calcule e informe o tempo
# aproximado de download do arquivo usando este link (em minutos).

# https://www.tecmundo.com.br/banda-larga/32749-megabit-x-megabyte-qual-a-real-velocidade-da-minha-conexao-.htm
# Jogue na sua calculadora o valor da sua conexão. Caso você tenha contratado um plano de 10 mega, digite 10;
# Depois, use a operação de divisão e divida o 10 por 8;
# Pronto, agora você sabe que a velocidade máxima da sua conexão é de 1,25 megabytes.

arquivo = float(input("Informe do tamanho do arquivo em MegaByte: "))
link = float(input("Informe a velocidade do link em Mbps: "))
tempo = ((arquivo * 8) / link) / 60
print("O tempo aproximado de download é de %.2f minutos" % tempo)



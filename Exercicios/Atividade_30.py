# Fazer um programa em Python para determinar o quadrante ao qual pertence um
# determinado ponto P(x, y).
while True:
    try:
        x, y = input("Digite as coordenadas de (x,y): ").split(",")
        if float(x) == 0 or float(y) == 0:
            print("Erro, X e/ou Y não pode ser zero.")
        elif float(x) > 0 and float(y) > 0:
            print(f"As coordenadas de {x,y} encontra-se no primeiro quadrante (+,+)")
        elif float(x) < 0 < float(y):
            print(f"As coordenadas de {x,y} encontra-se segundo quadrante (-,+)")
        elif float(x) < 0 and float(y) < 0:
            print(f"As coordenadas de {x,y} encontra-se terceiro quadrante (-,-)")
        elif float(x) > 0 > float(y):
            print(f"As coordenadas de {x,y} encontra-se quarto quadrante (+,-)")
            break
    except ValueError:
        print('Número não identificado.')
        pass

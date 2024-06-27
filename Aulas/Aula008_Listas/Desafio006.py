valores = [[], []]


for i in range(7):
    valor = int(input(f"Digite o {i+1}º valor: "))
    if valor % 2 == 0:
        valores[0].append(valor)  #Par
    else:
        valores[1].append(valor)  #Ímpar


valores[0].sort()
valores[1].sort()

print("Valores pares:", valores[0])
print("Valores ímpares:", valores[1])
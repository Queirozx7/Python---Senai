matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para [{i},{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("Matriz 3x3:")
for linha in matriz:
    for valor in linha:
        print(f"{valor:^5}", end=" ")
    print()  

soma_pares = 0
for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            soma_pares += valor

soma_terceira_coluna = 0
for linha in matriz:
    soma_terceira_coluna += linha[2]

maior_segunda_linha = max(matriz[1])


print(f"\nA) Soma dos valores pares: {soma_pares}")
print(f"B) Soma dos valores da terceira coluna: {soma_terceira_coluna}")
print(f"C) Maior valor da segunda linha: {maior_segunda_linha}")


numeros = []
pares = []
impares = []

while True:
    num = int(input("Digite um número (ou 0 para sair): "))
    if num == 0:
        break
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Todos os números:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)

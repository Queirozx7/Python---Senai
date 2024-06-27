pessoas = []
mais_pesado = mais_leve = 0

while True:
    nome = input("Nome da pessoa (ou 'fim' para encerrar): ")
    if nome.lower() == 'fim':
        break
    peso = float(input("Peso da pessoa: "))
    pessoas.append((nome, peso))
    
   
    if peso > mais_pesado:
        mais_pesado = peso
    if mais_leve == 0 or peso < mais_leve:
        mais_leve = peso

qtd_pessoas = len(pessoas)

pessoas_pesadas = [pessoa[0] for pessoa in pessoas if pessoa[1] == mais_pesado]

pessoas_leves = [pessoa[0] for pessoa in pessoas if pessoa[1] == mais_leve]

print(f"A) Quantidade de pessoas cadastradas: {qtd_pessoas}")
print("B) Pessoas mais pesadas:")
for pessoa in pessoas_pesadas:
    print(f"   - {pessoa}")
print("C) Pessoas mais leves:")
for pessoa in pessoas_leves:
    print(f"   - {pessoa}")

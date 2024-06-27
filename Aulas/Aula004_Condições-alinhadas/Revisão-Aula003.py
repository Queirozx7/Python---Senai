# aula 004 python -  revisando aula 003 

NomeCidade = str(input('Digite o nome da cidade: '))
divideNomeCidade = NomeCidade.split()

primeiroNomeCidade = divideNomeCidade[0].upper()
verificaPalavraEmFrase = 'SANTO' in primeiroNomeCidade
# Indica se possui uma PALAVRA em uma frase

print(f'O nome da cidade {NomeCidade} começa com Santo?: {verificaPalavraEmFrase}')

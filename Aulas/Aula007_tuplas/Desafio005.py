# Crie um programa que tenha uma TUPLA única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma lsitagem de preços organizando os dados em forma TABULAR. 

produtos = ('Sofa' , 800.00 , 'Geladeira' , 700.00, 'Fogão' , 700.00 , 'Forno' , 300.00)

tamanho = len(produtos)

print("PRODUTO  ------------ PREÇO")

for i in range(0,tamanho,2):
    print(f"{produtos[i]} --    -    -- R${produtos[i+1]}")
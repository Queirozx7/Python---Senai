# DICIONÁRIO EM PYTHON 
# armazena pares chave-valor






# testes DICIONARIO

meu_dicionary={
    "Nome": "Bob",
    "Sobrenome": "Esponja",
    "Idade": 15
} 


###lista de dicionários:
personagens = [
    {'Nome' : 'Bob','Sobrenome' : 'Esponja','idade' : 35},{'Nome' : 'Patrick','Sobrenome' : 'Estrela','Idade' : 34},{'Nome': 'Sandy','Sobrenome': 'Esquilo','Idade' : 45}
]
    
primeiro_registro = personagens


print(f'O pensonagem {primeiro_registro["Nome"]} {primeiro_registro["Sobrenome"]} possui a idade {primeiro_registro["Idade"]}')
# or 
# print(f'O personagem {personagens[0]["Nome"]} {personagens[0]["Sobrenome"]} e possui a idade {personagens[0]["Idade"]}')

for k,v in meu_dicionary[0].items():
    print(f'{k} é {v}')
    
print("-="*20)
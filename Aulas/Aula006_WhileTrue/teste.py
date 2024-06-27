# UTULIZANDO (WHILE)

x= 1
while x<10:
    print(x)
    x=x+1
else:
    print('acabou o loop')
    
numero = 0 
while numero < 5:
    numero += 1 
    
    if numero == 3:
        print('Vamos Pular a interação para',numero)
        continue
    
    print('Numero:', numero)
print ('===Fim do loop===')

while True: 
    resposta = input('Deseja sair? (s/n):')
    if resposta.lower() == 's':
        print('Saindo do loop.')
        break
    print('Continuando o loop...')
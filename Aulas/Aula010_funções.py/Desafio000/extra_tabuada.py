
def tabuada(numero,fim):
    print(f'Tabuada do {numero}: ')
    for i in range(1,fim+1):
        resultado = numero * i 
        print(f'{numero} x {i} = {resultado}')
        
        

def dados():
    print('Olá {nome}, seja bem vindo! ')

nome = str(input('Digite o seu nome: '))
numero = int(input('Digite o Numero que deseja multiplicar: '))
fim = int(input('Digite o limite da tabuada: '))

#chamando as funções 
dados(nome)
tabuada(numero,fim)

valor_casa = float(input("Digite o valor da casa: "))
salario = float(input('Digite o eu salário: '))
anos_pagar = int(input("Em quantos anos pretende realizar o pagamento: "))
print('')
meses=anos_pagar*12
prestacion= valor_casa/meses
print(f'Meses a serem pagos = {meses}')
print(f'Valor das prestações = {prestacion} ')

max_prestacion = salario*0.30

print('')
if prestacion<max_prestacion:
    print('Empréstimo aprovado, parabéns !!! ')
else:
    print('Infelizmente o empréstimo foi negado! ')
    print('MOTIVO: Prestações ultrapassam 30% (porcento) de seu salário')
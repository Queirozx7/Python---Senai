# CRIE UM PROGRAMA QUE TENHA UMA DUPLA TOTALMENTE PREENCHIDA COM UMACONTAEM POR EXTENSO DE 0 ATÉ 20
#  SEU PROGRAMA DEVERÁ LER UM NUMERO PELO TECLADO (0 a 20) e mostra-lo por extenso (ZERO a VINTE)


num_extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um número entre 0 a 20 (Zero a Vinte): '))
    for i in range(0,1):
        if num>20 and num<0:
            print("Número incorreto")
            break
        else:
            print(num_extenso[num])
 
 
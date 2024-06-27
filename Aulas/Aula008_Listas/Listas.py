
# ==================================================== COMANDOS PRA LISTA =====================================================

lista = [4,5,6,7,8]
print(lista) #lista completa
print(lista[4]) #mostra num 8
print(lista[-1]) #mostra o ultimo da lista

# =====================================================================
lista[-1] = "Senai" # Substitiu a ultima coisa da lista
print(lista) #[4,5,6,7,'Senai']

# ==================================================================
lista.append(101) #Acrescenta algo no final da lista
print(lista) #[4,5,6,7, 'Senai' , 101]

# ===================================================================================
lista.insert(1,'Nami') #1 é a posição onde vai ser inserido o valor 'Nami Jafet'
# pode ser usado o -1 para colocar o valor no final da lista
print(lista) # print(lista) [4,5,6,7, 'Senai' ' Nami Jafet', 101]

# ======================================================================================================
lista.remove(3) # remove (valor) apaga o valor o primeiro que achar (de acordo com oq pediu)
print(lista) # [4,5,6,'Senai' ' Nami Jafet', 101] (retirou o '7')

# ==========================================================================================
mlista = [4,5,6,7,8] # so pode ser usado se tiver apenas um tipo (ou só txt ou só num)
mlista.sort() #(vai organizar a lista de forma crescente)
mlista.reverse() #(vai organizar a lista de forma decrescente)

# =================================================================================
milista = mlista.pop() #remove o ultimo 'valor' da lista (SISTEMA DE 'PILHA')
print(mlista) # remove salvando em outra variavel 


# =============================================================
del lista[2:6]# apaga o que esta nas posiçõs 2e6 ( apagados)
print(mlista) # [4,5,8] (num 6 e 7 excluidos)

#====================================== 
lista.clear #(faz o clear)
print(lista) # lista fica vazia 


# =============================================== LISTA DENTRO DE OUTRA LISTA =====================================================

compras = [15.5,45.4,2.99,5,66]
print(compras) # compras = [15.5,45.4,2.99,5,66]

compras = [15.5,45.4,2.99,5,66 ['macarrao' , 'arroz' , 'fini' , 'sabão']]
print(compras) # [15.5,45.4,2.99,5,66, 'macarrao' 'arroz' 'fini' 'sabão']]


produtos = compras[4] #deixa preços + os produtos (neste caso)
print(produtos) # 'macarrao' , 'arroz' , 'fini' , 'sabão'


letras = ['a,b,c']

numeros = [1,2,3]

tudo = letras,numeros
print(tudo) # [[a, b, c] , [ 1 ,2 ,3 ]]
 
# =========================== VERIFICAR A EXISTENCIA DE UM VALOR ==============================================


letras = ['a , b , c , d , e']
var = input('informe a letra: ')


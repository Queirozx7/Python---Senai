import sys
from PyQt6.QtWidgets import *

app  = QApplication(sys.argv)


with open('estilo_calculadora.css','r') as file:
    app.setStyleSheet(file.read())
    
janela = QWidget()
janela.resize(370,600) # (x, y)

operador1 = QLineEdit("",janela)
operador2 = QLineEdit("",janela)
sinal = QLineEdit("",janela)


    

#### FUNÇÕES
def limparVisor():
    visor.setText("")
    
def exibirNoVisor(numero):
    valor = visor.text()
    visor.setText(valor + numero)

def somar ():
    operador1.setText(visor.text())
    sinal.setText("+")
    visor.setText('')

def calcular():
    operador2.setText(visor.text())
    
    if sinal.text() == "+":
        somaValores = float(operador1.text()) + float(operador2.text())
        visor.setText(str(somaValores))


visor = QLineEdit('',janela)

letraC = QPushButton('C',janela)
letraC.setGeometry(10,155,260,80)
letraC.setStyleSheet('background-color: white;color:tomato;border-style: solid;border-color:tomato;border-width: 1px;border-radius: 5px;font-size: 20px;')
letraC.clicked.connect(limparVisor)
    
#Coluna 1
numero7 = QPushButton('7',janela)
numero7.setGeometry(10,245,80,80)
numero7.clicked.connect(lambda: exibirNoVisor('7'))


numero4 = QPushButton('4',janela)
numero4.setGeometry(10,335,80,80)
numero4.clicked.connect(lambda: exibirNoVisor('4'))


numero1 = QPushButton('1',janela)
numero1.setGeometry(10,425,80,80)
numero1.clicked.connect(lambda: exibirNoVisor('1'))


sinais1 = QPushButton('0',janela)
sinais1.setGeometry(10,515,170,80)
sinais1.clicked.connect(lambda: exibirNoVisor('0'))


#Coluna 2
numero8 = QPushButton('8',janela)
numero8.setGeometry(100,245,80,80)
numero8.clicked.connect(lambda: exibirNoVisor('8'))


numero5 = QPushButton('5',janela)
numero5.setGeometry(100,335,80,80)
numero5.clicked.connect(lambda: exibirNoVisor('5'))


numero2 = QPushButton('2',janela)
numero2.setGeometry(100,425,80,80)
numero2.clicked.connect(lambda: exibirNoVisor('2'))


#Coluna 3
numero9 = QPushButton('9',janela)
numero9.setGeometry(190,245,80,80)
numero9.clicked.connect(lambda: exibirNoVisor('9'))


numero6 = QPushButton('6',janela)
numero6.setGeometry(190,335,80,80)
numero6.clicked.connect(lambda: exibirNoVisor('6'))


numero3 = QPushButton('3',janela)
numero3.setGeometry(190,425,80,80)
numero3.clicked.connect(lambda: exibirNoVisor('3'))


ponto = QPushButton('.',janela)
ponto.setGeometry(190,515,80,80)
ponto.clicked.connect(lambda: exibirNoVisor('.'))


#Coluna 4
divisao = QPushButton('/',janela)
divisao.setGeometry(280,155,80,80)


multiplicacao = QPushButton('x',janela)
multiplicacao.setGeometry(280,245,80,80)


subtracao = QPushButton('-',janela)
subtracao.setGeometry(280,335,80,80)


soma = QPushButton('+',janela)
soma.setGeometry(280,425,80,80)
soma.clicked.connect(somar)


igual = QPushButton('=',janela)
igual.setGeometry(280,515,80,80)
igual.clicked.connect(calcular)



janela.show()
app.exec()
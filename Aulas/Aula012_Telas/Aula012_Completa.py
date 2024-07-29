# Introdução a telas no python

# utilizando bibliotecas

# mais usadas 
# pyQT - QTwidgetts 

import sys
from PyQt6.QtWidgets import * #pega tudo
# from pyQt6.Qtwidgets import QApplication, Qwidget # importar alguns especificos

def funcao_apertou():
    print('Voçe apertou-me 😳😳😳')
    txt1.setText("EITA 😨😨")
    txt1 = linha_de_texto.text()
    txt1.setText(txt1) #label

app  = QApplication(sys.argv)

janela = QWidget()
janela.resize(400,400) # (x, y)

txt1 = QLabel("Digite seu nome: ",janela) #texto e onde será inserido 
txt1.setGeometry(15,10,380,20) # 4 valores (x,y dps LARGURA e ALTURA)


### OPEN CSS 
with open('estil0.css','r') as file:
    app.setStyleSheet(file.read())

linha_de_texto = QLineEdit("",janela)
linha_de_texto.setGeometry(10,50,280,20)


botao = QPushButton('Não me aperte',janela)
botao.setGeometry(166,200,100,50) #(166 = X , 200 = Y , 80 = largura do botao , 50 = altura do botao)
botao.clicked.connect(funcao_apertou)


janela.show()
app.exec()






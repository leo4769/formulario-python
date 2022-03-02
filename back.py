from PyQt5 import uic, QtWidgets

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    linha4 = formulario.lineEdit_4.text()
    linha5 = formulario.lineEdit_5.text()
    linha6 = formulario.lineEdit_6.text()

    print('ID de Venda: ', linha1)
    print('Produto: ', linha2)
    print('Preço: ',linha3)
    print('Cliente: ', linha4)
    print('Quantidade: ', linha5)
    print('Data: ', linha6)

    if formulario.radioButton.isChecked():
        print('Categoria Eletrônicos')
    elif formulario.radioButton_2.ischecked():
        print('Categoria Informática')




app=QtWidgets.QApplication([])
formulario = uic.loadUi("formulário.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()



import sys
import os
from PyQt5.QtWidgets import QDialog, QApplication
from interfaz import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.rename01)
        self.show()
    def rename01(self):
        cant = self.ui.lineEdit.text()
        exten = self.ui.lineEdit_2.text()
        renom = self.ui.lineEdit_3.text()
        for nameinit in os.listdir("."):
            if nameinit[-1*int(cant):]==("."+str(exten)):
                nombre=nameinit[0:-1*int(cant):]
                newname=""
                newname=str(renom)+nombre+'.'+str(exten)
                os.rename(nameinit,newname)
        self.ui.textomensaje.setText("Se ha renombrado a los archivos")
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

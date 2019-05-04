from PyQt5.QtCore import QObject,pyqtSignal
from PyQt5.QtWidgets import *
import sys
class Winform(QWidget):
    button_clicked_signal=pyqtSignal(int)
    def __init__(self):
        super(Winform, self).__init__()
        self.setWindowTitle("信号槽实例")
        self.resize(400,100)
        btn=QPushButton('弹出',self)
        btn.clicked.connect(self.btn_clicked)
        self.button_clicked_signal.connect(self.message)

    def btn_clicked(self):
        self.button_clicked_signal.emit(4)

    def message(self,val):

        QMessageBox.information(self,'提示','sasas')

if __name__=='__main__':
    app=QApplication(sys.argv)
    win=Winform()
    win.show()
    sys.exit(app.exec_())
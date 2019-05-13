from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

# class myLabel(QLabel):
#     def mousePressEvent(self, evt):
#         self.setStyleSheet("background-color:red;")

class win(QWidget):
    def mousePressEvent(self, evt):
        my=self.childAt(evt.x(),evt.y())
        if my is not None:
            my.setStyleSheet("background-color:blue;")

app=QApplication(sys.argv)
window=win()
window.resize(500,500)
for i in range(1,10):
    label=QLabel(window)
    label.setText("标签"+str(i))
    label.move(30*i,30*i)

window.show()
sys.exit(app.exec_())
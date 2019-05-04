import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView,QHeaderView,QTableWidget,QHBoxLayout,QApplication,QTableWidgetItem,QWidget
class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("QTableWidget例子")
        self.resize(400,300)
        conLayout=QHBoxLayout()
        tableWidget=QTableWidget(4,3)
        tableWidget.horizontalHeader().setHidden(True)
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #tableWidget.setRowCount(4)
        #tableWidget.setColumnCount(3)
        conLayout.addWidget(tableWidget)
        tableWidget.setHorizontalHeaderLabels(['姓名11111111111111111111111','性别','体重'])
        list=[['张三','男','123'],['李四','男','150'],['王五','男','160']]
        for i in list:
            for j in i:
                newItem=QTableWidgetItem(j)
                newItem.setTextAlignment(Qt.AlignRight|Qt.AlignBottom)
                tableWidget.setItem(list.index(i),i.index(j),newItem)
        self.setLayout(conLayout)
if __name__=='__main__':
    app=QApplication(sys.argv)
    example=Table()
    example.show()
    sys.exit(app.exec_())
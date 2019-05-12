from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class win(QWidget):
    def __init__(self):
        super(win, self).__init__()
        self.pressstate=False
    def mousePressEvent(self,evt):
        self.pressstate=True
        self.point_x=evt.globalX()#获取鼠标点下时的全局坐标
        self.point_y=evt.globalY()
        #print(self.point_x,self.point_y)
        self.origin_x = self.x()#获取鼠标点下时的窗口原点的坐标
        self.origin_y = self.y()


    def mouseMoveEvent(self, evt):
        if self.pressstate==True:
            self.loaction_x=evt.globalX()
            self.loaction_y=evt.globalY()
            #print(self.loaction_x,self.loaction_y)
            length_x=self.loaction_x-self.point_x#计算移动距离
            length_y = self.loaction_y - self.point_y
            self.move(length_x+self.origin_x,length_y+self.origin_y)#原始点加上移动距离
            # print(length_x,length_y)
    def mouseReleaseEvent(self,evt):
        self.pressstate=False

app=QApplication(sys.argv)
window=win()
window.resize(500,500)
window.setWindowTitle("测试窗口")
window.setMaximumSize(1000,1000)
window.setMinimumSize(200,200)
window.setMouseTracking(True)
label=QLabel(window)
label.setText("我是一个标签")
label.move(100,100)
label.setStyleSheet("font-size:50PX;")
window.show()
sys.exit(app.exec_())
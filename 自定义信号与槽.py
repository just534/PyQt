from PyQt5.QtCore import QObject,pyqtSignal
class CustSignal(QObject):
    signal1=pyqtSignal()
    singnal2=pyqtSignal(int)
    singnal3=pyqtSignal([int,str],[str])

    def __init__(self):
        super(CustSignal, self).__init__()
        self.signal1.connect(self.singnalcall1)
        self.singnal2.connect(self.singnalcall2)
        self.singnal3[int,str].connect(self.signalcall3)
        self.singnal3[str].connect(self.signalcalleOverLoad)

        self.signal1.emit()
        self.singnal2.emit(3)
        self.singnal3[int,str].emit(4,"123")
        self.singnal3[str].emit("231321")

    def singnalcall1(self):
        print("signal1 emit")
    def singnalcall2(self,val):
        print("signal2 emit,value",val)
    def signalcall3(self,val,text):
        print("signal3 emit,value:",val,text)
    def signalcalleOverLoad(self,val):
        print("signal3OverLoad,value:",val)

if __name__=='__main__':
    custsignal=CustSignal()
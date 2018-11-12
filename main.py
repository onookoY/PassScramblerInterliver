import sys
from PyQt5.QtWidgets import QWidget, QApplication
from events import events

class MainWindow(events):
    def __init__(self, Form):
        self.setupUi(Form)
        self.connect()
    def connect(self):
        self.btnGo.pressed.connect(self.AllCalc)
        self.btnGenerate.pressed.connect(self.GeneratorPass)
        return(None)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()
    ui = MainWindow(widget)
    widget.show()

    sys.exit(app.exec_())

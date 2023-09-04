from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic

class MyGUI(QMainWindow):
    
    def __init__(self, parent=None):
        super(MyGUI, self).__init__()
        uic.loadUi('editor.ui', self)
        self.show()
        
        self.setWindowTitle("ElCruzo NotePad Clone")
        self.action12pt.triggered.connect(lambda: self.change_size(12))
        self.action18pt.triggered.connect(lambda: self.change_size(18))
        self.action24pt.triggered.connect(lambda: self.change_size(24))
    
    def change_size(self, size):
        self.plainTextEdit.setFont(QFont("Arial", size))
        
def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()
    
if __name__ == "__main__":
    main()
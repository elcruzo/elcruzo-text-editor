from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyGUI(QMainWindow):
    
    def __init__(self, parent=None):
        super(MyGUI, self).__init__()
        uic.loadUi('editor.ui', self)
        self.show()
        
        self.setWindowTitle("ElCruzo NotePad Clone")
        
def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()
    
if __name__ == "__main__":
    main()
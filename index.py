
from PyQt5.QtWidgets import *
import sys
import translator
from PyQt5.QtWidgets import QVBoxLayout,QGridLayout,QMainWindow,QApplication,QLabel,QWidget, QLineEdit
from PyQt5.QtCore import *

class MainProgram(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label1 = QLabel(self)
        self.label1.setText('<font size=10>Pig Latin Translator</font>')
        self.label1.adjustSize()
        self.label1.setAlignment(Qt.AlignCenter)
        
        self.label1.move(252, 10) 
        self.pl_input = QPlainTextEdit(self)
        self.pl_input.adjustSize()
        self.pl_input.resize(350, 150)
        self.pl_input.setPlaceholderText('Type your text in Pig Latin')
        self.pl_input.move(35, 100)

        
        self.translate_input = QPlainTextEdit(self)
        self.translate_input.adjustSize()
        self.translate_input.resize(350, 150)
        self.translate_input.setPlaceholderText('Here is will be translated text')
        self.translate_input.move(410, 100)
        self.translate_input.setReadOnly(True)

        self.translate_btn = QPushButton('Translate',self)
        self.translate_btn.adjustSize()
        self.translate_btn.resize(170, 70)        
        self.translate_btn.move(310, 275)

        self.footer = QLabel(self)
        self.footer.setText('<font size=4>&copy;Danila Emelyanov <a href="https://github.com/jezmunh/piglatin-translator">GitHub</a></font>')
        self.footer.adjustSize()
        self.footer.move(310, 470)

        self.translate_btn.clicked.connect(self.translate)
        vbox = QVBoxLayout()
        vbox.addWidget(self.pl_input)   
        vbox.addWidget(self.label1) 

        #self.setLayout(vbox)
        self.setWindowTitle('Pig Latin Translator')
        self.move(300, 300)
    def test(self):
        print(self.pl_input.toPlainText())
    def translate(self):
        try:
            rez = translator.TranslateText(self.pl_input.toPlainText())            
            self.translate_input.setPlainText(rez)
        except:
            self.msg = QMessageBox()
            self.msg.setText("Ooops...")
            self.msg.setInformativeText('Something went wrong...')
            self.msg.setWindowTitle("Error")
            self.msg.setIcon(QMessageBox.Critical)

            self.msg.exec_()

        
        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = MainProgram()   
    main.show()
    main.setFixedSize(800, 500)
    sys.exit(app.exec_())





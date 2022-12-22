import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QLineEdit, QLCDNumber, QDoubleSpinBox, QFormLayout, QGridLayout, QLineEdit, QAbstractSpinBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QKeySequence, QShortcut
from PyQt6 import QtGui, QtCore

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.container = QWidget()
        self.layout = QGridLayout()
        self.setFixedSize(300, 300)
        self.setWindowIcon(QIcon('Python\APL Tasks\calc.ico'))
        
        self.button1 = QPushButton("1")
        self.button2 = QPushButton("2")
        self.button3 = QPushButton("3")
        self.button4 = QPushButton("4")
        self.button5 = QPushButton("5")
        self.button6 = QPushButton("6")
        self.button7 = QPushButton("7")
        self.button8 = QPushButton("8")
        self.button9 = QPushButton("9")
        self.button0 = QPushButton("0")
        self.buttonDot = QPushButton(".")
        self.buttonSign = QPushButton("+/-")

        self.buttonEqual = QPushButton("=")
        self.plusButton = QPushButton("+")
        self.minusButton = QPushButton("-")
        self.multiplyButton = QPushButton("*")
        self.divideButton = QPushButton("/")
        
        self.modButton = QPushButton("%")
        self.clearAllButton = QPushButton("C")
        self.exponentButton = QPushButton("^")

        self.numInput = QLineEdit("")
        self.numInput.keyPressEvent = self.keyPressEvent

        self.setStyleSheet("QMainWindow{background: #F5F7FA}QApplication{background:rgba(76, 175, 80, 0.3)}QLineEdit{height:55px;font-size:36px;background-color:#fdfdfd!important;font-family:Segoe UI;border-radius:4px;border: 1px solid lightgrey}QPushButton::checked{background-color:black;color:white}QPushButton::hover{background-color:black;color:white;border-radius:3px}")

        self.layout.addWidget(self.numInput, 1, 0, 1, 5)

        self.layout.addWidget(self.exponentButton,2,0,1,1)
        self.layout.addWidget(self.clearAllButton,2,2,1,1)
        self.layout.addWidget(self.modButton,2,1,1,1)

        self.layout.addWidget(self.button7,3,0,1,1)
        self.layout.addWidget(self.button8,3,1,1,1)
        self.layout.addWidget(self.button9,3,2,1,1)
        self.layout.addWidget(self.button4,4,0,1,1)
        self.layout.addWidget(self.button5,4,1,1,1)
        self.layout.addWidget(self.button6,4,2,1,1)
        self.layout.addWidget(self.button1,5,0,1,1)
        self.layout.addWidget(self.button2,5,1,1,1)
        self.layout.addWidget(self.button3,5,2,1,1)
        self.layout.addWidget(self.button0,6,1,1,1)
        self.layout.addWidget(self.buttonDot,6,2,1,1)
        self.layout.addWidget(self.buttonSign,6,0,1,1)

        self.layout.addWidget(self.buttonEqual,6,4,1,1)
        self.layout.addWidget(self.plusButton,2,4,1,1)
        self.layout.addWidget(self.minusButton,3,4,1,1)
        self.layout.addWidget(self.multiplyButton,4,4,1,1)
        self.layout.addWidget(self.divideButton,5,4,1,1)

        self.button0.setCheckable(True)
        self.button1.setCheckable(True)
        self.button2.setCheckable(True)
        self.button3.setCheckable(True)
        self.button4.setCheckable(True)
        self.button5.setCheckable(True)
        self.button6.setCheckable(True)
        self.button7.setCheckable(True)
        self.button8.setCheckable(True)
        self.button9.setCheckable(True)
        self.buttonDot.setCheckable(True)
        self.buttonSign.setCheckable(True)
        
        self.plusButton.setCheckable(True)
        self.minusButton.setCheckable(True)
        self.multiplyButton.setCheckable(True)
        self.divideButton.setCheckable(True)
        self.plusButton.setCheckable(True)
        self.modButton.setCheckable(True)
        self.exponentButton.setCheckable(True)
        
        self.button0.clicked.connect(self.buttonClicked)
        self.button1.clicked.connect(self.buttonClicked)
        self.button2.clicked.connect(self.buttonClicked)
        self.button3.clicked.connect(self.buttonClicked)
        self.button4.clicked.connect(self.buttonClicked)
        self.button5.clicked.connect(self.buttonClicked)
        self.button6.clicked.connect(self.buttonClicked)
        self.button7.clicked.connect(self.buttonClicked)
        self.button8.clicked.connect(self.buttonClicked)
        self.button9.clicked.connect(self.buttonClicked)
        self.buttonDot.clicked.connect(self.buttonClicked)
        self.buttonSign.clicked.connect(self.buttonClicked)
        
        self.plusButton.clicked.connect(self.takeInput)
        self.minusButton.clicked.connect(self.takeInput)
        self.multiplyButton.clicked.connect(self.takeInput)
        self.divideButton.clicked.connect(self.takeInput)
        self.modButton.clicked.connect(self.takeInput)
        self.exponentButton.clicked.connect(self.takeInput)

        
        self.buttonEqual.clicked.connect(self.calculate)

        self.clearAllButton.clicked.connect(self.numInput.clear)
        
        # key=Qt.Key_Plus()
        # self.plusButton.setShortcut(QKeySequence.Key_Plus)
        # self.plusShortcut = QShortcut(QKeySequence("+"))
        # self.plusShortcut.activated.connect(self.plusButton.setChecked(True))
        
        self.setCentralWidget(self.container)
        self.container.setLayout(self.layout)
        
    def keyPressEvent(self, e):
        if e.text()  == "+":
            self.takeInput()
            self.plusButton.setChecked(True)
        elif e.text()  == "-":
            self.takeInput()
            self.minusButton.setChecked(True)
        elif e.text()  == "*":
            self.takeInput()
            self.multiplyButton.setChecked(True)
        elif e.text()  == "/":
            self.takeInput()
            self.divideButton.setChecked(True)
        elif e.text()  == "%":
            self.takeInput()
            self.modButton.setChecked(True)
        elif e.text()  == "^":
            self.takeInput()
            self.exponentButton.setChecked(True)
        elif e.text()  == "=":
            self.calculate()
        elif e.text() >="0" and e.text()<="9" or e.text()==".":
            prevStr = self.numInput.text()
            self.numInput.setText(prevStr+e.text())
    
    def buttonClicked(self):
        if(self.button0.isChecked()):
            self.check = 0
        elif(self.button1.isChecked()):
            self.check = 1
        elif(self.button2.isChecked()):
            self.check = 2
        elif(self.button3.isChecked()):
            self.check = 3
        elif(self.button4.isChecked()):
            self.check = 4
        elif(self.button5.isChecked()):
            self.check = 5
        elif(self.button6.isChecked()):
            self.check = 6
        elif(self.button7.isChecked()):
            self.check = 7
        elif(self.button8.isChecked()):
            self.check = 8
        elif(self.button9.isChecked()):
            self.check = 9
        elif(self.buttonDot.isChecked()):
            self.check = 10
        elif(self.buttonSign.isChecked()):
            self.check = 11

        if self.check == 0:
            prevStr = self.numInput.text()
            self.numInput.setText(prevStr+"0")
            self.button0.setChecked(False)
        elif self.check == 1:
            prevStr = self.numInput.text()
            self.numInput.setText(prevStr+"1")
            self.button1.setChecked(False)
        elif self.check == 2:
            prevStr = self.numInput.text()
            self.numInput.setText(prevStr+"2")
            self.button2.setChecked(False)
        elif self.check == 3:
            prevStr = self.numInput.text()
            self.numInput.setText(prevStr+"3")
            self.button3.setChecked(False)
        elif self.check == 4:
            prevStr = self.numInput.text()
            self.numInput.setText(prevStr+"4")
            self.button4.setChecked(False)
        elif self.check == 5:
            prevStr = self.numInput.text()
            self.numInput.setText(prevStr+"5")
            self.button5.setChecked(False)
        elif self.check == 6:
            prevStr = self.numInput.text()
            self.numInput.setText(prevStr+"6")
            self.button6.setChecked(False)
        elif self.check == 7:
            prevStr = self.numInput.text()
            self.numInput.setText(prevStr+"7")
            self.button7.setChecked(False)
        elif self.check == 8:
            prevStr = self.numInput.text()
            self.numInput.setText(prevStr+"8")
            self.button8.setChecked(False)
        elif self.check == 9:
            prevStr = self.numInput.text()
            self.numInput.setText(prevStr+"9")
            self.button9.setChecked(False)
        elif self.check == 10:
            prevStr = self.numInput.text()
            self.numInput.setText(prevStr+".")
            self.buttonDot.setChecked(False)
        elif self.check == 11:
            prevStr = self.numInput.text()
            self.numInput.setText("-"+prevStr)
            self.buttonSign.setChecked(False)

    def calculate(self):
        if(self.plusButton.isChecked()):
            self.value = 1
        elif(self.minusButton.isChecked()):
            self.value = 2
        elif(self.multiplyButton.isChecked()):
            self.value = 3
        elif(self.divideButton.isChecked()):
            self.value = 4
        elif(self.modButton.isChecked()):
            self.value = 5
        elif(self.exponentButton.isChecked()):
            self.value = 6
        self.num2 = float(self.numInput.text())
        answer = 0
        if self.value == 1:
            answer = self.num1+self.num2
            self.plusButton.setChecked(False)
        elif self.value == 2:
            answer = self.num1-self.num2
            self.minusButton.setChecked(False)
        elif self.value == 3:
            answer = self.num1*self.num2
            self.multiplyButton.setChecked(False)
        elif self.value == 4:
            answer = self.num1/self.num2
            self.divideButton.setChecked(False)
        elif self.value == 5:
            answer = self.num1%self.num2
            self.modButton.setChecked(False)
        elif self.value == 6:
            answer = pow(self.num1, self.num2)
            self.exponentButton.setChecked(False)
        self.numInput.setText(str(answer))
        
    def takeInput(self):
        self.num1 = float(self.numInput.text())
        self.numInput.clear()

# Main Code
app = QApplication(sys.argv)

window = MyMainWindow()
window.setWindowTitle("Calculator")
window.show()

app.exec()
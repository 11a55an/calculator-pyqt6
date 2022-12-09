import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QLineEdit, QSpinBox, QFormLayout

class MyMainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QFormLayout()

        self.plusButton = QPushButton("+")
        self.minusButton = QPushButton("-")
        self.multiplyButton = QPushButton("*")
        self.divideButton = QPushButton("/")
        self.modButton = QPushButton("%")

        self.num1Input = QSpinBox()
        self.num2Input = QSpinBox()

        self.num1Input.clear()
        self.num2Input.clear()

        self.label = QLabel("")

        self.layout.addRow("Enter 1st number: ", self.num1Input)
        self.layout.addRow("Enter 2nd number: ", self.num2Input)
        self.layout.addRow(self.label)
        self.layout.addRow(self.plusButton)
        self.layout.addRow(self.minusButton)
        self.layout.addRow(self.multiplyButton)
        self.layout.addRow(self.divideButton)
        self.layout.addRow(self.modButton)

        self.plusButton.clicked.connect(self.pButtonClicked)
        self.minusButton.clicked.connect(self.miButtonClicked)
        self.multiplyButton.clicked.connect(self.muButtonClicked)
        self.divideButton.clicked.connect(self.dButtonClicked)
        self.modButton.clicked.connect(self.moButtonClicked)
        self.setLayout(self.layout)
        
    def takeInput(self):
        self.num1 = int(self.num1Input.text())
        # self.numInput.clear()
        self.num2 = int(self.num2Input.text())

    def pButtonClicked(self):
        self.takeInput()
        sum = self.num1+self.num2 
        self.label.setText("Sum = "+ str(sum))

    def miButtonClicked(self):
        self.takeInput()
        minus = self.num1-self.num2 
        self.label.setText("Minus = "+ str(minus))

    def muButtonClicked(self):
        self.takeInput()
        multiply = self.num1*self.num2 
        self.label.setText("Multipliation = "+ str(multiply))

    def dButtonClicked(self):
        self.takeInput()
        div = self.num1/self.num2 
        self.label.setText("Division = "+ str(div))

    def moButtonClicked(self):
        self.takeInput()
        mod = self.num1%self.num2 
        self.label.setText("Mod = "+ str(mod))

# Main Code
app = QApplication(sys.argv)

window = MyMainWindow()
window.setWindowTitle("Calculator")
window.show()

app.exec()
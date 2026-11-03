import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel

#Class for main window
class MainWindow(QMainWindow):
    #Method for any core UI objects
    def __init__(self):
        super().__init__()
        #Window attributes
        self.setGeometry(100,100,1200,700)
        self.setWindowTitle("LimboVR")

        #Links any attributes from initUI method
        self.initUI()

    #Attributes for different UI components
    def initUI(self):
        #Sets central widget to allow for layouts
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        #Widgets
        label1 = QLabel("1", self)
        label2 = QLabel("2", self)
        label3 = QLabel("3", self)
        label4 = QLabel("4", self)
        label5 = QLabel("5", self)
        label6 = QLabel("6", self)
        label7 = QLabel("7", self)
        label8 = QLabel("8", self)

        camlabel = QLabel("Cam", self)



        label1.setStyleSheet("background-color: pink")
        label2.setStyleSheet("background-color: red")
        label3.setStyleSheet("background-color: orange")
        label4.setStyleSheet("background-color: yellow")
        label5.setStyleSheet("background-color: green")
        label6.setStyleSheet("background-color: turquoise")
        label7.setStyleSheet("background-color: blue")
        label8.setStyleSheet("background-color: purple")

        camlabel.setStyleSheet("background-color: white")

        #layout
        grid = QGridLayout()

        #Add widgets to grid
        grid.addWidget(label1, 1, 1)
        grid.addWidget(label2, 2, 2)
        grid.addWidget(label3, 3, 3)
        grid.addWidget(label4, 4, 4)
        grid.addWidget(label5, 5, 5)
        grid.addWidget(label6, 6, 6)
        grid.addWidget(label7, 7, 7)
        grid.addWidget(label8, 8, 8)
        grid.addWidget(camlabel, 1, 4, 5, 8)

        central_widget.setLayout(grid)

#Main function to make the UI work
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

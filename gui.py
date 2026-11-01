import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

#Class for main window
class MainWindow(QMainWindow):
    #Method for any core UI objects
    def __init__(self):
        super().__init__()
        #Window attributes
        self.setGeometry(100,100,700,550)
        self.setWindowTitle("LimboVR")

        #Links any attributes from initUI method
        self.initUI()

    #Attributes for different UI components
    def initUI(self):
        pass

#Main function to make the UI work
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
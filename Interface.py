import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QTextEdit, QAction, QDesktopWidget, QMainWindow
from PyQt5.QtGui import QIcon


class Downloader(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusbar = self.statusBar()
        self.statusBar().showMessage('Ready')

        self.resize(500, 200)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        self.setWindowTitle('Youtube Downloader')
        self.setWindowIcon(QIcon('download.png'))

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 60)
        self.textbox.resize(280, 40)

        exitAct = QAction('Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    d = Downloader()
    sys.exit(app.exec_())

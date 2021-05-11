import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QFileDialog, QLabel, QVBoxLayout, QHBoxLayout, \
    QGroupBox, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.data = None
        self.LBtxt = None

    def initUI(self):
        openAct = QAction(QIcon('open.png'), '&Open', self)
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('Open file dialog')
        openAct.triggered.connect(self.openFile)

        exitAct = QAction(QIcon('exit.jpg'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAct)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        self.LBtxt = QLabel("ESSAIS")
        self.GBstats = QGroupBox("Stats")
        self.GBdetails = QGroupBox("Détails")

        self.tableWidget = QTableWidget()

        layoutH = QHBoxLayout()
        layoutV = QVBoxLayout()

        layoutV.setContentsMargins(0, 0, 0, 0)

        widgetLstat = QWidget()
        widgetLstat.setLayout(layoutV)

        layoutV.addWidget(self.GBstats, 1)
        layoutV.addWidget(self.GBdetails, 1)

        layoutH.addWidget(self.tableWidget, 3)
        layoutH.addWidget(widgetLstat, 1)

        widget = QWidget()
        widget.setLayout(layoutH)

        self.setCentralWidget(widget)

        self.setGeometry(0, 0, 800, 800)
        self.setWindowTitle('Simple menu')
        self.show()

    def openFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;CSV File (*.csv)", options=options)
        if fileName:
            file = open(fileName, 'r')
            self.data = [i.split(";") for i in file.read().split("\n")]
            self.tableWidget.setRowCount(len(self.data))
            self.tableWidget.setColumnCount(len(self.data[0]))
            print(self.data)
            try:
                for numL, a in enumerate(self.data):
                    for numC, b in enumerate(self.data[numL]):
                        self.tableWidget.setItem(numL, numC, QTableWidgetItem(b))
            except Exception as e:
                print(e)


        return


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

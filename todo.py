from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(340, 406)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(340, 406))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/gmrab/OneDrive/Pictures/Golam_mostafa_rabby.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.Additem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Add_it())
        self.Additem_pushButton.setGeometry(QtCore.QRect(10, 50, 91, 31))
        self.Additem_pushButton.setObjectName("Additem_pushButton")
        
        self.Deleteitem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.Delete_it())
        self.Deleteitem_pushButton.setGeometry(QtCore.QRect(120, 50, 101, 31))
        self.Deleteitem_pushButton.setObjectName("Deleteitem_pushButton")
        
        self.Clearall_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.Clear_it())
        self.Clearall_pushButton.setGeometry(QtCore.QRect(240, 50, 91, 31))
        self.Clearall_pushButton.setObjectName("Clearall_pushButton")
        self.Additem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Additem_lineEdit.setGeometry(QtCore.QRect(12, 9, 321, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Additem_lineEdit.sizePolicy().hasHeightForWidth())
        self.Additem_lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Additem_lineEdit.setFocus()
        self.Additem_lineEdit.setFont(font)
        self.Additem_lineEdit.setObjectName("Additem_lineEdit")
        self.todo_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.todo_listWidget.setGeometry(QtCore.QRect(15, 91, 311, 231))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.todo_listWidget.sizePolicy().hasHeightForWidth())
        self.todo_listWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.todo_listWidget.setFont(font)
        self.todo_listWidget.setObjectName("todo_listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(20, 342, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    # Add item
    def Add_it(self):
        item = self.Additem_lineEdit.text()
        if (item.strip() !="" ):
            self.todo_listWidget.addItem(item)
            self.Additem_lineEdit.clear()

    # Delete item
    def Delete_it(self):
        clicked = self.todo_listWidget.currentRow()
        self.todo_listWidget.takeItem(clicked)
        
    # clear items
    def Clear_it(self):
        self.todo_listWidget.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do List"))
        self.Additem_pushButton.setText(_translate("MainWindow", "Add Item"))
        self.Deleteitem_pushButton.setText(_translate("MainWindow", "Delete Item"))
        self.Clearall_pushButton.setText(_translate("MainWindow", "Clear All"))
        self.label.setText(_translate("MainWindow", "Prepaid by Golam Mostafa Rabby"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

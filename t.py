# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 't.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 321)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(160, 68, 391, 22))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.txtpass = QtWidgets.QLineEdit(self.centralwidget)
        self.txtpass.setGeometry(QtCore.QRect(160, 100, 391, 20))
        self.txtpass.setObjectName("txtpass")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 70, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 47, 13))
        self.label_2.setObjectName("label_2")
        self.btnlog = QtWidgets.QPushButton(self.centralwidget)
        self.btnlog.setGeometry(QtCore.QRect(160, 130, 181, 41))
        self.btnlog.setObjectName("btnlog")
        self.lbldone = QtWidgets.QLabel(self.centralwidget)
        self.lbldone.setGeometry(QtCore.QRect(170, 210, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbldone.setFont(font)
        self.lbldone.setAlignment(QtCore.Qt.AlignCenter)
        self.lbldone.setObjectName("lbldone")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "username"))
        self.label_2.setText(_translate("MainWindow", "password"))
        self.btnlog.setText(_translate("MainWindow", "login"))
        self.lbldone.setText(_translate("MainWindow", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

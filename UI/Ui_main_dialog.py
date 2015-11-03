# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wulf/Program/HQ_food/UI/main_dialog.ui'
#
# Created: Tue Nov  3 09:05:54 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(538, 415)
        self.splitter = QtGui.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(10, 20, 381, 121))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.pushButton_1 = QtGui.QPushButton(self.splitter)
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.pushButton_2 = QtGui.QPushButton(self.splitter)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.splitter)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 20, 123, 121))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 350, 511, 51))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "超品豆腐", None))
        self.pushButton_1.setText(_translate("Dialog", "客戶設定", None))
        self.pushButton_2.setText(_translate("Dialog", "每日記賬", None))
        self.pushButton_3.setText(_translate("Dialog", "每月結算", None))
        self.pushButton_4.setText(_translate("Dialog", "技術分析", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


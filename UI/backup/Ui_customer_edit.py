# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wulf/HQfood/HQ_food/UI/customer_edit.ui'
#
# Created: Mon Sep 21 15:09:39 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from header import PRODUCT_NAME

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
        Dialog.resize(597, 380)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 581, 351))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.splitter = QtGui.QSplitter(self.tab_3)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 561, 301))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.textBrowser = QtGui.QTextBrowser(self.splitter)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.lineEdit_addguest = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_addguest.setObjectName(_fromUtf8("lineEdit_addguest"))
        self.horizontalLayout_6.addWidget(self.lineEdit_addguest)
        self.pushButton_addguest = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_addguest.setObjectName(_fromUtf8("pushButton_addguest"))
        self.horizontalLayout_6.addWidget(self.pushButton_addguest)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.layoutWidget1 = QtGui.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 10, 551, 291))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.comboBox_customer = QtGui.QComboBox(self.layoutWidget1)
        self.comboBox_customer.setObjectName(_fromUtf8("comboBox_customer"))
        self.horizontalLayout_2.addWidget(self.comboBox_customer)
        self.comboBox_version = QtGui.QComboBox(self.layoutWidget1)
        self.comboBox_version.setObjectName(_fromUtf8("comboBox_version"))
        self.horizontalLayout_2.addWidget(self.comboBox_version)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_1 = QtGui.QLabel(self.layoutWidget1)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.horizontalLayout.addWidget(self.label_1)
        self.dateEdit_from = QtGui.QDateEdit(self.layoutWidget1)
        self.dateEdit_from.setReadOnly(True)
        self.dateEdit_from.setDate(QtCore.QDate(2011, 11, 11))
        self.dateEdit_from.setObjectName(_fromUtf8("dateEdit_from"))
        self.horizontalLayout.addWidget(self.dateEdit_from)
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.dateEdit_to = QtGui.QDateEdit(self.layoutWidget1)
        self.dateEdit_to.setReadOnly(True)
        self.dateEdit_to.setDate(QtCore.QDate(2011, 11, 11))
        self.dateEdit_to.setObjectName(_fromUtf8("dateEdit_to"))
        self.horizontalLayout.addWidget(self.dateEdit_to)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_10 = QtGui.QLabel(self.layoutWidget1)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_3.addWidget(self.label_10)
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.layoutWidget1)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.layoutWidget1)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_3.addWidget(self.label_8)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_9 = QtGui.QLabel(self.layoutWidget1)
        self.label_9.setIndent(-1)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_4.addWidget(self.label_9)
        self.spinBox_big = QtGui.QSpinBox(self.layoutWidget1)
        self.spinBox_big.setReadOnly(True)
        self.spinBox_big.setMaximum(10000)
        self.spinBox_big.setObjectName(_fromUtf8("spinBox_big"))
        self.horizontalLayout_4.addWidget(self.spinBox_big)
        self.spinBox_small = QtGui.QSpinBox(self.layoutWidget1)
        self.spinBox_small.setReadOnly(True)
        self.spinBox_small.setMaximum(10000)
        self.spinBox_small.setObjectName(_fromUtf8("spinBox_small"))
        self.horizontalLayout_4.addWidget(self.spinBox_small)
        self.spinBox_oil = QtGui.QSpinBox(self.layoutWidget1)
        self.spinBox_oil.setReadOnly(True)
        self.spinBox_oil.setMaximum(10000)
        self.spinBox_oil.setObjectName(_fromUtf8("spinBox_oil"))
        self.horizontalLayout_4.addWidget(self.spinBox_oil)
        self.spinBox_tri = QtGui.QSpinBox(self.layoutWidget1)
        self.spinBox_tri.setReadOnly(True)
        self.spinBox_tri.setMaximum(10000)
        self.spinBox_tri.setObjectName(_fromUtf8("spinBox_tri"))
        self.horizontalLayout_4.addWidget(self.spinBox_tri)
        self.spinBox_stinky = QtGui.QSpinBox(self.layoutWidget1)
        self.spinBox_stinky.setReadOnly(True)
        self.spinBox_stinky.setMaximum(10000)
        self.spinBox_stinky.setObjectName(_fromUtf8("spinBox_stinky"))
        self.horizontalLayout_4.addWidget(self.spinBox_stinky)
        self.spinBox_milk = QtGui.QSpinBox(self.layoutWidget1)
        self.spinBox_milk.setObjectName(_fromUtf8("spinBox_milk"))
        self.horizontalLayout_4.addWidget(self.spinBox_milk)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButton_load = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_load.setEnabled(False)
        self.pushButton_load.setObjectName(_fromUtf8("pushButton_load"))
        self.horizontalLayout_5.addWidget(self.pushButton_load)
        self.pushButton_add = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.horizontalLayout_5.addWidget(self.pushButton_add)
        self.pushButton_edit = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_edit.setObjectName(_fromUtf8("pushButton_edit"))
        self.horizontalLayout_5.addWidget(self.pushButton_edit)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "客戶設定", None))
        self.label.setText(_translate("Dialog", "NOTE:新增資料重開視窗才會出現", None))
        self.pushButton_addguest.setText(_translate("Dialog", "新增", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "新增客戶", None))
        self.label_1.setText(_translate("Dialog", "起始:", None))
        self.dateEdit_from.setDisplayFormat(_translate("Dialog", "yyyy/MM/dd", None))
        self.label_2.setText(_translate("Dialog", "結束(2011/11/11=現在)", None))
        self.dateEdit_to.setDisplayFormat(_translate("Dialog", "yyyy/MM/dd", None))
        self.label_10.setText(_translate("Dialog", "項目", None))
        self.label_3.setText(_translate("Dialog", PRODUCT_NAME[0], None))
        self.label_4.setText(_translate("Dialog", PRODUCT_NAME[1], None))
        self.label_5.setText(_translate("Dialog", PRODUCT_NAME[2], None))
        self.label_6.setText(_translate("Dialog", PRODUCT_NAME[3], None))
        self.label_7.setText(_translate("Dialog", PRODUCT_NAME[4], None))
        self.label_8.setText(_translate("Dialog", PRODUCT_NAME[5], None))
        self.label_9.setText(_translate("Dialog", "$", None))
        self.pushButton_load.setText(_translate("Dialog", "讀取",  None))
        self.pushButton_add.setText(_translate("Dialog", "新增", None))
        self.pushButton_edit.setText(_translate("Dialog", "編輯", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "價格設定", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


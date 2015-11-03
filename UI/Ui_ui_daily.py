# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wulf/Program/HQ_food/UI/ui_daily.ui'
#
# Created: Tue Nov  3 09:05:52 2015
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

class Ui_Dialog_daily(object):
    def setupUi(self, Dialog_daily):
        Dialog_daily.setObjectName(_fromUtf8("Dialog_daily"))
        Dialog_daily.resize(465, 505)
        self.horizontalLayoutWidget_7 = QtGui.QWidget(Dialog_daily)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(11, 410, 441, 80))
        self.horizontalLayoutWidget_7.setObjectName(_fromUtf8("horizontalLayoutWidget_7"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.textEdit = QtGui.QTextEdit(self.horizontalLayoutWidget_7)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout_7.addWidget(self.textEdit)
        self.buttonBox = QtGui.QDialogButtonBox(self.horizontalLayoutWidget_7)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_7.addWidget(self.buttonBox)
        self.layoutWidget = QtGui.QWidget(Dialog_daily)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 29, 441, 371))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.combo_select = QtGui.QComboBox(self.layoutWidget)
        self.combo_select.setObjectName(_fromUtf8("combo_select"))
        self.horizontalLayout.addWidget(self.combo_select)
        self.dateEdit = QtGui.QDateEdit(self.layoutWidget)
        self.dateEdit.setReadOnly(True)
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout.addWidget(self.dateEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.spinBox_big = QtGui.QSpinBox(self.layoutWidget)
        self.spinBox_big.setObjectName(_fromUtf8("spinBox_big"))
        self.horizontalLayout_2.addWidget(self.spinBox_big)
        self.horizontalSlider_big = QtGui.QSlider(self.layoutWidget)
        self.horizontalSlider_big.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_big.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider_big.setObjectName(_fromUtf8("horizontalSlider_big"))
        self.horizontalLayout_2.addWidget(self.horizontalSlider_big)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.spinBox_small = QtGui.QSpinBox(self.layoutWidget)
        self.spinBox_small.setObjectName(_fromUtf8("spinBox_small"))
        self.horizontalLayout_3.addWidget(self.spinBox_small)
        self.horizontalSlider_small = QtGui.QSlider(self.layoutWidget)
        self.horizontalSlider_small.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_small.setObjectName(_fromUtf8("horizontalSlider_small"))
        self.horizontalLayout_3.addWidget(self.horizontalSlider_small)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.spinBox_oil = QtGui.QSpinBox(self.layoutWidget)
        self.spinBox_oil.setObjectName(_fromUtf8("spinBox_oil"))
        self.horizontalLayout_4.addWidget(self.spinBox_oil)
        self.horizontalSlider_oil = QtGui.QSlider(self.layoutWidget)
        self.horizontalSlider_oil.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_oil.setObjectName(_fromUtf8("horizontalSlider_oil"))
        self.horizontalLayout_4.addWidget(self.horizontalSlider_oil)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_5.addWidget(self.label_6)
        self.spinBox_tri = QtGui.QSpinBox(self.layoutWidget)
        self.spinBox_tri.setObjectName(_fromUtf8("spinBox_tri"))
        self.horizontalLayout_5.addWidget(self.spinBox_tri)
        self.horizontalSlider_tri = QtGui.QSlider(self.layoutWidget)
        self.horizontalSlider_tri.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_tri.setObjectName(_fromUtf8("horizontalSlider_tri"))
        self.horizontalLayout_5.addWidget(self.horizontalSlider_tri)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_6.addWidget(self.label_7)
        self.spinBox_stinky = QtGui.QSpinBox(self.layoutWidget)
        self.spinBox_stinky.setObjectName(_fromUtf8("spinBox_stinky"))
        self.horizontalLayout_6.addWidget(self.spinBox_stinky)
        self.horizontalSlider_stinky = QtGui.QSlider(self.layoutWidget)
        self.horizontalSlider_stinky.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_stinky.setObjectName(_fromUtf8("horizontalSlider_stinky"))
        self.horizontalLayout_6.addWidget(self.horizontalSlider_stinky)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_8.addWidget(self.label_8)
        self.spinBox_milk = QtGui.QSpinBox(self.layoutWidget)
        self.spinBox_milk.setObjectName(_fromUtf8("spinBox_milk"))
        self.horizontalLayout_8.addWidget(self.spinBox_milk)
        self.horizontalSlider_milk = QtGui.QSlider(self.layoutWidget)
        self.horizontalSlider_milk.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_milk.setObjectName(_fromUtf8("horizontalSlider_milk"))
        self.horizontalLayout_8.addWidget(self.horizontalSlider_milk)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.retranslateUi(Dialog_daily)
        QtCore.QMetaObject.connectSlotsByName(Dialog_daily)

    def retranslateUi(self, Dialog_daily):
        Dialog_daily.setWindowTitle(_translate("Dialog_daily", "每日銷售", None))
        self.dateEdit.setDisplayFormat(_translate("Dialog_daily", "yyyy/MM/dd", None))
        self.label_3.setText(_translate("Dialog_daily", "BIG", None))
        self.label_4.setText(_translate("Dialog_daily", "SMALL", None))
        self.label_5.setText(_translate("Dialog_daily", "OIL", None))
        self.label_6.setText(_translate("Dialog_daily", "TRI", None))
        self.label_7.setText(_translate("Dialog_daily", "STINKY", None))
        self.label_8.setText(_translate("Dialog_daily", "Milk", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_daily = QtGui.QDialog()
    ui = Ui_Dialog_daily()
    ui.setupUi(Dialog_daily)
    Dialog_daily.show()
    sys.exit(app.exec_())


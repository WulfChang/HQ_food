# -*- coding: utf-8 -*-

"""
Module implementing Dialog_main.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_main_dialog import Ui_Dialog

from ui_daily import Dialog_daily
from customer_edit import Dialog_cedit

from month_report import Dialog_report
from Ui_month_report import Ui_Dialog_report

class Dialog_main(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_pushButton_3_clicked(self):
        """
        Month report
        """
        ui_mon = Dialog_report()
        ui_mon.exec_()

    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        daily accounting
        """
        ui_day = Dialog_daily()
        ui_day.exec_()
    
    @pyqtSignature("")
    def on_pushButton_1_clicked(self):
        """
        customer edit
        """
        ui_edit = Dialog_cedit()
        
        if ui_edit != None:
            ui_edit.exec_()            
        else:
            print('Open customer edit failed!')
            


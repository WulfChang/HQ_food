# -*- coding: utf-8 -*-

"""
Module implementing Dialog_daily.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature, QDate

from Ui_ui_daily import Ui_Dialog_daily
from customer_file import Customer_list
from day_file import Dfile
from header import ERROR_MSG

class Dialog_daily(QDialog, Ui_Dialog_daily):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        #set today ( for file usage)
        self.qdate = QDate.currentDate()
        self.dateEdit.setDate( self.qdate )
    
        #declare customer list object
        try:
            self.cfile = Customer_list()
        except IOError as e:
            print('Error:' + str(e) )
            return None
        
        #read company list
        self.m_clist={}
        self.m_clist = self.cfile.readCompany()
        
        #set combo box
        self.setCombo(self.m_clist)
        
    def setCombo(self,  str):
        """
        set combo box
        """
        for i in str:
            self.combo_select.addItem(i)        
  
    def clearSpinbox(self,  value=0):
        """
        clear all spin box
        """
        
        self.spinBox_big.setValue(value)
        self.spinBox_small.setValue(value)
        self.spinBox_oil.setValue(value)
        self.spinBox_tri.setValue(value)
        self.spinBox_stinky.setValue(value)
        self.spinBox_milk.setValue(value)
        
    
    @pyqtSignature("")
    def on_buttonBox_accepted(self):
        """
        save data into file
        """
        i_year = self.qdate.year()
        i_month = self.qdate.month()
        i_name = self.cfile.readCvalue( str(self.combo_select.currentText().toUtf8()) )
        
        #declare Dfile object
        self.dfile = Dfile( i_year,  i_month,  i_name )
        
        #open file
        self.dfile.open_dfile()
        
        if self.dfile.checkRwrite( self.qdate.day() ) == True:
            
            #write ui data into file
            i_big = self.spinBox_big.value()
            i_small = self.spinBox_small.value()
            i_oil = self.spinBox_oil.value()
            i_tri = self.spinBox_tri.value()
            i_stinky = self.spinBox_stinky.value()
            i_milk = self.spinBox_milk.value()
        
            spindata = [ i_big,  i_small,  i_oil,  i_tri,  i_stinky, i_milk]
            self.dfile.write_dfile(spindata)
            
        else:
            self.textEdit.append( ERROR_MSG[0] )
            
        #close file
        self.dfile.close_dfile() 
        
    
    @pyqtSignature("")
    def on_buttonBox_rejected(self):
        """
        Clear all value to zero
        """
        self.clearSpinbox()
    
    @pyqtSignature("int")
    def on_horizontalSlider_big_valueChanged(self, value):
        """
        Synchronized with spinBox_big
        """
        self.spinBox_big.setValue(value)
    
    @pyqtSignature("int")
    def on_spinBox_big_valueChanged(self, p0):
        """
        Synchronized with Slider_big
        """
        self.horizontalSlider_big.setValue(p0)
    
    @pyqtSignature("int")
    def on_spinBox_small_valueChanged(self, p0):
        """
        Synchronized with Slider small
        """
        self.horizontalSlider_small.setValue(p0)
    
    @pyqtSignature("int")
    def on_horizontalSlider_small_valueChanged(self, value):
        """
        Synchronized with Spinbox small
        """
        self.spinBox_small.setValue(value)
    
    @pyqtSignature("int")
    def on_spinBox_oil_valueChanged(self, p0):
        """
        Synchronized with Slider oil
        """
        self.horizontalSlider_oil.setValue(p0)
    
    @pyqtSignature("int")
    def on_horizontalSlider_oil_valueChanged(self, value):
        """
        Synchronized with spinBox_oil
        """
        self.spinBox_oil.setValue(value)
    
    @pyqtSignature("int")
    def on_spinBox_tri_valueChanged(self, p0):
        """
        Synchronized with Slider tri
        """
        self.horizontalSlider_tri.setValue(p0)
    
    @pyqtSignature("int")
    def on_horizontalSlider_tri_valueChanged(self, value):
        """
        Synchronized with spinBox_tri
        """
        self.spinBox_tri.setValue(value)
    
    
    @pyqtSignature("int")
    def on_spinBox_stinky_valueChanged(self, p0):
        """
        Synchronized with Slider stinky
        """
        self.horizontalSlider_stinky.setValue(p0)
    
    @pyqtSignature("int")
    def on_horizontalSlider_stinky_valueChanged(self, value):
        """
        Synchronized with spinBox_stinky
        """
        self.spinBox_stinky.setValue(value)
    
    @pyqtSignature("int")
    def on_spinBox_milk_valueChanged(self, p0):
        """
        Synchronized with Slider milk
        """
        self.horizontalSlider_milk.setValue(p0)
    
    @pyqtSignature("int")
    def on_horizontalSlider_milk_valueChanged(self, value):
        """
        Synchronized with spinBox_milk
        """
        self.spinBox_milk.setValue(value)

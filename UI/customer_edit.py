# -*- coding: utf-8 -*-

"""
Module implementing Dialog_cedit.
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_customer_edit import Ui_Dialog

from customer_file import Customer_list
from customer_file import Customer_price


class Dialog_cedit(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        #set invisible
        self.pushButton_add.setVisible(False)
        
        #declare object
        try:
            self.clist = Customer_list()
        except IOError as e:
            print('Error:' + str(e) )
        
        self.cprice = Customer_price()
        
        #read company list
        self.m_clist={}
        self.m_clist = self.clist.readCompany()
        
        #set combo
        self.setCombo( 1,  self.m_clist )
        
        #set initial one
        self.comboBox_customer.setCurrentIndex(0)
        self.on_comboBox_customer_activated(0)
        
        #add customer to text browser
        self.setTextbrowser()
        
    def setTextbrowser(self):
        
        #show company list over text browser  
        for i in self.m_clist:
            self.textBrowser.append(i)
    
    @pyqtSignature("QString")
    def on_comboBox_customer_activated(self, p0):
        """
        set version combo box
        """
        #set to initial status
        self.setInitstatus()
        
        #read combo text and dict value
        self.str_customercombo = str( self.comboBox_customer.currentText().toUtf8() )
        self.i_customercombo = self.clist.readCvalue( self.str_customercombo )
        
        #get number of version file
        self.i_numversion = self.cprice.numGuestprice( self.i_customercombo )
    
        #iterate the version number
        i = 0
        m_version = []
        self.ultimateversion = 0
        while i <= self.i_numversion: 
            m_version.append('v'+str(i))
            self.ultimateversion = i
            i+=1

        #set combo box
        self.setCombo(2,  m_version)  
        
   
    @pyqtSignature("QString")
    def on_comboBox_version_activated(self, p0):
        """
        get version start and end date
        """
        #set to initial status
        self.setInitstatus()

        if self.comboBox_version.count != 0:
            #get selected version
            str_selectversion = self.comboBox_version.currentText()
            self.i_versioncombo = int( str_selectversion[1] )
            
            #set version date, if version equals 0, date shall be 20150101
            if self.i_versioncombo!=0:
                #get start date
                str_startdate = self.cprice.getStartdate( self.i_customercombo,  self.i_versioncombo )
                self.dateEdit_from.setDate( self.setQdate(str_startdate) )
            
                #get end date
                str_enddate = self.cprice.getEnddate( self.i_customercombo,  self.i_versioncombo )
                self.dateEdit_to.setDate( self.setQdate(str_enddate) )
                
                #enable pushButton
                self.pushButton_load.setEnabled(True)
            else:
                self.dateEdit_from.setDate( self.setQdate(self.cprice.INI_DATE) )
                self.dateEdit_to.setDate( self.setQdate(self.cprice.INI_DATE) )
   
    @pyqtSignature("")
    def on_pushButton_load_clicked(self):
        """
        load data into user interface
        """
        if self.pushButton_load.isEnabled():
            dict_loadprice = self.cprice.readPrice(  self.i_customercombo, self.i_versioncombo )
            
            #set spinbox value
            self.spinBox_big.setValue( dict_loadprice['big'] )
            self.spinBox_small.setValue( dict_loadprice['small'] )
            self.spinBox_oil.setValue( dict_loadprice['oil'] )
            self.spinBox_tri.setValue( dict_loadprice['tri'] )
            self.spinBox_stinky.setValue( dict_loadprice['stinky'] )
            self.spinBox_milk.setValue( dict_loadprice['milk'] )
        
    @pyqtSignature("")
    def on_pushButton_edit_clicked(self):
        """
        change to add mode
        """
        self.setMode('edit')
        
        #set next month 1st day
        if self.ultimateversion != 0:
            qdate = self.setNextmon( QDate.currentDate() )
            self.dateEdit_from.setDate( qdate )
            self.str_qdate = self.getStrdate( qdate )
        else:
            self.dateEdit_from.setDate( QDate.currentDate() )
            self.str_qdate = self.getStrdate( QDate.currentDate() )
        
        #set initial date
        self.dateEdit_to.setDate( self.setQdate(self.cprice.INI_DATE) )
    
    @pyqtSignature("")
    def on_pushButton_add_clicked(self):
        """
        dump value into yaml
        """  

        #dump ymal data
        self.cprice.writePrice(  self.i_customercombo, self.str_qdate ,  self.getSpinboxvalue()  )
        
        self.setMode('add')
    
        
    @pyqtSignature("")
    def on_pushButton_addguest_clicked(self):
        """
        add new customer to yaml list
        """
        if self.lineEdit_addguest.text() != '':
            str_name = str( self.lineEdit_addguest.text().toUtf8() )
            self.clist.writeCompany( str_name.decode('utf8') )       

        
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    self function
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def setInitstatus(self,  status = False):
        """
        set ui to initial status
        """
        #clear all button status
        self.clearSpinbox()
        self.pushButton_load.setEnabled(status)
        self.dateEdit_from.setDate( self.setQdate(self.cprice.INI_DATE) )
        self.dateEdit_to.setDate( self.setQdate(self.cprice.INI_DATE) )
        
    def setCombo(self, comboselect, m_str):
        """
        set combo box
        """
        if comboselect == 1:
            for i in m_str:
                self.comboBox_customer.addItem(i)
        elif comboselect == 2:
            self.comboBox_version.clear()
            for i in m_str:                
                self.comboBox_version.addItem(i)

    
    def setMode(self,  str_mode):
        
        """
        set different ui mode
        """
        #set status depends on edit or add mode
        b_status = True
        if str_mode == 'edit':
            b_status = True
        elif str_mode == 'add':
            b_status = False        

        self.clearSpinbox()
        self.pushButton_load.setEnabled(False)    
        self.setreadonlySpinbox(not b_status)
        self.pushButton_add.setVisible(b_status)
        self.pushButton_edit.setVisible(not b_status)
        self.comboBox_version.setEnabled(not b_status)
        self.comboBox_customer.setEnabled(not b_status)
    
    def getStrdate(self,  qdate):
        
        """
        convert qdate to strdate
        """
        #form a string date
        str_year = str(qdate.year())
        
        if qdate.month() < 10:
            str_month = '0'+ str(qdate.month())
        else: 
            str_month = str(qdate.month())
        
        if qdate.day() < 10:
            str_day = '0'+ str(qdate.day())
        else:
            str_day = str(qdate.day())

        return str_year + str_month + str_day    

    def setNextmon(self,  qdate ):
        """
        set import date as next month 1st
        """
        if qdate.month() == 12:
            qdate.setDate( qdate.year()+1,  1,  1)
        else:
            qdate.setDate( qdate.year(),  qdate.month()+1,  1)
            
        return qdate    
    
    def clearSpinbox(self):
        """
        clean all spin box as zero
        """
        self.spinBox_big.setValue( 0 )
        self.spinBox_small.setValue( 0 )
        self.spinBox_oil.setValue( 0 )
        self.spinBox_tri.setValue( 0 )
        self.spinBox_stinky.setValue( 0 )
        self.spinBox_milk.setValue( 0 )
        
    def getSpinboxvalue(self):
        
        """
        get all spin box value in a matrix
        """
        spinboxs_data = [ self.spinBox_big.value(), self.spinBox_small.value(),  self.spinBox_oil.value(), 
                                      self.spinBox_tri.value(), self.spinBox_stinky.value(),  self.spinBox_milk.value() ]
        
        return spinboxs_data
        
    def setreadonlySpinbox( self, status ):
        
        """
        set spin box as read only type
        """
        self.spinBox_big.setReadOnly(status)
        self.spinBox_small.setReadOnly(status)
        self.spinBox_oil.setReadOnly(status)
        self.spinBox_tri.setReadOnly(status)
        self.spinBox_stinky.setReadOnly(status)
        self.spinBox_milk.setReadOnly(status)         
           
            
    def setQdate(self,  str_date):
        """
         set str date (ex:20150201) to Qdate
        """
        i_year = int(str_date[0:4])
        i_month = int(str_date[4:6])
        i_day = int(str_date[6:9])
        
        return QDate(i_year,  i_month,  i_day)


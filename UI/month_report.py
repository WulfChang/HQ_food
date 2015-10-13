# -*- coding: utf-8 -*-

"""
Module implementing Dialog_report.
"""

from PyQt4.QtGui import QDialog, QVBoxLayout, QStandardItemModel
from PyQt4.QtCore import pyqtSignature,  Qt,  QVariant

from Ui_month_report import Ui_Dialog_report
from header import PRODUCT_NAME

from customer_file import Customer_list
from customer_file import Customer_price
from day_file import Dfile


class Dialog_report(QDialog, Ui_Dialog_report):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
                
        #construct Customer list class
        self.clist = Customer_list()        
                
        #construct accounting class
        self.caccount = Dfile()
        
        #construct customer price class
        self.cprice = Customer_price()
        
        #construct standard table
        self.tablemodel = QStandardItemModel(31,  len(PRODUCT_NAME) )
        self.setTableheader()

        #save customer list int
        self.list_customer = self.clist.readCompany()
        self.setCombo( 1,  self.list_customer )  
  
    def setMode(self, str_mode):
        
        if str_mode == 'init':
            self.clearAllshow()
            
    def setCombo(self, comboselect, m_str):
        """
        set combo box
        """
        if comboselect == 1:
            for i in m_str:
                self.comboBox_name.addItem(i)
        elif comboselect == 2:
            self.comboBox_date.clear()
            for i in m_str:                
                self.comboBox_date.addItem(i)
                
    
    def clearAllshow(self):
        
        #clear all spin box 
        self.setAllspin(0)
        
        #clear table
        self.clearTableview()
        
    def setAllspin(self,  int_value):
         self.spinBox_1.setValue(int_value)
         self.spinBox_2.setValue(int_value)
         self.spinBox_3.setValue(int_value)
         self.spinBox_4.setValue(int_value)
         self.spinBox_5.setValue(int_value)
         self.spinBox_6.setValue(int_value)
         self.spinBox_7.setValue(int_value)
         self.spinBox_8.setValue(int_value)
         self.spinBox_9.setValue(int_value)
         self.spinBox_10.setValue(int_value)
         self.spinBox_11.setValue(int_value)
         self.spinBox_12.setValue(int_value)
         self.spinBox_13.setValue(int_value)
         self.spinBox_14.setValue(int_value)
         self.spinBox_15.setValue(int_value)
         self.spinBox_16.setValue(int_value)
         self.spinBox_17.setValue(int_value)
         self.spinBox_18.setValue(int_value)
         self.spinBox_19.setValue(int_value)
         self.spinBox_19.setValue(0)
         
    def setTableheader(self):
                
        #set header data
        self.tablemodel.setHeaderData(0, Qt.Horizontal, PRODUCT_NAME[0] )
        self.tablemodel.setHeaderData(1, Qt.Horizontal, PRODUCT_NAME[1] )
        self.tablemodel.setHeaderData(2, Qt.Horizontal, PRODUCT_NAME[2] )
        self.tablemodel.setHeaderData(3, Qt.Horizontal, PRODUCT_NAME[3] )
        self.tablemodel.setHeaderData(4, Qt.Horizontal, PRODUCT_NAME[4] )
        self.tablemodel.setHeaderData(5, Qt.Horizontal, PRODUCT_NAME[5] )
        
    def setTableview(self,  dlist_data ):
        """
        set data into tableview model
        """
        #show data
        row = 0
        for i in dlist_data:
            self.tablemodel.setData(self.tablemodel.index(row, 0), QVariant(i[0]))
            self.tablemodel.setData(self.tablemodel.index(row, 1), QVariant(i[1]))
            self.tablemodel.setData(self.tablemodel.index(row, 2), QVariant(i[2]))
            self.tablemodel.setData(self.tablemodel.index(row, 3), QVariant(i[3]))
            self.tablemodel.setData(self.tablemodel.index(row, 4), QVariant(i[4]))
            self.tablemodel.setData(self.tablemodel.index(row, 5), QVariant(i[5]))
            row += 1
        
        #set table into tableview
        self.tableView.setModel(self.tablemodel)
        
    def clearTableview(self):
        """
        clear table
        """
        #show data
        row = 0
        i = [0, 0, 0, 0, 0, 0]
        for row in range(31):
            self.tablemodel.setData(self.tablemodel.index(row, 0), QVariant(i[0]))
            self.tablemodel.setData(self.tablemodel.index(row, 1), QVariant(i[1]))
            self.tablemodel.setData(self.tablemodel.index(row, 2), QVariant(i[2]))
            self.tablemodel.setData(self.tablemodel.index(row, 3), QVariant(i[3]))
            self.tablemodel.setData(self.tablemodel.index(row, 4), QVariant(i[4]))
            self.tablemodel.setData(self.tablemodel.index(row, 5), QVariant(i[5]))
        
        #set table into tableview
        self.tableView.setModel(self.tablemodel)
    
    @pyqtSignature("QString")
    def on_comboBox_name_currentIndexChanged(self, p0):
        """
        when name index change, set combo date
        """
        #set to initial status
        self.setMode('init')
        
        #read combo text and dict value
        self.str_customercombo = str( self.comboBox_name.currentText().toUtf8() )
        self.i_customercombo = self.clist.readCvalue( self.str_customercombo )
        
        #read all guest accounting data
        self.list_date = self.caccount.listDatafile( self.i_customercombo )
        
        self.setCombo(2, self.list_date)
    
    @pyqtSignature("QString")
    def on_comboBox_date_currentIndexChanged(self, p0):
        """
        search price data and load accounting into table
        """
        
        self.str_filename = str( self.comboBox_date.currentText() )
        
        if self.str_filename != '':
            self.str_datecombo = self.str_filename[3:9]
        
            #get price version
            self.i_priceversion = self.cprice.selectPrice( self.i_customercombo, self.str_datecombo )
            
            #get price dict
            dict_price = self.cprice.readPrice( self.i_customercombo, self.i_priceversion )
            self.list_price = self.cprice.getClist( dict_price )
            
            #show price 
            self.setPricespin( self.list_price )
            
            #show table
            self.caccount.open_dfile( self.str_filename )
            self.table_data = self.caccount.read_alldfile()
            self.setTableview( self.table_data )
            
            #calculate and show single amount
            self.eachamount = self.sumEachamount( self.table_data )
            self.setEachamount( self.eachamount )
            
            #calculate single price amount
            self.eachpriceamount = [ self.eachamount[i]*self.list_price[i] for i in range(len(PRODUCT_NAME))]
            self.setEachpriceamount( self.eachpriceamount )
            
            #show in total income
            self.spinBox_19.setValue( sum(self.eachpriceamount ) )
            
            
    def setPricespin( self,  list ):
        
         self.spinBox_1.setValue( list[0] )
         self.spinBox_2.setValue( list[1] )
         self.spinBox_3.setValue( list[2] )
         self.spinBox_4.setValue( list[3] )
         self.spinBox_5.setValue( list[4] )
         self.spinBox_6.setValue( list[5] )
    
    def setEachamount( self,  list ):
        
         self.spinBox_7.setValue( list[0] )
         self.spinBox_8.setValue( list[1] )
         self.spinBox_9.setValue( list[2] )
         self.spinBox_10.setValue( list[3] )
         self.spinBox_11.setValue( list[4] )
         self.spinBox_12.setValue( list[5] )
         
    def setEachpriceamount(self,  list ):
        
         self.spinBox_13.setValue( list[0] )
         self.spinBox_14.setValue( list[1] )
         self.spinBox_15.setValue( list[2] )
         self.spinBox_16.setValue( list[3] )
         self.spinBox_17.setValue( list[4] )
         self.spinBox_18.setValue( list[5] )
    
    #sum each item total amount
    def sumEachamount(self,  duallist ):
        
        eachamount = [0, 0, 0, 0, 0, 0]
        count = 0
        for i in duallist:
            for j in i:
                eachamount[count] += j
                count += 1
            count = 0
            
        return eachamount
        
        

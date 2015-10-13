# encoding: utf-8

import xlwt
from datetime import datetime

import header

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Function: write daily work status in log file, currently, the version only save the latest log
Author: Wulf Chang
Version: v1.1
History: 2015/10/05 programming start
             2015/10/06 beta release v1.1

----------------------------------------------------------------------------------------------------------------------------
Example of using xlwt:

        style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
        num_format_str='#,##0.00')
        style1 = xlwt.easyxf(num_format_str='HH:MM:SS')

        wb = xlwt.Workbook()
        ws = wb.add_sheet('A Test Sheet')

        ws.write(0, 0, 1234.56, style0)
        ws.write(1, 0, datetime.now(), style1)
        ws.write(2, 0, 1)
        ws.write(2, 1, 1)
        ws.write(2, 2, xlwt.Formula("A3+B3"))

        wb.save('example.xls')
        
        #show today
        a=datetime.today()
        a.strftime("%Y%m%d")
----------------------------------------------------------------------------------------------------------------------------

             
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

log_path = header.HQ_LOG_PATH
log_name = header.HQ_LOG_NAME

class LogIO:
    
    """"
    Initialize the class
    para: string
    return null
    """
    def __init__( self ):
        
        #set filename
        self.openLogsheet()

        #set time stamp style
        self.setTstamp()

        #declare a count for evaluating number of row
        self.count = 0

    """"
    start the log sheet, if it's existed, overwrite is made
    para: string
    return none
    """    
    def openLogsheet(self): 
        
        #set current sheet name
        self.setSheetname()
        
        #creat workbook and sheet
        self.wb = xlwt.Workbook()
        self.ws = self.wb.add_sheet( self.s_logfilename,  True )
    
    """"
    End the file by write into file
    para: none
    return none
    """
    def writeLogfile( self ):
        self.wb = self.wb.save( log_path+log_name )
     
    """"
    set time stamp style
    para: none
    return none
    """
    def setTstamp(self):
        self.timestamp = xlwt.easyxf(num_format_str='HH:MM:SS')
    
    """"
    set file name by taking date
    para: none
    return none
    """
    def setSheetname(self):
        t_current = datetime.today()
        self.s_logfilename = t_current.strftime("%Y%m%d") + '_' + 'log'
    
    """"
    save msg and time into sheet
    para: string, string
    return none
    """
    def writeLog( self,  s_event_msg,  s_type ):
        
        #ex: 13:55:27  |   the file has been open  |  normal
        #save timestamp in the first column
        self.ws.write( self.count, 0, datetime.now(), self.timestamp)
        self.ws.write( self.count, 1, s_event_msg)
        self.ws.write( self.count, 2, s_type)
        
        #iterate to next row
        self.count +=1
        
    



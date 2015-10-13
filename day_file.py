
import os.path
import fnmatch

#header module
import header

"""
Function: save daily data into file
Author: Wulf Chang
History: 2015/09/15 releasing
             2015/10/05 beta version ready
"""

DF_path = header.HQ_ACCOUNT_PATH

class Dfile:
    #initialize function
    def __init__( self, year=0, month=0, name=0, num_of_date=31 ):
        self.year = year
        self.month = month
        self.name = name
        self.num_of_date = num_of_date
    
    #open daily file
    def open_dfile( self,  str_fname ='' ):         
   
        #open file
        if str_fname == '':
            if self.month >= 10:
                self.fname = DF_path +'HQ' + '_' + str(self.year) +  str(self.month) + '_' + str(self.name)
            else:
                self.fname = DF_path +'HQ' + '_' + str(self.year) + '0'+ str(self.month) + '_' + str(self.name)
        else:
            self.fname = DF_path + str_fname
            
        self.fptr =  open( self.fname, 'a+' )
    
    #check file overflow status
    def overflow_dfile( self ):

        lines = self.count_dfile()         
        return True if lines < self.num_of_date else False
    
    #write data into daily file
    def write_dfile( self, datalist=[] ):        
        if  self.overflow_dfile() == True:
            for i in datalist:
                self.fptr.write( str(i) + '\t' )
            self.fptr.write('\n')
            return True
        else:
            print 'dfile overflow'
            return False
    
    #read specific line in daily file: return matrix
    def read_dfile( self,  lines ):
        array =[]
        count=0
        if lines <= self.count_dfile():
            for line in self.fptr:
                count+=1
                if count == lines:
                    line = line.strip()
                    array = map(int, line.split() )
                    return array
        else:
            print 'the input lines is over total lines'
            
    def read_alldfile(self):
        
        data = []
        array =[]
        count=0
    
        for line in self.fptr:
            line = line.strip()
            array = map(int, line.split() )
            data.append( array )

        return data

    #count  daily file
    def count_dfile(self):
       count=0
             
       if os.path.exists( self.fname ):
            for line in self.fptr:
               count+=1           
            self.fptr.seek(0, 0)
            
       return count
       
    #check repetitive write
    def checkRwrite(self,  day):
        if self.count_dfile() < day:
            return True
        else:
            return False
    
    #close daily file
    def close_dfile(self):
        self.fptr.close()
        
    #read all file and return list of 
    def listDatafile( self, i_guestnum ):
        
           #search accounting data
           list_num_file = fnmatch.filter(os.listdir(DF_path), '*_'+ str(i_guestnum) )
           
           #sort date from new to old
           list_date = sorted(list_num_file, reverse=True)
           return list_date

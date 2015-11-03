
import yaml
import os
import fnmatch

#header module
import header

"""
Function: edit customer file,  customer_list.yaml,  guestX.yaml
Author: Wulf Chang
History: 2015/09/11 programming start
             2015/10/05 beta version ready
             2015/11/02 add Customer_list class raise error
"""

HQ_path = header.HQ_PATH
HQ_price = header.HQ_PRICE_PATH
HQ_list = header.HQ_LIST_NAME

"""
Edit the list of customer, the list is saved in "HQ_path+HQ_list" with yaml format
"""
class Customer_list():
    
        """
        open file and load yaml, which is a company list
        """        
        def __init__(self):            
            if os.path.exists( HQ_path+HQ_list ):
                #fptr open
                self.list_str = open( HQ_path+HQ_list,  'a+')
                #load file
                self.clist = yaml.load( self.list_str )
               #convert to dict type 
                self.__getCdict( self.clist )
            else:
                #file opening error
                raise IOError(header.ERROR_MSG[0])
                
        """
        write company into yaml list
        """
        def writeCompany(self,  name):            
            if name:                    
                #write data into yaml
                current_num = self.__numCompany()+1
                data = [{name: current_num}]
                yaml.dump(data,  self.list_str)
                
                #add to dict
                self.__addCdict(data)
            else:
                raise ValueError(header.ERROR_MSG[1])
                
        """
        read keys of company
        """    
        def readCompany(self):
            return self.cdict.keys()  
        
        """
        read key of company from input name string
        """
        def readCvalue(self, name):
            name = name.decode('utf8')
            return self.cdict[name]
        
        """
        convert to UTF8
        """
        def __cvtUTF8(self,  str):
            str_temp = str.encode('utf8')                
            return str_temp
        
        """
        convert list to dict
        """
        def __getCdict(self, clist):
            #declare
            self.cdict = {}
            
            if clist != []:
                #convert clist(matrix) to cdict(dictionary)
                for i in clist:
                    self.cdict.update( i )           
            
            return self.cdict
        
        """
        count number of company in the dict
        """    
        def __numCompany(self):
            return len(self.cdict)

        """
        add data to cdict
        """
        def __addCdict(self, data):
            self.cdict.update(data[0])        
 
"""
load customer setting price from guest number and version
(the guest number is defined in customer list file)
"""        
class Customer_price():
        
        """
        Initialization
        """
        def __init__(self):
            #assign the version non valid date
            self.INI_DATE = header.NONVALID
            
        """    
        obtain number of version 
        """
        def numGuestprice(self,  i_guestnum):
            str_num_file = fnmatch.filter(os.listdir(HQ_price), '*_'+ str(i_guestnum)+'.yaml')
            num_file = len(str_num_file)
            return num_file
        """
        get start date of specific version
        """
        def getStartdate(self,  i_guestnum, i_version):            
            str_filename = self.__getFilename(  i_guestnum, i_version )
            
            if str_filename:
                return str_filename[3:11]
            else:
                raise NameError(header.ERROR_MSG[2])
        
        """ 
        get end date of specifict version
        """
        def getEnddate(self,  i_guestnum, i_version):            
            str_filename = self.__getFilename(  i_guestnum, i_version )
            
            if str_filename:
                return str_filename[12:20]
            else:
                raise NameError(header.ERROR_MSG[2])
            
        """    
        write price into file, which is totally new
        """
        def writePrice(self,  i_guestnum, str_nowdate,  m_data ):            
            #read current version
            current_version = self.numGuestprice( i_guestnum )
            
            #end current version price file
            if current_version != 0:                
                self.endFile( i_guestnum,  current_version, str_nowdate  )
            
            #set newest version    
            newversion = current_version+1
            
            #form filename
            str_version_filename = self.__formNewfilename( str_nowdate, newversion, i_guestnum )
            
            #write into file
            with open(  str_version_filename,  'w+' ) as fprt_price:         
                data = [{'big': m_data[0]},  {'small': m_data[1]}, {'oil': m_data[2]},  {'tri': m_data[3]},  {'stinky': m_data[4]},  {'milk': m_data[5]}]
                yaml.dump(data,  fprt_price)
        
        """    
        read price from file
        """        
        def readPrice(self,  i_guestnum,  i_version):
            
            self.dict_price = {}
            
            #get full file name
            str_fullname = self.__getFilename(  i_guestnum,  i_version )
            
            #open file and covnert list to dict
            with open( HQ_price+str_fullname,  'r') as fptr_file:
                m_price = yaml.load( fptr_file )            
                self.dict_price = self.__getCdict( m_price )
            
            if self.dict_price:  
                return self.dict_price
            else:
                raise  IOError(header.ERROR_MSG[0])
        
        """
        convert dict to list
        """
        def getClist(self,  cdict):
            return [ cdict['big'],  cdict['small'],  cdict['oil'],  cdict['tri'],  cdict['stinky'],  cdict['milk'] ]    

        """    
        terminate the price file, namely, add end date in the file name
        """
        def endFile(self,  i_guestnum, i_version,  end_date):
            
            #current file name and current fiel end date
            current_fname = self.__getFilename(i_guestnum, i_version)
               
            #rename
            os.rename( HQ_price+current_fname,  HQ_price+current_fname.replace( self.INI_DATE,  end_date))
            
        """    
        select setting price and return its  version
        """
        def selectPrice( self,  i_guestnum, str_accountdate ):
            
            #count total file number
            i_pricenumber = self.numGuestprice(i_guestnum)
            
            if i_pricenumber == 0:
                raise IOError(header.ERROR_MSG[0])
            else:
                #search from latest version
                while i_pricenumber > 0:
                    #get start date
                    str_stardate = self.getStartdate( i_guestnum, i_pricenumber )
                    
                    if str_accountdate >= str_stardate[0:6]:
                        return i_pricenumber                    
                    
                    #search previous one version
                    i_pricenumber -=1
                    
                raise IOError(header.ERROR_MSG[0])
                        
        """
        convert clist(matrix) to cdict(dictionary)
        """
        def __getCdict(self, clist):            
            self.cdict = {}
            for i in clist:
                self.cdict.update(i)                
            return self.cdict
                        
        """        
        establish new file name
        """   
        def __formNewfilename(self,  str_nowdate,  i_newversion,  i_guestnum):
            
            str_nfilename =  HQ_price + 'HQ_'+ str_nowdate+'_' + self.INI_DATE +'_v'+str(i_newversion)+'_'+str(i_guestnum)+'.yaml'
            return str_nfilename
            
                        
        """
        get full file name   
        """
        def __getFilename(self,  i_guestnum, i_version ):
            #search file
            part_name = '*v' + str(i_version)+'_'+str(i_guestnum)+'.yaml'
            filename = fnmatch.filter(os.listdir(HQ_price), part_name)
            str_filename = filename[0]
            
            return str_filename

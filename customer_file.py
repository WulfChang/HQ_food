
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
"""

HQ_path = header.HQ_PATH
HQ_price = header.HQ_PRICE_PATH
HQ_list = header.HQ_LIST_NAME


class Customer_list():
        def __init__(self):            
            if os.path.exists( HQ_path+HQ_list ):
                #fptr open
                self.list_str = open( HQ_path+HQ_list,  'a+')
                #load file
                self.clist = yaml.load( self.list_str )
               #convert to dict type 
                self.getCdict( self.clist )
            else:
                raise IOError('customer list file does not exist!')
                
        def cvtUTF8(self,  str):
            str_temp = str.encode('utf8')                
            return str_temp
        
        def getCdict(self, clist):            
            #convert clist(matrix) to cdict(dictionary)
            self.cdict = {}
            for i in clist:
                self.cdict.update( i )           
            return self.cdict
    
        def readCompany(self):
            return self.cdict.keys()
            
        def readCvalue(self, name):
            name = name.decode('utf8')
            return self.cdict[name]
            
        def numCompany(self):
            return len(self.cdict)
            
        def writeCompany(self,  name):
            #write data into yaml
            current_num = self.numCompany()+1
            data = [{name: current_num}]
            yaml.dump(data,  self.list_str)
            
            #add to dict
            self.addCdict(data)
            
        def addCdict(self, data):
            self.cdict.update(data[0])
            
        def closeCfile(self):
            self.list_str.close()
        
        
        
class Customer_price():
        
        INI_DATE = header.NONVALID
        
        def __init__(self):
            print 'init'
            
        #obtain number of version 
        def numGuestprice(self,  i_guestnum):
            str_num_file = fnmatch.filter(os.listdir(HQ_price), '*_'+ str(i_guestnum)+'.yaml')
            num_file = len(str_num_file)
            return num_file
        
        #get start date of specific version
        def getStartdate(self,  i_guestnum, i_version):
            
            str_filename = self.getFilename(  i_guestnum, i_version )            
            return str_filename[3:11]
         
        #get end date of specifict version
        def getEnddate(self,  i_guestnum, i_version):
            
            str_filename = self.getFilename(  i_guestnum, i_version )           
            return str_filename[12:20]
       
        #establish new file name   
        def formNewfilename(self,  str_nowdate,  i_newversion,  i_guestnum):
            
            str_nfilename =  HQ_price + 'HQ_'+ str_nowdate+'_' + self.INI_DATE +'_v'+str(i_newversion)+'_'+str(i_guestnum)+'.yaml'
            return str_nfilename
            
        #write price into file, which is totally new
        def writePrice(self,  i_guestnum, str_nowdate,  m_data ):
            
            #read current version
            current_version = self.numGuestprice( i_guestnum )
            
            if current_version != 0:
                #end current version price file
                self.endFile( i_guestnum,  current_version, str_nowdate  )
                
            newversion = current_version+1
            
            #form filename
            str_version_filename = self.formNewfilename( str_nowdate, newversion, i_guestnum )
            fprt_price = open(  str_version_filename,  'w+' )
            
            #write into file
            data = [{'big': m_data[0]},  {'small': m_data[1]}, {'oil': m_data[2]},  {'tri': m_data[3]},  {'stinky': m_data[4]},  {'milk': m_data[5]}]
            yaml.dump(data,  fprt_price)
        
        #get full file name   
        def getFilename(self,  i_guestnum, i_version ):
            #search file
            part_name = '*v' + str(i_version)+'_'+str(i_guestnum)+'.yaml'
            filename = fnmatch.filter(os.listdir(HQ_price), part_name)
            str_filename = filename[0]
            
            return str_filename
            
        def readPrice(self,  i_guestnum,  i_version):
            #get full file name
            str_fullname = self.getFilename(  i_guestnum,  i_version )
            
            #open file
            fptr_file = open( HQ_price+str_fullname,  'r')
            m_price = yaml.load( fptr_file )
            
            #convert list to dict
            self.dict_price = self.getCdict( m_price )
            
            return self.dict_price

        def getCdict(self, clist):            
            #convert clist(matrix) to cdict(dictionary)
            self.cdict = {}
            for i in clist:
                self.cdict.update(i)                
            return self.cdict
           
        def getClist(self,  cdict):
            return [ cdict['big'],  cdict['small'],  cdict['oil'],  cdict['tri'],  cdict['stinky'],  cdict['milk'] ]
            
        #terminate the price file, namely, add end date in the file name
        def endFile(self,  i_guestnum, i_version,  end_date):
            
            #current file name and current fiel end date
            current_fname = self.getFilename(i_guestnum, i_version)
               
            #rename
            os.rename( HQ_price+current_fname,  HQ_price+current_fname.replace( self.INI_DATE,  end_date))
            
        #select setting price and return its  version
        def selectPrice( self,  i_guestnum, str_accountdate ):
            
            #count total file number
            i_pricenumber = self.numGuestprice(i_guestnum)
            
            if i_pricenumber == 0:
                print 'No price setting file!'
                return 0
            else:
                #search from latest version
                while i_pricenumber > 0:
                    #get start date
                    str_stardate = self.getStartdate( i_guestnum, i_pricenumber )
                    
                    if str_accountdate >= str_stardate[0:6]:
                        return i_pricenumber                    
                    
                    #search previous one version
                    i_pricenumber -=1
                    
                print 'please check price setting file'
                return 0
            

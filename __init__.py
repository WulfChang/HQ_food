
#from PyQt4 import QtCore, QtGui
import PyQt4

from UI.main_dialog import Dialog_main

    
def main():
    app = PyQt4.QtGui.QApplication(sys.argv)
    ui = Dialog_main()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
   import sys
   main()    

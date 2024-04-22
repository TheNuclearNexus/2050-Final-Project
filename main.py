import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from PYQTCreatorRecipeUI import Ui_main_window

def main():

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
    
main()
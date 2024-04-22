import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from PYQTCreatorRecipeUI import Ui_main_window
from RecipeUI import RecipeUI

def main():

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = RecipeUI()
    ui.show()
    sys.exit(app.exec_())
    
main()
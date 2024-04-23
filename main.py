import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from RecipeUI import RecipeUI

def main():

    app = QtWidgets.QApplication(sys.argv)
    ui = RecipeUI()
    ui.show()
    sys.exit(app.exec_())
    
main()
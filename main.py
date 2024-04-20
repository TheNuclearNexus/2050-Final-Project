import sys
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import QIcon

from RecipeUI import RecipeUI

def main():
    app = QApplication(sys.argv)
    gui = RecipeUI()
    gui.show()
    sys.exit(app.exec_())
    
main()
import sys
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import QIcon

class RecipeUI(QMainWindow):
    #initalizes variables such as window height, width, and calls setup_window() to set up the window
    def __init__(self):
        super(RecipeUI, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Example Window")
        # note that some systems like macOS will not show the icon on the window
        self.setWindowIcon(QIcon('my_ui_icon.png'))
        self.window()

    # sets up the window and assigns a window title
    def setup_window():
        
        return 0

    # takes in a list of recipe objects and displays them using a GridLayout as shown in the image -> more info at PDF
    def layout_ui(recipes):
        return 0

    # called when the user clicks the next button. 
    def next():
        return 0

    def previous():
        return 0

    def first():
        return 0

    def last():
        return 0

    def search(recipe_keywords):
        return 0

    # clears the search results and returns to normal pagination of the list of recipes
    def reset():
        return 0



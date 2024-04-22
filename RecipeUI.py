import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

from Recipe import Recipe
from RecipeProcessor import RecipeProcessor
from RecipeDetails import RecipeDetails
recipes = RecipeProcessor()
recipes.load_recipes("recipes.json")


class RecipeUI(QMainWindow,QWidget):
    def __init__(self, parent=None):
        self.current_page = 0
        self.recipes_per_page = 4
        super(RecipeUI, self).__init__(parent)
        self.setup_window()


    def setup_window(self):
        # Set up the main window and layout
        self.setWindowTitle("Team 15 Recipe Viewer")
        self.setGeometry(100, 60, 1000, 800)
        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Add search bar and buttons at the top
        search_layout = QHBoxLayout()
        self.search_bar = QLineEdit()
        search_button = QPushButton('Search')
        reset_button = QPushButton('Reset')
        # Connect buttons to their functions...
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(search_button)
        search_layout.addWidget(reset_button)

        # search_button.clicked.connect(self.search(self, recipe_keywords))
        reset_button.clicked.connect(self.reset)

        # Create a grid layout for recipes
        # self.recipe_grid = QGridLayout()
        self.recipe_grid = self.layout_ui(recipes)







        # Add navigation buttons at the bottom
        navigation_layout = QHBoxLayout()
        first_button = QPushButton('First')
        previous_button = QPushButton('Previous')
        next_button = QPushButton('Next')
        last_button = QPushButton('Last')

        
        
        # Connect buttons to their functions...
        navigation_layout.addWidget(first_button)
        navigation_layout.addWidget(previous_button)
        navigation_layout.addWidget(next_button)
        navigation_layout.addWidget(last_button)

        first_button.clicked.connect(self.first)
        previous_button.clicked.connect(self.previous)
        next_button.clicked.connect(self.next)
        last_button.clicked.connect(self.last)
        # Combine all layouts into the main layout
        main_layout.addLayout(search_layout)
        main_layout.addLayout(self.recipe_grid)
        main_layout.addLayout(navigation_layout)

    def layout_ui(self, recipes):
        
        recipes = recipes.get_recipes()
        self.max_num = len(recipes)
        # Setup the grid layout
        grid_layout = QGridLayout()

        # Create and add recipe cards to the grid layout
        for i in range(4*self.current_page-1,4*self.current_page+3):
            if i > self.max_num:
                return grid_layout
            else:


                recipe_widget = QWidget()
                recipe_layout = QVBoxLayout(recipe_widget)

                image_label = QLabel()
                pixmap = QPixmap(recipes[i].get_image()) 
                image_label.setPixmap(pixmap.scaled(200, 180, Qt.KeepAspectRatio))
                recipe_layout.addWidget(image_label)
        
                recipe_number_label = QLabel(f'Recipe #: {i+2}')
                recipe_name_label = QLabel(f'Recipe Name: {recipes[i].get_name()}')  # Update with actual recipe name
                prep_time_label = QLabel(f'Prep Time: {recipes[i].get_prep_time()}')  # Update with actual prep time
                cook_time_label = QLabel(f'Cook Time: {recipes[i].get_cook_time()}')  # Update with actual cook time
                view_recipe_button = QPushButton('View Recipe')
                # Optional: Connect view_recipe_button to a function to handle button click
                
                # Add labels and button to the recipe layout
                recipe_layout.addWidget(recipe_number_label)
                recipe_layout.addWidget(recipe_name_label)
                recipe_layout.addWidget(prep_time_label)
                recipe_layout.addWidget(cook_time_label)
                recipe_layout.addWidget(view_recipe_button)
                
                # view_recipe_button.clicked.connect(self.show_recipe(i))

                grid_layout.addWidget(recipe_widget, (i+1) // 2, (i+1) % 2)  # 2 columns grid

        # Set the grid layout to the main window
        self.setLayout(grid_layout)

        return grid_layout

    
    def next(self):
        
        if self.current_page == self.max_num:
            return
        else:
            self.current_page = self.current_page + 1
            self.setup_window()
       

    def previous(self):
        
        if self.current_page == 0:
            pass
        else:
            self.current_page = self.current_page - 1
            self.setup_window()
        

    def first(self):
        self.current_page = 0
        self.setup_window()


    def last(self):
        
        max_page = (self.max_num - 1)//4
        if self.current_page == max_page:
            pass
        self.current_page = max_page
        self.setup_window()

    def show_recipe(self, index: int):
        details = RecipeDetails()
        details.setupUi(details)
        details.set_recipe(recipes.get_recipes()[index], index + 1)
        details.exec()

    def search(self, recipe_keywords):
        
        pass

    def reset(self):
        pass


# Entry point of the application
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = RecipeUI()
    window.show()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

from Recipe import Recipe
from RecipeProcessor import RecipeProcessor
from RecipeDetails import RecipeDetails
recipes_processor = RecipeProcessor()
recipes_processor.load_recipes("recipes.json")
recipe_num = recipes_processor.get_recipe_num()


class RecipeUI(QMainWindow,QWidget):
    def __init__(self, parent=None):
        self.current_index = 0
        self.recipes_per_page = 4
        super(RecipeUI, self).__init__(parent)
        self.recipes = recipes_processor.get_recipes()
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
 
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(search_button)
        search_layout.addWidget(reset_button)

        search_button.clicked.connect(self.clicked_search)
        reset_button.clicked.connect(self.reset)

        # Create a grid
        self.recipe_grid = self.layout_ui(self.recipes)

        # Add navigation buttons at the bottom
        navigation_layout = QHBoxLayout()
        first_button = QPushButton('First')
        previous_button = QPushButton('Previous')
        next_button = QPushButton('Next')
        last_button = QPushButton('Last')

        # Add display label
        display_label = QLabel(f"Displaying {self.current_index + 1}-{min(self.current_index + 4, len(self.recipes))} of {len(self.recipes)} recipes")
        display_label.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        display_label.setStyleSheet("background-color: #ddd; padding: 6px;")
        displaying_layout = QHBoxLayout()
        displaying_layout.addWidget(display_label)
        
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
        main_layout.addLayout(search_layout, stretch=0)
        main_layout.addLayout(self.recipe_grid, stretch=10)
        main_layout.addLayout(navigation_layout, stretch=0)
        main_layout.addWidget(display_label, stretch=0)

    def layout_ui(self, recipes):

        self.max_num = len(recipes)
        # Setup the grid layout
        grid_layout = QGridLayout()
        
        # Create and add recipe cards to the grid layout
        for i in range(0,4):
            if i >= len(recipes):
                recipe_widget = QWidget()
                grid_layout.addWidget(recipe_widget, i // 2, i % 2) 
            elif i > self.max_num:
                return grid_layout
            else:
                index = self.current_index + i

                recipe_widget = QWidget()
                recipe_layout = QVBoxLayout(recipe_widget)

                image_label = QLabel()
                pixmap = QPixmap(recipes[index].get_image()) 
                image_label.setPixmap(pixmap.scaled(200, 180, Qt.KeepAspectRatio))
                recipe_layout.addWidget(image_label)
        
                recipe_number_label = QLabel(f'Recipe #: {index + 1}')
                recipe_name_label = QLabel(f'Recipe Name: {recipes[index].get_name()}')  # Update with actual recipe name
                prep_time_label = QLabel(f'Prep Time: {recipes[index].get_prep_time()}')  # Update with actual prep time
                cook_time_label = QLabel(f'Cook Time: {recipes[index].get_cook_time()}')  # Update with actual cook time
                view_recipe_button = QPushButton('View Recipe')
                # Optional: Connect view_recipe_button to a function to handle button click
                
                # Add labels and button to the recipe layout
                recipe_layout.addWidget(recipe_number_label)
                recipe_layout.addWidget(recipe_name_label)
                recipe_layout.addWidget(prep_time_label)
                recipe_layout.addWidget(cook_time_label)
                recipe_layout.addWidget(view_recipe_button)

                # The code is working not as I intentioned!!!!
                
                if i % 4 == 0:
                    view_recipe_button.clicked.connect(lambda _ : self.show_recipe(self.current_index))
                elif i % 4 == 1:
                    view_recipe_button.clicked.connect(lambda _ : self.show_recipe(self.current_index + 1))
                elif i % 4 == 2:
                    view_recipe_button.clicked.connect(lambda _ : self.show_recipe(self.current_index + 2))
                elif i % 4 == 3:
                    view_recipe_button.clicked.connect(lambda _ : self.show_recipe(self.current_index + 3))

                grid_layout.addWidget(recipe_widget, i // 2, i % 2)  # 2 columns grid

        # Set the grid layout to the main window
        if self.layout() == None:
            self.setLayout(grid_layout)

        return grid_layout

    def next(self):
        
        if self.current_index >= len(self.recipes)-4:
            return
        else:
            self.current_index = self.current_index + 4
            self.setup_window()
       

    def previous(self):
        
        if self.current_index < 4:
            self.current_index = 0
        else:
            self.current_index = self.current_index - 4
        
        self.setup_window()
        

    def first(self):
        self.current_index = 0
        self.setup_window()


    def last(self):
        
        self.current_index = len(self.recipes)-4
        if self.current_index < 0:
            self.current_index = 0
        
        self.setup_window()

    def show_recipe(self, index: int):
        details = RecipeDetails()
        details.set_recipe(self.recipes[index], index + 1)
        details.exec()

    def clicked_search(self):
        
        search_text = self.search_bar.text()
        self.search(search_text)
        
    def get_all_info(self, recipe: Recipe):
        all_to_string = " ".join([
            recipe.get_name(),
            recipe.get_description(), 
            recipe.get_recipe_yield(),
            " ".join(recipe.get_ingredients())
        ])
        
        all_to_string = all_to_string.lower()
        return all_to_string

    def search(self, recipe_keywords):
        
        found_recipe = []

        search_text = recipe_keywords.lower()
        recipes = recipes_processor.get_recipes()

        for recipe in recipes: 
            word = self.get_all_info(recipe)
            if search_text in word:
                found_recipe.append(recipe)

        print(found_recipe)

        self.current_index=0
        self.recipes = found_recipe
        self.setup_window()


    

    def reset(self):
        self.current_index=0
        self.recipes = recipes_processor.get_recipes()
        self.setup_window()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = RecipeUI()
    window.show()
    sys.exit(app.exec_())

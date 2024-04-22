# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipe_detailshjOinb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

from Recipe import Recipe
from RecipeProcessor import RecipeProcessor


class RecipeDetails(QDialog):
    def __init__(self):
        super().__init__()

        self.layout = None
        self.height = 700
        self.width = 500

        self.setup()

    def setup(self):
        self.setWindowTitle("Recipe Details")
        self.setGeometry(100, 100, self.width, self.height)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.recipe_image = QLabel()
        self.recipe_image.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        
        image_layout = QHBoxLayout()
        image_layout.addWidget(self.recipe_image, alignment=Qt.AlignmentFlag.AlignCenter)
        
    
        self.recipe_info = QGridLayout()
        self.recipe_info.setColumnStretch(0, 0)
        self.recipe_info.setColumnStretch(1, 10)
        self.setup_recipe_info(self.recipe_info)

        group = QGroupBox()
        group.setLayout(self.recipe_info)

        info_scroll_area = QScrollArea()
        info_scroll_area.setWidget(group)
        info_scroll_area.setWidgetResizable(True)


        self.layout.addLayout(image_layout, stretch=0)
        self.layout.addWidget(info_scroll_area, stretch=10)

    def make_labels(
        self, grid: QGridLayout, row: int, labelText: str, valueText: str
    ) -> tuple[QLabel, QLabel]:
        label = QLabel()
        label.setText(labelText)
        label.setSizePolicy(QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum, ))
        value = QLabel()
        value.setText(valueText)

        grid.addWidget(label, row, 0)
        grid.addWidget(value, row, 1)

        return (label, value)

    def setup_recipe_info(self, grid: QGridLayout):
        self.recipe_number = self.make_labels(grid, 1, "Recipe Number:", "0")

        self.recipe_name = self.make_labels(grid, 2, "Recipe Name:", "Recipe Name")

        self.recipe_cook_time = self.make_labels(grid, 3, "Cook Time:", "00:00")

        self.recipe_prep_time = self.make_labels(grid, 4, "Prep Time:", "00:00")

        self.recipe_description = self.make_labels(
            grid, 5, "Description:", "Longgggg desciptionnnnnnnnnnnnnnnnnnnnnn"
        )
        self.recipe_description[1].setWordWrap(True)

        self.recipe_ingredients = self.make_labels(
            grid, 6, "Ingredients:", "1\n2\n3\n4\n5"
        )
        self.recipe_ingredients[1].setWordWrap(True)

    def set_recipe(self, recipe: Recipe, recipe_number: int):
        self.recipe_image.setPixmap(QPixmap(recipe.get_image()).scaledToHeight(300))

        self.recipe_number[1].setText(str(recipe_number))
        self.recipe_name[1].setText(recipe.get_name())
        self.recipe_cook_time[1].setText(recipe.get_cook_time())
        self.recipe_prep_time[1].setText(recipe.get_prep_time())
        self.recipe_description[1].setText(recipe.get_description())
        self.recipe_ingredients[1].setText("\n".join(recipe.ingredients))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    processor = RecipeProcessor()
    processor.load_recipes("recipes.json")
    details = RecipeDetails()
    details.set_recipe(processor.get_recipes()[0], 1)
    details.exec()

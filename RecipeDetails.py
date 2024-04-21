# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipe_detailshjOinb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Recipe import Recipe


class RecipeDetails(QDialog):
    def setupUi(self, RecipeDetails):
        if not RecipeDetails.objectName():
            RecipeDetails.setObjectName(u"RecipeDetails")
        RecipeDetails.resize(471, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RecipeDetails.sizePolicy().hasHeightForWidth())
        RecipeDetails.setSizePolicy(sizePolicy)
        RecipeDetails.setMaximumSize(QSize(16777215, 700))
        RecipeDetails.setSizeGripEnabled(False)
        self.scrollArea_2 = QScrollArea(RecipeDetails)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(10, 10, 451, 681))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy1)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 449, 679))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy2)
        self.verticalLayoutWidget = QWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 490, 584))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.image_box = QLabel(self.verticalLayoutWidget)
        self.image_box.setObjectName(u"image_box")
        self.image_box.setPixmap(QPixmap(u"images/asparagussoup_83241_16x9.jpg"))

        self.verticalLayout.addWidget(self.image_box)

        self.recipe_1 = QGridLayout()
        self.recipe_1.setObjectName(u"recipe_1")
        self.recipe_prep_time = QLabel(self.verticalLayoutWidget)
        self.recipe_prep_time.setObjectName(u"recipe_prep_time")

        self.recipe_1.addWidget(self.recipe_prep_time, 2, 1, 1, 1)

        self.recipe_cook_time = QLabel(self.verticalLayoutWidget)
        self.recipe_cook_time.setObjectName(u"recipe_cook_time")

        self.recipe_1.addWidget(self.recipe_cook_time, 3, 1, 1, 1)

        self.recipe_ingredients = QLabel(self.verticalLayoutWidget)
        self.recipe_ingredients.setObjectName(u"recipe_ingredients")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.recipe_ingredients.sizePolicy().hasHeightForWidth())
        self.recipe_ingredients.setSizePolicy(sizePolicy3)

        self.recipe_1.addWidget(self.recipe_ingredients, 6, 1, 1, 1)

        self.recipe_number = QLabel(self.verticalLayoutWidget)
        self.recipe_number.setObjectName(u"recipe_number")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.recipe_number.sizePolicy().hasHeightForWidth())
        self.recipe_number.setSizePolicy(sizePolicy4)

        self.recipe_1.addWidget(self.recipe_number, 0, 1, 1, 1)

        self.first_recipe_0_0 = QLabel(self.verticalLayoutWidget)
        self.first_recipe_0_0.setObjectName(u"first_recipe_0_0")
        sizePolicy3.setHeightForWidth(self.first_recipe_0_0.sizePolicy().hasHeightForWidth())
        self.first_recipe_0_0.setSizePolicy(sizePolicy3)

        self.recipe_1.addWidget(self.first_recipe_0_0, 0, 0, 1, 1)

        self.first_recipe_3_2 = QLabel(self.verticalLayoutWidget)
        self.first_recipe_3_2.setObjectName(u"first_recipe_3_2")
        sizePolicy3.setHeightForWidth(self.first_recipe_3_2.sizePolicy().hasHeightForWidth())
        self.first_recipe_3_2.setSizePolicy(sizePolicy3)

        self.recipe_1.addWidget(self.first_recipe_3_2, 6, 0, 1, 1)

        self.first_recipe_3_5 = QLabel(self.verticalLayoutWidget)
        self.first_recipe_3_5.setObjectName(u"first_recipe_3_5")
        sizePolicy3.setHeightForWidth(self.first_recipe_3_5.sizePolicy().hasHeightForWidth())
        self.first_recipe_3_5.setSizePolicy(sizePolicy3)

        self.recipe_1.addWidget(self.first_recipe_3_5, 5, 0, 1, 1)

        self.first_recipe_2_0 = QLabel(self.verticalLayoutWidget)
        self.first_recipe_2_0.setObjectName(u"first_recipe_2_0")
        sizePolicy3.setHeightForWidth(self.first_recipe_2_0.sizePolicy().hasHeightForWidth())
        self.first_recipe_2_0.setSizePolicy(sizePolicy3)

        self.recipe_1.addWidget(self.first_recipe_2_0, 2, 0, 1, 1)

        self.first_recipe_1_0 = QLabel(self.verticalLayoutWidget)
        self.first_recipe_1_0.setObjectName(u"first_recipe_1_0")
        sizePolicy3.setHeightForWidth(self.first_recipe_1_0.sizePolicy().hasHeightForWidth())
        self.first_recipe_1_0.setSizePolicy(sizePolicy3)

        self.recipe_1.addWidget(self.first_recipe_1_0, 1, 0, 1, 1)

        self.first_recipe_3_0 = QLabel(self.verticalLayoutWidget)
        self.first_recipe_3_0.setObjectName(u"first_recipe_3_0")
        sizePolicy3.setHeightForWidth(self.first_recipe_3_0.sizePolicy().hasHeightForWidth())
        self.first_recipe_3_0.setSizePolicy(sizePolicy3)

        self.recipe_1.addWidget(self.first_recipe_3_0, 3, 0, 1, 1)

        self.recipe_name = QLabel(self.verticalLayoutWidget)
        self.recipe_name.setObjectName(u"recipe_name")

        self.recipe_1.addWidget(self.recipe_name, 1, 1, 1, 1)

        self.recipe_description = QLabel(self.verticalLayoutWidget)
        self.recipe_description.setObjectName(u"recipe_description")

        self.recipe_1.addWidget(self.recipe_description, 5, 1, 1, 1)


        self.verticalLayout.addLayout(self.recipe_1)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(RecipeDetails)

        QMetaObject.connectSlotsByName(RecipeDetails)
    # setupUi

    def retranslateUi(self, RecipeDetails):
        RecipeDetails.setWindowTitle(QCoreApplication.translate("RecipeDetails", u"Recipe Details", None))
        self.image_box.setText("")
        self.recipe_prep_time.setText(QCoreApplication.translate("RecipeDetails", u"TextLabel", None))
        self.recipe_cook_time.setText(QCoreApplication.translate("RecipeDetails", u"TextLabel", None))
        self.recipe_ingredients.setText("")
        self.recipe_number.setText(QCoreApplication.translate("RecipeDetails", u"TextLabel", None))
        self.first_recipe_0_0.setText(QCoreApplication.translate("RecipeDetails", u"Recipe #:", None))
        self.first_recipe_3_2.setText(QCoreApplication.translate("RecipeDetails", u"Ingredients", None))
        self.first_recipe_3_5.setText(QCoreApplication.translate("RecipeDetails", u"Description:", None))
        self.first_recipe_2_0.setText(QCoreApplication.translate("RecipeDetails", u"Prep Time:", None))
        self.first_recipe_1_0.setText(QCoreApplication.translate("RecipeDetails", u"Recipe Name:", None))
        self.first_recipe_3_0.setText(QCoreApplication.translate("RecipeDetails", u"Cook Time:", None))
        self.recipe_name.setText(QCoreApplication.translate("RecipeDetails", u"TextLabel", None))
        self.recipe_description.setText(QCoreApplication.translate("RecipeDetails", u"TextLabel", None))
    # retranslateUi


    def set_recipe(self, recipe: Recipe, recipe_number: int):
        self.recipe_number.setText(str(recipe_number))
        self.recipe_name.setText(recipe.get_name())
        self.recipe_cook_time.setText(recipe.get_cook_time())
        self.recipe_prep_time.setText(recipe.get_prep_time())
        self.recipe_description.setText(recipe.get_description())
        self.recipe_ingredients.setText("\n".join(recipe.ingredients))


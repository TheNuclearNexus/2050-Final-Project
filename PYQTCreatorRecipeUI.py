# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(642, 737)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 40, 641, 171))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.recipie_row_0 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.recipie_row_0.setContentsMargins(0, 0, 0, 0)
        self.recipie_row_0.setObjectName("recipie_row_0")
        self.recepie_1_pic = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.recepie_1_pic.setScaledContents(True)
        self.recepie_1_pic.setObjectName("recepie_1_pic")
        self.recipie_row_0.addWidget(self.recepie_1_pic)
        self.recepie_2_pic = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.recepie_2_pic.setScaledContents(True)
        self.recepie_2_pic.setObjectName("recepie_2_pic")
        self.recipie_row_0.addWidget(self.recepie_2_pic)
        self.recepie_3_pic = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.recepie_3_pic.setScaledContents(True)
        self.recepie_3_pic.setObjectName("recepie_3_pic")
        self.recipie_row_0.addWidget(self.recepie_3_pic)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 350, 641, 171))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.recipie_row_1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.recipie_row_1.setContentsMargins(0, 0, 0, 0)
        self.recipie_row_1.setObjectName("recipie_row_1")
        self.recepie_4_pic = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.recepie_4_pic.setScaledContents(True)
        self.recepie_4_pic.setObjectName("recepie_4_pic")
        self.recipie_row_1.addWidget(self.recepie_4_pic)
        self.recepie_6_pic = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.recepie_6_pic.setScaledContents(True)
        self.recepie_6_pic.setObjectName("recepie_6_pic")
        self.recipie_row_1.addWidget(self.recepie_6_pic)
        self.recepie_5_pic = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.recepie_5_pic.setScaledContents(True)
        self.recepie_5_pic.setObjectName("recepie_5_pic")
        self.recipie_row_1.addWidget(self.recepie_5_pic)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(140, 660, 499, 32))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.browse_button = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.browse_button.setContentsMargins(0, 0, 0, 0)
        self.browse_button.setObjectName("browse_button")
        self.previous_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.previous_button.setObjectName("previous_button")
        self.browse_button.addWidget(self.previous_button)
        self.first_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.first_button.setObjectName("first_button")
        self.browse_button.addWidget(self.first_button)
        self.last_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.last_button.setObjectName("last_button")
        self.browse_button.addWidget(self.last_button)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton.setObjectName("pushButton")
        self.browse_button.addWidget(self.pushButton)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 220, 160, 94))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.recipe_1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.recipe_1.setContentsMargins(0, 0, 0, 0)
        self.recipe_1.setObjectName("recipe_1")
        self.first_recipe_3_0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.first_recipe_3_0.setObjectName("first_recipe_3_0")
        self.recipe_1.addWidget(self.first_recipe_3_0, 3, 0, 1, 1)
        self.first_recipe_0_0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.first_recipe_0_0.setObjectName("first_recipe_0_0")
        self.recipe_1.addWidget(self.first_recipe_0_0, 0, 0, 1, 1)
        self.first_recipe_2_0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.first_recipe_2_0.setObjectName("first_recipe_2_0")
        self.recipe_1.addWidget(self.first_recipe_2_0, 2, 0, 1, 1)
        self.first_recipe_1_0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.first_recipe_1_0.setObjectName("first_recipe_1_0")
        self.recipe_1.addWidget(self.first_recipe_1_0, 1, 0, 1, 1)
        self.first_recipe_1_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.first_recipe_1_1.setObjectName("first_recipe_1_1")
        self.recipe_1.addWidget(self.first_recipe_1_1, 1, 1, 1, 1)
        self.first_recipe_0_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.first_recipe_0_1.setObjectName("first_recipe_0_1")
        self.recipe_1.addWidget(self.first_recipe_0_1, 0, 1, 1, 1)
        self.first_recipe_2_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.first_recipe_2_1.setObjectName("first_recipe_2_1")
        self.recipe_1.addWidget(self.first_recipe_2_1, 2, 1, 1, 1)
        self.first_recipe_3_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.first_recipe_3_1.setObjectName("first_recipe_3_1")
        self.recipe_1.addWidget(self.first_recipe_3_1, 3, 1, 1, 1)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(9, 0, 621, 33))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.search_bar_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.search_bar_layout.setContentsMargins(0, 0, 0, 0)
        self.search_bar_layout.setObjectName("search_bar_layout")
        self.search_bar = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.search_bar.setObjectName("search_bar")
        self.search_bar_layout.addWidget(self.search_bar)
        self.search_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.search_button.setObjectName("search_button")
        self.search_bar_layout.addWidget(self.search_button)
        self.reset_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.reset_button.setObjectName("reset_button")
        self.search_bar_layout.addWidget(self.reset_button)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(220, 220, 160, 94))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.recipe_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.recipe_2.setContentsMargins(0, 0, 0, 0)
        self.recipe_2.setObjectName("recipe_2")
        self.second_recipe_3_0 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.second_recipe_3_0.setObjectName("second_recipe_3_0")
        self.recipe_2.addWidget(self.second_recipe_3_0, 3, 0, 1, 1)
        self.second_recipe_0_0 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.second_recipe_0_0.setObjectName("second_recipe_0_0")
        self.recipe_2.addWidget(self.second_recipe_0_0, 0, 0, 1, 1)
        self.second_recipe_2_0 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.second_recipe_2_0.setObjectName("second_recipe_2_0")
        self.recipe_2.addWidget(self.second_recipe_2_0, 2, 0, 1, 1)
        self.second_recipe_1_0 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.second_recipe_1_0.setObjectName("second_recipe_1_0")
        self.recipe_2.addWidget(self.second_recipe_1_0, 1, 0, 1, 1)
        self.second_recipe_1_1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.second_recipe_1_1.setObjectName("second_recipe_1_1")
        self.recipe_2.addWidget(self.second_recipe_1_1, 1, 1, 1, 1)
        self.second_recipe_0_1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.second_recipe_0_1.setObjectName("second_recipe_0_1")
        self.recipe_2.addWidget(self.second_recipe_0_1, 0, 1, 1, 1)
        self.second_recipe_2_1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.second_recipe_2_1.setObjectName("second_recipe_2_1")
        self.recipe_2.addWidget(self.second_recipe_2_1, 2, 1, 1, 1)
        self.second_recipe_3_1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.second_recipe_3_1.setObjectName("second_recipe_3_1")
        self.recipe_2.addWidget(self.second_recipe_3_1, 3, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(430, 220, 160, 94))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.recipe_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.recipe_3.setContentsMargins(0, 0, 0, 0)
        self.recipe_3.setObjectName("recipe_3")
        self.third_recipe_3_0 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.third_recipe_3_0.setObjectName("third_recipe_3_0")
        self.recipe_3.addWidget(self.third_recipe_3_0, 3, 0, 1, 1)
        self.third_recipe_0_0 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.third_recipe_0_0.setObjectName("third_recipe_0_0")
        self.recipe_3.addWidget(self.third_recipe_0_0, 0, 0, 1, 1)
        self.third_recipe_2_0 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.third_recipe_2_0.setObjectName("third_recipe_2_0")
        self.recipe_3.addWidget(self.third_recipe_2_0, 2, 0, 1, 1)
        self.third_recipe_1_0 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.third_recipe_1_0.setObjectName("third_recipe_1_0")
        self.recipe_3.addWidget(self.third_recipe_1_0, 1, 0, 1, 1)
        self.third_recipe_1_1 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.third_recipe_1_1.setObjectName("third_recipe_1_1")
        self.recipe_3.addWidget(self.third_recipe_1_1, 1, 1, 1, 1)
        self.third_recipe_0_1 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.third_recipe_0_1.setObjectName("third_recipe_0_1")
        self.recipe_3.addWidget(self.third_recipe_0_1, 0, 1, 1, 1)
        self.third_recipe_2_1 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.third_recipe_2_1.setObjectName("third_recipe_2_1")
        self.recipe_3.addWidget(self.third_recipe_2_1, 2, 1, 1, 1)
        self.third_recipe_3_1 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.third_recipe_3_1.setObjectName("third_recipe_3_1")
        self.recipe_3.addWidget(self.third_recipe_3_1, 3, 1, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(0, 530, 160, 94))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.recipe_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.recipe_4.setContentsMargins(0, 0, 0, 0)
        self.recipe_4.setObjectName("recipe_4")
        self.fourth_recipe_3_0 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.fourth_recipe_3_0.setObjectName("fourth_recipe_3_0")
        self.recipe_4.addWidget(self.fourth_recipe_3_0, 3, 0, 1, 1)
        self.fourth_recipe_0_0 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.fourth_recipe_0_0.setObjectName("fourth_recipe_0_0")
        self.recipe_4.addWidget(self.fourth_recipe_0_0, 0, 0, 1, 1)
        self.fourth_recipe_2_0 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.fourth_recipe_2_0.setObjectName("fourth_recipe_2_0")
        self.recipe_4.addWidget(self.fourth_recipe_2_0, 2, 0, 1, 1)
        self.fourth_recipe_1_0 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.fourth_recipe_1_0.setObjectName("fourth_recipe_1_0")
        self.recipe_4.addWidget(self.fourth_recipe_1_0, 1, 0, 1, 1)
        self.fourth_recipe_1_1 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.fourth_recipe_1_1.setObjectName("fourth_recipe_1_1")
        self.recipe_4.addWidget(self.fourth_recipe_1_1, 1, 1, 1, 1)
        self.fourth_recipe_0_1 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.fourth_recipe_0_1.setObjectName("fourth_recipe_0_1")
        self.recipe_4.addWidget(self.fourth_recipe_0_1, 0, 1, 1, 1)
        self.fourth_recipe_2_1 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.fourth_recipe_2_1.setObjectName("fourth_recipe_2_1")
        self.recipe_4.addWidget(self.fourth_recipe_2_1, 2, 1, 1, 1)
        self.fourth_recipe_3_1 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.fourth_recipe_3_1.setObjectName("fourth_recipe_3_1")
        self.recipe_4.addWidget(self.fourth_recipe_3_1, 3, 1, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(220, 530, 160, 94))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.recipe_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.recipe_5.setContentsMargins(0, 0, 0, 0)
        self.recipe_5.setObjectName("recipe_5")
        self.fifth_recipe_3_0 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.fifth_recipe_3_0.setObjectName("fifth_recipe_3_0")
        self.recipe_5.addWidget(self.fifth_recipe_3_0, 3, 0, 1, 1)
        self.fifth_recipe_0_0 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.fifth_recipe_0_0.setObjectName("fifth_recipe_0_0")
        self.recipe_5.addWidget(self.fifth_recipe_0_0, 0, 0, 1, 1)
        self.fifth_recipe_2_0 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.fifth_recipe_2_0.setObjectName("fifth_recipe_2_0")
        self.recipe_5.addWidget(self.fifth_recipe_2_0, 2, 0, 1, 1)
        self.fifth_recipe_1_0 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.fifth_recipe_1_0.setObjectName("fifth_recipe_1_0")
        self.recipe_5.addWidget(self.fifth_recipe_1_0, 1, 0, 1, 1)
        self.fifth_recipe_1_1 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.fifth_recipe_1_1.setObjectName("fifth_recipe_1_1")
        self.recipe_5.addWidget(self.fifth_recipe_1_1, 1, 1, 1, 1)
        self.fifth_recipe_0_1 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.fifth_recipe_0_1.setObjectName("fifth_recipe_0_1")
        self.recipe_5.addWidget(self.fifth_recipe_0_1, 0, 1, 1, 1)
        self.fifth_recipe_2_1 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.fifth_recipe_2_1.setObjectName("fifth_recipe_2_1")
        self.recipe_5.addWidget(self.fifth_recipe_2_1, 2, 1, 1, 1)
        self.fifth_recipe_3_1 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.fifth_recipe_3_1.setObjectName("fifth_recipe_3_1")
        self.recipe_5.addWidget(self.fifth_recipe_3_1, 3, 1, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(430, 530, 160, 94))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.recipe_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.recipe_6.setContentsMargins(0, 0, 0, 0)
        self.recipe_6.setObjectName("recipe_6")
        self.sixth_recipe_3_0 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.sixth_recipe_3_0.setObjectName("sixth_recipe_3_0")
        self.recipe_6.addWidget(self.sixth_recipe_3_0, 3, 0, 1, 1)
        self.sixth_recipe_0_0 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.sixth_recipe_0_0.setObjectName("sixth_recipe_0_0")
        self.recipe_6.addWidget(self.sixth_recipe_0_0, 0, 0, 1, 1)
        self.sixth_recipe_2_0 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.sixth_recipe_2_0.setObjectName("sixth_recipe_2_0")
        self.recipe_6.addWidget(self.sixth_recipe_2_0, 2, 0, 1, 1)
        self.sixth_recipe_1_0 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.sixth_recipe_1_0.setObjectName("sixth_recipe_1_0")
        self.recipe_6.addWidget(self.sixth_recipe_1_0, 1, 0, 1, 1)
        self.sixth_recipe_1_1 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.sixth_recipe_1_1.setObjectName("sixth_recipe_1_1")
        self.recipe_6.addWidget(self.sixth_recipe_1_1, 1, 1, 1, 1)
        self.sixth_recipe_0_1 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.sixth_recipe_0_1.setObjectName("sixth_recipe_0_1")
        self.recipe_6.addWidget(self.sixth_recipe_0_1, 0, 1, 1, 1)
        self.sixth_recipe_2_1 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.sixth_recipe_2_1.setObjectName("sixth_recipe_2_1")
        self.recipe_6.addWidget(self.sixth_recipe_2_1, 2, 1, 1, 1)
        self.sixth_recipe_3_1 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.sixth_recipe_3_1.setObjectName("sixth_recipe_3_1")
        self.recipe_6.addWidget(self.sixth_recipe_3_1, 3, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 320, 100, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 320, 100, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 320, 100, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(490, 630, 100, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(280, 630, 100, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(60, 630, 100, 32))
        self.pushButton_7.setObjectName("pushButton_7")
        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(main_window)
        self.action_open.setObjectName("action_open")
        self.action_copy = QtWidgets.QAction(main_window)
        self.action_copy.setObjectName("action_copy")
        self.action_update = QtWidgets.QAction(main_window)
        self.action_update.setObjectName("action_update")

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.recepie_1_pic.setText(_translate("main_window", "TextLabel"))
        self.recepie_2_pic.setText(_translate("main_window", "TextLabel"))
        self.recepie_3_pic.setText(_translate("main_window", "TextLabel"))
        self.recepie_4_pic.setText(_translate("main_window", "TextLabel"))
        self.recepie_6_pic.setText(_translate("main_window", "TextLabel"))
        self.recepie_5_pic.setText(_translate("main_window", "TextLabel"))
        self.previous_button.setText(_translate("main_window", "<<Previous"))
        self.first_button.setText(_translate("main_window", "First"))
        self.last_button.setText(_translate("main_window", "Last"))
        self.pushButton.setText(_translate("main_window", "Next>>"))
        self.first_recipe_3_0.setText(_translate("main_window", "Cook Time:"))
        self.first_recipe_0_0.setText(_translate("main_window", "Recipe #:"))
        self.first_recipe_2_0.setText(_translate("main_window", "Prep Time:"))
        self.first_recipe_1_0.setText(_translate("main_window", "Recipe Name:"))
        self.first_recipe_1_1.setText(_translate("main_window", "TextLabel"))
        self.first_recipe_0_1.setText(_translate("main_window", "TextLabel"))
        self.first_recipe_2_1.setText(_translate("main_window", "TextLabel"))
        self.first_recipe_3_1.setText(_translate("main_window", "TextLabel"))
        self.search_button.setText(_translate("main_window", "Search"))
        self.reset_button.setText(_translate("main_window", "Reset"))
        self.second_recipe_3_0.setText(_translate("main_window", "Cook Time:"))
        self.second_recipe_0_0.setText(_translate("main_window", "Recipe #:"))
        self.second_recipe_2_0.setText(_translate("main_window", "Prep Time:"))
        self.second_recipe_1_0.setText(_translate("main_window", "Recipe Name:"))
        self.second_recipe_1_1.setText(_translate("main_window", "TextLabel"))
        self.second_recipe_0_1.setText(_translate("main_window", "TextLabel"))
        self.second_recipe_2_1.setText(_translate("main_window", "TextLabel"))
        self.second_recipe_3_1.setText(_translate("main_window", "TextLabel"))
        self.third_recipe_3_0.setText(_translate("main_window", "Cook Time:"))
        self.third_recipe_0_0.setText(_translate("main_window", "Recipe #:"))
        self.third_recipe_2_0.setText(_translate("main_window", "Prep Time:"))
        self.third_recipe_1_0.setText(_translate("main_window", "Recipe Name:"))
        self.third_recipe_1_1.setText(_translate("main_window", "TextLabel"))
        self.third_recipe_0_1.setText(_translate("main_window", "TextLabel"))
        self.third_recipe_2_1.setText(_translate("main_window", "TextLabel"))
        self.third_recipe_3_1.setText(_translate("main_window", "TextLabel"))
        self.fourth_recipe_3_0.setText(_translate("main_window", "Cook Time:"))
        self.fourth_recipe_0_0.setText(_translate("main_window", "Recipe #:"))
        self.fourth_recipe_2_0.setText(_translate("main_window", "Prep Time:"))
        self.fourth_recipe_1_0.setText(_translate("main_window", "Recipe Name:"))
        self.fourth_recipe_1_1.setText(_translate("main_window", "TextLabel"))
        self.fourth_recipe_0_1.setText(_translate("main_window", "TextLabel"))
        self.fourth_recipe_2_1.setText(_translate("main_window", "TextLabel"))
        self.fourth_recipe_3_1.setText(_translate("main_window", "TextLabel"))
        self.fifth_recipe_3_0.setText(_translate("main_window", "Cook Time:"))
        self.fifth_recipe_0_0.setText(_translate("main_window", "Recipe #:"))
        self.fifth_recipe_2_0.setText(_translate("main_window", "Prep Time:"))
        self.fifth_recipe_1_0.setText(_translate("main_window", "Recipe Name:"))
        self.fifth_recipe_1_1.setText(_translate("main_window", "TextLabel"))
        self.fifth_recipe_0_1.setText(_translate("main_window", "TextLabel"))
        self.fifth_recipe_2_1.setText(_translate("main_window", "TextLabel"))
        self.fifth_recipe_3_1.setText(_translate("main_window", "TextLabel"))
        self.sixth_recipe_3_0.setText(_translate("main_window", "Cook Time:"))
        self.sixth_recipe_0_0.setText(_translate("main_window", "Recipe #:"))
        self.sixth_recipe_2_0.setText(_translate("main_window", "Prep Time:"))
        self.sixth_recipe_1_0.setText(_translate("main_window", "Recipe Name:"))
        self.sixth_recipe_1_1.setText(_translate("main_window", "TextLabel"))
        self.sixth_recipe_0_1.setText(_translate("main_window", "TextLabel"))
        self.sixth_recipe_2_1.setText(_translate("main_window", "TextLabel"))
        self.sixth_recipe_3_1.setText(_translate("main_window", "TextLabel"))
        self.pushButton_2.setText(_translate("main_window", "View Recipie"))
        self.pushButton_3.setText(_translate("main_window", "View Recipie"))
        self.pushButton_4.setText(_translate("main_window", "View Recipie"))
        self.pushButton_5.setText(_translate("main_window", "View Recipie"))
        self.pushButton_6.setText(_translate("main_window", "View Recipie"))
        self.pushButton_7.setText(_translate("main_window", "View Recipie"))
        self.action_open.setText(_translate("main_window", "Open"))
        self.action_copy.setText(_translate("main_window", "Copy"))
        self.action_update.setText(_translate("main_window", "Update"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())

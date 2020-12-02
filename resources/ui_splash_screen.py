# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenUOJhXU.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import resources_rc

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.setEnabled(True)
        SplashScreen.resize(622, 470)
        SplashScreen.setMaximumSize(QSize(799, 550))
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
"	background-color: transparent;	\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 20, 591, 71))
        font = QFont()
        font.setFamily(u"QUARTZO")
        font.setPointSize(35)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 80, 601, 20))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(10)
        self.label_description.setFont(font1)
        self.label_description.setAlignment(Qt.AlignCenter)
        self.graphicsView = QGraphicsView(self.dropShadowFrame)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(0, 0, 601, 451))
        self.graphicsView.setStyleSheet(u"QGraphicsView {\n"
"	background-image:url(:/bg/620x470.jpg);\n"
"}")
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(80, 390, 441, 20))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color:rgb(248, 220, 155);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(248, 170, 20);\n"
"}")
        self.progressBar.setValue(24)
        self.loading_text = QLabel(self.dropShadowFrame)
        self.loading_text.setObjectName(u"loading_text")
        self.loading_text.setGeometry(QRect(0, 360, 601, 31))
        self.loading_text.setFont(font1)
        self.loading_text.setAlignment(Qt.AlignCenter)
        self.label_description_2 = QLabel(self.dropShadowFrame)
        self.label_description_2.setObjectName(u"label_description_2")
        self.label_description_2.setGeometry(QRect(460, 50, 131, 41))
        font2 = QFont()
        font2.setFamily(u"Roboto Bk")
        font2.setPointSize(8)
        self.label_description_2.setFont(font2)
        self.label_description_2.setAlignment(Qt.AlignCenter)
        self.graphicsView.raise_()
        self.label_title.raise_()
        self.label_description.raise_()
        self.progressBar.raise_()
        self.loading_text.raise_()
        self.label_description_2.raise_()

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"EXPENSES TRACKER", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u"Basic Python Program that Tracks your Expenses", None))
        self.loading_text.setText(QCoreApplication.translate("SplashScreen", u"Loading..", None))
        self.label_description_2.setText(QCoreApplication.translate("SplashScreen", u"v1.0", None))
    # retranslateUi


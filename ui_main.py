# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, rss.rss

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setMaximumSize(QtCore.QSize(1024, 600))
        MainWindow.setStyleSheet("background-color: #202225;\n"
"\n"
"QStackedWidget {\n"
"    background-color: rgba(54, 57, 63, 100);\n"
"    border: none;\n"
"    border-top-left-radius: 20px;\n"
"    margin-left: 20px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 35))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.widget.setFont(font)
        self.widget.setStyleSheet("background-color: #2F3136;\n"
"border: none;\n"
"")
        self.widget.setObjectName("widget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setMinimumSize(QtCore.QSize(15, 15))
        self.label_8.setMaximumSize(QtCore.QSize(15, 15))
        self.label_8.setStyleSheet("image: url(:/img/svg/template.svg);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.title_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_label.setScaledContents(False)
        self.title_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.title_label.setObjectName("title_label")
        self.horizontalLayout_8.addWidget(self.title_label)
        self.pushButton_windows_min = QtWidgets.QPushButton(self.widget)
        self.pushButton_windows_min.setMinimumSize(QtCore.QSize(27, 17))
        self.pushButton_windows_min.setMaximumSize(QtCore.QSize(27, 17))
        self.pushButton_windows_min.setStyleSheet("QPushButton{\n"
"image: url(:/img/svg/minimize_icon.svg);\n"
"border: none;\n"
"border-radius: 8px;\n"
"color: rgba(255, 255, 255, 255);\n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(255, 255, 255, 50);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:8px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(255, 255, 255, 100);\n"
"  border-radius:8px;\n"
"}")
        self.pushButton_windows_min.setText("")
        self.pushButton_windows_min.setObjectName("pushButton_windows_min")
        self.horizontalLayout_8.addWidget(self.pushButton_windows_min)
        self.pushButton_window_max = QtWidgets.QPushButton(self.widget)
        self.pushButton_window_max.setMinimumSize(QtCore.QSize(27, 17))
        self.pushButton_window_max.setMaximumSize(QtCore.QSize(27, 17))
        self.pushButton_window_max.setStyleSheet("QPushButton{\n"
"image: url(:/img/svg/maximize_icon.svg);\n"
"border: none;\n"
"border-radius: 8px;\n"
"color: rgba(255, 255, 255, 255);\n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(255, 255, 255, 50);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:8px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(255, 255, 255, 100);\n"
"  border-radius:8px;\n"
"}")
        self.pushButton_window_max.setText("")
        self.pushButton_window_max.setObjectName("pushButton_window_max")
        self.horizontalLayout_8.addWidget(self.pushButton_window_max)
        self.pushButton_windows_close = QtWidgets.QPushButton(self.widget)
        self.pushButton_windows_close.setMinimumSize(QtCore.QSize(27, 17))
        self.pushButton_windows_close.setMaximumSize(QtCore.QSize(27, 17))
        self.pushButton_windows_close.setStyleSheet("QPushButton{\n"
"image: url(:/img/svg/close_icon_2.svg);\n"
"border: none;\n"
"border-radius: 8px;\n"
"color: rgba(255, 255, 255, 255);\n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(255, 255, 255, 50);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:8px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(255, 255, 255, 100);\n"
"  border-radius:8px;\n"
"}")
        self.pushButton_windows_close.setText("")
        self.pushButton_windows_close.setObjectName("pushButton_windows_close")
        self.horizontalLayout_8.addWidget(self.pushButton_windows_close)
        self.verticalLayout_3.addWidget(self.widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_2.setStyleSheet("QPushButton{\n"
"border: none;\n"
"border-radius: 15px;\n"
"color: rgba(170, 170, 255, 150);\n"
"text-align: left;\n"
"padding-left: 20px;\n"
"margin: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #36393F;\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:15px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 200);\n"
"}")
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 49, 54, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 49, 54, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 49, 54, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 49, 54, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 49, 54, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 49, 54, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 49, 54, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 49, 54, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 49, 54, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(47, 49, 54, 200);\n"
"border: none;\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setMinimumSize(QtCore.QSize(30, 30))
        self.label_3.setMaximumSize(QtCore.QSize(30, 30))
        self.label_3.setStyleSheet("image: url(:/img/svg/home.svg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.btn_home = QtWidgets.QPushButton(self.frame_2)
        self.btn_home.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_home.setMaximumSize(QtCore.QSize(150, 50))
        self.btn_home.setAutoFillBackground(False)
        self.btn_home.setStyleSheet("")
        self.btn_home.setObjectName("btn_home")
        self.horizontalLayout_3.addWidget(self.btn_home)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setMinimumSize(QtCore.QSize(30, 30))
        self.label_5.setMaximumSize(QtCore.QSize(30, 30))
        self.label_5.setStyleSheet("image: url(:/img/svg/line_chart.svg);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.btn_mpd = QtWidgets.QPushButton(self.frame_2)
        self.btn_mpd.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_mpd.setMaximumSize(QtCore.QSize(150, 50))
        self.btn_mpd.setAutoFillBackground(False)
        self.btn_mpd.setStyleSheet("")
        self.btn_mpd.setObjectName("btn_mpd")
        self.horizontalLayout_5.addWidget(self.btn_mpd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setMinimumSize(QtCore.QSize(30, 30))
        self.label_4.setMaximumSize(QtCore.QSize(30, 30))
        self.label_4.setStyleSheet("image: url(:/img/svg/heat_map.svg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.btn_ther = QtWidgets.QPushButton(self.frame_2)
        self.btn_ther.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_ther.setMaximumSize(QtCore.QSize(150, 50))
        self.btn_ther.setAutoFillBackground(False)
        self.btn_ther.setStyleSheet("")
        self.btn_ther.setObjectName("btn_ther")
        self.horizontalLayout_4.addWidget(self.btn_ther)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setMinimumSize(QtCore.QSize(30, 30))
        self.label_6.setMaximumSize(QtCore.QSize(30, 30))
        self.label_6.setStyleSheet("image: url(:/img/svg/combo_chart.svg);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.btn_tec_volt = QtWidgets.QPushButton(self.frame_2)
        self.btn_tec_volt.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_tec_volt.setMaximumSize(QtCore.QSize(150, 50))
        self.btn_tec_volt.setAutoFillBackground(False)
        self.btn_tec_volt.setStyleSheet("")
        self.btn_tec_volt.setObjectName("btn_tec_volt")
        self.horizontalLayout_6.addWidget(self.btn_tec_volt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setMinimumSize(QtCore.QSize(30, 30))
        self.label_7.setMaximumSize(QtCore.QSize(30, 30))
        self.label_7.setStyleSheet("image: url(:/img/svg/combo_chart.svg);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.btn_tec_curr = QtWidgets.QPushButton(self.frame_2)
        self.btn_tec_curr.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_tec_curr.setMaximumSize(QtCore.QSize(150, 50))
        self.btn_tec_curr.setAutoFillBackground(False)
        self.btn_tec_curr.setStyleSheet("")
        self.btn_tec_curr.setObjectName("btn_tec_curr")
        self.horizontalLayout_7.addWidget(self.btn_tec_curr)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setMinimumSize(QtCore.QSize(30, 30))
        self.label_9.setMaximumSize(QtCore.QSize(30, 30))
        self.label_9.setStyleSheet("image: url(:/img/svg/bar_chart.svg);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.btn_ld_volt = QtWidgets.QPushButton(self.frame_2)
        self.btn_ld_volt.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_ld_volt.setMaximumSize(QtCore.QSize(150, 50))
        self.btn_ld_volt.setAutoFillBackground(False)
        self.btn_ld_volt.setStyleSheet("")
        self.btn_ld_volt.setObjectName("btn_ld_volt")
        self.horizontalLayout_9.addWidget(self.btn_ld_volt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setMinimumSize(QtCore.QSize(30, 30))
        self.label_10.setMaximumSize(QtCore.QSize(30, 30))
        self.label_10.setStyleSheet("image: url(:/img/svg/bar_chart.svg);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.btn_ld_curr = QtWidgets.QPushButton(self.frame_2)
        self.btn_ld_curr.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_ld_curr.setMaximumSize(QtCore.QSize(150, 50))
        self.btn_ld_curr.setAutoFillBackground(False)
        self.btn_ld_curr.setStyleSheet("")
        self.btn_ld_curr.setObjectName("btn_ld_curr")
        self.horizontalLayout_10.addWidget(self.btn_ld_curr)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setMinimumSize(QtCore.QSize(30, 30))
        self.label_11.setMaximumSize(QtCore.QSize(30, 30))
        self.label_11.setStyleSheet("image: url(:/img/svg/settings.svg);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.btn_setting = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_setting.sizePolicy().hasHeightForWidth())
        self.btn_setting.setSizePolicy(sizePolicy)
        self.btn_setting.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_setting.setMaximumSize(QtCore.QSize(150, 50))
        self.btn_setting.setAutoFillBackground(False)
        self.btn_setting.setStyleSheet("")
        self.btn_setting.setObjectName("btn_setting")
        self.horizontalLayout_11.addWidget(self.btn_setting)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 5, 5, -1)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #FFF;\n"
"margin-left: 20px;")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setStyleSheet("QWidget#widget_2{\n"
"background-color: rgba(54, 57, 63, 100);\n"
"border: none;\n"
"border-top-left-radius: 20px;\n"
"margin-left: 20px;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_2)
        self.stackedWidget.setMaximumSize(QtCore.QSize(1024, 600))
        self.stackedWidget.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"margin-left: 10px;\n"
"margin-top: 5px;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.dashboard = QtWidgets.QWidget()
        self.dashboard.setStyleSheet("QLabel{\n"
"color: rgba(255, 255, 255, 160);\n"
"margin: 0px;\n"
"padding: 0px;\n"
"text-align: cetner;\n"
"}\n"
"")
        self.dashboard.setObjectName("dashboard")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.dashboard)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_26 = QtWidgets.QLabel(self.dashboard)
        self.label_26.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_26.setStyleSheet("color: #fff;\n"
"padding-left: 20px;")
        self.label_26.setObjectName("label_26")
        self.verticalLayout_5.addWidget(self.label_26)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_c13_4 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c13_4.sizePolicy().hasHeightForWidth())
        self.label_c13_4.setSizePolicy(sizePolicy)
        self.label_c13_4.setMinimumSize(QtCore.QSize(40, 16))
        self.label_c13_4.setMaximumSize(QtCore.QSize(16, 16))
        self.label_c13_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);\n"
"padding: 0px;\n"
"margin-left: 0px;")
        self.label_c13_4.setText("")
        self.label_c13_4.setObjectName("label_c13_4")
        self.gridLayout_2.addWidget(self.label_c13_4, 13, 6, 1, 1)
        self.pushButton_stop_2 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_stop_2.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_stop_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop_2.setFont(font)
        self.pushButton_stop_2.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(205, 118, 132, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(205, 118, 132, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_stop_2.setObjectName("pushButton_stop_2")
        self.gridLayout_2.addWidget(self.pushButton_stop_2, 2, 2, 1, 1)
        self.label_c8 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c8.sizePolicy().hasHeightForWidth())
        self.label_c8.setSizePolicy(sizePolicy)
        self.label_c8.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c8.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c8.setObjectName("label_c8")
        self.gridLayout_2.addWidget(self.label_c8, 8, 3, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.dashboard)
        self.label_33.setMinimumSize(QtCore.QSize(0, 20))
        self.label_33.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout_2.addWidget(self.label_33, 7, 0, 1, 1)
        self.label_91 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_91.sizePolicy().hasHeightForWidth())
        self.label_91.setSizePolicy(sizePolicy)
        self.label_91.setMinimumSize(QtCore.QSize(0, 30))
        self.label_91.setMaximumSize(QtCore.QSize(1000, 30))
        self.label_91.setStyleSheet("margin: 0px;\n"
"padding: 0px;\n"
"background-color: rgba(0, 0, 0, 100);\n"
"border: none;\n"
"border-radius: 15px;")
        self.label_91.setAlignment(QtCore.Qt.AlignCenter)
        self.label_91.setObjectName("label_91")
        self.gridLayout_2.addWidget(self.label_91, 0, 6, 1, 1)
        self.label_c12 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c12.sizePolicy().hasHeightForWidth())
        self.label_c12.setSizePolicy(sizePolicy)
        self.label_c12.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c12.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c12.setObjectName("label_c12")
        self.gridLayout_2.addWidget(self.label_c12, 12, 3, 1, 1)
        self.label_c7_4 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c7_4.sizePolicy().hasHeightForWidth())
        self.label_c7_4.setSizePolicy(sizePolicy)
        self.label_c7_4.setMinimumSize(QtCore.QSize(40, 16))
        self.label_c7_4.setMaximumSize(QtCore.QSize(16, 16))
        self.label_c7_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);\n"
"padding: 0px;\n"
"margin-left: 0px;")
        self.label_c7_4.setText("")
        self.label_c7_4.setObjectName("label_c7_4")
        self.gridLayout_2.addWidget(self.label_c7_4, 7, 6, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.dashboard)
        self.label_29.setMinimumSize(QtCore.QSize(0, 20))
        self.label_29.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 3, 0, 1, 1)
        self.label_c11_3 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c11_3.sizePolicy().hasHeightForWidth())
        self.label_c11_3.setSizePolicy(sizePolicy)
        self.label_c11_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c11_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c11_3.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c11_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c11_3.setObjectName("label_c11_3")
        self.gridLayout_2.addWidget(self.label_c11_3, 11, 5, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.dashboard)
        self.label_42.setMinimumSize(QtCore.QSize(0, 20))
        self.label_42.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.gridLayout_2.addWidget(self.label_42, 16, 0, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.dashboard)
        self.label_37.setMinimumSize(QtCore.QSize(0, 20))
        self.label_37.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout_2.addWidget(self.label_37, 11, 0, 1, 1)
        self.label_c9_4 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c9_4.sizePolicy().hasHeightForWidth())
        self.label_c9_4.setSizePolicy(sizePolicy)
        self.label_c9_4.setMinimumSize(QtCore.QSize(40, 16))
        self.label_c9_4.setMaximumSize(QtCore.QSize(40, 16))
        self.label_c9_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);\n"
"padding: 0px;\n"
"margin-left: 0px;")
        self.label_c9_4.setText("")
        self.label_c9_4.setObjectName("label_c9_4")
        self.gridLayout_2.addWidget(self.label_c9_4, 9, 6, 1, 1)
        self.label_c7_2 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c7_2.sizePolicy().hasHeightForWidth())
        self.label_c7_2.setSizePolicy(sizePolicy)
        self.label_c7_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c7_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c7_2.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c7_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c7_2.setObjectName("label_c7_2")
        self.gridLayout_2.addWidget(self.label_c7_2, 7, 4, 1, 1)
        self.label_c7_3 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c7_3.sizePolicy().hasHeightForWidth())
        self.label_c7_3.setSizePolicy(sizePolicy)
        self.label_c7_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c7_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c7_3.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c7_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c7_3.setObjectName("label_c7_3")
        self.gridLayout_2.addWidget(self.label_c7_3, 7, 5, 1, 1)
        self.label_c16_4 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c16_4.sizePolicy().hasHeightForWidth())
        self.label_c16_4.setSizePolicy(sizePolicy)
        self.label_c16_4.setMinimumSize(QtCore.QSize(40, 16))
        self.label_c16_4.setMaximumSize(QtCore.QSize(16, 16))
        self.label_c16_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);\n"
"padding: 0px;\n"
"margin-left: 0px;")
        self.label_c16_4.setText("")
        self.label_c16_4.setObjectName("label_c16_4")
        self.gridLayout_2.addWidget(self.label_c16_4, 16, 6, 1, 1)
        self.label_75 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy)
        self.label_75.setMinimumSize(QtCore.QSize(140, 30))
        self.label_75.setMaximumSize(QtCore.QSize(140, 30))
        self.label_75.setStyleSheet("margin: 0px;\n"
"padding: 0px;\n"
"background-color: rgba(0, 0, 0, 100);\n"
"border: none;\n"
"border-radius: 15px;")
        self.label_75.setAlignment(QtCore.Qt.AlignCenter)
        self.label_75.setObjectName("label_75")
        self.gridLayout_2.addWidget(self.label_75, 0, 4, 1, 1)
        self.label_c11_4 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c11_4.sizePolicy().hasHeightForWidth())
        self.label_c11_4.setSizePolicy(sizePolicy)
        self.label_c11_4.setMinimumSize(QtCore.QSize(40, 16))
        self.label_c11_4.setMaximumSize(QtCore.QSize(40, 16))
        self.label_c11_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);\n"
"padding: 0px;\n"
"margin-left: 0px;")
        self.label_c11_4.setText("")
        self.label_c11_4.setObjectName("label_c11_4")
        self.gridLayout_2.addWidget(self.label_c11_4, 11, 6, 1, 1)
        self.label_c10 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c10.sizePolicy().hasHeightForWidth())
        self.label_c10.setSizePolicy(sizePolicy)
        self.label_c10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c10.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c10.setObjectName("label_c10")
        self.gridLayout_2.addWidget(self.label_c10, 10, 3, 1, 1)
        self.label_c10_2 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c10_2.sizePolicy().hasHeightForWidth())
        self.label_c10_2.setSizePolicy(sizePolicy)
        self.label_c10_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c10_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c10_2.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c10_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c10_2.setObjectName("label_c10_2")
        self.gridLayout_2.addWidget(self.label_c10_2, 10, 4, 1, 1)
        self.label_c14_4 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c14_4.sizePolicy().hasHeightForWidth())
        self.label_c14_4.setSizePolicy(sizePolicy)
        self.label_c14_4.setMinimumSize(QtCore.QSize(40, 16))
        self.label_c14_4.setMaximumSize(QtCore.QSize(16, 16))
        self.label_c14_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);\n"
"padding: 0px;\n"
"margin-left: 0px;")
        self.label_c14_4.setText("")
        self.label_c14_4.setObjectName("label_c14_4")
        self.gridLayout_2.addWidget(self.label_c14_4, 14, 6, 1, 1)
        self.label_c1_1 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c1_1.sizePolicy().hasHeightForWidth())
        self.label_c1_1.setSizePolicy(sizePolicy)
        self.label_c1_1.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c1_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c1_1.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c1_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c1_1.setObjectName("label_c1_1")
        self.gridLayout_2.addWidget(self.label_c1_1, 1, 3, 1, 1)
        self.label_c3_4 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c3_4.sizePolicy().hasHeightForWidth())
        self.label_c3_4.setSizePolicy(sizePolicy)
        self.label_c3_4.setMinimumSize(QtCore.QSize(40, 16))
        self.label_c3_4.setMaximumSize(QtCore.QSize(40, 16))
        self.label_c3_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);\n"
"padding: 0px;\n"
"margin-left: 0px;")
        self.label_c3_4.setText("")
        self.label_c3_4.setObjectName("label_c3_4")
        self.gridLayout_2.addWidget(self.label_c3_4, 3, 6, 1, 1)
        self.label_c2_4 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c2_4.sizePolicy().hasHeightForWidth())
        self.label_c2_4.setSizePolicy(sizePolicy)
        self.label_c2_4.setMinimumSize(QtCore.QSize(40, 16))
        self.label_c2_4.setMaximumSize(QtCore.QSize(40, 16))
        self.label_c2_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);\n"
"padding: 0px;\n"
"margin-left: 0px;")
        self.label_c2_4.setText("")
        self.label_c2_4.setObjectName("label_c2_4")
        self.gridLayout_2.addWidget(self.label_c2_4, 2, 6, 1, 1)
        self.pushButton_start_2 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_start_2.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_start_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start_2.setFont(font)
        self.pushButton_start_2.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_start_2.setObjectName("pushButton_start_2")
        self.gridLayout_2.addWidget(self.pushButton_start_2, 2, 1, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.dashboard)
        self.label_36.setMinimumSize(QtCore.QSize(0, 20))
        self.label_36.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout_2.addWidget(self.label_36, 10, 0, 1, 1)
        self.label_c15 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c15.sizePolicy().hasHeightForWidth())
        self.label_c15.setSizePolicy(sizePolicy)
        self.label_c15.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c15.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c15.setObjectName("label_c15")
        self.gridLayout_2.addWidget(self.label_c15, 15, 3, 1, 1)
        self.label_c12_4 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c12_4.sizePolicy().hasHeightForWidth())
        self.label_c12_4.setSizePolicy(sizePolicy)
        self.label_c12_4.setMinimumSize(QtCore.QSize(40, 16))
        self.label_c12_4.setMaximumSize(QtCore.QSize(16, 16))
        self.label_c12_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);\n"
"padding: 0px;\n"
"margin-left: 0px;")
        self.label_c12_4.setText("")
        self.label_c12_4.setObjectName("label_c12_4")
        self.gridLayout_2.addWidget(self.label_c12_4, 12, 6, 1, 1)
        self.label_c8_2 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c8_2.sizePolicy().hasHeightForWidth())
        self.label_c8_2.setSizePolicy(sizePolicy)
        self.label_c8_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c8_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c8_2.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c8_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c8_2.setObjectName("label_c8_2")
        self.gridLayout_2.addWidget(self.label_c8_2, 8, 4, 1, 1)
        self.label_c14_2 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c14_2.sizePolicy().hasHeightForWidth())
        self.label_c14_2.setSizePolicy(sizePolicy)
        self.label_c14_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c14_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c14_2.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c14_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c14_2.setObjectName("label_c14_2")
        self.gridLayout_2.addWidget(self.label_c14_2, 14, 4, 1, 1)
        self.label_c3_3 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c3_3.sizePolicy().hasHeightForWidth())
        self.label_c3_3.setSizePolicy(sizePolicy)
        self.label_c3_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c3_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c3_3.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c3_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c3_3.setObjectName("label_c3_3")
        self.gridLayout_2.addWidget(self.label_c3_3, 3, 5, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.dashboard)
        self.label_38.setMinimumSize(QtCore.QSize(0, 20))
        self.label_38.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.gridLayout_2.addWidget(self.label_38, 12, 0, 1, 1)
        self.label_c9_3 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c9_3.sizePolicy().hasHeightForWidth())
        self.label_c9_3.setSizePolicy(sizePolicy)
        self.label_c9_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c9_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c9_3.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c9_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c9_3.setObjectName("label_c9_3")
        self.gridLayout_2.addWidget(self.label_c9_3, 9, 5, 1, 1)
        self.label_c5 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c5.sizePolicy().hasHeightForWidth())
        self.label_c5.setSizePolicy(sizePolicy)
        self.label_c5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c5.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c5.setObjectName("label_c5")
        self.gridLayout_2.addWidget(self.label_c5, 5, 3, 1, 1)
        self.label_c9 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c9.sizePolicy().hasHeightForWidth())
        self.label_c9.setSizePolicy(sizePolicy)
        self.label_c9.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c9.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c9.setObjectName("label_c9")
        self.gridLayout_2.addWidget(self.label_c9, 9, 3, 1, 1)
        self.label_c11_2 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c11_2.sizePolicy().hasHeightForWidth())
        self.label_c11_2.setSizePolicy(sizePolicy)
        self.label_c11_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c11_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c11_2.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c11_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c11_2.setObjectName("label_c11_2")
        self.gridLayout_2.addWidget(self.label_c11_2, 11, 4, 1, 1)
        self.label_c3_2 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c3_2.sizePolicy().hasHeightForWidth())
        self.label_c3_2.setSizePolicy(sizePolicy)
        self.label_c3_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c3_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c3_2.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c3_2.setObjectName("label_c3_2")
        self.gridLayout_2.addWidget(self.label_c3_2, 3, 4, 1, 1)
        self.label_c4_2 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c4_2.sizePolicy().hasHeightForWidth())
        self.label_c4_2.setSizePolicy(sizePolicy)
        self.label_c4_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c4_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c4_2.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c4_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c4_2.setObjectName("label_c4_2")
        self.gridLayout_2.addWidget(self.label_c4_2, 4, 4, 1, 1)
        self.label_c5_3 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c5_3.sizePolicy().hasHeightForWidth())
        self.label_c5_3.setSizePolicy(sizePolicy)
        self.label_c5_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c5_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c5_3.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c5_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c5_3.setObjectName("label_c5_3")
        self.gridLayout_2.addWidget(self.label_c5_3, 5, 5, 1, 1)
        self.label_c7 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c7.sizePolicy().hasHeightForWidth())
        self.label_c7.setSizePolicy(sizePolicy)
        self.label_c7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c7.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c7.setObjectName("label_c7")
        self.gridLayout_2.addWidget(self.label_c7, 7, 3, 1, 1)
        self.label_c4 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c4.sizePolicy().hasHeightForWidth())
        self.label_c4.setSizePolicy(sizePolicy)
        self.label_c4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c4.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c4.setObjectName("label_c4")
        self.gridLayout_2.addWidget(self.label_c4, 4, 3, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.dashboard)
        self.label_30.setMinimumSize(QtCore.QSize(0, 20))
        self.label_30.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 4, 0, 1, 1)
        self.label_c6 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c6.sizePolicy().hasHeightForWidth())
        self.label_c6.setSizePolicy(sizePolicy)
        self.label_c6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c6.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c6.setObjectName("label_c6")
        self.gridLayout_2.addWidget(self.label_c6, 6, 3, 1, 1)
        self.pushButton_start = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_start.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_start.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_start.setFlat(False)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout_2.addWidget(self.pushButton_start, 1, 1, 1, 1)
        self.label_c6_2 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c6_2.sizePolicy().hasHeightForWidth())
        self.label_c6_2.setSizePolicy(sizePolicy)
        self.label_c6_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c6_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c6_2.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c6_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c6_2.setObjectName("label_c6_2")
        self.gridLayout_2.addWidget(self.label_c6_2, 6, 4, 1, 1)
        self.label_c1_4 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c1_4.sizePolicy().hasHeightForWidth())
        self.label_c1_4.setSizePolicy(sizePolicy)
        self.label_c1_4.setMinimumSize(QtCore.QSize(40, 16))
        self.label_c1_4.setMaximumSize(QtCore.QSize(16, 16))
        self.label_c1_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);\n"
"padding: 0px;\n"
"margin-left: 0px;")
        self.label_c1_4.setText("")
        self.label_c1_4.setObjectName("label_c1_4")
        self.gridLayout_2.addWidget(self.label_c1_4, 1, 6, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.dashboard)
        self.label_39.setMinimumSize(QtCore.QSize(0, 20))
        self.label_39.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.gridLayout_2.addWidget(self.label_39, 13, 0, 1, 1)
        self.label_c4_3 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c4_3.sizePolicy().hasHeightForWidth())
        self.label_c4_3.setSizePolicy(sizePolicy)
        self.label_c4_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c4_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c4_3.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c4_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c4_3.setObjectName("label_c4_3")
        self.gridLayout_2.addWidget(self.label_c4_3, 4, 5, 1, 1)
        self.label_c15_3 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c15_3.sizePolicy().hasHeightForWidth())
        self.label_c15_3.setSizePolicy(sizePolicy)
        self.label_c15_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c15_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c15_3.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c15_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c15_3.setObjectName("label_c15_3")
        self.gridLayout_2.addWidget(self.label_c15_3, 15, 5, 1, 1)
        self.label_c12_3 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c12_3.sizePolicy().hasHeightForWidth())
        self.label_c12_3.setSizePolicy(sizePolicy)
        self.label_c12_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c12_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c12_3.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c12_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c12_3.setObjectName("label_c12_3")
        self.gridLayout_2.addWidget(self.label_c12_3, 12, 5, 1, 1)
        self.label_c16_3 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c16_3.sizePolicy().hasHeightForWidth())
        self.label_c16_3.setSizePolicy(sizePolicy)
        self.label_c16_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c16_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c16_3.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c16_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c16_3.setObjectName("label_c16_3")
        self.gridLayout_2.addWidget(self.label_c16_3, 16, 5, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.dashboard)
        self.label_41.setMinimumSize(QtCore.QSize(0, 20))
        self.label_41.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_41.setStyleSheet("")
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout_2.addWidget(self.label_41, 15, 0, 1, 1)
        self.label_c11 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c11.sizePolicy().hasHeightForWidth())
        self.label_c11.setSizePolicy(sizePolicy)
        self.label_c11.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c11.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c11.setObjectName("label_c11")
        self.gridLayout_2.addWidget(self.label_c11, 11, 3, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.dashboard)
        self.label_35.setMinimumSize(QtCore.QSize(0, 20))
        self.label_35.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_2.addWidget(self.label_35, 9, 0, 1, 1)
        self.label_c16 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c16.sizePolicy().hasHeightForWidth())
        self.label_c16.setSizePolicy(sizePolicy)
        self.label_c16.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c16.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c16.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c16.setObjectName("label_c16")
        self.gridLayout_2.addWidget(self.label_c16, 16, 3, 1, 1)
        self.label_c14 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c14.sizePolicy().hasHeightForWidth())
        self.label_c14.setSizePolicy(sizePolicy)
        self.label_c14.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c14.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c14.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c14.setObjectName("label_c14")
        self.gridLayout_2.addWidget(self.label_c14, 14, 3, 1, 1)
        self.label_c13_2 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c13_2.sizePolicy().hasHeightForWidth())
        self.label_c13_2.setSizePolicy(sizePolicy)
        self.label_c13_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c13_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c13_2.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c13_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c13_2.setObjectName("label_c13_2")
        self.gridLayout_2.addWidget(self.label_c13_2, 13, 4, 1, 1)
        self.label_c13_3 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c13_3.sizePolicy().hasHeightForWidth())
        self.label_c13_3.setSizePolicy(sizePolicy)
        self.label_c13_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c13_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c13_3.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c13_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c13_3.setObjectName("label_c13_3")
        self.gridLayout_2.addWidget(self.label_c13_3, 13, 5, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.dashboard)
        self.label_40.setMinimumSize(QtCore.QSize(0, 20))
        self.label_40.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.gridLayout_2.addWidget(self.label_40, 14, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.dashboard)
        self.label_28.setMinimumSize(QtCore.QSize(0, 20))
        self.label_28.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout_2.addWidget(self.label_28, 2, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.dashboard)
        self.label_31.setMinimumSize(QtCore.QSize(0, 20))
        self.label_31.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 5, 0, 1, 1)
        self.label_c2_2 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c2_2.sizePolicy().hasHeightForWidth())
        self.label_c2_2.setSizePolicy(sizePolicy)
        self.label_c2_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c2_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c2_2.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c2_2.setObjectName("label_c2_2")
        self.gridLayout_2.addWidget(self.label_c2_2, 2, 4, 1, 1)
        self.label_c12_2 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c12_2.sizePolicy().hasHeightForWidth())
        self.label_c12_2.setSizePolicy(sizePolicy)
        self.label_c12_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c12_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c12_2.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c12_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c12_2.setObjectName("label_c12_2")
        self.gridLayout_2.addWidget(self.label_c12_2, 12, 4, 1, 1)
        self.label_c5_4 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c5_4.sizePolicy().hasHeightForWidth())
        self.label_c5_4.setSizePolicy(sizePolicy)
        self.label_c5_4.setMinimumSize(QtCore.QSize(40, 16))
        self.label_c5_4.setMaximumSize(QtCore.QSize(16, 16))
        self.label_c5_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);\n"
"padding: 0px;\n"
"margin-left: 0px;")
        self.label_c5_4.setText("")
        self.label_c5_4.setObjectName("label_c5_4")
        self.gridLayout_2.addWidget(self.label_c5_4, 5, 6, 1, 1)
        self.label_c5_2 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c5_2.sizePolicy().hasHeightForWidth())
        self.label_c5_2.setSizePolicy(sizePolicy)
        self.label_c5_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c5_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c5_2.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c5_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c5_2.setObjectName("label_c5_2")
        self.gridLayout_2.addWidget(self.label_c5_2, 5, 4, 1, 1)
        self.label_c4_4 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c4_4.sizePolicy().hasHeightForWidth())
        self.label_c4_4.setSizePolicy(sizePolicy)
        self.label_c4_4.setMinimumSize(QtCore.QSize(40, 16))
        self.label_c4_4.setMaximumSize(QtCore.QSize(16, 16))
        self.label_c4_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);\n"
"padding: 0px;\n"
"margin-left: 0px;")
        self.label_c4_4.setText("")
        self.label_c4_4.setObjectName("label_c4_4")
        self.gridLayout_2.addWidget(self.label_c4_4, 4, 6, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy)
        self.label_74.setMinimumSize(QtCore.QSize(140, 30))
        self.label_74.setMaximumSize(QtCore.QSize(140, 30))
        self.label_74.setStyleSheet("margin: 0px;\n"
"padding: 0px;\n"
"background-color: rgba(0, 0, 0, 100);\n"
"border: none;\n"
"border-radius: 15px;")
        self.label_74.setAlignment(QtCore.Qt.AlignCenter)
        self.label_74.setObjectName("label_74")
        self.gridLayout_2.addWidget(self.label_74, 0, 3, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.dashboard)
        self.label_27.setMinimumSize(QtCore.QSize(0, 20))
        self.label_27.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_27.setWhatsThis("")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 1, 0, 1, 1)
        self.label_90 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_90.sizePolicy().hasHeightForWidth())
        self.label_90.setSizePolicy(sizePolicy)
        self.label_90.setMinimumSize(QtCore.QSize(140, 30))
        self.label_90.setMaximumSize(QtCore.QSize(140, 30))
        self.label_90.setStyleSheet("margin: 0px;\n"
"padding: 0px;\n"
"background-color: rgba(0, 0, 0, 100);\n"
"border: none;\n"
"border-radius: 15px;")
        self.label_90.setAlignment(QtCore.Qt.AlignCenter)
        self.label_90.setObjectName("label_90")
        self.gridLayout_2.addWidget(self.label_90, 0, 5, 1, 1)
        self.label_c2_3 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c2_3.sizePolicy().hasHeightForWidth())
        self.label_c2_3.setSizePolicy(sizePolicy)
        self.label_c2_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c2_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c2_3.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c2_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c2_3.setObjectName("label_c2_3")
        self.gridLayout_2.addWidget(self.label_c2_3, 2, 5, 1, 1)
        self.label_c16_2 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c16_2.sizePolicy().hasHeightForWidth())
        self.label_c16_2.setSizePolicy(sizePolicy)
        self.label_c16_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c16_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c16_2.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c16_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c16_2.setObjectName("label_c16_2")
        self.gridLayout_2.addWidget(self.label_c16_2, 16, 4, 1, 1)
        self.label_c10_4 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c10_4.sizePolicy().hasHeightForWidth())
        self.label_c10_4.setSizePolicy(sizePolicy)
        self.label_c10_4.setMinimumSize(QtCore.QSize(40, 16))
        self.label_c10_4.setMaximumSize(QtCore.QSize(16, 16))
        self.label_c10_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);\n"
"padding: 0px;\n"
"margin-left: 0px;")
        self.label_c10_4.setText("")
        self.label_c10_4.setObjectName("label_c10_4")
        self.gridLayout_2.addWidget(self.label_c10_4, 10, 6, 1, 1)
        self.label_c14_3 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c14_3.sizePolicy().hasHeightForWidth())
        self.label_c14_3.setSizePolicy(sizePolicy)
        self.label_c14_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c14_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c14_3.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c14_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c14_3.setObjectName("label_c14_3")
        self.gridLayout_2.addWidget(self.label_c14_3, 14, 5, 1, 1)
        self.label_c1_2 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c1_2.sizePolicy().hasHeightForWidth())
        self.label_c1_2.setSizePolicy(sizePolicy)
        self.label_c1_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c1_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c1_2.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c1_2.setObjectName("label_c1_2")
        self.gridLayout_2.addWidget(self.label_c1_2, 1, 4, 1, 1)
        self.label_c13 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c13.sizePolicy().hasHeightForWidth())
        self.label_c13.setSizePolicy(sizePolicy)
        self.label_c13.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c13.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c13.setObjectName("label_c13")
        self.gridLayout_2.addWidget(self.label_c13, 13, 3, 1, 1)
        self.label_c9_2 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c9_2.sizePolicy().hasHeightForWidth())
        self.label_c9_2.setSizePolicy(sizePolicy)
        self.label_c9_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c9_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c9_2.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c9_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c9_2.setObjectName("label_c9_2")
        self.gridLayout_2.addWidget(self.label_c9_2, 9, 4, 1, 1)
        self.label_c15_2 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c15_2.sizePolicy().hasHeightForWidth())
        self.label_c15_2.setSizePolicy(sizePolicy)
        self.label_c15_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c15_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c15_2.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c15_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c15_2.setObjectName("label_c15_2")
        self.gridLayout_2.addWidget(self.label_c15_2, 15, 4, 1, 1)
        self.label_c6_3 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c6_3.sizePolicy().hasHeightForWidth())
        self.label_c6_3.setSizePolicy(sizePolicy)
        self.label_c6_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c6_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c6_3.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c6_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c6_3.setObjectName("label_c6_3")
        self.gridLayout_2.addWidget(self.label_c6_3, 6, 5, 1, 1)
        self.label_c10_3 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c10_3.sizePolicy().hasHeightForWidth())
        self.label_c10_3.setSizePolicy(sizePolicy)
        self.label_c10_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c10_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c10_3.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c10_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c10_3.setObjectName("label_c10_3")
        self.gridLayout_2.addWidget(self.label_c10_3, 10, 5, 1, 1)
        self.label_c8_3 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c8_3.sizePolicy().hasHeightForWidth())
        self.label_c8_3.setSizePolicy(sizePolicy)
        self.label_c8_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c8_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c8_3.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c8_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c8_3.setObjectName("label_c8_3")
        self.gridLayout_2.addWidget(self.label_c8_3, 8, 5, 1, 1)
        self.label_c6_4 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c6_4.sizePolicy().hasHeightForWidth())
        self.label_c6_4.setSizePolicy(sizePolicy)
        self.label_c6_4.setMinimumSize(QtCore.QSize(40, 16))
        self.label_c6_4.setMaximumSize(QtCore.QSize(16, 16))
        self.label_c6_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);\n"
"padding: 0px;\n"
"margin-left: 0px;")
        self.label_c6_4.setText("")
        self.label_c6_4.setObjectName("label_c6_4")
        self.gridLayout_2.addWidget(self.label_c6_4, 6, 6, 1, 1)
        self.label_c8_4 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c8_4.sizePolicy().hasHeightForWidth())
        self.label_c8_4.setSizePolicy(sizePolicy)
        self.label_c8_4.setMinimumSize(QtCore.QSize(40, 16))
        self.label_c8_4.setMaximumSize(QtCore.QSize(16, 16))
        self.label_c8_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);\n"
"padding: 0px;\n"
"margin-left: 0px;")
        self.label_c8_4.setText("")
        self.label_c8_4.setObjectName("label_c8_4")
        self.gridLayout_2.addWidget(self.label_c8_4, 8, 6, 1, 1)
        self.label_c1_3 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c1_3.sizePolicy().hasHeightForWidth())
        self.label_c1_3.setSizePolicy(sizePolicy)
        self.label_c1_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c1_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c1_3.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c1_3.setObjectName("label_c1_3")
        self.gridLayout_2.addWidget(self.label_c1_3, 1, 5, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.dashboard)
        self.label_34.setMinimumSize(QtCore.QSize(0, 20))
        self.label_34.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout_2.addWidget(self.label_34, 8, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.dashboard)
        self.label_32.setMinimumSize(QtCore.QSize(0, 20))
        self.label_32.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout_2.addWidget(self.label_32, 6, 0, 1, 1)
        self.label_c15_4 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c15_4.sizePolicy().hasHeightForWidth())
        self.label_c15_4.setSizePolicy(sizePolicy)
        self.label_c15_4.setMinimumSize(QtCore.QSize(40, 16))
        self.label_c15_4.setMaximumSize(QtCore.QSize(16, 16))
        self.label_c15_4.setStyleSheet("image: url(:/img/svg/close_icon_2.svg);\n"
"padding: 0px;\n"
"margin-left: 0px;")
        self.label_c15_4.setText("")
        self.label_c15_4.setObjectName("label_c15_4")
        self.gridLayout_2.addWidget(self.label_c15_4, 15, 6, 1, 1)
        self.label_c2 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c2.sizePolicy().hasHeightForWidth())
        self.label_c2.setSizePolicy(sizePolicy)
        self.label_c2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c2.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c2.setObjectName("label_c2")
        self.gridLayout_2.addWidget(self.label_c2, 2, 3, 1, 1)
        self.label_c3 = QtWidgets.QLabel(self.dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c3.sizePolicy().hasHeightForWidth())
        self.label_c3.setSizePolicy(sizePolicy)
        self.label_c3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_c3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_c3.setStyleSheet("margin: 0px;\n"
"padding: 0px;")
        self.label_c3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c3.setObjectName("label_c3")
        self.gridLayout_2.addWidget(self.label_c3, 3, 3, 1, 1)
        self.pushButton_stop = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_stop.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_stop.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(205, 118, 132, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(205, 118, 132, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.gridLayout_2.addWidget(self.pushButton_stop, 1, 2, 1, 1)
        self.pushButton_start_3 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_start_3.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_start_3.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start_3.setFont(font)
        self.pushButton_start_3.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_start_3.setObjectName("pushButton_start_3")
        self.gridLayout_2.addWidget(self.pushButton_start_3, 3, 1, 1, 1)
        self.pushButton_start_4 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_start_4.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_start_4.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start_4.setFont(font)
        self.pushButton_start_4.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_start_4.setObjectName("pushButton_start_4")
        self.gridLayout_2.addWidget(self.pushButton_start_4, 4, 1, 1, 1)
        self.pushButton_start_5 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_start_5.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_start_5.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start_5.setFont(font)
        self.pushButton_start_5.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_start_5.setObjectName("pushButton_start_5")
        self.gridLayout_2.addWidget(self.pushButton_start_5, 5, 1, 1, 1)
        self.pushButton_start_6 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_start_6.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_start_6.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start_6.setFont(font)
        self.pushButton_start_6.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_start_6.setObjectName("pushButton_start_6")
        self.gridLayout_2.addWidget(self.pushButton_start_6, 6, 1, 1, 1)
        self.pushButton_start_7 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_start_7.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_start_7.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start_7.setFont(font)
        self.pushButton_start_7.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_start_7.setObjectName("pushButton_start_7")
        self.gridLayout_2.addWidget(self.pushButton_start_7, 7, 1, 1, 1)
        self.pushButton_start_8 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_start_8.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_start_8.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start_8.setFont(font)
        self.pushButton_start_8.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_start_8.setObjectName("pushButton_start_8")
        self.gridLayout_2.addWidget(self.pushButton_start_8, 8, 1, 1, 1)
        self.pushButton_start_9 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_start_9.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_start_9.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start_9.setFont(font)
        self.pushButton_start_9.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_start_9.setObjectName("pushButton_start_9")
        self.gridLayout_2.addWidget(self.pushButton_start_9, 9, 1, 1, 1)
        self.pushButton_start_10 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_start_10.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_start_10.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start_10.setFont(font)
        self.pushButton_start_10.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_start_10.setObjectName("pushButton_start_10")
        self.gridLayout_2.addWidget(self.pushButton_start_10, 10, 1, 1, 1)
        self.pushButton_start_11 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_start_11.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_start_11.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start_11.setFont(font)
        self.pushButton_start_11.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_start_11.setObjectName("pushButton_start_11")
        self.gridLayout_2.addWidget(self.pushButton_start_11, 11, 1, 1, 1)
        self.pushButton_start_12 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_start_12.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_start_12.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start_12.setFont(font)
        self.pushButton_start_12.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_start_12.setObjectName("pushButton_start_12")
        self.gridLayout_2.addWidget(self.pushButton_start_12, 12, 1, 1, 1)
        self.pushButton_start_13 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_start_13.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_start_13.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start_13.setFont(font)
        self.pushButton_start_13.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_start_13.setObjectName("pushButton_start_13")
        self.gridLayout_2.addWidget(self.pushButton_start_13, 13, 1, 1, 1)
        self.pushButton_start_14 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_start_14.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_start_14.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start_14.setFont(font)
        self.pushButton_start_14.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_start_14.setObjectName("pushButton_start_14")
        self.gridLayout_2.addWidget(self.pushButton_start_14, 14, 1, 1, 1)
        self.pushButton_start_15 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_start_15.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_start_15.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start_15.setFont(font)
        self.pushButton_start_15.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_start_15.setObjectName("pushButton_start_15")
        self.gridLayout_2.addWidget(self.pushButton_start_15, 15, 1, 1, 1)
        self.pushButton_start_16 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_start_16.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_start_16.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start_16.setFont(font)
        self.pushButton_start_16.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_start_16.setObjectName("pushButton_start_16")
        self.gridLayout_2.addWidget(self.pushButton_start_16, 16, 1, 1, 1)
        self.pushButton_stop_3 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_stop_3.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_stop_3.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop_3.setFont(font)
        self.pushButton_stop_3.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(205, 118, 132, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(205, 118, 132, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_stop_3.setObjectName("pushButton_stop_3")
        self.gridLayout_2.addWidget(self.pushButton_stop_3, 3, 2, 1, 1)
        self.pushButton_stop_4 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_stop_4.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_stop_4.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop_4.setFont(font)
        self.pushButton_stop_4.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(205, 118, 132, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(205, 118, 132, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_stop_4.setObjectName("pushButton_stop_4")
        self.gridLayout_2.addWidget(self.pushButton_stop_4, 4, 2, 1, 1)
        self.pushButton_stop_5 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_stop_5.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_stop_5.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop_5.setFont(font)
        self.pushButton_stop_5.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(205, 118, 132, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(205, 118, 132, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_stop_5.setObjectName("pushButton_stop_5")
        self.gridLayout_2.addWidget(self.pushButton_stop_5, 5, 2, 1, 1)
        self.pushButton_stop_6 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_stop_6.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_stop_6.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop_6.setFont(font)
        self.pushButton_stop_6.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(205, 118, 132, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(205, 118, 132, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_stop_6.setObjectName("pushButton_stop_6")
        self.gridLayout_2.addWidget(self.pushButton_stop_6, 6, 2, 1, 1)
        self.pushButton_stop_7 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_stop_7.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_stop_7.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop_7.setFont(font)
        self.pushButton_stop_7.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(205, 118, 132, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(205, 118, 132, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_stop_7.setObjectName("pushButton_stop_7")
        self.gridLayout_2.addWidget(self.pushButton_stop_7, 7, 2, 1, 1)
        self.pushButton_stop_8 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_stop_8.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_stop_8.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop_8.setFont(font)
        self.pushButton_stop_8.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(205, 118, 132, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(205, 118, 132, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_stop_8.setObjectName("pushButton_stop_8")
        self.gridLayout_2.addWidget(self.pushButton_stop_8, 8, 2, 1, 1)
        self.pushButton_stop_9 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_stop_9.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_stop_9.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop_9.setFont(font)
        self.pushButton_stop_9.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(205, 118, 132, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(205, 118, 132, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_stop_9.setObjectName("pushButton_stop_9")
        self.gridLayout_2.addWidget(self.pushButton_stop_9, 9, 2, 1, 1)
        self.pushButton_stop_10 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_stop_10.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_stop_10.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop_10.setFont(font)
        self.pushButton_stop_10.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(205, 118, 132, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(205, 118, 132, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_stop_10.setObjectName("pushButton_stop_10")
        self.gridLayout_2.addWidget(self.pushButton_stop_10, 10, 2, 1, 1)
        self.pushButton_stop_11 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_stop_11.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_stop_11.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop_11.setFont(font)
        self.pushButton_stop_11.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(205, 118, 132, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(205, 118, 132, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_stop_11.setObjectName("pushButton_stop_11")
        self.gridLayout_2.addWidget(self.pushButton_stop_11, 11, 2, 1, 1)
        self.pushButton_stop_12 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_stop_12.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_stop_12.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop_12.setFont(font)
        self.pushButton_stop_12.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(205, 118, 132, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(205, 118, 132, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_stop_12.setObjectName("pushButton_stop_12")
        self.gridLayout_2.addWidget(self.pushButton_stop_12, 12, 2, 1, 1)
        self.pushButton_stop_13 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_stop_13.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_stop_13.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop_13.setFont(font)
        self.pushButton_stop_13.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(205, 118, 132, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(205, 118, 132, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_stop_13.setObjectName("pushButton_stop_13")
        self.gridLayout_2.addWidget(self.pushButton_stop_13, 13, 2, 1, 1)
        self.pushButton_stop_14 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_stop_14.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_stop_14.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop_14.setFont(font)
        self.pushButton_stop_14.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(205, 118, 132, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(205, 118, 132, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_stop_14.setObjectName("pushButton_stop_14")
        self.gridLayout_2.addWidget(self.pushButton_stop_14, 14, 2, 1, 1)
        self.pushButton_stop_15 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_stop_15.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_stop_15.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop_15.setFont(font)
        self.pushButton_stop_15.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(205, 118, 132, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(205, 118, 132, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_stop_15.setObjectName("pushButton_stop_15")
        self.gridLayout_2.addWidget(self.pushButton_stop_15, 15, 2, 1, 1)
        self.pushButton_stop_16 = QtWidgets.QPushButton(self.dashboard)
        self.pushButton_stop_16.setMinimumSize(QtCore.QSize(100, 20))
        self.pushButton_stop_16.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop_16.setFont(font)
        self.pushButton_stop_16.setStyleSheet("QPushButton{\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(205, 118, 132, 255);\n"
"border-radius: 10px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(205, 118, 132, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_stop_16.setObjectName("pushButton_stop_16")
        self.gridLayout_2.addWidget(self.pushButton_stop_16, 16, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        self.stackedWidget.addWidget(self.dashboard)
        self.mpd = QtWidgets.QWidget()
        self.mpd.setStyleSheet("QPushButton{\n"
"border: none;\n"
"border-radius:13px;\n"
"color: rgba(170, 170, 255, 150);\n"
"background-color: #36393F;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #36393F;\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:13px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 200);\n"
"}")
        self.mpd.setObjectName("mpd")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.mpd)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_3 = MatplotlibWidget(self.mpd)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 400))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 400))
        self.widget_3.setStyleSheet("background-color: rgba(170, 170, 255, 10);\n"
"border: none;\n"
"border-radius: 5px;")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_6.addWidget(self.widget_3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(9, 0, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.bnt_mpd_10 = QtWidgets.QPushButton(self.mpd)
        self.bnt_mpd_10.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_mpd_10.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_mpd_10.setObjectName("bnt_mpd_10")
        self.gridLayout_4.addWidget(self.bnt_mpd_10, 1, 1, 1, 1)
        self.bnt_mpd_16 = QtWidgets.QPushButton(self.mpd)
        self.bnt_mpd_16.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_mpd_16.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_mpd_16.setObjectName("bnt_mpd_16")
        self.gridLayout_4.addWidget(self.bnt_mpd_16, 1, 7, 1, 1)
        self.bnt_mpd_4 = QtWidgets.QPushButton(self.mpd)
        self.bnt_mpd_4.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_mpd_4.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_mpd_4.setObjectName("bnt_mpd_4")
        self.gridLayout_4.addWidget(self.bnt_mpd_4, 0, 3, 1, 1)
        self.bnt_mpd = QtWidgets.QPushButton(self.mpd)
        self.bnt_mpd.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_mpd.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_mpd.setObjectName("bnt_mpd")
        self.gridLayout_4.addWidget(self.bnt_mpd, 0, 0, 1, 1)
        self.bnt_mpd_7 = QtWidgets.QPushButton(self.mpd)
        self.bnt_mpd_7.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_mpd_7.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_mpd_7.setObjectName("bnt_mpd_7")
        self.gridLayout_4.addWidget(self.bnt_mpd_7, 0, 6, 1, 1)
        self.bnt_mpd_2 = QtWidgets.QPushButton(self.mpd)
        self.bnt_mpd_2.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_mpd_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_mpd_2.setObjectName("bnt_mpd_2")
        self.gridLayout_4.addWidget(self.bnt_mpd_2, 0, 1, 1, 1)
        self.bnt_mpd_5 = QtWidgets.QPushButton(self.mpd)
        self.bnt_mpd_5.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_mpd_5.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_mpd_5.setObjectName("bnt_mpd_5")
        self.gridLayout_4.addWidget(self.bnt_mpd_5, 0, 4, 1, 1)
        self.bnt_mpd_14 = QtWidgets.QPushButton(self.mpd)
        self.bnt_mpd_14.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_mpd_14.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_mpd_14.setObjectName("bnt_mpd_14")
        self.gridLayout_4.addWidget(self.bnt_mpd_14, 1, 5, 1, 1)
        self.bnt_mpd_3 = QtWidgets.QPushButton(self.mpd)
        self.bnt_mpd_3.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_mpd_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_mpd_3.setObjectName("bnt_mpd_3")
        self.gridLayout_4.addWidget(self.bnt_mpd_3, 0, 2, 1, 1)
        self.bnt_mpd_15 = QtWidgets.QPushButton(self.mpd)
        self.bnt_mpd_15.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_mpd_15.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_mpd_15.setObjectName("bnt_mpd_15")
        self.gridLayout_4.addWidget(self.bnt_mpd_15, 1, 6, 1, 1)
        self.bnt_mpd_6 = QtWidgets.QPushButton(self.mpd)
        self.bnt_mpd_6.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_mpd_6.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_mpd_6.setObjectName("bnt_mpd_6")
        self.gridLayout_4.addWidget(self.bnt_mpd_6, 0, 5, 1, 1)
        self.bnt_mpd_8 = QtWidgets.QPushButton(self.mpd)
        self.bnt_mpd_8.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_mpd_8.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_mpd_8.setObjectName("bnt_mpd_8")
        self.gridLayout_4.addWidget(self.bnt_mpd_8, 0, 7, 1, 1)
        self.bnt_mpd_13 = QtWidgets.QPushButton(self.mpd)
        self.bnt_mpd_13.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_mpd_13.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_mpd_13.setObjectName("bnt_mpd_13")
        self.gridLayout_4.addWidget(self.bnt_mpd_13, 1, 4, 1, 1)
        self.bnt_mpd_9 = QtWidgets.QPushButton(self.mpd)
        self.bnt_mpd_9.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_mpd_9.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_mpd_9.setObjectName("bnt_mpd_9")
        self.gridLayout_4.addWidget(self.bnt_mpd_9, 1, 0, 1, 1)
        self.bnt_mpd_11 = QtWidgets.QPushButton(self.mpd)
        self.bnt_mpd_11.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_mpd_11.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_mpd_11.setObjectName("bnt_mpd_11")
        self.gridLayout_4.addWidget(self.bnt_mpd_11, 1, 2, 1, 1)
        self.bnt_mpd_12 = QtWidgets.QPushButton(self.mpd)
        self.bnt_mpd_12.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_mpd_12.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_mpd_12.setObjectName("bnt_mpd_12")
        self.gridLayout_4.addWidget(self.bnt_mpd_12, 1, 3, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_4)
        self.stackedWidget.addWidget(self.mpd)
        self.thermistor = QtWidgets.QWidget()
        self.thermistor.setStyleSheet("QPushButton{\n"
"border: none;\n"
"border-radius:13px;\n"
"color: rgba(170, 170, 255, 150);\n"
"background-color: #36393F;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #36393F;\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:13px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 200);\n"
"}")
        self.thermistor.setObjectName("thermistor")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.thermistor)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_4 = MatplotlibWidget(self.thermistor)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 400))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 400))
        self.widget_4.setStyleSheet("background-color: rgba(170, 170, 255, 10);\n"
"border: none;\n"
"border-radius: 5px;")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_8.addWidget(self.widget_4)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setContentsMargins(9, 0, -1, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.bnt_them_10 = QtWidgets.QPushButton(self.thermistor)
        self.bnt_them_10.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_them_10.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_them_10.setObjectName("bnt_them_10")
        self.gridLayout_5.addWidget(self.bnt_them_10, 1, 1, 1, 1)
        self.bnt_them_16 = QtWidgets.QPushButton(self.thermistor)
        self.bnt_them_16.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_them_16.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_them_16.setObjectName("bnt_them_16")
        self.gridLayout_5.addWidget(self.bnt_them_16, 1, 7, 1, 1)
        self.bnt_them_4 = QtWidgets.QPushButton(self.thermistor)
        self.bnt_them_4.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_them_4.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_them_4.setObjectName("bnt_them_4")
        self.gridLayout_5.addWidget(self.bnt_them_4, 0, 3, 1, 1)
        self.bnt_them = QtWidgets.QPushButton(self.thermistor)
        self.bnt_them.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_them.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_them.setObjectName("bnt_them")
        self.gridLayout_5.addWidget(self.bnt_them, 0, 0, 1, 1)
        self.bnt_them_7 = QtWidgets.QPushButton(self.thermistor)
        self.bnt_them_7.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_them_7.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_them_7.setObjectName("bnt_them_7")
        self.gridLayout_5.addWidget(self.bnt_them_7, 0, 6, 1, 1)
        self.bnt_them_2 = QtWidgets.QPushButton(self.thermistor)
        self.bnt_them_2.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_them_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_them_2.setObjectName("bnt_them_2")
        self.gridLayout_5.addWidget(self.bnt_them_2, 0, 1, 1, 1)
        self.bnt_them_5 = QtWidgets.QPushButton(self.thermistor)
        self.bnt_them_5.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_them_5.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_them_5.setObjectName("bnt_them_5")
        self.gridLayout_5.addWidget(self.bnt_them_5, 0, 4, 1, 1)
        self.bnt_them_14 = QtWidgets.QPushButton(self.thermistor)
        self.bnt_them_14.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_them_14.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_them_14.setObjectName("bnt_them_14")
        self.gridLayout_5.addWidget(self.bnt_them_14, 1, 5, 1, 1)
        self.bnt_them_3 = QtWidgets.QPushButton(self.thermistor)
        self.bnt_them_3.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_them_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_them_3.setObjectName("bnt_them_3")
        self.gridLayout_5.addWidget(self.bnt_them_3, 0, 2, 1, 1)
        self.bnt_them_15 = QtWidgets.QPushButton(self.thermistor)
        self.bnt_them_15.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_them_15.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_them_15.setObjectName("bnt_them_15")
        self.gridLayout_5.addWidget(self.bnt_them_15, 1, 6, 1, 1)
        self.bnt_them_6 = QtWidgets.QPushButton(self.thermistor)
        self.bnt_them_6.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_them_6.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_them_6.setObjectName("bnt_them_6")
        self.gridLayout_5.addWidget(self.bnt_them_6, 0, 5, 1, 1)
        self.bnt_them_8 = QtWidgets.QPushButton(self.thermistor)
        self.bnt_them_8.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_them_8.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_them_8.setObjectName("bnt_them_8")
        self.gridLayout_5.addWidget(self.bnt_them_8, 0, 7, 1, 1)
        self.bnt_them_13 = QtWidgets.QPushButton(self.thermistor)
        self.bnt_them_13.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_them_13.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_them_13.setObjectName("bnt_them_13")
        self.gridLayout_5.addWidget(self.bnt_them_13, 1, 4, 1, 1)
        self.bnt_them_9 = QtWidgets.QPushButton(self.thermistor)
        self.bnt_them_9.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_them_9.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_them_9.setObjectName("bnt_them_9")
        self.gridLayout_5.addWidget(self.bnt_them_9, 1, 0, 1, 1)
        self.bnt_them_11 = QtWidgets.QPushButton(self.thermistor)
        self.bnt_them_11.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_them_11.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_them_11.setObjectName("bnt_them_11")
        self.gridLayout_5.addWidget(self.bnt_them_11, 1, 2, 1, 1)
        self.bnt_them_12 = QtWidgets.QPushButton(self.thermistor)
        self.bnt_them_12.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_them_12.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_them_12.setObjectName("bnt_them_12")
        self.gridLayout_5.addWidget(self.bnt_them_12, 1, 3, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_5)
        self.stackedWidget.addWidget(self.thermistor)
        self.tec_volt = QtWidgets.QWidget()
        self.tec_volt.setStyleSheet("QPushButton{\n"
"border: none;\n"
"border-radius:13px;\n"
"color: rgba(170, 170, 255, 150);\n"
"background-color: #36393F;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #36393F;\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:13px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 200);\n"
"}")
        self.tec_volt.setObjectName("tec_volt")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tec_volt)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_5 = MatplotlibWidget(self.tec_volt)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 400))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 400))
        self.widget_5.setStyleSheet("background-color: rgba(170, 170, 255, 10);\n"
"border: none;\n"
"border-radius: 5px;")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_9.addWidget(self.widget_5)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setContentsMargins(9, 0, -1, -1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.bnt_tv_10 = QtWidgets.QPushButton(self.tec_volt)
        self.bnt_tv_10.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tv_10.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tv_10.setObjectName("bnt_tv_10")
        self.gridLayout_6.addWidget(self.bnt_tv_10, 1, 1, 1, 1)
        self.bnt_tv_16 = QtWidgets.QPushButton(self.tec_volt)
        self.bnt_tv_16.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tv_16.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tv_16.setObjectName("bnt_tv_16")
        self.gridLayout_6.addWidget(self.bnt_tv_16, 1, 7, 1, 1)
        self.bnt_tv_4 = QtWidgets.QPushButton(self.tec_volt)
        self.bnt_tv_4.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tv_4.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tv_4.setObjectName("bnt_tv_4")
        self.gridLayout_6.addWidget(self.bnt_tv_4, 0, 3, 1, 1)
        self.bnt_tv = QtWidgets.QPushButton(self.tec_volt)
        self.bnt_tv.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tv.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tv.setObjectName("bnt_tv")
        self.gridLayout_6.addWidget(self.bnt_tv, 0, 0, 1, 1)
        self.bnt_tv_7 = QtWidgets.QPushButton(self.tec_volt)
        self.bnt_tv_7.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tv_7.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tv_7.setObjectName("bnt_tv_7")
        self.gridLayout_6.addWidget(self.bnt_tv_7, 0, 6, 1, 1)
        self.bnt_tv_2 = QtWidgets.QPushButton(self.tec_volt)
        self.bnt_tv_2.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tv_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tv_2.setObjectName("bnt_tv_2")
        self.gridLayout_6.addWidget(self.bnt_tv_2, 0, 1, 1, 1)
        self.bnt_tv_5 = QtWidgets.QPushButton(self.tec_volt)
        self.bnt_tv_5.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tv_5.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tv_5.setObjectName("bnt_tv_5")
        self.gridLayout_6.addWidget(self.bnt_tv_5, 0, 4, 1, 1)
        self.bnt_tv_14 = QtWidgets.QPushButton(self.tec_volt)
        self.bnt_tv_14.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tv_14.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tv_14.setObjectName("bnt_tv_14")
        self.gridLayout_6.addWidget(self.bnt_tv_14, 1, 5, 1, 1)
        self.bnt_tv_3 = QtWidgets.QPushButton(self.tec_volt)
        self.bnt_tv_3.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tv_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tv_3.setObjectName("bnt_tv_3")
        self.gridLayout_6.addWidget(self.bnt_tv_3, 0, 2, 1, 1)
        self.bnt_tv_15 = QtWidgets.QPushButton(self.tec_volt)
        self.bnt_tv_15.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tv_15.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tv_15.setObjectName("bnt_tv_15")
        self.gridLayout_6.addWidget(self.bnt_tv_15, 1, 6, 1, 1)
        self.bnt_tv_6 = QtWidgets.QPushButton(self.tec_volt)
        self.bnt_tv_6.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tv_6.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tv_6.setObjectName("bnt_tv_6")
        self.gridLayout_6.addWidget(self.bnt_tv_6, 0, 5, 1, 1)
        self.bnt_tv_8 = QtWidgets.QPushButton(self.tec_volt)
        self.bnt_tv_8.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tv_8.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tv_8.setObjectName("bnt_tv_8")
        self.gridLayout_6.addWidget(self.bnt_tv_8, 0, 7, 1, 1)
        self.bnt_tv_13 = QtWidgets.QPushButton(self.tec_volt)
        self.bnt_tv_13.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tv_13.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tv_13.setObjectName("bnt_tv_13")
        self.gridLayout_6.addWidget(self.bnt_tv_13, 1, 4, 1, 1)
        self.bnt_tv_9 = QtWidgets.QPushButton(self.tec_volt)
        self.bnt_tv_9.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tv_9.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tv_9.setObjectName("bnt_tv_9")
        self.gridLayout_6.addWidget(self.bnt_tv_9, 1, 0, 1, 1)
        self.bnt_tv_11 = QtWidgets.QPushButton(self.tec_volt)
        self.bnt_tv_11.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tv_11.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tv_11.setObjectName("bnt_tv_11")
        self.gridLayout_6.addWidget(self.bnt_tv_11, 1, 2, 1, 1)
        self.bnt_tv_12 = QtWidgets.QPushButton(self.tec_volt)
        self.bnt_tv_12.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tv_12.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tv_12.setObjectName("bnt_tv_12")
        self.gridLayout_6.addWidget(self.bnt_tv_12, 1, 3, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_6)
        self.stackedWidget.addWidget(self.tec_volt)
        self.tec_curr = QtWidgets.QWidget()
        self.tec_curr.setStyleSheet("QPushButton{\n"
"border: none;\n"
"border-radius:13px;\n"
"color: rgba(170, 170, 255, 150);\n"
"background-color: #36393F;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #36393F;\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:13px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 200);\n"
"}")
        self.tec_curr.setObjectName("tec_curr")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tec_curr)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.widget_6 = MatplotlibWidget(self.tec_curr)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 400))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 400))
        self.widget_6.setStyleSheet("background-color: rgba(170, 170, 255, 10);\n"
"border: none;\n"
"border-radius: 5px;")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_10.addWidget(self.widget_6)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setContentsMargins(9, 0, -1, -1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.bnt_tc_10 = QtWidgets.QPushButton(self.tec_curr)
        self.bnt_tc_10.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tc_10.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tc_10.setObjectName("bnt_tc_10")
        self.gridLayout_7.addWidget(self.bnt_tc_10, 1, 1, 1, 1)
        self.bnt_tc_16 = QtWidgets.QPushButton(self.tec_curr)
        self.bnt_tc_16.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tc_16.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tc_16.setObjectName("bnt_tc_16")
        self.gridLayout_7.addWidget(self.bnt_tc_16, 1, 7, 1, 1)
        self.bnt_tc_4 = QtWidgets.QPushButton(self.tec_curr)
        self.bnt_tc_4.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tc_4.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tc_4.setObjectName("bnt_tc_4")
        self.gridLayout_7.addWidget(self.bnt_tc_4, 0, 3, 1, 1)
        self.bnt_tc = QtWidgets.QPushButton(self.tec_curr)
        self.bnt_tc.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tc.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tc.setObjectName("bnt_tc")
        self.gridLayout_7.addWidget(self.bnt_tc, 0, 0, 1, 1)
        self.bnt_tc_7 = QtWidgets.QPushButton(self.tec_curr)
        self.bnt_tc_7.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tc_7.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tc_7.setObjectName("bnt_tc_7")
        self.gridLayout_7.addWidget(self.bnt_tc_7, 0, 6, 1, 1)
        self.bnt_tc_2 = QtWidgets.QPushButton(self.tec_curr)
        self.bnt_tc_2.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tc_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tc_2.setObjectName("bnt_tc_2")
        self.gridLayout_7.addWidget(self.bnt_tc_2, 0, 1, 1, 1)
        self.bnt_tc_5 = QtWidgets.QPushButton(self.tec_curr)
        self.bnt_tc_5.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tc_5.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tc_5.setObjectName("bnt_tc_5")
        self.gridLayout_7.addWidget(self.bnt_tc_5, 0, 4, 1, 1)
        self.bnt_tc_14 = QtWidgets.QPushButton(self.tec_curr)
        self.bnt_tc_14.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tc_14.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tc_14.setObjectName("bnt_tc_14")
        self.gridLayout_7.addWidget(self.bnt_tc_14, 1, 5, 1, 1)
        self.bnt_tc_3 = QtWidgets.QPushButton(self.tec_curr)
        self.bnt_tc_3.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tc_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tc_3.setObjectName("bnt_tc_3")
        self.gridLayout_7.addWidget(self.bnt_tc_3, 0, 2, 1, 1)
        self.bnt_tc_15 = QtWidgets.QPushButton(self.tec_curr)
        self.bnt_tc_15.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tc_15.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tc_15.setObjectName("bnt_tc_15")
        self.gridLayout_7.addWidget(self.bnt_tc_15, 1, 6, 1, 1)
        self.bnt_tc_6 = QtWidgets.QPushButton(self.tec_curr)
        self.bnt_tc_6.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tc_6.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tc_6.setObjectName("bnt_tc_6")
        self.gridLayout_7.addWidget(self.bnt_tc_6, 0, 5, 1, 1)
        self.bnt_tc_8 = QtWidgets.QPushButton(self.tec_curr)
        self.bnt_tc_8.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tc_8.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tc_8.setObjectName("bnt_tc_8")
        self.gridLayout_7.addWidget(self.bnt_tc_8, 0, 7, 1, 1)
        self.bnt_tc_13 = QtWidgets.QPushButton(self.tec_curr)
        self.bnt_tc_13.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tc_13.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tc_13.setObjectName("bnt_tc_13")
        self.gridLayout_7.addWidget(self.bnt_tc_13, 1, 4, 1, 1)
        self.bnt_tc_9 = QtWidgets.QPushButton(self.tec_curr)
        self.bnt_tc_9.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tc_9.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tc_9.setObjectName("bnt_tc_9")
        self.gridLayout_7.addWidget(self.bnt_tc_9, 1, 0, 1, 1)
        self.bnt_tc_11 = QtWidgets.QPushButton(self.tec_curr)
        self.bnt_tc_11.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tc_11.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tc_11.setObjectName("bnt_tc_11")
        self.gridLayout_7.addWidget(self.bnt_tc_11, 1, 2, 1, 1)
        self.bnt_tc_12 = QtWidgets.QPushButton(self.tec_curr)
        self.bnt_tc_12.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_tc_12.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_tc_12.setObjectName("bnt_tc_12")
        self.gridLayout_7.addWidget(self.bnt_tc_12, 1, 3, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout_7)
        self.stackedWidget.addWidget(self.tec_curr)
        self.ld_volt = QtWidgets.QWidget()
        self.ld_volt.setStyleSheet("QPushButton{\n"
"border: none;\n"
"border-radius:13px;\n"
"color: rgba(170, 170, 255, 150);\n"
"background-color: #36393F;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #36393F;\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:13px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 200);\n"
"}")
        self.ld_volt.setObjectName("ld_volt")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.ld_volt)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.widget_7 = MatplotlibWidget(self.ld_volt)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 400))
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 400))
        self.widget_7.setStyleSheet("background-color: rgba(170, 170, 255, 10);\n"
"border: none;\n"
"border-radius: 5px;")
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_11.addWidget(self.widget_7)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setContentsMargins(9, 0, -1, -1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.bnt_ldv_10 = QtWidgets.QPushButton(self.ld_volt)
        self.bnt_ldv_10.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldv_10.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldv_10.setObjectName("bnt_ldv_10")
        self.gridLayout_8.addWidget(self.bnt_ldv_10, 1, 1, 1, 1)
        self.bnt_ldv_16 = QtWidgets.QPushButton(self.ld_volt)
        self.bnt_ldv_16.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldv_16.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldv_16.setObjectName("bnt_ldv_16")
        self.gridLayout_8.addWidget(self.bnt_ldv_16, 1, 7, 1, 1)
        self.bnt_ldv_4 = QtWidgets.QPushButton(self.ld_volt)
        self.bnt_ldv_4.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldv_4.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldv_4.setObjectName("bnt_ldv_4")
        self.gridLayout_8.addWidget(self.bnt_ldv_4, 0, 3, 1, 1)
        self.bnt_ldv = QtWidgets.QPushButton(self.ld_volt)
        self.bnt_ldv.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldv.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldv.setObjectName("bnt_ldv")
        self.gridLayout_8.addWidget(self.bnt_ldv, 0, 0, 1, 1)
        self.bnt_ldv_7 = QtWidgets.QPushButton(self.ld_volt)
        self.bnt_ldv_7.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldv_7.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldv_7.setObjectName("bnt_ldv_7")
        self.gridLayout_8.addWidget(self.bnt_ldv_7, 0, 6, 1, 1)
        self.bnt_ldv_2 = QtWidgets.QPushButton(self.ld_volt)
        self.bnt_ldv_2.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldv_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldv_2.setObjectName("bnt_ldv_2")
        self.gridLayout_8.addWidget(self.bnt_ldv_2, 0, 1, 1, 1)
        self.bnt_ldv_5 = QtWidgets.QPushButton(self.ld_volt)
        self.bnt_ldv_5.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldv_5.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldv_5.setObjectName("bnt_ldv_5")
        self.gridLayout_8.addWidget(self.bnt_ldv_5, 0, 4, 1, 1)
        self.bnt_ldv_14 = QtWidgets.QPushButton(self.ld_volt)
        self.bnt_ldv_14.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldv_14.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldv_14.setObjectName("bnt_ldv_14")
        self.gridLayout_8.addWidget(self.bnt_ldv_14, 1, 5, 1, 1)
        self.bnt_ldv_3 = QtWidgets.QPushButton(self.ld_volt)
        self.bnt_ldv_3.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldv_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldv_3.setObjectName("bnt_ldv_3")
        self.gridLayout_8.addWidget(self.bnt_ldv_3, 0, 2, 1, 1)
        self.bnt_ldv_15 = QtWidgets.QPushButton(self.ld_volt)
        self.bnt_ldv_15.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldv_15.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldv_15.setObjectName("bnt_ldv_15")
        self.gridLayout_8.addWidget(self.bnt_ldv_15, 1, 6, 1, 1)
        self.bnt_ldv_6 = QtWidgets.QPushButton(self.ld_volt)
        self.bnt_ldv_6.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldv_6.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldv_6.setObjectName("bnt_ldv_6")
        self.gridLayout_8.addWidget(self.bnt_ldv_6, 0, 5, 1, 1)
        self.bnt_ldv_8 = QtWidgets.QPushButton(self.ld_volt)
        self.bnt_ldv_8.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldv_8.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldv_8.setObjectName("bnt_ldv_8")
        self.gridLayout_8.addWidget(self.bnt_ldv_8, 0, 7, 1, 1)
        self.bnt_ldv_13 = QtWidgets.QPushButton(self.ld_volt)
        self.bnt_ldv_13.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldv_13.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldv_13.setObjectName("bnt_ldv_13")
        self.gridLayout_8.addWidget(self.bnt_ldv_13, 1, 4, 1, 1)
        self.bnt_ldv_9 = QtWidgets.QPushButton(self.ld_volt)
        self.bnt_ldv_9.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldv_9.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldv_9.setObjectName("bnt_ldv_9")
        self.gridLayout_8.addWidget(self.bnt_ldv_9, 1, 0, 1, 1)
        self.bnt_ldv_11 = QtWidgets.QPushButton(self.ld_volt)
        self.bnt_ldv_11.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldv_11.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldv_11.setObjectName("bnt_ldv_11")
        self.gridLayout_8.addWidget(self.bnt_ldv_11, 1, 2, 1, 1)
        self.bnt_ldv_12 = QtWidgets.QPushButton(self.ld_volt)
        self.bnt_ldv_12.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldv_12.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldv_12.setObjectName("bnt_ldv_12")
        self.gridLayout_8.addWidget(self.bnt_ldv_12, 1, 3, 1, 1)
        self.verticalLayout_11.addLayout(self.gridLayout_8)
        self.stackedWidget.addWidget(self.ld_volt)
        self.ld_curr = QtWidgets.QWidget()
        self.ld_curr.setStyleSheet("QPushButton{\n"
"border: none;\n"
"border-radius:13px;\n"
"color: rgba(170, 170, 255, 150);\n"
"background-color: #36393F;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #36393F;\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:13px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 200);\n"
"}")
        self.ld_curr.setObjectName("ld_curr")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.ld_curr)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.widget_8 = MatplotlibWidget(self.ld_curr)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 400))
        self.widget_8.setMaximumSize(QtCore.QSize(16777215, 400))
        self.widget_8.setStyleSheet("background-color: rgba(170, 170, 255, 10);\n"
"border: none;\n"
"border-radius: 5px;")
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_12.addWidget(self.widget_8)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setContentsMargins(9, 0, -1, -1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.bnt_ldc_10 = QtWidgets.QPushButton(self.ld_curr)
        self.bnt_ldc_10.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldc_10.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldc_10.setObjectName("bnt_ldc_10")
        self.gridLayout_9.addWidget(self.bnt_ldc_10, 1, 1, 1, 1)
        self.bnt_ldc_16 = QtWidgets.QPushButton(self.ld_curr)
        self.bnt_ldc_16.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldc_16.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldc_16.setObjectName("bnt_ldc_16")
        self.gridLayout_9.addWidget(self.bnt_ldc_16, 1, 7, 1, 1)
        self.bnt_ldc_4 = QtWidgets.QPushButton(self.ld_curr)
        self.bnt_ldc_4.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldc_4.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldc_4.setObjectName("bnt_ldc_4")
        self.gridLayout_9.addWidget(self.bnt_ldc_4, 0, 3, 1, 1)
        self.bnt_ldc = QtWidgets.QPushButton(self.ld_curr)
        self.bnt_ldc.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldc.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldc.setObjectName("bnt_ldc")
        self.gridLayout_9.addWidget(self.bnt_ldc, 0, 0, 1, 1)
        self.bnt_ldc_7 = QtWidgets.QPushButton(self.ld_curr)
        self.bnt_ldc_7.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldc_7.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldc_7.setObjectName("bnt_ldc_7")
        self.gridLayout_9.addWidget(self.bnt_ldc_7, 0, 6, 1, 1)
        self.bnt_ldc_2 = QtWidgets.QPushButton(self.ld_curr)
        self.bnt_ldc_2.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldc_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldc_2.setObjectName("bnt_ldc_2")
        self.gridLayout_9.addWidget(self.bnt_ldc_2, 0, 1, 1, 1)
        self.bnt_ldc_5 = QtWidgets.QPushButton(self.ld_curr)
        self.bnt_ldc_5.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldc_5.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldc_5.setObjectName("bnt_ldc_5")
        self.gridLayout_9.addWidget(self.bnt_ldc_5, 0, 4, 1, 1)
        self.bnt_ldc_14 = QtWidgets.QPushButton(self.ld_curr)
        self.bnt_ldc_14.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldc_14.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldc_14.setObjectName("bnt_ldc_14")
        self.gridLayout_9.addWidget(self.bnt_ldc_14, 1, 5, 1, 1)
        self.bnt_ldc_3 = QtWidgets.QPushButton(self.ld_curr)
        self.bnt_ldc_3.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldc_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldc_3.setObjectName("bnt_ldc_3")
        self.gridLayout_9.addWidget(self.bnt_ldc_3, 0, 2, 1, 1)
        self.bnt_ldc_15 = QtWidgets.QPushButton(self.ld_curr)
        self.bnt_ldc_15.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldc_15.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldc_15.setObjectName("bnt_ldc_15")
        self.gridLayout_9.addWidget(self.bnt_ldc_15, 1, 6, 1, 1)
        self.bnt_ldc_6 = QtWidgets.QPushButton(self.ld_curr)
        self.bnt_ldc_6.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldc_6.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldc_6.setObjectName("bnt_ldc_6")
        self.gridLayout_9.addWidget(self.bnt_ldc_6, 0, 5, 1, 1)
        self.bnt_ldc_8 = QtWidgets.QPushButton(self.ld_curr)
        self.bnt_ldc_8.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldc_8.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldc_8.setObjectName("bnt_ldc_8")
        self.gridLayout_9.addWidget(self.bnt_ldc_8, 0, 7, 1, 1)
        self.bnt_ldc_13 = QtWidgets.QPushButton(self.ld_curr)
        self.bnt_ldc_13.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldc_13.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldc_13.setObjectName("bnt_ldc_13")
        self.gridLayout_9.addWidget(self.bnt_ldc_13, 1, 4, 1, 1)
        self.bnt_ldc_9 = QtWidgets.QPushButton(self.ld_curr)
        self.bnt_ldc_9.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldc_9.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldc_9.setObjectName("bnt_ldc_9")
        self.gridLayout_9.addWidget(self.bnt_ldc_9, 1, 0, 1, 1)
        self.bnt_ldc_11 = QtWidgets.QPushButton(self.ld_curr)
        self.bnt_ldc_11.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldc_11.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldc_11.setObjectName("bnt_ldc_11")
        self.gridLayout_9.addWidget(self.bnt_ldc_11, 1, 2, 1, 1)
        self.bnt_ldc_12 = QtWidgets.QPushButton(self.ld_curr)
        self.bnt_ldc_12.setMinimumSize(QtCore.QSize(0, 25))
        self.bnt_ldc_12.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bnt_ldc_12.setObjectName("bnt_ldc_12")
        self.gridLayout_9.addWidget(self.bnt_ldc_12, 1, 3, 1, 1)
        self.verticalLayout_12.addLayout(self.gridLayout_9)
        self.stackedWidget.addWidget(self.ld_curr)
        self.setting = QtWidgets.QWidget()
        self.setting.setStyleSheet("QPushButton{\n"
"border: none;\n"
"border-radius:13px;\n"
"color: rgba(170, 170, 255, 150);\n"
"background-color: #36393F;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #36393F;\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:13px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(205, 118, 132, 200);\n"
"}\n"
"QLineEdit {\n"
"background-color: #36393F;\n"
"border:none;\n"
"border-radius: 13px;\n"
"color:rgba(255, 255, 255, 230);\n"
"padding: 5px;\n"
"margin: 0px;\n"
"}\n"
"QLabel {\n"
"color:rgba(255, 255, 255, 230);\n"
"}")
        self.setting.setObjectName("setting")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.setting)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_12 = QtWidgets.QLabel(self.setting)
        self.label_12.setMinimumSize(QtCore.QSize(150, 0))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(self.label_12)
        self.lineEdit_st = QtWidgets.QLineEdit(self.setting)
        self.lineEdit_st.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_st.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_st.setClearButtonEnabled(False)
        self.lineEdit_st.setObjectName("lineEdit_st")
        self.horizontalLayout_13.addWidget(self.lineEdit_st)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.verticalLayout_13.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_16 = QtWidgets.QLabel(self.setting)
        self.label_16.setMinimumSize(QtCore.QSize(150, 0))
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_17.addWidget(self.label_16)
        self.lineEdit_st_7 = QtWidgets.QLineEdit(self.setting)
        self.lineEdit_st_7.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_st_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_st_7.setObjectName("lineEdit_st_7")
        self.horizontalLayout_17.addWidget(self.lineEdit_st_7)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem2)
        self.verticalLayout_13.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_15 = QtWidgets.QLabel(self.setting)
        self.label_15.setMinimumSize(QtCore.QSize(150, 0))
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_16.addWidget(self.label_15)
        self.lineEdit_st_2 = QtWidgets.QLineEdit(self.setting)
        self.lineEdit_st_2.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_st_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_st_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_st_2.setObjectName("lineEdit_st_2")
        self.horizontalLayout_16.addWidget(self.lineEdit_st_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem3)
        self.verticalLayout_13.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_20 = QtWidgets.QLabel(self.setting)
        self.label_20.setMinimumSize(QtCore.QSize(150, 0))
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_22.addWidget(self.label_20)
        self.lineEdit_st_3 = QtWidgets.QLineEdit(self.setting)
        self.lineEdit_st_3.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_st_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_st_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_st_3.setObjectName("lineEdit_st_3")
        self.horizontalLayout_22.addWidget(self.lineEdit_st_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem4)
        self.verticalLayout_13.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_13 = QtWidgets.QLabel(self.setting)
        self.label_13.setMinimumSize(QtCore.QSize(150, 0))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_14.addWidget(self.label_13)
        self.lineEdit_st_4 = QtWidgets.QLineEdit(self.setting)
        self.lineEdit_st_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_st_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_st_4.setObjectName("lineEdit_st_4")
        self.horizontalLayout_14.addWidget(self.lineEdit_st_4)
        self.pushButton_st = QtWidgets.QPushButton(self.setting)
        self.pushButton_st.setMinimumSize(QtCore.QSize(100, 26))
        self.pushButton_st.setStyleSheet("image: url(:/img/svg/folder.svg);\n"
"padding-left: -40px;\n"
"text-align: right;")
        self.pushButton_st.setObjectName("pushButton_st")
        self.horizontalLayout_14.addWidget(self.pushButton_st)
        self.verticalLayout_13.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_14 = QtWidgets.QLabel(self.setting)
        self.label_14.setMinimumSize(QtCore.QSize(150, 0))
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_15.addWidget(self.label_14)
        self.lineEdit_st_5 = QtWidgets.QLineEdit(self.setting)
        self.lineEdit_st_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_st_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_st_5.setObjectName("lineEdit_st_5")
        self.horizontalLayout_15.addWidget(self.lineEdit_st_5)
        self.pushButton_st_2 = QtWidgets.QPushButton(self.setting)
        self.pushButton_st_2.setMinimumSize(QtCore.QSize(100, 26))
        self.pushButton_st_2.setStyleSheet("image: url(:/img/svg/folder.svg);\n"
"padding-left: -40px;\n"
"text-align: right;")
        self.pushButton_st_2.setObjectName("pushButton_st_2")
        self.horizontalLayout_15.addWidget(self.pushButton_st_2)
        self.verticalLayout_13.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_21 = QtWidgets.QLabel(self.setting)
        self.label_21.setMinimumSize(QtCore.QSize(150, 0))
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_23.addWidget(self.label_21)
        self.lineEdit_st_6 = QtWidgets.QTextEdit(self.setting)
        self.lineEdit_st_6.setStyleSheet("QTextEdit{\n"
"border: none;\n"
"border-radius: 13px;\n"
"background-color: #36393F;\n"
"padding: 5px;\n"
"margin: 0px;\n"
"}")
        self.lineEdit_st_6.setObjectName("lineEdit_st_6")
        self.horizontalLayout_23.addWidget(self.lineEdit_st_6)
        self.verticalLayout_13.addLayout(self.horizontalLayout_23)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem5)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_st_3 = QtWidgets.QPushButton(self.setting)
        self.pushButton_st_3.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_st_3.setObjectName("pushButton_st_3")
        self.horizontalLayout_12.addWidget(self.pushButton_st_3)
        self.pushButton_st_4 = QtWidgets.QPushButton(self.setting)
        self.pushButton_st_4.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_st_4.setObjectName("pushButton_st_4")
        self.horizontalLayout_12.addWidget(self.pushButton_st_4)
        self.verticalLayout_13.addLayout(self.horizontalLayout_12)
        self.stackedWidget.addWidget(self.setting)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_window_max.clicked.connect(MainWindow.showFullScreen)
        self.pushButton_windows_close.clicked.connect(MainWindow.close)
        self.pushButton_windows_min.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_home, self.btn_mpd)
        MainWindow.setTabOrder(self.btn_mpd, self.btn_ther)
        MainWindow.setTabOrder(self.btn_ther, self.btn_tec_volt)
        MainWindow.setTabOrder(self.btn_tec_volt, self.btn_tec_curr)
        MainWindow.setTabOrder(self.btn_tec_curr, self.btn_ld_volt)
        MainWindow.setTabOrder(self.btn_ld_volt, self.btn_ld_curr)
        MainWindow.setTabOrder(self.btn_ld_curr, self.btn_setting)
        MainWindow.setTabOrder(self.btn_setting, self.pushButton_windows_close)
        MainWindow.setTabOrder(self.pushButton_windows_close, self.pushButton_windows_min)
        MainWindow.setTabOrder(self.pushButton_windows_min, self.pushButton_window_max)
        MainWindow.setTabOrder(self.pushButton_window_max, self.pushButton_stop)
        MainWindow.setTabOrder(self.pushButton_stop, self.pushButton_start)
        MainWindow.setTabOrder(self.pushButton_start, self.pushButton_start_2)
        MainWindow.setTabOrder(self.pushButton_start_2, self.pushButton_stop_2)
        MainWindow.setTabOrder(self.pushButton_stop_2, self.pushButton_start_3)
        MainWindow.setTabOrder(self.pushButton_start_3, self.pushButton_start_4)
        MainWindow.setTabOrder(self.pushButton_start_4, self.pushButton_start_5)
        MainWindow.setTabOrder(self.pushButton_start_5, self.pushButton_start_6)
        MainWindow.setTabOrder(self.pushButton_start_6, self.pushButton_start_7)
        MainWindow.setTabOrder(self.pushButton_start_7, self.pushButton_start_8)
        MainWindow.setTabOrder(self.pushButton_start_8, self.pushButton_start_9)
        MainWindow.setTabOrder(self.pushButton_start_9, self.pushButton_start_10)
        MainWindow.setTabOrder(self.pushButton_start_10, self.pushButton_start_11)
        MainWindow.setTabOrder(self.pushButton_start_11, self.pushButton_start_12)
        MainWindow.setTabOrder(self.pushButton_start_12, self.pushButton_start_13)
        MainWindow.setTabOrder(self.pushButton_start_13, self.pushButton_start_14)
        MainWindow.setTabOrder(self.pushButton_start_14, self.pushButton_start_15)
        MainWindow.setTabOrder(self.pushButton_start_15, self.pushButton_start_16)
        MainWindow.setTabOrder(self.pushButton_start_16, self.pushButton_stop_3)
        MainWindow.setTabOrder(self.pushButton_stop_3, self.pushButton_stop_4)
        MainWindow.setTabOrder(self.pushButton_stop_4, self.pushButton_stop_5)
        MainWindow.setTabOrder(self.pushButton_stop_5, self.pushButton_stop_6)
        MainWindow.setTabOrder(self.pushButton_stop_6, self.pushButton_stop_7)
        MainWindow.setTabOrder(self.pushButton_stop_7, self.pushButton_stop_8)
        MainWindow.setTabOrder(self.pushButton_stop_8, self.pushButton_stop_9)
        MainWindow.setTabOrder(self.pushButton_stop_9, self.pushButton_stop_10)
        MainWindow.setTabOrder(self.pushButton_stop_10, self.pushButton_stop_11)
        MainWindow.setTabOrder(self.pushButton_stop_11, self.pushButton_stop_12)
        MainWindow.setTabOrder(self.pushButton_stop_12, self.pushButton_stop_13)
        MainWindow.setTabOrder(self.pushButton_stop_13, self.pushButton_stop_14)
        MainWindow.setTabOrder(self.pushButton_stop_14, self.pushButton_stop_15)
        MainWindow.setTabOrder(self.pushButton_stop_15, self.pushButton_stop_16)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "25G DML, EML Burn-in Program (draft)"))
        self.title_label.setText(_translate("MainWindow", "25G DML, EML Burn-in Program (draft)"))
        self.label_2.setText(_translate("MainWindow", "Menu"))
        self.btn_home.setText(_translate("MainWindow", "Home"))
        self.btn_mpd.setText(_translate("MainWindow", "MPD"))
        self.btn_ther.setText(_translate("MainWindow", "Thermistor"))
        self.btn_tec_volt.setText(_translate("MainWindow", "TEC Voltage"))
        self.btn_tec_curr.setText(_translate("MainWindow", "TEC Current"))
        self.btn_ld_volt.setText(_translate("MainWindow", "LD Voltage"))
        self.btn_ld_curr.setText(_translate("MainWindow", "LD Current"))
        self.btn_setting.setText(_translate("MainWindow", "Setting"))
        self.label.setText(_translate("MainWindow", ":: Home"))
        self.label_26.setText(_translate("MainWindow", "State infomation & Control"))
        self.pushButton_stop_2.setText(_translate("MainWindow", "Stop"))
        self.label_c8.setText(_translate("MainWindow", "00d 00h 00m 00s"))
        self.label_33.setText(_translate("MainWindow", "Ch0 7"))
        self.label_91.setText(_translate("MainWindow", "State"))
        self.label_c12.setText(_translate("MainWindow", "00d 00h 00m 00s"))
        self.label_29.setText(_translate("MainWindow", "Ch 03"))
        self.label_c11_3.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_42.setText(_translate("MainWindow", "Ch 16"))
        self.label_37.setText(_translate("MainWindow", "Ch 11"))
        self.label_c7_2.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c7_3.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_75.setText(_translate("MainWindow", "Start Time"))
        self.label_c10.setText(_translate("MainWindow", "00d 00h 00m 00s"))
        self.label_c10_2.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c1_1.setText(_translate("MainWindow", "00d 00h 00m 00s"))
        self.pushButton_start_2.setText(_translate("MainWindow", "Start"))
        self.label_36.setText(_translate("MainWindow", "Ch 10"))
        self.label_c15.setText(_translate("MainWindow", "00d 00h 00m 00s"))
        self.label_c8_2.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c14_2.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c3_3.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_38.setText(_translate("MainWindow", "Ch 12"))
        self.label_c9_3.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c5.setText(_translate("MainWindow", "00d 00h 00m 00s"))
        self.label_c9.setText(_translate("MainWindow", "00d 00h 00m 00s"))
        self.label_c11_2.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c3_2.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c4_2.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c5_3.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c7.setText(_translate("MainWindow", "00d 00h 00m 00s"))
        self.label_c4.setText(_translate("MainWindow", "00d 00h 00m 00s"))
        self.label_30.setText(_translate("MainWindow", "Ch 04"))
        self.label_c6.setText(_translate("MainWindow", "00d 00h 00m 00s"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.label_c6_2.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_39.setText(_translate("MainWindow", "Ch 13"))
        self.label_c4_3.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c15_3.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c12_3.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c16_3.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_41.setText(_translate("MainWindow", "Ch 15"))
        self.label_c11.setText(_translate("MainWindow", "00d 00h 00m 00s"))
        self.label_35.setText(_translate("MainWindow", "Ch 09"))
        self.label_c16.setText(_translate("MainWindow", "00d 00h 00m 00s"))
        self.label_c14.setText(_translate("MainWindow", "00d 00h 00m 00s"))
        self.label_c13_2.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c13_3.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_40.setText(_translate("MainWindow", "Ch 14"))
        self.label_28.setText(_translate("MainWindow", "Ch 02"))
        self.label_31.setText(_translate("MainWindow", "Ch 05"))
        self.label_c2_2.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c12_2.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c5_2.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_74.setText(_translate("MainWindow", "Time remaining"))
        self.label_27.setText(_translate("MainWindow", "Ch 01"))
        self.label_90.setText(_translate("MainWindow", "End Time"))
        self.label_c2_3.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c16_2.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c14_3.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c1_2.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c13.setText(_translate("MainWindow", "00d 00h 00m 00s"))
        self.label_c9_2.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c15_2.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c6_3.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c10_3.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c8_3.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_c1_3.setText(_translate("MainWindow", "0000-00-00 00:00:00"))
        self.label_34.setText(_translate("MainWindow", "Ch 08"))
        self.label_32.setText(_translate("MainWindow", "Ch 06"))
        self.label_c2.setText(_translate("MainWindow", "00d 00h 00m 00s"))
        self.label_c3.setText(_translate("MainWindow", "00d 00h 00m 00s"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop"))
        self.pushButton_start_3.setText(_translate("MainWindow", "Start"))
        self.pushButton_start_4.setText(_translate("MainWindow", "Start"))
        self.pushButton_start_5.setText(_translate("MainWindow", "Start"))
        self.pushButton_start_6.setText(_translate("MainWindow", "Start"))
        self.pushButton_start_7.setText(_translate("MainWindow", "Start"))
        self.pushButton_start_8.setText(_translate("MainWindow", "Start"))
        self.pushButton_start_9.setText(_translate("MainWindow", "Start"))
        self.pushButton_start_10.setText(_translate("MainWindow", "Start"))
        self.pushButton_start_11.setText(_translate("MainWindow", "Start"))
        self.pushButton_start_12.setText(_translate("MainWindow", "Start"))
        self.pushButton_start_13.setText(_translate("MainWindow", "Start"))
        self.pushButton_start_14.setText(_translate("MainWindow", "Start"))
        self.pushButton_start_15.setText(_translate("MainWindow", "Start"))
        self.pushButton_start_16.setText(_translate("MainWindow", "Start"))
        self.pushButton_stop_3.setText(_translate("MainWindow", "Stop"))
        self.pushButton_stop_4.setText(_translate("MainWindow", "Stop"))
        self.pushButton_stop_5.setText(_translate("MainWindow", "Stop"))
        self.pushButton_stop_6.setText(_translate("MainWindow", "Stop"))
        self.pushButton_stop_7.setText(_translate("MainWindow", "Stop"))
        self.pushButton_stop_8.setText(_translate("MainWindow", "Stop"))
        self.pushButton_stop_9.setText(_translate("MainWindow", "Stop"))
        self.pushButton_stop_10.setText(_translate("MainWindow", "Stop"))
        self.pushButton_stop_11.setText(_translate("MainWindow", "Stop"))
        self.pushButton_stop_12.setText(_translate("MainWindow", "Stop"))
        self.pushButton_stop_13.setText(_translate("MainWindow", "Stop"))
        self.pushButton_stop_14.setText(_translate("MainWindow", "Stop"))
        self.pushButton_stop_15.setText(_translate("MainWindow", "Stop"))
        self.pushButton_stop_16.setText(_translate("MainWindow", "Stop"))
        self.bnt_mpd_10.setText(_translate("MainWindow", "Ch 10"))
        self.bnt_mpd_16.setText(_translate("MainWindow", "Ch 16"))
        self.bnt_mpd_4.setText(_translate("MainWindow", "Ch 04"))
        self.bnt_mpd.setText(_translate("MainWindow", "Ch 01"))
        self.bnt_mpd_7.setText(_translate("MainWindow", "Ch 07"))
        self.bnt_mpd_2.setText(_translate("MainWindow", "Ch 02"))
        self.bnt_mpd_5.setText(_translate("MainWindow", "Ch 05"))
        self.bnt_mpd_14.setText(_translate("MainWindow", "Ch 14"))
        self.bnt_mpd_3.setText(_translate("MainWindow", "Ch 03"))
        self.bnt_mpd_15.setText(_translate("MainWindow", "Ch 15"))
        self.bnt_mpd_6.setText(_translate("MainWindow", "Ch 06"))
        self.bnt_mpd_8.setText(_translate("MainWindow", "Ch 08"))
        self.bnt_mpd_13.setText(_translate("MainWindow", "Ch 13"))
        self.bnt_mpd_9.setText(_translate("MainWindow", "Ch 09"))
        self.bnt_mpd_11.setText(_translate("MainWindow", "Ch 11"))
        self.bnt_mpd_12.setText(_translate("MainWindow", "Ch 12"))
        self.bnt_them_10.setText(_translate("MainWindow", "Ch 10"))
        self.bnt_them_16.setText(_translate("MainWindow", "Ch 16"))
        self.bnt_them_4.setText(_translate("MainWindow", "Ch 04"))
        self.bnt_them.setText(_translate("MainWindow", "Ch 01"))
        self.bnt_them_7.setText(_translate("MainWindow", "Ch 07"))
        self.bnt_them_2.setText(_translate("MainWindow", "Ch 02"))
        self.bnt_them_5.setText(_translate("MainWindow", "Ch 05"))
        self.bnt_them_14.setText(_translate("MainWindow", "Ch 14"))
        self.bnt_them_3.setText(_translate("MainWindow", "Ch 03"))
        self.bnt_them_15.setText(_translate("MainWindow", "Ch 15"))
        self.bnt_them_6.setText(_translate("MainWindow", "Ch 06"))
        self.bnt_them_8.setText(_translate("MainWindow", "Ch 08"))
        self.bnt_them_13.setText(_translate("MainWindow", "Ch 13"))
        self.bnt_them_9.setText(_translate("MainWindow", "Ch 09"))
        self.bnt_them_11.setText(_translate("MainWindow", "Ch 11"))
        self.bnt_them_12.setText(_translate("MainWindow", "Ch 12"))
        self.bnt_tv_10.setText(_translate("MainWindow", "Ch 10"))
        self.bnt_tv_16.setText(_translate("MainWindow", "Ch 16"))
        self.bnt_tv_4.setText(_translate("MainWindow", "Ch 04"))
        self.bnt_tv.setText(_translate("MainWindow", "Ch 01"))
        self.bnt_tv_7.setText(_translate("MainWindow", "Ch 07"))
        self.bnt_tv_2.setText(_translate("MainWindow", "Ch 02"))
        self.bnt_tv_5.setText(_translate("MainWindow", "Ch 05"))
        self.bnt_tv_14.setText(_translate("MainWindow", "Ch 14"))
        self.bnt_tv_3.setText(_translate("MainWindow", "Ch 03"))
        self.bnt_tv_15.setText(_translate("MainWindow", "Ch 15"))
        self.bnt_tv_6.setText(_translate("MainWindow", "Ch 06"))
        self.bnt_tv_8.setText(_translate("MainWindow", "Ch 08"))
        self.bnt_tv_13.setText(_translate("MainWindow", "Ch 13"))
        self.bnt_tv_9.setText(_translate("MainWindow", "Ch 09"))
        self.bnt_tv_11.setText(_translate("MainWindow", "Ch 11"))
        self.bnt_tv_12.setText(_translate("MainWindow", "Ch 12"))
        self.bnt_tc_10.setText(_translate("MainWindow", "Ch 10"))
        self.bnt_tc_16.setText(_translate("MainWindow", "Ch 16"))
        self.bnt_tc_4.setText(_translate("MainWindow", "Ch 04"))
        self.bnt_tc.setText(_translate("MainWindow", "Ch 01"))
        self.bnt_tc_7.setText(_translate("MainWindow", "Ch 07"))
        self.bnt_tc_2.setText(_translate("MainWindow", "Ch 02"))
        self.bnt_tc_5.setText(_translate("MainWindow", "Ch 05"))
        self.bnt_tc_14.setText(_translate("MainWindow", "Ch 14"))
        self.bnt_tc_3.setText(_translate("MainWindow", "Ch 03"))
        self.bnt_tc_15.setText(_translate("MainWindow", "Ch 15"))
        self.bnt_tc_6.setText(_translate("MainWindow", "Ch 06"))
        self.bnt_tc_8.setText(_translate("MainWindow", "Ch 08"))
        self.bnt_tc_13.setText(_translate("MainWindow", "Ch 13"))
        self.bnt_tc_9.setText(_translate("MainWindow", "Ch 09"))
        self.bnt_tc_11.setText(_translate("MainWindow", "Ch 11"))
        self.bnt_tc_12.setText(_translate("MainWindow", "Ch 12"))
        self.bnt_ldv_10.setText(_translate("MainWindow", "Ch 10"))
        self.bnt_ldv_16.setText(_translate("MainWindow", "Ch 16"))
        self.bnt_ldv_4.setText(_translate("MainWindow", "Ch 04"))
        self.bnt_ldv.setText(_translate("MainWindow", "Ch 01"))
        self.bnt_ldv_7.setText(_translate("MainWindow", "Ch 07"))
        self.bnt_ldv_2.setText(_translate("MainWindow", "Ch 02"))
        self.bnt_ldv_5.setText(_translate("MainWindow", "Ch 05"))
        self.bnt_ldv_14.setText(_translate("MainWindow", "Ch 14"))
        self.bnt_ldv_3.setText(_translate("MainWindow", "Ch 03"))
        self.bnt_ldv_15.setText(_translate("MainWindow", "Ch 15"))
        self.bnt_ldv_6.setText(_translate("MainWindow", "Ch 06"))
        self.bnt_ldv_8.setText(_translate("MainWindow", "Ch 08"))
        self.bnt_ldv_13.setText(_translate("MainWindow", "Ch 13"))
        self.bnt_ldv_9.setText(_translate("MainWindow", "Ch 09"))
        self.bnt_ldv_11.setText(_translate("MainWindow", "Ch 11"))
        self.bnt_ldv_12.setText(_translate("MainWindow", "Ch 12"))
        self.bnt_ldc_10.setText(_translate("MainWindow", "Ch 10"))
        self.bnt_ldc_16.setText(_translate("MainWindow", "Ch 16"))
        self.bnt_ldc_4.setText(_translate("MainWindow", "Ch 04"))
        self.bnt_ldc.setText(_translate("MainWindow", "Ch 01"))
        self.bnt_ldc_7.setText(_translate("MainWindow", "Ch 07"))
        self.bnt_ldc_2.setText(_translate("MainWindow", "Ch 02"))
        self.bnt_ldc_5.setText(_translate("MainWindow", "Ch 05"))
        self.bnt_ldc_14.setText(_translate("MainWindow", "Ch 14"))
        self.bnt_ldc_3.setText(_translate("MainWindow", "Ch 03"))
        self.bnt_ldc_15.setText(_translate("MainWindow", "Ch 15"))
        self.bnt_ldc_6.setText(_translate("MainWindow", "Ch 06"))
        self.bnt_ldc_8.setText(_translate("MainWindow", "Ch 08"))
        self.bnt_ldc_13.setText(_translate("MainWindow", "Ch 13"))
        self.bnt_ldc_9.setText(_translate("MainWindow", "Ch 09"))
        self.bnt_ldc_11.setText(_translate("MainWindow", "Ch 11"))
        self.bnt_ldc_12.setText(_translate("MainWindow", "Ch 12"))
        self.label_12.setText(_translate("MainWindow", "Duration Time (hours)"))
        self.label_16.setText(_translate("MainWindow", "Time Interval (minutes)"))
        self.label_15.setText(_translate("MainWindow", "File Name"))
        self.label_20.setText(_translate("MainWindow", "Operator"))
        self.label_13.setText(_translate("MainWindow", "Template File Open"))
        self.pushButton_st.setText(_translate("MainWindow", "Open     "))
        self.label_14.setText(_translate("MainWindow", "Save Folder Open"))
        self.pushButton_st_2.setText(_translate("MainWindow", "Open     "))
        self.label_21.setText(_translate("MainWindow", "Description"))
        self.pushButton_st_3.setText(_translate("MainWindow", "Save"))
        self.pushButton_st_4.setText(_translate("MainWindow", "Restore"))
from matplotlibwidget import MatplotlibWidget

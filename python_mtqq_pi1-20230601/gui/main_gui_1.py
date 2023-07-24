# -- coding:UTF-8
import sys
import time
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import numpy as np
import pyqtgraph as pq
from PyQt5 import QtCore,QtGui
from PyQt5.Qt import *
from pyqtgraph import PlotWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from dev.entity import global_var
from dev.mqtt_1 import Mqtt1run
from dev.mqtt_3 import mqtt_run1
from dev.mqtt_1 import message_queue_StartandStopFlag

IndividualInfoFlag = 0
InjuryInfoFlag = 0
os.environ["QT_IM_MODULE"]="qtvirtualkeyboard"
ToolButtonColor = 'rgb(0, 0, 0)'

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.__setup_ui__()

        # mqtt_run1()
        self.worker = Worker()
        self.worker1 = Worker1()
        self.valueWorker = ValueWorker()
        self.valueWorker.timerSignal.connect(self.getValue)
        self.stacked_layout.setCurrentIndex(0)
        self.start()

    def __setup_ui__(self):
        self.setWindowTitle("应急专项开发系统")
        # 获取显示器分辨率
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.screenheight = self.screenRect.height()
        self.screenwidth = self.screenRect.width()
        # self.setWindowFlags(Qt.FramelessWindowHint)  #去除窗口边框
        print("Screen height {}".format(self.screenheight))
        print("Screen width {}".format(self.screenwidth))

        # 窗口大小
        # self.resize(1000, 500)
        self.resize(self.screenwidth, self.screenheight)
        # 工具栏
        self.frame_tool = QFrame(self)
        self.frame_tool.setObjectName("frame_tool")
        self.frame_tool.setGeometry(0, 0, self.width(), 50)
        self.frame_tool.setStyleSheet("border-color: rgb(255, 255, 0);")
        self.frame_tool.setStyleSheet("border-bottom-width: 200;")
        self.frame_tool.setFrameShape(QFrame.Panel)
        self.frame_tool.setFrameShadow(QFrame.Raised)

        # 曲线测试数据
        self.data3_1 = np.zeros(300)
        self.data3_2 = np.zeros(300)
        self.data3_3 = np.zeros(300)
        self.data3_4 = np.zeros(300)
        self.data3_5 = np.zeros(300)
        self.data3_6 = np.zeros(300)
        self.data3_7 = np.zeros(300)
        self.data3_8 = np.zeros(300)
        self.data3_9 = np.zeros(300)
        self.data3_10 = np.zeros(300)
        self.data3_11 = np.zeros(300)
        self.data3_12 = np.zeros(300)

        self.data4_1 = np.zeros(300)
        self.data4_2 = np.zeros(300)
        self.data4_2 = np.zeros(60)

        self.data5_1 = np.zeros(600)
        self.data5_2 = np.zeros(600)
        self.data5_3 = np.zeros(600)

        # 设置时间
        #         self.labelTime = QLabel(self)
        #         self.labelTime.setFixedWidth(300) #200
        # #        self.labelTime.setFixedHeight(50)
        #         self.labelTime.move(0, 30)   #（0，30）
        #         self.labelTime.setStyleSheet("QLabel{background:white;}"
        #                                      "QLabel{color:rgb(300,300,300,120);font-size:15px;font-weight:bold;font-family:宋体;}"
        #                                      )
        #         # 动态显示时间在label上
        #         timer = QTimer(self)
        #         timer.timeout.connect(self.showtime)
        #         timer.start()

        # 1.1 界面1按钮
        win_btn_w = self.screenwidth / 5
        win_btn_h = 50

        self.window1_btn = QToolButton(self.frame_tool)
        self.window1_btn.setCheckable(True)
        self.window1_btn.setText("首页")
        self.window1_btn.setStyleSheet("color: " + ToolButtonColor + "; font-size: 40px; font: bold;")
        self.window1_btn.setObjectName("menu_btn")
        self.window1_btn.resize(win_btn_w, win_btn_h)  # （100,25）
        self.window1_btn.clicked.connect(self.click_window1)
        self.window1_btn.setAutoRaise(True)

        # # 1.2 界面2按钮
        # self.window2_btn = QToolButton(self.frame_tool)
        # self.window2_btn.setCheckable(True)
        # self.window2_btn.setText("舱体信息")
        # self.window2_btn.setObjectName("menu_btn")
        # self.window2_btn.resize(win_btn_w, win_btn_h)
        # self.window2_btn.move(self.window1_btn.width(), 0)
        # self.window2_btn.clicked.connect(self.click_window2)
        # self.window2_btn.setAutoRaise(True)

        # 1.3 界面3按钮
        self.window3_btn = QToolButton(self.frame_tool)
        self.window3_btn.setCheckable(True)
        self.window3_btn.setText("ECG")
        self.window3_btn.setStyleSheet("color: " + ToolButtonColor + "; font-size: 40px; font: bold;")
        self.window3_btn.setObjectName("menu_btn")
        self.window3_btn.resize(win_btn_w, win_btn_h)
        self.window3_btn.move(self.window1_btn.width(), 0)
        # self.window3_btn.move(self.window1_btn.width(), 0)
        self.window3_btn.clicked.connect(self.click_window2)
        self.window3_btn.setAutoRaise(True)

        self.btn_group = QButtonGroup(self.frame_tool)
        self.btn_group.addButton(self.window1_btn, 1)
        # self.btn_group.addButton(self.window2_btn, 2)
        self.btn_group.addButton(self.window3_btn, 2)
        # self.btn_group.

        # 1.4 界面4按钮
        self.window4_btn = QToolButton(self.frame_tool)
        self.window4_btn.setCheckable(True)
        self.window4_btn.setText("呼吸")
        self.window4_btn.setStyleSheet("color: " + ToolButtonColor + "; font-size: 40px; font: bold;")
        self.window4_btn.setObjectName("menu_btn")
        self.window4_btn.resize(win_btn_w, win_btn_h)
        self.window4_btn.move(self.window1_btn.width() + self.window3_btn.width(), 0)
        self.window4_btn.clicked.connect(self.click_window3)
        self.window4_btn.setAutoRaise(True)

        # 1.5 界面5按钮
        self.window5_btn = QToolButton(self.frame_tool)
        self.window5_btn.setCheckable(True)
        self.window5_btn.setText("心音")
        self.window5_btn.setStyleSheet("color: " + ToolButtonColor + "; font-size: 40px; font: bold;")
        self.window5_btn.setObjectName("menu_btn")
        self.window5_btn.resize(win_btn_w, win_btn_h)
        self.window5_btn.move(self.window1_btn.width() + self.window3_btn.width() + self.window4_btn.width(), 0)
        self.window5_btn.clicked.connect(self.click_window4)
        self.window5_btn.setAutoRaise(True)

        # 1.6 界面6按钮
        self.window6_btn = QToolButton(self.frame_tool)
        self.window6_btn.setCheckable(True)
        self.window6_btn.setText("设备信息")
        self.window6_btn.setStyleSheet("color: " + ToolButtonColor + "; font-size: 40px; font: bold;")
        self.window6_btn.setObjectName("menu_btn")
        self.window6_btn.resize(win_btn_w, win_btn_h)
        self.window6_btn.move(
            self.window1_btn.width() + self.window3_btn.width() + self.window4_btn.width() + self.window5_btn.width(),
            0)
        self.window6_btn.clicked.connect(self.click_window5)
        self.window6_btn.setAutoRaise(True)

        self.btn_group = QButtonGroup(self.frame_tool)
        self.btn_group.addButton(self.window1_btn, 1)
        # self.btn_group.addButton(self.window2_btn, 2)
        self.btn_group.addButton(self.window3_btn, 2)
        self.btn_group.addButton(self.window4_btn, 3)
        self.btn_group.addButton(self.window5_btn, 4)
        self.btn_group.addButton(self.window6_btn, 5)

        # 2. 工作区域
        self.main_frame = QFrame(self)
        self.main_frame.setGeometry(0, 50, self.width(), self.height() - self.frame_tool.height())
        # self.main_frame.setStyleSheet("background-color: rgb(65, 95, 255)")

        # 创建堆叠布局
        self.stacked_layout = QStackedLayout(self.main_frame)

        # 第一个布局界面 - 首页
        self.main_frame1 = QMainWindow()
        self.label1 = QLabel()
        self.frame1_bar = QStatusBar()

        self.frame1_bar.setObjectName("frame1_bar")
        self.frame1_bar.showMessage("欢迎进入frame1")
        self.title = QLabel('Title')
        self.main_frame1.setStatusBar(self.frame1_bar)

        rom_frame = QFrame(self.main_frame1)
        rom_frame.setGeometry(0, 0, self.width(), self.main_frame.height() - 25)
        rom_frame.setFrameShape(QFrame.Panel)
        rom_frame.setFrameShadow(QFrame.Raised)

        # 图片
        pix1_1 = QPixmap('a.png')
        label_pix1_1 = QLabel(self.main_frame1)
        label_pix1_1.setGeometry(1600, 40, 250, 450)
        # label_pix1_1.setStyleSheet("border: 2px solid red")
        label_pix1_1.setScaledContents(True)
        label_pix1_1.setPixmap(pix1_1)

        # 上面的
        self.label1_1_1 = QLabel('患者姓名：', self.main_frame1)
        self.label1_1_1.resize(200, 40)
        self.label1_1_1.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label1_1_1.move(30, 30)
        self.edit1_1_1 = QLineEdit(self.main_frame1)
        self.edit1_1_1.resize(170, 35)
        self.edit1_1_1.move(230, 32)
        self.edit1_1_1.setText('吴某某')
        self.edit1_1_1.setStyleSheet("background: rgb(240, 240, 240);font-size: 30px;")

        self.label1_1_2 = QLabel('患者性别：', self.main_frame1)
        self.label1_1_2.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label1_1_2.resize(200, 40)
        self.label1_1_2.move(450, 30)
        self.edit1_1_2 = QComboBox(self.main_frame1)
        self.edit1_1_2.resize(60, 35)
        self.edit1_1_2.move(650, 32)
        self.edit1_1_2.addItem("")
        self.edit1_1_2.addItem("男", 0)
        self.edit1_1_2.addItem("女", 1)
        self.edit1_1_2.setStyleSheet("color: black ; font-size: 30px")

        self.label1_1_3 = QLabel('患者血型：', self.main_frame1)
        self.label1_1_3.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label1_1_3.resize(200, 40)
        self.label1_1_3.move(750, 30)
        self.edit1_1_3 = QComboBox(self.main_frame1)
        self.edit1_1_3.resize(60, 35)
        self.edit1_1_3.move(950, 32)
        self.edit1_1_3.addItem("")
        self.edit1_1_3.addItem("A", 0)
        self.edit1_1_3.addItem("B", 1)
        self.edit1_1_3.addItem("O", 2)
        self.edit1_1_3.addItem("AB", 3)
        self.edit1_1_3.addItem("不详", 4)
        self.edit1_1_3.setStyleSheet("color: black; font-size: 30px")

        self.label1_1_9 = QLabel('患者年龄：', self.main_frame1)
        self.label1_1_9.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label1_1_9.resize(200, 40)
        self.label1_1_9.move(1050, 30)
        self.edit1_1_9 = QLineEdit(self.main_frame1)
        self.edit1_1_9.resize(50, 35)
        self.edit1_1_9.move(1250, 32)
        self.edit1_1_9.setText('102')
        self.edit1_1_9.setStyleSheet("background: rgb(240, 240, 240);font-size: 30px;")

        self.label1_1_10 = QLabel('受伤时间：', self.main_frame1)
        self.label1_1_10.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label1_1_10.resize(200, 40)
        self.label1_1_10.move(30, 100)
        self.edit1_1_10 = QDateTimeEdit(QDateTime.currentDateTime(), self.main_frame1)
        self.edit1_1_10.resize(320, 35)
        self.edit1_1_10.move(230, 102)
        self.edit1_1_10.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.edit1_1_10.setStyleSheet("border:none ;background: rgb(240, 240, 240);font-size: 30px;")

        self.label1_1_11 = QLabel('受伤类型：', self.main_frame1)
        self.label1_1_11.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label1_1_11.resize(200, 40)
        self.label1_1_11.move(750, 100)
        self.edit1_1_11 = QComboBox(self.main_frame1)
        self.edit1_1_11.addItem("")
        self.edit1_1_11.addItem("挤压综合征", 0)
        self.edit1_1_11.addItem("肺水肿", 1)
        self.edit1_1_11.addItem("热射病", 2)
        self.edit1_1_11.addItem("骨折", 3)
        self.edit1_1_11.addItem("失血性休克", 4)
        self.edit1_1_11.addItem("脑外伤", 5)
        self.edit1_1_11.addItem("其他", 6)
        self.edit1_1_11.resize(180, 35)
        self.edit1_1_11.move(950, 102)
        self.edit1_1_11.setStyleSheet("color: black; font-size: 30px")

        self.label1_1_8 = QLabel('标识：', self.main_frame1)
        self.label1_1_8.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label1_1_8.resize(120, 40)
        self.label1_1_8.move(1190, 100)
        self.edit1_1_8 = QLineEdit(self.main_frame1)
        self.edit1_1_8.resize(80, 35)
        self.edit1_1_8.move(1310, 102)
        self.edit1_1_8.setText('1000')
        self.edit1_1_8.setStyleSheet("background: rgb(240, 240, 240);font-size: 30px;")

        self.label1_1_14 = QLabel('受伤部位：', self.main_frame1)
        self.label1_1_14.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label1_1_14.resize(200, 40)
        self.label1_1_14.move(30, 170)
        self.edit1_1_14 = QComboBox(self.main_frame1)
        self.edit1_1_14.addItem("")
        self.edit1_1_14.addItem("头部", 0)
        self.edit1_1_14.addItem("五官", 1)
        self.edit1_1_14.addItem("颈部", 2)
        self.edit1_1_14.addItem("胸部", 3)
        self.edit1_1_14.addItem("腹部", 4)
        self.edit1_1_14.addItem("四肢", 5)
        self.edit1_1_14.addItem("其他", 6)
        self.edit1_1_14.resize(150, 35)
        self.edit1_1_14.move(230, 172)
        self.edit1_1_14.setStyleSheet("color: black; font-size: 30px")

        self.label1_1_12 = QLabel('特殊处置情况：', self.main_frame1)
        self.label1_1_12.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label1_1_12.resize(280, 40)
        self.label1_1_12.move(750, 170)
        # self.edit1_1_12 = QTextEdit(self.main_frame1)
        self.edit1_1_12 = QLineEdit(self.main_frame1)
        self.edit1_1_12.resize(400, 35)
        self.edit1_1_12.move(1030, 172)
        self.edit1_1_12.setStyleSheet("background: rgb(240, 240, 240);font-size: 30px;")

        self.label1_1_15 = QLabel('病情分类：', self.main_frame1)
        self.label1_1_15.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label1_1_15.resize(200, 40)
        self.label1_1_15.move(30, 240)
        self.edit1_1_15 = QComboBox(self.main_frame1)
        self.edit1_1_15.resize(130, 35)
        self.edit1_1_15.move(230, 242)
        self.edit1_1_15.addItem("")
        self.edit1_1_15.addItem("非急症", 0)
        self.edit1_1_15.addItem("急症", 1)
        self.edit1_1_15.addItem("危重", 2)
        self.edit1_1_15.addItem("濒危", 3)
        self.edit1_1_15.setStyleSheet("color: black; font-size: 30px")

        self.label1_1_13 = QLabel('受伤地点：经度', self.main_frame1)
        self.label1_1_13.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label1_1_13.resize(300, 40)
        self.label1_1_13.move(750, 240)
        self.edit1_1_13 = QLineEdit(self.main_frame1)
        self.edit1_1_13.resize(100, 35)
        self.edit1_1_13.move(1050, 242)
        self.edit1_1_13.setStyleSheet("background: rgb(240, 240, 240);font-size: 30px;")
        self.label1_1_19 = QLabel('纬度', self.main_frame1)
        self.label1_1_19.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label1_1_19.resize(100, 40)
        self.label1_1_19.move(1160, 240)
        self.edit1_1_19 = QLineEdit(self.main_frame1)
        self.edit1_1_19.resize(80, 35)
        self.edit1_1_19.move(1260, 242)
        self.edit1_1_19.setStyleSheet("background: rgb(240, 240, 240);font-size: 30px;")

        self.label1_1_4 = QLabel('紧急联系人姓名：', self.main_frame1)
        self.label1_1_4.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label1_1_4.resize(320, 40)
        self.label1_1_4.move(30, 310)
        self.edit1_1_4 = QLineEdit(self.main_frame1)
        self.edit1_1_4.resize(150, 35)
        self.edit1_1_4.move(350, 312)
        self.edit1_1_4.setText('张某某某')
        self.edit1_1_4.setStyleSheet("background: rgb(240, 240, 240);font-size: 30px;")

        self.label1_1_5 = QLabel('紧急联系人电话：', self.main_frame1)
        self.label1_1_5.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label1_1_5.resize(320, 40)
        self.label1_1_5.move(750, 310)
        self.edit1_1_5 = QLineEdit(self.main_frame1)
        self.edit1_1_5.resize(300, 35)
        self.edit1_1_5.move(1070, 312)
        self.edit1_1_5.setText('18097246792')
        self.edit1_1_5.setStyleSheet("background: rgb(240, 240, 240);font-size: 30px;")

        self.label1_1_16 = QLabel('舱体标识：', self.main_frame1)
        self.label1_1_16.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label1_1_16.resize(200, 40)
        self.label1_1_16.move(30, 380)
        self.edit1_1_16 = QLineEdit(self.main_frame1)
        self.edit1_1_16.resize(150, 35)
        self.edit1_1_16.move(230, 382)
        self.edit1_1_16.setStyleSheet("background: rgb(240, 240, 240);font-size: 30px;")

        self.label1_1_18 = QLabel('舱体类型：', self.main_frame1)
        self.label1_1_18.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label1_1_18.resize(200, 40)
        self.label1_1_18.move(750, 380)
        self.edit1_1_18 = QComboBox(self.main_frame1)
        self.edit1_1_18.resize(250, 35)
        self.edit1_1_18.move(950, 382)
        self.edit1_1_18.addItem("")
        self.edit1_1_18.addItem("ZYC 5000-20", 1)
        self.edit1_1_18.addItem("ZYC 95+55", 2)
        self.edit1_1_18.setStyleSheet("color: black; font-size: 30px")

        self.label1_1_6 = QLabel('伤员过敏史：', self.main_frame1)
        self.label1_1_6.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label1_1_6.resize(240, 40)
        self.label1_1_6.move(30, 450)
        self.edit1_1_6 = QLineEdit(self.main_frame1)
        self.edit1_1_6.resize(800, 35)
        self.edit1_1_6.move(270, 452)
        self.edit1_1_6.setStyleSheet("background: rgb(240, 240, 240);font-size: 30px;")

        self.label1_1_7 = QLabel('伤员既往病史：', self.main_frame1)
        self.label1_1_7.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label1_1_7.resize(280, 40)
        self.label1_1_7.move(30, 520)
        # self.edit1_1_7 = QTextEdit(self.main_frame1)
        self.edit1_1_7 = QLineEdit(self.main_frame1)
        self.edit1_1_7.resize(760, 35)
        self.edit1_1_7.move(310, 522)
        self.edit1_1_7.setStyleSheet("background: rgb(240, 240, 240);font-size: 30px;")

        self.label1_1_17 = QLabel('后送医院：', self.main_frame1)  # 后送医院以后需要从下发信息中获取
        self.label1_1_17.setStyleSheet("color:red; font-size: 30px")
        self.label1_1_17.resize(150, 50)
        self.label1_1_17.move(1550, 630)
        self.edit1_1_17 = QLabel('等待调度', self.main_frame1)  # 先设置为等待调度，后续获取
        self.edit1_1_17.setStyleSheet("color:red; font-size: 60px; font: bold")
        self.edit1_1_17.resize(300, 80)
        self.edit1_1_17.move(1600, 780)

        # 下面的

        self.button1 = QPushButton('发送', self.main_frame1)
        self.button1.resize(150, 110)
        self.button1.move(1100, 450)
        self.button1.clicked.connect(self.onButton1Click)
        self.button1.setStyleSheet("color: rgb(158, 88, 31); font-size: 60px")

        self.button2 = QPushButton('结束', self.main_frame1)
        self.button2.resize(150, 110)
        self.button2.move(1300, 450)
        self.button2.clicked.connect(self.onButton2Click)
        # self.button2.setEnabled(False)
        self.button2.setStyleSheet("color: rgb(158, 88, 31); font-size: 60px")
        # 图片
        pix2_1 = QPixmap('b.png')
        label_pix2_1 = QLabel(self.main_frame1)
        label_pix2_1.setGeometry(15, 650, 450, 300)
        # label_pix2_1.setStyleSheet("border: 2px solid red")
        label_pix2_1.setPixmap(pix2_1)

        # 信息显示
        # 舱体标识
        self.label2_1 = QLabel(self.main_frame1)
        self.label2_1.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label2_1.resize(450, 75)
        self.label2_1.move(550, 700)
        # 当地海拔高度
        self.label2_2 = QLabel(self.main_frame1)
        self.label2_2.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label2_2.resize(450, 75)
        self.label2_2.move(550, 770)
        # 电池电压
        self.label2_3 = QLabel(self.main_frame1)
        self.label2_3.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label2_3.resize(450, 75)
        self.label2_3.move(550, 840)
        # 舱内氧含量
        self.label2_4 = QLabel(self.main_frame1)
        self.label2_4.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label2_4.resize(450, 75)
        self.label2_4.move(920, 700)

        self.label2_5 = QLabel(self.main_frame1)
        self.label2_5.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label2_5.resize(450, 75)
        self.label2_5.move(920, 770)
        # 舱内压力（等效海拔）
        self.label2_6 = QLabel(self.main_frame1)
        self.label2_6.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label2_6.resize(550, 75)
        self.label2_6.move(920, 840)

        frame1_bar_frame = QFrame(self.main_frame1)
        frame1_bar_frame.setGeometry(0, self.main_frame.height(), self.width(), 25)

        # # 第二个布局界面 - 舱体信息

        # self.main_frame2 = QMainWindow()
        # self.frame2_bar = QStatusBar()
        # self.frame2_bar.setObjectName("frame2_bar")
        # self.main_frame2.setStatusBar(self.frame2_bar)
        # self.frame2_bar.showMessage("欢迎进入frame2")
        #
        # custom_frame = QFrame(self.main_frame2)
        # custom_frame.setGeometry(0, 0, self.width(), self.main_frame.height() - 25)
        # custom_frame.setFrameShape(QFrame.Panel)
        # custom_frame.setFrameShadow(QFrame.Raised)
        #
        # frame2_bar_frame = QFrame(self.main_frame2)
        # frame2_bar_frame.setGeometry(0, self.main_frame.height(), self.width(), 25)

        # 第三个布局界面 - ECG
        self.main_frame3 = QMainWindow()
        self.frame3_bar = QStatusBar()
        self.frame3_bar.setObjectName("frame2_bar")
        self.main_frame3.setStatusBar(self.frame3_bar)
        self.frame3_bar.showMessage("欢迎进入frame2")

        self.label3_1 = QLabel("ecgI", self.main_frame3)
        self.label3_1.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label3_1.resize(450, 75)
        self.label3_1.move(15, 15)
        self.label3_2 = QLabel("ecgII", self.main_frame3)
        self.label3_2.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label3_2.resize(450, 75)
        self.label3_2.move(15, 145)
        self.label3_3 = QLabel("ecgIII", self.main_frame3)
        self.label3_3.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label3_3.resize(450, 75)
        self.label3_3.move(15, 275)
        self.label3_4 = QLabel("ecgAvr", self.main_frame3)
        self.label3_4.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label3_4.resize(450, 75)
        self.label3_4.move(15, 405)
        self.label3_5 = QLabel("ecgAvl", self.main_frame3)
        self.label3_5.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label3_5.resize(450, 75)
        self.label3_5.move(15, 535)
        self.label3_6 = QLabel("ecgAvf", self.main_frame3)
        self.label3_6.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label3_6.resize(450, 75)
        self.label3_6.move(15, 665)
        self.label3_7 = QLabel("ecgV1", self.main_frame3)
        self.label3_7.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label3_7.resize(600, 75)
        self.label3_7.move(980, 15)
        self.label3_8 = QLabel("ecgV2", self.main_frame3)
        self.label3_8.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label3_8.resize(600, 75)
        self.label3_8.move(980, 145)
        self.label3_9 = QLabel("ecgV3", self.main_frame3)
        self.label3_9.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label3_9.resize(600, 75)
        self.label3_9.move(980, 275)
        self.label3_10 = QLabel("ecgV4", self.main_frame3)
        self.label3_10.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label3_10.resize(600, 75)
        self.label3_10.move(980, 405)
        self.label3_11 = QLabel("ecgV5", self.main_frame3)
        self.label3_11.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label3_11.resize(600, 75)
        self.label3_11.move(980, 535)
        self.label3_12 = QLabel("ecgV6", self.main_frame3)
        self.label3_12.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label3_12.resize(600, 75)
        self.label3_12.move(980, 665)
        self.label3_13 = QLabel(self.main_frame3)  # 心率
        self.label3_13.setStyleSheet("color: red; font-size: 40px; font: bold;")
        self.label3_13.resize(450, 75)
        self.label3_13.move(15, 860)

        self.plotWidget_3_1 = PlotWidget(self.main_frame3)
        self.plotWidget_3_1.setGeometry(QtCore.QRect(145, 40 + 130 * 0, 800, 120))
        self.plotWidget_3_1.setBackground(QBrush(QColor(240, 240, 240)))
        self.plotWidget_3_2 = PlotWidget(self.main_frame3)
        self.plotWidget_3_2.setGeometry(QtCore.QRect(145, 40 + 130 * 1, 800, 120))
        self.plotWidget_3_2.setBackground(QBrush(QColor(240, 240, 240)))
        self.plotWidget_3_3 = PlotWidget(self.main_frame3)
        self.plotWidget_3_3.setGeometry(QtCore.QRect(145, 40 + 130 * 2, 800, 120))
        self.plotWidget_3_3.setBackground(QBrush(QColor(240, 240, 240)))
        self.plotWidget_3_4 = PlotWidget(self.main_frame3)
        self.plotWidget_3_4.setGeometry(QtCore.QRect(145, 40 + 130 * 3, 800, 120))
        self.plotWidget_3_4.setBackground(QBrush(QColor(240, 240, 240)))
        self.plotWidget_3_5 = PlotWidget(self.main_frame3)
        self.plotWidget_3_5.setGeometry(QtCore.QRect(145, 40 + 130 * 4, 800, 120))
        self.plotWidget_3_5.setBackground(QBrush(QColor(240, 240, 240)))
        self.plotWidget_3_6 = PlotWidget(self.main_frame3)
        self.plotWidget_3_6.setGeometry(QtCore.QRect(145, 40 + 130 * 5, 800, 120))
        self.plotWidget_3_6.setBackground(QBrush(QColor(240, 240, 240)))
        self.curve3_1 = self.plotWidget_3_1.plot(self.data3_1, name="mode1", pen='b')
        self.curve3_2 = self.plotWidget_3_2.plot(self.data3_2, name="mode2", pen='b')
        self.curve3_3 = self.plotWidget_3_3.plot(self.data3_3, name="mode3", pen='b')
        self.curve3_4 = self.plotWidget_3_4.plot(self.data3_4, name="mode4", pen='b')
        self.curve3_5 = self.plotWidget_3_5.plot(self.data3_5, name="mode5", pen='b')
        self.curve3_6 = self.plotWidget_3_6.plot(self.data3_6, name="mode6", pen='b')

        self.plotWidget_3_7 = PlotWidget(self.main_frame3)
        # self.plotWidget_3_7.getAxis('left').setTextPen('r')
        self.plotWidget_3_7.setGeometry(QtCore.QRect(1100, 40 + 130 * 0, 800, 120))
        self.plotWidget_3_7.setBackground(QBrush(QColor(240, 240, 240)))
        self.plotWidget_3_8 = PlotWidget(self.main_frame3)
        self.plotWidget_3_8.setGeometry(QtCore.QRect(1100, 40 + 130 * 1, 800, 120))
        self.plotWidget_3_8.setBackground(QBrush(QColor(240, 240, 240)))
        self.plotWidget_3_9 = PlotWidget(self.main_frame3)
        self.plotWidget_3_9.setGeometry(QtCore.QRect(1100, 40 + 130 * 2, 800, 120))
        self.plotWidget_3_9.setBackground(QBrush(QColor(240, 240, 240)))
        self.plotWidget_3_10 = PlotWidget(self.main_frame3)
        self.plotWidget_3_10.setGeometry(QtCore.QRect(1100, 40 + 130 * 3, 800, 120))
        self.plotWidget_3_10.setBackground(QBrush(QColor(240, 240, 240)))
        self.plotWidget_3_11 = PlotWidget(self.main_frame3)
        self.plotWidget_3_11.setGeometry(QtCore.QRect(1100, 40 + 130 * 4, 800, 120))
        self.plotWidget_3_11.setBackground(QBrush(QColor(240, 240, 240)))
        self.plotWidget_3_12 = PlotWidget(self.main_frame3)
        self.plotWidget_3_12.setGeometry(QtCore.QRect(1100, 40 + 130 * 5, 800, 120))
        self.plotWidget_3_12.setBackground(QBrush(QColor(240, 240, 240)))
        self.curve3_7 = self.plotWidget_3_7.plot(self.data3_1, name="mode1", pen='b')
        self.curve3_8 = self.plotWidget_3_8.plot(self.data3_2, name="mode2", pen='b')
        self.curve3_9 = self.plotWidget_3_9.plot(self.data3_3, name="mode3", pen='b')
        self.curve3_10 = self.plotWidget_3_10.plot(self.data3_4, name="mode4", pen='b')
        self.curve3_11 = self.plotWidget_3_11.plot(self.data3_5, name="mode5", pen='b')
        self.curve3_12 = self.plotWidget_3_12.plot(self.data3_6, name="mode6", pen='b')

        frame3 = QFrame(self.main_frame3)
        frame3.setGeometry(0, 0, self.width(), self.main_frame.height() - 25)
        frame3.setFrameShape(QFrame.Panel)
        frame3.setFrameShadow(QFrame.Raised)

        frame3_bar_frame = QFrame(self.main_frame3)
        frame3_bar_frame.setGeometry(0, self.main_frame.height(), self.width(), 25)

        # 第四个布局界面 - 呼吸
        self.main_frame4 = QMainWindow()
        self.frame4_bar = QStatusBar()
        self.frame4_bar.setObjectName("frame3_bar")
        self.main_frame4.setStatusBar(self.frame4_bar)
        self.frame4_bar.showMessage("欢迎进入frame3")

        frame4 = QFrame(self.main_frame4)
        frame4.setGeometry(0, 0, self.width(), self.main_frame.height() - 25)
        frame4.setFrameShape(QFrame.Panel)
        frame4.setFrameShadow(QFrame.Raised)

        self.label4_1 = QLabel("RESP", self.main_frame4)
        self.label4_1.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_1.resize(450, 75)
        self.label4_1.move(15, 50)
        self.label4_2 = QLabel("CO2", self.main_frame4)
        self.label4_2.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_2.resize(450, 75)
        self.label4_2.move(15, 350)

        self.plotWidget_4_1 = PlotWidget(self.main_frame4)
        self.plotWidget_4_1.setGeometry(QtCore.QRect(120, 39, 1125, 275))
        self.plotWidget_4_1.setBackground(QBrush(QColor(240, 240, 240)))
        self.plotWidget_4_2 = PlotWidget(self.main_frame4)
        self.plotWidget_4_2.setGeometry(QtCore.QRect(120, 344, 1125, 275))
        self.plotWidget_4_2.setBackground(QBrush(QColor(240, 240, 240)))
        self.curve4_1 = self.plotWidget_4_1.plot(self.data4_1, name="mode1", pen='b')
        self.curve4_2 = self.plotWidget_4_2.plot(self.data4_2, name="mode1", pen='b')

        # 峰值压力
        self.label4_3 = QLabel(self.main_frame4)
        self.label4_3.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_3.resize(450, 75)
        self.label4_3.move(20, 630)
        # 平台压力
        self.label4_4 = QLabel(self.main_frame4)
        self.label4_4.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_4.resize(450, 75)
        self.label4_4.move(500, 630)
        # 平均压力
        self.label4_5 = QLabel(self.main_frame4)
        self.label4_5.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_5.resize(450, 75)
        self.label4_5.move(980, 630)
        # CO2_呼吸率
        self.label4_6 = QLabel(self.main_frame4)
        self.label4_6.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_6.resize(450, 75)
        self.label4_6.move(20, 730)
        # 呼末二氧化碳
        self.label4_7 = QLabel(self.main_frame4)
        self.label4_7.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_7.resize(450, 75)
        self.label4_7.move(500, 730)
        # 大气压
        self.label4_8 = QLabel(self.main_frame4)
        self.label4_8.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_8.resize(450, 75)
        self.label4_8.move(980, 730)

        # 呼吸率
        self.label4_10 = QLabel(self.main_frame4)
        self.label4_10.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_10.resize(450, 75)
        self.label4_10.move(1400, 20)
        # 氧气浓度11
        self.label4_11 = QLabel(self.main_frame4)
        self.label4_11.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_11.resize(450, 75)
        self.label4_11.move(1400, 80)
        # 潮气量
        self.label4_12 = QLabel(self.main_frame4)
        self.label4_12.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_12.resize(450, 75)
        self.label4_12.move(1400, 140)
        # 呼出潮气量
        self.label4_13 = QLabel(self.main_frame4)
        self.label4_13.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_13.resize(450, 75)
        self.label4_13.move(1400, 200)
        # 气道压力
        self.label4_14 = QLabel(self.main_frame4)
        self.label4_14.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_14.resize(450, 75)
        self.label4_14.move(1400, 260)
        # 呼末正压
        self.label4_15 = QLabel(self.main_frame4)
        self.label4_15.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_15.resize(450, 75)
        self.label4_15.move(1400, 320)
        # 氧气浓度
        self.label4_16 = QLabel(self.main_frame4)
        self.label4_16.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_16.resize(450, 75)
        self.label4_16.move(1400, 380)
        # 呼吸频率
        self.label4_17 = QLabel(self.main_frame4)
        self.label4_17.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_17.resize(450, 75)
        self.label4_17.move(1400, 440)
        # 分钟通气量
        self.label4_18 = QLabel(self.main_frame4)
        self.label4_18.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_18.resize(450, 75)
        self.label4_18.move(1400, 500)
        # 吸气时间
        self.label4_19 = QLabel(self.main_frame4)
        self.label4_19.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_19.resize(450, 75)
        self.label4_19.move(1400, 560)
        # 呼气时间
        self.label4_20 = QLabel(self.main_frame4)
        self.label4_20.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_20.resize(450, 75)
        self.label4_20.move(1400, 620)
        # 吸入潮气量
        self.label4_21 = QLabel(self.main_frame4)
        self.label4_21.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_21.resize(450, 75)
        self.label4_21.move(1400, 680)

        # 收缩压
        self.label4_22 = QLabel(self.main_frame4)
        self.label4_22.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_22.resize(450, 75)
        self.label4_22.move(20, 830)
        # 舒张压
        self.label4_23 = QLabel(self.main_frame4)
        self.label4_23.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_23.resize(450, 75)
        self.label4_23.move(500, 830)
        # 平均压
        self.label4_24 = QLabel(self.main_frame4)
        self.label4_24.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_24.resize(450, 75)
        self.label4_24.move(980, 830)

        # 体温1
        self.label4_25 = QLabel(self.main_frame4)
        self.label4_25.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_25.resize(450, 75)
        self.label4_25.move(1400, 800)
        # 体温2
        self.label4_26 = QLabel(self.main_frame4)
        self.label4_26.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_26.resize(450, 75)
        self.label4_26.move(1400, 860)

        # 气体温度
        self.label4_9 = QLabel(self.main_frame4)
        self.label4_9.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        self.label4_9.resize(450, 75)
        self.label4_9.move(1400, 740)

        frame4_bar_frame = QFrame(self.main_frame4)
        frame4_bar_frame.setGeometry(0, self.main_frame.height(), self.width(), 25)

        # 第五个布局界面
        self.main_frame5 = QMainWindow()
        self.frame5_bar = QStatusBar()
        self.frame5_bar.setObjectName("frame4_bar")
        self.main_frame5.setStatusBar(self.frame5_bar)
        self.frame5_bar.showMessage("欢迎进入frame4")

        frame5 = QFrame(self.main_frame4)
        frame5.setGeometry(0, 0, self.width(), self.main_frame.height() - 25)
        frame5.setFrameShape(QFrame.Panel)
        frame5.setFrameShadow(QFrame.Raised)

        self.label4_1 = QLabel("cdc1", self.main_frame5)
        self.label4_1.setStyleSheet("color: rgb(158, 88, 31); font-size: 30px; font: bold;")
        self.label4_1.resize(450, 75)
        self.label4_1.move(15, 39)

        self.label4_2 = QLabel("cdc2", self.main_frame5)
        self.label4_2.setStyleSheet("color: rgb(158, 88, 31); font-size: 30px; font: bold;")
        self.label4_2.resize(450, 75)
        self.label4_2.move(15, 189)

        self.label4_2 = QLabel("cdc3", self.main_frame5)
        self.label4_2.setStyleSheet("color: rgb(158, 88, 31); font-size: 30px; font: bold;")
        self.label4_2.resize(450, 75)
        self.label4_2.move(15, 339)

        # 添加 PlotWidget 控件
        self.plotWidget_5_1 = PlotWidget(self.main_frame5)
        self.plotWidget_5_1.setGeometry(QtCore.QRect(120, 39, 1650, 150))
        self.plotWidget_5_1.setBackground(QBrush(QColor(240, 240, 240)))
        self.plotWidget_5_2 = PlotWidget(self.main_frame5)
        self.plotWidget_5_2.setGeometry(QtCore.QRect(120, 195, 1650, 150))
        self.plotWidget_5_2.setBackground(QBrush(QColor(240, 240, 240)))
        self.plotWidget_5_3 = PlotWidget(self.main_frame5)
        self.plotWidget_5_3.setGeometry(QtCore.QRect(120, 350, 1650, 150))
        self.plotWidget_5_3.setBackground(QBrush(QColor(240, 240, 240)))
        self.curve5_1 = self.plotWidget_5_1.plot(self.data5_1, name="mode1", pen = pq.mkPen(color = 'b', width = 3))
        self.curve5_2 = self.plotWidget_5_2.plot(self.data5_2, name="mode1", pen = pq.mkPen(color = 'b', width = 3))
        self.curve5_3 = self.plotWidget_5_3.plot(self.data5_3, name="mode1", pen = pq.mkPen(color = 'b', width = 3))

        # TODO　设定定时器，后期可以去掉
        self.timer = pq.QtCore.QTimer()
        # 定时器信号绑定 update_data 函数
        self.timer.timeout.connect(self.update_data)
        # 定时器间隔50ms，可以理解为 50ms 刷新一次数据
        self.timer.start(50)

        frame5_bar_frame = QFrame(self.main_frame5)
        frame5_bar_frame.setGeometry(0, self.main_frame.height(), self.width(), 25)

        # 第六个布局界面
        self.main_frame6 = QMainWindow()
        self.frame6_bar = QStatusBar()
        self.frame6_bar.setObjectName("frame5_bar")
        self.main_frame6.setStatusBar(self.frame6_bar)
        self.frame6_bar.showMessage("欢迎进入frame5")

        label6_1 = QLabel('设备名称: 应急专向开发系统', self.main_frame6)
        label6_1.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        label6_1.resize(600, 75)
        label6_1.move(75, 100)
        label6_2 = QLabel('设备型号:Gateway-01', self.main_frame6)
        label6_2.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        label6_2.resize(600, 75)
        label6_2.move(75, 150)
        label6_3 = QLabel('设备功能:多通道数据转发/数据显示/边缘计算', self.main_frame6)
        label6_3.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        label6_3.resize(800, 75)
        label6_3.move(75, 200)
        label6_4 = QLabel('制造厂商:中科院空天信息创新研究院', self.main_frame6)
        label6_4.setStyleSheet("color: rgb(158, 88, 31); font-size: 40px; font: bold;")
        label6_4.resize(700, 75)
        label6_4.move(75, 250)

        frame6 = QFrame(self.main_frame6)
        frame6.setGeometry(0, 0, self.width(), self.main_frame.height() - 25)
        frame6.setFrameShape(QFrame.Panel)
        frame6.setFrameShadow(QFrame.Raised)

        frame6_bar_frame = QFrame(self.main_frame6)
        frame6_bar_frame.setGeometry(0, self.main_frame.height(), self.width(), 25)

        # 把六个布局界面放进去
        self.stacked_layout.addWidget(self.main_frame1)
        # self.stacked_layout.addWidget(self.main_frame2)
        self.stacked_layout.addWidget(self.main_frame3)
        self.stacked_layout.addWidget(self.main_frame4)
        self.stacked_layout.addWidget(self.main_frame5)
        self.stacked_layout.addWidget(self.main_frame6)

    def onButton1Click(self):
        global IndividualInfoFlag
        global StartFlag
        lingLatitude = []
        IndividualInfoFlag += 1
        # StartFlag += 1
        # 设置 flag
        global_var.set_value('IndividualInfoFlag', IndividualInfoFlag)

        # global_var.getIndividualInfofunc.release()
        global_var.set_value('StartFlag', 1)
        # global_var.set_value('EndFlag', 0)

        global_var.set_value('personName', self.edit1_1_1.text())
        global_var.set_value('personGender', self.edit1_1_2.currentData())
        global_var.set_value('personBloodType', self.edit1_1_3.currentData())
        global_var.set_value('personEmergencyContactName', self.edit1_1_4.text())
        global_var.set_value('personEmergencyContactNumber', self.edit1_1_5.text())
        global_var.set_value('personAllergies', self.edit1_1_6.text())
        global_var.set_value('personPmh', self.edit1_1_7.text())
        global_var.set_value('personId', self.edit1_1_8.text())
        global_var.set_value('personAge', self.edit1_1_9.text())

        ######################################################################这一参数先加上，以后再改GUI显示框!!!!!!
        #global_var.set_value('hospitalInfor', self.edit1_1_17.text())
        #####################################################################################################

        lingLatitude.append(float(self.edit1_1_13.text()))#获取经度
        lingLatitude.append(float(self.edit1_1_19.text()))#获取纬度
        global_var.set_value('cabinID_w', self.edit1_1_16.text())
        #global_var.set_value('cabinID_w', 100)
        global_var.set_value('injuryTime', self.edit1_1_10.text())
        global_var.set_value('injuryAddress', lingLatitude)
        global_var.set_value('injuryType', self.edit1_1_11.currentData())
        global_var.set_value('injuryParts', self.edit1_1_14.currentData())
        global_var.set_value('injurySpecialCase', self.edit1_1_12.text())
        global_var.set_value('injuryClassification', self.edit1_1_15.currentData())
        # global_var.set_value('cabinType', self.edit1_1_18.currentData())
        global_var.set_value('cabinType', 1)
        d = {
            'StartFlag': 1
        }
        message_queue_StartandStopFlag.put(d)

        self.button2.setEnabled(True)
        self.button1.setEnabled(False)


    def onButton2Click(self):
        global InjuryInfoFlag
        global EndFlag
        InjuryInfoFlag += 1
        # EndFlag += 1
        # 设置 flag
        global_var.set_value('InjuryInfoFlag', InjuryInfoFlag)
        # global_var.getInjuryInfofunc.release()
        global_var.set_value('StartFlag', 0)

        d = {
            'StartFlag': 0
        }
        message_queue_StartandStopFlag.put(d)

        self.button1.setEnabled(True)
        self.button2.setEnabled(False)
        # global_var.set_value('EndFlag', 1)
        # global_var.set_value('injuryTime', self.edit1_1_10.text())
        # global_var.set_value('injuryAddress', self.edit1_1_11.text())
        # global_var.set_value('injuryType', self.edit1_1_12.text())
        # global_var.set_value('injuryParts', self.edit1_1_13.text())
        # global_var.set_value('injurySpecialCase', self.edit1_1_14.text())
        # global_var.set_value('injuryClassification', self.edit1_1_15.text())

    #画线，分割显示区域
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        pen = QPen(Qt.black, 3, Qt.SolidLine)
        qp.setPen(pen)
        if self.stacked_layout.currentIndex() == 0:
            qp.drawLine(0, 680, self.width(), 680)
            qp.drawLine(1520, 50, 1520, self.height()-26)
        size = self.size()
        qp.end()


    # 信息展示,需添加体温1，体温2和收缩压，舒张压和平均压等参数
    def getValue(self):
        import numpy as np
        # 舱体标识
        str2_1 = '舱体标识:' + str(global_var.get_value('cabinId'))
        self.label2_1.setText(str2_1)
        str2_2 = '当地海拔高度:' + str(global_var.get_value('cabinAltitude'))
        self.label2_2.setText(str2_2)
        str2_3 = '电池电压:' + str(global_var.get_value('cabinVbat')) + 'V'
        self.label2_3.setText(str2_3)
        str2_4 = '舱内氧含量:' + str(global_var.get_value('cabinInsideO2')) + '%'
        self.label2_4.setText(str2_4)
        str2_5 = '舱内温度:' + str(round(global_var.get_value('cabinInsideTemperature') - 50, 2)) + '℃'
        self.label2_5.setText(str2_5)
        str2_6 = '舱内压力:' + str(global_var.get_value('cabinInterStress')) + 'kPa'
        self.label2_6.setText(str2_6)
        # ECG
        if (global_var.get_value('ecgI') != None):
            ecgI_list = global_var.get_value('ecgI')
            if len(ecgI_list)!=0:
                for I in ecgI_list:
                    if I != 0x8000:
                        self.data3_1[:-1] = self.data3_1[1:]
                        self.data3_1[-1] = I
                        self.curve3_1.setData(self.data3_1, pen = pq.mkPen(color = 'b', width = 3))
        if (global_var.get_value('ecgIi') != None):
            ecgIi_list = global_var.get_value('ecgIi')
            if len(ecgIi_list)!=0:
                for Ii in ecgIi_list:
                    if Ii != 0x8000:
                        self.data3_2[:-1] = self.data3_2[1:]
                        self.data3_2[-1] = Ii
                        self.curve3_2.setData(self.data3_2, pen = pq.mkPen(color = 'b', width = 3))
        '''if (global_var.get_value('ecgI') != None and global_var.get_value('ecgIi') != None):
            ecgI_list = global_var.get_value('ecgI')
            ecgIi_list = global_var.get_value('ecgIi')
            ecgI_num = len(ecgI_list)
            ecgIi_num = len(ecgIi_list)
            if ecgI_num == ecgIi_num:
                for num in range(ecgI_num):
                    if ecgI_list[num] != 0x8000 and ecgIi_list[num] != 0x8000:

                        Iii = ecgIi_list[num] - ecgI_list[num]
                        self.data3_3[:-1] = self.data3_3[1:]
                        self.data3_3[-1] = Iii
                        self.curve3_3.setData(self.data3_3, pen=pq.mkPen(color='b', width=3))

                        Avr = (ecgI_list[num] + ecgIi_list[num]) * (-0.5)
                        self.data3_4[:-1] = self.data3_4[1:]
                        self.data3_4[-1] = Avr
                        self.curve3_4.setData(self.data3_4, pen=pq.mkPen(color='b', width=3))

                        Avl = ecgI_list[num] - ecgIi_list[num] * 0.5
                        self.data3_5[:-1] = self.data3_5[1:]
                        self.data3_5[-1] = Avl
                        self.curve3_5.setData(self.data3_5, pen=pq.mkPen(color='b', width=3))

                        Avf = ecgIi_list[num] - ecgI_list[num] * 0.5
                        self.data3_6[:-1] = self.data3_6[1:]
                        self.data3_6[-1] = Avf
                        self.curve3_6.setData(self.data3_6, pen=pq.mkPen(color='b', width=3))'''

        if (global_var.get_value('ecgIii') != None):
            ecgIii_list = global_var.get_value('ecgIii')
            if len(ecgIii_list) != 0:
                for Iii in ecgIii_list:
                    if Iii != 0x8000:
                        self.data3_3[:-1] = self.data3_3[1:]
                        self.data3_3[-1] = Iii
                        self.curve3_3.setData(self.data3_3,pen = pq.mkPen(color = 'b', width = 3))
        if (global_var.get_value('ecgAvr') != None):
            ecgAvr_list = global_var.get_value('ecgAvr')
            if len(ecgAvr_list) != 0:
                for Avr in ecgAvr_list:
                    if Avr != 0x8000:
                        self.data3_4[:-1] = self.data3_4[1:]
                        self.data3_4[-1] = Avr
                        self.curve3_4.setData(self.data3_4,pen = pq.mkPen(color = 'b', width = 3))
        if (global_var.get_value('ecgAvl') != None):
            ecgAvl_list = global_var.get_value('ecgAvl')
            if len(ecgAvl_list) != 0:
                for Avl in ecgAvl_list:
                    if Avl != 0x8000:
                        self.data3_5[:-1] = self.data3_5[1:]
                        self.data3_5[-1] = Avl
                        self.curve3_5.setData(self.data3_5,pen = pq.mkPen(color = 'b', width = 3))
        if (global_var.get_value('ecgAvf') != None):
            ecgAvf_list = global_var.get_value('ecgAvf')
            if len(ecgAvf_list) != 0:
                for Avf in ecgAvf_list:
                    if Avf != 0x8000:
                        self.data3_6[:-1] = self.data3_6[1:]
                        self.data3_6[-1] = Avf
                        self.curve3_6.setData(self.data3_6,pen = pq.mkPen(color = 'b', width = 3))
        if (global_var.get_value('ecgV1') != None):
            ecgV1_list = global_var.get_value('ecgV1')
            if len(ecgV1_list) != 0:
                for V1 in ecgV1_list:
                    if V1 != 0x8000:
                        self.data3_7[:-1] = self.data3_7[1:]
                        self.data3_7[-1] = V1
                        self.curve3_7.setData(self.data3_7,pen = pq.mkPen(color = 'b', width = 3))
        if (global_var.get_value('ecgV2') != None):
            ecgV2_list = global_var.get_value('ecgV2')
            if len(ecgV2_list) != 0:
                for V2 in ecgV2_list:
                    if V2 != 0x8000:
                        self.data3_8[:-1] = self.data3_8[1:]
                        self.data3_8[-1] = V2
                        self.curve3_8.setData(self.data3_8,pen = pq.mkPen(color = 'b', width = 3))
        if (global_var.get_value('ecgV3') != None):
            ecgV3_list = global_var.get_value('ecgV3')
            if len(ecgV3_list) != 0:
                for V3 in ecgV3_list:
                    if V3 != 0x8000:
                        self.data3_9[:-1] = self.data3_9[1:]
                        self.data3_9[-1] = V3
                        self.curve3_9.setData(self.data3_9,pen = pq.mkPen(color = 'b', width = 3))
        if (global_var.get_value('ecgV4') != None):
            ecgV4_list = global_var.get_value('ecgV4')
            if len(ecgV4_list) != 0:
                for V4 in ecgV4_list:
                    if V4 != 0x8000:
                        self.data3_10[:-1] = self.data3_10[1:]
                        self.data3_10[-1] = V4
                        self.curve3_10.setData(self.data3_10,pen = pq.mkPen(color = 'b', width = 3))
        if (global_var.get_value('ecgV5') != None):
            ecgV5_list = global_var.get_value('ecgV5')
            if len(ecgV5_list) != 0:
                for V5 in ecgV5_list:
                    if V5 != 0x8000:
                        self.data3_11[:-1] = self.data3_11[1:]
                        self.data3_11[-1] = V5
                        self.curve3_11.setData(self.data3_11,pen = pq.mkPen(color = 'b', width = 3))
        if (global_var.get_value('ecgV6') != None):
            ecgV6_list = global_var.get_value('ecgV6')
            if len(ecgV6_list) != 0:
                for V6 in ecgV6_list:
                    if V6 != 0x8000:
                        self.data3_12[:-1] = self.data3_12[1:]
                        self.data3_12[-1] = V6
                        self.curve3_12.setData(self.data3_12,pen = pq.mkPen(color = 'b', width = 3))
        str3_13 = '心率(bpm)：' + str(global_var.get_value('heartRate'))
        self.label3_13.setText(str3_13)
        # 呼吸
        if (global_var.get_value('respWave') != None):
            resp_list = global_var.get_value('respWave')
            if len(resp_list) != 0:
                for resp in resp_list:
                    if resp != 0x8000:
                        self.data4_1[:-1] = self.data4_1[1:]
                        self.data4_1[-1] = resp
                        self.curve4_1.setData(self.data4_1,pen = pq.mkPen(color = 'b', width = 3))
        if (global_var.get_value('co2Curve') != None):
            co2_list = global_var.get_value('co2Curve')
            if len(co2_list) != 0:
                for co2 in co2_list:
                    if co2 != 0x8000:
                        self.data4_2[:-1] = self.data4_2[1:]
                        self.data4_2[-1] = co2
                        self.curve4_2.setData(self.data4_2,pen = pq.mkPen(color = 'b', width = 3))
        bPeak_aver=np.mean(global_var.get_value('bPeak'))
        if bPeak_aver < 3000:
            str4_3 = '峰值压力：' + str(bPeak_aver)
            self.label4_3.setText(str4_3)
        else:
            self.label4_3.setText('峰值压力：未知')
        bPlatform_aver = np.mean(global_var.get_value('bPlatform'))
        if bPlatform_aver < 3000:
            str4_4 = '平台压力：' + str(bPlatform_aver)
            self.label4_4.setText(str4_4)
        else:
            self.label4_4.setText('平台压力：未知')
        bAvg_aver = np.mean(global_var.get_value('bAvg'))
        if bAvg_aver <= 100:
            str4_5 = '血氧：' + str(bAvg_aver)
            self.label4_5.setText(str4_5)
        else:
            self.label4_5.setText('血氧：未知')
        co2Rr_aver = np.mean(global_var.get_value('co2Rr'))
        if co2Rr_aver < 30000:
            str4_6 = 'CO2_呼吸率：' + str(co2Rr_aver)
            self.label4_6.setText(str4_6)
        else:
            self.label4_6.setText('CO2_呼吸率：未知')
        co2Etco2_aver = np.mean(global_var.get_value('co2Etco2'))
        if co2Etco2_aver < 30000:
            str4_7 = '呼末二氧化碳：' + str(co2Etco2_aver)
            self.label4_7.setText(str4_7)
        else:
            self.label4_7.setText('呼末二氧化碳：未知')
        co2BaroPress_aver = np.mean(global_var.get_value('co2BaroPress'))
        str4_8 = '大气压：' + str(co2BaroPress_aver)
        self.label4_8.setText(str4_8)
        co2GasPress_aver = np.mean(global_var.get_value('co2GasTemp'))
        str4_9 = '气体温度：' + str(co2GasPress_aver)
        self.label4_9.setText(str4_9)
        h = global_var.get_value('respRate')
        if h < 300:
            str4_10 = '呼吸率：' + str(h)
            self.label4_10.setText(str4_10)
        else:
            self.label4_10.setText('呼吸频率：未知')
        bO2_11_aver = np.mean(global_var.get_value('bO2_11'))
        if bO2_11_aver < 3000:
            str4_11 = '氧气浓度11：' + str(bO2_11_aver)
            self.label4_11.setText(str4_11)
        else:
            self.label4_11.setText('氧气浓度11：未知')
        bTidal_aver = np.mean(global_var.get_value('bTidal'))
        if bTidal_aver < 30000:
            str4_12 = '潮气量：' + str(bTidal_aver)
            self.label4_12.setText(str4_12)
        else:
            self.label4_12.setText('潮气量：未知')
        bVte_aver = np.mean(global_var.get_value('bVte'))
        if bVte_aver < 30000:
            str4_13 = '呼出潮气量：' + str(bVte_aver)
            self.label4_13.setText(str4_13)
        else:
            self.label4_13.setText('呼出潮气量：未知')
        bPmb_aver = np.mean(global_var.get_value('bPmb'))
        if bPmb_aver < 3000:
            str4_14 = '气道压力：' + str(bPmb_aver)
            self.label4_14.setText(str4_14)
        else:
            self.label4_14.setText('气道压力：未知')
        bPeepPmb_aver = np.mean(global_var.get_value('bPeepPmb'))
        if bPeepPmb_aver < 3000:
            str4_15 = '呼末正压：' + str(bPeepPmb_aver)
            self.label4_15.setText(str4_15)
        else:
            str4_15 = '呼末正压：未知'
            self.label4_15.setText(str4_15)
        bO2_aver = np.mean(global_var.get_value('bO2'))
        if bO2_aver < 3000:
            str4_16 = '氧气浓度：' + str(bO2_aver)
            self.label4_16.setText(str4_16)
        else:
            self.label4_16.setText('氧气浓度：未知')
        bHz_aver = np.mean(global_var.get_value('bHz'))
        if bHz_aver < 300:
            str4_17 = '呼吸频率：' + str(bHz_aver)
            self.label4_17.setText(str4_17)
        else:
            self.label4_17.setText('呼吸频率：未知')
        bFztql_aver = np.mean(global_var.get_value('bFztql'))
        if bFztql_aver < 300:
            str4_18 = '分钟通气量：' + str(bFztql_aver)
            self.label4_18.setText(str4_18)
        else:
            self.label4_18.setText('分钟通气量：未知')
        bTinsp_aver = np.mean(global_var.get_value('bTinsp'))
        if bTinsp_aver < 300:
            str4_19 = '吸气时间：' + str(bTinsp_aver)
            self.label4_19.setText(str4_19)
        else:
            self.label4_19.setText('吸气时间：未知')
        bHuqi_aver = np.mean(global_var.get_value('bHuqi'))
        str4_20 = '呼气时间：' + str(bHuqi_aver)
        self.label4_20.setText(str4_20)
        bXrTidal_aver = np.mean(global_var.get_value('bXrTidal'))
        str4_21 = '吸入潮气量：' + str(bXrTidal_aver)
        self.label4_21.setText(str4_21)
        h_bpressh_aver = np.mean(global_var.get_value('h_bpressh'))
        if h_bpressh_aver < 300:
            str4_22 = '收缩压：' + str(h_bpressh_aver)
            self.label4_22.setText(str4_22)
        else:
            self.label4_22.setText('收缩压：未知')
        h_bpressl_aver = np.mean(global_var.get_value('h_bpressl'))
        if h_bpressl_aver < 300:
            str4_23 = '舒张压：' + str(h_bpressl_aver)
            self.label4_23.setText(str4_23)
        else:
            self.label4_23.setText('舒张压：未知')
        h_bpressv_aver = np.mean(global_var.get_value('h_bpressv'))
        if h_bpressv_aver < 300:
            str4_24 = '平均压：' + str(h_bpressv_aver)
            self.label4_24.setText(str4_24)
        else:
            self.label4_24.setText('平均压：未知')
        h_temp1_aver = np.mean(global_var.get_value('h_temp1'))
        if h_temp1_aver < 50:
            str4_25 = '体温1：' + str(h_temp1_aver)
            self.label4_25.setText(str4_25)
        else:
            self.label4_25.setText('体温1：未知')
        h_temp2_aver = np.mean(global_var.get_value('h_temp2'))
        if h_temp2_aver < 50:
            str4_26 = '体温2：' + str(h_temp2_aver)
            self.label4_26.setText(str4_26)
        else:
            self.label4_26.setText('体温2：未知')

        #心音
        if (global_var.get_value('cardiechema1') != None):
            cardiechema1_list = global_var.get_value('cardiechema1')
            if len(cardiechema1_list) != 0:
                for card in cardiechema1_list:
                    if card != 0x8000:
                        self.data5_1[:-1] = self.data5_1[1:]
                        self.data5_1[-1] = card
                        self.curve5_1.setData(self.data5_1)
        if (global_var.get_value('cardiechema2') != None):
            cardiechema2_list = global_var.get_value('cardiechema2')
            if len(cardiechema2_list) != 0:
                for card in cardiechema2_list:
                    if card != 0x8000:
                        self.data5_2[:-1] = self.data5_2[1:]
                        self.data5_2[-1] = card
                        self.curve5_2.setData(self.data5_2)
        if (global_var.get_value('cardiechema3') != None):
            cardiechema3_list = global_var.get_value('cardiechema3')
            if len(cardiechema3_list) != 0:
                for card in cardiechema3_list:
                    if card != 0x8000:
                        self.data5_3[:-1] = self.data5_3[1:]
                        self.data5_3[-1] = card
                        self.curve5_3.setData(self.data5_3)

    def start(self):
        # 启动线程
        # 自动调用类内的 run 方法
        self.worker.start()
        self.worker1.start()
        self.valueWorker.start()

    # 数据左移
    def update_data(self):
        pass

    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString()
        self.labelTime.setText("     " + text)

    def click_window1(self):
        if self.stacked_layout.currentIndex() != 0:
            self.stacked_layout.setCurrentIndex(0)
            self.frame1_bar.showMessage("欢迎进入frame1")

    def click_window2(self):
        if self.stacked_layout.currentIndex() != 1:
            self.stacked_layout.setCurrentIndex(1)
            #self.frame2_bar.showMessage("欢迎进入frame2")

    def click_window3(self):
        if self.stacked_layout.currentIndex() != 2:
            self.stacked_layout.setCurrentIndex(2)
            self.frame3_bar.showMessage("欢迎进入frame3")

    def click_window4(self):
        if self.stacked_layout.currentIndex() != 3:
            self.stacked_layout.setCurrentIndex(3)
            self.frame4_bar.showMessage("欢迎进入frame4")

    def click_window5(self):
        if self.stacked_layout.currentIndex() != 4:
            self.stacked_layout.setCurrentIndex(4)
            self.frame5_bar.showMessage("欢迎进入frame5")

    def click_window6(self):
        if self.stacked_layout.currentIndex() != 5:
            self.stacked_layout.setCurrentIndex(5)
            self.frame6_bar.showMessage("欢迎进入frame6")


class Worker(QThread):
    def __init__(self):
        super(Worker, self).__init__()

    def run(self):
        # while 持续发送
        while True:
            Mqtt1run()

class Worker1(QThread):
    def __init__(self):
        super(Worker1, self).__init__()

    def run(self):
        # while 持续发送
        while True:
            mqtt_run1()


class ValueWorker(QThread):
    timerSignal = pyqtSignal()

    def __init__(self):
        super(ValueWorker, self).__init__()

    def run(self):
        while True:
            self.timerSignal.emit()
            time.sleep(1)

def global_val_init():
    #
    # global_var.set_value('cabinID_w', 0)
    #
    # global_var.set_value('injuryTime', 0)
    # global_var.set_value('injuryAddress', 0)
    # global_var.set_value('injuryType', 0)
    # global_var.set_value('injuryParts', 0)
    # global_var.set_value('injurySpecialCase', 0)
    # global_var.set_value('injuryClassification', 0)
    #
    global_var.set_value('5G_sate_flag', 0)
    global_var.set_value('cabinId',0)
    global_var.set_value('cabinID_w',0)
    global_var.set_value('cabinType',1)
    global_var.set_value('cabinAltitude',0)
    global_var.set_value('cabinVbat',0)
    global_var.set_value('cabinInsideO2',0)
    global_var.set_value('cabinInsideTemperature',50)
    global_var.set_value('cabinInterStress',0)
    global_var.set_value('ecgI',[0])
    global_var.set_value('ecgIi',[0])
    global_var.set_value('ecgIii',[0])
    global_var.set_value('ecgAvr',[0])
    global_var.set_value('ecgAvl', [0])
    global_var.set_value('ecgAvf',[0])
    global_var.set_value('ecgV1',[0])
    global_var.set_value('ecgV2',[0])
    global_var.set_value('ecgV3',[0])
    global_var.set_value('ecgV4',[0])
    global_var.set_value('ecgV5',[0])
    global_var.set_value('ecgV6',[0])
    global_var.set_value('heartRate', 0)
    global_var.set_value('respRate',0)
    global_var.set_value('respWave',[0])
    global_var.set_value('co2Curve',[0])
    global_var.set_value('bPeak',[0])
    global_var.set_value('bPlatform',[0])
    global_var.set_value('bAvg',[0])
    global_var.set_value('co2Rr',[0])
    global_var.set_value('co2Etco2',[0])
    global_var.set_value('co2BaroPress',[0])
    global_var.set_value('co2GasTemp',[0])
    global_var.set_value('h_temp1', 0)
    global_var.set_value('h_temp2', 0)
    global_var.set_value('h_bpressh', 0)
    global_var.set_value('h_bpressl', 0)
    global_var.set_value('h_bpressv', 0)
    global_var.set_value('bO2_11',[0])
    global_var.set_value('bTidal',[0])
    global_var.set_value('bVte',[0])
    global_var.set_value('bPmb',[0])
    global_var.set_value('bPeepPmb',[0])
    global_var.set_value('bO2',[0])
    global_var.set_value('bHz',[0])
    global_var.set_value('bFztql',[0])
    global_var.set_value('bTinsp',[0])
    global_var.set_value('bHuqi',[0])
    global_var.set_value('bXrTidal',[0])


# from PySide2 import QtGui

def handleVisibleChanged():
    if not QGuiApplication.inputMethod().isVisible():
        return
    for w in QGuiApplication.allWindows():
        if w.metaObject().className()=="QtVirtualKeyboard::InputView":
            keyboard = w.findChild(QtCore.QObject, "Keyboard")
            if keyboard is not None:
                # region=w.mask()
                # rect = [w.geometry()]
                # rect[0].moveTop(keyboard.property("y"))
                # region.setRects(rect)
                # w.setMask(region)
                r = w.geometry()
                r.moveTop(keyboard.property("y"))
                w.setMask(QRegion(r))
                return

if __name__ == "__main__":
    global_var._init()
    global_var.set_value('IndividualInfoFlag', 0)
    global_var.set_value('InjuryInfoFlag', 0)
    global_var.set_value('StartFlag', 0)
    global_var.set_value('EndFlag', 0)
    global_var.set_value('cardiechema1',[0])
    global_var.set_value('cardiechema2', [0])
    global_var.set_value('cardiechema3', [0])
    global_var.set_value('flag_r', 0)
    global_var.set_value('flag_s', 0)
    global_val_init()
    app = QApplication(sys.argv)

    QGuiApplication.inputMethod().visibleChanged.connect(handleVisibleChanged)

    window = Demo()
    window.show()
    sys.exit(app.exec_())

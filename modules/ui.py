from PyQt5 import QtCore, QtWidgets, QtGui
from modules.switch_connect import *
from modules.file_handing import *
import re, time, os
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):

    def __init__(self):

        self.cus_flag = None
        self.path = None
        self.cmd = None
        self.run_flag = 1

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(661, 487)
        MainWindow.setFixedSize(661, 487)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 20, 251, 361))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 260, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(370, 320, 261, 101))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 440, 111, 21))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(450, 120, 171, 22))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 120, 41, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(370, 220, 201, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(575, 219, 45, 22))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.toolButton.setFont(font)
        self.toolButton.setObjectName("toolButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 190, 61, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(450, 160, 171, 20))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(9)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(420, 120, 16, 20))
        self.radioButton.setText("")
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(420, 160, 16, 16))
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 300, 61, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(40, 390, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setObjectName("toolButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(430, 30, 191, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 30, 51, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 70, 191, 20))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 70, 51, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(180, 390, 111, 31))
        self.toolButton_3.setObjectName("toolButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.start_clicked)
        self.pushButton_2.clicked.connect(self.stop_clicked)
        # self.radioButton.clicked.connect(self.def_cmd)  # type: ignore
        # self.radioButton_2.clicked.connect(self.custom_cmd)  # type: ignore
        self.toolButton.clicked.connect(self.save_path)  # type: ignore
        self.toolButton_2.clicked.connect(self.get_ip_from_txt)  # type: ignore
        self.toolButton_3.clicked.connect(self.plainTextEdit.clear)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "交换机配置导出工具"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "要导出配置的交换机IP，批量导出每行一个IP"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.pushButton_2.setText(_translate("MainWindow", "停止"))
        self.label_3.setText(_translate("MainWindow", "Powered By Train"))
        self.comboBox.setItemText(0, _translate("MainWindow", "display current-configuration"))
        self.comboBox.setItemText(1, _translate("MainWindow", "display mac-add"))
        self.comboBox.setItemText(2, _translate("MainWindow", "display arp all"))
        # self.comboBox.setCurrentIndex(2)
        self.label_4.setText(_translate("MainWindow", "命令："))
        self.toolButton.setText(_translate("MainWindow", "浏览"))
        self.label_5.setText(_translate("MainWindow", "保存位置："))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "自定义命令"))
        self.label_6.setText(_translate("MainWindow", "操作记录："))
        self.toolButton_2.setText(_translate("MainWindow", "从txt文件导入"))
        self.label.setText(_translate("MainWindow", "用户名："))
        self.label_2.setText(_translate("MainWindow", "密  码："))
        self.toolButton_3.setText(_translate("MainWindow", "清空IP"))
        self.lineEdit_3.setText(_translate("MainWindow", os.path.dirname(os.path.abspath('.'))))  # 获取程序所在目录作为默认保存目录
        self.cmd = self.comboBox.currentText()

    def write_to_textbrowser(self, log):  # 打印在操作记录中
        self.textBrowser.append(log)  # textBrowser可以是文本部件或标签部件
        QApplication.processEvents()
        time.sleep(0.2)

    def start_clicked(self):
        log_start()
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        # path = self.lineEdit_3 + '/'
        path = self.lineEdit_3.text() + '/'  #
        ip_list = self.plainTextEdit.toPlainText()  # 获取IP地址输入框值

        if self.radioButton.isChecked():  # 获取命令（下拉框）
            self.cmd = self.comboBox.currentText()
        else:  # 获取命令（自定义）
            self.cmd = self.lineEdit_4.text()

        try:
            for ip in ip_list.splitlines():  # 遍历获取到的IP地址并进行操作
                if self.run_flag == 1:
                    login_start = "开始操作交换机" + ip
                    self.write_to_textbrowser(login_start)
                    res_list = telnetsw(ip, username, password, self.cmd)
                    disposition = res_list[0]
                    res_log = res_list[1]
                    self.write_to_textbrowser(res_log)
                    login_fail = re.compile('failed')
                    login_success = re.compile('<(.*)>')
                    if login_fail.search(disposition):
                        log = "交换机" + ip + "配置获取失败"
                        self.write_to_textbrowser(log)
                        logs_adding(log)
                    if login_success.search(disposition):
                        log = "配置获取成功，等待写入"
                        self.write_to_textbrowser(log)
                        logs_adding(log)
                        write_log = file_save(ip, disposition, path)
                        self.write_to_textbrowser(write_log)
                    else:
                        log = "配置匹配出错，不写入"
                        self.write_to_textbrowser(log + "\n---------------------")
                        logs_adding(log)
                else:
                    self.write_to_textbrowser("程序被手动结束")

            log_end()

        except Exception as e:
            self.write_to_textbrowser(str(e))
            logs_adding(e)

    def stop_clicked(self):
        self.run_flag = 0

    def get_ip_from_txt(self):
        # self指向自身，"Open File"为文件名，"./"为当前路径，最后为文件类型筛选器
        fname, ftype = QFileDialog.getOpenFileName(None,
                                                   "Open File",
                                                   "./",
                                                   "Txt (*.txt)")  # 如果添加多个类型则需要加两个分号
        # 该方法返回一个tuple,里面有两个内容，第一个是路径， 第二个是要打开文件的类型，所以用两个变量去接受
        # 如果用户主动关闭文件对话框，则返回值为空
        if fname:  # 判断路径非空
            # f = QFile(fname)  # 创建文件对象，不创建文件对象也不报错 也可以读文件和写文件
            # open()会自动返回一个文件对象
            with open(fname, "r", encoding="utf-8") as f:
                data = f.read()
                import re
                # 创建IP地址匹配对象
                pattern = re.compile(
                    "(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)"
                )
                iplist = pattern.findall(data)  # 匹配得到的元组
                # print(iplist)
                addr_list = []
                for addr in iplist:  # 提取元组数据
                    ip = addr[0] + '.' + addr[1] + '.' + addr[2] + '.' + addr[3]  # 拼接IP地址
                    if ip not in addr_list:  # 去除重复地址
                        addr_list.append(ip)
                        self.plainTextEdit.appendPlainText(ip)  # 显示到IP地址输入框
                f.close()

    def save_path(self):
        self.path = QFileDialog.getExistingDirectory()  # 获取选择的路径
        # print(self.path)
        self.lineEdit_3.setText(self.path)  # 显示到目录编辑框

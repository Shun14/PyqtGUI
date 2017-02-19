# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from dbhandler import mysqlhandler

class Ui_mainWindow(object):
    showTableList = []
    tableDatas = []
    columnlist = []
    currShowTable = []
    removeid = []
    dbhandler = mysqlhandler()
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(495, 402)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 110, 331, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")

        self.tableView = QtWidgets.QTableView(self.gridLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)

        self.label.setGeometry(QtCore.QRect(10, 10, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 10, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 10, 151, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 110, 71, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 150, 71, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 190, 71, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 70, 71, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 251, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 201, 16))
        self.label_5.setObjectName("label_5")
        self.gridLayoutWidget.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.lineEdit.raise_()
        self.label_5.raise_()
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 495, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        mainWindow.setMenuBar(self.menubar)
        self.actionexit = QtWidgets.QAction(mainWindow)
        self.actionexit.setObjectName("actionexit")
        self.menu.addSeparator()
        self.menu.addAction(self.actionexit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(mainWindow)

        self.pushButton.clicked.connect(self.modify_button_click)
        self.pushButton_2.clicked.connect(self.delete_button_click)
        self.pushButton_3.clicked.connect(self.add_button_click)
        self.pushButton_4.clicked.connect(self.lookfor_button_click)
        self.actionexit.triggered['bool'].connect(mainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "工控数据库管理界面"))

        self.setTableView(mainWindow,self.currShowTable)


        self.label.setText(_translate("mainWindow", "用户名："))
        self.label_2.setText(_translate("mainWindow", "root"))
        self.label_3.setText(_translate("mainWindow", "当前数据类型："))

        # self.pushButton.setToolTip(__translate("ref_query", "set the ino",None))
        self.pushButton.setText(_translate("mainWindow", "保存"))
        self.pushButton_2.setText(_translate("mainWindow", "删除"))
        self.pushButton_3.setText(_translate("mainWindow", "新增"))
        self.pushButton_4.setText(_translate("mainWindow", "查询"))
        self.label_5.setText(_translate("mainWindow", "请输入需要查询的数据类型："))
        self.menu.setTitle(_translate("mainWindow", "文件"))
        self.actionexit.setText(_translate("mainWindow", "退出"))


    def setTableView(self, mainWindow, tablename):

        self.currShowTable = tablename
        self.label_4.setText(QtCore.QCoreApplication.translate("mainWindow", str(self.currShowTable)))
        self.columnlist,self.removeid = self.dbhandler.getTableColumnList(tablename)
        self.tableDatas = self.dbhandler.getTableDatas(self.showTableList)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        print('set before,columnlist:',self.columnlist)
        print('set before,tableDatas',self.tableDatas)
        print('set before,showtablelists:',self.showTableList)

        if self.showTableList:
            index = self.showTableList.index(tablename)
            columnText = len(self.columnlist)
            rowText = len(self.tableDatas[index])
        else:
            index = -2
        # mainWindow.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        if index != -2:
            self.model = QStandardItemModel(rowText, columnText)
            self.model.setHorizontalHeaderLabels(self.columnlist)
            self.tableView.setModel(self.model)

            for row in range(rowText):
                for column in range(1,columnText+1):
                    item = QStandardItem("%s" % (self.tableDatas[index][row][column]))
                    self.model.setItem(row, column-1, item)
        else:
            print("showTableList is NULL")

    def modify_button_click(self):
        button = QtWidgets.QMessageBox.information(self.pushButton, "标题", "是否修改？请选中需要保存的数据",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if button == QtWidgets.QMessageBox.Yes:
            indexes = self.tableView.selectedIndexes()
            if indexes:

                self.dbhandler.modifiedData(self.currShowTable,self.columnlist,indexes,self.model,self.removeid)
                print("modified")
                QtWidgets.QMessageBox.information(self.pushButton, "成功", "修改成功！")
            else:
                print('请选中需要保存的数据')
        else:
            print("modified failed")
            QtWidgets.QMessageBox.information(self.pushButton_4, "失败", "修改失败！")
            return

    def delete_button_click(self):
        button = QtWidgets.QMessageBox.information(self.pushButton_2, "标题", "是否删除？将删除整行数据！",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if button == QtWidgets.QMessageBox.Yes:
            indexes = self.tableView.selectedIndexes()
            if indexes:
                self.dbhandler.deleteData(self.currShowTable,self.columnlist,indexes,self.model,self.removeid)
                print("delete")
                QtWidgets.QMessageBox.information(self.pushButton_2, "成功", "删除成功！")
        else:
            print("delete error")
            QtWidgets.QMessageBox.information(self.pushButton_2, "错误", "删除失败！")

        return

    def add_button_click(self):
        button = QtWidgets.QMessageBox.information(self.pushButton_3, "标题", "是否新增",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if button == QtWidgets.QMessageBox.Yes:
            self.model.insertRow(self.model.rowCount())

            self.dbhandler.addRowData(self.currShowTable)
        else:
            QtWidgets.QMessageBox.information(self.pushButton_3, "错误", "插入失败！！")
            print("insert failed")

        return
    def lookfor_button_click(self,mainWindow):
        lookforContent = self.lineEdit.text()
        print("search for :",lookforContent)
        if lookforContent == '':
            print("input is NULL")
        else:
            table = self.dbhandler.lookforTable(lookforContent,self.showTableList)
            print("after table",table)
            if table == None:
                print('search the table failed, no such table in the list')
                QtWidgets.QMessageBox.information(self.pushButton_4,"错误","非空数据库中无此表单")
            else:
                print('search the table:',lookforContent,'success')
                self.setTableView(mainWindow,lookforContent)
                QtWidgets.QMessageBox.information(self.pushButton_4, "成功","查询成功！")
        return




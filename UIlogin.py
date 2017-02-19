# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication , QMainWindow


from mainWindow import Ui_mainWindow
from dbhandler import mysqlhandler
import sys



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow =QMainWindow()

    ui = Ui_mainWindow()
    handler = mysqlhandler()
    #数据非零的表名
    showTableList = handler.getShowTables()

    ui.currShowTable = showTableList[0]
    columnlist,removeid = handler.getTableColumnList(ui.currShowTable)

    tableDatas = handler.getTableDatas(showTableList)
# 赋值给MainWindow
    ui.showTableList = showTableList
    ui.tableDatas = tableDatas
    ui.columnlist = columnlist
    ui.removeid = removeid
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

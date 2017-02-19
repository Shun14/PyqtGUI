# -*- coding: utf-8 -*-
import pymysql
import sys

from PyQt5.QtSql import QSqlTableModel


class mysqlhandler(object):
    def getShowTables(self):
        tables = []
        try:
            dbhandler = pymysql.connect("123.207.25.62", "root", "123456", "information_schema")
            cursor = dbhandler.cursor()
            judgesql = "SELECT table_schema,table_name,table_rows FROM TABLES WHERE TABLE_SCHEMA='IPC' AND table_rows != 0 ORDER BY table_rows DESC"
            try:
                cursor.execute(judgesql)
                data = cursor.fetchall()
                for row in data:
                    tables.append(row[1])
            except:
                print("Get not Null tables failed")

            cursor.close()
            dbhandler.close()
        except:
            print("Mysql connect failed")
        return tables

    def getTableColumnList(self,tableName):
        Columnlist = []
        try:
            dbhandler = pymysql.connect(
                "123.207.25.62", "root", "123456", "information_schema"
            )
            cursor = dbhandler.cursor()
            selectsql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '"+tableName+"' and table_schema = 'IPC'"

            try:
                cursor.execute(selectsql)
                data = cursor.fetchall()
                for row in data:
                    Columnlist.append(row[0])

                removeid = Columnlist[0]
                Columnlist.remove(removeid)

            except:
                print("Get table columnlist failed")

            cursor.close()
            dbhandler.close()
        except:
            print("MySql connect falied,getTableColumnlist failed")

        return Columnlist,removeid

    def getTableData(self,tableName):
        tabledata = []
        try:
            dbhandler = pymysql.connect(
                "123.207.25.62", "root", "123456", "IPC"
            )
            cursor = dbhandler.cursor()
            selectsql = "select * from " + tableName

            try:
                cursor.execute(selectsql)
                data = cursor.fetchall()
                for row in data:
                    tabledata.append(row)
            except:
                print("get table" + tableName + "failed")

            cursor.close()
            dbhandler.close()
        except:
            print("MySql connect failed, gettabledata is empty")

        return tabledata

    def getTableDatas(self,showTableList):
        tableDatas = []
        for tablename in showTableList:
            tableData = self.getTableData(tablename)
            tableDatas.append(tableData)
        return tableDatas

    def lookforTable(self,lookforContent,showTableList):
        table = []
        print("lookfor list:",showTableList)
        if showTableList != []:
            for table in showTableList:
                if table == lookforContent:
                    print("look for success",table)
                    return table
        else:
            print("showTableList is NULL")
            return table

    def modifiedData(self,tableName,columnlist,indexes,model,removeid):
        print('removeid',removeid)
        try:
            dbhandler = pymysql.connect(
                "123.207.25.62", "root", "123456", "IPC"
            )
        except:
            print("MySql connect failed,modified data error")

        else:
            cursor = dbhandler.cursor()
            allRowCount = model.rowCount()
            print("allRow", allRowCount)
            for index in indexes:
                selectrow = str(index.row() + 1)
                column = index.column()
                data = index.data()
                modifiedsql = "update " + tableName + " set " + columnlist[column] + "='" + data + "' where " + removeid + "=" + selectrow
                print("modifiedsql", modifiedsql)
                try:
                    cursor.execute(modifiedsql)
                except:
                    print("set table " + tableName + " data failed")

            cursor.close()
            dbhandler.close()

    def addRowData(self,tableName):
        try:
            dbhandler = pymysql.connect(
                "123.207.25.62", "root", "123456", "IPC"
            )
            cursor = dbhandler.cursor()
        except:
            print("MySql connect failed,modified data error")
        else:
            modifiedsql = "insert into " + tableName + " values()"
            print("modifiedsql", modifiedsql)
            try:
                cursor.execute(modifiedsql)
            except:
                print("set table " + tableName + " data failed")

            cursor.close()
            dbhandler.close()

    def deleteData(self,tableName,columnlist,indexes,model,removeid):
        try:
            dbhandler = pymysql.connect(
                "123.207.25.62", "root", "123456", "IPC"
            )
            cursor = dbhandler.cursor()

            for index in indexes:
                model.removeRow(index.row())
                selectrow = str(index.row() + 1)

                deletesql = "delete from "+ tableName + " where "+removeid+"="+selectrow

                updateidsql = "alter table "+ tableName + " add " + removeid + "int not null first"
                print("modifiedsql:", deletesql)
                try:
                    cursor.execute(deletesql)
                    # cursor.execute(updateidsql)

                except:
                    print("delete table" + tableName + "data failed")

            cursor.close()
            dbhandler.close()
        except:
            print("MySql connect failed, gettabledata is empty")


    def login(self,id,passwd):
        try:
            dbhandler = pymysql.connect("123.207.25.62", "root", "123456", "USER")
            cursor = dbhandler.cursor()
            loginsql = ""
            try:
                cursor.execute(loginsql)
                data = cursor.fetchall()
                print(data)
                for row in data:
                    if row == passwd:
                        #go to mainWindow
                        break
                    else:
                        return
            except:
                print("Login failed")

            cursor.close()
            dbhandler.close()
        except:
            # go to new login widget
            print("Mysql connect failed,请重新登陆")

    def register(self,id,passwd):
        try:
            dbhandler = pymysql.connect("123.207.25.62", "root", "123456", "USER")
            cursor = dbhandler.cursor()
            registersql = ""
            try:
                cursor.execute(registersql)
                data = cursor.fetchall()

            except:
                print("register failed")

            cursor.close()
            dbhandler.close()
        except:
            # go to new register widget
            print("Mysql connect failed,请重新注册")

        # go to new login widget
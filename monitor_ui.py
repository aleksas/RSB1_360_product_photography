# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\monitor.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CommunicationsMonitor(object):
    def setupUi(self, CommunicationsMonitor):
        CommunicationsMonitor.setObjectName("CommunicationsMonitor")
        CommunicationsMonitor.resize(358, 517)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(CommunicationsMonitor)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(CommunicationsMonitor)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.table_gcode_log = QtWidgets.QTableWidget(self.groupBox_2)
        self.table_gcode_log.setObjectName("table_gcode_log")
        self.table_gcode_log.setColumnCount(2)
        self.table_gcode_log.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_gcode_log.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_gcode_log.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.table_gcode_log, 0, 0, 1, 1)
        self.push_clear = QtWidgets.QPushButton(self.groupBox_2)
        self.push_clear.setObjectName("push_clear")
        self.gridLayout.addWidget(self.push_clear, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.retranslateUi(CommunicationsMonitor)
        QtCore.QMetaObject.connectSlotsByName(CommunicationsMonitor)

    def retranslateUi(self, CommunicationsMonitor):
        _translate = QtCore.QCoreApplication.translate
        CommunicationsMonitor.setWindowTitle(_translate("CommunicationsMonitor", "Communications Monitor"))
        self.groupBox_2.setTitle(_translate("CommunicationsMonitor", "Realtime communication monitor"))
        item = self.table_gcode_log.horizontalHeaderItem(0)
        item.setText(_translate("CommunicationsMonitor", "Command"))
        item = self.table_gcode_log.horizontalHeaderItem(1)
        item.setText(_translate("CommunicationsMonitor", "Response"))
        self.push_clear.setText(_translate("CommunicationsMonitor", "Clear"))

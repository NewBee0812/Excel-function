# Form implementation generated from reading ui file 'excelspliter.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ExcelSpliter(object):
    def setupUi(self, ExcelSpliter):
        ExcelSpliter.setObjectName("ExcelSpliter")
        ExcelSpliter.resize(754, 537)
        self.verticalLayout = QtWidgets.QVBoxLayout(ExcelSpliter)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=ExcelSpliter)
        self.label.setStyleSheet("*{\n"
"    font-size:16px;\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton_choose_dir = QtWidgets.QPushButton(parent=ExcelSpliter)
        self.pushButton_choose_dir.setObjectName("pushButton_choose_dir")
        self.horizontalLayout.addWidget(self.pushButton_choose_dir)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lineEdit_choose_path = QtWidgets.QLineEdit(parent=ExcelSpliter)
        self.lineEdit_choose_path.setStyleSheet("*{\n"
"    font-size:10px\n"
"}")
        self.lineEdit_choose_path.setObjectName("lineEdit_choose_path")
        self.verticalLayout.addWidget(self.lineEdit_choose_path)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=ExcelSpliter)
        self.label_2.setStyleSheet("*{\n"
"    font-size:16px\n"
"}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_rowselecter = QtWidgets.QComboBox(parent=ExcelSpliter)
        self.comboBox_rowselecter.setObjectName("comboBox_rowselecter")
        self.comboBox_rowselecter.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_rowselecter)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_output_dir = QtWidgets.QLineEdit(parent=ExcelSpliter)
        self.lineEdit_output_dir.setStyleSheet("*{\n"
"    font-size:10px\n"
"}")
        self.lineEdit_output_dir.setObjectName("lineEdit_output_dir")
        self.horizontalLayout_3.addWidget(self.lineEdit_output_dir)
        self.pushButton_output_dir = QtWidgets.QPushButton(parent=ExcelSpliter)
        self.pushButton_output_dir.setObjectName("pushButton_output_dir")
        self.horizontalLayout_3.addWidget(self.pushButton_output_dir)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushButton_execute_split = QtWidgets.QPushButton(parent=ExcelSpliter)
        self.pushButton_execute_split.setObjectName("pushButton_execute_split")
        self.verticalLayout.addWidget(self.pushButton_execute_split)

        self.retranslateUi(ExcelSpliter)
        QtCore.QMetaObject.connectSlotsByName(ExcelSpliter)

    def retranslateUi(self, ExcelSpliter):
        _translate = QtCore.QCoreApplication.translate
        ExcelSpliter.setWindowTitle(_translate("ExcelSpliter", "拆分Excel文件"))
        self.label.setText(_translate("ExcelSpliter", "請選擇要拆分的文件："))
        self.pushButton_choose_dir.setText(_translate("ExcelSpliter", "選擇文件"))
        self.label_2.setText(_translate("ExcelSpliter", "請選擇要拆分哪一列："))
        self.comboBox_rowselecter.setItemText(0, _translate("ExcelSpliter", "*****無*****"))
        self.pushButton_output_dir.setText(_translate("ExcelSpliter", "選擇輸出的目錄"))
        self.pushButton_execute_split.setText(_translate("ExcelSpliter", "執行拆分"))

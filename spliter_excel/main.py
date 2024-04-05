import sys,os
from PyQt6.QtWidgets import (
    QApplication, QMessageBox, QDialog, QFileDialog)

import excelspliter
import pandas as pd
import split_excel

class MyExcelSpliter(excelspliter.Ui_ExcelSpliter, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.excel_path = ""
        self.pushButton_choose_dir.clicked.connect(
            self.do_choose_excel
        )
        self.output_dir = ""
        self.pushButton_output_dir.clicked.connect(
            self.do_choose_dir
        )
        
        self.pushButton_execute_split.clicked.connect(
            self.do_split
        ) 
        
    def do_split(self):
        if not os.path.exists(self.excel_path):
            QMessageBox.warning(self, "提示", "請先選擇文件路徑!")
            return
        if not os.path.exists(self.output_dir):
            QMessageBox.warning(self, "提示", "請選擇輸出目錄!")
            return
        
        split_col = self.comboBox_rowselecter.currentText()
        if not split_col:
            QMessageBox.warning(self,"提示", "請先選擇拆分的列!")
            
        split_excel.split_excel(self.excel_path, split_col, self.output_dir)
        QMessageBox.warning(self,"提示", "處理成功!")
            
    
    def do_choose_dir(self):
        self.output_dir = QFileDialog.getExistingDirectory(self, "請選擇目錄", os.getcwd()) #getExisitingDirectory:取得資料夾路徑
        self.lineEdit_output_dir.setText(self.output_dir)
        
    def do_choose_excel(self):
        self.excel_path, filetype = QFileDialog.getOpenFileName(                           #getOpenFileName:取得檔案路徑 
            self, "請選擇excel文件", os.getcwd(), "Excel files(*.xlsx)")
        self.lineEdit_choose_path.setText(self.excel_path)
        
        df = pd.read_excel(self.excel_path)
        col = list(df.columns)
        self.comboBox_rowselecter.clear()
        self.comboBox_rowselecter.addItems(col)
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myExcelSpliter= MyExcelSpliter()
    sys.exit(app.exec())
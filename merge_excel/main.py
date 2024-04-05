import os, sys
from PyQt6.QtWidgets import (
    QApplication, QDialog, QFileDialog, QMessageBox
)
import merge
import excel_merge


class MyExcelMerge(merge.Ui_ExceMerger, QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.show()
        
        self.pushButton_choose_dir.clicked.connect(
            self.do_choose_dir
        )

        self.pushButton_remove.clicked.connect(
            self.remove_path
        )
        
        self.pushButton_merge.clicked.connect(
            self.excel_merge
        )

    def do_choose_dir(self):
        file_dir = QFileDialog.getExistingDirectory(self, "請選擇目錄", os.getcwd())
        
        self.lineEdit_dirpath.setText(file_dir)
        
        excel_paths =[]
        for fname in os.listdir(file_dir):
            if fname.startswith("~$"):
                continue
            if fname.endswith(".xlsx"):
                excel_paths.append(os.path.join(file_dir, fname))
                
        self.listWidge_excel_path.clear()
        self.listWidge_excel_path.addItems(excel_paths)
        
    def remove_path(self):
        item = self.listWidge_excel_path.currentItem()
        if item:
            row = self.listWidge_excel_path.row(item)
            self.listWidge_excel_path.takeItem(row)
            
    def excel_merge(self):
        if self.listWidge_excel_path.count() == 0:
            QMessageBox.warning(self, "提示", "合併列表資料不得為空")
            return
        excel_paths = []
        for idx in range(self.listWidge_excel_path.count()):
            item = self.listWidge_excel_path.item(idx)
            excel_paths.append(item.text())
            
        out_path, filetype = QFileDialog.getSaveFileName(
            self, "請保存文件", os.getcwd(), "Excel files(*.xlsx)"
        )
        
        excel_merge.merge_excels(excel_paths, out_path)
        QMessageBox.warning(self, "提示", "合併成功")
        
if __name__ == "__main__":
    app= QApplication(sys.argv)
    myexcelmerge = MyExcelMerge()
    sys.exit(app.exec())

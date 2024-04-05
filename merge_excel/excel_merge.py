import pandas as pd
import os
def merge_excels(excel_paths, out_path):
   """
   合併不同的excel成一張
   :param excel_path: list，多個excel路徑
   :param out_path: 合併後excel的路徑
   """ 
   df_list=[]
   for excel_path in excel_paths:
       if not os.path.exists(excel_path):
           continue
       df_list.append(pd.read_excel(excel_path))
   df_all = pd.concat(df_list)
   df_all.to_excel(out_path, index=False)

if __name__ == "__main__":
    excel_paths=[
        r"D:\SideProject\pyQt+Excel\output\拆分後--God.xlsx",
        r"D:\SideProject\pyQt+Excel\output\拆分後--Sally.xlsx"
    ]
    out_path = "合併後的excel.xlsx"
    merge_excels(excel_paths, out_path)
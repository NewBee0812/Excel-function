import pandas as pd

def split_excel(input_excel, split_col, output_dir):
    """
        拆分excel文件，存到指定目標。
        input_excel (_type_): 輸入excel位址
        split_col (_type_): 拆分的列
        output_dir (_type_): 輸出目錄
    """

    df_input = pd.read_excel(input_excel)
    unique_values = df_input[split_col].unique()
    for unique_value in unique_values:
        df_single = df_input[df_input[split_col] == unique_value] 
        df_single.to_excel(f"{output_dir}/拆分後--{unique_value}.xlsx", index=False)
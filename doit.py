import openpyxl

def txt2xlsx(txt_file, xlsx_file):
    # 创建一个新的xlsx工作簿
    wb = openpyxl.Workbook()
    ws = wb.active

    # 打开txt文件
    with open(txt_file, 'r', encoding='utf-8') as f:
        # 逐行读取txt文件内容
        for i,line in enumerate(f.readlines()):
            contents = line.split('>')
            col = contents[0].count('-')
            # print(f'row ={i+1},col={col+1}')
            cell_value = contents[1]
            # print(f'cell_value={cell_value}')

            ws.cell(row=i + 1, column=col + 1, value=cell_value)

    # 保存xlsx文件
    wb.save(xlsx_file)

txt_file_all= r'D:\all.txt'
xlsx_file_all = r'D:\all.xlsx'

txt_file_part= r'D:\part.txt'
xlsx_file_part = r'D:\part.xlsx'

txt2xlsx(txt_file_all,xlsx_file_all)
txt2xlsx(txt_file_part,xlsx_file_part)
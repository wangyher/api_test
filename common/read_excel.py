import xlrd
import os

from common.config import root_path

excel_file_path = os.path.join(root_path, "data")


def get_excel_data(file_name, sheet_name):
    file_path = excel_file_path+"/{}.xlsx".format(file_name)
    # 获取到book对象
    book = xlrd.open_workbook(file_path)
    # 获取sheet对象
    sheet = book.sheet_by_name(sheet_name)

    rows, cols = sheet.nrows, sheet.ncols
    l = []
    title = sheet.row_values(0)

    # 获取其他行
    for i in range(1, rows):
        l.append(dict(zip(title, sheet.row_values(i))))
        print(dict(zip(title, sheet.row_values(i))))
    # print(l)
    return l


if __name__ == '__main__':

    get_excel_data("contacts_manage", "create_department")
    get_excel_data("contacts_manage", "delete_department")

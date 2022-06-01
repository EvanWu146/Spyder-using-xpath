from xlwt import Workbook


def initial(workbook, sheet):
    titles = ['姓名','出生日期（选填）', '出生地（选填）','现工作单位',
              '现职位', '单位行业领域', '电子邮箱','手机（选填）',
              '座机（选填）','微信号（选填）', 'qq号（选填）', '擅长领域',
              '个人简介（选填）', '教育经历', '工作经历','信息来源']
    i = 0
    for t in titles:
        sheet.write(0, i, t)
        i = i+1


def write_down(sheet, count_row, src_data):
    titles = ['name', 'birthday', 'birthplace', 'workplace',
              'position', 'field', 'email', 'phone',
              'telephone', 'wechat', 'qq', 'special_field',
              'self_intro', 'edu_exp', 'work_exp', 'url']
    print("正在写入：", src_data['name'], " 的相关信息")
    i = 0
    for t in titles:
        if t in src_data.keys():
            sheet.write(count_row, i, src_data[t])
        i = i + 1
    print(src_data['name'], " 的相关信息下载完成")


if __name__ == '__main__':
    pass


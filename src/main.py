import re
from xlwt import Workbook
from download_url import download
import save_to_excel
import findAll
import lxml.etree
import js_parser
from tag_filter import filter_tags


def spider_url(src_url, data=None):
    global totalRow
    html, selectors = download(src_url)
    # print(html)
    if selectors is not None:
        if data is None:
            data = {}
        tem = selectors.xpath('string(/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div)').split(' ')
        data["name"] = tem[0]

        data["workplace"] = 'xxx'

        data["email"] = findAll.find_all_email(html, sep='@@')
        data['email'] = data['email'].replace('@@','@')

        data["self_intro"] = filter_tags(selectors.xpath("string(/html/body/div/div/div/div/div/div/div)")[0:].strip())

        if len(tem) > 0:
            data['position'] = tem[1]

        if len(data["self_intro"]) > 5000:
            data["self_intro"] = ''

        data["edu_exp"] = findAll.find_all_educationExperience(html)
        data["url"] = src_url

        if len(data['email']) > 0:
            print("载入：" + data['name'])
            print(data['position'])
            print(data['email'])
            print(data['self_intro'])
            print(data['edu_exp'])
            save_to_excel.write_down(sheet, totalRow, data)
            totalRow = totalRow + 1


if __name__ == '__main__':
    wb = Workbook()
    sheet = wb.add_sheet("sheet1")
    save_to_excel.initial(wb, sheet)
    totalRow = 1

    url = 'http://www.chem.ynu.edu.cn/szdw/zzjg/'
    hrefs = ['dzgltd.htm', 'bkjxyyjtd.htm', 'kjkfyfxcstd.htm', 'flfxkxyjtd.htm', 'chyswrzlgcyjtd.htm', 'gnclhxyjtd.htm',
             'xgjsyjhxyjtd.htm', 'swhxfzyjtd.htm']
    hrefs1 = []
    text=''
    for href in hrefs:
        # text, selectors = download(url + href)
        selectors = lxml.etree.HTML(text)
        if selectors is not None:
            urls = selectors.xpath('/html/body/div/div[2]/div[2]/div[1]/div/div/p[1]//a/@href')
            for u in urls:
                print(u)


    #wb.save("out.xls")

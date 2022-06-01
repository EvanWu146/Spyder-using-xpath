import re


def clean_str(src):
    if isinstance(src, str):
        re_object = re.compile(r'\n|&nbsp|\xa0|\\xa0|\u3000|\\u3000|\\u0020|\u0020|\t|\r')  # 转换成满足正则表达式的匹配对象
        c_str = re_object.sub('', src)
        return c_str


def alter_str(src, before, after):
    if isinstance(src, str):
        re_object = re.compile(before)  # 转换成满足正则表达式的匹配对象
        c_str = re_object.sub(after, src)
        return c_str

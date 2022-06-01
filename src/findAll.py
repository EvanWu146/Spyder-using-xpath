# coding=utf-8
import time
import bs4
import re
import requests
import clean


def find_position(src_text):
    args = ['副主任', '主任', '副教授', '教授', '讲师', '副研究员', '研究员']
    i = 0
    for arg in args:
        if arg in src_text:
            return arg
        i = i + 1
    return '-'


def find_all_email(src_text, sep='@', exception=None):
    __email_pattern = r"[a-z0-9\.\-+_]+"+sep+"[a-z0-9\.\-+_]+\.[a-z]+[\.a-z]*"
    emails = re.findall(__email_pattern, src_text)
    if emails is not None:
        emails = list(set(emails))

        if exception is not None:
            for exc in exception:
                for e in emails:
                    if exc in e:
                        emails.remove(e)

        return ", ".join(emails)
    else:
        return None


def find_all_url(src_url):
    links = []
    with requests.get(src_url) as res:
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
            links.append(link.get('href'))
    time.sleep(2)
    return links


def judge_endWith(src_text, src_lists):
    for s in src_lists:
        if src_text.endswith(s):
            return True
    return False


def judge_contain(src_text, src_lists):
    for s in src_lists:
        if s in src_text:
            return True
    return False


def judge_startWith(src_text, src_lists):
    result = src_text
    for s in src_lists:
        if result.startswith(s):
            result = result.replace(s, '')
    return result


def find_all_educationExperience(src_text):
    """\u0030-\u0039"""
    """\u4e00-\u9fa5"""
    """"""
    # result = re.findall(u"[\u4e00-\u9fa5\uff1b\uff0c]+博士[\u4e00-\u9fa5\uff1b\uff0c]+", src_text
    result = re.findall(u"[\u4e00-\u9fa5]+[\u4e00-\u9fa5\uff1b\uff0c\u00A0\u0020\u3000\u0041-\u005a\u0061-\u007a]+\
博士[\u4e00-\u9fa5\uff1b\uff0c\u00A0\u0020\u3000\u3002\u0041-\u005a\u0061-\u007a]*", src_text)
    result = list(set(result))
    i = 0
    for i in range(0, len(result)):
        result[i] = clean.alter_str(result[i], r'&nbsp', '')

    args = ['博士导师', '博士后', '在读']
    args1 = ['年', '月', '，', '于', '得', '就读于', '毕业于', '在', '获', '并']
    args2 = ['获得', '获', '攻读']
    for i in range(0, len(result)):
        if i < len(result):
            if judge_contain(result[i], args):
                result.remove(result[i])
            else:
                result[i] = judge_startWith(result[i], args1)

    for i in range(0, len(result)):
        for j in range(0, len(args2)):
            if args2[j] in result[i]:
                result[i] = result[i].replace(args2[j], " ")

    return '\n'.join(result)


def divide_url(src_u):
    for i in range(0, len(src_u)):
        if src_u[i] == 'i':
            return src_u[i - 1:]
    return src_u


if __name__ == '__main__':
    pass
# Spider人才信息爬虫器

## Intro

用于从高校网站上爬取展示的老师基本介绍信息，包括名称、工作地点、邮箱、简介、职位、教育经历、url等。使用xpath爬取、etree解析结构、re正则匹配解析文本内容，并将结果保存至excel。

## 模块介绍

findAll.py：包含了具有以下功能的函数：匹配职位、匹配邮箱、匹配url、判断给定字符串src是否起始/包含/终止于给定的字符串列表src_lists中任意字符串、匹配教育经历（用关键词进行匹配，代码中仅仅包含了匹配博士的经历）、分割url



clean.py：清洗字符串、替换给定字符串的部分内容



download_url.py：从给定的url下载html，并用etree解析，返回html和etree解析结果



main.py：url读取、文本解析、写入excel



redirect.py：url的重定向，返回重定向的网址



save_to_excel.py：保存至excel中



tag_filter.py：html中标签的过滤器
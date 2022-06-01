import time
import requests
from lxml import etree


def download(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        }
        # time.sleep(1)
        print("try to connect", url)
        r = requests.get(url, headers=headers, timeout=1)
        time.sleep(1)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            print("Successfully connect.", r.status_code)
            text = r.text.strip()
            r.close()
            return text, etree.HTML(text)
        else:
            print(url, "Fail to connect.", r.status_code)
            return "", None
    except:
        return "", None


if __name__ == '__main__':
    url = "xxx"
    download(url)
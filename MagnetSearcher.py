import re
import random
from urllib import parse
from urllib import request
from urllib.parse import quote
import requests
import psutil
import time
import os

file_name = 'BT.txt'
listdir_file_name = 'listdir.txt'
search_file_name = 'searchkeyword.txt'
urlPart_row = "https://btsow.beauty/magnet/detail/hash/"
delay_mult = 5

my_headers = [
    {'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"},
    {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"},
    {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"},
    {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14"},
    {'User-Agent': "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"},
    {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'},
    {'User-Agent': 'Opera/9.25 (Windows NT 5.1; U; en)'},
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)'},
    {'User-Agent': 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)'},
    {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12'},
    {'User-Agent': 'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'},
    {'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7"},
    {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0"},
    {'User-Agent': "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6"},
]

def get_now_time():
    """
    获取当前日期时间
    :return:当前日期时间
    """
    now = time.localtime()
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", now)
    return now_time

def file_name_listdir(file_dir):
    f_log = open(r'F:\log\%s' % listdir_file_name, 'a+', encoding='utf-8')
    lines_BT = f_log.read()
    for files in os.listdir(file_dir):  # 不仅仅是文件，当前目录下的文件夹也会被认为遍历到
        if files not in lines_BT:
            f_log.write(str(files) + '\n')
    f_log.close()

def strDecode(uriCode):
    a = re.sub('[+"]', '', uriCode)
    b = parse.unquote(a)
    c = re.compile(r'<[^>]+>', re.S)
    str = c.sub('', b)
    return str

def judge_repet(test, inputKeyWord):
    f_log_BT = open(r'F:\log\%s' % listdir_file_name, 'r', encoding='utf-8')
    lines_BT = f_log_BT.read()
    f_log_BT.close()
    # try:
    #     f_log_listfir = open(r'.\log\BT\%s' % inputKeyWord, 'r', encoding='utf-8')
    # except:
    #     lines_listfir = ""
    # else:
    #     lines_listfir = f_log_listfir.read()
    #     f_log_listfir.close()
    if test in lines_BT:
        return -1
    # elif test in lines_listfir:
    #     return -2
    else:
        return 1

def search_BT(urlPart, pageNummax, inputKeyWord, filter):
    filter_flag = 0
    continue_flag = 0

    for pageNum in range(1, pageNummax):
        url = urlPart + str(pageNum)
        print(url)
        for i in range(5):
            req = request.Request(url=url, headers=random.choice(my_headers))
            time.sleep(random.random() * delay_mult + random.randint(0, pow(i, 2)) * 10)
            try:
                res = request.urlopen(req)
                ret = res.read().decode("utf-8")
            except:
                print("HTTP Error 403")
                continue_flag = 1
            else:
                continue_flag = 0
                break

        if continue_flag:
            continue

        row_url = re.findall(r'<a href="//btsow.beauty/magnet/detail/hash/(.*?)>', ret, re.S)

        for i in range(len(row_url)):
            if inputKeyWord in row_url[i]:
                filter_flag = 0
                row_test = re.findall(r'" title="(.*?)"', row_url[i], re.S)
                for j in range(len(filter)):
                    if filter[j] in row_test[0]:
                        filter_flag = 1
                        break
                if filter_flag == 0:
                    url_row = urlPart_row + (re.findall(r'(.*?)" title="', row_url[i], re.S))[0]
                    print(url_row)
                    for i in range(3):
                        req_row = request.Request(url=url_row, headers=random.choice(my_headers))
                        time.sleep(random.random() * delay_mult + random.randint(0, pow(i, 2)) * 10)
                        # print(req_row)
                        try:
                            res_row = request.urlopen(req_row)
                            ret_row = res_row.read().decode("utf-8")
                        except:
                            print("HTTP Error 403")
                        else:
                            row_test = re.findall(r'</div>		<h3>(.*?)</h3>', ret_row, re.S)
                            row_BT = re.findall(r'class="magnet-link hidden-xs" readonly>(.*?)</textarea>', ret_row, re.S)
                            if judge_repet(row_test[0], inputKeyWord) < 0:
                                break
                            f_log = open(r'F:\log\BT\%s' % inputKeyWord, 'a', encoding='utf-8')
                            f_log.write(row_test[0] + '\n')
                            f_log.write(row_BT[0] + '\n')
                            f_log.close()
                            f_log = open(r'F:\log\%s' % listdir_file_name, 'a', encoding='utf-8')
                            f_log.write(row_test[0] + '\n')
                            f_log.close()
                            break

def assemble_url(inputKeyWord, filter, pageNummax):
    for i in range(len(inputKeyWord)):
        f_log = open(r'F:\log\%s' % search_file_name, 'a', encoding='utf-8')
        f_log.write(inputKeyWord[i] + " pageNummax = " + str(pageNummax) + " " + get_now_time() +' \n')
        f_log.close()
        urlPart1 = "https://btsow.beauty/search/"
        urlPart2 = quote(inputKeyWord[i])+"/page/"
        search_BT(urlPart1 + urlPart2, pageNummax + 1, inputKeyWord[i], filter)

if __name__ == "__main__":
    # 过滤文本含以下关键字的种子
    filter = ["rar", "zip", "直播"]
    # 搜索关键字
    inputKeyWord = ["测试", "大学", ]
    # 获取对应目录的文件夹和文件名，避免重复
    file_name_listdir("F:\迅雷下载")
    # 开始爬取，20代表爬取前20页
    assemble_url(inputKeyWord, filter, 20)

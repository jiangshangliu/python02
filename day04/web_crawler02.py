#-*- coding:UTF-8 -*-

##############################单线程###############################

import urllib.request,re

def getMeta(url_obj):
    fp = urllib.request.urlopen(url_obj)
    html = fp.read()
    shtml = str(html)
    list0 = re.findall(r'charset=(.+?)"',shtml)
    char_cos = list0[0]
    return (html,char_cos)



url_cos = r'http://www.meituba.com/rentiyishu/'
html = getMeta(url_cos)[0]
char_cos = getMeta(url_cos)[1]

text = html.decode(char_cos)
reg = r'src="(.+\.jpg)"'
img_reg = re.compile(reg)
list_img = re.findall(img_reg,text)

num = 1
for i in list_img:
    path0 = r'C:\Users\刘小川\PycharmProjects\python02\day04\00img00/'
    path1 = path0 + '人体艺术' + str(num) + '.jpg'
    urllib.request.urlretrieve(i, path1)
    print("%s下载完成!" % path1)
    num += 1

print("__main__结束!")





























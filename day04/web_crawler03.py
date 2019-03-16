#-*- coding:UTF-8 -*-

import urllib.request,re
# url_cos = r'http://www.chinagirlol.cc/forum-99-1.html'
# fp = urllib.request.urlopen(url_cos)
# info_cos = fp.info()
# print(info_cos)
#
# str_info = str(info_cos)
# list0 = re.findall(r'charset=(.+?)\n',str_info)
# meta = list0[0]
# print(meta)



###############################HTML################################

def getMeta(url_obj):
    fp = urllib.request.urlopen(url_obj)
    html = fp.read()
    shtml = str(html)
    list0 = re.findall(r'charset=(.+?)"',shtml)
    char_cos = list0[0]
    return html,char_cos

url_cos = r'http://www.chinagirlol.cc/forum-99-1.html'
meta = getMeta(url_cos)[1]
print(meta)






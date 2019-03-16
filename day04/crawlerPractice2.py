#-*- coding:utf-8 -*-

#########################多线程#############################

import urllib.request,re,threading

def getPicture():
    path0 = r'C:\Users\刘小川\PycharmProjects\python02\day04\00img00/'
    global num
    global index
    global list_img
    while True:
        lock.acquire()
        if index < len(list_img):
            path1 = path0 + '人体艺术' + str(num) + '.jpg'
            urllib.request.urlretrieve(list_img[index],path1)
            num += 1
            index += 1
            print("%s下载完成!" % path1)
        else:
            lock.release()
            break
        lock.release()

url_cos = r'http://www.meituba.com/rentiyishu/'
fp = urllib.request.urlopen(url_cos)
html = fp.read()
shtml = str(html)
list0 = re.findall(r'charset=(.+?)"',shtml)
char_cos = list0[0]

text = html.decode(char_cos)
reg = r'src="(.+\.jpg)"'
img_reg = re.compile(reg)
list_img = re.findall(img_reg,text)

index = 0
num = 1
list_thread = []
lock = threading.Lock()

for i in range(20):
    t = threading.Thread(target=getPicture)
    list_thread.append(t)

for i in list_thread:
    i.start()

for i in list_thread:
    i.join()

print("__main__"*5,'结束!')




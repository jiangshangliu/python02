#-*- coding:utf-8 -*-
'''
/uploads/photo/2018/hsajmm/hsajmm01.jpg   #源码中图片地址
http://www.chinaart8.com/uploads/photo/2018/hsajmm/hsajmm05.jpg    #完整图片地址
'''
import urllib.request
url_K8 = r'http://www.chinaart8.com/sheying/rxsy/201704/1869.html'

tf = urllib.request.urlopen(url_K8)
html = tf.read()
text = html.decode('UTF-8')
list_img = []
text = text.replace('"',' ')
list_ys = text.split()
ul0 = r'http://www.chinaart8.com'
for i in list_ys:
    if 'hsajmm' in i:
        list_img.append(ul0+i)

for i in list_img:
    print(i)

path0 = r'C:\Users\刘小川\PycharmProjects\python02\day04\00img00'
num = 1
for i in list_img:
        path1 = path0 + '/' + 'K8傲娇萌萌1' + str(num) + '.jpg'
        urllib.request.urlretrieve(i,path1)
        num += 1
        print(i,'下载完成！')



###########################单行版#######################################

#import requests,time
# headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
# num = 1
# path0 = r"C:\Users\刘小川\PycharmProjects\python02\day04\00img00/"
# response=requests.get('http://www.chinaart8.com/uploads/photo/2018/hsajmm/hsajmm01.jpg',headers=headers)
# path1 = path0 + 'K8傲娇萌萌0' + str(num) + '.jpg'
# with open(path1,'wb') as file0:
#     file0.write(response.content)
#     time.sleep(5)
#
# num += 1
# print(path1,"下载完成！")






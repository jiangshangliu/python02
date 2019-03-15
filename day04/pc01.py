#-*- coding:utf-8 -*-

import requests,time

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}

response=requests.get("http://www.xinhuanet.com/forum/sqgj/fzltqz1/201802207pic.jpg",headers=headers)
with open('a.png','wb') as file0:
    file0.write(response.content)
    time.sleep(3)














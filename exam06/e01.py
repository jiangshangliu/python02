#-*- coding:UTF-8 -*-

"""
（一）编写一个程序， 输入一个字符串，请用正则表达式实现。
1.判断该字符串是否属于格式正确的电子邮箱，输出结果。
2.如果是电子邮箱，输出该电子邮箱的用户名
"""
#rui4_la34@lad.com
def getUserName():
    #状态码，决定循环是否继续
    state = 1
    import re
    reg = r'^(\w+)@\w+\.com$'
    pattern = re.compile(reg)
    # state值为 0或 1
    while state:
        mail = input("请输入邮箱地址：\n")
        m = pattern.match(mail)
        # m是否为空，空/False，非空/True
        if m :
            username = m.group(1)
            print("邮箱地址正确!")
            print("您的用户名是%s" % username )
            state = input("键入1继续输入，键入0结束:\n")
            while state not in ['0', '1']:
                state = input("指令错误！请重新键入1继续输入，键入0结束:\n")
            state = int(state)
        else:
            print("邮箱地址错误!")
            state = input("键入1继续输入，键入0结束:\n")
            while state not in ['0','1']:
                state = input("指令错误！请重新键入1继续输入，键入0结束:\n")
            state = int(state)

#getUserName()


#   r'C:\Users\刘小川\Desktop'
# import os
# l =os.walk(os.curdir)
# print(list(l))

from math import floor
print(2%3)    #2
print(-30%-4)  #-2
print(  -30-(-4)*floor(-30/-4)  ) #-2
print('#'*10)
print(-3%2)   #1
print(  -3-2*floor(-3/2)  ) #1
print(10%-6)   #-2
print( 10-(-6)*floor(10/-6) ) #-2





#-*- coding:utf-8 -*-
class Guess:
    __item = 0
    def setItem(self,item):
        self.__item = item
    def __init__(self,item):
        self.__item = item
    def binary_search(self):
        item = self.__item
        try:
            list_range = int(input("请输入此数字的最大范围：\n"))
        except ValueError:
            print("未查找到数字！")
        list0 = list(range(0,list_range))    #指定一个搜索范围
        print(list)
        #跟踪要在其中查找的列表部分
        low = 0
        high = list_range-1
        count = 0
        b = 0
        while low <= high:
            count += 1
            mid = int((low + high)/2)
            guess = list0[mid]
            if guess == item:
                b = 1
                print("该数字是%d,在列表中的索引是%d,一共查找了%d次" % (guess,mid,count) )
            if guess < item:
                low = mid + 1
            else:
                high = mid -1
        if b == 0:
            print("未查找到数字！")
    def __del__(self):
        print("析构成功！")


gs = Guess(888654)
gs.binary_search()
del gs
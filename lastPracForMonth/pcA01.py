#-*- coding:UTF-8 -*-
'''
1.编程实现输出1-1000内的所有素数（本题中，假设1也算做素数）（40分）
【素数：只能被1和它自身整除的数，如5，7，11，17】
(1)用单线程实现，每输出5个素数换行；最后输出1-1000内所有素数的个数（16分）
①　输出素数结果正确  5分
②　输出素数按从小到大排列  3分
③　每5个数换行 3分
④　正确输出全部素数的个数  5分
【输出参考示例：】
1   2   3   5   7
11  13  17  19  23
。。。
1-1000内全部素数个数为： xxx
'''

#>>>>>>>>>>>>>>>>>>>>普通方法<<<<<<<<<<<<<<<<<<<
# def isPrime(num):
#     if num > 1:
#         for i in range(2,num):
#             if num % i == 0:
#                 return False
#         else:
#             return True
#     else:
#         return False

#>>>>>>>>>>>>>>>>>>>>质数规律判断法<<<<<<<<<<<<<<<<<<<
'''
首先看一个关于质数分布的规律：大于等于5的质数一定和6的倍数相邻。例如5和7，11和13,17和19等等；
证明：令x≥1，将大于等于5的自然数表示如下：
······6x-2，6x-1，6x，6x+1，6x+2，6x+3，6x+4，6x+5，6x+6，6x+7······
也就是
······2(3x-1)，6x-1，6x，6x+1，2(3x+1)，3(2x+1)，2(3x+2)，6x+5，6(x+1)，6(x+1)+1······
可以看到，不在6的倍数两侧，即6x两侧的数为6x+2，6x+3，6x+4，由于2(3x+1)，3(2x+1)，2(3x+2)，
所以它们一定不是素数，再除去6x本身，显然，素数要出现只可能出现在6x的相邻两侧。
这里要注意的一点是，在6的倍数相邻两侧并不是一定就是质数。
根据以上规律，判断质数可以6个为单元快进，即将方法（2）循环中i++步长加大为6，加快判断速度，代码如下：
'''

def prime(num):
    if num == 2 or num == 3:  # 对两个较小的数进行处理
        return True
    '''
    一定要使用and,都不满足才能返回False
    '''
    if num % 6 != 5 and num % 6 != 1:  # 不在6两侧的数一定不是素数
        return False
    '''
    寻找一个数是否是质数，就是能否找到除了1以外的因子，比较快的就是在
    range(2,sqrt(num))范围内找，因为如果一个数不是平方数，它的因子一定在
    sqrt(num)的两侧，如果在sqrt(num)找不到因子，这个数一定是质数。
    '''
    sqnum = int(num**0.5)
    '''
    观察: ...6x+5，6(x+1)，6x+7... 6的倍数两侧的数，如果两侧的数不是质数，那么
    它们就是5或者7的倍数，结合上面sqrt(num)的查找规律，可以把范围缩小到从5开始
    查找，即(5, int( sqrt(num) )+1 );步长加大2,即 %i 或 %(i+2)等于0即可
    '''
    for i in range(5,sqnum+1):
        if num % i == 0 or num % (i+2) == 0:  # 在6的倍数两侧的也可能不是质数
            return False
    return True # 剩下的全是质数

#判断是否是质数
def isPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    #如果上面是print的话，一定要写break
            break
    #此处是开关，上面循环内操作不执行时，执行else内操作
    else:
        return True

num1000 = [i+1 for i in range(1000)]

#>>>>>>>>>>>>>>>>>>单线程输出1-1000内所有素数<<<<<<<<<<<<<<<<<<<<<
import time
sta1 = time.time()
pst = []
#找出1000以内的所有素数并存储到列表
# for i in num1000:
#     if isPrime(i):
#         pst.append(i)
#
# print('1-1000内所有素数为：')
# for i in range(len(pst)):
#     if ( i+1 ) % 5 == 0:  #每5个元素换行
#         print(pst[i])
#     else:
#         print(pst[i],end='\t') #输出不换行
# end1 = time.time()
# print()
# print('1-1000内一共有{prime}个素数.'.format(prime=len(pst)),end1-sta1)


'''
(2)用多线程实现（开辟2-5个子线程即可，不用很多），最后输出1-1000内所有素数的个数
①　正确定义并使用全局变量  4分
②　输出的判断结果正确  4分
③　1-1000每个数只被判断一次 4分
④　正确输出全部素数的个数  4分
⑤　子线程定义、调用正确 4分
⑥　正确使用线程锁  4分
【输出参考示例：】
子线程名        
线程1输出  ：   1 是素数
线程2输出  ：   2是素数
'''
import threading,time
sta2 = time.time()
lock = threading.Lock()
count_su = 0

def findPrime():
    #声明全局变量
    global num1000
    global count_su
    while True:
        # 上锁
        lock.acquire()
        if num1000 != []:
            flag = isPrime(num1000[0])  #判断是否是素数
            if flag:
                count_su += 1
                print('{tname}输出素数  :   {num}'
                .format(tname=threading.current_thread().name,num=num1000[0]))
            del num1000[0]
        else:
            #解锁
            lock.release()
            break
        #解锁
        lock.release()

#创建线程
thread_pool = []
for i in range(5):
    t = threading.Thread(target=findPrime,name='线程%s'% str(i+1))
    thread_pool.append(t)

#启动线程
for i in  thread_pool:
    i.start()

#阻塞主线程，等待子线程执行完毕
for i in thread_pool:
    i.join()
end2 = time.time()
print('1-1000一共有%d个素数' % count_su,end2-sta2)

















# import numpy as np
# B = [ [1,0,2,4], [3,2,0,1], [-1, 1,0,-2], [5,2,4,9] ]
# b = np.mat(B)
# print(b.T)







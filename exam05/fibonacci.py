#-*- coding:UTF-8 -*-

def fibonacci(n):
    """
    斐波那契数列的计算
    :param n:  第n个数
    :return:   前2个数的和
    """
    # 第一个数为 0，第二个数为 1，接着，每一个数都是前2个数的和
    if n == 0:
        return 0
    elif n ==1 :
        return 1
    else:
        # 调用函数自身
        return fibonacci(n-1)+fibonacci(n-2)

result = fibonacci(5)
print(result)
'''
上面的函数中，当n不为0和1时，就会调用函数自身，将参数分别减1和2。
这样的写法，叫做递归。  
递归会以栈的形式依次调用函数自身，直到条件发生变化到底，
才会依次返回每一次递归调用的值。
'''
"""
 /**
  **
说实话，递归很占内存。
我们是可以用循环改写此函数的。
  **
  **/
"""

def fibonacci_2(n):
    #斐波那契数列的计算
    """
    :param n: 第 n 个数
    :return: 第 n 个数的值
    """
    # # 第一个数为 0，第二个数为 1，接着，每一个数都是前2个数的和
    i,a,b = 1,0,1
    while i <= n :
        # i 为第 i个数，a为前一个数，b为后一个数，默认第一个数是a (值为0)
        a,b = b,a+b
        """
        /**
         **
            这段代码相当于：
            d1 = b
            d2 = a + b
            a = d1
            b = d2
        **
        **/
        """
        i += 1
    return a


res2 = fibonacci_2(1000)
print(res2)




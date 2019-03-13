#-*- coding:utf-8 -*-
list1 = list( range(1,11) )
print(list1)

list2 = [i*i for i in range(1,10)]
print( list2 )

list3 = [i*i for i in range(2,11,2)]
print(list3)

list3 = [i*i for i in range(1,11) if i%2==0]
print(list3)

list4 = [m+n for m in 'ABC' for n in 'UVW']
print(list4)

d = {'A':'U','B':'V','C':'W'}
list5 = [k+'='+v for k,v in d.items()]
print(list5)

'''
1. 把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
'''

L = ['Hello', 'World', 'IBM', 'Apple']

list0 = [i.lower() for i in L]
print('list0--->',list0)
# print(dir('a'))

'''
2.  如果在list中既包含字符串，又包含其它类型数据，
如何修改1中的生成式实现把一个list中所有的字符串变成小写？
（内建的isinstance(x, str)函数可以判断一个变量是不是字符串）
L2 = ['Hello', 'World', 12.5 ,'IBM', 'Apple', 6]
'''

L2 = ['Hello', 'World', 12.5 ,'IBM', 'Apple', 6]
list6 = [i.lower() for i in L2 if isinstance(i,str)]
print('list6--->',list6)

L3 = [i.upper() if isinstance(i,str) else str(i) for i in L2]
print('L3--->',L3)
L4 = [i.upper() for i in L2   if isinstance(i,str)]
print('L4-->',L4)

'''
报错，if语句放前面必须包含完整的 if--else--结构
L5 = [i.upper() if isinstance(i,str)   for i in L2]
'''


#print("@".join(['mydtr','op']))  # mydtr@op






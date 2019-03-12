##############################################


# path0 = r'G:\00 八维文件\000000   Python与数理统计  -- 备课\19-02 大数据Python+数理基础-01 题目（新大纲）-yang\2019_02_人工智能(python和数理基础-01)__月考（原18-10月月考）\2019-02-大数据系-python和数理基础（1）-月考A卷\2019-02-大数据系-python和数理基础（1）-月考A卷技能'
#
# path = path0 + '\\'+ 'topsearch.txt'
# dict0 = {}
# # print( path0)
# # print( path )
# with open( path, 'r' ) as f:
#     list0 = f.readlines()
#     text = []
#     for i in list0:
#         text.append( i.rstrip('\n') )

# # 统计词频
#     for i in text:
#         if i in dict0 :
#             dict0 [i] += 1
#         else:
#             dict0[i] = 1
#
#     # print('关键词', '    ', '词频')
#     # for k,v in dict0.items():
#     #     print( k,'\t',v )
#
# # 将词频统计结果排序
# list_sort = sorted( dict0.items() ,key = lambda a : a[1], reverse=True )
#
# # print( list_sort )
# pathwrite = r'C:\Users\dell\Desktop\00img00\freq-1.txt'
# # file = 'freq-1.txt'
# # 将排序后的结果写入文件
#
# with open( pathwrite, 'w' ) as f2 :
#     for i in list_sort :
#         f2.write( i[0] +'\t'+ str(i[1]) + '\n' )

#####################################################
# 第一题第2问
# path0 = r'G:\00 八维文件\000000   Python与数理统计  -- 备课\19-02 大数据Python+数理基础-01 题目（新大纲）-yang\2019_02_人工智能(python和数理基础-01)__月考（原18-10月月考）\2019-02-大数据系-python和数理基础（1）-月考A卷\2019-02-大数据系-python和数理基础（1）-月考A卷技能'
#
# path = path0 + '\\'+ 'topsearch.txt'
# dict0 = {}
# # print( path0)
# # print( path )
# with open( path, 'r' ) as f:
#     list0 = f.readlines()
#     text = []
#     for i in list0:
#         text.append( i.rstrip('\n') )
#
# # 打开文件后，读取到的所有搜索关键词信息，现在存储在 text 中
# dict_replace = {
#     'iPhone X':'苹果X',
#     'nongfushanquan': '农夫山泉',
#     'guizhoumaotai':'贵州茅台',
#     'huaweirongyao':'华为荣耀',
#     'jiqixuexi': '机器学习',
#     'meidibingxiang': '美的冰箱'}
#
# # 替换拼音关键词
# rep = []  #
# for i in text :
#     if i in dict_replace:
#         rep.append( dict_replace[i] )
#     else:
#         rep.append( i )
#
# # 将替换结果写入top-中文.txt中
#
# pathwrite2 = r'C:\Users\dell\Desktop\00img00\topsearch-中文.txt'
#
# # 将替换后的结果写入文件
# with open( pathwrite2, 'w' ) as f3 :
#     for i in rep:
#         f3.write( i + '\n' )

###############################################
# 第一题第3问


# path0 = r'G:\00 八维文件\000000   Python与数理统计  -- 备课\19-02 大数据Python+数理基础-01 题目（新大纲）-yang\2019_02_人工智能(python和数理基础-01)__月考（原18-10月月考）\2019-02-大数据系-python和数理基础（1）-月考A卷\2019-02-大数据系-python和数理基础（1）-月考A卷技能'
#
# path = path0 + '\\'+ 'topsearch.txt'
# dict0 = {}
# # print( path0)
# # print( path )
# with open( path, 'r' ) as f:
#     list0 = f.readlines()
#     text = []
#     for i in list0:
#         text.append( i.rstrip('\n') )
#
# # 统计词频
#     for i in text:
#         if i in dict0 :
#             dict0 [i] += 1
#         else:
#             dict0[i] = 1


# 将词频统计结果排序
# list_sort = sorted( dict0.items() ,key = lambda a : a[1], reverse=True )
#
# dictresult2 = dict( list_sort )
#
# print( dictresult2 )
#
# pathwrite2 = r'C:\Users\dell\Desktop\00img00\freq-2.txt'
#
#
# dict_replace = {
#     'iPhone X':'苹果X',  # dict_replace[i]
#     'nongfushanquan': '农夫山泉',
#     'guizhoumaotai':'贵州茅台',
#     'huaweirongyao':'华为荣耀',
#     'jiqixuexi': '机器学习',
#     'meidibingxiang': '美的冰箱'}
#
# for i in dict_replace :
#     china = dict_replace[i]
#     dictresult2[ china ] += dictresult2[ i ]
#     del dictresult2[ i ]
#
# for k, v in dictresult2.items():
#     print( k,'------', v )

# 将统计结果写入文件freq-2.txt（略）

###############################################
# 第二题第1问

path0 = r'G:\00 八维文件\000000   Python与数理统计  -- 备课\19-02 大数据Python+数理基础-01 题目（新大纲）-yang\2019_02_人工智能(python和数理基础-01)__月考（原18-10月月考）\2019-02-大数据系-python和数理基础（1）-月考A卷\2019-02-大数据系-python和数理基础（1）-月考A卷技能'
path = path0 + '\\'+ 'price.txt'
dict0 = {}
with open( path, 'r' ) as f:
    title = f.readline()  # 读取价格文件的标题行
    # print( title )
    list0 = f.readlines()
    text = []
    for i in list0:
        text.append( i.rstrip('\n') )

    list_num = []

    for line in text :
        temp0 = line.split()   # '贵州茅台               2388     2360     2398      2400\n'
        # print( temp0 )
        for i in temp0[ -4: ] :
            if '.' in i:
                list_num.append( float(i) )
            else :
                try :
                    list_num.append( int(i) )
                except:
                    list_num.append( 0 )
        dict0[ line ] = list_num
        list_num =[]

# for  k, v in dict0.items():
#     print( k ,'---', v )

while True:
    num = int( input('\n请输入一个数字1-4：  ') )
    print( '按照第%d价格从高到低排序后的结果为：' %num )
    print( title.rstrip('\n') )

    list_result = sorted( dict0.items() , key = lambda x:x[1][num-1] , reverse=True )

    for i in list_result:
        print( i[0] )


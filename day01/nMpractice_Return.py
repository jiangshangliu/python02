'''
(1)打开并读取topsearch.txt文件，统计其中的所有热搜关键词的搜索次数，
   并将热搜关键词与其对应的搜索次数按搜索频次由高到低排序后，
   储存至一个新的文件中，命名为freq-1.txt（6分）
'''
#指定文件路径
path0 = r'E:\COM_BEIWEI_BEIJING_PACKAGE\Python与数理基础01\考试习题与记录\刘小川python和数理基础（1）-月考B卷技能\Mytxt2'
def partone():
    path1 = path0 + '/' + 'topsearch.txt'
    path2 = path0 + '/' + 'freq-1.txt'
    list0 = []
    dict0 = {}
    with open(path2,'w') as fw :
        with open(path1,'r') as fr:
            lines = fr.readlines()
            for ln in lines:
                list0.append(ln.rstrip("\n")) #移除右侧换行符
            for i in list0:
                if i not in dict0:
                    dict0[i] = 1
                else:
                    dict0[i] += 1
            #倒序排序
            newList = sorted(dict0.items(), key=lambda x : x[1], reverse=True)
        for tup in newList:
            s = tup[0] + '\t' + str(tup[1]) + '\n'  #计数部分是数字，需要用str()函数
            fw.write(s)
    print("freq-1写入结束！")
# partone()
'''
(2)因为有些用户在搜索框中输入的是商品的拼音或英文，
所以为了正确统计关键词的搜索次数，请根据freq-1.txt中的统计结果，
用Python编程将原文件topsearch.txt中出现的所有商品的拼音
（共有6个拼音/英文关键词需替换后合并统计），对应替换为该商品的中文名，
同时将拼音关键词的搜索次数，加到中文关键词中，并保存为新文件topsearch-中文.txt（5分）
【六个需要替换的关键词：iPhone X；nongfushanquan；guizhoumaotai；
                       huaweirongyao；jiqixuexi；meidibingxiang】
'''
def parttwo():
    path3 = path0 + '/' + 'topsearch.txt'
    path4 = path0 + '/' + 'topsearch-中文.txt'
    #定义替换字典
    dt_replace = {'iPhone X':'苹果X','nongfushanquan':'农夫山泉','guizhoumaotai':'贵州茅台',
    'huaweirongyao':'华为荣耀','jiqixuexi':'机器学习','meidibingxiang':'美的空调'}

    list0 = []
    with open(path4, 'w') as fw:
        with open(path3, 'r') as fr:
            lines = fr.readlines()
            for ln in lines:
                i = ln.rstrip('\n')
                #判断是否在替换字典中，进行替换
                if i not in dt_replace:
                    list0.append(i)
                else:
                    china = dt_replace[i]
                    list0.append(china)
        for i in list0:
            s = i + '\n'
            fw.write(s)
    print("topsearch-中文.txt写入结束！")
#parttwo()
'''
(3)根据修改后的文件topsearch-中文.txt，给出热搜关键词的搜索次数，
   并将其按照搜索频次由高到低的顺序，写入文件freq-2.txt（6分）
'''
def partthree():
    path5 = path0 + '/' + 'freq-1.txt'
    path6 = path0 + '/' + 'freq-2.txt'
    dt_replace = {'iPhone X': '苹果X', 'nongfushanquan': '农夫山泉', 'guizhoumaotai': '贵州茅台',
                  'huaweirongyao': '华为荣耀', 'jiqixuexi': '机器学习', 'meidibingxiang': '美的冰箱'}
    dict0 = {}
    with open(path6,'w') as fw:
        with open(path5,'r') as fr:
            lines = fr.readlines()
            for ln in lines:
                l = ln.rstrip('\n')
                lis = l.split('\t')  #切割出字符和搜索次数
                dict0[lis[0]] = int(lis[1])  #转换为数字用于后面的加和
        # 遍历替换字典进行拼音次数加和，然后移除拼音
        for key in dt_replace:
                china = dt_replace[key]
                dict0[china] += dict0[key]
                del dict0[key]
        #倒序排序
        nlist = sorted(dict0.items(), key=lambda x : x[1], reverse=True)
        for i in nlist:
            s = i[0] + '\t' + str(i[1]) + '\n'
            fw.write(s)
    print("freq-2.txt写入结束！")
# partthree()



'''
2.在主函数中循环输入一个整数num， num的取值为1-4，程序输出结果为对price.txt中的全部商品，
  按照其价格的第num列由高到低排序。
 【num=1时，对应第一列淘宝价格，num=2时对应第二列京东价格。。。】（20分）
①　循环输入整数num  2分
②　做好对输入num时非法数据的判断和处理（用异常语句实现）  4分
③　正确实现（2）中功能，实现由高到低排序  6分
④　能正确处理价格标记为“-”的商品，排序时放在最后。  4分
⑤　程序主体框架清晰  2分
⑥　输出结果格式清晰、工整  2分
'''
def partfour():
    path0 = r'E:\COM_BEIWEI_BEIJING_PACKAGE\Python与数理基础01\考试习题与记录\刘小川python和数理基础（1）-月考B卷技能\Mytxt2'
    path = path0 + '/' + 'price.txt'
    dict0 = {}
    list_num = []
    with open(path,'r') as f:
        title = f.readline()
        lines = f.readlines()
        for ln in lines:
            sr = ln.rstrip('\n')
            list0 = sr.split()
            list1 = list0[-4:]
            #判断数字类型和‘-’，并进行处理
            for i in list1:
                try:
                    if '.' in i:
                        list_num.append(float(i))
                    else:
                        list_num.append(int(i)) #转换‘-’会引发异常
                except ValueError:
                    list_num.append(0)
            dict0[ln] = list_num
            list_num = []
    #转换完毕输入数字，进行循环排序
    while True:
        try:
            num = int(input("\n请输入1-4的整数："))
            if num not in [1,2,3,4]:
                raise ValueError
            #倒序排序
            newList = sorted(dict0.items(), key=lambda x : x[1][num-1], reverse=True)
            print(title)
            for i in newList:
                print(i[0])
        except ValueError:
            print("请输入正确数字！")


partfour()
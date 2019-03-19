#-*- coding:UTF-8 -*-

'''
（一）附件文件是八维某班同学的月考成绩表，
（其中，成绩表第一列是序号，第二列是考试成绩。）
请编程实现：读取文件内容，并用两种方法分别完成统计所有同学月考的总成绩和平均分，
最后输出。（100分）
1.不用正则表达式
2.用正则表达式
'''
import re
score_com = []
score_reg = []
with open('day06技能--附件.txt','r') as f:
    #不用正则表达式
    lines = f.readlines()
    for i in lines:
       i = i.rstrip('\n')
       score = i.split()[1]
       score_com.append(int(score))
    print('不用正则:',score_com)
    print("不用正则总成绩：",sum(score_com))
    print("不用正则平均成绩：",sum(score_com)/len(score_com))

    # 使用正则表达式
    f.seek(0,0)
    con = f.read()   #1 92\n2   80\n
    list_s = re.findall(r'\d+\s+(\d+)(?=\n{0,1})',con)
    for i in list_s:
        score_reg.append(int(i))
    print('使用正则:',score_reg)
    print("使用正则总成绩：", sum(score_reg))
    print("使用正则平均成绩：", sum(score_reg) / len(score_reg))


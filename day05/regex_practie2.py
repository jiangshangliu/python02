#-*- coding:UTF-8 -*-
'''
2) 两个非常大的整数求和，不能使用现成的API (数据用字符串表示,超过了整数范围)。
   例如：a = "6894567169781269423"   b = "89568216453521366545522"
   求 a+b 并输出结果 (字符串表示)
'''

def addLongNum(addend,augend):
    #最终的结果变量
    NS = ''
    #保证addend始终是较长的字符串
    if len(addend) < len(augend):
        t       = addend
        addend  = augend
        augend  = t
    #长度对齐
    sbu         = ''
    n1          = len(addend)
    n2          = len(augend)
    for i in range(0,n1-n2):
        sbu += '0'
    augend      = sbu + augend

    #相加结果保存在长度为 1+n1 的 '0'字符列表ch中
    ch          = []
    for i in range(0,n1+1):
        ch.append('0')
    i           = n1
    try:
        while i > 0:
            '''
                取出相加的数，并转为数值型用于计算
            '''
            a       = int(addend[i-1])
            b       = int(augend[i-1])
            '''
                一定要加上前一步进上的数值
            '''
            c       = int(ch[i])+a+b
            '''
                ch[i]本位和ch[i-1]进位
            '''
            ch[i]   = str( c%10 )
            ch[i-1] = str( c//10 )
            i -= 1
        if ch[0] == '0':
            del ch[0]
            NS      = ''.join(ch)
        else:
            NS      = ''.join(ch)
        print(len(NS))
        return NS
    except ValueError:
        return  "输入错误！"

a = "6894567169781269423"
b = "89568216453521366545522"
print(addLongNum(a,b))


while True:
    num1 = input('请输入超长数：\n')
    sh = ['结束','exit','stop','end','over','finish']
    if num1 in sh:
        break
    num2 = input('请输入超长数：\n')
    print(addLongNum(num1,num2))



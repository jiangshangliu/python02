#-*- coding:utf-8 -*-
'''
第二题
创建一个类Weapon
1）包含的属性为：武力值、价格、颜色。分别定义变量的setter方法、getter方法
2）定义一个攻击attack方法，打印内容“开火！”
3）定义一个保养keep方法，打印内容“xx武器正在保养”

1）定义一个枪类gun，包含属性：射击范围、口径。分别定义变量的setter方法、getter方法
2）定义一个攻击attack方法，打印内容“打死你个龟孙儿”
3）定义一个杀伤力lethality方法，打印内容“极高火力杀伤”

1）定义一个手枪类，继承枪类和武器类，优先继承枪类。
2）重写杀伤力lethality方法，打印内容“50米近程杀伤力很高”

1）用手枪类实例化一个对象，Eagle（沙漠之鹰）
2）重新定义Eagle的价格：40000元、重新定义Eagle的口径：6寸，打印出来
3）打印attack方法，打印keep方法，打印lethality方法
'''

# 创建一个类Weapon
# 1）包含的属性为：武力值、价格、颜色。分别定义变量的setter方法、getter方法
# 2）定义一个攻击attack方法，打印内容“开火！”
# 3）定义一个保养keep方法，打印内容“xx武器正在保养”
class weapon(object):
    name = ''
    __power = 9
    __price = 3900
    __color = '青色'
    def setPower(self,power):
        self.__power = power
    def getPower(self):
        return self.__power
    def setPrice(self,price):
        self.__price = price
    def getPrice(self):
        return self.__price
    def setColor(self,color):
        self.__color = color
    def getColor(self):
        return self.__color

    def attact(self):
        print("%s开火！" % self.name)
    def keep(self):
        print("%s正在保养！" % self.name)
    def __del__(self):
        print("%s被析构" %self.name)

# 1）定义一个枪类gun，包含属性：射击范围、口径。分别定义变量的setter方法、getter方法
# 2）定义一个攻击attack方法，打印内容“打死你个龟孙儿”
# 3）定义一个杀伤力lethality方法，打印内容“极高火力杀伤”
class gun:
    __sjrange = 50
    __kj = '37mm'

    def setSjrange(self, sjrange):
        self.__sjrange = sjrange
    def getSjrange(self):
        return self.__sjrange
    def setKj(self, kj):
        self.__kj = kj
    def getKj(self):
        return self.__kj

    def attact(self):
        print("打死你个龟孙儿！")

    def lethality(self):
        print("%s拥有极高火力杀伤" % self.name)
    def __del__(self):
        print("%s被析构" % self.name)

# 1）定义一个手枪类，继承枪类和武器类，优先继承枪类。
# 2）重写杀伤力lethality方法，打印内容“50米近程杀伤力很高”
class handgun(gun,weapon):
    def lethality(self):
        print("%s50米近程杀伤力很高" % self.name)
    def __init__(self,name,price,kj):
        self.name = name
        self.setPrice(price)
        self.setKj(kj)
    def __del__(self):
        print("%s被析构" % self.name)


# 1）用手枪类实例化一个对象，Eagle（沙漠之鹰）
# 2）重新定义Eagle的价格：40000元、重新定义Eagle的口径：6寸，打印出来
# 3）打印attack方法，打印keep方法，打印lethality方法
Eagle = handgun('沙漠之鹰',80,'3寸')
Eagle.setPrice(40000)
Eagle.setKj('6寸')
Eagle.attact()
Eagle.keep()
Eagle.lethality()
print()
print()
print()
'''
第三题：
实现下面几个类，
矩形、正方形、三角形、圆

第三题要求，
1、类中定义出该类最关键的一个或多个属性
2、在类中定义两个方法，通过1中最关键的一个或多个属性，能够计算特定实例的周长和面积。
'''
class rectangle():
    __length = 0
    __width = 0
    def setLength(self,leng):
        self.__length = leng
    def setWidth(self,wdh):
        self.__width = wdh
    def perimeter(self):
        c = (self.__length + self.__width) * 2
        print("长方形周长是%d" % c)
    def area(self):
        s = self.__length * self.__width
        print("长方形的面积是%d" % s)
    def __init__(self,l,w):
        self.__length = l
        self.__width = w
    def __del__(self):
        print("---------长方形被析构！---------")


class square():
    __border = 0
    def setBorder(self,bd):
        self.__border = bd
    def perimeter(self):
        c = self.__border * 4
        print("正方形周长是%d" % c)
    def area(self):
        s = self.__border * self.__border
        print("正方形的面积是%d" % s)
    def __init__(self,l):
        self.__border = l
    def __del__(self):
        print("---------正方形被析构！---------")

class triangle():
    __a = 0
    __b = 0
    __c = 0
    def setA(self,a):
        self.__a = a
    def setB(self,b):
        self.__b = b
    def setC(self,c):
        self.__c = c
    def perimeter(self):
        cl = self.__a + self.__b + self.__c
        print("三角形周长是%d" % cl)
    def area(self):
        from math import sqrt
        a = self.__a
        b = self.__b
        c = self.__c
        #海伦公式
        p = ( a + b + c)/2
        s = sqrt(p*(p-a)*(p-b)*(p-c))
        print("三角形的面积是%d" % s)
    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c
    def __del__(self):
        print("---------三角形被析构！---------")

class circle():
    from math import pi
    __pai = pi
    __r = 0
    def setR(self,r):
        self.__r = r
    def perimeter(self):
        c = self.__pai * self.__r * 2
        print("圆形周长是%d" % c)
    def area(self):
        s = self.__pai * self.__r * self.__r
        print("圆形的面积是%d" % s)
    def __init__(self,r):
        self.__r = r
    def __del__(self):
        print("---------圆形被析构！---------")

c = rectangle(13,7)
c.perimeter()
c.area()
del c
z = square(9)
z.perimeter()
z.area()
del z
s = triangle(5,7,11)
s.perimeter()
s.area()
del s
y = circle(8)
y.perimeter()
y.area()
del y

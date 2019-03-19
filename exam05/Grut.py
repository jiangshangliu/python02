#-*- coding:UTF-8 -*-
'''
2.编程实现一个小游戏，英雄和格鲁特大战。（30分）
1）创建两个类分别为Hero和Grout,两个类代表两个角色。英雄的血格为100，攻击力为10.
英雄具有发射射线技能（6分）
2）格鲁特的血格值为80，攻击力为15。格鲁特具有发射飞镖的技能（6分）
3）游戏开始后生成英雄1号和2号。生成大，中，小三个格鲁特。相互混战（6分）
4）英雄一号收到攻击3次，英雄2号收到攻击2次。（攻击者随意）（6分）
例如大格鲁特使用技能攻击英雄1号，那么英雄一号的血格会相映减少攻击力的数值。
经过过程4的一系列打斗后问，显示两位英雄的血格值（6分）
'''

#英雄类
class Hero:
    # 英雄的血格为100
    hero_HP = 100
    #攻击力为10
    hero_ATTC = 10
    #构造函数
    def __init__(self,n,h,a):
        self.name = n
        self.hero_HP = h
        self.hero_ATTC = a
    #英雄具有发射射线技能
    def sendSX(self):
        print('%s发出射线攻击--------' % self.name)
    #英雄遭受攻击损失血量
    def getFuck(self,g):
        g.sendFB()
        self.hero_HP -= g.grout_ATTC
        print('%s遭受%s的攻击,HP -%d' %(self.name,g.name,g.grout_ATTC) )
        print('%s当前血量%d' %(self.name,self.hero_HP) )
    #重写析构方法
    def __del__(self):
        print("%s被析构$" %self.name )

#格鲁特类
class Grout:
    #格鲁特的血格值为80
    grout_HP = 80
    #攻击力为15
    grout_ATTC = 15
    # 构造函数
    def __init__(self,n,h,a):
        self.name = n
        self.grout_HP = h
        self.grout_ATTC = a
    #格鲁特具有发射飞镖的技能
    def sendFB(self):
        print('%s发出飞镖攻击>>>>>' % self.name)
    #格鲁特遭受攻击损失血量
    def getFuck(self,h):
        h.sendSX()
        self.grout_HP -= h.hero_ATTC
        print('%s遭受%s的攻击,HP -%d' %(self.name,h.name,h.hero_ATTC) )
        print('%s当前血量%d' % (self.name, self.grout_HP))
    #重写析构方法
    def __del__(self):
        print("%s被析构$" %self.name )


#游戏开始后生成英雄1号和2号。
h1 = Hero('英雄1号',100,10)
h2 = Hero('英雄2号',100,10)
#生成大，中，小三个格鲁特。相互混战
gtop = Grout('大格鲁特',80,15)
gmid = Grout('中格鲁特',80,15)
gbot = Grout('小格鲁特',80,15)

#英雄一号收到攻击3次，英雄2号收到攻击2次。（攻击者随意）
h1.getFuck(gtop)
h2.getFuck(gtop)
h1.getFuck(gbot)
h2.getFuck(gmid)
h1.getFuck(gmid)

#战斗结束后，两位英雄的血格值
print('>'*20+'<'*20)
print("%s现在的血量: %d" %(h1.name,h1.hero_HP) )
print("%s现在的血量: %d" %(h2.name,h2.hero_HP) )
print('>'*20+'<'*20)

#释放并回收对象资源
del gtop
del gmid
del gbot
del h1
del h2







list1 = [1,2,3,4,5]
def f(x):
    return x*x*x

#Python3中为了节省资源，map()方法返回的是一个对象
#需要使用列表的工厂函数list()方法转换为列表
obj = map(f,list1)
n3 = list(obj)
print(n3)




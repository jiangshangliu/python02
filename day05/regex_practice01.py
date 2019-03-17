#-*- coding:utf-8 -*-

import re,keyword

# reg = r'src="(.+?\.jpg)" pic_ext'  # 正则表达式，得到图片地址
# imgre = re.compile(reg)  # re.compile() 可以把正则表达式编译成一个正则表达式对象.
# html = html.decode('utf-8')  # python3
# imglist = re.findall(imgre, html)  # re.findall() 方法读取html 中包含 imgre（正则表达式）的数据





#1. 输入一个Email地址字符串，判断该字符串是否是一个正确的Email地址。
# reg_mail = '\w+@\w+\.com'
# mpattern = re.compile(reg_mail)
# while True:
#     mail = input("请输入邮箱地址:\n")
#     if mail == '结束':
#         break
#     m = mpattern.match(mail)
#     if m :
#         print("%s是正确的邮箱地址!" % mail)
#     else:
#         print("非法邮箱%s！" % mail)



#////////////////////////////练习2\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#2. 输入一个字符串，判断该字符串是否可用做Python的变量名
# reg = '[a-zA-Z_][\da-zA-Z_]+'
# pattern = re.compile(reg)
# while True:
#     str0 = input("请输入变量名：\n")
#     if str0 == '结束':
#         break
#     flag = keyword.iskeyword(str0)
#     m = re.match(pattern,str0)
#     if (not flag) and m:
#         print('%s可以做Python的变量名' % str0)
#     else:
#         print('%s是非法的Python变量名' % str0)


#////////////////////////////练习3\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#3：用正则表达式进行爬虫的图片网址匹配

text = '''
   <!DOCTYPE html>
   <html lang="zh-cn">
   <head>
   <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
   <title>K8傲娇萌萌Vivian大胆露胸写真摄影_人像摄影_摄影艺术吧</title>
   <meta name="keywords" content="青豆客,模特K8傲娇萌萌Vivian,露胸,私房,性感女神" />
   <meta name="description" content="美女模特，经历的多了，忘记了淡泊，不敢惹相思，禁不住，逃不脱。忘记了珍惜，贪食着诱惑，不敢纵欲望，捆不住，心膨胀。眼前这傲娇的女孩如同熟透了的蜜桃，令人垂涎。" />
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="renderer" content="webkit">
   <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
   <link rel="shortcut icon" type="image/ico" href="/templets/chinaart8/images/favicon.ico">
   <link rel="stylesheet" href="/templets/chinaart8/css/chinaart8.min.css">
   <script src="/templets/chinaart8/js/chinaart8.min.JS"></script>
   </head>
   <body>
   <!--顶部-->
   <div class="layout bg-black bg-inverse hidden-l">
     <div class="container-layout height-big container">
     <span class="float-left">欢迎来到摄影艺术吧，本站兼容手机浏览！网址：www.chinaart8.com　<span class="icon-qq"> 摄影QQ群：37280875</span></span>
       <span class="float-right"><a href="http://www.chinaart8.com/dh.html">摄影网址导航</a>　|　<a href="/tags.php">标签</a>　|　<a href="/about.html" >关于</a>　|　<a href="http://www.chinaart8.com/down.html" rel="nofollow"><span class="icon-cloud-download"></span> 下载APP</a></span>
     </div>
   </div>

   <!--导航-->
   <div class="demo-nav fixed bg-main bg-inverse margin-bottom">

   <div class="container padding-top padding-bottom">

     <div class="line">

         <div class="xl12 xs3 xm2 xb2">
           <button class="button icon-navicon float-right bg-white margin-top" data-target="#header-demo4"></button>
           <a href='/'><img src="/templets/chinaart8/images/logo.png"/ alt="摄影艺术吧LOGO"></a>
         </div>

         <div class=" xl12 xs9 xm10 xb10 padding-top nav-navicon" id="header-demo4">
             <div class="xs12 xm12 xb10">
             <ul class="nav nav-menu nav-inline nav-pills">
               <li><a href='http://www.chinaart8.com/sheying/rxsy/'>人像摄影</a></li>
               <li><a href='http://www.chinaart8.com/sheying/fjsy/'>风景摄影</a></li>
               <li><a href='http://www.chinaart8.com/sheying/syjc/'>摄影教程</a></li>
               <li><a href='http://www.chinaart8.com/sheying/syll/'>摄影理论</a></li>        
               <li><a href='http://www.chinaart8.com/sheying/syqt/'>摄影趣图</a></li>
               <li><a href='http://www.chinaart8.com/sheying/zpgs/'>照片故事</a></li>
               <li><a href='http://www.chinaart8.com/sysj/'>摄影书籍</a></li>
               <li><a href='http://www.chinaart8.com/sysp/'>摄影视频</a></li>
               <!--li><a href='http://www.chinaart8.com/sys/'>摄影师</a></li-->
             </ul>
             </div>

             <div class="hidden-s hidden-m xb2 text-right">
               <form name="formsearch" action="/plus/search.php">
                 <div class="input-group padding-little-top">
                   <input name="q" type="text" id="search-keyword" class="input" size="30" placeholder="关键词" />
                     <select name="searchtype" class="hidden" id="search-option">
                      <option value="title" selected='1'>检索标题</option><option value="titlekeyword">智能模糊</option>
                     </select>
                   <span class="addbtn"><button type="submit" class="button bg">搜!</button></span>
                 </div>
               </form>
             </div>
         </div>

     </div>

   </div>
   </div>

   <div class="container">
   <!--路径导航-->
   <ul class="bread"><li><span class="icon-home"></span><a href='http://www.chinaart8.com/'>首页</a> > <a href='/sheying/'>摄影</a> > <a href='/sheying/rxsy/'>人像摄影</a> > </li></ul>
   <hr>
   <div class="line-big">
       <!--左边-->
       <div class="xb9 xm9 xs12 xl12">
           <!--内容详情-->
           <div class="detail" style="font-size:16px;">
               <h1>K8傲娇萌萌Vivian大胆露胸写真摄影</h1>
               <p class="text-center">[ 时间:2018-11-06 23:27 来源:摄影艺术吧 作者:青豆客 点击:<script src="/plus/count.php?view=yes&aid=1869&mid=0" type='text/javascript' language="javascript"></script>次 ]</p>
               <p>相关标签： <a href='/tags.php?/%E7%A7%81%E6%88%BF/'><button class="button border-dot button-little">私房</button></a> <a href='/tags.php?/%E9%9D%92%E8%B1%86%E5%AE%A2/'><button class="button border-dot button-little">青豆客</button></a> <a href='/tags.php?/%E6%A8%A1%E7%89%B9K8%E5%82%B2%E5%A8%87%E8%90%8C%E8%90%8CVivian/'><button class="button border-dot button-little">模特K8傲娇萌萌Vivian</button></a> <a href='/tags.php?/%E9%9C%B2%E8%83%B8/'><button class="button border-dot button-little">露胸</button></a> <a href='/tags.php?/%E6%80%A7%E6%84%9F%E5%A5%B3%E7%A5%9E/'><button class="button border-dot button-little">性感女神</button></a></p>
               <p>

               <div class="border bg padding margin-top margin-bottom">摘要：美女模特，经历的多了，忘记了淡泊，不敢惹相思，禁不住，逃不脱。忘记了珍惜，贪食着诱惑，不敢纵欲望，捆不住，心膨胀。眼前这傲娇的女孩如同熟透了的蜜桃，令人垂涎。</div>

               </p>
               <div>
               <p align="center"><img alt="K8傲娇萌萌Vivian大胆露胸写真摄影" src="/uploads/photo/2018/hsajmm/hsajmm01.jpg" /></p>
   <p align="center"><img alt="K8傲娇萌萌Vivian大胆露胸写真摄影" src="/uploads/photo/2018/hsajmm/hsajmm02.jpg" /></p>
   <p align="center"><img alt="K8傲娇萌萌Vivian大胆露胸写真摄影" src="/uploads/photo/2018/hsajmm/hsajmm03.jpg" /></p>
   <p align="center"><img alt="K8傲娇萌萌Vivian大胆露胸写真摄影" src="/uploads/photo/2018/hsajmm/hsajmm04.jpg" /></p>
   <p align="center"><img alt="K8傲娇萌萌Vivian大胆露胸写真摄影" src="/uploads/photo/2018/hsajmm/hsajmm05.jpg" /></p>
   <p align="center">
               </div>
               <!--分享代码-->
               <div class="bdsharebuttonbox"><a href="#" class="bds_more" data-cmd="more">分享到：</a><a href="#" class="bds_weixin" data-cmd="weixin" title="分享到微信">微信</a><a href="#" class="bds_qzone" data-cmd="qzone" title="分享到QQ空间">QQ空间</a><a href="#" class="bds_tsina" data-cmd="tsina" title="分享到新浪微博">新浪微博</a><a href="#" class="bds_sqq" data-cmd="sqq" title="分享到QQ好友">QQ好友</a><a href="#" class="bds_tqq" data-cmd="tqq" title="分享到腾讯微博">腾讯微博</a></div>
               <script>window._bd_share_config={"common":{"bdSnsKey":{},"bdText":"","bdMini":"1","bdMiniList":false,"bdPic":"","bdStyle":"0","bdSize":"24"},"share":{"bdSize":16}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];</script>
               <p><ul class="pagination"><li><a>共3页: </a></li><li><a href='#'>上一页</a></li><li class="thisclass"><a href='#'>1</a></li><li><a href='1869_2.html'>2</a></li><li><a href='1869_3.html'>3</a></li><li><a href='1869_2.html'>下一页</a></li></ul></p>
               <p>
               <ul class="text-center">
               <li class="button margin-top margin-bottom">上一篇：<a href='/sheying/rxsy/201704/1868.html'>可爱黑丝妹子k8傲娇萌萌黑色蕾丝内衣私房照</a> </li>
               <li class="button margin-top margin-bottom">下一篇：<a href='/sheying/rxsy/201704/2211.html'>EsSe人体私房写真</a> </li>
               </ul>
               </p>
           </div>

         <!-- 中国艺术吧APP -->
           <div class="hidden-l">
               <div class="xb2 xm2 xs3 xl12"><img src="/images/down.png" class="img-responsive"></div>
               <div class="xb10 xm10 xs9 xl12">
               <h3 class="height-big">
               您的收藏是对我们最大动力，电脑用户按<span class="text-red">Ctrl+D</span>收藏本站！<br />
               牢记我们的域名<span class="text-red">www.chinaart8.com</span>，手机浏览器输入网址访问本站。<br />
               手机用户还可以通过<span class="text-red">扫描二维码下载「摄影艺术吧」APP安卓版</span>客户端。<br />
               <a href="http://www.chinaart8.com/chinaart8.apk"><button class="button border-red icon-android"> 点击下载APP安卓版</button></a>
               </h3>
               </div>
           </div>
           <div class="hidden-b hidden-m hidden-s show-l">
               <h3 class="icon-star text-red"> 站长寄语：如果喜欢本站可以下载「摄影艺术吧」手机版APP软件。<br />
               <a href="http://www.chinaart8.com/chinaart8.apk"><button class="button border-red icon-android margin-top margin-bottom"> 点击下载APP安卓版</button></a>
               </h3>
           </div>

       </div>

       <!--右侧-->
       <div class="xb3 xm3 xs12 xl12">

           <!--广告-->
           <div class="xb12 xm12 xs12 xl12">

           </div>
           <!--热点图集-->
           <div class="margin-top line-middle">
               <h2 class="icon-caret-right"> 人像作品推荐</h2>
               <hr>
                   <div id='tag81a9ebe2acb86cf788aee17d06af7301'>
   <div class="xb6 xm6 xs4 xl6 margin-bottom">
               <div class="media clearfix">
               <div><a href="/sheying/rxsy/201511/1323.html"><img src="/uploads/photo/2015/cui-ran-tan-xiang/cui-ran-tan-xiang-a.jpg" class="img-responsive" alt="翠冉潭香"/></a><div class="media-body"><a href="/sheying/rxsy/201511/1323.html">翠冉潭香</a></div></div>
               </div>
               </div>
   <div class="xb6 xm6 xs4 xl6 margin-bottom">
               <div class="media clearfix">
               <div><a href="/sheying/rxsy/201510/1217.html"><img src="/uploads/photo/2015/zui-mei-de-ji-jie/zui-mei-de-ji-jie-a.jpg" class="img-responsive" alt="最美的季节最美的你"/></a><div class="media-body"><a href="/sheying/rxsy/201510/1217.html">最美的季节最美的你</a></div></div>
               </div>
               </div>
   <div class="xb6 xm6 xs4 xl6 margin-bottom">
               <div class="media clearfix">
               <div><a href="/sheying/rxsy/201506/51.html"><img src="/uploads/photo/2015/Teenage-girl/Teenage-girl-a.jpg" class="img-responsive" alt="秋季阳光·花季少女"/></a><div class="media-body"><a href="/sheying/rxsy/201506/51.html">秋季阳光·花季少女</a></div></div>
               </div>
               </div>
   <div class="xb6 xm6 xs4 xl6 margin-bottom">
               <div class="media clearfix">
               <div><a href="/sheying/rxsy/201508/313.html"><img src="/uploads/photo/2015/qing-liang-nv-hai/qing-liang-nv-hai-a.jpg" class="img-responsive" alt="清凉女孩"/></a><div class="media-body"><a href="/sheying/rxsy/201508/313.html">清凉女孩</a></div></div>
               </div>
               </div>
   <div class="xb6 xm6 xs4 xl6 margin-bottom">
               <div class="media clearfix">
               <div><a href="/sheying/rxsy/201507/113.html"><img src="/uploads/photo/2015/jin-yu-huo-hua/jin-yu-huo-hua-a.jpg" class="img-responsive" alt="金鱼花火"/></a><div class="media-body"><a href="/sheying/rxsy/201507/113.html">金鱼花火</a></div></div>
               </div>
               </div>
   <div class="xb6 xm6 xs4 xl6 margin-bottom">
               <div class="media clearfix">
               <div><a href="/sheying/rxsy/201603/1619.html"><img src="/uploads/photo/2016/zuo-zhu/zuo-zhu-a.jpg" class="img-responsive" alt="COSPLAY宇智波佐助"/></a><div class="media-body"><a href="/sheying/rxsy/201603/1619.html">COSPLAY宇智波佐助</a></div></div>
               </div>
               </div>
       </div>

           </div>
           <!--推荐图集-->
           <div class="margin-top line-middle">
               <h2 class="icon-caret-right"> 相关摄影作品</h2>
               <hr>
                   <div id='tag0d360c0a3c6bb2189f1f5a8f02e1b162'>
   <div class="xb6 xm6 xs4 xl6 margin-bottom">
               <div class="media clearfix">
               <div><a href="/sheying/fjsy/201509/1068.html"><img src="/uploads/photo/2015/xiu-lun-hu/xiu-lun-hu-a.jpg" class="img-responsive" alt="加拿大休伦湖迷人晚霞映红天"/></a><div class="media-body"><a href="/sheying/fjsy/201509/1068.html">加拿大休伦湖迷人晚霞映红天</a></div></div>
               </div>
               </div>
   <div class="xb6 xm6 xs4 xl6 margin-bottom">
               <div class="media clearfix">
               <div><a href="/sheying/fjsy/201509/1129.html"><img src="/uploads/photo/2015/an-da-lue-hu-pan/an-da-lue-hu-pan-a.jpg" class="img-responsive" alt="多伦多安大略湖畔灿烂无比的晚霞风"/></a><div class="media-body"><a href="/sheying/fjsy/201509/1129.html">多伦多安大略湖畔灿烂无比的晚霞风</a></div></div>
               </div>
               </div>
   <div class="xb6 xm6 xs4 xl6 margin-bottom">
               <div class="media clearfix">
               <div><a href="/sheying/syqt/201603/1584.html"><img src="/uploads/photo/2016/qi-pa-shun-jian/qi-pa-shun-jian-a.jpg" class="img-responsive" alt="日本街拍遇到的搞怪奇葩瞬间"/></a><div class="media-body"><a href="/sheying/syqt/201603/1584.html">日本街拍遇到的搞怪奇葩瞬间</a></div></div>
               </div>
               </div>
   <div class="xb6 xm6 xs4 xl6 margin-bottom">
               <div class="media clearfix">
               <div><a href="/sheying/zpgs/201508/932.html"><img src="/uploads/zpgs/2015/吉尼斯世界纪录60周年回顾惊人之最.jpg" class="img-responsive" alt="吉尼斯世界纪录60周年回顾惊人之最"/></a><div class="media-body"><a href="/sheying/zpgs/201508/932.html">吉尼斯世界纪录60周年回顾惊人之最</a></div></div>
               </div>
               </div>
   <div class="xb6 xm6 xs4 xl6 margin-bottom">
               <div class="media clearfix">
               <div><a href="/sheying/zpgs/201508/632.html"><img src="/uploads/zpgs/2015/兴坪只为遇见你.jpg" class="img-responsive" alt="兴坪只为遇见你"/></a><div class="media-body"><a href="/sheying/zpgs/201508/632.html">兴坪只为遇见你</a></div></div>
               </div>
               </div>
   <div class="xb6 xm6 xs4 xl6 margin-bottom">
               <div class="media clearfix">
               <div><a href="/sheying/fjsy/201509/1128.html"><img src="/uploads/photo/2015/xing-zou-luo-ji-shan/xing-zou-luo-ji-shan-a.jpg" class="img-responsive" alt="行走落基山脉"/></a><div class="media-body"><a href="/sheying/fjsy/201509/1128.html">行走落基山脉</a></div></div>
               </div>
               </div>
       </div>

           </div>
       </div>

   </div>    

   </div>
   <!--页底及版权-->
   <div class="container margin-top">
     <div class="border-top padding-top clearfix footnav">
       <div class="text-center height-big">Copyright 2005-2018 <a href="http://www.chinaart8.com">摄影艺术吧</a> All Rights Reserved 闽ICP备05032568号</div>
     </div>
   </div>
   <div class="doc-backtop win-backtop icon-arrow-circle-up"></div>
   <script>var _hmt=_hmt||[];(function(){var hm=document.createElement("script");hm.src="https://hm.baidu.com/hm.js?7945731dcb5787ed1dc3af7d51d9fc7b";var s=document.getElementsByTagName("script")[0];s.parentNode.insertBefore(hm,s)})();</script>
   </body>
   </html>
   '''
###################图片地址实例######################
'''
<img src="/uploads/photo/2015/zui-mei-de-ji-jie.jpg" class="img-responsive" alt="最美的季节最美的你"/>
#结果: /uploads/photo/2015/zui-mei-de-ji-jie.jpg
'''

reg_1 = r'(?<=src=")\S+?jpg'   #方法1--零宽断言
list1 = re.findall(reg_1,text)
for i in list1:
    print(i)
print()
print( '#'*35 + '方法2' + '#'*35 )
print()
reg_html = r'src="(.+\.jpg)"'
list_img = re.findall(reg_html,text)
for i in list_img:
    print(i)





# strs = ['_aaa','1aaa','aaaa','a_12','a1','a_123','1234','____']
# p = re.compile(r'^(?!_)(?!\d)(?![a-zA-Z]+$)\w{4}$')
#
# print('【Output】')
# for s in strs:
#     print( re.findall(p,s) )




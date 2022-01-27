# --------------------------------
# LOVE69_Renpy_Remaster_Project
# 主脚本模块（脚本入口）
# Author:Luckykeeper
# 版本 0.4 "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 开坑日期 2021年8月28日
# 修订日期 2022年1月27日

#----------------------------------------------------------------
# 主程序开始

# 制作流程
# ①导入全部文本+润色汉化，不带图像
# ②修图，替换日语内容
# ③为op加上嵌入字幕（ass，然后嵌入），参考十月翻译组版本；为里面的视频加字幕
# ④完成视觉资源的waifu2x，从720p放大到2K
#（主流手机屏幕和大多数设备的情况，大小和质量的均衡点（偏质量）根据之前的测试，视频插帧效果不好，所以只放大）
# 二测，只有op的效果不好，除 op 外都做60帧
# ⑤导入图像和视频，对照程序逆向出特效，以及音频（音频不需要进行处理）
# ⑥制作GUI
# ⑦打包发布

# 翻译原则
# a、采用机翻+润色的方式进行，因为我是个日语渣，翻译初稿来自百度为主+彩云小译为辅的结果，部分结果来自DeepL
# b、主体采用意译的方式，因为本来就是电波向作品，很多地方并不好直译
# c、不会翻的地方使用 // 标出，希望老哥们帮帮忙
# d、翻译力图在尽量准确的同时最大程度的让文字变得有趣，希望让本作受到更多人的喜爱
# e、第一次做翻译，也是第一次用 Ren'py ，活整的不好还请带伙见谅

# 流程 ①
# Author:Luckykeeper
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 开始日期 2021年8月28日
# 主程序正式开始，现在只加入文本
# 版本：null（还未完成）

###### 定义：周目数 ######
# 周目相关持久化变量
# 默认：一周目
# Demo 版预定义周目数为一便于与后续版本继承
default persistent.playthrough = 1

# 一二周目变量预定义
default persistent.one = False
default persistent.two = False

# 判断是否进行过游戏
default persistent.gameStarted = False

# 周目处理函数
init python:
    def check_playthrough():
        # 一周目完成后，才能进二周目
        if(persistent.playthrough == 1 and persistent.one):
            persistent.playthrough = 2

# 保存并输出周目数到log

        renpy.save_persistent()
        renpy.log((persistent.one, persistent.two))
        renpy.log("当前周目数: %s" % persistent.playthrough)




###### 定义：动态序列帧图 ######
# 定义的脚本非常多，手动打是不可能的（callgif是我手动打的），请活用excel生成脚本
# 注意前面是tab不是4个空格
# 参考学习资料：https://zhidao.baidu.com/question/396252272874502485.html
# 参考学习资料2：https://zhidao.baidu.com/question/2116616608204628667.html?qbl=relate_question_3&word=excel%20%CA%E4%C8%EBtab
# 即：=""&REPT(" ",4)&A1
# 经测试，使用替换功能是最简单的，前面先打一个空格，然后用替换功能，tab从vscode里面复制
# 发现我确实是不会用office，怪不得计算机二级office没过呢（2333）
# 感谢 WorldlineChanger 的提醒

# 来自 Luckykeeper 的提醒：
# callscr （60张图）基本上达到了机械硬盘读取文件的瓶颈，再做大了会非常卡顿，多的一定要做视频来放

# 定义真冬介绍小动画
# 不做了，参考scene01的166行
# image dongintro:
#     "images/pac/真冬カットイン/真冬カットイン00000.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00001.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00002.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00003.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00004.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00005.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00006.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00007.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00008.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00009.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00010.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00011.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00012.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00013.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00014.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00015.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00016.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00017.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00018.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00019.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00020.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00021.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00022.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00023.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00024.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00025.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00026.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00027.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00028.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00029.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00030.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00031.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00032.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00033.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00034.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00035.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00036.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00037.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00038.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00039.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00040.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00041.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00042.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00043.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00044.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00045.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00046.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00047.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00048.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00049.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00050.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00051.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00052.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00053.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00054.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00055.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00056.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00057.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00058.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00059.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00060.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00061.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00062.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00063.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00064.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00065.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00066.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00067.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00068.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00069.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00070.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00071.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00072.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00073.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00074.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00075.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00076.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00077.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00078.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00079.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00080.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00081.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00082.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00083.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00084.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00085.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00086.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00087.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00088.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00089.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00090.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00091.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00092.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00093.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00094.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00095.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00096.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00097.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00098.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00099.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00100.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00101.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00102.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00103.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00104.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00105.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00106.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00107.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00108.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00109.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00110.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00111.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00112.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00113.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00114.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00115.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00116.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00117.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00118.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00119.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00120.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00121.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00122.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00123.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00124.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00125.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00126.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00127.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00128.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00129.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00130.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00131.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00132.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00133.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00134.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00135.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00136.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00137.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00138.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00139.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00140.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00141.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00142.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00143.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00144.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00145.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00146.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00147.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00148.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00149.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00150.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00151.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00152.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00153.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00154.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00155.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00156.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00157.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00158.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00159.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00160.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00161.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00162.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00163.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00164.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00165.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00166.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00167.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00168.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00169.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00170.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00171.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00172.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00173.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00174.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00175.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00176.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00177.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00178.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00179.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00180.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00181.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00182.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00183.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00184.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00185.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00186.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00187.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00188.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00189.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00190.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00191.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00192.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00193.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00194.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00195.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00196.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00197.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00198.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00199.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00200.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00201.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00202.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00203.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00204.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00205.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00206.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00207.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00208.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00209.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00210.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00211.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00212.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00213.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00214.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00215.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00216.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00217.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00218.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00219.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00220.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00221.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00222.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00223.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00224.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00225.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00226.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00227.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00228.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00229.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00230.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00231.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00232.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00233.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00234.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00235.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00236.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00237.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00238.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00239.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00240.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00241.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00242.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00243.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00244.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00245.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00246.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00247.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00248.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00249.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00250.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00251.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00252.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00253.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00254.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00255.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00256.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00257.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00258.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00259.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00260.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00261.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00262.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00263.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00264.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00265.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00266.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00267.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00268.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00269.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00270.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00271.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00272.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00273.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00274.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00275.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00276.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00277.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00278.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00279.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00280.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00281.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00282.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00283.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00284.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00285.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00286.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00287.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00288.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00289.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00290.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00291.png"
#     pause 0.0166666666666667
#     "images/pac/真冬カットイン/真冬カットイン00292.png"
#     pause 0.0166666666666667



#######################################################################################
# 定义callgif 即来电时的gif 屏幕中间一横线写 CALL
image callgif:
    "images/pac/call/call00000.png"
    pause 0.0166666666666667
    "images/pac/call/call00001.png"
    pause 0.0166666666666667
    "images/pac/call/call00002.png"
    pause 0.0166666666666667
    "images/pac/call/call00003.png"
    pause 0.0166666666666667
    "images/pac/call/call00004.png"
    pause 0.0166666666666667
    "images/pac/call/call00005.png"
    pause 0.0166666666666667
    "images/pac/call/call00006.png"
    pause 0.0166666666666667
    "images/pac/call/call00007.png"
    pause 0.0166666666666667
    "images/pac/call/call00008.png"
    pause 0.0166666666666667
    "images/pac/call/call00009.png"
    pause 0.0166666666666667
    "images/pac/call/call00010.png"
    pause 0.0166666666666667
    "images/pac/call/call00011.png"
    pause 0.0166666666666667
    "images/pac/call/call00012.png"
    pause 0.0166666666666667
    "images/pac/call/call00013.png"
    pause 0.0166666666666667
    "images/pac/call/call00014.png"
    pause 0.0166666666666667
    "images/pac/call/call00015.png"
    pause 0.0166666666666667
    "images/pac/call/call00016.png"
    pause 0.0166666666666667
    "images/pac/call/call00017.png"
    pause 0.0166666666666667
    "images/pac/call/call00018.png"
    pause 0.0166666666666667
    "images/pac/call/call00019.png"
    pause 0.0166666666666667
    "images/pac/call/call00020.png"
    pause 0.0166666666666667
    "images/pac/call/call00021.png"
    pause 0.0166666666666667
    "images/pac/call/call00022.png"
    pause 0.0166666666666667
    "images/pac/call/call00023.png"
    pause 0.0166666666666667
    "images/pac/call/call00024.png"
    pause 0.0166666666666667
    "images/pac/call/call00025.png"
    pause 0.0166666666666667
    "images/pac/call/call00026.png"
    pause 0.0166666666666667
    "images/pac/call/call00027.png"
    pause 0.0166666666666667
    "images/pac/call/call00028.png"
    pause 0.0166666666666667
    "images/pac/call/call00029.png"
    pause 0.0166666666666667
    "images/pac/call/call00030.png"
    pause 0.0166666666666667
    "images/pac/call/call00031.png"
    pause 0.0166666666666667
    "images/pac/call/call00032.png"
    pause 0.0166666666666667
    "images/pac/call/call00033.png"
    pause 0.0166666666666667
    "images/pac/call/call00034.png"
    pause 0.0166666666666667
    "images/pac/call/call00035.png"
    pause 0.0166666666666667
    "images/pac/call/call00036.png"
    pause 0.0166666666666667
    "images/pac/call/call00037.png"
    pause 0.0166666666666667
    "images/pac/call/call00038.png"
    pause 0.0166666666666667
    "images/pac/call/call00039.png"
    pause 0.0166666666666667
    "images/pac/call/call00040.png"
    pause 0.0166666666666667
    "images/pac/call/call00041.png"
    pause 0.0166666666666667
    "images/pac/call/call00042.png"
    pause 0.0166666666666667
    "images/pac/call/call00043.png"
    pause 0.0166666666666667
    "images/pac/call/call00044.png"
    pause 0.0166666666666667
    "images/pac/call/call00045.png"
    pause 0.0166666666666667
    "images/pac/call/call00046.png"
    pause 0.0166666666666667
    "images/pac/call/call00047.png"
    pause 0.0166666666666667
    "images/pac/call/call00048.png"
    pause 0.0166666666666667
    "images/pac/call/call00049.png"
    pause 0.0166666666666667
    "images/pac/call/call00050.png"
    pause 0.0166666666666667
    "images/pac/call/call00051.png"
    pause 0.0166666666666667
    "images/pac/call/call00052.png"
    pause 0.0166666666666667
    "images/pac/call/call00053.png"
    pause 0.0166666666666667
    "images/pac/call/call00054.png"
    pause 0.0166666666666667
    "images/pac/call/call00055.png"
    pause 0.0166666666666667
    "images/pac/call/call00056.png"
    pause 0.0166666666666667
    "images/pac/call/call00057.png"
    pause 0.0166666666666667
    "images/pac/call/call00058.png"
    pause 0.0166666666666667
    "images/pac/call/call00059.png"
    pause 0.0166666666666667
    repeat

###### 定义：界面（screen） ####
# align (0.5,0.5)阔以将其放在中间
screen callscr:
    add "callgif" align (0.5,0.5)
# 真冬介绍动画不做了，参考scene01的166行
# screen dongintroscr:
#     add "dongintro" align (0.5,0.5)

# 一周目开始前 主题BGM：anonatsu_piano.ogg

label start:



# 游戏开始
    stop music fadeout 2.0 # 停止主菜单音乐
    play sound "voice/effect/start.ogg" # 播放开始音效
    with fade # 主菜单到正式游戏的过场
    pause 0.8
    # $ persistent.one = True # 调试用
    $ persistent.gameStarted = True
    $ check_playthrough()
    jump scene01 # 开始 scene01 的脚本

# 主程序入口脚本结束！
#######################################################################

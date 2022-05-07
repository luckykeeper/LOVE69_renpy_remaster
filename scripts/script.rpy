# --------------------------------
# LOVE69_Renpy_Remaster_Project
# 主脚本模块（脚本入口）
# Author:Luckykeeper WorldlineChanger
# 版本 NightBuild "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 开坑日期 2021年8月28日
# 修订日期 2022年5月7日

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
# c、不会翻的地方使用 && 标出，希望老哥们帮帮忙
# d、翻译力图在尽量准确的同时最大程度的让文字变得有趣，希望让本作受到更多人的喜爱
# e、第一次做翻译，也是第一次用 Ren'Py ，活整的不好还请带伙见谅

# 流程 编写脚本AIO Process
# Author:Luckykeeper
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 开始日期 2021年8月28日
# 主程序正式开始

###### 定义：周目数 ######
# 周目相关持久化变量
# 默认：一周目
# Demo 版预定义周目数为一便于与后续版本继承
default persistent.playthrough = 1

# 一二周目变量预定义
default persistent.one = False
default persistent.two = False

# 一周目选择肢预定义
default eat_ice = True

# 判断是否进行过游戏
default persistent.gameStarted = False

# 周目处理函数
init python:
    def check_playthrough():
        # 一周目完成后，才能进二周目
        if(persistent.playthrough == 1 and persistent.one):
            persistent.playthrough = 2

            # # 创建 one.luckykeeper ，详见 gui.rpy 开头 和 options.rpy 主菜单音乐部分
            # ## 注意这里只能使用 Python2 来写，尝试过 flie.write 无法使用

            # file = open('one.luckykeeper','w')
            # file.write('bgm/bgm01.ogg')
            # file.close()


        # 保存并输出周目数到log

        renpy.save_persistent()
        print "当前一周目状态: "
        print persistent.one
        print ";当前二周目状态: "
        print persistent.two
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

#######################################################################################
# 定义Let's Rock! 动画
image letsrock:
    "images/pac/LETSROCK/00000004.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000005.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000006.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000007.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000008.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000009.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000010.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000011.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000012.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000013.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000014.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000015.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000016.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000017.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000018.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000019.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000020.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000021.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000022.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000023.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000024.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000025.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000026.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000027.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000028.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000029.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000030.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000031.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000032.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000033.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000034.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000035.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000036.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000037.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000038.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000039.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000040.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000041.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000042.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000043.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000044.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000045.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000046.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000047.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000048.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000049.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000050.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000051.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000052.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000053.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000054.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000055.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000056.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000057.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000058.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000059.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000060.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000061.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000062.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000063.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000064.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000065.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000066.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000067.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000068.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000069.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000070.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000071.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000072.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000073.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000074.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000075.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000076.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000077.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000078.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000079.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000080.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000081.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000082.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000083.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000084.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000085.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000086.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000087.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000088.jpg"
    pause 0.0166666666666667
    "images/pac/LETSROCK/00000089.jpg"
    pause 0.0166666666666667


#######################################################################################
# CDD Part By WorldlineChanger
# CDD-自定义可视化组件 定义 STAFF 动画
# 正式型 初号机-Initial

# init python:

#     class StaffAnimator(renpy.Displayable):

#         # 文件扩展名由Ren'Py预处理,加油捏
#         # 其他3项（前缀 prefix、分隔符 separator、序列帧 begin & end_index）为 StaffAnimator 的3种必备入参
#         # 序列帧应是两个整型入参，或者一个二元元组，分别表示起始帧序列号和结束帧序列号(此处使用2个整型入参)
#         # 用4个入参找到符合规范的一组图片
#         def __init__(self, prefix, separator, begin_index, end_index, interval, loop=False, **kwargs):
#             super(StaffAnimator, self).__init__(**kwargs)
#             # 前缀
#             self.prefix = prefix
#             # 分隔符
#             self.separator = separator
#             # 起始帧序列号
#             self.begin_index = begin_index
#             # 结束帧序列号
#             self.end_index = end_index
#             # 序列帧长度
#             self.length = end_index - begin_index + 1

#             # 可视组件列表
#             self.sequence = []
#             for i in range(begin_index, end_index+1):
#                 # 将前缀、分隔符和序列号拼接，对应名称的可视组件顺序添加到列表中
#                 self.sequence.append(renpy.displayable(self.prefix + self.separator + str(i)))

#             # 当前帧在可视组件列表中的索引
#             self.current_index = 0
#             # 关键帧时间轴
#             self.show_timebase = 0
#             # 播放间隔
#             self.interval = interval
#             # 循环播放
#             self.loop = loop

#         # 根据时间渲染对应的可视组件
#         def render(self, width, height, st, at):
#             if (st >= (self.show_timebase + self.interval)):
#                 self.show_timebase = st
#                 self.current_index += 1
#                 if self.current_index >= self.length:
#                     # 若循环播放，将可视组件列表索引归零
#                     if self.loop:
#                         self.current_index = 0
#                     else:
#                         self.current_index = self.length - 1

#             # 默认所有序列帧图片都具有相同尺寸
#             render = renpy.render(self.sequence[self.current_index], width, height, st, at)
#             renpy.redraw(self, 0)

#             return render

# # 创建实例并使用，序列帧命名规则：【staff_1.webp ~ staff_1457.webp】
# image staff = StaffAnimator("staff", "_", 1, 1457, 0.0166666666666667)

# 播放
#label start:
#    show staff at truecenter

#######################################################################################
# CDD Part By WorldlineChanger and Modified By Luckykeeper
# CDD-自定义可视化组件 定义 STAFF 动画
# 正式型 贰号机-"LuckyWL"
# 尝试解决读档后 staff 表不能从头播放问题 By Luckykeeper
# https://github.com/luckykeeper/LOVE69_renpy_remaster/issues/19
# 解决方法：将 current_index 注册为全局变量，在播放前手动置 0 一次
init -1 python:
    current_index = 0 # 将 current_index 注册为全局变量，这个过程需要在 StaffAnimator 类之前加载完成
init python:

    class StaffAnimator(renpy.Displayable):

        # 文件扩展名由Ren'Py预处理,加油捏
        # 其他3项（前缀 prefix、分隔符 separator、序列帧 begin & end_index）为 StaffAnimator 的3种必备入参
        # 序列帧应是两个整型入参，或者一个二元元组，分别表示起始帧序列号和结束帧序列号(此处使用2个整型入参)
        # 用4个入参找到符合规范的一组图片
        def __init__(self, prefix, separator, begin_index, end_index, interval, loop=False, **kwargs):
            super(StaffAnimator, self).__init__(**kwargs)
            # 前缀
            self.prefix = prefix
            # 分隔符
            self.separator = separator
            # 起始帧序列号
            self.begin_index = begin_index
            # 结束帧序列号
            self.end_index = end_index
            # 序列帧长度
            self.length = end_index - begin_index + 1

            # 可视组件列表
            self.sequence = []
            for i in range(begin_index, end_index+1):
                # 将前缀、分隔符和序列号拼接，对应名称的可视组件顺序添加到列表中
                self.sequence.append(renpy.displayable(self.prefix + self.separator + str(i)))

            # 当前帧在可视组件列表中的索引
            global current_index
            current_index = 0
            # 关键帧时间轴
            self.show_timebase = 0
            # 播放间隔
            self.interval = interval
            # 循环播放
            self.loop = loop

        # 根据时间渲染对应的可视组件
        def render(self, width, height, st, at):
            global current_index
            if (st >= (self.show_timebase + self.interval)):
                self.show_timebase = st
                current_index += 1
                if current_index >= self.length:
                    # 若循环播放，将可视组件列表索引归零
                    if self.loop:
                        current_index = 0
                    else:
                        current_index = self.length - 1

            # 默认所有序列帧图片都具有相同尺寸
            render = renpy.render(self.sequence[current_index], width, height, st, at)
            renpy.redraw(self, 0)

            return render

# 创建实例并使用，序列帧命名规则：【staff_1.webp ~ staff_1457.webp】
image staff = StaffAnimator("staff", "_", 1, 1457, 0.0166666666666667)

#######################################################################################
# 定义 STAFF 动画
# WebP Test
# image staff:
#     "images/pac/staff/00000001.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000002.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000003.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000004.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000005.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000006.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000007.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000008.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000009.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000010.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000011.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000012.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000013.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000014.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000015.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000016.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000017.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000018.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000019.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000020.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000021.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000022.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000023.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000024.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000025.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000026.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000027.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000028.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000029.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000030.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000031.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000032.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000033.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000034.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000035.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000036.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000037.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000038.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000039.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000040.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000041.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000042.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000043.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000044.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000045.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000046.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000047.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000048.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000049.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000050.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000051.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000052.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000053.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000054.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000055.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000056.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000057.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000058.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000059.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000060.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000061.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000062.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000063.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000064.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000065.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000066.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000067.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000068.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000069.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000070.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000071.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000072.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000073.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000074.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000075.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000076.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000077.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000078.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000079.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000080.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000081.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000082.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000083.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000084.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000085.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000086.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000087.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000088.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000089.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000090.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000091.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000092.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000093.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000094.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000095.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000096.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000097.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000098.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000099.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000100.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000101.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000102.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000103.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000104.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000105.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000106.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000107.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000108.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000109.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000110.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000111.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000112.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000113.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000114.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000115.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000116.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000117.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000118.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000119.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000120.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000121.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000122.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000123.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000124.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000125.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000126.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000127.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000128.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000129.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000130.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000131.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000132.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000133.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000134.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000135.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000136.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000137.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000138.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000139.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000140.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000141.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000142.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000143.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000144.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000145.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000146.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000147.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000148.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000149.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000150.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000151.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000152.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000153.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000154.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000155.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000156.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000157.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000158.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000159.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000160.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000161.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000162.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000163.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000164.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000165.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000166.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000167.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000168.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000169.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000170.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000171.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000172.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000173.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000174.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000175.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000176.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000177.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000178.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000179.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000180.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000181.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000182.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000183.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000184.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000185.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000186.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000187.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000188.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000189.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000190.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000191.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000192.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000193.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000194.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000195.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000196.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000197.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000198.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000199.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000200.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000201.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000202.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000203.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000204.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000205.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000206.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000207.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000208.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000209.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000210.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000211.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000212.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000213.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000214.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000215.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000216.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000217.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000218.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000219.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000220.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000221.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000222.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000223.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000224.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000225.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000226.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000227.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000228.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000229.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000230.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000231.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000232.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000233.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000234.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000235.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000236.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000237.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000238.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000239.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000240.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000241.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000242.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000243.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000244.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000245.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000246.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000247.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000248.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000249.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000250.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000251.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000252.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000253.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000254.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000255.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000256.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000257.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000258.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000259.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000260.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000261.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000262.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000263.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000264.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000265.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000266.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000267.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000268.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000269.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000270.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000271.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000272.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000273.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000274.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000275.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000276.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000277.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000278.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000279.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000280.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000281.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000282.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000283.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000284.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000285.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000286.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000287.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000288.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000289.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000290.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000291.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000292.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000293.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000294.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000295.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000296.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000297.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000298.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000299.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000300.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000301.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000302.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000303.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000304.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000305.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000306.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000307.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000308.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000309.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000310.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000311.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000312.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000313.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000314.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000315.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000316.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000317.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000318.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000319.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000320.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000321.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000322.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000323.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000324.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000325.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000326.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000327.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000328.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000329.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000330.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000331.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000332.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000333.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000334.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000335.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000336.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000337.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000338.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000339.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000340.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000341.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000342.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000343.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000344.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000345.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000346.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000347.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000348.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000349.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000350.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000351.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000352.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000353.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000354.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000355.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000356.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000357.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000358.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000359.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000360.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000361.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000362.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000363.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000364.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000365.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000366.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000367.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000368.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000369.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000370.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000371.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000372.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000373.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000374.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000375.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000376.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000377.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000378.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000379.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000380.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000381.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000382.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000383.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000384.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000385.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000386.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000387.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000388.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000389.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000390.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000391.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000392.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000393.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000394.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000395.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000396.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000397.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000398.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000399.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000400.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000401.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000402.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000403.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000404.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000405.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000406.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000407.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000408.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000409.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000410.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000411.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000412.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000413.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000414.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000415.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000416.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000417.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000418.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000419.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000420.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000421.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000422.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000423.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000424.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000425.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000426.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000427.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000428.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000429.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000430.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000431.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000432.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000433.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000434.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000435.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000436.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000437.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000438.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000439.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000440.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000441.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000442.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000443.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000444.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000445.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000446.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000447.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000448.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000449.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000450.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000451.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000452.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000453.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000454.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000455.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000456.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000457.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000458.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000459.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000460.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000461.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000462.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000463.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000464.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000465.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000466.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000467.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000468.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000469.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000470.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000471.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000472.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000473.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000474.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000475.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000476.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000477.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000478.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000479.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000480.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000481.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000482.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000483.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000484.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000485.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000486.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000487.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000488.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000489.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000490.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000491.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000492.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000493.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000494.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000495.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000496.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000497.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000498.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000499.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000500.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000501.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000502.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000503.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000504.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000505.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000506.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000507.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000508.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000509.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000510.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000511.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000512.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000513.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000514.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000515.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000516.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000517.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000518.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000519.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000520.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000521.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000522.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000523.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000524.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000525.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000526.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000527.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000528.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000529.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000530.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000531.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000532.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000533.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000534.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000535.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000536.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000537.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000538.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000539.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000540.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000541.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000542.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000543.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000544.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000545.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000546.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000547.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000548.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000549.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000550.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000551.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000552.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000553.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000554.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000555.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000556.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000557.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000558.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000559.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000560.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000561.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000562.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000563.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000564.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000565.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000566.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000567.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000568.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000569.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000570.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000571.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000572.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000573.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000574.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000575.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000576.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000577.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000578.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000579.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000580.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000581.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000582.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000583.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000584.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000585.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000586.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000587.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000588.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000589.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000590.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000591.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000592.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000593.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000594.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000595.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000596.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000597.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000598.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000599.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000600.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000601.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000602.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000603.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000604.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000605.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000606.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000607.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000608.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000609.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000610.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000611.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000612.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000613.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000614.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000615.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000616.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000617.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000618.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000619.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000620.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000621.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000622.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000623.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000624.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000625.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000626.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000627.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000628.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000629.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000630.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000631.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000632.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000633.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000634.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000635.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000636.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000637.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000638.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000639.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000640.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000641.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000642.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000643.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000644.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000645.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000646.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000647.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000648.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000649.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000650.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000651.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000652.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000653.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000654.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000655.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000656.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000657.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000658.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000659.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000660.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000661.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000662.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000663.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000664.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000665.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000666.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000667.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000668.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000669.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000670.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000671.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000672.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000673.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000674.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000675.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000676.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000677.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000678.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000679.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000680.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000681.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000682.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000683.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000684.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000685.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000686.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000687.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000688.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000689.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000690.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000691.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000692.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000693.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000694.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000695.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000696.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000697.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000698.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000699.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000700.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000701.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000702.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000703.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000704.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000705.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000706.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000707.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000708.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000709.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000710.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000711.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000712.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000713.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000714.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000715.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000716.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000717.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000718.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000719.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000720.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000721.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000722.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000723.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000724.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000725.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000726.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000727.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000728.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000729.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000730.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000731.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000732.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000733.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000734.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000735.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000736.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000737.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000738.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000739.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000740.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000741.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000742.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000743.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000744.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000745.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000746.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000747.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000748.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000749.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000750.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000751.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000752.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000753.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000754.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000755.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000756.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000757.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000758.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000759.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000760.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000761.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000762.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000763.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000764.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000765.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000766.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000767.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000768.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000769.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000770.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000771.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000772.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000773.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000774.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000775.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000776.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000777.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000778.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000779.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000780.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000781.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000782.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000783.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000784.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000785.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000786.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000787.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000788.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000789.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000790.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000791.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000792.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000793.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000794.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000795.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000796.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000797.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000798.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000799.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000800.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000801.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000802.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000803.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000804.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000805.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000806.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000807.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000808.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000809.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000810.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000811.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000812.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000813.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000814.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000815.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000816.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000817.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000818.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000819.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000820.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000821.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000822.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000823.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000824.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000825.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000826.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000827.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000828.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000829.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000830.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000831.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000832.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000833.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000834.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000835.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000836.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000837.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000838.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000839.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000840.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000841.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000842.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000843.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000844.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000845.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000846.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000847.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000848.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000849.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000850.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000851.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000852.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000853.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000854.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000855.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000856.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000857.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000858.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000859.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000860.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000861.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000862.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000863.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000864.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000865.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000866.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000867.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000868.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000869.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000870.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000871.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000872.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000873.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000874.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000875.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000876.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000877.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000878.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000879.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000880.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000881.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000882.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000883.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000884.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000885.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000886.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000887.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000888.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000889.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000890.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000891.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000892.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000893.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000894.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000895.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000896.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000897.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000898.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000899.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000900.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000901.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000902.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000903.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000904.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000905.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000906.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000907.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000908.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000909.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000910.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000911.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000912.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000913.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000914.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000915.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000916.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000917.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000918.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000919.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000920.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000921.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000922.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000923.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000924.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000925.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000926.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000927.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000928.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000929.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000930.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000931.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000932.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000933.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000934.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000935.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000936.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000937.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000938.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000939.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000940.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000941.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000942.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000943.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000944.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000945.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000946.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000947.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000948.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000949.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000950.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000951.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000952.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000953.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000954.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000955.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000956.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000957.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000958.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000959.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000960.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000961.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000962.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000963.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000964.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000965.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000966.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000967.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000968.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000969.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000970.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000971.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000972.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000973.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000974.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000975.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000976.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000977.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000978.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000979.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000980.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000981.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000982.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000983.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000984.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000985.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000986.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000987.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000988.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000989.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000990.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000991.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000992.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000993.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000994.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000995.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000996.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000997.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000998.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00000999.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001000.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001001.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001002.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001003.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001004.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001005.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001006.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001007.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001008.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001009.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001010.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001011.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001012.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001013.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001014.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001015.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001016.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001017.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001018.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001019.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001020.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001021.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001022.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001023.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001024.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001025.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001026.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001027.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001028.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001029.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001030.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001031.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001032.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001033.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001034.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001035.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001036.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001037.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001038.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001039.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001040.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001041.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001042.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001043.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001044.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001045.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001046.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001047.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001048.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001049.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001050.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001051.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001052.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001053.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001054.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001055.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001056.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001057.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001058.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001059.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001060.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001061.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001062.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001063.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001064.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001065.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001066.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001067.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001068.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001069.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001070.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001071.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001072.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001073.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001074.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001075.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001076.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001077.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001078.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001079.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001080.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001081.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001082.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001083.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001084.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001085.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001086.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001087.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001088.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001089.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001090.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001091.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001092.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001093.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001094.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001095.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001096.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001097.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001098.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001099.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001100.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001101.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001102.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001103.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001104.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001105.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001106.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001107.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001108.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001109.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001110.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001111.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001112.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001113.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001114.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001115.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001116.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001117.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001118.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001119.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001120.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001121.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001122.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001123.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001124.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001125.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001126.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001127.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001128.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001129.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001130.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001131.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001132.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001133.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001134.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001135.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001136.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001137.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001138.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001139.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001140.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001141.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001142.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001143.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001144.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001145.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001146.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001147.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001148.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001149.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001150.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001151.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001152.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001153.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001154.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001155.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001156.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001157.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001158.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001159.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001160.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001161.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001162.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001163.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001164.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001165.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001166.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001167.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001168.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001169.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001170.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001171.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001172.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001173.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001174.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001175.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001176.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001177.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001178.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001179.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001180.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001181.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001182.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001183.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001184.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001185.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001186.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001187.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001188.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001189.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001190.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001191.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001192.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001193.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001194.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001195.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001196.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001197.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001198.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001199.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001200.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001201.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001202.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001203.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001204.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001205.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001206.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001207.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001208.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001209.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001210.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001211.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001212.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001213.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001214.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001215.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001216.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001217.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001218.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001219.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001220.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001221.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001222.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001223.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001224.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001225.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001226.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001227.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001228.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001229.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001230.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001231.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001232.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001233.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001234.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001235.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001236.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001237.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001238.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001239.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001240.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001241.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001242.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001243.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001244.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001245.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001246.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001247.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001248.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001249.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001250.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001251.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001252.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001253.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001254.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001255.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001256.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001257.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001258.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001259.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001260.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001261.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001262.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001263.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001264.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001265.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001266.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001267.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001268.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001269.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001270.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001271.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001272.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001273.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001274.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001275.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001276.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001277.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001278.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001279.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001280.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001281.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001282.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001283.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001284.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001285.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001286.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001287.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001288.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001289.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001290.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001291.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001292.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001293.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001294.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001295.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001296.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001297.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001298.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001299.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001300.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001301.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001302.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001303.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001304.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001305.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001306.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001307.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001308.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001309.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001310.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001311.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001312.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001313.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001314.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001315.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001316.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001317.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001318.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001319.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001320.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001321.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001322.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001323.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001324.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001325.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001326.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001327.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001328.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001329.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001330.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001331.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001332.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001333.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001334.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001335.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001336.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001337.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001338.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001339.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001340.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001341.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001342.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001343.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001344.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001345.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001346.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001347.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001348.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001349.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001350.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001351.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001352.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001353.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001354.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001355.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001356.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001357.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001358.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001359.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001360.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001361.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001362.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001363.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001364.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001365.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001366.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001367.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001368.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001369.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001370.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001371.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001372.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001373.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001374.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001375.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001376.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001377.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001378.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001379.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001380.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001381.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001382.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001383.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001384.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001385.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001386.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001387.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001388.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001389.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001390.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001391.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001392.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001393.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001394.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001395.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001396.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001397.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001398.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001399.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001400.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001401.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001402.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001403.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001404.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001405.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001406.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001407.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001408.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001409.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001410.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001411.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001412.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001413.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001414.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001415.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001416.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001417.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001418.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001419.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001420.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001421.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001422.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001423.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001424.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001425.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001426.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001427.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001428.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001429.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001430.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001431.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001432.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001433.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001434.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001435.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001436.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001437.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001438.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001439.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001440.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001441.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001442.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001443.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001444.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001445.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001446.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001447.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001448.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001449.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001450.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001451.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001452.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001453.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001454.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001455.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001456.webp"
#     pause 0.0166666666666667
#     "images/pac/staff/00001457.webp"
#     pause 0.0166666666666667


####
# PNG
# image staff:
#     "images/pac/staff/00000001.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000002.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000003.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000004.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000005.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000006.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000007.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000008.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000009.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000010.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000011.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000012.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000013.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000014.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000015.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000016.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000017.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000018.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000019.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000020.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000021.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000022.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000023.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000024.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000025.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000026.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000027.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000028.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000029.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000030.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000031.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000032.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000033.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000034.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000035.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000036.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000037.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000038.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000039.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000040.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000041.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000042.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000043.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000044.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000045.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000046.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000047.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000048.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000049.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000050.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000051.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000052.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000053.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000054.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000055.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000056.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000057.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000058.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000059.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000060.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000061.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000062.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000063.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000064.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000065.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000066.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000067.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000068.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000069.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000070.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000071.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000072.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000073.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000074.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000075.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000076.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000077.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000078.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000079.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000080.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000081.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000082.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000083.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000084.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000085.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000086.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000087.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000088.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000089.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000090.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000091.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000092.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000093.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000094.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000095.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000096.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000097.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000098.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000099.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000100.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000101.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000102.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000103.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000104.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000105.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000106.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000107.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000108.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000109.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000110.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000111.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000112.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000113.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000114.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000115.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000116.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000117.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000118.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000119.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000120.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000121.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000122.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000123.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000124.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000125.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000126.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000127.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000128.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000129.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000130.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000131.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000132.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000133.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000134.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000135.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000136.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000137.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000138.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000139.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000140.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000141.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000142.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000143.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000144.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000145.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000146.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000147.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000148.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000149.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000150.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000151.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000152.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000153.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000154.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000155.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000156.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000157.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000158.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000159.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000160.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000161.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000162.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000163.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000164.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000165.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000166.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000167.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000168.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000169.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000170.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000171.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000172.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000173.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000174.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000175.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000176.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000177.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000178.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000179.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000180.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000181.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000182.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000183.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000184.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000185.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000186.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000187.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000188.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000189.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000190.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000191.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000192.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000193.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000194.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000195.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000196.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000197.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000198.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000199.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000200.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000201.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000202.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000203.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000204.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000205.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000206.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000207.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000208.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000209.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000210.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000211.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000212.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000213.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000214.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000215.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000216.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000217.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000218.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000219.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000220.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000221.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000222.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000223.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000224.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000225.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000226.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000227.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000228.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000229.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000230.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000231.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000232.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000233.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000234.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000235.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000236.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000237.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000238.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000239.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000240.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000241.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000242.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000243.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000244.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000245.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000246.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000247.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000248.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000249.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000250.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000251.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000252.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000253.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000254.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000255.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000256.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000257.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000258.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000259.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000260.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000261.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000262.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000263.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000264.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000265.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000266.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000267.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000268.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000269.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000270.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000271.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000272.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000273.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000274.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000275.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000276.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000277.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000278.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000279.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000280.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000281.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000282.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000283.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000284.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000285.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000286.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000287.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000288.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000289.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000290.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000291.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000292.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000293.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000294.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000295.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000296.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000297.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000298.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000299.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000300.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000301.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000302.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000303.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000304.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000305.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000306.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000307.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000308.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000309.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000310.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000311.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000312.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000313.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000314.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000315.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000316.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000317.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000318.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000319.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000320.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000321.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000322.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000323.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000324.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000325.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000326.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000327.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000328.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000329.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000330.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000331.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000332.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000333.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000334.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000335.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000336.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000337.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000338.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000339.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000340.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000341.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000342.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000343.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000344.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000345.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000346.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000347.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000348.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000349.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000350.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000351.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000352.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000353.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000354.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000355.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000356.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000357.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000358.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000359.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000360.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000361.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000362.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000363.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000364.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000365.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000366.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000367.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000368.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000369.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000370.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000371.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000372.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000373.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000374.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000375.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000376.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000377.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000378.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000379.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000380.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000381.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000382.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000383.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000384.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000385.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000386.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000387.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000388.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000389.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000390.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000391.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000392.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000393.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000394.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000395.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000396.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000397.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000398.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000399.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000400.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000401.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000402.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000403.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000404.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000405.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000406.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000407.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000408.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000409.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000410.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000411.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000412.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000413.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000414.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000415.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000416.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000417.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000418.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000419.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000420.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000421.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000422.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000423.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000424.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000425.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000426.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000427.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000428.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000429.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000430.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000431.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000432.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000433.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000434.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000435.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000436.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000437.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000438.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000439.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000440.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000441.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000442.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000443.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000444.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000445.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000446.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000447.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000448.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000449.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000450.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000451.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000452.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000453.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000454.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000455.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000456.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000457.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000458.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000459.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000460.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000461.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000462.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000463.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000464.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000465.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000466.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000467.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000468.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000469.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000470.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000471.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000472.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000473.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000474.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000475.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000476.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000477.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000478.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000479.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000480.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000481.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000482.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000483.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000484.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000485.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000486.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000487.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000488.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000489.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000490.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000491.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000492.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000493.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000494.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000495.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000496.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000497.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000498.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000499.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000500.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000501.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000502.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000503.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000504.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000505.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000506.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000507.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000508.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000509.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000510.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000511.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000512.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000513.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000514.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000515.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000516.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000517.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000518.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000519.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000520.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000521.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000522.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000523.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000524.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000525.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000526.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000527.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000528.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000529.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000530.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000531.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000532.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000533.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000534.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000535.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000536.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000537.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000538.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000539.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000540.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000541.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000542.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000543.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000544.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000545.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000546.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000547.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000548.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000549.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000550.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000551.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000552.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000553.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000554.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000555.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000556.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000557.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000558.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000559.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000560.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000561.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000562.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000563.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000564.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000565.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000566.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000567.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000568.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000569.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000570.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000571.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000572.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000573.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000574.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000575.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000576.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000577.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000578.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000579.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000580.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000581.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000582.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000583.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000584.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000585.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000586.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000587.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000588.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000589.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000590.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000591.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000592.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000593.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000594.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000595.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000596.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000597.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000598.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000599.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000600.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000601.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000602.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000603.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000604.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000605.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000606.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000607.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000608.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000609.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000610.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000611.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000612.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000613.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000614.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000615.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000616.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000617.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000618.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000619.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000620.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000621.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000622.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000623.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000624.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000625.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000626.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000627.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000628.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000629.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000630.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000631.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000632.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000633.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000634.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000635.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000636.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000637.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000638.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000639.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000640.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000641.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000642.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000643.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000644.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000645.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000646.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000647.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000648.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000649.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000650.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000651.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000652.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000653.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000654.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000655.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000656.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000657.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000658.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000659.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000660.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000661.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000662.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000663.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000664.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000665.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000666.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000667.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000668.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000669.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000670.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000671.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000672.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000673.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000674.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000675.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000676.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000677.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000678.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000679.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000680.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000681.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000682.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000683.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000684.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000685.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000686.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000687.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000688.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000689.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000690.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000691.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000692.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000693.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000694.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000695.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000696.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000697.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000698.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000699.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000700.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000701.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000702.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000703.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000704.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000705.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000706.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000707.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000708.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000709.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000710.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000711.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000712.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000713.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000714.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000715.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000716.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000717.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000718.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000719.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000720.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000721.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000722.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000723.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000724.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000725.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000726.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000727.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000728.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000729.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000730.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000731.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000732.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000733.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000734.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000735.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000736.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000737.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000738.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000739.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000740.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000741.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000742.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000743.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000744.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000745.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000746.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000747.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000748.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000749.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000750.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000751.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000752.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000753.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000754.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000755.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000756.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000757.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000758.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000759.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000760.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000761.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000762.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000763.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000764.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000765.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000766.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000767.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000768.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000769.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000770.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000771.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000772.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000773.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000774.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000775.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000776.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000777.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000778.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000779.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000780.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000781.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000782.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000783.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000784.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000785.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000786.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000787.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000788.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000789.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000790.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000791.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000792.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000793.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000794.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000795.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000796.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000797.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000798.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000799.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000800.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000801.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000802.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000803.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000804.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000805.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000806.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000807.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000808.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000809.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000810.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000811.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000812.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000813.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000814.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000815.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000816.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000817.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000818.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000819.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000820.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000821.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000822.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000823.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000824.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000825.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000826.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000827.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000828.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000829.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000830.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000831.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000832.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000833.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000834.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000835.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000836.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000837.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000838.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000839.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000840.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000841.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000842.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000843.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000844.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000845.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000846.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000847.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000848.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000849.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000850.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000851.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000852.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000853.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000854.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000855.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000856.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000857.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000858.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000859.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000860.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000861.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000862.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000863.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000864.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000865.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000866.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000867.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000868.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000869.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000870.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000871.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000872.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000873.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000874.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000875.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000876.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000877.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000878.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000879.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000880.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000881.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000882.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000883.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000884.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000885.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000886.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000887.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000888.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000889.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000890.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000891.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000892.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000893.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000894.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000895.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000896.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000897.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000898.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000899.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000900.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000901.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000902.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000903.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000904.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000905.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000906.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000907.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000908.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000909.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000910.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000911.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000912.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000913.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000914.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000915.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000916.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000917.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000918.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000919.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000920.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000921.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000922.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000923.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000924.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000925.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000926.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000927.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000928.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000929.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000930.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000931.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000932.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000933.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000934.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000935.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000936.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000937.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000938.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000939.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000940.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000941.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000942.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000943.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000944.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000945.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000946.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000947.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000948.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000949.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000950.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000951.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000952.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000953.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000954.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000955.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000956.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000957.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000958.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000959.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000960.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000961.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000962.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000963.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000964.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000965.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000966.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000967.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000968.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000969.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000970.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000971.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000972.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000973.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000974.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000975.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000976.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000977.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000978.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000979.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000980.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000981.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000982.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000983.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000984.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000985.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000986.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000987.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000988.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000989.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000990.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000991.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000992.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000993.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000994.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000995.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000996.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000997.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000998.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00000999.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001000.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001001.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001002.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001003.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001004.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001005.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001006.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001007.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001008.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001009.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001010.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001011.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001012.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001013.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001014.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001015.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001016.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001017.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001018.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001019.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001020.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001021.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001022.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001023.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001024.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001025.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001026.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001027.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001028.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001029.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001030.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001031.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001032.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001033.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001034.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001035.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001036.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001037.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001038.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001039.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001040.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001041.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001042.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001043.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001044.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001045.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001046.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001047.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001048.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001049.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001050.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001051.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001052.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001053.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001054.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001055.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001056.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001057.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001058.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001059.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001060.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001061.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001062.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001063.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001064.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001065.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001066.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001067.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001068.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001069.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001070.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001071.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001072.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001073.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001074.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001075.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001076.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001077.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001078.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001079.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001080.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001081.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001082.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001083.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001084.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001085.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001086.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001087.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001088.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001089.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001090.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001091.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001092.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001093.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001094.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001095.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001096.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001097.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001098.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001099.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001100.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001101.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001102.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001103.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001104.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001105.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001106.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001107.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001108.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001109.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001110.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001111.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001112.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001113.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001114.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001115.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001116.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001117.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001118.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001119.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001120.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001121.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001122.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001123.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001124.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001125.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001126.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001127.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001128.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001129.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001130.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001131.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001132.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001133.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001134.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001135.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001136.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001137.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001138.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001139.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001140.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001141.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001142.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001143.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001144.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001145.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001146.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001147.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001148.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001149.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001150.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001151.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001152.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001153.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001154.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001155.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001156.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001157.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001158.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001159.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001160.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001161.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001162.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001163.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001164.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001165.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001166.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001167.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001168.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001169.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001170.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001171.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001172.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001173.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001174.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001175.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001176.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001177.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001178.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001179.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001180.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001181.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001182.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001183.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001184.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001185.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001186.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001187.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001188.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001189.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001190.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001191.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001192.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001193.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001194.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001195.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001196.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001197.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001198.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001199.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001200.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001201.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001202.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001203.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001204.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001205.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001206.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001207.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001208.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001209.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001210.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001211.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001212.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001213.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001214.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001215.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001216.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001217.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001218.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001219.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001220.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001221.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001222.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001223.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001224.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001225.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001226.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001227.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001228.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001229.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001230.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001231.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001232.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001233.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001234.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001235.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001236.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001237.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001238.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001239.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001240.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001241.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001242.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001243.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001244.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001245.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001246.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001247.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001248.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001249.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001250.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001251.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001252.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001253.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001254.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001255.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001256.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001257.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001258.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001259.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001260.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001261.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001262.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001263.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001264.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001265.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001266.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001267.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001268.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001269.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001270.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001271.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001272.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001273.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001274.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001275.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001276.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001277.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001278.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001279.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001280.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001281.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001282.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001283.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001284.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001285.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001286.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001287.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001288.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001289.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001290.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001291.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001292.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001293.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001294.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001295.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001296.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001297.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001298.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001299.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001300.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001301.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001302.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001303.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001304.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001305.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001306.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001307.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001308.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001309.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001310.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001311.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001312.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001313.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001314.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001315.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001316.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001317.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001318.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001319.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001320.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001321.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001322.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001323.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001324.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001325.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001326.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001327.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001328.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001329.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001330.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001331.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001332.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001333.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001334.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001335.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001336.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001337.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001338.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001339.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001340.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001341.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001342.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001343.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001344.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001345.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001346.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001347.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001348.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001349.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001350.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001351.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001352.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001353.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001354.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001355.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001356.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001357.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001358.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001359.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001360.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001361.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001362.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001363.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001364.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001365.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001366.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001367.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001368.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001369.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001370.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001371.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001372.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001373.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001374.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001375.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001376.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001377.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001378.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001379.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001380.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001381.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001382.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001383.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001384.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001385.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001386.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001387.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001388.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001389.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001390.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001391.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001392.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001393.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001394.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001395.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001396.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001397.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001398.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001399.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001400.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001401.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001402.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001403.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001404.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001405.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001406.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001407.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001408.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001409.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001410.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001411.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001412.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001413.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001414.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001415.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001416.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001417.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001418.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001419.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001420.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001421.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001422.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001423.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001424.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001425.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001426.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001427.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001428.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001429.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001430.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001431.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001432.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001433.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001434.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001435.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001436.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001437.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001438.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001439.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001440.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001441.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001442.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001443.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001444.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001445.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001446.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001447.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001448.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001449.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001450.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001451.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001452.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001453.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001454.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001455.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001456.png"
#     pause 0.0166666666666667
#     "images/pac/staff/00001457.png"
#     pause 0.0166666666666667

#######################################################################################
# 定义紙吹雪动画
image papersnow:
    "images/pac/紙吹雪/00000001.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000002.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000003.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000004.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000005.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000006.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000007.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000008.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000009.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000010.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000011.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000012.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000013.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000014.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000015.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000016.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000017.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000018.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000019.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000020.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000021.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000022.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000023.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000024.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000025.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000026.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000027.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000028.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000029.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000030.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000031.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000032.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000033.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000034.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000035.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000036.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000037.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000038.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000039.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000040.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000041.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000042.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000043.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000044.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000045.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000046.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000047.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000048.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000049.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000050.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000051.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000052.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000053.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000054.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000055.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000056.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000057.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000058.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000059.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000060.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000061.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000062.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000063.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000064.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000065.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000066.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000067.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000068.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000069.png"
    pause 0.0166666666666667
    "images/pac/紙吹雪/00000070.png"
    pause 0.0166666666666667

#######################################################################################
# 定义SEND动画
image send:
    "images/pac/SEND/00000001.png"
    pause 0.03
    "images/pac/SEND/00000002.png"
    pause 0.03
    "images/pac/SEND/00000003.png"
    pause 0.03
    "images/pac/SEND/00000004.png"
    pause 0.03
    "images/pac/SEND/00000005.png"
    pause 0.03
    "images/pac/SEND/00000006.png"
    pause 0.03
    "images/pac/SEND/00000007.png"
    pause 0.03
    "images/pac/SEND/00000008.png"
    pause 0.03
    "images/pac/SEND/00000009.png"
    pause 0.03
    "images/pac/SEND/00000010.png"
    pause 0.03
    "images/pac/SEND/00000011.png"
    pause 0.03
    "images/pac/SEND/00000012.png"
    pause 0.03
    "images/pac/SEND/00000013.png"
    pause 0.03
    "images/pac/SEND/00000014.png"
    pause 0.03
    "images/pac/SEND/00000015.png"
    pause 0.03
    repeat

###### 定义：界面（screen） ####
# align (0.5,0.5)阔以将其放在中间
screen callscr:
    add "callgif" align (0.5,0.5)

screen send:
    add "send" align (0.5,0.5)

screen letsrockscr:
    add "letsrock" align (0.5,0.5)

screen staff:
    add "staff" align (0.5,0.5)

screen papersnow:
    add "papersnow" align (0.5,0.5)


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

# Author:Luckykeeper
# Blog：http://b.luckykeeper.site
# 脚本模块
# 开坑日期 2021年8月28日

#----------------------------------------------------------------
# 主程序开始
# Author:Luckykeeper
# Blog：http://b.luckykeeper.site
# 开始日期 2021年8月28日
# 修订日期 2021年9月5日

# 制作流程
# ①导入全部文本+润色汉化，不带图像
# ②修图，替换日语内容
# ③为op加上嵌入字幕（ass，然后嵌入），参考十月翻译组版本；为里面的视频加字幕
# ④完成视觉资源的waifu2x，从720p放大到2K
#（主流手机屏幕和大多数设备的情况，大小和质量的均衡点（偏质量）根据之前的测试，视频插帧效果不好，所以只放大）
# ⑤导入图像和视频，对照程序逆向出特效，以及音频（音频不需要进行处理）
# ⑥制作GUI
# ⑦打包发布

# 翻译原则
# a、采用机翻+润色的方式进行，因为我是个日语渣，翻译初稿来自百度为主+彩云小译为辅的结果
# b、主体采用意译的方式，因为本来就是电波向作品，很多地方并不好直译
# c、不会翻的地方使用 // 标出，希望老哥们帮帮忙
# d、翻译力图在尽量准确的同时最大程度的让文字变得有趣，希望让本作受到更多人的喜爱
# e、第一次做翻译，也是第一次用ren'py，活整的不好还请带伙见谅

# 流程 ①
# Author:Luckykeeper
# Blog：http://b.luckykeeper.site
# 开始日期 2021年8月28日
# 主程序正式开始，现在只加入文本
# 版本：null（还未完成）

# 定义callgif
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

# ###### 定义：界面（screen） ####
screen callscr:
    add "callgif" align (0.5,0.5)

# 一周目开始前 主题BGM：anonatsu_piano.ogg

label start:
# 游戏开始
    stop music # 停止主菜单音乐
    play sound "voice/effect/start.ogg" # 播放开始音效
    with fade # 主菜单到正式游戏的过场
    pause 0.8
    jump scene01 # 开始 scene01 的脚本

# 一周目，共通线（一周目莫得选项）

# sence01
# Author:Luckykeeper
# Blog：http://b.luckykeeper.site
# 开始日期 2021年8月28日
# 版本：null（还未完成）

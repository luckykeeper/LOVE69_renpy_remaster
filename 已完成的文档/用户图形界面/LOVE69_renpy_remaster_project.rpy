# --------------------------------
# LOVE69_Renpy_Remaster_Project
# 开场动画设定脚本
# Author:Luckykeeper
# 版本 0.6 "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年3月17日

# image pure_black = "#000"
# 开场画面
# $ renpy.pause(1, hard=True) 在每一个不想被跳过的scene、show和hide语句的下一行，都加上一句，就能阻止鼠标点击跳过
# 务必注意文件命名不要重复，这里的图片不需要定义和导入，放在 images/splashscreen 即可直接食用
# 这里的声音初步判断是由se里面的门的声音（07_ドア1～あける）+心爱的voice 实际填voice的时候应该能找到
label splashscreen:
    # 同人logo
    show ロゴ at truecenter with Dissolve(1.0)
    # 这里的开门声对了，但是人物声音是不对的，Demo版暂时使用这个音声占位，原版应该是心爱的语音，后面应该是能找到的，找到了再换上
    # 找到啦！
    play sound "voice/effect/07_ドア1～あける.ogg"
    pause 1.0
    voice "voice/心愛/cca_a1_0331.ogg"
    $ renpy.pause(1.5, hard=True)
    pause 1.5
    $ renpy.pause(1, hard=True)
    hide ロゴ with Dissolve(1.0)
    $ renpy.pause(1, hard=True)

    # LOVE69_Renpy_Remaster_Project
    show pureblack at truecenter
    show love69renpyremasterproject at truecenter with Dissolve(1.0)
    $ renpy.pause(1, hard=True)
    pause 1.0
    $ renpy.pause(1, hard=True)
    hide love69renpyremasterproject with Dissolve(1.0)
    hide pureblack
    $ renpy.pause(1, hard=True)

    # Warning 后面会做，要修图，记得一定要加上癫痫提醒，里面很多地方闪来闪去，不然会死人的！
    # 已经做了
    # show white:
    #     zoom 2.0

        # caution 画面，开发时注释
    # show caution with Dissolve(1.0):
    #     zoom 0.24
    # $ renpy.pause(10, hard=True)
    # pause 10.0
    # $ renpy.pause(10, hard=True)
    # 关于 caution 画面的小说明
    # 有的人可能会觉得 caution 画面显示时间太长了（10s），而且用鼠标还没有办法跳过（其实我也这么觉得，后面可能会取消吧）
    # 如果你恰巧看到了这里，其实这个画面看过一次之后是可以像对话一样用 Ctrl 键来C过去的（doge）
    # 不过移动端就没有 Ctrl 键了，嘛，开始之前去稍微活动一下不是也挺好的嘛（doge）

    hide caution with Dissolve(1.0)
    $ renpy.pause(1, hard=True)


# 主菜单之前

# label before_main_menu:

#     pass

# 主菜单

# label main_menu:

#     pass


# 2022年1月7日 关于Warning后的想法
# A：提示到游戏目录“初次打开前查看”文件看说明（推奖）
# B：再写一个说明放在后面
# 原因：
# 1、可以写更多东西（做成可以跳过的）
# 2、不再拖启动时间了
# 3、可以让人注意到游戏目录里面的彩蛋（彩蛋后面还要放不少东西，关于原作 Bug 的吐槽(都做成 PDF 版)，豆知识统一做 PDF 文档考证，取消 Demo 版的加密压缩包方式）
# （汉化的一些小彩蛋(可能会有)，关于原版的两个彩蛋(前作免费领)可能会先放在这里，等等）

# 2022年1月13日，关于Cation画面的想法
#   考虑仅第一次打开时间长，以后时间短且可跳过

# --------------------------------
# LOVE69_Renpy_Remaster_Project
# 开场动画设定
# Author:Luckykeeper
# 版本 0.0.4
# Blog：http://b.luckykeeper.site
# 修订日期 2021年8月30日

# image pure_black = "#000"
# 开场画面
# $ renpy.pause(1, hard=True) 在每一个不想被跳过的scene、show和hide语句的下一行，都加上一句，就能阻止鼠标点击跳过
# 务必注意文件命名不要重复，这里的图片不需要定义和导入，放在 images/splashscreen 即可直接食用
label splashscreen:
    # 同人logo
    show ロゴ at truecenter with Dissolve(1.0)
    $ renpy.pause(1, hard=True)
    pause 1.0
    $ renpy.pause(1, hard=True)
    hide ロゴ with Dissolve(1.0)
    $ renpy.pause(1, hard=True)
    # # Warning 后面会做，要修图
    # show coution at truecenter with Dissolve(1.0)
    # $ renpy.pause(1, hard=True)
    # pause 1.0
    # $ renpy.pause(1, hard=True)
    # hide coution with Dissolve(1.0)
    # $ renpy.pause(1, hard=True)
    # LOVE69_Renpy_Remaster_Project
    show pureblack at truecenter
    show love69renpyremasterproject at truecenter with Dissolve(1.0)
    $ renpy.pause(1, hard=True)
    pause 1.0
    $ renpy.pause(1, hard=True)
    hide love69renpyremasterproject with Dissolve(1.0)
    hide pureblack
    $ renpy.pause(1, hard=True)

# 主菜单之前

# label before_main_menu:

#     pass

# 主菜单

# label main_menu:

#     pass

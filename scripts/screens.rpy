# --------------------------------
# LOVE69_Renpy_Remaster_Project
# 各种GUI设定的详细设置
# Author:Luckykeeper
# 版本 NightBuild "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年5月1日

################################################################################
## 初始化
################################################################################

init offset = -1




################################################################################
## 定义几个全局变量
## 全局变量需要 init python in 命名空间，使用时引入
    # init python:
    #     import store.命名空间 as xxx
### 以上需要在if外使用
################################################################################
### SideImage() 相关
# 显示初始size（真冬）的参数
# 使用下面这样的语句阔以针对不同大小的入参人物分别调整
#    $ sideimagesize.SideImageXalign = 0.0
#    $ sideimagesize.SideImageYalign = -50
#    $ sideimagesize.SideImageZoom = 0.5
# 下面三个参数需要先给出初始值，通过持久化数据存储这些参数
init python in sideimagesize:
    # 这里的缩放莫名其妙多了一格，不知道为啥，姑且删掉
    SideImageXalign = 0.08
    SideImageYalign = -29.35
    SideImageZoom = 0.95

# 针对大的 add SideImage() xalign 0.12 yalign 9.1 zoom 0.35 使用时调用以下参数
# SideImageXalign = 0.0
# SideImageYalign = 1.0
# SideImageZoom = 0.0

################################################################################
## 样式
################################################################################

style default:
    properties gui.text_properties()
    language gui.language
    # 全部字体描边，增强可读性
    outlines [(1, "#0c65c9", 1, 1)]

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 游戏内界面
################################################################################


## 对话界面 ########################################################################
##
## 对话界面用于向玩家显示对话。它需要两个参数，“who”和“what”，分别是叙述人的名称
## 和所叙述的内容。（如果没有名称，参数“who”可以是“None”。）
##
## 此界面必须创建一个 id 为“what”的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为“who”和 id 为“window”的可视控件来应用样式属性。
##
## https://www.renpy.cn/doc/screen_special.html#say

# 设置音频不中断
## https://renpy.cn/doc/preferences.html?highlight=preference#var-preferences.voice_sustain
default preferences.voice_sustain = True

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        # 在这里从命名空间导入变量，记得需要在if判断体前完成哦，不过不能超出window部分
        # 2021年10月26日 下面这句居然开始报warning（store.sideimagesize，去store就好，但是跑不起来）了，但是store不能去，去了就炸
        # 开发使用Ren'py7.4.6，此时官网最新版为7.4.10，怀疑是新版改了些什么东西
        # 暂时不考虑升级最新版，但是由于这版在Win11视频解码存在问题，最终做完之后考虑上下最新版
        # 2022年1月28日 报warning 的问题应该是IDE插件的锅，现在没有了
        # 而解码实际上没有问题，应该只是W的电脑太菜了解不动2K
        $ import store.sideimagesize as sideimagesize104

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        # text what id "what"
        # if renpy.is_seen(ever = True) and persistent.lightRead: 这句在移动端似乎不起作用？
        # 已读未读文本不同颜色

        # 增加描边
        # https://www.renpy.cn/thread-278-1-1.html
        if renpy.is_seen(ever = True):  # ever 为false时对本次运行起效，此处需要对过去所有阅读起效
            text what id "what" color "#f9d198" # 标记颜色
        else:
            text what id "what" color "#FFFFFF" # 未读颜色


    ## 如果有对话框头像，会将其显示在文本之上。请不要在手机界面下显示这个，因为
    ## 没有空间。
    # 小头像的位置在这里调整 用zoom可以缩放图片
    ### if not renpy.variant("small"):
    ### add SideImage() xalign 0.0 yalign 1.0
    ### 针对大的 add SideImage() xalign 0.12 yalign 9.1 zoom 0.35

    if not renpy.variant("small"):

        add SideImage() xalign sideimagesize.SideImageXalign yalign sideimagesize.SideImageYalign zoom sideimagesize.SideImageZoom


# 定义 ctc ，就是一般 gal 里面提示“单击继续”的那个小箭头/符号

screen ctc():
    add "texticon" align (0.99,0.91)

image texticon:
    "gui/texticon/icon_01.png"
    pause 0.1
    "gui/texticon/icon_02.png"
    pause 0.1
    "gui/texticon/icon_03.png"
    pause 0.1
    "gui/texticon/icon_04.png"
    pause 0.1
    "gui/texticon/icon_05.png"
    pause 0.1
    "gui/texticon/icon_06.png"
    pause 0.1
    "gui/texticon/icon_07.png"
    pause 0.1
    "gui/texticon/icon_08.png"
    pause 0.1
    "gui/texticon/icon_09.png"
    pause 0.1
    "gui/texticon/icon_10.png"
    pause 0.1
    repeat

## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## 输入界面 ########################################################################
##
## 此界面用于显示 renpy.input。“prompt”参数用于传递文本提示。
##
## 此界面必须创建一个 id 为“input”的输入可视控件来接受各种输入参数。
##
## https://www.renpy.cn/doc/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## 选择界面 ########################################################################
##
## 此界面用于显示由“menu”语句生成的游戏内选项。参数“items”是一个对象列表，每个对
## 象都有标题和操作字段。
##
## https://www.renpy.cn/doc/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## 若为 True，菜单内的叙述会使用旁白角色。若为 False，叙述会显示为菜单内的文字说
## 明。
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## 快捷菜单界面 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。

screen quick_menu():
    # Ren'Py 提供了更改zorder的方法
    ## https://www.renpy.cn/doc/displaying_images.html?highlight=zorder#renpy.change_zorder
    ## 确保该菜单出现在其他界面之上，
    zorder 100


    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            # 旧 quick_menu 之 textbutton
            # # textbutton _("回退") action Rollback()
            # # textbutton _("历史") action ShowMenu('history')
            # textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            # textbutton _("自动") action Preference("auto-forward", "toggle")
            # textbutton _("保存") action ShowMenu("game_save")
            # textbutton _("读取") action ShowMenu("game_load")
            # textbutton _("快存") action QuickSave()
            # textbutton _("快读") action QuickLoad()
            # textbutton _("设置") action ShowMenu('preferences')

            # 新 quick_menu 之 image button
            ## 对 btn 的顺序进行微调

            # 存档
            imagebutton:
                idle "gui/quick_menu/btn_save_base.png"
                hover "gui/quick_menu/btn_save_onMouse.png"
                selected_hover "gui/quick_menu/btn_save_onClick.png"
                hover_sound "voice/effect/マウス乗せ音.ogg"
                activate_sound "voice/effect/メニュー決定音.ogg"
                action ShowMenu("game_save")

            # 读档
            imagebutton:
                idle "gui/quick_menu/btn_load_base.png"
                hover "gui/quick_menu/btn_load_onMouse.png"
                selected_hover "gui/quick_menu/btn_load_onClick.png"
                hover_sound "voice/effect/マウス乗せ音.ogg"
                activate_sound "voice/effect/メニュー決定音.ogg"
                action ShowMenu("game_load")

            # Q.Save
            imagebutton:
                idle "gui/quick_menu/btn_qsave_base.png"
                hover "gui/quick_menu/btn_qsave_onMouse.png"
                selected_hover "gui/quick_menu/btn_qsave_onClick.png"
                hover_sound "voice/effect/マウス乗せ音.ogg"
                activate_sound "voice/effect/メニュー決定音.ogg"
                action QuickSave()

            # Q.Load
            imagebutton:
                idle "gui/quick_menu/btn_qload_base.png"
                hover "gui/quick_menu/btn_qload_onMouse.png"
                selected_hover "gui/quick_menu/btn_qload_onClick.png"
                hover_sound "voice/effect/マウス乗せ音.ogg"
                activate_sound "voice/effect/メニュー決定音.ogg"
                action QuickLoad()

            # 快进
            ## 快进和自动属于要保存状态的按钮，多一个 selected_idle 特性
            imagebutton:
                idle "gui/quick_menu/btn_skip_base.png"
                hover "gui/quick_menu/btn_skip_onMouse.png"
                selected_hover "gui/quick_menu/btn_skip_onClick.png"
                selected_idle "gui/quick_menu/btn_skip_Clicked.png"
                hover_sound "voice/effect/マウス乗せ音.ogg"
                activate_sound "voice/effect/メニュー決定音.ogg"
                action Skip() alternate Skip(fast=True, confirm=True)

            # 自动
            imagebutton:
                idle "gui/quick_menu/btn_auto_base.png"
                hover "gui/quick_menu/btn_auto_onMouse.png"
                selected_hover "gui/quick_menu/btn_auto_onClick.png"
                selected_idle "gui/quick_menu/btn_auto_Clicked.png"
                hover_sound "voice/effect/マウス乗せ音.ogg"
                activate_sound "voice/effect/メニュー決定音.ogg"
                action Preference("auto-forward", "toggle")

            # 设置
            imagebutton:
                idle "gui/quick_menu/btn_config_base.png"
                hover "gui/quick_menu/btn_config_onMouse.png"
                selected_hover "gui/quick_menu/btn_config_onClick.png"
                hover_sound "voice/effect/マウス乗せ音.ogg"
                activate_sound "voice/effect/メニュー決定音.ogg"
                action ShowMenu('preferences')


## 此语句确保只要玩家没有明确隐藏界面，就会在游戏中显示“quick_menu”界面。
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## 标题和游戏菜单界面
################################################################################

## 导航界面 ########################################################################
##
## 该界面包含在标题菜单和游戏菜单中，并提供导航到其他菜单，以及启动游戏。

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        # 功能已被新Main_Menu取代
        if main_menu:
            pass
            # textbutton _("开始游戏") action Start()

        else:

            textbutton _("历史") action ShowMenu("history")

            # textbutton _("保存") action ShowMenu("game_save")

        # textbutton _("读取游戏") action ShowMenu("game_load")

        textbutton _("设置") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("结束回放") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("标题界面") action MainMenu()

        textbutton _("关于") action ShowMenu("about")

        # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
        # if renpy.variant("pc") or (renpy.variant("web") and renpy.variant("mobile")):

            ## “帮助”对移动设备来说并非必需或相关。
        textbutton _("帮助") action ShowMenu("help")

        if renpy.variant("pc"):

            ## “退出”按钮在 iOS 上被禁止设置，在安卓和网页上也不是必需的。
            textbutton _("退出") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## 标题菜单界面 ######################################################################
##
## 用于在 Ren'Py 启动时显示标题菜单。
##
## https://www.renpy.cn/doc/screen_special.html#main-menu

# 新 Main_Menu ，采用图片 Button 进行引导
screen main_menu():

    ## tag menu 的作用是来清其它界面，确保不被覆盖
    tag menu

    # 也可以直接引入一张图片
    add "gui/main_menu/main_menu_1.png"

    # 因为按钮大小不一，单独定制位置
    # Start btn 的 vbox
    vbox:
        # 定位
        ## xalign 1.0->在最左边
        ## yalign 0->在最上面
        xalign 1.0
        yalign 0

        imagebutton:
            # Start btn 放大到 1080p 对应的大小是 380x193 px ，稍稍大几个像素方便定位
            ## idle 初始状态
            ## hover 鼠标放在上面的状态
            ## selected_hover 按下 btn 的状态
            idle "gui/main_menu/btn_start_base.png"
            hover "gui/main_menu/btn_start_onMouse.png"
            selected_hover "gui/main_menu/btn_start_onClick.png"
            hover_sound "voice/effect/マウス乗せ音.ogg"
            activate_sound "voice/effect/メニュー決定音.ogg"
            action Start()

    # Load btn 的 vbox
    vbox:
        # 定位
        xalign 0.891
        yalign 0.25

        imagebutton:
            # Load btn 放大到 1080p 对应的大小是 191x304 px ，稍稍大几个像素方便定位
            ## idle 初始状态
            ## hover 鼠标放在上面的状态
            ## selected_hover 按下 btn 的状态
            idle "gui/main_menu/btn_load_base.png"
            hover "gui/main_menu/btn_load_onMouse.png"
            selected_hover "gui/main_menu/btn_load_onClick.png"
            hover_sound "voice/effect/マウス乗せ音.ogg"
            activate_sound "voice/effect/メニュー決定音.ogg"
            action ShowMenu("game_load")


# Q.Load 功能
    # # 手机端第一次会报错，但是功能正常
    # ## https://www.renpy.cn/thread-843-1-1.html
    # $ latest_file = renpy.newest_slot(regexp=None)
    # $ latest_file_str = str(latest_file)

    # # 测试：防止移动端抛出错误
    # # AttributeError: 'NoneType' object has no attribute 'split'
    # ## https://www.cnblogs.com/shijieli/p/10791247.html
    # # $ latest_file = latest_file.encode("utf-8")

    # # 仍然出错，继续尝试
    # # 'NoneType' object has no attribute 'encoding'
    # ## https://www.cnblogs.com/wxvirus/p/14774838.html
    # # $ latest_file = latest_file.encode("utf8")

    # $ l_f_page = latest_file_str.split('-',1)[0] #所在页 #auto-1表示自动存档页第一位
    # $ l_f_name = latest_file_str.split('-',1)[1] #槽位名

    # 用 try 防止抛出错误

    $ latest_file = renpy.newest_slot(regexp=None)
    default l_f_page = "auto"
    default l_f_name = "1"

# 似乎不影响运行，用 try 来跑，转最下



    # Q.Load btn 的 vbox
    vbox:
        # 定位
        xalign 1.0
        yalign 0.25
        if persistent.gameStarted: # 防止没有开始游戏就去点击导致的出错
            imagebutton:
                # Q.Load btn 放大到 1080p 对应的大小是 191x304 px ，稍稍大几个像素方便定位
                ## idle 初始状态
                ## hover 鼠标放在上面的状态
                ## selected_hover 按下 btn 的状态
                idle "gui/main_menu/btn_qload_base.png"
                hover "gui/main_menu/btn_qload_onMouse.png"
                selected_hover "gui/main_menu/btn_qload_onClick.png"
                hover_sound "voice/effect/マウス乗せ音.ogg"
                activate_sound "voice/effect/メニュー決定音.ogg"
                action [FileLoad(name=l_f_name, confirm=True, page=l_f_page)]
                # action [FileLoad(name=renpy.newest_slot(regexp=None).split('-',1)[0], confirm=True, page=renpy.newest_slot(regexp=None).split('-',1)[1])]

    # Config btn 的 vbox
    vbox:
        # 定位
        xalign 1.0
        yalign 0.64

        imagebutton:
            # Config btn 放大到 1080p 对应的大小是 191x304 px ，稍稍大几个像素方便定位
            ## idle 初始状态
            ## hover 鼠标放在上面的状态
            ## selected_hover 按下 btn 的状态
            idle "gui/main_menu/btn_config_base.png"
            hover "gui/main_menu/btn_config_onMouse.png"
            selected_hover "gui/main_menu/btn_config_onClick.png"
            hover_sound "voice/effect/マウス乗せ音.ogg"
            activate_sound "voice/effect/メニュー決定音.ogg"
            action ShowMenu("preferences")

    # Extra btn 的 vbox
    ## Extra 涉及到周目，由可变的 btn 组成，根据周目变量变化
    ## Extra 功能待做
    vbox:
        # 定位
        xalign 0.891
        yalign 0.64
        if persistent.one: # 一周目完成之后可以进入 Extra
        # if 1==1: # 调试用
            imagebutton:
                # Extra btn 放大到 1080p 对应的大小是 191x304 px ，稍稍大几个像素方便定位
                ## idle 初始状态
                ## hover 鼠标放在上面的状态
                ## selected_hover 按下 btn 的状态
                idle "gui/main_menu/btn_extra_base.png"
                hover "gui/main_menu/btn_extra_onMouse.png"
                selected_hover "gui/main_menu/btn_extra_onClick.png"
                hover_sound "voice/effect/マウス乗せ音.ogg"
                activate_sound "voice/effect/メニュー決定音.ogg"
                action ShowMenu("main_menu_2")

    # Project btn 的 vbox
    # 官方 Website 莫得了，所以这里就换 Project 的 Website 好了
    # 这个页面还没做，先跳转about页面
    vbox:
        # 定位
        xalign 1.0
        yalign 0.87

        imagebutton:
            # End btn 放大到 1080p 对应的大小是 381x125 px ，稍稍大几个像素方便定位
            ## idle 初始状态
            ## hover 鼠标放在上面的状态
            ## selected_hover 按下 btn 的状态
            idle "gui/main_menu/btn_project_base.png"
            hover "gui/main_menu/btn_project_onMouse.png"
            selected_hover "gui/main_menu/btn_project_onClick.png"
            hover_sound "voice/effect/マウス乗せ音.ogg"
            activate_sound "voice/effect/メニュー決定音.ogg"
            action OpenURL("https://love69renpyremasterproject.github.io/")

    # End btn 的 vbox
    vbox:
        # 定位
        xalign 1.0
        yalign 1.0

        imagebutton:
            # End btn 放大到 1080p 对应的大小是 381x125 px ，稍稍大几个像素方便定位
            ## idle 初始状态
            ## hover 鼠标放在上面的状态
            ## selected_hover 按下 btn 的状态
            idle "gui/main_menu/btn_end_base.png"
            hover "gui/main_menu/btn_end_onMouse.png"
            selected_hover "gui/main_menu/btn_end_onClick.png"
            hover_sound "voice/effect/マウス乗せ音.ogg"
            activate_sound "voice/effect/メニュー決定音.ogg"
            action Quit(confirm=True)

##################################################################################
# main_menu_2
screen main_menu_2():

    ## tag menu 的作用是来清其它界面，确保不被覆盖
    tag menu

    # 引入图片
    add "gui/main_menu/main_menu_2.png"

    vbox:
        # 尝试统一定位
        # 可以通过以下方法来排列图标，比上面的方法更好，处理图片时按比例缩放到指定宽度即可
        xalign 1.0
        yalign 0
        # Gallery
        hbox:
            imagebutton:
                idle "gui/main_menu/btn_cgmode_base.png"
                hover "gui/main_menu/btn_cgmode_onMouse.png"
                selected_hover "gui/main_menu/btn_cgmode_onClick.png"
                hover_sound "voice/effect/マウス乗せ音.ogg"
                activate_sound "voice/effect/メニュー決定音.ogg"
                action ShowMenu("gallery")

        # Replay
        hbox:
            imagebutton:
                idle "gui/main_menu/btn_replaymode_base.png"
                hover "gui/main_menu/btn_replaymode_onMouse.png"
                selected_hover "gui/main_menu/btn_replaymode_onClick.png"
                hover_sound "voice/effect/マウス乗せ音.ogg"
                activate_sound "voice/effect/メニュー決定音.ogg"
                action ShowMenu("replay")

        # Music
        hbox:
            imagebutton:
                idle "gui/main_menu/btn_bgmmode_base.png"
                hover "gui/main_menu/btn_bgmmode_onMouse.png"
                selected_hover "gui/main_menu/btn_bgmmode_onClick.png"
                hover_sound "voice/effect/マウス乗せ音.ogg"
                activate_sound "voice/effect/メニュー決定音.ogg"
                action ShowMenu("music_room")

        # ExtraGames
        hbox:
            imagebutton:
                idle "gui/main_menu/btn_exgame_base.png"
                hover "gui/main_menu/btn_exgame_onMouse.png"
                selected_hover "gui/main_menu/btn_exgame_onClick.png"
                hover_sound "voice/effect/マウス乗せ音.ogg"
                activate_sound "voice/effect/メニュー決定音.ogg"
                action ShowMenu("extra_games")

        # Back
        hbox:
            imagebutton:
                idle "gui/main_menu/btn_omakeback_base.png"
                hover "gui/main_menu/btn_omakeback_onMouse.png"
                selected_hover "gui/main_menu/btn_omakeback_onClick.png"
                hover_sound "voice/effect/マウス乗せ音.ogg"
                activate_sound "voice/effect/メニュー決定音.ogg"
                # 这里不能用 MainMenu() ，只能用 ShowMenu 来返回
                action ShowMenu("main_menu")

        # Exit
        hbox:
            imagebutton:
                idle "gui/main_menu/btn_end_base.png"
                hover "gui/main_menu/btn_end_onMouse.png"
                selected_hover "gui/main_menu/btn_end_onClick.png"
                hover_sound "voice/effect/マウス乗せ音.ogg"
                activate_sound "voice/effect/メニュー決定音.ogg"
                action Quit(confirm=True)




# 以下是初始 Main_Menu 备份
# screen main_menu():

#     ## 此语句可确保替换掉任何其他菜单界面。
#     tag menu

#     add gui.main_menu_background

#     ## 此空框可使标题菜单变暗。
#     frame:
#         style "main_menu_frame"

#     ## “use”语句将其他的界面包含进此界面。标题界面的实际内容在导航界面中。
#     use navigation

#     if gui.show_name:

#         vbox:
#             style "main_menu_vbox"

#             text "[config.name!t]":
#                 style "main_menu_title"

#             text "[config.version]":
#                 style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## 游戏菜单界面 ######################################################################
##
## 此界面列出了游戏菜单的基本共同结构。可使用界面标题调用，并显示背景、标题和导
## 航菜单。
##
## “scroll”参数可以是“None”，也可以是“viewport”或“vpgrid”。当此界面与一个或多个
## 子菜单同时使用时，这些子菜单将被转移（放置）在其中。

# 新 Game_Menu （还没有开始改动捏）
screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 导航部分的预留空间。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("返回"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

# 以下是初始 Game_Menu 备份
# screen game_menu(title, scroll=None, yinitial=0.0):

#     style_prefix "game_menu"

#     if main_menu:
#         add gui.main_menu_background
#     else:
#         add gui.game_menu_background

#     frame:
#         style "game_menu_outer_frame"

#         hbox:

#             ## 导航部分的预留空间。
#             frame:
#                 style "game_menu_navigation_frame"

#             frame:
#                 style "game_menu_content_frame"

#                 if scroll == "viewport":

#                     viewport:
#                         yinitial yinitial
#                         scrollbars "vertical"
#                         mousewheel True
#                         draggable True
#                         pagekeys True

#                         side_yfill True

#                         vbox:
#                             transclude

#                 elif scroll == "vpgrid":

#                     vpgrid:
#                         cols 1
#                         yinitial yinitial

#                         scrollbars "vertical"
#                         mousewheel True
#                         draggable True
#                         pagekeys True

#                         side_yfill True

#                         transclude

#                 else:

#                     transclude

#     use navigation

#     textbutton _("返回"):
#         style "return_button"

#         action Return()

#     label title

#     if main_menu:
#         key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## 关于界面 ########################################################################
##
## 此界面提供有关游戏和 Ren'Py 的制作人员和版权信息。
##
## 此界面没有什么特别之处，因此它也是如何制作自定义界面的一个例子。

screen about():

    tag menu

    ## 此“use”语句将包含“game_menu”界面到此处。子级“vbox”将包含在“game_menu”界面
    ## 的“viewport”内。
    use game_menu(_("关于"), scroll="viewport"):

        style_prefix "about"

        vbox:

            # label "[config.name!t]"
            # text _("版本 [config.version!t]\n")

            ## “gui.about”通常在 options.rpy 中设置。
            if gui.about:
                text "[gui.about!t]\n"

            # text _("Ren'Py引擎版本： [renpy.version_only]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## 读取和保存界面 #####################################################################
##
## 这些界面负责让玩家保存游戏并能够再次读取。由于它们几乎完全一样，因此它们都是
## 以第三方界面“file_slots”来实现的。
##
## https://www.renpy.cn/doc/screen_special.html#save https://www.renpy.cn/doc/
## screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))



screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("AutoSave"), quick=_("QuickSave"))

    use game_menu(title):

        fixed:

            ## 此语句确保输入控件在任意按钮执行前可以获取“enter”事件。
            order_reverse True

            ## 页面名称，可以通过单击按钮进行编辑。
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## 存档位网格。
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## 用于访问其他页面的按钮。
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## “range(1, 10)”给出 1 到 9 之间的数字。
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")



### 魔改存读档界面

screen game_save():

    tag menu

    add "gui/saveload/back_save.png"

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("AutoSave"), quick=_("QuickSave"))

    fixed:

        ## 此语句确保输入控件在任意按钮执行前可以获取“enter”事件。
        order_reverse True

        ## 页面名称，可以通过单击按钮进行编辑。
        button:
            style "page_label"

            key_events True
            xalign 0.5
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value

        ## 存档位网格。
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileSave(slot)

                    has vbox

                    add FileScreenshot(slot) xalign 0.5

                    text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("莫得存档")):
                        style "slot_time_text"

                    text FileSaveName(slot):
                        style "slot_name_text"

                    key "save_delete" action FileDelete(slot)

        ## 用于访问其他页面的按钮。
        hbox:
            style_prefix "page"

            xalign 0.5
            yalign 1.0

            spacing gui.page_spacing

            textbutton _("<") action FilePagePrevious()
            key "mousedown_4" action FilePagePrevious()

            if config.has_autosave:
                textbutton _("{#auto_page}A") action FilePage("auto")

            if config.has_quicksave:
                textbutton _("{#quick_page}Q") action FilePage("quick")

            ## “range(1, 10)”给出 1 到 9 之间的数字。
            for page in range(1, 21):
                textbutton "[page]" action FilePage(page)

            textbutton _(">") action FilePageNext()
            key "mousedown_5" action FilePageNext()

        vbox:
            xalign 0.90
            yalign 0.95

            imagebutton:
                idle "gui/saveload/btn_back_base.png"
                hover "gui/saveload/btn_back_onMouse.png"
                selected_hover "gui/saveload/btn_back_onClick.png"
                action Return()

        vbox:
            xalign 0.95
            yalign 0.90

            imagebutton:
                idle "gui/saveload/btn_title_base.png"
                hover "gui/saveload/btn_title_onMouse.png"
                selected_hover "gui/saveload/btn_title_onClick.png"
                action MainMenu()

        vbox:
            xalign 0.1
            yalign 0.95
            text "这是存档界面哦\n热知识: 在本页面内，将鼠标放在已经有存档的格子上，按键盘上的“Delete”键就可以删除已有存档啦~"


screen game_load():

    tag menu

    add "gui/saveload/back_load.png"

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("AutoSave"), quick=_("QuickSave"))

    fixed:

        ## 此语句确保输入控件在任意按钮执行前可以获取“enter”事件。
        order_reverse True

        ## 页面名称，可以通过单击按钮进行编辑。
        button:
            style "page_label"

            key_events True
            xalign 0.5
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value

        ## 存档位网格。
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileLoad(slot)

                    has vbox

                    add FileScreenshot(slot) xalign 0.5

                    text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("莫得存档")):
                        style "slot_time_text"

                    text FileSaveName(slot):
                        style "slot_name_text"

                    key "save_delete" action FileDelete(slot)


        ## 用于访问其他页面的按钮。
        hbox:
            style_prefix "page"

            xalign 0.5
            yalign 1.0

            spacing gui.page_spacing

            textbutton _("<") action FilePagePrevious()
            key "mousedown_4" action FilePagePrevious()

            if config.has_autosave:
                textbutton _("{#auto_page}A") action FilePage("auto")

            if config.has_quicksave:
                textbutton _("{#quick_page}Q") action FilePage("quick")

            ## “range(1, 10)”给出 1 到 9 之间的数字。
            for page in range(1, 21):
                textbutton "[page]" action FilePage(page)

            textbutton _(">") action FilePageNext()
            key "mousedown_5" action FilePageNext()

        vbox:
            xalign 0.90
            yalign 0.95

            imagebutton:
                idle "gui/saveload/btn_back_base.png"
                hover "gui/saveload/btn_back_onMouse.png"
                selected_hover "gui/saveload/btn_back_onClick.png"
                action Return()

        vbox:
            xalign 0.95
            yalign 0.90

            imagebutton:
                idle "gui/saveload/btn_title_base.png"
                hover "gui/saveload/btn_title_onMouse.png"
                selected_hover "gui/saveload/btn_title_onClick.png"
                action MainMenu()

        vbox:
            xalign 0.1
            yalign 0.95
            text "这是读档界面捏\n热知识: 在本页面内，将鼠标放在已经有存档的格子上，按键盘上的“Delete”键就可以删除已有存档啦~"





## 设置界面 ########################################################################
##
## 设置界面允许玩家配置游戏以更好地适应自己的习惯。
##
## https://www.renpy.cn/doc/screen_special.html#preferences

# 使用硬解
# https://www.renpy.cn/doc/config.html?highlight=config%20hw_video#var-config.hw_video

default persistent.hwVideo = False
define config.hw_video = persistent.hwVideo

########################
# 提升性能，用内存缓存提升加载速度
# 使用内存缓存（默认开启）
default persistent.useCache = True
define config.cache_surfaces = persistent.useCache

# HScene 梗图模式，默认关闭
default persistent.hsceneG = False

# persistent.mouseScroll 鼠标滚轮功能，默认关闭
default persistent.mouseScroll = False

screen preferences():

    tag menu

    use game_menu(_("设置"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("显示")
                        textbutton _("窗口") action Preference("display", "window")
                        textbutton _("全屏") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("回退操作区")
                    textbutton _("禁用") action Preference("rollback side", "disable")
                    textbutton _("屏幕左侧") action Preference("rollback side", "left")
                    textbutton _("屏幕右侧") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("快进")
                    textbutton _("未读文本") action Preference("skip", "toggle")
                    textbutton _("选项后继续") action Preference("after choices", "toggle")
                    textbutton _("忽略转场") action InvertSelected(Preference("transitions", "toggle"))

                vbox:
                    style_prefix "check"
                    label _("实验选项，重启生效")
                    textbutton _("使用软解（稳定）") :
                        action [SetVariable("persistent.hwVideo",False),renpy.save_persistent()]
                        tooltip "默认选项，调用软件解码器对媒体进行解码，非常稳定但是耗费性能，对低端设备不友好"
                    textbutton _("使用硬解（更快）") :
                        action [SetVariable("persistent.hwVideo",True),renpy.save_persistent()]
                        tooltip "调用硬件解码器对媒体进行解码，速度快且高效，前提需要设备支持（程序的媒体文件有主要有png、webm、ogg、webp四种，请确保您的设备支持），可能会导致一些问题，如遇到视频拉伸，无法正常播放等问题，请切换回软件解码器，如果你的设备不属于低性能设备，强烈建议使用软件解码器"
                    textbutton _("使用内存缓存"):
                        action [SetVariable("persistent.useCache",True),renpy.save_persistent()]
                        tooltip "默认选项，素材文件预缓存至内存再从内存调用，运行速度大幅提升，对低内存设备不友好，但是只需要有1.2G以上空闲内存或开启了虚拟内存（一般系统都是默认开启的）就可以放心选择此项"
                    textbutton _("直接从硬盘读取") :
                        action [SetVariable("persistent.useCache",False),renpy.save_persistent()]
                        tooltip "程序直接从硬盘读取素材文件，只使用必要的内存，对硬盘性能要求高，但是内存开销较小，适合低内存设备，但是若硬盘读取性能不佳时可能会发生卡顿现象"

                vbox:
                    style_prefix "check"
                    label _("要加点儿梗嘛")
                    textbutton _("关闭HScene梗图模式（默认，推荐）") :
                        action [SetVariable("persistent.hsceneG",False),renpy.save_persistent()]
                        tooltip "默认选项，不看项目组瞎整活，调整该选项不影响HScene(因为根本没有)，调整该选项理论上无需重启生效"
                    textbutton _("开启HScene梗图模式") :
                        action [SetVariable("persistent.hsceneG",True),renpy.save_persistent()]
                        tooltip "来看项目组胡乱整活，调整该选项不影响HScene(因为根本没有)，请根据个人喜好谨慎开启，调整该选项理论上无需重启生效"

                # 鼠标滚轮只针对有鼠标的平台生效
                if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                    vbox:
                        style_prefix "check"
                        label _("个性化")
                        textbutton _("禁用鼠标滚轮向下新对话") :
                            action [SetVariable("persistent.mouseScroll",False),renpy.save_persistent()]
                            tooltip "默认选项，鼠标滚轮仅用于回顾历史对话，需要重启生效"
                        textbutton _("启用鼠标滚轮向下新对话") :
                            action [SetVariable("persistent.mouseScroll",True),renpy.save_persistent()]
                            tooltip "使鼠标滚轮除回顾历史对话还能开始新对话，需要重启生效"
                ## 可以在此处添加类型为“radio_pref”或“check_pref”的其他“vbox”，
                ## 以添加其他创建者定义的首选项设置。

            # https://www.renpy.cn/doc/screen_actions.html?highlight=gettooltip#tooltips
                $ tooltip = GetTooltip()

            if tooltip:
                text "[tooltip]"

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("文字速度")

                    bar value Preference("text speed")

                    label _("自动前进时间")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("音乐音量")

                        hbox:
                            bar value Preference("music volume")


                    if config.has_sound:

                        label _("音效音量")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("测试") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("语音音量")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("测试") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("全部静音"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## 历史界面 ########################################################################
##
## 这是一个向玩家显示对话历史的界面。虽然此界面没有任何特殊之处，但它必须访问储
## 存在“_history_list”中的对话历史记录。
##
## https://www.renpy.cn/doc/history.html

screen history():

    tag menu

    ## 避免预缓存此界面，因为它可能非常大。
    predict False

    use game_menu(_("历史"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## 此语句可确保如果“history_height”为“None”的话仍可正常显示条
                ## 目。
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## 若角色颜色已设置，则从“Character”对象中读取颜色到叙述
                        ## 人文本中。
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                # 历史记录跳跃
                ## https://www.renpy.cn/thread-221-1-1.html
                textbutton what:

                    substitute False
                    style "history_text"
                    action Confirm("要跳转到该处吗？", yes=RollbackToIdentifier(h.rollback_identifier), no=None, confirm_selected=False),

        if not _history_list:
            label _("尚无对话历史记录。")

# 旧 history 存档
# screen history():

#     tag menu

#     ## 避免预缓存此界面，因为它可能非常大。
#     predict False

#     use game_menu(_("历史"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

#         style_prefix "history"

#         for h in _history_list:

#             window:

#                 ## 此语句可确保如果“history_height”为“None”的话仍可正常显示条
#                 ## 目。
#                 has fixed:
#                     yfit True

#                 if h.who:

#                     label h.who:
#                         style "history_name"
#                         substitute False

#                         ## 若角色颜色已设置，则从“Character”对象中读取颜色到叙述
#                         ## 人文本中。
#                         if "color" in h.who_args:
#                             text_color h.who_args["color"]

#                 $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
#                 # 历史记录跳跃
#                 ## https://www.renpy.cn/thread-221-1-1.html
#                 textbutton what:

#                     substitute False
#                     style "history_text"
#                     action Confirm("要跳转到该处吗？", yes=RollbackToIdentifier(h.rollback_identifier), no=None, confirm_selected=False),

#         if not _history_list:
#             label _("尚无对话历史记录。")


## 此语句决定了允许在历史记录界面上显示哪些标签。

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## 帮助界面 ########################################################################
##
## 提供有关键盘和鼠标映射信息的界面。它使用其它界面
## （“keyboard_help”，“mouse_help“和”gamepad_help“）来显示实际的帮助内容。

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("帮助"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 30

            hbox:

                textbutton _("键盘和设置帮助") action SetScreenVariable("device", "keyboard")
                textbutton _("鼠标") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("手柄") action SetScreenVariable("device", "gamepad")

                # 在这里加上豆知识速查，第一次游玩提示一次有这个东西，然后不再提示
                # textbutton _("豆知识速查") action ShowMenu("douKnowledge")
                # 这里偷个懒，用和鼠标键盘类似的方式引入
                # textbutton _("设置帮助") action SetScreenVariable("device", "settingHelp")

                textbutton _("豆知识速查") action SetScreenVariable("device", "douKnowledge")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help
            elif 1==1:
                use douKnowledge
            # elif 1==1:
                # use settingHelp




screen keyboard_help():

    hbox:
        label _("回车")
        text _("推进对话并激活界面。")

    hbox:
        label _("空格")
        text _("推进对话但不激活选项。")

    hbox:
        label _("方向键")
        text _("导航界面。")

    hbox:
        label _("Esc")
        text _("访问游戏菜单。")

    hbox:
        label _("Ctrl")
        text _("按住时快进对话。")

    hbox:
        label _("Tab")
        text _("切换对话快进。")

    hbox:
        label _("Page Up")
        text _("回退至先前的对话。")

    hbox:
        label _("Page Down")
        text _("向前至之后的对话。")

    hbox:
        label "H"
        text _("隐藏用户界面。")

    hbox:
        label "S"
        text _("截图。")

    hbox:
        label "V"
        text _("切换辅助自动朗读。")

    hbox:
        label "Delete"
        text _("在存、读档界面可以删除存档")

    # hbox:
    #     label _("实验选项")
    #     text _("对设置中实验选项进行说明，注意更改实验选项必须重启游戏，否则可能不会生效")

    # hbox:
    #     label _("使用软解")
    #     text _("默认选项，调用软件解码器对媒体进行解码，非常稳定但是耗费性能，对低端设备不友好")

    # hbox:
    #     label _("使用硬解")
    #     text _("调用硬件解码器对媒体进行解码，速度快且高效，前提需要设备支持（程序的媒体文件有主要有png、webm、ogg三种，请确保您的设备支持），可能会导致一些问题，如遇到视频拉伸，无法正常播放等问题，请切换会软件解码器，如果你的设备不属于低性能设备，强烈建议使用软件解码器")

    # hbox:
    #     label _("使用内存缓存")
    #     text _("默认选项，素材文件预缓存至内存再从内存调用，运行速度大幅提升，对低内存设备不友好，但是只需要有1.2G以上空闲内存或开启了虚拟内存（一般系统都是默认开启的）就可以放心选择此项")

    # hbox:
    #     label _("直接从硬盘读取")
    #     text _("程序直接从硬盘读取素材文件，只使用必要的内存，对硬盘性能要求高，但是内存开销较小，适合低内存设备，但是若硬盘读取性能不佳时可能会发生卡顿现象")

    hbox:
        label _("音量设置")
        text _("由于原作BGM声音过大，建议将BGM音量调小，音效音量适中，以获得更好游戏体验")


screen mouse_help():

    hbox:
        label _("左键点击")
        text _("推进对话并激活界面。")

    hbox:
        label _("中键点击")
        text _("隐藏用户界面。")

    hbox:
        label _("右键点击")
        text _("访问游戏菜单。")

    hbox:
        label _("鼠标滚轮上")
        text _("回退至先前的对话。")

    hbox:
        label _("鼠标滚轮下")
        text _("向前至之后的对话。")


screen gamepad_help():

    hbox:
        label _("右扳机键\nA/底键")
        text _("推进对话并激活界面。")

    hbox:
        label _("左扳机键\n左肩键")
        text _("回退至先前的对话。")

    hbox:
        label _("右肩键")
        text _("向前至之后的对话。")


    hbox:
        label _("十字键，摇杆")
        text _("导航界面。")

    hbox:
        label _("开始，向导")
        text _("访问游戏菜单。")

    hbox:
        label _("Y/顶键")
        text _("隐藏用户界面。")

    textbutton _("校准") action GamepadCalibrate()


    # 设置帮助
    # 移至键盘部分
# screen settingHelp():

    # hbox:
    #     label _("实验选项")
    #     text _("对设置中实验选项进行说明，注意更改实验选项必须重启游戏，否则可能不会生效")

    # hbox:
    #     label _("使用软解")
    #     text _("默认选项，调用软件解码器对媒体进行解码，非常稳定但是耗费性能，对低端设备不友好")

    # hbox:
    #     label _("使用硬解")
    #     text _("调用硬件解码器对媒体进行解码，速度快且高效，前提需要设备支持（程序的媒体文件有主要有png、webm、ogg三种，请确保您的设备支持），可能会导致一些问题，如遇到视频拉伸，无法正常播放等问题，请切换会软件解码器，如果你的设备不属于低性能设备，强烈建议使用软件解码器")

    # hbox:
    #     label _("使用内存缓存")
    #     text _("默认选项，素材文件预缓存至内存再从内存调用，运行速度大幅提升，对低内存设备不友好")

    # hbox:
    #     label _("直接从硬盘读取")
    #     text _("程序直接从硬盘读取素材文件，只使用必要的内存，对硬盘性能要求高，但是内存开销较小")

    # hbox:
    #     label _("其它")
    #     text _("由于原作BGM声音过大，建议将BGM音量调小以获得更好游戏体验")

    # 豆知识
screen douKnowledge():

    hbox:
        label _("{a=https://love69renpyremasterproject.github.io/knowledge/}移动版点这里下载{/a}")
        text _("PC版请到游戏目录/extra文件夹寻找文档")



style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## 其他界面
################################################################################


## 确认界面 ########################################################################
##
## 当 Ren'Py 需要询问玩家有关确定或取消的问题时，会调用确认界面。
##
## https://www.renpy.cn/doc/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 显示此界面时，确保其他界面无法输入。
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("确定") action yes_action
                textbutton _("取消") action no_action

    ## 右键点击退出并答复“no”（取消）。
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## 快进指示界面 ######################################################################
##
## “skip_indicator”界面用于指示快进正在进行中。
##
## https://www.renpy.cn/doc/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("正在快进")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## 我们必须使用包含“BLACK RIGHT-POINTING SMALL TRIANGLE”字形的字体。
    font "DejaVuSans.ttf"


## 通知界面 ########################################################################
##
## 通知界面用于向玩家显示消息。（例如，当游戏快速保存或已截屏时。）
##
## https://www.renpy.cn/doc/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL 模式界面 ####################################################################
##
## 此界面用于 NVL 模式的对话和菜单。
##
## https://www.renpy.cn/doc/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## 在“vpgrid”或“vbox”中显示对话框。
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## 如果给定，则显示“menu”。 如果“config.narrator_menu”设置为“True”，
        ## 则“menu”可能显示不正确，如前述。
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 此语句控制一次可以显示的 NVL 模式条目的最大数量。
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## 移动设备界面
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## 由于鼠标可能不存在，我们将快捷菜单替换为更容易触摸且按钮更少更大的版本。
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            # textbutton _("回退") action Rollback()
            # textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            # textbutton _("自动") action Preference("auto-forward", "toggle")
            # textbutton _("菜单") action ShowMenu()

            # 由于存读档入口调整，调整按钮与其它平台一致
            # 旧 quick_menu 之 textbutton
            # # textbutton _("回退") action Rollback()
            # # textbutton _("历史") action ShowMenu('history')
            # textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            # textbutton _("自动") action Preference("auto-forward", "toggle")
            # textbutton _("保存") action ShowMenu("game_save")
            # textbutton _("读取") action ShowMenu("game_load")
            # textbutton _("快存") action QuickSave()
            # textbutton _("快读") action QuickLoad()
            # textbutton _("设置") action ShowMenu('preferences')

            # 新 quick_menu 之 image button
            ## 对 btn 的顺序进行微调

            # 存档
            imagebutton:
                idle "gui/quick_menu/btn_save_base.png"
                hover "gui/quick_menu/btn_save_onMouse.png"
                selected_hover "gui/quick_menu/btn_save_onClick.png"
                hover_sound "voice/effect/メニュー決定音.ogg"
                action ShowMenu("game_save")

            # 读档
            imagebutton:
                idle "gui/quick_menu/btn_load_base.png"
                hover "gui/quick_menu/btn_load_onMouse.png"
                selected_hover "gui/quick_menu/btn_load_onClick.png"
                hover_sound "voice/effect/メニュー決定音.ogg"
                action ShowMenu("game_load")

            # Q.Save
            imagebutton:
                idle "gui/quick_menu/btn_qsave_base.png"
                hover "gui/quick_menu/btn_qsave_onMouse.png"
                selected_hover "gui/quick_menu/btn_qsave_onClick.png"
                hover_sound "voice/effect/メニュー決定音.ogg"
                action QuickSave()

            # Q.Load
            imagebutton:
                idle "gui/quick_menu/btn_qload_base.png"
                hover "gui/quick_menu/btn_qload_onMouse.png"
                selected_hover "gui/quick_menu/btn_qload_onClick.png"
                hover_sound "voice/effect/メニュー決定音.ogg"
                action QuickLoad()

            # 快进
            ## 快进和自动属于要保存状态的按钮，多一个 selected_idle 特性
            imagebutton:
                idle "gui/quick_menu/btn_skip_base.png"
                hover "gui/quick_menu/btn_skip_onMouse.png"
                selected_hover "gui/quick_menu/btn_skip_onClick.png"
                selected_idle "gui/quick_menu/btn_skip_Clicked.png"
                hover_sound "voice/effect/メニュー決定音.ogg"
                action Skip() alternate Skip(fast=True, confirm=True)

            # 自动
            imagebutton:
                idle "gui/quick_menu/btn_auto_base.png"
                hover "gui/quick_menu/btn_auto_onMouse.png"
                selected_hover "gui/quick_menu/btn_auto_onClick.png"
                selected_idle "gui/quick_menu/btn_auto_Clicked.png"
                hover_sound "voice/effect/メニュー決定音.ogg"
                action Preference("auto-forward", "toggle")

            # 设置
            imagebutton:
                idle "gui/quick_menu/btn_config_base.png"
                hover "gui/quick_menu/btn_config_onMouse.png"
                selected_hover "gui/quick_menu/btn_config_onClick.png"
                hover_sound "voice/effect/メニュー決定音.ogg"
                action ShowMenu('preferences')

style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900


# 可变 BGM
## https://lemmasoft.renai.us/forums/viewtopic.php?t=51629
## https://www.renpy.cn/doc/label.html?highlight=before_main_menu
label before_main_menu:
    if persistent.one:
        $ renpy.music.play("bgm/bgm01.ogg", channel='music', loop=True)
    else:
        $ renpy.music.play("bgm/bgm08.ogg", channel='music', loop=True)
    return

# ______________________________________________________________________________________________
# Gallery (ALBUM)
screen gallery:
    tag menu
    # 在这里播放音乐会导致 main_menu 的音乐混乱，暂时没有找到好的解决方法，后面再康康
    # 解决，这个可以参照 “MusicRoom” 的用法，下面的 “replace” 就是具体写法
    # $ renpy.music.play("bgm/bgm50.ogg", channel='music', loop=True, fadeout=1.0, synchro_start=False, fadein=1.0, if_changed=False)
    add "gui/cgmode/album.png"

    hbox:
        xalign 0.5
        yalign 0.5


        grid 5 4:
            spacing 60

            add g.make_button("one", "gui/cgmode/cg/one/small/mcg01_1_1.png")

            add g.make_button("two", "gui/cgmode/cg/one/small/アイキャッチ心愛.png")

            add g.make_button("three", "gui/cgmode/cg/one/small/sdcg01a.png")

            add g.make_button("four", "gui/cgmode/cg/one/small/mcg_02_1.png")

            add g.make_button("five", "gui/cgmode/cg/one/small/sdcg04a.png")


            add g.make_button("six", "gui/cgmode/cg/one/small/ハワイa.png")

            add g.make_button("seven", "gui/cgmode/cg/one/small/ルート解禁.png")

            add g.make_button("eight", "gui/cgmode/cg/one/small/屋上_夕.png")

            add g.make_button("nine", "gui/cgmode/cg/one/small/ボウリング場.png")

            add g.make_button("ten", "gui/cgmode/cg/one/small/ccg01_1_1.png")

            add g.make_button("eleven", "gui/cgmode/cg/one/small/遊園地_商店街.png")

            add g.make_button("twelve", "gui/cgmode/cg/one/small/水着cgゲーム用.png")


            if persistent.two:
                add g.make_button("thirteen", "gui/cgmode/cg/two/small/空.png")

                add g.make_button("fourteen", "gui/cgmode/cg/two/small/天の川.png")

                add g.make_button("fifteen", "gui/cgmode/cg/two/small/繁華街_昼.png")

                add g.make_button("sixteen", "gui/cgmode/cg/two/small/歩道橋_昼.png")

                add g.make_button("seventeen", "gui/cgmode/cg/two/small/横浜_山下公園.png")

                add g.make_button("eighteen", "gui/cgmode/cg/two/small/rcg01_4_0.png")

                add g.make_button("nineteen", "gui/cgmode/cg/two/small/電柱.png")

                add g.make_button("twenty", "gui/cgmode/cg/two/small/自宅風呂場.png")

            else:
                imagebutton:
                    idle "gui/cgmode/btn_thumb.png"
                imagebutton:
                    idle "gui/cgmode/btn_thumb.png"
                imagebutton:
                    idle "gui/cgmode/btn_thumb.png"

                imagebutton:
                    idle "gui/cgmode/btn_thumb.png"
                imagebutton:
                    idle "gui/cgmode/btn_thumb.png"
                imagebutton:
                    idle "gui/cgmode/btn_thumb.png"
                imagebutton:
                    idle "gui/cgmode/btn_thumb.png"
                imagebutton:
                    idle "gui/cgmode/btn_thumb.png"

    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "gui/saveload/btn_back_base.png"
        hover "gui/saveload/btn_back_onMouse.png"
        selected_hover "gui/saveload/btn_back_onClick.png"
        action ShowMenu("main_menu_2")

    # 页面下方的提示
    vbox:
        xalign 0
        yalign 1.0
        text "By Luckykeeper: Gallery 附带了一些彩蛋，包括一些原作没有使用但是也被打包进去的素材，\n                                    以及移植版没有使用的素材，还请注意。如需获取全部CG，可参照{a=https://love69-renpy-remaster-project.github.io/Doc/dev/%E8%A7%A3%E5%8C%85.html}项目组文档站{/a}指南解包"
    # 进入退出音乐效果
    on "replace" action Play("music", "bgm/bgm50.ogg")
    on "replaced" action Play("music", "bgm/bgm01.ogg")

# ______________________________________________________________________________________________
# Replay
# 问：HS都没有，Replay 放个毛啊！
# 所以这里就提供给大伙 jump scene 的功能吧
screen replay:
    tag menu
    add "gui/replay/back.png"
    vbox:
        xalign 0.1
        yalign 0.1
        text "Scene Replay"
    hbox:
        xalign 0.5
        yalign 0.5

        grid 3 8:
            textbutton _("Scene01 序幕 我们的故事从这里开始") action Replay("scene01")
            textbutton _("Scene02 真冬&心爱线 和心爱酱约会") action Replay("scene02")
            textbutton _("Scene03 真冬&心爱线 心爱酱的夜访") action Replay("scene03")
            textbutton _("Scene04 真冬&心爱线 真冬酱的心意") action Replay("scene04")
            textbutton _("Scene05 真冬&心爱线 兄妹间的爱恋") action Replay("scene05")
            textbutton _("Scene06 真冬&心爱线 寄的莲和二人") action Replay("scene06")
            textbutton _("Scene07 真冬&心爱线 心爱酱的烦恼") action Replay("scene07")
            textbutton _("Scene08 真冬&心爱线 心爱酱再夜访") action Replay("scene08")
            textbutton _("Scene09 真冬&心爱线 从隔阂到幸终") action Replay("scene09")
            textbutton _("Scene10 真冬&心爱线 三人新的开始") action Replay("scene10")
            textbutton _("Scene11 真冬&心爱线 现在是女子会") action Replay("scene11")
            textbutton _("Scene12 真冬&心爱线 二人奇妙体验") action Replay("scene12")
            textbutton _("Scene13 真冬&心爱线 夏威夷我来啦") action Replay("scene13")
            textbutton _("Scene14 真冬&心爱线 三人心跳时刻") action Replay("scene14")
            textbutton _("Scene15 真冬&心爱线 故事还将继续") action Replay("scene15")
            if persistent.two:
                textbutton _("Scene16       里昂线       意料外的选择") action Replay("scene16")
                textbutton _("Scene17       里昂线       初合演纸芝居") action Replay("scene17")
                textbutton _("Scene18       里昂线       班主任的考验") action Replay("scene18")
                textbutton _("Scene19       里昂线       和里昂初约会") action Replay("scene19")
                textbutton _("Scene20       里昂线       考验后的幸福") action Replay("scene20")
                textbutton _("Scene21       里昂线       梦想的第一战") action Replay("scene21")
                textbutton _("Scene22       里昂线       忙碌快乐日常") action Replay("scene22")
                textbutton _("Scene Replay By Luckykeeper")
                textbutton _("Enjoy The Game!")
            else:
                textbutton _("Locked!")
                textbutton _("Locked!")
                textbutton _("Locked!")
                textbutton _("Locked!")
                textbutton _("Locked!")
                textbutton _("Locked!")
                textbutton _("Locked!")
                textbutton _("Scene Replay By Luckykeeper")
                textbutton _("Enjoy The Game!")

    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "gui/saveload/btn_back_base.png"
        hover "gui/saveload/btn_back_onMouse.png"
        selected_hover "gui/saveload/btn_back_onClick.png"
        action ShowMenu("main_menu_2")

    # 页面下方的提示
    vbox:
        xalign 0
        yalign 1.0
        text "By Luckykeeper: 因为移植版莫得 HScene ，所以给带伙做了一个回顾大场景的功能， Scene 以过场人物动画为界"

# ______________________________________________________________________________________________
# Music
screen music_room:
    tag menu
    add "gui/music_room/back.png"

    # Spriterecordings Url
    imagebutton:
        xalign 0.636
        yalign 0.725
        idle "gui/music_room/btn_site_off.png"
        hover "gui/music_room/btn_site_over.png"
        selected_hover "gui/music_room/btn_site_one.png"
        action OpenURL("http://spriterecordings.upper.jp/EmotiveBrilliance/")

    # 01_heartbeat
    imagebutton:
        xalign 0.0700899
        yalign 0.059
        idle "gui/music_room/btn_bgm01_off.png"
        hover "gui/music_room/btn_bgm01_onover.png"
        selected_idle "gui/music_room/btn_bgm01_on.png"
        action mr.Play("bgm/bgm01.ogg")

    # 01_heartbeat
    imagebutton:
        xalign 0.0700899
        yalign 0.059
        idle "gui/music_room/btn_bgm01_off.png"
        hover "gui/music_room/btn_bgm01_onover.png"
        selected_idle "gui/music_room/btn_bgm01_on.png"
        action mr.Play("bgm/bgm01.ogg")

    # 08_あの夏まで
    imagebutton:
        xalign 0.0700899
        yalign 0.2516
        idle "gui/music_room/btn_bgm02_off.png"
        hover "gui/music_room/btn_bgm02_onover.png"
        selected_idle "gui/music_room/btn_bgm02_on.png"
        action mr.Play("bgm/bgm05.ogg")

    # prominence
    imagebutton:
        xalign 0.0700899
        yalign 0.466
        idle "gui/music_room/btn_bgm03_off.png"
        hover "gui/music_room/btn_bgm03_onover.png"
        selected_idle "gui/music_room/btn_bgm03_on.png"
        action mr.Play("bgm/bgm03.ogg")

    if persistent.two:
    # 世迷い恋慕
        imagebutton:
            xalign 0.0700899
            yalign 0.675
            idle "gui/music_room/btn_bgm04_off.png"
            hover "gui/music_room/btn_bgm04_onover.png"
            selected_idle "gui/music_room/btn_bgm04_on.png"
            action mr.Play("bgm/bgm49.ogg")
    else:
        imagebutton:
            xalign 0.0700899
            yalign 0.675
            idle "gui/music_room/btn_bgm04_na.png"

    # anonatsu_piano
    imagebutton:
        xalign 0.0700899
        yalign 0.9
        idle "gui/music_room/btn_bgm05_off.png"
        hover "gui/music_room/btn_bgm05_onover.png"
        selected_idle "gui/music_room/btn_bgm05_on.png"
        action mr.Play("bgm/bgm08.ogg")

    # あの夏rock1111
    imagebutton:
        xalign 0.685
        yalign 0.063
        idle "gui/music_room/btn_bgm06_off.png"
        hover "gui/music_room/btn_bgm06_onover.png"
        selected_idle "gui/music_room/btn_bgm06_on.png"
        action mr.Play("bgm/bgm42.ogg")

    # スターチス nightcore
    imagebutton:
        xalign 0.69595
        yalign 0.2575
        idle "gui/music_room/btn_bgm07_off.png"
        hover "gui/music_room/btn_bgm07_onover.png"
        selected_idle "gui/music_room/btn_bgm07_on.png"
        action mr.Play("bgm/bgm47.ogg")

    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "gui/saveload/btn_back_base.png"
        hover "gui/saveload/btn_back_onMouse.png"
        selected_hover "gui/saveload/btn_back_onClick.png"
        action ShowMenu("main_menu_2")

    # 页面下方的提示
    vbox:
        xalign 0
        yalign 1.0
        text "By Luckykeeper:想回顾全部 BGM？请参照{a=https://love69-renpy-remaster-project.github.io/Doc/dev/%E8%A7%A3%E5%8C%85.html}项目组文档站{/a}指南进行解包~"

    # 进入退出音乐效果
    on "replace" action mr.Play()
    on "replaced" action Play("music", "bgm/bgm01.ogg")

# ______________________________________________________________________________________________
# Extra Games
screen extra_games:
    tag menu
    add "gui/extra_games/back3.png"

    # S.I.S Url
    imagebutton:
        xalign 0.1
        yalign 0.2
        idle "gui/extra_games/btn_sis.png"
        hover "gui/extra_games/btn_sis.png"
        selected_hover "gui/extra_games/btn_sis.png"
        action OpenURL("http://www.hyperiyon.com/100periyon/sistri/dl.php")

    # COW Url
    imagebutton:
        xalign 0.1
        yalign 0.77
        idle "gui/extra_games/btn_cow.png"
        hover "gui/extra_games/btn_cow.png"
        selected_hover "gui/extra_games/btn_cow.png"
        action OpenURL("http://www.hyperiyon.com/100periyon/cow/dlcode.php")

    # 页面下方的提示

    vbox:
        xalign 0
        yalign 1.0
        text "By Luckykeeper:这里原作是想让大家白嫖这两部游戏（是本作的前作），在我开始翻译本作的时候去看了一眼，\n一部放的 Google Drive 已经过期了，另一部提供的链接也下载不了了，大伙也可以去试试，想支持本作的原作\n团队也可以考虑买这两部，只要100日元（人民币6块多点儿）"

    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "gui/saveload/btn_back_base.png"
        hover "gui/saveload/btn_back_onMouse.png"
        selected_hover "gui/saveload/btn_back_onClick.png"
        action ShowMenu("main_menu_2")


# 由于修改了存读档界面，需要调整存储区变量的默认行为，这个变量要在SplashScreen之后再加载，不能 init python -1，必须使用普通的写法让它在后面加载
# https://www.renpy.cn/doc/store_variables.html?highlight=game_menu_screen#var-_game_menu_screen
init python:
    _game_menu_screen = "history"

# 自动存档功能，用 try 防止抛出错误，该错误属于 Warning ，不影响运行
# 这个 Warning 是由于 Python2 自身的一个问题导致的
# except 的内容会在控制台（Release看不到）和 Linux 版（在终端能看到）输出
    try:
        l_f_page = latest_file_str.split('-',1)[0] #所在页 #auto-1表示自动存档页第一位
        l_f_name = latest_file_str.split('-',1)[1] #槽位名
    except:
        print("Powered By Luckykeeper and LOVE69 Ren'Py Remaster Project")
        print("Luckykeeper's Blog: https://luckykeeper.site/")
        print("Offical Website: https://love69renpyremasterproject.github.io/")
        print("GitHub: https://github.com/luckykeeper/LOVE69_renpy_remaster")
        print("Gitee: https://gitee.com/luckykeeper/LOVE69_renpy_remaster")
        print("GitLab: https://gitlab.com/luckykeeper/LOVE69_renpy_remaster")
        print("你 Star 了嘛？还没的话快去到 GitHub 或者 Gitee 或者 GitLab 给我们个 Star 呗！")

    if persistent.useCache:
        # 这里指定是否使用内存的设置，设置成使用会设置最大 1G 的内存
        # 设置成不使用会设置最大 150M 的内存（比默认小，保证大部分脚本流畅运行）
        config.image_cache_size_mb = 1024
    else:
        config.image_cache_size_mb = 150


    # Gallery (ALBUM) 对象
    # Step1，创建Gallery对象
    g = Gallery()

    # Step2 创建要展示的实例
    # 一周目不考虑解锁问题，直接加上，因为之前 EXTRA 没有开放
    g.button("one") # prpr真冬

    g.image("gui/cgmode/cg/one/mcg01_1_1.png")
    g.image("gui/cgmode/cg/one/mcg01_1_2.png")
    g.image("gui/cgmode/cg/one/mcg01_1_3.png")
    g.image("gui/cgmode/cg/one/mcg01_2_1.png")
    g.image("gui/cgmode/cg/one/mcg01_2_2.png")

    g.button("two") # 过场动画

    g.image("gui/cgmode/cg/one/アイキャッチ心愛＆真冬.png")
    g.image("gui/cgmode/cg/one/アイキャッチ心愛.png")
    g.image("gui/cgmode/cg/one/アイキャッチ真冬.png")
    g.image("gui/cgmode/cg/one/アイキャッチ心愛＆真冬水着.png")
    if persistent.two:
        g.image("images/bg/アイキャッチリオン.png") # 二周目之后展示的话可以这么写

    g.button("three") # 心爱&真冬 SDCG

    g.image("gui/cgmode/cg/one/sdcg01a.png")
    g.image("gui/cgmode/cg/one/sdcg01b.png")

    g.button("four") # 真冬教室

    g.image("gui/cgmode/cg/one/mcg_02_3.png")
    g.image("gui/cgmode/cg/one/mcg_02_2.png")
    g.image("gui/cgmode/cg/one/mcg_02_1.png")

    g.button("five") # 看戏四人组

    g.image("gui/cgmode/cg/one/sdcg04a.png")
    g.image("gui/cgmode/cg/one/sdcg04b.png")
    g.image("gui/cgmode/cg/one/体験版終了.png")

    g.button("six") # Hawaii!!!

    g.image("gui/cgmode/cg/one/ハワイa.png")
    g.image("gui/cgmode/cg/one/ハワイb.png")
    g.image("gui/cgmode/cg/one/ハワイc.png")
    g.image("gui/cgmode/cg/one/ハワイd.png")
    g.image("gui/cgmode/cg/one/ハワイe.png")
    g.image("gui/cgmode/cg/one/ハワイf.png")
    g.image("gui/cgmode/cg/one/ハワイg.png")
    g.image("gui/cgmode/cg/one/ハワイh.png")

    g.button("seven") # 里昂路线解禁

    g.image("gui/cgmode/cg/one/ルート解禁.png")

    g.button("eight") # 彩蛋素材：学校屋顶

    g.image("gui/cgmode/cg/one/屋上_昼.png")
    g.image("gui/cgmode/cg/one/屋上_夕.png")
    g.image("gui/cgmode/cg/one/屋上_夜.png")

    g.button("nine") # 和心爱酱的约会场所

    g.image("gui/cgmode/cg/one/ボウリング場.png")
    g.image("gui/cgmode/cg/one/チョコレートファクトリー.png")
    g.image("gui/cgmode/cg/one/コールドストーン.png")
    g.image("gui/cgmode/cg/one/寿司屋.png")
    g.image("gui/cgmode/cg/one/ゲームセンター.png")
    g.image("gui/cgmode/cg/one/ハンズ.png")

    g.button("ten") # 心爱酱的钢琴表演

    g.image("gui/cgmode/cg/one/ccg01_1_1.png")
    g.image("gui/cgmode/cg/one/ccg01_2_1.png")
    g.image("gui/cgmode/cg/one/ccg01_2_2.png")
    g.image("gui/cgmode/cg/one/ccg01_3_2.png")
    g.image("gui/cgmode/cg/one/ccg01_4_1.png")
    g.image("gui/cgmode/cg/one/ccg01_4_2.png")

    g.button("eleven") # 遊園地

    g.image("gui/cgmode/cg/one/遊園地_商店街.png")
    g.image("gui/cgmode/cg/one/遊園地_ポップコーン.png")

    g.button("twelve") # CG 1/2

    g.image("gui/cgmode/cg/one/main_menu_1.png")
    g.image("gui/cgmode/cg/one/水着cgゲーム用.png")

    g.button("thirteen") # 空

    g.image("gui/cgmode/cg/two/空.png")
    g.image("gui/cgmode/cg/two/空_夕b.png")
    g.image("gui/cgmode/cg/two/空_夕a.png")
    g.image("gui/cgmode/cg/two/空_雨.png")

    g.button("fourteen") # 天の川

    g.image("gui/cgmode/cg/two/天の川.png")
    g.image("gui/cgmode/cg/two/月.png")

    g.button("fifteen") # 繁華街_昼

    g.image("gui/cgmode/cg/two/繁華街_昼.png")
    g.image("gui/cgmode/cg/two/繁華街_夕.png")
    g.image("gui/cgmode/cg/two/繁華街_夜.png")
    g.image("gui/cgmode/cg/two/繁華街_雨.png")
    g.image("gui/cgmode/cg/two/ロータリー_昼.png")
    g.image("gui/cgmode/cg/two/ロータリー_夜.png")

    g.button("sixteen") # 歩道橋_昼

    g.image("gui/cgmode/cg/two/歩道橋_朝.png")
    g.image("gui/cgmode/cg/two/歩道橋_昼.png")
    g.image("gui/cgmode/cg/two/歩道橋_夕.png")
    g.image("gui/cgmode/cg/two/公園_夕.png")

    g.button("seventeen") # 横浜

    g.image("gui/cgmode/cg/two/横浜_山下公園.png")
    g.image("gui/cgmode/cg/two/横浜_港の見える丘公園.png")
    g.image("gui/cgmode/cg/two/横浜_中華街.png")
    g.image("gui/cgmode/cg/two/横浜_大桟橋.png")
    g.image("gui/cgmode/cg/two/横須賀.png")
    g.image("gui/cgmode/cg/two/横浜_赤煉瓦.png")
    g.image("gui/cgmode/cg/two/横浜_カップヌードルミュージアム.png")
    g.image("gui/cgmode/cg/two/横浜_クイーンズスクエア.png")
    g.image("gui/cgmode/cg/two/横浜_山下公園_夜.png")
    g.image("gui/cgmode/cg/two/横浜_観覧車.png")
    g.image("gui/cgmode/cg/two/横浜_観覧車2.png")

    g.button("eighteen") # rcg

    g.image("gui/cgmode/cg/two/rcg01_4_0.png")
    g.image("gui/cgmode/cg/two/rcg01_4_1.png")
    g.image("gui/cgmode/cg/two/rcg01t_4_1.png")
    g.image("gui/cgmode/cg/two/rcg01t_4_2.png")
    g.image("gui/cgmode/cg/two/rcg01t_1_1.png")
    g.image("gui/cgmode/cg/two/rcg01t_1_2.png")
    g.image("gui/cgmode/cg/two/rcg01t_2_1.png")
    g.image("gui/cgmode/cg/two/rcg01_4_2.png")
    g.image("gui/cgmode/cg/two/rcg01_5_2.png")

    g.button("nineteen") # 電柱

    g.image("gui/cgmode/cg/two/電柱.png")
    g.image("gui/cgmode/cg/two/鉄塔.png")

    g.button("twenty") # 自宅風呂場

    g.image("gui/cgmode/cg/two/自宅風呂場.png")
    g.image("gui/cgmode/cg/two/自宅洗面所_昼.png")
    g.image("gui/cgmode/cg/two/自宅洗面所_夕.png")
    g.image("gui/cgmode/cg/two/自宅洗面所_夜.png")

    # 用于图像切换使用的转场(transition)
    g.transition = dissolve

    # MusicRoom 实例
    # Step1，创建一个 MusicRoom 实例。
    mr = MusicRoom(fadeout=1.0)

    # Step2. 添加音乐文件。
    mr.add("bgm/bgm01.ogg") # 01_heartbeat
    mr.add("bgm/bgm05.ogg") # 08_あの夏まで
    mr.add("bgm/bgm03.ogg", always_unlocked=True) # prominence
    if persistent.two:
        mr.add("bgm/bgm49.ogg", always_unlocked=True) # 世迷い恋慕
    else:
        mr.add("bgm/bgm49.ogg")
    mr.add("bgm/bgm08.ogg") # anonatsu_piano
    mr.add("bgm/bgm42.ogg") # あの夏rock1111
    mr.add("bgm/bgm47.ogg") # スターチス nightcore

# 测试：鼠标滚轮向下开启新对话
# init python:
    if persistent.mouseScroll:
        config.keymap['dismiss'].append('mousedown_5')
    else:
        try:
            config.keymap['dismiss'].remove('mousedown_5')
        except:
            print("没有开启鼠标滚轮向下开启新对话功能")

# --------------------------------
# LOVE69_Renpy_Remaster_Project
# GUI自定义脚本
# Author:Luckykeeper
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年3月31日
# 版本号 0.8 "LuckyDev"


## 基础 ##########################################################################

## 用户可读的游戏名称。此命令用来设置默认窗口标题，并且会在界面和错误报告中出
## 现。
##
## 带有 _() 的字符串表示其可被翻译。

# sence01 完成之后会做一个demo来验证可行性，下面是 demo 的暂定标题
# Demo版的版本名为 "LuckyGal"
# 开发版的版本名为 "LuckyDev"
# 一二周目做完之后的发行版的的版本名为 "LuckyCocoa"
define config.name = _("LOVEPOTION SIXTYNINE 汉化移植版 内部测试版 ver0.8 “LuckyDev” ，由 Luckykeeper 和 LOVE69 Ren'py Remaster Project 倾情奉献")


## 决定上面给出的标题是否显示在标题界面屏幕。设置为 False 来隐藏标题。

define gui.show_name = False


## 游戏版本号。

define config.version = "0.8"

## 放置在游戏“关于”屏幕的文本。将文本放在三个引号之间，并在段落之间留一个空行。

# Demo 版的说明
define gui.about = _p("""
LOVEPOTION SIXTYNINE 汉化移植版 内部测试版 ver0.8 “LuckyDev” ，由 Luckykeeper 和 LOVE69 Ren'py Remaster Project 倾情奉献

点击蓝字后将调用系统默认浏览器打开指定网页

项目开源页面：{a=https://github.com/luckykeeper/LOVE69_renpy_remaster}https://github.com/luckykeeper/LOVE69_renpy_remaster{/a}

项目组官网：{a=https://github.com/luckykeeper/LOVE69_renpy_remaster}https://love69renpyremasterproject.github.io/{/a}

项目组文档站（gh-pages）：{a=https://love69-renpy-remaster-project.github.io/Doc/}https://love69-renpy-remaster-project.github.io/Doc/{/a}

项目组文档站（国内镜像站）：{a=https://love69doc.luckykeeper.site:44443/Doc/}https://love69doc.luckykeeper.site:44443/Doc/{/a}

希望各位看官老爷到我们的项目页面给我们一个Star，秋梨膏，你们的Star是我做下去的动力！Star摩多摩多，动力摩多摩多！

当前版本制作成员

组长：Luckykeeper

程序：Luckykeeper

翻译：Luckykeeper

美工：Luckykeeper

校对：Luckykeeper

测试/润色：Luckykeeper，WorldlineChanger，Santa-Weaves

项目组网站构建、维护：Luckykeeper

Demo 版小感言

Luckykeeper：今天是项目开始的第42天，没想到能这么快从完全0基础到现在的地步呢，我从这个项目里面学到了非常多的东西，也感谢陪伴我一起做Demo版的WorldlineChanger和Santa-Weaves，虽然你们做的不多，但是没有你们的参与，大家也看不到现在的这个东西。总之，期待和各位在正式版再度见面！

WorldlineChanger：从八月的L决定启动项目，到十月份Demo版本的测试放出，可谓是用爱发电行为其高效性的又一次有力证明！也正是这个项目，让我接触到了这个相对冷门但十分有趣的GAL，我也相信会有更多人会因为它而感受到游戏的乐趣和开源共享精神的珍贵。
在Demo制作期间由于学业繁忙等鸽子原因，没有帮上很多忙:P 但我们的时间还有很多，在正式版的推进过程里，希望能有足够时间来一起修缮这个大工程~
关于游戏，无论是舒服的CV表现还是颇具新意的剧情推进风格，都能令人感受到一种与GAL经典流程不同的尝试，在Demo结尾附近心爱夺取冰淇淋时的演出更是令人印象深刻> <。 此外，得益于L君堪称细致入微的豆科普时间，让love69更像是个梗百科科普全书了（2333 那么，正式版与各位的再次相遇，敬请期待吧！

Santa-Weaves：很荣幸能参加进项目里，希望Luckykeeper能把这份热爱继续下去，越做越好！
""")


## 在生成的发布版中，可执行文件和目录所使用的短名称。此处必须是仅 ASCII 字符，并
## 且不得包含空格、冒号和分号。

define build.name = "LOVE69RenPyRemasterProject"


## 音效和音乐 #######################################################################

## 这三个变量控制默认显示给用户的混音器。任一设置为 False 将隐藏对应的混音器。

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## 允许用户在音效或语音轨道上播放测试音频文件，将以下语句取消注释并设置样音就可
## 以使用。

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"
# 这个写到gui了


## 将以下语句取消注释就可以设置标题界面播放的背景音乐文件。此文件将在整个游戏中
## 持续播放，直至音乐停止或其他文件开始播放。

# 可变主菜单 BGM ，详见 gui.rpy 开头和 scene15 结尾
# https://lemmasoft.renai.us/forums/viewtopic.php?t=51629
# define config.main_menu_music = main_menu_music

## 转场 ##########################################################################
##
## 这些变量用来控制某些事件发生时的转场。每一个变量都应设置成一个转场，或者是
## None 来表示无转场。

## 进入或退出游戏菜单。

define config.enter_transition = dissolve
define config.exit_transition = dissolve

## 各小头像之间的转场
# define config.side_image_same_transform = dissolve
# define config.side_image_change_transform =  dissolve

## 各个游戏菜单之间的转场。

define config.intra_transition = dissolve


## 载入游戏后使用的转场。

define config.after_load_transition = dissolve


## 在游戏结束之后进入主菜单时使用的转场。

define config.end_game_transition = dissolve


## 用于控制在游戏开始标签不存在时转场的变量。作为替代，在显示初始化场景后使用
## with 声明。


## 窗口管理 ########################################################################
##
## 此命令控制对话框窗口何时显示。如果是“show”，对话框将永远显示。如果是“hide”，
## 仅在存在对话时显示。如果是“auto”，对话框会在 scene 声明前隐藏，并在有新对话时
## 重新显示。
##
## 在游戏开始后，此变量可通过“window show”、“window hide”和“window auto”声明来改
## 变。

define config.window = "auto"


## 用于显示和隐藏对话框窗口的转场

define config.window_show_transition = Dissolve(.5)
define config.window_hide_transition = Dissolve(.5)


## 默认设置 ########################################################################

## 控制默认的文字显示速度。默认的 0 是瞬间，而其他数字则是每秒显示出的字符数。

default preferences.text_cps = 25


## 默认的自动前进延迟。越大的数字会产生越长的等待，有效范围为 0 - 30。

default preferences.afm_time = 15


## 存档目录 ########################################################################
##
## 控制 Ren'Py 为此游戏放置存档的，基于平台的特定目录。存档文件将放置在：
##
## Windows：%APPDATA%\RenPy\<config.save_directory>
##
## Macintosh：$HOME/Library/RenPy/<config.save_directory>
##
## Linux：$HOME/.renpy/<config.save_directory>
##
## 该命令一般不应变更，若要变更，应为有效字符串而不是表达式。

# 正式发行版存档文件夹
# define config.save_directory = "LOVE69RenpyRemaster-Release-ver1.0-SaveData"

# 开发版存档文件夹
define config.save_directory = "LOVE69RenpyRemaster-Dev-SaveData"

# Demo 版存档文件夹
# define config.save_directory = "LOVE69RenpyRemaster"


## 图标 ##########################################################################
##
## 在任务栏或 Dock 上显示的图标。
# ren'py给的默认图像的是png格式，使用ico问题也莫得问题
# LOVE69_renpy_remaster 的ico文件来自love69.exe解包（内含4个ico，取最大的1.ico，并重命名为gui/window_icon.ico）

define config.window_icon = "gui/window_icon.ico"

## 生成配置 ########################################################################
##
## 这部分控制 Ren'Py 如何将您的工程转变为发行版文件。

init python:

    ## 以下功能为指定文件模式。文件模式大小写不敏感，且匹配基础目录相关的路径，
    ## 包括或不包括 /。如果多个文件模式匹配，将执行第一个。
    ##
    ## 在一个文件模式中：
    ##
    ## / 是目录分隔符。
    ##
    ## * 匹配所有字符，目录分隔符除外。
    ##
    ## ** 匹配所有字符，包括目录分隔符。
    ##
    ## 例如，“*.txt”匹配基础目录中所有的 txt 文件，“game/**.ogg”匹配所有的游戏目
    ## 录或子目录中的 ogg 文件，“**.psd”匹配工程中任何位置的 psd 文件。

    ## 将文件列为 None 来使其从已生成的分发版中排除。

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## 若要打包文件，需将其列为“archive”。

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    # 将数据打包起来
    ## 脚本
    build.classify("game/scripts/**", "scripts")
    build.archive("scripts", "all")

    ## 图像
    build.classify("game/images/**", "images")
    build.archive("images", "all")
    ## 音频
    build.classify("game/bgm/**", "bgm")
    build.classify("game/voice/**", "voice")
    build.archive("bgm", "all")
    build.archive("voice", "all")
    ## 视频
    build.classify("game/video/**", "video")
    build.archive("video", "all")
    ## GUI
    build.classify("game/gui/**", "gui")
    build.archive("gui", "all")
    # 字体
    build.classify('game/**.ttf', 'font')
    build.classify('game/**.otf', 'font')
    build.archive("font", "all")

    ## 匹配为文档模式的文件会在 Mac 应用生成中重复出现，所以它们同时出现在 app
    ## 和 zip 文件中。

    build.documentation('*.html')
    build.documentation('*.txt')


## 需要一个 Google Play 授权密钥来下载扩展文件并执行应用内购。授权密钥可以在
## Google Play 开发者控制台的“服务和 API”页面找到。

# define build.google_play_key = "..."


## 与 itch.io 工程关联的用户名和工程名，以斜杠分隔。

# define build.itch_project = "renpytom/test-project"

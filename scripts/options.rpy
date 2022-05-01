# --------------------------------
# LOVE69_Renpy_Remaster_Project
# GUI自定义脚本
# Author:Luckykeeper
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年5月1日
# 版本 NightBuild "LuckyDev"


## 基础 ##########################################################################

## 用户可读的游戏名称。此命令用来设置默认窗口标题，并且会在界面和错误报告中出
## 现。
##
## 带有 _() 的字符串表示其可被翻译。

# sence01 完成之后会做一个demo来验证可行性，下面是 demo 的暂定标题
# Demo版的版本名为 "LuckyGal"
# 开发版的版本名为 "LuckyDev"
# 一二周目做完之后的发行版的的版本名为 "LuckyCocoa"
define config.name = _("LOVEPOTION SIXTYNINE 汉化移植版 NightBuild “LuckyDev” ，由 Luckykeeper 和 LOVE69 Ren'py Remaster Project 倾情奉献 (Build 20220428)")


## 决定上面给出的标题是否显示在标题界面屏幕。设置为 False 来隐藏标题。

define gui.show_name = False


## 游戏版本号。

define config.version = "1.0"

## 放置在游戏“关于”屏幕的文本。将文本放在三个引号之间，并在段落之间留一个空行。

# 1.0正式版的说明
define gui.about = _p("""
LOVEPOTION SIXTYNINE 汉化移植版 NightBuild “LuckyDev” ，由 Luckykeeper 和 LOVE69 Ren'py Remaster Project 倾情奉献 (Build 20220428)

此版本是夜间构建版，由计算机自动发起构建，未经严格测试

仅供学习 Ren'Py 使用，请不要用于其它用途！项目代码和程序完全开源、免费！

点击蓝字后将调用系统默认浏览器打开指定网页，能访问的情况下请尽量不要使用镜像站

项目开源页面（Github）：{a=https://github.com/luckykeeper/LOVE69_renpy_remaster}https://github.com/luckykeeper/LOVE69_renpy_remaster{/a}

项目开源页面（Gitee）：{a=https://gitee.com/luckykeeper/LOVE69_renpy_remaster}https://gitee.com/luckykeeper/LOVE69_renpy_remaster{/a}

项目开源页面（GitLab）：{a=https://gitlab.com/luckykeeper/LOVE69_renpy_remaster}https://gitlab.com/luckykeeper/LOVE69_renpy_remaster{/a}

项目组官网：{a=https://github.com/luckykeeper/LOVE69_renpy_remaster}https://love69renpyremasterproject.github.io/{/a}

项目组官网（国内镜像站）：{a=https://love69.luckykeeper.site:44443/}https://love69.luckykeeper.site:44443/{/a}

项目组文档站（gh-pages）：{a=https://love69-renpy-remaster-project.github.io/Doc/}https://love69-renpy-remaster-project.github.io/Doc/{/a}

项目组文档站（国内镜像站）：{a=https://love69doc.luckykeeper.site:44443/Doc/}https://love69doc.luckykeeper.site:44443/Doc/{/a}

小游戏（移动版适配，请使用现代浏览器打开）：{a=https://eatcocoa.luckykeeper.site:44443/}https://eatcocoa.luckykeeper.site:44443/{/a}

希望各位到我们的{a=https://github.com/luckykeeper/LOVE69_renpy_remaster}项目页面{/a}给我们一个Star，秋梨膏，你们的Star对我们非常重要！

问题/Bug 反馈、技术交流请前往 {a=https://github.com/luckykeeper/LOVE69_renpy_remaster}GitHub{/a}

当前版本制作成员

{a=https://github.com/luckykeeper}Luckykeeper{/a}：组长、程序、翻译、美工、校对、测试、润色、素材增分辨率、项目组网站构建/维护

{a=https://github.com/WorldlineChanger}WorldlineChanger{/a}：测试/润色、OP翻译、OP字幕制作、OP视频压制/增分辨率、staff动画优化

{a=https://github.com/Santa-Weaves}Santa-Weaves{/a}：测试/润色、OP翻译

正式版感言

Luckykeeper：终于，在项目开始第243天，克服无数困难，在项目组成员的共同努力下，我们交出了让自己满意的答卷，仅主项目就写了6万多行，
不由得感叹这段时间的成果！谨以此作献给各位参与过汉化的前辈们，也希望能够通过本作推广简单好用的 Ren'Py ，希望激发更多的人参与到汉化移植中来，后面我还会去不断完善文档站的内容，
希望能够帮助正在学习 Ren'Py 的你。最后，希望本作能在这个特殊的时期给你带来一些欢乐，让我们一起共克时艰，战胜疫情！\n
顺带一提，再过几个月的秋招我就要去找工作准备成为社畜了，所以特别希望你能给我的项目一个 Star! 这将给我以极大的帮助，要是能内推一下我就更好了（笑）\n
另外，不来康康我的其它开源项目嘛？\n
{a=https://github.com/luckykeeper/attackMap}attackMap{/a} 可以自建的酷炫网络攻击地图，支持 docker 部署\n
{a=https://github.com/luckykeeper/docker_plumemo}docker_plumemo{/a} plumemo博客容器镜像，效果参考{a=https://luckykeeper.site/}我的个人博客{/a}\n
{a=https://github.com/luckykeeper/CocoaPush}CocoaPush{/a} 心爱酱钉钉消息推送机器人，让可爱的心爱酱帮你照看各个设备的运行状态

另外虽然W酱平时挺鸽的，但是鸽子回笼的时候雀食非常顶捏，在测试的最后几天真是辛苦了捏，肝了不少东西出来，W酱，我的超人~

WorldlineChanger：项目的正式版本终于上线啦~在着手项目的文本优化工作后更是能感受到L在这期间投入的时间成本和大量精力，欢迎大家给这个小小项目点一个Star，就是对我们最棒的支持！\n
感谢开发商Steroider的倾情奉献以及cittan*的优秀音乐，本作几乎通篇玩梗，翻译中也尽可能地为其做出了解释，也许这种特色对能够理解的你来说能够享受其中。\n
不能习惯也没有关系~这里还有着不少值得一玩的闪光点待你发现。本作的BGM相较于大部分GAL来说创新感十足，欧美Trance电子音乐的旋律十分带感，同时无论是CV的功底还是游戏内的演出效果都处于较高的水准，很多时候都能够令人会心一笑，希望屏幕前的你能够喜欢！\n
也欢迎到{a=https://luckykeeper.site/}L的博客{/a}和{a=https://air.moe/}W的小站{/a}逛一逛哦\n
Enjoy :)

Santa-Weaves：其实没帮上太大的忙，一周目也没走完，不过就玩过的地方来看还没有发现bug移植的很完美！

另外，本作的完成离不开下列开源项目的帮助，感谢各位大佬的项目！这些项目是

{a=https://github.com/hanmin0822/MisakaTranslator}MisakaTranslator{/a} 提供的文本 HOOK 工具

{a=https://github.com/AaronFeng753/Waifu2x-Extension-GUI}Waifu2x-Extension-GUI{/a} 提供的素材升分辨率工具

{a=https://github.com/huanghaozi/AutoMatting}AutoMatting{/a} 提供的自动抠图工具

{a=https://github.com/nagadomi/waifu2x}waifu2x{/a} 提供的OP扩分辨率工具

{a=https://github.com/nihui/rife-ncnn-vulkan}rife-ncnn-vulkan{/a} 提供的OP补帧工具

{a=https://github.com/renpy/renpy}renpy{/a} 本作的游戏引擎

同时，也要感谢以下工具，大大提升了我们的制作效率

{a=https://code.visualstudio.com/}Visual Studio Code{/a} 提供的简洁好用的 IDE 工具

{a=https://www.tabnine.com/}tabnine{/a} 提供的 AI 代码补全工具

最后，感谢大家选择了我们项目组的汉化移植版本！祝大家游玩愉快！

本作基于 Ren'Py 7.4.6 制作，关于引擎涉及到的相关软件的许可证情况，请{a=https://www.renpy.org/doc/html/license.html}点击这里查看{/a}
""")
# ------------------------ 我是分割线，下面是考古内容 ------------------------

# Demo 版小感言

# Luckykeeper：今天是项目开始的第42天，没想到能这么快从完全0基础到现在的地步呢，我从这个项目里面学到了非常多的东西，也感谢陪伴我一起做Demo版的WorldlineChanger和Santa-Weaves，虽然你们做的不多，但是没有你们的参与，大家也看不到现在的这个东西。总之，期待和各位在正式版再度见面！

# WorldlineChanger：从八月的L决定启动项目，到十月份Demo版本的测试放出，可谓是用爱发电行为其高效性的又一次有力证明！也正是这个项目，让我接触到了这个相对冷门但十分有趣的GAL，我也相信会有更多人会因为它而感受到游戏的乐趣和开源共享精神的珍贵。
# 在Demo制作期间由于学业繁忙等鸽子原因，没有帮上很多忙:P 但我们的时间还有很多，在正式版的推进过程里，希望能有足够时间来一起修缮这个大工程~
# 关于游戏，无论是舒服的CV表现还是颇具新意的剧情推进风格，都能令人感受到一种与GAL经典流程不同的尝试，在Demo结尾附近心爱夺取冰淇淋时的演出更是令人印象深刻> <。 此外，得益于L君堪称细致入微的豆科普时间，让love69更像是个梗百科科普全书了（2333 那么，正式版与各位的再次相遇，敬请期待吧！

# Santa-Weaves：很荣幸能参加进项目里，希望Luckykeeper能把这份热爱继续下去，越做越好！

# ------------------------ 我是分割线，上面是考古内容 ------------------------

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
define config.save_directory = "LOVE69RenpyRemaster-Release-ver1.0-SaveData"

# 开发版存档文件夹
# define config.save_directory = "LOVE69RenpyRemaster-Dev-SaveData"

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

    # Test: cache tl
    build.classify('game/cache/**', 'sys')
    build.classify('game/tl/**', 'sys')
    build.archive("sys", "all")

    ## 匹配为文档模式的文件会在 Mac 应用生成中重复出现，所以它们同时出现在 app
    ## 和 zip 文件中。

    build.documentation('*.html')
    build.documentation('*.txt')
    build.documentation('*.pdf')
    build.documentation('*.md')


## 需要一个 Google Play 授权密钥来下载扩展文件并执行应用内购。授权密钥可以在
## Google Play 开发者控制台的“服务和 API”页面找到。

# define build.google_play_key = "..."


## 与 itch.io 工程关联的用户名和工程名，以斜杠分隔。

# define build.itch_project = "renpytom/test-project"

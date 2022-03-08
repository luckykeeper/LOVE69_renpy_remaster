# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene15 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：
# 版本 0.5 "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年3月8日

#   本脚本为一周目的最后一幕，从Scene16开始就是二周目内容了

# 当前流程：编写脚本AIO Process

label scene15:
    # scene15 开始

    # scene15 场景1 【一周目_尾声】 开始

    # 地点：教室
    # 人物：心爱 真冬 莲
    # BGM：あの夏まで...

    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)
    image bg ハワイg = "images/bg/ハワイg.png"
    scene 教室_昼 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)
    play music bgmfive fadein 2.0

    # 显示 quick_menu
    $ quick_menu = True

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「夏休みが…終わった…」
    show 心愛_制服_基本_ぶわー at love69_right with dissolve
    voice "voice/心愛/cca_a1_1851.ogg"
    ai 心愛_制服_基本_ぶわー "暑假…结束了…"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「…うん」
    show 真冬_制服_基本_ジト目 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1496.ogg"
    dong 真冬_制服_基本_ジト目 "…嗯"

    # 莲 「何絶望した顔してんだよ」
    lian "为啥摆出这么绝望的表情啊"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「あーあ…始まっちまったか…クソみてぇに反吐がでるぜ…」
    show 想瑠_スーツ_本気 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0229.ogg"
    liu 想瑠_スーツ_本気 "啊——啊…开始了吗……真〇〇的恶心……！"

    # 莲 「あんたは気合い入れろ！」
    lian "你要鼓起干劲啊喂！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「歯ァ食いしばれ－！」
    show 心愛_制服_基本_ニタァ at love69_right with dissolve
    voice "voice/心愛/cca_a1_1852.ogg"
    ai 心愛_制服_基本_ニタァ "咬紧牙关吧——！"
    hide 心愛_制服_基本_ぶわー

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ぐわぁー！」
    show 想瑠_スーツ_驚き at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0230.ogg"
    liu 想瑠_スーツ_驚き "嘎——！"
    hide 想瑠_スーツ_本気

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「もういっちょ！」
    show 真冬_制服_基本_ニタァ at love69_left with dissolve
    voice "voice/真冬/maf_a1_1497.ogg"
    dong 真冬_制服_基本_ニタァ "再来一次！"
    hide 真冬_制服_基本_ジト目

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ぐぇー！！」
    show 想瑠_スーツ_ぶわ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0231.ogg"
    liu 想瑠_スーツ_ぶわ "呜欸——！！"
    hide 想瑠_スーツ_驚き

    # 想瑠 「し、しどいわ…愛する教え子に始業そうそう袋だたきなんて…」
    show 想瑠_スーツ_悲しみ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0232.ogg"
    liu 想瑠_スーツ_悲しみ "真、真讨厌……被亲爱的学生在刚开学就开始围攻……"
    hide 想瑠_スーツ_ぶわ

    # nil 「心愛と真冬と過ごす、蜜月のような夏休みが終わり、俺達は今では婚約者同士として、いつもの学園にやってきていた。」
    "和心爱和真冬一起度过的蜜月般的暑假结束了，我们现在作为未婚夫妻，来到了往常的学园"

    # nil 「変わらない教室。変わっていく関係。」
    "不变的教室。逐渐改变的关系"

    # nil 「いつも見ている世界だったのに、今では、何もかもが違って見える。」
    "明明是一直在看着的世界，现在却什么都看起来不一样"

    # nil 「こうして、世界は少しずつ変わっていく。」
    "就这样，世界一点点地变化着"

    # nil 「でも、変わらない物だってある。」
    "但是，也有不变的东西"

    # nil 「心愛と真冬が選んでくれた、俺への婚約指輪を見つめた。」
    "凝视着心爱和真冬为我挑选的订婚戒指"

    # nil 「変わらず、俺の前の席に隣同士で並んで座る、二人の恋人を眺めながら、俺は物思いに耽っていた。」
    "还是一如既往地坐在我前面的座位，望着两个恋人，我陷入了沉思"

    # 莲 「なぁ…心愛、真冬」
    lian "那个……心爱，真冬"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 心爱&真冬 「『はーい♪』」
    show 真冬_制服_基本_微笑み at love69_left
    show 心愛_制服_基本_笑顔 at love69_right
    with dissolve
    voice "voice/真冬/maf_a1_1498.ogg"
    ai_dong "『嗯——♪』"
    hide 真冬_制服_基本_ニタァ
    hide 心愛_制服_基本_ニタァ

    # nil 「二人は同時に俺の方へ振り向いた。」
    "两个人同时向我回头"

    # 莲 「愛してるよ」
    lian "我爱你们"

    # 心爱&真冬 「『私も、愛してる♪』」
    show 真冬_制服_基本_にっこり_1 at love69_left
    show 心愛_制服_基本_にっこり1 at love69_right
    with dissolve
    voice "voice/真冬/maf_a1_1499.ogg"
    ai_dong "『我也是，爱你♪』"
    hide 真冬_制服_基本_微笑み
    hide 心愛_制服_基本_笑顔

    # nil 「二人はにっこりと笑顔で、即答してくれた。」
    "两个人微笑着马上回答了"

    # nil 「教室は生徒が沢山いるし、みんなに見られてるけど、キスしたくなった。」
    "教室里有很多学生，虽然大家都在看，但是我想吻她们"

    # nil 「それは、二人も同じだったようだ。」
    "看来，她们两个人也一样"

    # 这里的少了小头像，就不加了
    # 心爱&真冬 「『…だーいすき。ちゅっ♪』」
    # voice "voice/心愛/cca_a1_1854.ogg"
    # voice "voice/真冬/maf_a1_1500.ogg"
    voice "voice/その他/ex1_a1_0001.ogg"
    ai_dong 真冬_制服_基本_にっこり_1 "『最喜欢了，啾♪』"

    # nil 「二人はこっそり、俺の唇に唇を合せた」
    "两个人悄悄地把嘴唇合在了我的唇上"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「バカップルが居るぞ－！」
    show 想瑠_スーツ_ニヤリ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0233.ogg"
    liu 想瑠_スーツ_ニヤリ "笨蛋CP在这里哦——！"
    hide 想瑠_スーツ_悲しみ

    # 女子学生A 「ころせー！」
    voice "voice/その他/ot1_a1_0006.ogg"
    wsa "杀了他们——！"

    # 女子学生B 「脚をおっちまえ！」
    # 记得加人物表
    voice "voice/その他/足折る.ogg"
    wsb "把你的腿拿开！"

    # 莲 「やれやれ、落ち着いてキスもできねぇな」
    lian "哎呀哎呀，完全不能冷静下来Kiss啊"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「上等！　どっからでもかってきやがれ！」
    show 心愛_制服_基本_もぐもぐ at love69_right with dissolve
    voice "voice/心愛/cca_a1_1855.ogg"
    ai 心愛_制服_基本_もぐもぐ "来吧！随便去哪儿都行！"
    hide 心愛_制服_基本_にっこり1

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まぁいでしょう。たまには二人のお遊びに付き合ってあげます」
    show 真冬_制服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_1500.ogg"
    dong 真冬_制服_基本_目閉じ "嘛，也好了，偶尔陪你们两个玩玩"
    hide 真冬_制服_基本_にっこり_1

    # 三人 「『Rock you！！！』」
    # 人物表+++
    hide 真冬_制服_基本_目閉じ
    show 真冬_制服_中指_見下し_1 at love69_left
    show 心愛_制服_基本_ニタァ at love69_right
    with dissolve
    voice "voice/真冬/maf_a1_1501.ogg"
    lianaidong 真冬_制服_中指_見下し_1 "『Rock you！！！』"
    hide 心愛_制服_基本_もぐもぐ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぶえ…」
    show 心愛_制服_基本_ぶわー at love69_right with dissolve
    voice "voice/心愛/cca_a1_1857.ogg"
    ai 心愛_制服_基本_ぶわー "呜欸……"
    hide 心愛_制服_基本_ニタァ

    # 莲 「いや、ほんとすんませんでした」
    lian "那个，真的对不起"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「はい…気をつけます…」
    hide 真冬_制服_中指_見下し_1
    show 真冬_制服_基本_泣き at love69_left
    with dissolve
    voice "voice/真冬/maf_a1_1502.ogg"
    dong 真冬_制服_基本_泣き "好吧…我会注意的…"

    # 画面淡入蓝天
    scene 空 at love69_bg1440 with Dissolve(2.0)

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「あ、そうだ、転校生いるんだった忘れてた。紹介しよう、遥か遠くイギリスから直輸入！リオン＝マクスウェルちゃんでぇす！」
    # L:本作统一不使用日式写法，即リオン＝マクスウェルちゃん，而是按中式写法，即里昂·麦克斯韦
    voice "voice/想瑠/sol_a1_0234.ogg"
    liu 想瑠_スーツ_見下し "啊，对了，我忘记有转校生了。我来介绍一下，从遥远的英国直接进口！里昂·麦克斯韦酱的说！"

    # nil 「ガラガラッ」
    "嘎啦嘎啦"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「また会えたね、みんな」
    voice "voice/リオン/ron_a1_1105.ogg"
    lion リオン_私服_基本_にっこり "欸嘿，又见面了呢，大家"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱&真冬 「『わーい！』」
    # 改下名字
    voice "voice/真冬/maf_a1_1503.ogg"
    play xinaiab "voice/心愛/cca_a1_1858.ogg"
    dong_ai 心愛_制服_基本_にっこり1 "『哇——咿！』"

    # scene15 场景1 【一周目_尾声】 结束！

    # 一周目结局 【你们都是我的翅膀】达成！二周目内容开放！

    # Scene15 结束！！！

    # 一周目内容，结束！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！

    # 过场：（提示：在物语的序章，新的选择肢出现了！）
    image bg ルート解禁 = "images/bg/ルート解禁.png"
    scene ルート解禁 with dissolve

    # 一周目完成，设置一周目变量为已经完成
    $ persistent.one = True
    $ persistent.playthrough == 1
    $ check_playthrough()

    $ renpy.pause(3.0, hard=True)

    # return before_main_menu

    # # 变换 BGM
    # $ checkFile = open('one.luckykeeper')
    # $ checkFileStr = checkFile.read()
    # if 'This File is Automatically Created By Luckykeeper because you have playthrough one end!' in checkFileStr:
    #     $ print "恭喜你已经完成一周目内容!"
    #     $ main_menu_music = "bgm/bgm01.ogg"
    # else:
    #     $ print "一周目完成状态:False"
    #     $ main_menu_music = "bgm/bgm08.ogg"



    # 一周目结束之后的变化
    #   开场BGM变为OP
    #   EXTRA开放（先不做）
    #   WEBSITE这个可以考虑实现一下
    #   好像没其它的了

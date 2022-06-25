# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene07 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：
# 版本 NightBuild "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年6月25日

# 当前流程：All Done!

label scene07:
    $ renpy.notify("BGM:jonay_-_want_you_to_know")
    # scene07 开始

    # scene07 场景1 【心爱酱的烦恼与时隔许久的演奏】 开始
    # 可变标题
    # Scene 序号
    $ sceneNo =  " scene07"
    # 存档名称和 Scene 大标题
    $ sceneName = " 真冬&心爱线 心爱酱的烦恼"
    # 小场景的名称
    $ partName = " 【心爱酱的烦恼与时隔许久的演奏】"
    $ changeTitleName()
    
    # 地点：雾叶店内
    # 人物：心爱 店长（雾叶） 莲
    # BGM：雾叶店内的音乐（嘤语的）

    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)
    scene 霧葉ちゃんのお店 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)

    # 显示 quick_menu
    $ quick_menu = True

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ごく……ごく……ごく……」
    # 没有跳过
    show 心愛_制服_基本_もぐもぐ at love69_right with dissolve
    voice "voice/心愛/cca_a1_0721.ogg"
    ai 心愛_制服_基本_もぐもぐ "唔……咕…咕……"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 定义雾叶在左的参数
    transform love69_wuye_left:
        zoom 1.5
        xalign 0.11
        yalign 0.015

    # 店长 「ぷっ…くすくすくす…」
    # 56-115 跳过
    show 店长_私服_不満_1 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0116.ogg"
    dinerowner 店长_私服_不満_1 "咳…哈哈哈~"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ごく…ごく…ぷはー」
    voice "voice/心愛/cca_a1_0722.ogg"
    ai 心愛_制服_基本_もぐもぐ "咕…咕……哇啊"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「くすくすくすくす…」
    voice "voice/霧葉/krh_a1_0117.ogg"
    dinerowner 店长_私服_不満_1 "嘿嘿…啊哈哈~"

    # nil 「激しい雨音が、窓の向こうから聞こえてくる。」
    "从窗外传来了猛烈的雨声"

    # nil 「夏は嫌いじゃないけど、やたら身体の先端だけを刺してくるモスキート野郎と、」
    "虽然不讨厌夏天，但是我不喜欢蚊子，这些混蛋总是用身体的尖端刺伤我的皮肤"

    # nil 「憲法９条ガン無視してゲリラ戦を挑んでくるこの豪雨だけは好きになれない。」
    # 参考资料：https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E5%9B%BD%E6%86%B2%E6%B3%95%E7%AC%AC9%E6%9D%A1
    # "我不喜欢这场无视宪法第九条挑起游击战的暴雨（L:日本宪法第二章第九条放弃了交战权，原文「日本国民衷心谋求基于正义与秩序的国际和平，永远放弃以国权发动战争、武力威胁或武力行使，作为解决国际争端的手段。为达到前项目的，不保持陆海空军及其他战争力量，不承认国家的交战权」）"
    if persistent.luckykeeperSay == "shutup":
        "我不喜欢这场无视宪法第九条挑起游击战的暴雨"
    else:
        "我不喜欢这场无视宪法第九条挑起游击战的暴雨（L:日本宪法第二章第九条放弃了交战权，原文「日本国民衷心谋求基于正义与秩序的国际和平，永远放弃以国权发动战争、武力威胁或武力行使，作为解决国际争端的手段。为达到前项目的，不保持陆海空军及其他战争力量，不承认国家的交战权」）"

    # nil 「私は、アメリカンダイナー『69thStreetDiner』のバーカウンターに座って、」
    "我坐在美式餐厅『69thStreetDiner』的吧台前"

    # nil 「店主謹製のアイスコア（冷たいコアの上にソフトクリームを乗せた飲み物）を頂いていた。」
    # 参考资料：https://en.wikipedia.org/wiki/Ice_cream_float
    # 原文是アイスコア是冰芯的意思（就是南极圈科学家挖出来用于考古的那个），根据原文括号里面的意思，应该是冰淇淋苏打（フロート/ice cream float/ice cream soda）
    "我收到了店主精心制作的冰淇淋苏打(冰块上放着软雪糕的饮料)"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「…はぁう～…これ、美味しいね、てんちょーさん！」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0723.ogg"
    ai 心愛_制服_基本_笑顔 "……哈呜…这个真是好喝呢、店长桑！"
    hide 心愛_制服_基本_もぐもぐ

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「そ、それは…よ、よかったですね…ありがと…く、く…」
    show 店长_私服_微笑み_1 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0118.ogg"
    dinerowner 店长_私服_微笑み_1 "这、这样啊……啊，真是太好了…谢谢……诶嘿嘿嘿~"
    hide 店长_私服_不満_1

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「…ねぇ、さっきからなんでそんな必死に笑いを堪えてるの？」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0724.ogg"
    ai 心愛_制服_基本_真顔 "……呐，刚才你为啥那么拼命地憋笑呢？"
    hide 心愛_制服_基本_笑顔

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「え、え？　そ、そんなことは…な、ないです…よ？　ぷーくすくす」
    voice "voice/霧葉/krh_a1_0119.ogg"
    dinerowner 店长_私服_微笑み_1 "啊、诶？那个、没有这样的事……没、没嘿嘿"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「いや、あからさまに笑いを堪えてる顔だよそれ。もしかして、私の顔になんかついてる？　目と鼻と口以外で」
    show 心愛_制服_基本_ジト目 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0725.ogg"
    ai 心愛_制服_基本_ジト目 "不，你这明显是憋笑的脸。难道我的脸上有什么东西吗？除了眼睛、鼻子和嘴巴以外"
    hide 心愛_制服_基本_真顔

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「いえいえ、特には、なに…もっ…！　くすくすくす…」
    show 店长_私服_不満_1 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0120.ogg"
    dinerowner 店长_私服_不満_1 "没没没，没什么，什么都每的嗦…！嘿嘿嘿嘿……"
    hide 店长_私服_微笑み_1

    # nil 「店長さんは必死な様子で、カウンターの奥に設置してあるウォーターサーバーから、」
    "店长似乎拼命地想从柜台后面的饮水机里接上一杯饮料"

    # nil 「ミネラルウォーターをグラスに注いで、そのグラスを口に当てた。」
    "她倒了一杯矿泉水，把它拿在嘴边"

    # nil 「水を注いでる最中も、私の事を横目で見ている。」
    "在倒水的时候，也在斜眼看着我"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「じー…まぁいけど」
    voice "voice/心愛/cca_a1_0726.ogg"
    ai 心愛_制服_基本_ジト目 "盯——……嘛，算了"

    # 心爱 「……ごく……ごく……ごく……」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0727.ogg"
    ai 心愛_制服_基本_笑顔 "……咕……咕…咕……"
    hide 心愛_制服_基本_ジト目

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ぶふっ」
    show 店长_私服_微笑み_1 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0121.ogg"
    dinerowner 店长_私服_微笑み_1 "噗噗"
    hide 店长_私服_不満_1

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ちょっと！？　店長さん大丈夫！？」
    show 心愛_制服_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0728.ogg"
    ai 心愛_制服_基本_驚き "等等！？店长你没事吧！？"
    hide 心愛_制服_基本_笑顔

    # nil 「普段、クールで静かな店長さんが、大きく水を吹きだした。」
    # "平时既冷静又安静的店长，开始大口喷水（L:群龙王.jpg）"
    if persistent.luckykeeperSay == "full":
        "平时既冷静又安静的店长，开始大口喷水（L:群龙王.jpg）"
    else:
        "平时既冷静又安静的店长，开始大口喷水"

    # nil 「タイミングからみて、このコアに何か仕掛けが…。」
    "从这个时机上来看，我感觉这个冰芯里面藏了什么诡计"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「え、え、ちょっと思わず吹きだしただけです…ぜぇーはぁー…くすくす」
    show 店长_私服_不満_1 at love69_wuye_left
    voice "voice/霧葉/krh_a1_0122.ogg"
    dinerowner 店长_私服_不満_1 "那、那个，我只是忍不住笑了起来……哈——啊——哈——啊嘿嘿"
    hide 店长_私服_微笑み_1

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あー！　もしかしてぇー、このコアに何か入れたでしょ！真冬ちゃんもこの前勝手に私のジュースにシリカゲル入れるしさー！」
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0729.ogg"
    ai 心愛_制服_基本_不機嫌 "啊！难道说，你在这个冰核里面放了什么东西! 前几天，真冬酱还擅自地在我的果汁里放了硅胶!"
    hide 心愛_制服_基本_驚き

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「死んじやいますよそれ……ふう……やつと、おちつ……ふつ……あははははははははははは。もーだめだーちくしょー、もう耐え切れない、あは」
    show 店长_私服_微笑み_1 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0123.ogg"
    dinerowner 店长_私服_微笑み_1 "差点死掉了，这个……真是不行啊，呵呵哈哈哈哈哈哈哈，我已经受不了了，岂可修！啊哈哈哈哈，我已经受不鸟了，哈哈哈哈哈"
    hide 店长_私服_不満_1

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「変な薬でもやってるのかよ」
    show 心愛_制服_基本_ジト目 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0730.ogg"
    ai 心愛_制服_基本_ジト目 "你嗑了什么奇怪的药吗?!"
    hide 心愛_制服_基本_不機嫌

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「だって、だって…くすっ、心愛が…コアを…くすくすくすくす。共食いかよっ！　って…ぷーくすくすくす」
    show 店长_私服_不満_1 at love69_wuye_left
    voice "voice/霧葉/krh_a1_0124.ogg"
    # dinerowner 店长_私服_不満_1 "可是，可是…呃哈哈，心爱（cocoa）……核心（core，刚刚说的饮料里面的冰核，ice core）…啊哈哈。一起吃了下去！（L:这里是谐音梗，心爱和核心这两个词的读音很相似）"
    if persistent.luckykeeperSay == "shutup":
        dinerowner 店长_私服_不満_1 "可是，可是…呃哈哈，心爱……核心…啊哈哈。一起吃了下去！"
    else:
        dinerowner 店长_私服_不満_1 "可是，可是…呃哈哈，心爱（cocoa）……核心（core，刚刚说的饮料里面的冰核，ice core）…啊哈哈。一起吃了下去！（L:这里是谐音梗，心爱和核心这两个词的读音很相似）"

    hide 店长_私服_微笑み_1

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「…そんなツボに入る事でもないやろ」
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0731.ogg"
    ai 心愛_制服_基本_不機嫌 "那也不至于这样吧"
    hide 心愛_制服_基本_ジト目

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「あははははははは…ひー…イヒヒヒヒヒ」
    show 店长_私服_微笑み_1 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0125.ogg"
    dinerowner 店长_私服_微笑み_1 "啊哈哈哈哈哈哈哈……欸嘿……嘿嘿嘿嘿嘿"
    hide 店长_私服_不満_1

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「……ごく…ごく…ぷはー」
    show 心愛_制服_基本_もぐもぐ at love69_right with dissolve
    voice "voice/心愛/cca_a1_0732.ogg"
    ai 心愛_制服_基本_もぐもぐ "……咕…咕"
    hide  心愛_制服_基本_不機嫌

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ぶふっ…あははははははははははは、やめてくださいほんと！マジでツボなんですから…あははははははは！」
    show 店长_私服_不満_1 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0126.ogg"
    dinerowner 店长_私服_不満_1 "啊哈，哈哈哈噗哈哈哈哈哈哈哈，请不要这样做真的！这里真的是个笑穴…啊哈哈哈哈哈哈哈！"
    hide 店长_私服_微笑み_1

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「…そっか」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0733.ogg"
    ai 心愛_制服_基本_真顔 "……是吗？"
    hide 心愛_制服_基本_もぐもぐ

    # nil 「それから凡そ約3分ほど、私がコアを飲みきるまで、店長さんはクールキャラとかどうでも良い事かのように、バーカウンターを叩きながら大笑いし続けました。」
    "接下来的大约3分钟，直到我喝完冰淇淋苏打为止，店长一边敲着吧台，一边大笑，好像那是一个很酷的角色或者其他什么都好的东西"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 霧葉ちゃんのお店 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ふう…こ一年で一番笑いました」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0127.ogg"
    dinerowner 店长_私服_目閉じ "啊哈… 这是一年来我笑得最开心的一次"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「幸せな事は良い事だと思うよ」
    show 心愛_制服_基本_ジト目 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0734.ogg"
    ai 心愛_制服_基本_ジト目 "如果感觉幸福的话我觉得是好事呢"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「沢山笑わせてもらったので、お代は良いですよ。もう一杯いきます？」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0128.ogg"
    dinerowner 店长_私服_微笑み "因为让我笑了不少，给你免去不少费用。所以，要再来一杯吗？"
    hide 店长_私服_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「すぐタダにしちゃうよね…経営は大丈夫なの？」
    show 心愛_制服_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0735.ogg"
    ai 心愛_制服_基本_泣き "马上就要免费了吧…这样经营没问题吗？"
    hide 心愛_制服_基本_ジト目

    show 店长_私服_不満 at love69_wuye_left with dissolve
    hide 店长_私服_微笑み

    # 心爱 「新作出たもんね…そのせいで、蓮くんが部屋から三日間でてこなくなっちゃって、真冬ちゃんと二人でドア開けて引っ張り出した記憶あるよ」
    voice "voice/心愛/cca_a1_0736.ogg"
    # ai 心愛_制服_基本_泣き "因为出了新作品……所以，我记得莲在房间里呆了三天没出来了，我和真冬两个人开门把他拉出去了（L:原作后半句就没有配音）"
    if persistent.luckykeeperSay == "shutup":
        ai 心愛_制服_基本_泣き "因为出了新作品……所以，我记得莲在房间里呆了三天没出来了，我和真冬两个人开门把他拉出去了"
    else:
        ai 心愛_制服_基本_泣き "因为出了新作品……所以，我记得莲在房间里呆了三天没出来了，我和真冬两个人开门把他拉出去了（L:原作后半句就没有配音）"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ドアの前で△ボタン押したんですね。やっぱMove your ass hole！とでも言ったんですか？」
    # L:这里的引号之前是错的，所以报错了，要用中文引号
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    ### 雾叶 129 跳过，这里的话，按理说一般心爱不应该连续说两次，所以我觉得是原作脚本落了一句，或者是收录的时候没有想好，在制作的时候做了临时改动
    voice "voice/霧葉/krh_a1_0130.ogg"
    dinerowner 店长_私服_微笑み "你在门前按了“△”按钮，对吗？ 我就知道! Move your ass hole！你有说过吗？"
    hide 店长_私服_不満

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「現実とゲームの操作を混同してるよ店長さん！」
    show 心愛_制服_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0737.ogg"
    ai 心愛_制服_基本_驚き "你把现实和游戏操作搞混了，店长桑! "
    hide 心愛_制服_基本_泣き

    # nil 「さて、私は一条心愛。」
    "我是一条心爱"

    # nil 「さっきも述べたように、散歩中に突然の豪雨に見舞われた私は、ちょうど良い雨宿りスポットとして、このお店を利用させてもらった。」
    "就像我刚才说的，我在散步的时候遇到了突如其来的暴雨，所以我选择了这家店作为避雨的好地方"

    # nil 「このお店に来るのは、蓮君と来て以来二度目になる。」
    "这是我和莲君来这家店之后第二次来这里"

    # nil 「相変わらず、客入りは無く、店内には私と、妙に若くて愛想の良い店長さんの二人きりだ。」
    "还是老样子，店里没有客人，只有我和和蔼可亲的年轻店长两个人"

    # nil 「心なしか、店内のディスプレイが増えた気がする。」
    "也许是心理作用吧，感觉商店里的陈列品数量增加了"

    # nil 「店の隅では、店長曰く「米軍からの払い下げ」のジュークボックスが、古びた音を奏でている。」
    "在店铺的角落里，一台据经店长说是「从美国军队传下来的」点唱机正在发出陈旧的声音"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「…あれ？」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0738.ogg"
    ai 心愛_制服_基本_真顔 "…嗯？啊咧？"
    hide 心愛_制服_基本_驚き

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ん？」
    show 店长_私服_不満 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0131.ogg"
    dinerowner 店长_私服_不満 "嗯？"
    hide 店长_私服_微笑み

    # nil 「私は前回来た時には明かになかったものに気づき、カウンター席を降りた。」
    "我注意到了上次来的时候没有的东西，于是走下了吧台"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ピアノなんてあったっけ？」
    show 心愛_制服_基本_無表情 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0739.ogg"
    ai 心愛_制服_基本_無表情 "有钢琴的嘛？"
    hide 心愛_制服_基本_真顔

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「あ、それ最近貰ったんですよ。友達の家にあったやつなんですけど、要らないっていうのでせっかくなので頂いてきちゃいました」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0132.ogg"
    dinerowner 店长_私服_微笑み "啊，那个是最近收到的。虽然是朋友家里的，但是因为他不需要所以好不容易才收到的"
    hide 店长_私服_不満

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「店長さん弾けるの？」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0740.ogg"
    ai 心愛_制服_基本_真顔 "店长你会弹吗？"
    hide 心愛_制服_基本_無表情

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「いや、私は楽器の類は全然。強いて言えば、『女』ぐらいですかね？　まともに鳴らせるのは」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0133.ogg"
    # dinerowner 店长_私服_目閉じ "不，我完全不喜欢乐器之类的。硬要说的话，只有『女』这种乐器吧？能让我好好『演奏』的"
    dinerowner 店长_私服_目閉じ "不，我完全不喜欢乐器之类的。硬要说的话，只有『女人』这种乐器吧？能让我好好『演奏』的"
    hide 店长_私服_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「それはさぞかし良い声で鳴くんでしょうね、貴方」
    show 心愛_制服_基本_ジト目 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0741.ogg"
    ai 心愛_制服_基本_ジト目 "它的叫声一定很好听吧，亲爱的?"
    hide 心愛_制服_基本_真顔

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「試してみますか？」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0134.ogg"
    dinerowner 店长_私服_微笑み "要试试吗？"
    hide 店长_私服_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「機会があればね」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0742.ogg"
    ai 心愛_制服_基本_真顔 "如果有机会的话?"
    hide 心愛_制服_基本_ジト目

    # nil 「私はグランドピアノの蓋を開けて、ド・レ・ミ・ファ・ソ・ラ・シ・ドを奏でる。」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%B0%E3%83%A9%E3%83%B3%E3%83%89%E3%83%94%E3%82%A2%E3%83%8E
    "我打开grand piano（大钢琴/三角钢琴）的盖子，演奏Do、Re、Mi、Fa、Sol、La、Si"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「昨日あたり、そのピアノをくれた友達がメンテナンスしたので、一応音はしっかり鳴るはずですが…」
    show 店长_私服_不満 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0135.ogg"
    dinerowner 店长_私服_不満 "昨天的时候，那个给我钢琴的朋友保养过了，所以应该会好好地响起来…"
    hide 店长_私服_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「うん、調律はされてるみたい」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_0743.ogg"
    ai 心愛_制服_基本_嬉しい "嗯，好像调过音了"
    hide 心愛_制服_基本_真顔

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「弾けるんですか？」
    show 店长_私服_無表情 at love69_wuye_left
    voice "voice/霧葉/krh_a1_0136.ogg"
    dinerowner 店长_私服_無表情 "你会弹吗? "
    hide 店长_私服_不満

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ちょっとね。好きって言ってくれた人がいるから、練習したの」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0744.ogg"
    ai 心愛_制服_基本_笑顔 "有点吧。有人说喜欢，所以我就练习了一下"
    hide 心愛_制服_基本_嬉しい

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「この前の…彼ですか」
    show 店长_私服_ニヤリ_1 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0137.ogg"
    dinerowner 店长_私服_ニヤリ_1 "是上次的…他吗？"
    hide 店长_私服_不満

    stop music fadeout 2.0
    image bg ccg01_2_1 = "images/ev/ccg01_2_1.png"
    scene ccg01_2_1 with dissolve

    # nil 「その問いには答えず、私はピアノの前に座ってゆっくりエボニーとアイボリーを叩き始める。」
    # 这里的两个事物指代颜色
    # 参考资料：https://en.wikipedia.org/wiki/Ivory_(color)
    "我没有回答那个问题，坐在钢琴前慢慢地开始敲击黑白琴键"

    play music bgmtwelve fadein 2.0
    $ renpy.notify("BGM:g線上kp")

    # 店长 「Ｇ線上のアリアですか…雨音にはよく合いますね」
    voice "voice/霧葉/krh_a1_0138.ogg"
    # dinerowner 店长_私服_目閉じ "是G线上的咏叹调吗…很适合雨声呢? （L:是巴赫代表作品之一，「第三号管弦乐组曲」的第二乐章主题）"
    if persistent.luckykeeperSay == "shutup":
        dinerowner 店长_私服_目閉じ "是G线上的咏叹调吗…很适合雨声呢? "
    else:
        dinerowner 店长_私服_目閉じ "是G线上的咏叹调吗…很适合雨声呢? （L:是巴赫代表作品之一，「第三号管弦乐组曲」的第二乐章主题）"

    # nil 「ジュークボックスから流れる音が止まる。店長が止めてくれたのだろう。」
    "从点唱机传出的声音停止了。一定是店长关掉的吧"

    # nil 「私は、第三番第二楽章を奏でながら、彼の事を思い浮かべる。」
    "我一边弹奏着第三号第二乐章，一边想起了他的事情"

    # nil 「そう。幼い頃、親に無理矢理習わされていたピアノの発表会を見に来てくれた彼が、」
    "是的，在我小的时候，他来观看我父母强迫我学习的钢琴的演奏发表会"

    # nil 「『こあちゃんのピアノはなんかよくわかんないけど好き』」
    "『我不太懂你的钢琴，但我喜欢』"

    # nil 「と言ってくれた事で、私はピアノを弾く事が苦ではなくなった。」
    "因为你这么说过，所以我弹钢琴就不再痛苦了"

    # nil 「成長して、ピアノに触れる機会は減ってしまった。最後に彼に聞かせたのはいつだろうか。」
    "长大之后，接触钢琴的机会逐渐减少了。最后一次弹给他听是在什么时候呢"

    # nil 「彼の事を考えると、胸が熱くなる。」
    "一想到他，我就心潮澎湃"

    # nil 「あの日以来、蓮君と身体を重ねた事はないし、特にこれといって進展は無かった。」
    "从那天以来，我没有和莲君重叠过身体，也没有什么特别的进展"

    # nil 「単純に、二人きりになる機会が無いだけと言えばそれだけだけど…。」
    "简单来说，如果说只是没有两个人独处的机会的话，也就只有这样了…"

    # nil 「でも、以前よりも、素直になれている気がして、それは嬉しい。」
    "但是，比起以前，我觉得我更坦率，我很开心"

    # nil 「でも…。」
    "但是…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「（まふまふちゃん…）」
    voice "voice/心愛/cca_a1_0745.ogg"
    ai 心愛_制服_基本_真顔 "（嘛呼嘛呼酱……）"

    # nil 「これは、憶測ではあるが、真冬ちゃんも、きっと、蓮君に対して、私と同じような感情を抱いているはずだ。」
    "虽然这只是我的猜测，但真冬一定也对莲君抱有和我一样的感情"

    # nil 「というか、もしかしたら、私の知らない所で、結ばれているかもしれない。」
    "或者说，也许，在我不知道的地方，已经结合在一起了"

    # nil 「別に、それについて私は一切ネガティブな感情を抱きはしなかった。」
    "不过，关于这个，我完全没有消极的感情"

    # nil 「だけど、真冬ちゃんは私が蓮くんと結ばれるとしたら、どんな風に思うだろう。」
    "但是，如果我能和莲君结婚的话，真冬酱会怎么想呢"

    # nil 「私は、真冬ちゃんの事も、蓮くんと同じように大好きで…。」
    "我对真冬酱的感情，就像我对莲君一样喜欢"

    # nil 「蓮くんと同じように、真冬ちゃんとも結ばれる事ができたら…。」
    "如果能和莲君一样，也能和真冬酱结婚的话……"

    # nil 「我ながら、それは自分勝手だとも思うし、異常だとも思う。」
    "我自己也觉得那是任性的，也是不正常的"

    # nil 「そんな戸惑いが、私の思いを、まだ揺るがせていた。」
    "这样的困惑，仍然动摇着我的思绪"

    stop music fadeout 2.0

    # nil 「気づいたら、私は曲を弾き終えていた。」
    "回过神来，我已经把曲子弹完了"

    # nil 「ぱちぱちぱちぱち　と一人分の拍手が響き渡る。」
    "劈里啪啦地响起一个人的掌声"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「お上手ですね」
    voice "voice/霧葉/krh_a1_0139.ogg"
    dinerowner 店长_私服_微笑み "弹的真好呢"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    image bg ccg01_3_2 = "images/ev/ccg01_3_2.png"
    scene ccg01_3_2 with dissolve

    # 心爱 「ありがと。でも、久しぶりだったから、所々ミスしちゃったけどね」
    voice "voice/心愛/cca_a1_0746.ogg"
    ai 心愛_制服_基本_嬉しい "谢谢啦。不过，因为好久没弹过了，有些地方出了差错"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ミスの原因は、果たして久しぶりだったからだけですかね？」
    voice "voice/霧葉/krh_a1_0140.ogg"
    dinerowner 店长_私服_目閉じ "失误的原因，果然只是因为很久没弹了吧？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    image bg ccg01_4_1 = "images/ev/ccg01_4_1.png"
    scene ccg01_4_1 with dissolve

    # 心爱 「へ？」
    voice "voice/心愛/cca_a1_0747.ogg"
    ai 心愛_制服_基本_真顔 "欸？！"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「いやー、音楽の事はわかりませんけど、音色から、なんだか、悩みでもあるよーな、そんなニュアンスを感じましたよ」
    voice "voice/霧葉/krh_a1_0141.ogg"
    dinerowner 店长_私服_微笑み "不，虽然我不知道音乐的事情，但是从音色上，总觉得有种烦恼的感觉"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    scene ccg01_3_2 with dissolve

    # 心爱 「あはー…んー、ちょっとね、ピアノ弾いてると、色々思い出しちゃうよね」
    voice "voice/心愛/cca_a1_0748.ogg"
    ai 心愛_制服_基本_嬉しい "啊哈哈哈…嗯，有点呢，在弹钢琴的时候，会想起很多事情呢"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「彼の事ですか？」
    voice "voice/霧葉/krh_a1_0142.ogg"
    dinerowner 店长_私服_不満 "是关于他的事情吗？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「半分正解」
    voice "voice/心愛/cca_a1_0749.ogg"
    ai 心愛_制服_基本_嬉しい "对了一半"

    image bg ccg01_2_2 = "images/ev/ccg01_2_2.png"
    scene ccg01_2_2 with dissolve

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ふーむ。私で良ければ聞きますよ？　あ、それと、演奏料としてどうぞ」&（配音感觉少了半句，？后面的没有）
    voice "voice/霧葉/krh_a1_0143.ogg"
    # dinerowner 店长_私服_目閉じ "嗯，如果你不介意的话，可以和我说说。啊，还有，作为演奏费（L:原作这句话也是只说了一半）"
    if persistent.luckykeeperSay == "shutup":
        dinerowner 店长_私服_目閉じ "嗯，如果你不介意的话，可以和我说说。啊，还有，作为演奏费"
    else:
        dinerowner 店长_私服_目閉じ "嗯，如果你不介意的话，可以和我说说。啊，还有，作为演奏费（L:原作这句话也是只说了一半）"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ありがとう、てんちょーさん」
    voice "voice/心愛/cca_a1_0750.ogg"
    ai 心愛_制服_基本_笑顔 "谢谢你，店长桑"

    # nil 「店長さんは微笑みながら、もう一杯私にアイスコアを振る舞ってくれた。」
    "店长一边微笑着，一边又拿来一杯冰淇淋苏打给我"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ぷっ…くすくすくす…あは。やっぱりダメだわらっちまうあは」
    voice "voice/霧葉/krh_a1_0144.ogg"
    dinerowner 店长_私服_にっこり "噗...噗...啊哈哈哈哈哈哈哈。果然还是不行，笑死人了啊哈哈哈哈"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    image bg ccg01_1_1 = "images/ev/ccg01_1_1.png"
    scene ccg01_1_1 with dissolve

    # 心爱 「だめだ耐えろ」
    voice "voice/心愛/cca_a1_0751.ogg"
    ai 心愛_制服_基本_真顔 "不行，忍一下！"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ぐっ…」
    voice "voice/霧葉/krh_a1_0145.ogg"
    dinerowner 店长_私服_不満 "咕…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「…よし」
    voice "voice/心愛/cca_a1_0752.ogg"
    ai 心愛_制服_基本_嬉しい "……好"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ぷっ」
    voice "voice/霧葉/krh_a1_0146.ogg"
    dinerowner 店长_私服_不満_1 "噗"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    scene ccg01_3_2 with dissolve

    # 心爱 「…」
    voice "voice/心愛/cca_a1_0753.ogg"
    ai 心愛_制服_基本_無表情 "……"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「で？　何をお悩みなんです？」
    voice "voice/霧葉/krh_a1_0147.ogg"
    dinerowner 店长_私服_目閉じ "所以……你在烦恼什么呢？"

    # nil 「店長さんは椅子を引っ張ってきて、私の隣に座った。」
    "店长拉过一把椅子，坐在了我的边上"

    # nil 「私は一度鍵盤の蓋を閉じて、そこにグラスを置いた。」
    "我合上琴盖，把杯子放在了上面"

    # nil 「ジュークボックスも、ピアノも音楽を奏でない。降りしきる雨音だけが、店内の静寂を彩っていた。」
    "点唱机和钢琴都不再发出声音。只有淅淅沥沥的雨声，点缀着店内的寂静"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「「んー、贅沢な悩みなのかな、あんまり人に相談するような事じゃないよ」」
    voice "voice/心愛/cca_a1_0754.ogg"
    ai 心愛_制服_基本_泣き "嗯——是不是有点奢侈的烦恼啊，没什么好和别人商量的呢"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「悩みに、贅沢もへったくれもあるんですかね？」
    voice "voice/霧葉/krh_a1_0148.ogg"
    dinerowner 店长_私服_微笑み "烦恼也是有奢侈和无聊的烦恼吧？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「そういうもんかな？　客観的に見て、全ては順調に進んでるはずだし…」
    voice "voice/心愛/cca_a1_0755.ogg"
    ai 心愛_制服_基本_無表情 "是这样吗？客观地看，一切都是在顺利进行……"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「恋愛は客観じゃなくて、主観ですよ。心が満たされてないから、苦しいんですよ」
    voice "voice/霧葉/krh_a1_0149.ogg"
    dinerowner 店长_私服_微笑み "恋爱不是客观的，而是主观的。因为心灵上没有满足，所以很痛苦吧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「うーん…」
    voice "voice/心愛/cca_a1_0756.ogg"
    ai 心愛_制服_基本_泣き "嗯……"

    # nil 「店長さんの言う事は正論だったが、口に出すのは少し憚れる。」
    "店长说得没错，但我有点不好意思说出口"

    # nil 「店長さんは微笑みを崩さないで、まっすぐに私の瞳を見つめている。」
    "店长微笑着，一直盯着我的眼睛"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「こんな事は良くない…なんて思っているのに、心が求めてしまう場合、どうすればいと思う？」
    voice "voice/心愛/cca_a1_0757.ogg"
    ai 心愛_制服_基本_真顔 "这样的事情不太好…明明这么想，心里却在寻求，你觉得应该怎么办比较好？"

    # nil 「私は一瞬逡巡したが、そう口に出した。」
    "我犹豫了一瞬间，这样说了出来"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「そうですねー。私の経験から言わせて貰うと、自分の心には素直に従った方が良いですよ」
    voice "voice/霧葉/krh_a1_0150.ogg"
    dinerowner 店长_私服_にっこり "是这样啊。以我的经验来看，还是顺从自己的内心比较好"

    # 店长 「素直になりきれずに、相手を傷付けてしまうなんて、かっこ悪いじゃないですか」
    voice "voice/霧葉/krh_a1_0151.ogg"
    dinerowner 店长_私服_微笑み "不能坦诚相待，却伤害了对方，这不是很不酷吗?"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「店長さんにもそんな過去が？」
    voice "voice/心愛/cca_a1_0758.ogg"
    ai 心愛_制服_基本_驚き "店长也有过这样的过去吗？"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「それは、悩みが解消された時にでも教えてあげますよ」
    voice "voice/霧葉/krh_a1_0152.ogg"
    dinerowner 店长_私服_ニヤリ_1 "这点的话，在你烦恼消除的时候会告诉你的"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「うーん。自分が求める事で、悪い方向に転がったら…って考えちゃうんだよね」&（这里配音也是少半句）
    voice "voice/心愛/cca_a1_0759.ogg"
    # ai 心愛_制服_基本_泣き "嗯……如果因为自己的追求，而使事情朝着不好的方向发展的话……会这么想吧（L:这里原作的配音也是不全）"
    if persistent.luckykeeperSay == "shutup":
        ai 心愛_制服_基本_泣き "嗯……如果因为自己的追求，而使事情朝着不好的方向发展的话……会这么想吧"
    else:
        ai 心愛_制服_基本_泣き "嗯……如果因为自己的追求，而使事情朝着不好的方向发展的话……会这么想吧（L:这里原作的配音也是不全）"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「その気持ちの根源が、好きという気持ちならば…。きっと、良い方に転ぶはずです」
    voice "voice/霧葉/krh_a1_0153.ogg"
    dinerowner 店长_私服_微笑み "如果这种心情的根源是喜欢......那就一定会向好的方向发展"

    # 店长 「もし、一度それで芳しく無い事態に陥っても…。諦めなければ、必ず良い結果に辿り着けますよ」
    voice "voice/霧葉/krh_a1_0154.ogg"
    dinerowner 店长_私服_目閉じ "即使一时陷入不好的境地.....只要不放弃，也一定会有好结果的"

    # 店长 「人を好きになるって、素敵な事じゃないですか」
    voice "voice/霧葉/krh_a1_0155.ogg"
    dinerowner 店长_私服_微笑み "喜欢上一个人，不是很美妙吗?"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「確かに…。好きになる事ができて、私は、幸せだよ。それは、絶対なんだ」
    voice "voice/心愛/cca_a1_0760.ogg"
    ai 心愛_制服_基本_真顔 "确实…能喜欢上他，我很幸福。那是绝对的"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「なら、例えどんな事があっても自分の気持ちを曲げず、突き進むのみです。応援していますよ、心愛ちゃん」
    voice "voice/霧葉/krh_a1_0156.ogg"
    dinerowner 店长_私服_にっこり "那么，不管发生什么事情，都不要改变自己的心情，勇往直前。我会支持你的，心爱酱"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「う、うん。あ、ありがとう。てんちょーさん、少しだけ、自分のすべき事がわかってきた気がするよ！」
    voice "voice/心愛/cca_a1_0761.ogg"
    ai 心愛_制服_基本_嬉しい "嗯，嗯！啊，谢谢你，店长桑，我觉得我稍微明白了自己该做的事"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「Holy Hallelujah！その意気です。今ならきっと、素敵な曲が弾けるんじゃないでしょうか」
    voice "voice/霧葉/krh_a1_0157.ogg"
    dinerowner 店长_私服_にっこり "Holy Hallelujah！就是这个意思。现在的话一定能弹出很棒的曲子吧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「そだね！じゃぁ…今の気分に合う一曲、弾いてみるね」
    voice "voice/心愛/cca_a1_0762.ogg"
    ai 心愛_制服_基本_笑顔 "是啊！那我就弹奏一首符合现在心情的曲子吧"

    # nil 「私はもう一度、ピアノに向かって座り、蓋を開いた。」
    "我再一次面向钢琴坐下，打开了钢琴的盖子"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「Let's get smokoin' party!!」
    voice "voice/心愛/cca_a1_0763.ogg"
    ai 心愛_制服_基本_笑顔 "Let's get smokoin' party!!"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「Bring It on!」
    voice "voice/霧葉/krh_a1_0158.ogg"
    dinerowner 店长_私服_にっこり "Bring It on!"

    play music bgmeight fadein 4.0
    $ renpy.notify("BGM:anonatsu_piano")

    # nil 「私はアップテンポのジャズナンバーを弾きながら、改めて二人の事を考える。」
    "我一边弹奏着快节奏的爵士乐曲，一边重新考虑两个人的事情"

    # nil 「そうだ。いちいち悩んでいても仕方がない。」
    "是的，一个接一个的烦恼是没用的"

    # nil 「自分の気持ちを信じて、攻めるのみだ。」
    "只有相信自己的心情，然后去进攻"

    # nil 「彼と重ねた唇、彼が触れた身体が、音楽にあわせて熱を帯び始める。」
    "和他重叠过的嘴唇，以及他触摸过的身体，随着音乐开始发热"

    # nil 「背後ではシャカシャカとシェイカーの音が、ビートを刻むパーカスのように、旋律を追いかける。」
    "在背后，沙沙声和振动器（Shakers）的声音，像打着节拍的打击乐手一样，追逐着钢琴的旋律"

    # nil 「私は自分の決意を固めるためにも、力強く鍵盤を叩く。」
    # "为了坚定自己的决心，我也用力地敲击着键盘（KeyBoard）"
    "为了坚定自己的决心，我也用力地敲击着琴键（KeyBoard）"

    # nil 「もう悩まない。」
    "不要再烦恼了"

    # nil 「二人の事を好きになってしまったし、彼には思いを告げてしまった。」
    # "我喜欢上了两个人，也告诉了他我的想法"
    "我喜欢上了两个人在一起的感觉，也告诉了他我的想法"

    # nil 「最初から後戻りなんてできやしないんだ。」
    "从开始就没有回头路了"

    # nil 「このま何もせず自然消滅する？」
    "这之后什么都不做就自然消失了？"

    # nil 「そんなのは嫌だ。」
    "我讨厌那样"

    # nil 「ならば…私から…。」
    "那么……由我来…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「（どんな事が、あっても…！）」
    voice "voice/心愛/cca_a1_0764.ogg"
    ai 心愛_制服_基本_真顔 "（无论发生什么事情…！）"

    # nil 「カランコロンカラーン」
    # 参考资料：http://blog.livedoor.jp/nanshiba/archives/6616200.html （（カランコロンカラーン　※注意：こういう音はしません。演出です））
    "我心中默念着"

    # 莲 「ぬわあん濡れたもおん。　シャツがもうビショビショだよ…」
    lian "全身都湿透了，连衬衫都已经湿透了..."

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「おや、こいつは…」
    voice "voice/霧葉/krh_a1_0159.ogg"
    dinerowner 店长_私服_目閉じ "哦呀，这家伙…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぶぇ！？」
    voice "voice/心愛/cca_a1_0765.ogg"
    ai 心愛_制服_基本_驚き "呜欸！？"

    # nil 「私は聞き慣れた声を耳にして、つい思わず演奏を止めてしまった。」
    "我听到了耳熟的声音，不由自主地停止了演奏"

    stop music fadeout 2.0

    # scene07 场景1 【心爱酱的烦恼与时隔许久的演奏】 结束
    # scene07 场景2 【说曹操曹操到】 开始
    # 小场景的名称
    $ partName = " 【说曹操曹操到】"
    $ changeTitleName()
    
    # 场景切回店内
    # BGM切回店内英文歌

    scene 霧葉ちゃんのお店 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)
    play music bgmfifteen fadein 4.0
    $ renpy.notify("BGM:jonay_-_want_you_to_know")

    # nil 「やれやれ厄介な雨だ。」
    "哎呀，真是场麻烦的雨"

    # nil 「夏はそんなに嫌いじゃないが、夜、狙ったかのように耳元で飛び回るモスキート野郎と、」
    "我并不那么讨厌夏天，但是晚上，总是有像是瞄准了什么似的混蛋在耳边飞来飞去"

    # nil 「終戦から60年も経っているというのに、ゲリラ戦を仕掛けてくるこの豪雨だけは好きになれない。」
    # "虽然战争结束已经超过60年了，但我还是不喜欢发起游击战的这场暴雨（L:作品是13年的，1945年8月15日日本宣布投降，并于9月2日在美国最后一艘战列舰密苏里号甲板上签署《降伏文书》，这也意味着第二次世界大战正式宣告结束）"
    if persistent.luckykeeperSay == "shutup":
        "虽然战争结束已经超过60年了，但我还是不喜欢发起游击战的这场暴雨"
    else:
        "虽然战争结束已经超过60年了，但我还是不喜欢发起游击战的这场暴雨（L:作品是13年的，1945年8月15日日本宣布投降，并于9月2日在美国最后一艘战列舰密苏里号甲板上签署《降伏文书》，这也意味着第二次世界大战正式宣告结束）"

    # nil 「お隣の赤い国では雲にミサイルを打ち込んで無理矢理晴れにしてた事もあるらしいが…。」
    # 参考资料：https://sports.yahoo.co.jp/column/detail/200808140015-spnavi
    # 参考资料：http://www.gov.cn/gzdt/2008-08/09/content_1068226.htm
    # "我听说在邻近的红色国家，好像也有把导弹打到云层里强行将其变为晴朗的情况…（L:这里说的是咱们，08年北京奥运会为保障开幕式不受影响，北京市人工影响天气中心共组织了20轮次地面消雨拦截作业，累计发射火箭1104枚）"
    if persistent.luckykeeperSay == "shutup":
        "我听说在邻近的红色国家，好像也有把导弹打到云层里强行将其变为晴朗的情况…"
    else:
        "我听说在邻近的红色国家，好像也有把导弹打到云层里强行将其变为晴朗的情况…（L:这里说的是咱们，08年北京奥运会为保障开幕式不受影响，北京市人工影响天气中心共组织了20轮次地面消雨拦截作业，累计发射火箭1104枚）"

    # nil 「不幸にも、散歩中に豪雨に見舞われた俺は雨宿りする場所を探し求めていたが、全く見つからず、ようやくこにたどり着いた。」
    "不幸的是，在散步的时候遭遇了暴雨，我一直在寻找避雨的地方，但是完全找不到，就这样慢慢地走到了这里"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「や、いらっしゃい。二名様でよろしかったですか？」
    show 店长_私服_微笑み at love69_wuye_center with dissolve
    voice "voice/霧葉/krh_a1_0160.ogg"
    dinerowner 店长_私服_微笑み "呀，欢迎光临。是两位客人对吗？"

    # 莲 「おいおい背後霊でも見えちまってるのか？夏だからって怪談するにはちょっと時間が早すぎるぜ、アンタ」
    lian "喂喂，你是不是看到了背后的幽灵? 现在是夏天，所以讲鬼故事有点太早了，店长桑"

    # 店长 「いやいや、見えてないのは貴方だけですよ。よく周りを見渡してみたらどうですか？」
    show 店长_私服_目閉じ at love69_wuye_center with dissolve
    voice "voice/霧葉/krh_a1_0161.ogg"
    dinerowner 店长_私服_目閉じ "不不不，看不见的只有你哦。仔细好好看看周围如何？"
    hide 店长_私服_微笑み

    # 莲 「まじかよ」
    lian "讲真？！"

    # nil 「俺は焦って背後を振り向いた。が、そこに誰もおらず、むしろ背後に人が立つスペースもない。」
    "我焦急地回头看了看背后。但是，那里什么都没有，甚至连人站在身后的空间都没有"

    # 店长 「こっちですよ」
    show 店长_私服_微笑み at love69_wuye_center with dissolve
    voice "voice/霧葉/krh_a1_0162.ogg"
    dinerowner 店长_私服_微笑み "在这边哦"
    hide 店长_私服_目閉じ

    # nil 「店主の女性は、ニヤりと笑いながら、別の方向を指差している。」
    "店长一边笑着一边指向别的方向"

    # 莲 「あん？」
    lian "啊？"

    # nil 「すると、どうにも見慣れたシルエットがこちらに目線を向けていた。」
    "这时，一个非常熟悉的轮廓正朝着这边看"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱闪现
    hide 店长_私服_微笑み
    show 店长_私服_微笑み:
        zoom 1.5
        yalign 0.015
        xalign 0.52
        linear 0.3 xalign 0.11

    # 心爱 「や、やっほー、蓮くん」
    show 心愛_制服_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0766.ogg"
    ai 心愛_制服_基本_泣き "呀，Yahoo~，莲君"

    # 莲 「こんな所で出会うとは…。よう、心愛。しかし…先客がいるとは、繁盛したもんだなこも」（生异形啊，你们哥俩。 ~~快进到萨日朗~~）
    lian "没想到会在这种地方相遇……哟，心爱。不过说起来……已经有客人在了，生意不戳啊"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「お陰様で。さてさて、びしょ濡れのまんまじゃ風邪引きますよ。奥にシャワーあるんで浴びてきたらどうですか？」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0163.ogg"
    dinerowner 店长_私服_目閉じ "托您的福。那么，湿淋淋的话可是会感冒的哦。里面有淋浴，去洗个澡怎么样？"
    hide 店长_私服_微笑み

    # 莲 「シャワーまでついてるのかよこの店は…」
    lian "这家店连淋浴都有的吗…"

    # 店长 「ただしタオルはレンタル100円です」
    show 店长_私服_ニヤリ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0164.ogg"
    # dinerowner 店长_私服_ニヤリ "但是毛巾要100日元来租（L:100日元换成软妹币就是6块多点，说起来，这作的两个前作是“100日元系列”的，正正好好只要100日元，有能力的话可以去支持一下）"
    if persistent.luckykeeperSay == "shutup":
        dinerowner 店长_私服_ニヤリ "但是毛巾要100日元来租"
    else:
        dinerowner 店长_私服_ニヤリ "但是毛巾要100日元来租（L:100日元换成软妹币就是6块多点，说起来，这作的两个前作是“100日元系列”的，正正好好只要100日元，有能力的话可以去支持一下）"

    hide 店长_私服_目閉じ

    # 莲 「わかった。じゃぁタオル無しで浴びるわ」
    lian "知道了。那我就不用毛巾洗了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「だ、だめだよ蓮くん！　風邪治ったばっかなんだからさ！」
    show 心愛_制服_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0767.ogg"
    ai 心愛_制服_基本_驚き "不、不可以的莲君！感冒才刚好的呢！"
    hide 心愛_制服_基本_泣き

    # 莲 「うお、いつになく正論だな！？という事だ、店長さん、タオルも出来ればタダで貸してくれないか」
    # lian "哦，这么说的话比你之前说的更有道理一些呢! ? 店长，如果可以的话，毛巾也可以免费借给我吗"
    lian "哦，这么说的话比你之前说的更有说服力一些呢! ? 店长，如果可以的话，毛巾也可以免费借给我吗"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「100円をケチる男はモテませんよ？」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0165.ogg"
    dinerowner 店长_私服_目閉じ "吝啬100日元的男人可不受欢迎哦？"
    hide 店长_私服_ニヤリ

    # 莲 「100円あればゲーム一本買える時代なんだよ…」
    # lian "现在是只要有100日元就能买一个游戏的时代哦（L:这里说的就是本作的前作S.I.S.T.A.R.S: Kiss of Trinity和Color of White）"
    if persistent.luckykeeperSay == "shutup":
        lian "现在是只要有100日元就能买一个游戏的时代哦"
    else:
        lian "现在是只要有100日元就能买一个游戏的时代哦（L:这里说的就是本作的前作S.I.S.T.A.R.S: Kiss of Trinity和Color of White）"

    # 店长 「まぁいでしょう、蓮くんの体調管理委員会からの指導により、タオルもご自由にどうぞ」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0166.ogg"
    dinerowner 店长_私服_微笑み "嘛，算了吧，在莲君健康管理委员会的指导下，毛巾也请自由使用"
    hide 店长_私服_目閉じ

    # 莲 「さんきゅーこあ」
    lian "那3Q啦~"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「おういぇす！まったくお大事にしなきゃダメなんだぞほんとはー」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_0768.ogg"
    ai 心愛_制服_基本_嬉しい "Oh Yes！真的是，一定要照顾好自己啊"
    hide 心愛_制服_基本_驚き

    # 莲 「へいへい。今度から折りたみ傘は持ち歩きますよ」
    lian "嘿嘿，下次我会带好折叠伞再出门的"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「それとコンドームもね」
    show 店长_私服_ニヤリ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0167.ogg"
    dinerowner 店长_私服_ニヤリ "也请带好避孕套哦"
    hide 店长_私服_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「それは大丈夫」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0769.ogg"
    ai 心愛_制服_基本_真顔 "这个的话没关系"
    hide 心愛_制服_基本_嬉しい

    # 莲 「なんでお前が答えるんだよ。まぁ持ってるけど」
    lian "为啥你要回答呢。嘛，我还真带着呢233"

    # nil 「とにかく、俺は店長に案内されて、シャワー室へと入った。」
    "总之，我被店长带去了浴室"

    # 莲 「覗くなよ？」
    lian "不要偷看哦？"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「マに習いませんでした？　寝言は寝て言えって」
    show 店长_私服_不満 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0168.ogg"
    dinerowner 店长_私服_不満 "没有和妈妈学过吗？梦话要在睡觉的时候说哦"
    hide 店长_私服_ニヤリ

    # 莲 「俺がマから習ったのは、フロントホックは片手で外せという事だけだ…」
    lian "我从妈妈那里学到的唯一一件事，就是用一只手解开前面的扣子..."

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「じー」
    show 心愛_制服_基本_ジト目 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0770.ogg"
    ai 心愛_制服_基本_ジト目 "盯——"
    hide 心愛_制服_基本_真顔

    # 莲 「いやん」
    lian "别呀"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 霧葉ちゃんのお店 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # nil 「シャツがビショビショだったので、お店特製のＴシャツを買いました（1200円）」
    # "因为衬衫是双排扣的，所以买了件店里特制的T恤（1200日元）（L:应该是单手没给解开2333）"
    if persistent.luckykeeperSay == "full":
        "因为衬衫是双排扣的，所以买了件店里特制的T恤（1200日元）（L:应该是单手没给解开2333）"
    else:
        "因为衬衫是双排扣的，所以买了件店里特制的T恤（1200日元）"

    # nil 「あと心愛ちゃんにキーホルダーも買ってあげました（600円）」
    "还给心爱酱买了条钥匙链（600日元）"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「タオルはケチるのに…」
    show 店长_私服_不満 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0169.ogg"
    dinerowner 店长_私服_不満 "借毛巾的时候明明很小气…"

    # 莲 「デザインが気に入った」
    lian "因为设计的挺不戳的"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「わーい♪早速穴あき包丁につけるね！」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0771.ogg"
    ai 心愛_制服_基本_笑顔 "哇——咿♪马上把它放在有洞的菜刀上吧!"

    # 莲 「あの穴、別にアクセをつける穴じゃねぇけどな…。切れなくなるから、他の物につけなさい」
    lian "那个洞，并不是用来装装饰品的洞…因为会切不了菜，所以请挂在别的东西上吧"

    # 心爱 「外付けハードディスクとか？」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0772.ogg"
    ai 心愛_制服_基本_真顔 "外置的Hard Disk之类的？"
    hide 心愛_制服_基本_笑顔

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「２４段変速ロードレーサーとか」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0170.ogg"
    dinerowner 店长_私服_無表情 "24级变速公路自行车什么的上面？"
    hide 店长_私服_不満

    # 莲 「遺伝子組み換えモロヘイアとかな」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%B7%E3%83%9E%E3%83%84%E3%83%8A%E3%82%BD
    # 搜到了有趣的东西捏：https://www.zhihu.com/question/274326256/answer/374965288
    # lian "转基因的缟纲麻上面（L:原产不明，有印度和北非说，在日本用来做调味料，做天妇罗之类的，其种子有强心作用，部分动物吃了会中毒而死，目前没有人类中毒的记录，在药理上有一定抑制高血压的作用）"
    if persistent.luckykeeperSay == "shutup":
        lian "转基因的缟纲麻上面"
    else:
        lian "转基因的缟纲麻上面（L:原产不明，有印度和北非说，在日本用来做调味料，做天妇罗之类的，其种子有强心作用，部分动物吃了会中毒而死，目前没有人类中毒的记录，在药理上有一定抑制高血压的作用）"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「何でも言えばいってもんじゃねぇぞ…」
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0773.ogg"
    ai 心愛_制服_基本_不機嫌 "不能什么都说啊..."
    hide 心愛_制服_基本_真顔

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 莲&店长 「すんません」
    # 要记得去人物表加人物，头像是店长的
    voice "voice/霧葉/krh_a1_0171.ogg"
    lian_and_dinerowner 店长_私服_無表情 "对不起"

    # nil 議論の結果『有機ＥＬディスプレイ』にくっつける事にきまりました。
    # 参考资料：https://www.weblio.jp/content/%E6%9C%89%E6%A9%9FEL%E3%83%87%E3%82%A3%E3%82%B9%E3%83%97%E3%83%AC%E3%82%A4
    # "经过讨论，我们决定把它贴在『有机EL显示器』上（L:有机EL显示器，即“有机电致发光显示器”，即“有机LED显示屏”，其实就是OLED显示器啦，原文非要说的那么绕233）"
    if persistent.luckykeeperSay == "shutup":
        "经过讨论，我们决定把它贴在『有机EL显示器』上"
    else:
        "经过讨论，我们决定把它贴在『有机EL显示器』上（L:有机EL显示器，即“有机电致发光显示器”，即“有机LED显示屏”，其实就是OLED显示器啦，原文非要说的那么绕233）"

    # nil 「さて、以前雨はしきりに降り注いだまです。」
    "话说到，刚才雨一直下个不停"

    # nil 「心愛と二人、隣同士でバーカウンターに座ります。」
    "和心爱两个人并排坐在吧台"

    # nil 「とりあえず雨が止むまで、こで心愛と一緒に雨宿りと洒落込みます。」
    "总之在雨停之前，我在这里和心爱一起躲雨"

    # nil 「真冬には一応、雨が止んだら帰るとのメールを送っておきました。」
    "我发了一封邮件告诉真冬说雨停了就回去"

    # nil 「それに対する返信は」
    "真冬对此的回复是"

    # nil 「『了解だお兄ちゃんこの野郎。ダンカンバカヤロウ』」
    # 参考资料：https://www.excite.co.jp/news/article/Real_Live_1596/
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%81%9F%E3%81%91%E3%81%97%E3%81%AE%E3%83%80%E3%83%B3%E3%82%AB%E3%83%B3%E9%A6%AC%E9%B9%BF%E9%87%8E%E9%83%8E!!
    # "『收到，欧尼酱你个混蛋，邓肯这个混蛋』（L:本作发售的2013年底，这个梗指的是10年9月12号在推特上火的一个梗，在法国的一场马赛中，11区的赛马不及邓肯（马的名字）落败，于是赛马迷纷纷在推上发布“邓肯这个混蛋”的推文，谜一般的火了起来）"
    if persistent.luckykeeperSay == "shutup":
        "『收到，欧尼酱你个混蛋，邓肯这个混蛋』"
    else:
        "『收到，欧尼酱你个混蛋，邓肯这个混蛋』（L:本作发售的2013年底，这个梗指的是10年9月12号在推特上火的一个梗，在法国的一场马赛中，11区的赛马不及邓肯（马的名字）落败，于是赛马迷纷纷在推上发布“邓肯这个混蛋”的推文，谜一般的火了起来）"

    luckykeeper "现在这个时点的话，这个一般指代富士电视台周五25:20——26:20的深夜综艺节目『たけしのダンカン馬鹿野郎!!』"

    # nil 「と書いてあったので、きっと、たけしさんにハマったのでしょう。」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%93%E3%83%BC%E3%83%88%E3%81%9F%E3%81%91%E3%81%97
    # "因为上面这么写着，所以一定是迷上了北野武先生吧（L:北野武，1947年1月18日－，是日本搞笑艺人，身兼电影导演、演员、电视节目主持人，东京都足立区岛根出身，其与田森、明石家秋刀鱼并称为日本搞笑艺人三巨头）"
    if persistent.luckykeeperSay == "shutup":
        "因为上面这么写着，所以一定是迷上了北野武先生吧"
    else:
        "因为上面这么写着，所以一定是迷上了北野武先生吧（L:北野武，1947年1月18日－，是日本搞笑艺人，身兼电影导演、演员、电视节目主持人，东京都足立区岛根出身，其与田森、明石家秋刀鱼并称为日本搞笑艺人三巨头）"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ごく……ごく……ごく……」
    show 心愛_制服_基本_もぐもぐ at love69_right with dissolve
    voice "voice/心愛/cca_a1_0774.ogg"
    ai 心愛_制服_基本_もぐもぐ "唔……咕…咕……"
    hide 心愛_制服_基本_不機嫌

    # 莲 「な、なぁ…心愛」
    lian "呐，呐…心爱"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ごく…ぷはー。はーい、なんでしょう」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0775.ogg"
    ai 心愛_制服_基本_笑顔 "唔……呼啊——嗯？怎么啦"
    hide 心愛_制服_基本_もぐもぐ

    # 莲 「一つ言っていか？」
    lian "我能说个事吗"

    # 心爱 「うんうん、なーに？」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_0776.ogg"
    ai 心愛_制服_基本_嬉しい "嗯嗯，是什么捏"
    hide 心愛_制服_基本_笑顔

    # 莲 「共食いだろ。お前がコア飲んだら」
    # lian "你这是同类相食吧，喝了冰核的话（L:还是刚才的谐音梗，饮料的冰核(ice core的core）和心爱(cocoa)）"
    if persistent.luckykeeperSay == "shutup":
        lian "你这是同类相食吧，喝了冰核的话"
    else:
        lian "你这是同类相食吧，喝了冰核的话（L:还是刚才的谐音梗，饮料的冰核(ice core的core）和心爱(cocoa)）"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ぶふっ」
    show 店长_私服_不満_1 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0172.ogg"
    dinerowner 店长_私服_不満_1 "噗噗"
    hide 店长_私服_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「だからー！　そのネタ引っ張り起こさないの！　さっきそれで大変な思いしたんだから！」
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0777.ogg"
    ai 心愛_制服_基本_不機嫌 "所以啊！不要把那个段子提起来啊！刚才我就觉得很牙白了！"
    hide 心愛_制服_基本_嬉しい

    # 莲 「大変な思いってなんだね」
    lian "那真是很辛苦呢"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「せっかく、我慢してたのに…く、く…あは！」
    show 店长_私服_微笑み_1 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0173.ogg"
    dinerowner 店长_私服_微笑み_1 "好不容易忍住了……哈哈、啊哈哈哈哈"
    hide 店长_私服_不満_1

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「これ」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0778.ogg"
    ai 心愛_制服_基本_真顔 "这个"
    hide 心愛_制服_基本_不機嫌

    # 莲 「ごめん」
    lian "对不起"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 霧葉ちゃんのお店 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「で」
    lian "呐"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「はい」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0174.ogg"
    dinerowner 店长_私服_無表情 "嗯？"

    # 莲 「さっき突っ込み忘れたけど、なんでピアノなんかあるんだ？前来た時なかったぞ」
    lian "刚才忘记吐槽了，为什么这里会有钢琴呢？上次来的时候记得没有来着"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「友達から貰ったんだってさ」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_0779.ogg"
    ai 心愛_制服_基本_嬉しい "听说是从朋友那里得到的"

    # 莲 「へー。店長、弾けんの？」
    lian "啊~店长，你不弹弹嘛？"

    # 心爱 「いや、店長さんは楽器類は扱えないんだって。強いて言えば、『女』ならい音奏でられるってさ』
    voice "voice/心愛/cca_a1_0780.ogg"
    ai 心愛_制服_基本_嬉しい "不，店长不擅长乐器。硬要说的话，她会演奏出『女人』风格的音乐"

    # 莲 「それじゃさぞかし良い声で鳴くんでしょうね貴方」
    lian "那你一定会用很好的声音叫出来吧"

    # 心爱 「試してみる？」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0781.ogg"
    ai 心愛_制服_基本_真顔 "你要试试吗？"
    hide 心愛_制服_基本_嬉しい

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「全部心愛ちゃんが答えちゃいましたね…しかも余計な所まで。あと男性はお断りします」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0175.ogg"
    dinerowner 店长_私服_目閉じ "全部都是由心爱酱回答的呢……而且还有点多余了，还有我拒绝男性……"
    hide 店长_私服_無表情

    # 莲 「心愛」
    lian "心爱"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「らじゃ」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_0782.ogg"
    ai 心愛_制服_基本_嬉しい "收到！"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「え…」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0176.ogg"
    dinerowner 店长_私服_微笑み "欸……"
    hide 店长_私服_目閉じ

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 霧葉ちゃんのお店 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「そうか、さっきは演奏中に邪魔しちまったな」
    lian "是吗，刚才在演奏中打扰了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「うん。まさか蓮くんが現れるなんて思ってなくて、ビックリしただけだよー」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_0783.ogg"
    ai 心愛_制服_基本_嬉しい "没有没有，我没想到莲君会出现，只是吓了一跳而已"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「噂をすればなんとや―モゴッ！」
    show 店长_私服_本気 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0177.ogg"
    dinerowner 店长_私服_本気 "说曹操曹操——呜唔!"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あーあーきこえなーい！」
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0784.ogg"
    ai 心愛_制服_基本_不機嫌 "啊ー啊ー我听不到!"
    hide 心愛_制服_基本_嬉しい

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「もご、モゴゴゴゴッ！　もごごごごご！」
    voice "voice/霧葉/krh_a1_0178.ogg"
    # %&^ 不支持，阔以用日语中的符号代替
    dinerowner 店长_私服_本気 "！＠＃＄％＾＆＊＊＆＾％＄＃＠！"

    # 莲 「あの、心愛ちゃん」
    lian "那个，心爱酱"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「なんでしょう蓮くん！」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0785.ogg"
    ai 心愛_制服_基本_笑顔 "怎么啦莲君"
    hide 心愛_制服_基本_不機嫌

    # 莲 「口と鼻を押さえるのはやめてあげなさい。店長さん苦しそうだから」
    lian "别再捂着嘴和鼻子了，店长看起来很痛苦的样子"

    # 心爱 「あっ」
    show 心愛_制服_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0786.ogg"
    ai 心愛_制服_基本_驚き "啊"
    hide 心愛_制服_基本_笑顔

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ぶはぁっ！　本格的に口封じするつもりですか…」
    voice "voice/霧葉/krh_a1_0179.ogg"
    dinerowner 店长_私服_本気 "哇啊！你真的打算封口吗…"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 霧葉ちゃんのお店 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「しっかし…心愛がピアノを弾くなんて久しぶりだよな…」
    lian "啊说起来……心爱好久没弹过钢琴了捏……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「そだねー。ついつい白熱しちゃったよ」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_0787.ogg"
    ai 心愛_制服_基本_嬉しい "是啊，不知不觉就有点上头了呢"

    # 莲 「リクエストしてもいか？」
    lian "我可以点个歌吗？"

    # 心爱 「えっ！？　い、いけど…？」
    show 心愛_制服_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0788.ogg"
    ai 心愛_制服_基本_驚き "欸！？倒是可以的说……？"
    hide 心愛_制服_基本_嬉しい

    # 莲 「月光で」
    # 应该是这首：https://www.youtube.com/watch?v=iyw6-KVmgow
    # 参考资料：https://www.zhihu.com/question/22301553
    # lian "月光（L:鬼束ちひろ - 月光，说的是这首，YTB上面有，阔以去听一下，歌手鬼束千寻是神秘派歌姬，整首歌的歌词比较压抑和诡异，不过旋律还是可以的）"
    if persistent.luckykeeperSay == "shutup":
        lian "月光"
    else:
        lian "月光（L:鬼束ちひろ - 月光，说的是这首，YTB上面有，阔以去听一下，歌手鬼束千寻是神秘派歌姬，整首歌的歌词比较压抑和诡异，不过旋律还是可以的）"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「店の空気が暗くなるんでダメです」
    show 店长_私服_不満 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0180.ogg"
    dinerowner 店长_私服_不満 "店里的气氛会变暗的所以不行"

    # 莲 「ぶええ」
    lian "呜欸欸"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぶええ」
    show 心愛_制服_基本_ぶわー at love69_right with dissolve
    voice "voice/心愛/cca_a1_0789.ogg"
    ai 心愛_制服_基本_ぶわー "呜欸欸"
    hide 心愛_制服_基本_驚き

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「…泣かれてもダメです。他の曲にしてください」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0181.ogg"
    dinerowner 店长_私服_微笑み "……哭也不行，请换成别的曲子"
    hide 店长_私服_不満

    # 莲 「じゃぁ…」
    lian "那么…"

    # 场景切换：心爱弹琴
    image bg ccg01_4_2 = "images/ev/ccg01_4_2.png"
    scene ccg01_4_2 with dissolve

    # nil 「ということで、さっきは心愛の演奏を邪魔してしまったので、改めて、心愛ちゃんにピアノを弾いて貰う事にしました。」
    "因此，刚才打扰了心爱的演奏，所以决定让心爱酱再此演奏起来"

    # nil 「店長特製のノンアルコールのカクテルをグラスに注いで貰い、カウンターテーブルに座る。」
    "店长特制的软性饮料鸡尾酒倒进杯子里，我坐在吧台前"

    # nil 「心愛は先ほどとは打って変わって、緊張した様子でピアノの前に座っている。肩もこちこちだ。」
    "心爱与刚才截然不同，紧张地坐在钢琴前，肩膀也很僵硬"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「えー…こほん。う゛～蓮くんに見られてると思うと緊張するよぉ…」
    voice "voice/心愛/cca_a1_0790.ogg"
    ai 心愛_制服_基本_泣き "呃…咳咳，嗯~一想到被莲君看到就很紧张啊…"

    # 莲 「でも嬉しいよ、俺、なんかわかんねぇけどお前のピアノ好きだからな」
    # lian "但是我很高兴，虽然我不知道为什么，但是我喜欢你的钢琴"
    lian "但是我很高兴，虽然不知道为什么，但是我很喜欢你弹琴的样子"

    # 心爱 「だ、だからー！　そーいう事言わないの！　恥ずかしいから！」
    voice "voice/心愛/cca_a1_0791.ogg"
    ai 心愛_制服_基本_不機嫌 "所、所以——! 不要这么说! 因为太害羞了!"

    # 莲 「は。なんか、小さかった頃の発表会を思い出すよ。あの頃のお前、ピアノ弾くの嫌がってたよな。何で好きになったんだっけ」
    lian "那个，总觉得，我想起了小时候的发表会。那个时候的你，讨厌弹钢琴吧。现在为什么会喜欢上呢？"

    # 心爱 「（それは君が今さっき言った台詞を、その時も言ったからでしょうが～！）」
    voice "voice/心愛/cca_a1_0792.ogg"
    ai 心愛_制服_基本_不機嫌 "（那是因为你刚才说的台词啊，那个时候也说了吧～！）"

    # 心爱 「と、とにかく、弾きますからね！」
    voice "voice/心愛/cca_a1_0793.ogg"
    ai 心愛_制服_基本_不機嫌 "总之，我会弹的！"

    # 莲 「おう」
    lian "请"

    # nil 「心愛は深呼吸して、鍵盤を叩き始める。」
    # "心爱深吸一口气，开始敲击键盘"
    "心爱深吸一口气，开始敲击琴键"

    scene ccg01_2_1 with dissolve
    play music bgmfortytwo fadein 2.0 fadeout 1.0
    $ renpy.notify("BGM:あの夏rock1111")

    # 心爱闭眼，音乐是开场的变奏曲，超好听的！！！
    # 暂时不更了，听会儿心爱酱的钢琴
    # nil 「アップテンポなポップスを心愛は弾き始めた。こんな曲も弾けたのか…。」
    # "心爱开始弹奏快节奏的流行音乐。原来你也会弹这样的曲子...（L:这个歌是本作作曲/作词的cittan*的あの夏まで…(new)背景音乐的变奏，原歌曲也非常好听，本项目Demo版中结尾用的就是原歌）"
    if persistent.luckykeeperSay == "shutup":
        "心爱开始弹奏快节奏的流行音乐。原来你也会弹这样的曲子..."
    else:
        "心爱开始弹奏快节奏的流行音乐。原来你也会弹这样的曲子...（L:这个歌是本作作曲/作词的cittan*的あの夏まで…(new)背景音乐的变奏，原歌曲也非常好听，本项目Demo版中结尾用的就是原歌）"

    # nil 「俺はノンアルコールのカクテルをすりながら、俺は心愛の演奏に聴き入っていた。」
    "我一边喝着店长特调的软性饮料鸡尾酒，一边听着心爱的演奏"

    # nil 「心愛は普段の様子とは裏腹に、割と何でも出来る子だ。」
    "与平时的样子相反，心爱是个什么都能做到的孩子"

    # nil 「心幼い頃は、何事にも不器用で、よく、ずんどこべろんちょしたものだ。」
    "小时候，对什么事情都很笨拙，经常笨手笨脚的"

    # nil 「それでも、俺と真冬の後ろを、いつも健気に追いかけてきた。」
    "尽管如此，在我和真冬的身后，她总是很勇敢地追赶着"

    # nil 「いつのまにか、俺が心愛の背中を追いかけるような事もあるようになってきた。」
    "但是，不知不觉中，我开始追逐心爱的背影了"

    # nil 「俺は、鍵盤に向かい合う心愛の姿を見つめながら、あの日の心愛の姿を思い出す。」
    # "我一边凝视着面向键盘的心爱的身姿，一边想起那天的心爱的身姿"
    "我一边凝视着面向琴键的心爱的身姿，一边想起那天的心爱的身姿"

    # nil 「身体を重ねた時の心愛は、甘えん坊であって、どこか包み込んでくれるような優しさもあって。」
    # "当身体重叠时，心爱是个爱撒娇的孩子，也有着包容别人的温柔"
    "当身体互相交织在一起时，心爱是个爱撒娇的孩子，也有着包容别人的温柔"

    # nil 「心愛は会う度に、いろんな顔や表情を見せてくれる。」
    "每次见面，都会让我们看到各种各样的表情和神情"

    # nil 「分裂しているようで、でも、芯は一筋で。」
    # "好像有点分裂的感觉，但是，核心是一条线："
    "虽然让人觉得有点分裂，但是，不管是怎么样的心爱："

    # nil 「俺と真冬は、そんな心愛が大好きだった。」
    # "我和真冬最喜欢那样的心爱了"
    "我和真冬都最喜欢了"

    # nil 「まだ小さい頃、泣いてしまった真冬にお菓子を与えて、ピアノの演奏をして慰めたエピソードを思い出す。」
    "我想起了小时候，给哭了的真冬点心，演奏钢琴来安慰她的事情"

    # nil 「心愛の演奏を聞いていると、なんだかよくわからないが、心温かい気持ちになれる。」
    "听着心爱的演奏，虽然不太清楚为什么，但是总感觉很温暖"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ふ、優しい顔になってますよ」
    voice "voice/霧葉/krh_a1_0182.ogg"
    dinerowner 店长_私服_微笑み "欸嘿嘿，表情看起来很温柔呢"

    # 莲 「あ…あ…色々、思い出しちまってな」
    lian "啊…啊…各种各样的事情，我都想起来了"

    # 店长 「良い思い出ですか？」
    voice "voice/霧葉/krh_a1_0183.ogg"
    dinerowner 店长_私服_微笑み "是美好的回忆吗？"

    # 莲 「うむ。　しかし、これ美味いな…もう一杯くれないか」
    lian "嗯，不过，这个很好喝啊……再给我一杯吧"

    # 店长 「かしこまりました」
    voice "voice/霧葉/krh_a1_0184.ogg"
    dinerowner 店长_私服_微笑み "遵命"

    # nil 「演奏に合わせて、店長がシェイカーを振る。妙に様になってるのが悔しい。」
    "随着音乐的演奏，店长挥舞着振动器（Shakers），我很后悔自己变得这么奇怪"

    # nil 「俺も、気づけばカウンターテーブルの上においた人差し指でリズムを刻んでいる。」
    "回过神来，我发现自己也在用放在柜台桌子上的食指打着节奏"

    # nil 「我ながら、らしくない時間の過ごし方だと思ったが、存外、悪くない。」
    "连我自己都觉得这种打发时间的方式很不像样，但是，没想到感觉还真不错"

    # nil 「なんだろう。演奏とノンアルとはいえ、このアダルティな空気にあてられたのか、」&&协力请求
    "到底是什么呢？虽然是演奏配上不含酒精的软饮料这种不会上瘾的东西，但是还是被这种气氛所吸引了吧"

    # nil 「心なしか体温があがってきたように感じる。」
    "也许是心理作用，我感觉体温升高了"

    # nil 「心愛も緊張がほぐれてきたのか、リラックスして弾けているようだ。」
    "也许是因为演奏歌曲的心爱也放松了下来，所以我的心情也随之放松了"

    # nil 「そして、その音色からは、心愛の気持ちが伝わってくるようで、幸福感が溢れてくる。」
    "而且，从音调之中，似乎可以感受到心爱的心情，充满了幸福感"

    # nil 「それと同時に、「また、心愛と繋がりたい」という気持ちも沸き立ってくる。」
    "与此同时，「还想与心爱联系在一起」的心情也逐渐沸腾起来"

    # nil 「ついちょっと前に、真冬としておきながら、このザマとは…我ながら恥ずかしくなる。」
    "就在不久之前，我居然还在和真冬做那样的事情...连我自己都觉得很丢脸"

    # 店长 「お待たせ致しました。スカイダイビングです」
    voice "voice/霧葉/krh_a1_0185.ogg"
    # dinerowner 店长_私服_にっこり "让您久等了，这是 Sky Diving （L:是一种鸡尾酒）"
    if persistent.luckykeeperSay == "shutup":
        dinerowner 店长_私服_にっこり "让您久等了，这是 Sky Diving"
    else:
        dinerowner 店长_私服_にっこり "让您久等了，这是 Sky Diving （L:是一种鸡尾酒）"

    # 莲 「あ、ありがとう」
    lian "啊，谢谢啦"

    # nil 「邪な感情を抑え込むために、ピアノリフに合わせて一気にグラスを空にする。」
    "为了抑制自己的邪恶情绪，我配合着钢琴曲一口气将玻璃杯喝空了"

    # 莲 「くはぁー！　効くぅ～。ノンアルとはおもえんね、こりゃ」
    lian "哇哈——！很棒啊，我不觉得是不含酒精的，这个"

    # nil 「ドキドキドキドキ」
    "dokidoki dokidoki"

    # nil 「まるで曲のＢＰＭかのように、鼓動が高鳴っていく。」
    # "简直就像歌曲的BPM一样，心跳不断地高涨起来（L:玩音游（比如OSU！）的应该都知道BPM，简单来说就是衡量音乐节奏的数值，数值越大节奏越快）"
    if persistent.luckykeeperSay == "shutup":
        "简直就像歌曲的BPM一样，心跳不断地高涨起来（L:玩音游（比如OSU！）的应该都知道BPM，简单来说就是衡量音乐节奏的数值，数值越大节奏越快）"
    else:
        "简直就像歌曲的BPM一样，心跳不断地高涨起来"
        
    # nil 「飲み干したのは逆効果だったか、より、俺の心はヒートアップしてしまった。」
    "也许是适得其反吧，我的心情更加激动了"

    stop music fadeout 4.0
    scene ccg01_3_2 with dissolve

    # nil 「心愛が最後の一小節を弾き終えた。」
    "心爱弹完了最后一小节"

    # 莲 「Bravo——！」
    # lian "Bravo——！（L:西班牙语棒极了的意思，现在在英语中也常用）"
    if persistent.luckykeeperSay == "shutup":
        lian "Bravo——！"
    else:
        lian "Bravo——！（L:西班牙语棒极了的意思，现在在英语中也常用）"

    # nil 「二人分の拍手と俺の歓声が、店内に響き渡る。」
    "两个人的掌声和我的欢呼声响彻店内"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「えへ…ご静聴ありがとうございました…」
    voice "voice/心愛/cca_a1_0794.ogg"
    ai 心愛_制服_基本_嬉しい "嗯…感谢您的聆听……"

    # 场景切回店内
    scene 霧葉ちゃんのお店 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)
    play music bgmfifteen fadein 4.0
    $ renpy.notify("BGM:jonay_-_want_you_to_know")

    # nil 「発表会のように、心愛は椅子から立ち上がりぺこりとお辞儀した。ほんのり、頬を赤くしている。」
    "就像发布会一样，心爱从椅子上站起来深深鞠了一躬。她的脸颊微微泛红"

    # 莲 「やっぱり、心愛のピアノはさいこ…お…お？」
    lian "果然，心爱的钢琴最棒了！…喔——哦？"

    # nil 「ぐらっ」
    "啊咧"

    # nil 「世界が揺れる。鼓動が最高潮に達していく。」
    "整个世界都在震动，我的心跳达到了最高潮"

    # nil 「次の瞬間。」
    "下一个瞬间"

    # nil 「バタァン！」
    "扑通！"

    # nil 「俺の身体が床に投げ出された。」
    "我的身体倒在了地板上"

    # nil 「そして…。」
    "然后…"

    # nil 「くかー…」
    "呼——……"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「寝ちゃった」
    show 店长_私服_無表情 at love69_wuye_right with dissolve
    voice "voice/霧葉/krh_a1_0186.ogg"
    dinerowner 店长_私服_無表情 "睡着了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ね、てんちょーさん…もしかして…これ…」
    show 心愛_制服_基本_ジト目 at love69_xinai_left with dissolve
    voice "voice/心愛/cca_a1_0795.ogg"
    ai 心愛_制服_基本_ジト目 "喂，店长桑…难道说…这个是……"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「あっ。二杯目、普通のリキュール使っちゃいましたね…」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%AA%E3%82%AD%E3%83%A5%E3%83%BC%E3%83%AB
    show 店长_私服_不満 at love69_wuye_right with dissolve
    voice "voice/霧葉/krh_a1_0187.ogg"
    # dinerowner 店长_私服_不満 "啊，第二杯，用的是普通的利口酒呢…（L:利口酒是一种使用蒸馏酒为原料的酒精饮料，以水果、坚果、草药、香料、花朵以及奶油增强酒水风味，在装瓶前通常会添加蔗糖或甜味剂，大多数利口酒的酒精浓度比烈酒低，在15-30％，但有的利口酒的酒精浓度也高达55％）"
    if persistent.luckykeeperSay == "shutup":
        dinerowner 店长_私服_不満 "啊，第二杯，用的是普通的利口酒呢…"
    else:
        dinerowner 店长_私服_不満 "啊，第二杯，用的是普通的利口酒呢…（L:利口酒是一种使用蒸馏酒为原料的酒精饮料，以水果、坚果、草药、香料、花朵以及奶油增强酒水风味，在装瓶前通常会添加蔗糖或甜味剂，大多数利口酒的酒精浓度比烈酒低，在15-30％，但有的利口酒的酒精浓度也高达55％）"

    hide 店长_私服_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「もー！　蓮君はお酒めっちゃ弱いんだよー！　初詣の御神酒ですら寝ちゃうのに！」
    show 心愛_制服_基本_驚き at love69_xinai_left with dissolve
    voice "voice/心愛/cca_a1_0796.ogg"
    ai 心愛_制服_基本_驚き "啊——！莲君的酒力太弱了！明明连喝新年参拜的御神酒都睡着了！"

    # 心爱 「あうあうあー。蓮くーん、起きて～！　ぺちぺちぺちぺちぺち」
    show 心愛_制服_基本_ぶわー at love69_xinai_left with dissolve
    voice "voice/心愛/cca_a1_0797.ogg"
    ai 心愛_制服_基本_ぶわー "啊呜啊呜啊——莲君，快起来~！啪唧啪唧啪唧啪唧！"
    hide 心愛_制服_基本_驚き

    # nil 「くかー…」
    "呃……"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 霧葉ちゃんのお店 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「雨、止みましたね」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0188.ogg"
    dinerowner 店长_私服_無表情 "雨、停下来了呢"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「でも、蓮君寝てるし…もうちょっと居て良い？」
    show 心愛_制服_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0798.ogg"
    ai 心愛_制服_基本_泣き "但是，莲君睡着了…可以再呆一会儿吗？"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ごゆっくりどうぞ」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0189.ogg"
    dinerowner 店长_私服_微笑み "请慢用"
    hide 店长_私服_無表情

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 霧葉ちゃんのお店 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あむ」
    show 心愛_制服_基本_もぐもぐ at love69_right with dissolve
    voice "voice/心愛/cca_a1_0799.ogg"
    ai 心愛_制服_基本_もぐもぐ "哈姆"

    # 莲 「はうあ！」
    lian "哈啊！"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「あ、起きた」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0190.ogg"
    dinerowner 店长_私服_無表情 "啊，起来了"

    # nil 「耳たぶに生暖かい湿った感覚を感じて俺は一気に意識を覚醒させた。」
    "我感觉到耳垂有一种温暖而湿润的感觉，意识一下子清醒了起来"

    # 店长 「耳ペロが寝坊助さんにこんなに効果があるとは…」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0191.ogg"
    dinerowner 店长_私服_目閉じ "没想到耳朵pr对睡懒觉的人有这么大的效果…"
    hide 店长_私服_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はあぅ～…ハズカシカッターヨ…」
    show 心愛_制服_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0800.ogg"
    ai 心愛_制服_基本_泣き "哈呜~~……好羞耻的说……"
    hide 心愛_制服_基本_もぐもぐ

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「よしよし」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0192.ogg"
    dinerowner 店长_私服_微笑み "好啦好啦"
    hide 店长_私服_目閉じ

    # 莲 「真冬に習った技をつかったな貴様…」
    lian "你这招是从真冬那儿学的吧……"

    # nil 「俺は寝ぼけた頭を横に振りながら、上体を起こす。辺りはすっかり暗くなってしまっていた。」
    "我摇摇迷糊糊的脑袋，坐起身来。天已经完全黑了"

    # nil 「何か知らんけど、身体のいろんな所が痛い。」
    "虽然不知道是怎么回事，但是身体的各个地方都很痛"

    # nil 「というか、なんかテーブルの上にバールのようなものとか、ドリルとか色々置いてある。」
    "怎么说呢，桌子上放着一些撬棍啊，钻头之类的东西"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ラストオーダーの時間ですよ」
    voice "voice/霧葉/krh_a1_0193.ogg"
    dinerowner 店长_私服_微笑み "到了最后点餐的时间了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ほんと何しても起きないよね蓮くん…舐める以外で」
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0801.ogg"
    ai 心愛_制服_基本_不機嫌 "真的无论做什么都不会起来啊莲君……除了舔之外"
    hide 心愛_制服_基本_泣き

    # 莲 「んあ…え、何、そんな寝てたの俺」
    lian "嗯…啊，什么，我睡得那么香啊"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「うん。さっき、まふまふちゃんから電話来て、夕飯どうするの？　って言ってたから、店長さんが電話とって、お兄ちゃん、酒飲んで寝てるよって言ったんで、そしたら―」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_0802.ogg"
    ai 心愛_制服_基本_嬉しい "嗯。刚才嘛呼嘛呼酱打电话来，问晚饭怎么办，店长在电话里说哥哥喝了酒在睡觉，然后——"
    hide 心愛_制服_基本_不機嫌

    # nil 「『二回ほどぶん殴って、それでも起きなかったら、夕飯は食べてきてって伝えといて』」
    # 这里应该放真冬（电话）或者是心爱的，但是原作就是放的旁白
    "『把他暴打两顿，即使那样也不起来的话，就告诉他吃完晚饭再回来』"

    # 莲 「だろ」
    lian "果然"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「おー流石真冬ちゃんのお兄ちゃん！」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0803.ogg"
    ai 心愛_制服_基本_笑顔 "哇~不愧是真冬酱的欧尼酱！"
    hide 心愛_制服_基本_嬉しい

    # 莲 「あ、そっか。心愛も一緒って言ってないのか」
    lian "啊，这样啊。没有说心爱也在一起吗？"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「あ、そうですね。私が電話とっちゃったので」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0194.ogg"
    dinerowner 店长_私服_無表情 "啊，是啊，是我接的电话"
    hide 店长_私服_微笑み

    # 莲 「あちゃー…真冬怒らせちゃったかな」
    lian "哎呀——……我是不是惹真冬生气了"

    # 店长 「んー…『お兄ちゃんにお酒飲まさないでね』って穏やかに言ってましたから、怒ってる要素ではありませんでしたね」
    voice "voice/霧葉/krh_a1_0195.ogg"
    dinerowner 店长_私服_無表情 "啊…因为她很平静地说『别让欧尼酱喝酒啊』，所以并不是生气的样子"

    # 莲 「あれ？　ていうか、アンタ真冬と知り合いなの？」
    lian "咦？话说，你认识真冬吗？"

    # 店长 「え、まぁ」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0196.ogg"
    dinerowner 店长_私服_微笑み "嗯，是啊"
    hide 店长_私服_無表情

    # 莲 「いつのまに…抜け目ないな、あんたも真冬も」
    # 参考资料：https://www.weblio.jp/content/%E6%8A%9C%E3%81%91%E7%9B%AE%E3%81%8C%E3%81%AA%E3%81%84
    lian "你什么时候…和真冬都这么聪明啊"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「私は！」
    show 心愛_制服_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0804.ogg"
    ai 心愛_制服_基本_驚き "我呢！"
    hide 心愛_制服_基本_笑顔

    # 莲 「どっちかっというと抜けてる方だな…」
    lian "你康起来就是个脱线的人啊……"

    # 心爱 「ぐぬぬ…」
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0805.ogg"
    ai 心愛_制服_基本_不機嫌 "咕奴奴奴……"
    hide 心愛_制服_基本_驚き

    # 莲 「じゃぁ、なんだ、心愛は夕飯食べたの？」
    lian "那个，那什么，心爱吃晚饭了吗？"

    # 心爱 「あ、いや、蓮君を待っていようかと思いまして」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_0806.ogg"
    ai 心愛_制服_基本_嬉しい "啊，还没，我想等莲君"
    hide 心愛_制服_基本_不機嫌

    # 莲 「あじゃぁ、それまで店長さんに遊んでもらったのか。よかったなーよーしよしよしよしよし」
    lian "那么，在这之前店长陪你玩了? 太好了呢!来摸摸摸摸摸摸！"

    # 心爱 「わーい、なでなでされちゃっ…ってバカにしてるでしょ！寝ぼけやがって…酔っぱらいが…」
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0807.ogg"
    ai 心愛_制服_基本_不機嫌 "哇——咿！被摸摸头啦……喂，你在瞧不起我吧！睡眼惺忪…一个醉鬼……"
    hide 心愛_制服_基本_嬉しい

    # 莲 「唐突に口悪くなるよなお前」
    lian "你这就有点口无遮拦了啊"

    # 心爱 「で、せっかくなら晩ご飯こで食べちゃおうって思ったんだけど、蓮君全然起きないので、最後の手段をとりました」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_0808.ogg"
    ai 心愛_制服_基本_嬉しい "于是，好不容易来一起吃一次晚饭，莲君却完全不起来，所以采取了最后的手段"
    hide 心愛_制服_基本_不機嫌

    # 莲 「あーそうか。それは悪い事したな…ありがとう、心愛。ついでに、このテーブルに置いてある鈍器の数々は？」
    lian "啊，是这样啊，那真是太糟糕了，谢谢你，心爱。顺便问一下，这张桌子上放着的一堆钝器是什么？"

    # 心爱 「真冬ちゃんが二回ほどぶん殴れつったから…」
    show 心愛_制服_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0809.ogg"
    ai 心愛_制服_基本_泣き "因为真冬酱让我们胖揍两顿来着……"
    hide 心愛_制服_基本_嬉しい

    # 莲 「だから、身体のあちこちいてぇのか…」
    lian "所以，现在身体各处才……"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ちなみに一人二回ずついきました」
    voice "voice/霧葉/krh_a1_0197.ogg"
    dinerowner 店长_私服_微笑み "顺便说一下，每人都揍了两次"

    # 莲 「永眠しちゃうよ！？」
    lian "我会永眠的！？"

    # 店长 「それでお客様。ご注文は？」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0198.ogg"
    dinerowner 店长_私服_無表情 "那么客人。您要点些什么？"
    hide 店长_私服_微笑み

    # 莲 「じゃぁこの、シカゴブルズステーキって奴で」
    lian "那么，这个叫芝加哥烤牛排的家伙"

    # 店长 「かしこまりました」
    show 店长_私服_にっこり at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0199.ogg"
    dinerowner 店长_私服_にっこり "遵命"
    hide 店长_私服_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「私は！」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0810.ogg"
    ai 心愛_制服_基本_笑顔 "我也要！"
    hide  心愛_制服_基本_泣き

    # 莲 「おいおい３００グラムのステーキなんぞ食えるのか」
    lian "喂，你能吃下３００克的牛排吗？"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「はい。少々お待ち下さい」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0200.ogg"
    dinerowner 店长_私服_微笑み "好的，请稍等"
    hide 店长_私服_にっこり

    # 莲 「もうなんでも有りだなこの店。」
    lian "这家店什么都有"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 霧葉ちゃんのお店 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぺろりんちょしました。グリルされた牛の肩ロースに…ほんのりとジャックダニエル風味がまた…良いですね！」&&协力请求
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%B8%E3%83%A3%E3%83%83%E3%82%AF%E3%83%80%E3%83%8B%E3%82%A8%E3%83%AB
    show 心愛_制服_基本_ペコちゃん at love69_right with dissolve
    voice "voice/心愛/cca_a1_0811.ogg"
    # ai 心愛_制服_基本_ペコちゃん "吃了不少东西呢。烤好的牛肩里脊…再加上一点杰克丹尼酒…真不错呢！（L:原版字就缺了一半，剩下的内容应该是「这个，Jack Daniel，fxxk！」。杰克丹尼（Jack Daniel's）是著名的美国威士忌品牌）"
    if persistent.luckykeeperSay == "shutup":
        ai 心愛_制服_基本_ペコちゃん "吃了不少东西呢。烤好的牛肩里脊…再加上一点杰克丹尼酒…真不错呢！"
    else:
        ai 心愛_制服_基本_ペコちゃん "吃了不少东西呢。烤好的牛肩里脊…再加上一点杰克丹尼酒…真不错呢！（L:原版字就缺了一半，剩下的内容应该是「这个，Jack Daniel，fxxk！」。杰克丹尼（Jack Daniel's）是著名的美国威士忌品牌）"

    # 莲 「俺まだ半分も食いきってねえぞ！？」
    lian "我还没吃完一半呢！？"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「そば湯置いときますね」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0201.ogg"
    dinerowner 店长_私服_無表情 "我去弄点儿荞麦汤"

    # 莲 「何に使うねん」
    lian "拿来干啥子咧"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 霧葉ちゃんのお店 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「えー、今日は長々と一日ありがとうございました、ぺこり」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_0812.ogg"
    ai 心愛_制服_基本_嬉しい "嗯——今天谢谢大家这么长时间的照顾，真是太好了呢"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「いえいえ、私も楽しかったですし、また来て下さいね。こんどは真冬ちゃんも一緒に」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0202.ogg"
    dinerowner 店长_私服_微笑み "不不不，我也玩的很开心，请下次再来，下次也和真冬一起带过来哦"

    # 莲 「そうさせてもらうよ、ありがとう店長さん」
    lian "我会的，谢谢你，店长"

    # 店长 「あっ。ちょっと待って下さいね。お土産を渡しますよ」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0203.ogg"
    dinerowner 店长_私服_目閉じ "啊，请稍等，我把特产给你"
    hide 店长_私服_微笑み

    # nil 「店長は一度店の奥に消えて、手提げの紙箱を持って現れた。」
    "店长消失在店里，拿着一个纸盒出来了"

    # 店长 「これお土産のケーキです。真冬ちゃんにも食べさせてあげてくださいね」
    show 店长_私服_にっこり at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0204.ogg"
    dinerowner 店长_私服_にっこり "这是特产蛋糕，请拿回去给真冬恰吧"
    hide 店长_私服_目閉じ

    # 莲 「お、ありがとう。心愛。全部食べるなよ」
    lian "哦，谢谢。心爱。不要全部吃完哦"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「う、うん。蓮くんの分まで我慢しとく」
    show 心愛_制服_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0813.ogg"
    ai 心愛_制服_基本_泣き "嗯，嗯，连同莲君的份也要忍耐下来呢"
    hide 心愛_制服_基本_嬉しい

    # 莲 「俺にも食わせろ！」
    lian "我的那份别给我吃啊！"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「二人分しか入ってないですよ？」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0205.ogg"
    dinerowner 店长_私服_微笑み "里面只放了两人份哦？"
    hide 店长_私服_にっこり

    # 莲 「悪鬼め～！」
    lian "魔鬼~！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「じゃぁ、半分こしよう！　…とでもこの私が言うと思ったか？」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0814.ogg"
    ai 心愛_制服_基本_真顔 "那么，一人一半吧！…你以为我会这么说吗？"
    hide 心愛_制服_基本_泣き

    # 莲 「それは心配に及ばない、期待してねぇ」
    lian "这不用担心，我不指望"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「あは、さてさて、仲良く気をつけて帰って下さいね？」
    show 店长_私服_にっこり at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0206.ogg"
    dinerowner 店长_私服_にっこり "啊哈哈，那么，回去的时候要好好注意哦？"
    hide 店长_私服_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はーい！　ばいばーい！」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0815.ogg"
    ai 心愛_制服_基本_笑顔 "好——~bye——bye！"
    hide 心愛_制服_基本_真顔

    # nil 「CLOSEの札のかったドアの前で、心愛と並んでお辞儀をする。」
    "在挂着“CLOSE”牌的门前，和心爱并排向店主辞别"

    # nil 「店主の女性は俺達に微笑み返して、閉店作業のとりかるため、店の奥へと消えていった。」
    "女店主对我们报以微笑，然后消失在店里，准备打烊"

    stop music fadeout 4.0

    # scene07 场景2 【说曹操曹操到】 结束
    # scene07 场景3 【和心爱的归家路】 开始
    # 小场景的名称
    $ partName = " 【和心爱的归家路】"
    $ changeTitleName()
    
    # 地点： 雾叶小店->通学路街道（夜）
    # 人物： 心爱 莲
    # BGM： 无
    image bg 通学路c_夜 = "images/bg/通学路c_夜.png"
    scene 通学路c_夜 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ふあーすっかり夜になっちゃったねー」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0816.ogg"
    ai 心愛_制服_基本_嬉しい "呼啊，已经完全到晚上了呢"

    # 莲 「いやーほんと、待たせてすまなかった」
    lian "哎呀，真的是呢，对不起让你久等了"

    # 心爱 「いのいの。さんざん楽しませてもらったしね！」
    voice "voice/心愛/cca_a1_0817.ogg"
    ai 心愛_制服_基本_嬉しい "没事的没事的，我玩得很开心呢！"

    # 莲 「んあ？　貴様、無防備な俺に何かしやがりましたか」
    lian "嗯？你对毫无防备的我做了什么吗？"

    # 心爱 「ひみつー！　にやにや」
    show 心愛_制服_基本_微笑み at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0818.ogg"
    ai 心愛_制服_基本_微笑み "是秘密！嘻嘻"
    hide 心愛_制服_基本_嬉しい

    # 莲 「ならば力尽くでも」
    lian "那么就算我尽全部力气也可以吧"

    # 心爱 「ホンゲェー！あ、ほらほら蓮君見て見て！」
    show 心愛_制服_基本_ポカーン at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0819.ogg"
    ai 心愛_制服_基本_ポカーン "疼呀！啊，那里那里莲君快看快看"
    hide 心愛_制服_基本_微笑み

    # 莲 「その手は乗らぬ」
    lian "我不会上当的"

    # 心爱 「いから！」
    show 心愛_制服_基本_不機嫌 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0820.ogg"
    ai 心愛_制服_基本_不機嫌 "好 了 啦！"
    hide 心愛_制服_基本_ポカーン

    # 莲 「ん？」
    lian "嗯？"

    # 画面切换到天空
    image bg 天の川 = "images/bg/天の川.png"
    scene 天の川 at love69_bg1440 with dissolve

    # 心爱 「星がこんなに出てるなんて珍しいね！」
    voice "voice/心愛/cca_a1_0821.ogg"
    ai 心愛_制服_基本_嬉しい "星星出来这么多真是少见啊！"

    # 莲 「おー。そうだな、雨で排気ガスとかが洗い流されたんかな」
    lian "哦。是啊，是不是因为下雨把灰尘都洗掉了呢？"

    # 心爱 「あ！！」
    voice "voice/心愛/cca_a1_0822.ogg"
    ai 心愛_制服_基本_驚き "哦！！"

    # 莲 「どうした？」
    lian "怎么了？"

    # 心爱 「蓮君みてなかった！？」
    voice "voice/心愛/cca_a1_0823.ogg"
    ai 心愛_制服_基本_泣き "莲君你没看到吗！？"

    # 莲 「何を？」
    lian "啥？"

    # 心爱 「流れ星だよー！　すっごいすっごい！」
    voice "voice/心愛/cca_a1_0824.ogg"
    ai 心愛_制服_基本_笑顔 "是流星啊！好厉害好厉害！"

    # 莲 「まじかよ。もう一回流れないかな。そしたら願い事すんのにな」
    lian "真的吗？那能不能再来一次？这样我就能许愿了"

    # 心爱 「何を？」
    voice "voice/心愛/cca_a1_0825.ogg"
    ai 心愛_制服_基本_真顔 "你说什么？"

    # 莲 「んー秘密」
    lian "嗯——秘密"

    # 心爱 「ならば力尽くでも！」
    voice "voice/心愛/cca_a1_0826.ogg"
    ai 心愛_制服_基本_真顔 "那我也尽全部力气吧！"

    # 莲 「ホンゲェー！」
    lian "啊呀！"

    # 莲 「あ！」
    lian "啊！"

    # 心爱 「その手は乗らぬ！」
    voice "voice/心愛/cca_a1_0827.ogg"
    ai 心愛_制服_基本_真顔 "我不会上当的!"

    # 莲 「ちゃうちゃう！　もう一発流れ星流れたんだって！」
    lian "不是！又有一颗流星已经划过去了！"

    # 心爱 「え、マジで！？　もー！　余計な事しよってからに！罰として、願い事を言いなさい」
    voice "voice/心愛/cca_a1_0828.ogg"
    ai 心愛_制服_基本_不機嫌 "啊，真的！？真是的！别多管闲事了！作为惩罚，请说出你的愿望"

    # 莲 「えー。じゃぁその後お前の願い事も教えてくれよ」
    lian "嗯——那之后也告诉我你的愿望吧"

    # 心爱 「だめだ」
    voice "voice/心愛/cca_a1_0829.ogg"
    ai 心愛_制服_基本_真顔 "不行"

    # 莲 「もう一度言ってみろ」
    lian "你再说一遍"

    # 心爱 「だめだ」
    voice "voice/心愛/cca_a1_0830.ogg"
    ai 心愛_制服_基本_真顔 "不行"

    # 莲 「なんでや」
    lian "为什么呢？"

    # 心爱 「なんでも」
    voice "voice/心愛/cca_a1_0831.ogg"
    ai 心愛_制服_基本_無表情 "不为什么"

    # 莲 「じゃぁ俺も言わない」
    lian "那我也不说了"

    # 莲&心爱 「あ」
    # 也要记得去人物表加人
    voice "voice/心愛/cca_a1_0832.ogg"
    lian_ai 心愛_制服_基本_驚き "哦"

    # 莲 「（どうか、もっと真冬と心愛が幸せになれますように）」
    lian "（请一定要让真冬和心爱变得更加幸福）"

    # 心爱 「（どうか、もっと蓮くんと真冬ちゃんが幸せになれますように）」
    voice "voice/心愛/cca_a1_0833.ogg"
    ai 心愛_制服_基本_にっこり "（请一定要让莲君和真冬酱更加幸福）"

    # 莲 「願えたか？」
    lian "许愿了吗？"

    # 心爱 「なんとか」
    voice "voice/心愛/cca_a1_0834.ogg"
    ai 心愛_制服_基本_真顔 "勉强吧"

    # 莲&心爱 「『なぁ（ねぇ）』」
    # 没有配音
    lian_ai "『呐（那个）』"

    # 莲 「お先にどうぞ」
    lian "你先说吧"

    # 心爱 「蓮くんからどうぞ」
    voice "voice/心愛/cca_a1_0835.ogg"
    ai 心愛_制服_基本_真顔 "莲君先说吧"

    # 莲 「レディファーストだ」
    lian "女士优先"

    # 心爱 「やだー」
    voice "voice/心愛/cca_a1_0836.ogg"
    ai 心愛_制服_基本_不機嫌 "亚哒——"

    # 莲 「むー」
    lian "那么"

    # nil 「俺は星空から、心愛の方顔に視線を移す。ちょうど同じタイミングで、心愛も俺の方へ視線を向ける。」
    "我的视线从星空移向心爱的方向。正好在同一时间，心爱也把目光投向我"

    # nil 「ドンピシャで、視線が交差してしまう。」
    # 参考资料：https://www.weblio.jp/content/%E3%83%89%E3%83%B3%E3%83%94%E3%82%B7%E3%83%A3
    # "don-pitchari（L:指时机和期望都恰到好处的情况），视线交叉了"
    if persistent.luckykeeperSay == "shutup":
        "don-pitchari，视线交叉了"
    else:
        "don-pitchari（L:指时机和期望都恰到好处的情况），视线交叉了"

    # 莲 「今日さ、うち、来ないか？」
    lian "今天啊，我家，要来吗？"

    # 心爱 「…うんっ」
    voice "voice/心愛/cca_a1_0837.ogg"
    ai 心愛_制服_基本_にっこり "…嗯"

    # nil 「恥ずかしくなって、もう一度二人で夜空を見上げる。」
    "感到害羞，两个人再次仰望夜空"

    # 心爱 「いこっか」
    voice "voice/心愛/cca_a1_0838.ogg"
    ai 心愛_制服_基本_笑顔 "出发吧"

    # 莲 「そうだな」
    lian "是啊"

    # nil 「ぎゅっ。」
    # 直译是“紧紧地”，但是和下文说不过去
    "然后"

    # nil 「心愛から、そっと手を握ってきた。指と指を絡め合う恋人繋ぎだ。」
    "心爱轻轻地握住我的手。是十指交缠的恋人握法"

    # nil 「俺もそっと心愛の小さな手を握り返す。」
    "我也轻轻回握住心爱的小手"

    # nil 「足はゆっくりと進み始めていたが、視線を前に戻すのはもう少し時間がかりそうだ。」
    "虽然脚开始慢慢地前进，但视线回到前面似乎还需要一些时间"

    # 画面切回街道
    scene 通学路c_夜 at love69_bg1440 with dissolve

    # 心爱 「あ、ケーキちゃんと3個入ってるじゃん」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0839.ogg"
    ai 心愛_制服_基本_嬉しい "啊，里面不是有3个蛋糕吗?"

    # 莲 「で、お前は何を言おうとしたの」
    lian "那么，你想说什么捏？"

    # 心爱 「ん？　なにが？　さっきの？」
    show 心愛_制服_基本_驚き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0840.ogg"
    ai 心愛_制服_基本_驚き "嗯？什么？刚才那个？"
    hide 心愛_制服_基本_嬉しい

    # 莲 「うん」
    lian "嗯"

    # 心爱 「秘密」
    show 心愛_制服_基本_にっこり at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0841.ogg"
    ai 心愛_制服_基本_にっこり "秘密"
    hide 心愛_制服_基本_驚き

    # 莲 「3回目はだめだ」
    lian "第三次也不行吗"

    # 心爱 「むー」
    show 心愛_制服_基本_不機嫌 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0842.ogg"
    ai 心愛_制服_基本_不機嫌 "嗯——"
    hide 心愛_制服_基本_にっこり

    # 心爱 「…」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0843.ogg"
    ai 心愛_制服_基本_真顔 "……"
    hide 心愛_制服_基本_不機嫌

    # 心爱 「笑わない？」
    show 心愛_制服_基本_不機嫌 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0844.ogg"
    ai 心愛_制服_基本_不機嫌 "不会笑吗？"
    hide 心愛_制服_基本_真顔

    # 莲 「多分」
    lian "大概"

    # 心爱 「多分じゃやだ！」
    voice "voice/心愛/cca_a1_0845.ogg"
    ai 心愛_制服_基本_不機嫌 "不要大概！"

    # 莲 「じゃぁ笑わない」
    lian "那我就不笑了"

    # 心爱 「じゃあ言う」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0846.ogg"
    ai 心愛_制服_基本_真顔 "那么我说了"
    hide 心愛_制服_基本_不機嫌

    # 心爱 「…」
    voice "voice/心愛/cca_a1_0847.ogg"
    ai 心愛_制服_基本_真顔 "……"

    # 莲 「…」
    lian "……"

    # 心爱 「今日、家、行って良い…？　って」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0848.ogg"
    ai 心愛_制服_基本_泣き "今天、你家、可以……去…吗？"
    hide 心愛_制服_基本_真顔

    # 莲 「ぷっ」
    lian "噗"

    # 心爱 「貴っ様ァア！　やはりケーキは私が食らいつくしてやるからな！」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0849.ogg"
    ai 心愛_制服_基本_真顔 "你这混蛋！果然我要把蛋糕全部吃光！"
    hide 心愛_制服_基本_泣き

    # 莲 「ホンゲェー！」
    lian "真是的！"

    # nil 「ちなみに心愛ちゃんは誘惑に耐えきれず、家につくまえにケーキをマジで2個平らげました。」
    "顺便一提，心爱酱经不住诱惑，在到家之前真的吃掉了两块蛋糕"

    # scene07 场景3 【和心爱的归家路】 结束
    # scene07 结束！
    # 今天Star过10，果然动力超强！一天肝了100多行，直接结束scene07，好耶！

    # 过场：心爱（常服）

    # 隐藏 quick_menu
    $ quick_menu = False

    play sound "voice/effect/moosehead honk (stinger).ogg"

    scene black
    scene アイキャッチ心愛 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)

    $ renpy.pause(1.5, hard=True)
    $ renpy.end_replay()

    jump scene08

# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene11 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：
# 版本 0.8 "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年3月31日

# 当前流程：编写脚本AIO Process

label scene11:
    # scene11 开始

    # scene11 场景1 【6人大集合，现在是女子会时间！】 开始

    # 地点：null/湛蓝天空
    # 人物：真冬
    # BGM：无

    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)
    scene 空 at love69_bg1440 with dissolve

    # 显示 quick_menu
    $ quick_menu = True

    # nil 「そして…あれから…三日ぐらい経ちました。」
    "然后…在那之后…大概过去了三天"

    # nil 「真冬です。」
    "我是真冬"

    # nil 「夏休みに入り三日三晩。お兄ちゃんと心愛ちゃんとエッチ三昧です。」
    "放暑假之后的三天三夜，和欧尼酱还有心爱一直在H"

    # nil 「我ながら健康的だな…なんて穿った見方をしてしまいます。」
    "连我自己都觉得这很健康……会有这样的看法真是不可思议呢"

    # nil 「そしてついに、本日、お兄ちゃんはガス欠を起こしたので、一日ぐらいゆっくり寝かせてあげようかと思います。」
    "最后，今天，欧尼酱终于被榨干了，今天就让他好好睡上一天吧"

    # nil 「心愛ちゃんはというと…」
    "说到心爱酱……"

    # 画面切换到雾叶小店
    # 人物：心爱 真冬 店长（雾叶）

    play music bgmfifteen fadeout 2.0 fadein 2.0
    scene 霧葉ちゃんのお店 with dissolve

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「てんちょー！　パンケーキおかわり！」
    ## 没有跳过
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1422.ogg"
    ai 心愛_制服_基本_笑顔 "店长！再来一份薄煎饼！"

    # nil 「全然元気です。」
    "非常元气呢"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「何枚目？」
    ## 没有跳过
    show 真冬_制服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_1113.ogg"
    dong 真冬_制服_基本_無表情 "第几张了？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「忘れた！」
    show 心愛_制服_基本_もぐもぐ at love69_right with dissolve
    voice "voice/心愛/cca_a1_1423.ogg"
    ai 心愛_制服_基本_もぐもぐ "忘记了！"
    hide 心愛_制服_基本_笑顔

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「はいはい。沢山食べておっぱい膨らますんですよ」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0219.ogg"
    dinerowner 店长_私服_目閉じ "好的好的。吃了这么多，欧派会鼓起来的"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「いえーい！　実はこの三日間でちょっとバストサイズ上がったんだよー！」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1424.ogg"
    ai 心愛_制服_基本_嬉しい "好耶！其实在过去的三天里我的欧派有增加一点儿呢！"
    hide 心愛_制服_基本_もぐもぐ

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「沢山揉まれてるからね」
    show 真冬_制服_基本_ニタァ at love69_center with dissolve
    voice "voice/真冬/maf_a1_1114.ogg"
    dong 真冬_制服_基本_ニタァ "因为被揉了很多呢"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぶええええ」
    show 心愛_制服_基本_ぶわー at love69_right with dissolve
    voice "voice/心愛/cca_a1_1425.ogg"
    ai 心愛_制服_基本_ぶわー "呜欸欸欸欸"
    hide 心愛_制服_基本_嬉しい

    # nil 「心愛ちゃんと一緒に水着を買って、その帰りにおやつ兼女子会に、例のアメリカンダイナーにやってきました。」
    "和心爱酱一起买了泳衣，然后回家的路上为了恰点心兼开女子会，去了那个美式的diner"

    # nil 「実は、心愛ちゃんと来るのは初めてです。」
    "其实，这是我第一次和心爱酱一起来"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「どなたに揉まれてるんでしょうね。くすくす」
    show 店长_私服_ニヤリ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0220.ogg"
    dinerowner 店长_私服_ニヤリ "谁能来揉揉我的呢？嘿嘿"
    hide 店长_私服_目閉じ

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そ、それは…まぁ…」
    show 真冬_制服_基本_泣き at love69_center with dissolve
    voice "voice/真冬/maf_a1_1115.ogg"
    dong 真冬_制服_基本_泣き "这、这个…嘛……"
    hide 真冬_制服_基本_ニタァ

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「はいはい。可愛い可愛い。真冬ちゃんは何か食べますか？」
    show 店长_私服_ニヤリ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0221.ogg"
    dinerowner 店长_私服_ニヤリ "好啦好啦，真可爱真可爱，真冬酱要恰点儿什么嘛？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「いの？」
    show 真冬_制服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_1116.ogg"
    dong 真冬_制服_基本_無表情 "可以吗？"
    hide 真冬_制服_基本_泣き
    hide 店长_私服_ニヤリ with dissolve

    # 想瑠喵在左的参数
    transform love69_xiangliu_left:
        zoom 1.5
        xalign -0.11
        yalign 0.07

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「おーう、今日は私のおごりだからな～！　たーんと食って飲むんだぞ～！　うい～！　きぃちゃん！　酒！　と　おっぱい！　げへ！」
    show 想瑠_スーツ_見下し at love69_xiangliu_left with dissolve
    voice "voice/想瑠/sol_a1_0159.ogg"
    liu 想瑠_スーツ_見下し "哦——，今天是我请客的啦~！好好吃好好喝啊~！好欸嘿嘿！好棒！这酒！欧派！欸嘿嘿！"
    # liu 想瑠_スーツ_見下し "哦——，今天是我请客的啦~！好好吃好好喝啊~！好欸嘿嘿！好棒！这酒！欧派！欸嘿嘿🤤🤤🤤！"
    # 坏了，🤤🤤🤤 渲染不出来，生艹的程度降低了！
    hide 想瑠_スーツ_見下し with dissolve

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「Suck on my shoes！」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0222.ogg"
    dinerowner 店长_私服_無表情 "Suck on my shoes！（L:意思是来舔我的鞋吧！）"
    hide 店长_私服_無表情 with dissolve

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ぶへぁー！」
    show 想瑠_スーツ_ぶわ at love69_xiangliu_left with dissolve
    voice "voice/想瑠/sol_a1_0160.ogg"
    liu 想瑠_スーツ_ぶわ "咕呀——！"

    # nil 「偶然にも、店長の友達で私達の担任の想瑠にゃんも遊びにきていました。」
    "碰巧，店长的朋友，我们的班主任想瑠喵也来玩了"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「じゃぁ、アイス貰えるかな」
    show 真冬_制服_基本_微笑み at love69_center with dissolve
    voice "voice/真冬/maf_a1_1117.ogg"
    dong 真冬_制服_基本_微笑み "那么，能给我冰淇淋吗？"
    hide 真冬_制服_基本_無表情
    hide 想瑠_スーツ_ぶわ with dissolve

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「かしこまりました。実は最近、新しいアイスを入荷しましてね…是非食べて貰いたいな…と…はいっ」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0223.ogg"
    dinerowner 店长_私服_目閉じ "遵命。其实最近，我们进了一批新的冰淇淋……希望你务必能尝尝呢……来……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「わ…おいしそ…」
    show 真冬_制服_基本_嬉しい at love69_center with dissolve
    voice "voice/真冬/maf_a1_1118.ogg"
    dong 真冬_制服_基本_嬉しい "哇…看起来很好吃…"
    hide 真冬_制服_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「わー！　てんちょーさん私にもちょーだい！」
    show 心愛_制服_基本_きらきら at love69_right with dissolve
    voice "voice/心愛/cca_a1_1426.ogg"
    ai 心愛_制服_基本_きらきら "哇——！店长桑~给我也整一个！"
    hide 心愛_制服_基本_ぶわー

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「はいはい、そのつもりですよっと…さぁ、召し上がれ」
    voice "voice/霧葉/krh_a1_0224.ogg"
    dinerowner 店长_私服_目閉じ "好好，我就是这么打算的……来，请品尝吧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「わーい！」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1427.ogg"
    ai 心愛_制服_基本_笑顔 "哇——咿！"
    hide 心愛_制服_基本_きらきら

    # nil 「私と心愛ちゃんの前にカクテルグラスの上に置かれたアイスクリームが出されました。」
    "摆在我和心爱酱面前的是放在鸡尾酒杯上的冰淇淋"

    # nil 「ターコイズブルーが爽やかな印象を抱かせてくれます。」
    "绿松石蓝的颜色给人以清新的印象"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「あむ…美味し…優しい味…まふ」
    show 真冬_制服_基本_まったり at love69_center with dissolve
    voice "voice/真冬/maf_a1_1119.ogg"
    dong 真冬_制服_基本_まったり "啊…好吃…温柔的味道…嘛呼"
    hide 真冬_制服_基本_嬉しい

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「もぐもぐもぐもぐ。美味しいにゃー！」
    show 心愛_制服_基本_もぐもぐ at love69_right with dissolve
    voice "voice/心愛/cca_a1_1428.ogg"
    ai 心愛_制服_基本_もぐもぐ "嗯嗯嗯嗯，真好恰喵——！"
    hide 心愛_制服_基本_笑顔

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ニヤリ」
    show 店长_私服_ニヤリ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0225.ogg"
    dinerowner 店长_私服_ニヤリ "哈"
    hide 店长_私服_目閉じ

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ん？」
    show 真冬_制服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_1120.ogg"
    dong 真冬_制服_基本_無表情 "嗯？"
    hide 真冬_制服_基本_まったり

    # nil 「今、一瞬、霧葉さんが含みのある笑みを浮かべたような…。」
    "现在，一瞬间，雾叶露出了含蓄的笑容…"

    hide 真冬_制服_基本_無表情 with dissolve

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「きぃーりぃーはちゃぁーん！　私にもアイスちょうだいよー！　リキュールをどばーっとかけてな！」
    show 想瑠_スーツ_ニヤリ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0161.ogg"
    liu 想瑠_スーツ_ニヤリ "雾~叶~叶~酱！也给我个冰淇淋吧！再往里加一勺利口酒！"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「少しは休んだらどうなんですか…昔みたいにケツに飴でもぶっさしてやりましょうか？」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0226.ogg"
    dinerowner 店长_私服_無表情 "稍微休息一下怎么样……就像以前那样往你的屁股塞上一块糖？"
    hide 店长_私服_ニヤリ

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「来いよ！　へいへい！　さぁ！　ぶち込んでみせろ！」
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0162.ogg"
    liu 想瑠_スーツ_見下し "来吧！嘿嘿！上吧！给我淦进去！"
    hide 想瑠_スーツ_ニヤリ

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「せい」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0227.ogg"
    dinerowner 店长_私服_目閉じ "嘿"
    hide 店长_私服_無表情

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ぐわぁー！」
    show 想瑠_スーツ_驚き at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0163.ogg"
    liu 想瑠_スーツ_驚き "哇啊——！"
    hide 想瑠_スーツ_見下し

    # 想瑠 「……」
    show 想瑠_スーツ_ぶわ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0164.ogg"
    liu 想瑠_スーツ_ぶわ "……"
    hide 想瑠_スーツ_驚き

    # 想瑠 「きゅぅ～」
    hide 想瑠_スーツ_ぶわ
    show 想瑠_スーツ_ぶわ:
        zoom 1.5
        xalign 0.41
        yalign 0.07
        linear 0.3 yalign -5.0
    voice "voice/想瑠/sol_a1_0165.ogg"
    liu "Q~~~"
    hide 想瑠_スーツ_ぶわ

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「厄介な担任を持って大変ですね、二人とも」
    voice "voice/霧葉/krh_a1_0228.ogg"
    dinerowner 店长_私服_目閉じ "有个麻烦的班主任很辛苦啊，你们两个"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「いやいやーこう見えても良い先生だよ？　ね！」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1429.ogg"
    ai 心愛_制服_基本_笑顔 "没有没有——看起来是个好老师吧？对吧！"
    hide 心愛_制服_基本_もぐもぐ

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「真面目に仕事しないけどね。でも、たまーにかっこい所はあるよ」
    show 真冬_制服_基本_微笑み at love69_center with dissolve
    voice "voice/真冬/maf_a1_1121.ogg"
    dong 真冬_制服_基本_微笑み "虽然不认真工作，但偶尔也会有很酷的地方"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「それはそれは…。で、どこまで聞きましたっけ？　二人と…彼との関係は」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0229.ogg"
    dinerowner 店长_私服_無表情 "这倒也是这倒也是……欸，刚才问到哪里了？两个人和……和他的关系是？"
    hide 店长_私服_目閉じ

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「全部説明しなきゃ、だめ？」
    show 真冬_制服_基本_泣き at love69_center with dissolve
    voice "voice/真冬/maf_a1_1122.ogg"
    dong 真冬_制服_基本_泣き "不全部说明的话，不行吗？"
    hide 真冬_制服_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「もぐもぐもぐ…てんちょーさんが聞きたいところって、ぶっちゃけピンポイントでしょー？」
    show 心愛_制服_基本_もぐもぐ at love69_right with dissolve
    voice "voice/心愛/cca_a1_1430.ogg"
    ai 心愛_制服_基本_もぐもぐ "咀嚼咀嚼咀嚼……店长桑想听的话，直截了当地说就是那个吧？"
    hide 心愛_制服_基本_笑顔

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「そんなそんな、そこまで下世話じゃないですよ」
    show 店长_私服_ニヤリ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0230.ogg"
    dinerowner 店长_私服_ニヤリ "怎么可能，我没那么下流"
    hide 店长_私服_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「まだ何も言ってないのにー！　どうせエッチな話を期待してるんだな！」
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1431.ogg"
    ai 心愛_制服_基本_不機嫌 "我还什么都没说呢！反正你就是在期待瑟琴的故事吧！"
    hide 心愛_制服_基本_もぐもぐ

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まふ…」
    show 真冬_制服_基本_まったり at love69_center with dissolve
    voice "voice/真冬/maf_a1_1123.ogg"
    dong 真冬_制服_基本_まったり "嘛呼……"
    hide 真冬_制服_基本_泣き

    # nil 「私だけでしょうか、何故か、心愛ちゃんの赤くなってる姿を見るとドキドキします。」
    "只有我是这样吗？不知道为什么，当我看到心爱酱脸红的时候，我就会心跳加速"

    # 真冬 「（心愛ちゃんに…触れたい…）」
    show 真冬_制服_基本_微笑み at love69_center with dissolve
    voice "voice/真冬/maf_a1_1124.ogg"
    dong 真冬_制服_基本_微笑み "（心爱酱……想去触摸）"
    hide 真冬_制服_基本_まったり

    # nil 「そんな衝動に駆られ、私の手は心愛ちゃんの髪に伸びていきます。」
    "在这种冲动的驱使下，我的手伸向了心爱酱的头发"

    # 想瑠喵在最右的参数
    transform love69_xiangliu_rightest:
        zoom 1.5
        xalign 1.28
        yalign 0.07

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「イッヒッヒ…私ぃ～も興味あるぞぉー…貴様らからは色々な汁の匂いがぷんぷんすんぜぇ…もごっ！」
    show 想瑠_スーツ_見下し at love69_xiangliu_rightest with dissolve
    voice "voice/想瑠/sol_a1_0166.ogg"
    liu 想瑠_スーツ_見下し "嘻嘻…我啊~也很有兴趣啊…你们身上散发出各种各样的汤的味道啊…呜咕！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「！」
    show 真冬_制服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_1125.ogg"
    dong 真冬_制服_基本_無表情 "！"
    hide 真冬_制服_基本_微笑み

    # nil 「伸びていたはずの、想瑠にゃんが起き上がって、私達の背後に迫ってきました。」
    "本应该在地上伸展开来的想瑠喵爬了起来，向向我们的背后逼近"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「想瑠にゃん！　め！」
    voice "voice/心愛/cca_a1_1432.ogg"
    ai 心愛_制服_基本_不機嫌 "想瑠喵！哈！"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「心愛ちゃん、鼻に三本指は流石に…」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0231.ogg"
    dinerowner 店长_私服_無表情 "心爱酱，在鼻孔里插了三根手指真不愧是……"
    hide 店长_私服_ニヤリ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あ」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1433.ogg"
    ai 心愛_制服_基本_真顔 "啊"
    hide 心愛_制服_基本_不機嫌

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ぷはぁっ…！　相変わらず照準のズレたお嬢さんだ…。大体指を突っ込むのは鼻じゃなくてもっと下って相場が決まってんだがな…」
    voice "voice/想瑠/sol_a1_0167.ogg"
    liu 想瑠_スーツ_見下し "噗啊啊…！你还是一如既往的瞄不准的大小姐啊…大概你手指插进去的不是鼻子，而是下面的某个地方……"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「最後に突っ込まれたのはいつです？」
    show 店长_私服_ニヤリ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0232.ogg"
    dinerowner 店长_私服_ニヤリ "你最后一次被插进去是什么时候？"
    hide 店长_私服_無表情

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「10分前かな、自分で突っ込んだ」
    voice "voice/想瑠/sol_a1_0168.ogg"
    liu 想瑠_スーツ_見下し "10分钟前吧，我自己插进去了"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「死ねばいのに」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0233.ogg"
    dinerowner 店长_私服_目閉じ "死了好了"
    hide 店长_私服_ニヤリ

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「マジな目で見るなよ！　ジョークだからジョーク！」
    show 想瑠_スーツ_驚き at love69_xiangliu_rightest with dissolve
    voice "voice/想瑠/sol_a1_0169.ogg"
    liu 想瑠_スーツ_驚き "别用“这是真的”眼神看我啊！这是玩笑啊玩笑！"
    hide 想瑠_スーツ_見下し

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「じゃぁ実際は？」
    voice "voice/心愛/cca_a1_1434.ogg"
    ai 心愛_制服_基本_真顔 "那实际上是？"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「昨日の夜です…姉に…無理矢理…」
    show 想瑠_スーツ_ぶわ at love69_xiangliu_rightest with dissolve
    voice "voice/想瑠/sol_a1_0170.ogg"
    liu 想瑠_スーツ_ぶわ "昨天晚上……被姐姐…强迫……"
    hide 想瑠_スーツ_驚き

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「良かったじゃないですか、ご無沙汰じゃなくて」
    # 参考资料：https://domani.shogakukan.co.jp/508197
    show 店长_私服_ニヤリ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0234.ogg"
    dinerowner 店长_私服_ニヤリ "不是挺好的吗，真是好久不见了"
    hide 店长_私服_目閉じ

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「まだまだ私だって若いわよ！　さすがに、ちょっと色恋とかは現役引退かなーって感じてきてるけどさー」
    # 参考资料：https://www.weblio.jp/content/%E3%81%A1%E3%82%87%E3%81%A3%E3%81%A8
    show 想瑠_スーツ_見下し at love69_xiangliu_rightest with dissolve
    voice "voice/想瑠/sol_a1_0171.ogg"
    liu 想瑠_スーツ_見下し "我明明还很年轻呢！不过，我现在也开始觉得恋爱什么的果然还是在一点点从现役引退啊"
    hide 想瑠_スーツ_ぶわ

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ぽー…」
    show 真冬_制服_基本_目閉じ_1 at love69_center with dissolve
    voice "voice/真冬/maf_a1_1126.ogg"
    dong 真冬_制服_基本_目閉じ_1 "呼…"
    hide 真冬_制服_基本_無表情

    # 真冬 「はっ、そういえば、ちょっと前に想瑠にゃん、自分の恋愛について教えてくれるって言ってたよね」
    show 真冬_制服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_1127.ogg"
    dong 真冬_制服_基本_無表情 "啊，这么说来，之前想瑠喵说过要告诉我关于自己的恋爱经历吧"
    hide 真冬_制服_基本_目閉じ_1

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「あ？　んだよ…記憶力良いなまふまふちゃん」
    voice "voice/想瑠/sol_a1_0172.ogg"
    liu 想瑠_スーツ_見下し "啊？是啊……你的记忆力真不错啊嘛呼嘛呼酱"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「まふ」
    show 心愛_制服_基本_もぐもぐ at love69_right with dissolve
    voice "voice/心愛/cca_a1_1435.ogg"
    ai 心愛_制服_基本_もぐもぐ "嘛呼"
    hide 心愛_制服_基本_真顔

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「まふ」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0235.ogg"
    dinerowner 店长_私服_微笑み "嘛呼"
    hide 店长_私服_ニヤリ

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まふ」
    show 真冬_制服_基本_まったり at love69_center with dissolve
    voice "voice/真冬/maf_a1_1128.ogg"
    dong 真冬_制服_基本_まったり "嘛呼"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「まふ」
    show 想瑠_スーツ_ニヤリ at love69_xiangliu_rightest with dissolve
    voice "voice/想瑠/sol_a1_0173.ogg"
    liu 想瑠_スーツ_ニヤリ "嘛呼"
    hide 想瑠_スーツ_見下し

    # 想瑠 「で…ま、いか。私は君ら二人と似たようなもんだよ。実の兄と双子の姉と出来てるってわけ。もう二年前かなーあの頃は、色々悩んだよ。そうだよな、霧葉ちゃん」
    show 想瑠_スーツ_見下し at love69_xiangliu_rightest with dissolve
    voice "voice/想瑠/sol_a1_0174.ogg"
    liu 想瑠_スーツ_見下し "这……嘛，算了？我和你们两个也挺相似。其实我也有哥哥和双胞胎姐姐。大概是两年前吧。那个时候，我也有很多烦恼。是这样吧，雾叶酱"
    hide 想瑠_スーツ_ニヤリ

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「え、そうですね。私は一年前に、姉への思いがですね…」
    voice "voice/霧葉/krh_a1_0236.ogg"
    dinerowner 店长_私服_微笑み "啊，是这样的呢，我一年前对姐姐的感情啊……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あ、それで…素直になりきれずに～みたいな話だったわけなのね」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1436.ogg"
    ai 心愛_制服_基本_真顔 "啊，然后……是不能坦诚相待的事情"
    hide 心愛_制服_基本_もぐもぐ

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「はい。今はとっても仲良しですよ？」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0237.ogg"
    dinerowner 店长_私服_目閉じ "是啊，不过现在关系很好哦？"
    hide 店长_私服_微笑み

    # nil 「カランコロンカラーン♪」
    "叮当叮当叮当♪"
    play sound "/voice/effect/カウベル.ogg"

    # 雾叶的姐姐，ATRI 初登场！
    # 定义亚十礼在最左的参数
    transform love69_atri_leftest:
        zoom 1.5
        xalign -0.135
        yalign -0.295

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「やっほー！　あっそびにきったよーん！」
    ## 音声接花盆君
    show アシュリー_私服_にっこり at love69_atri_leftest with dissolve
    voice "voice/アシュリー/ash_a1_0042.ogg"
    atri アシュリー_私服_にっこり "Yahoo~！我来找你玩儿啦！"

    hide 想瑠_スーツ_見下し with dissolve

    # 定义瑠那在最右的参数
    transform love69_liuna_rightest:
        zoom 1.5
        xalign 1.27
        yalign -0.01

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「おーっす。おやつだよ！全員しゅーごー！　のご様子ですかぁ？」
    ## 没有跳过
    show 瑠那_私服_にっこり at love69_liuna_rightest with dissolve
    voice "voice/瑠那/lun_a1_0006.ogg"
    na 瑠那_私服_にっこり "好耶！是点心哦！是“全员集合！”这样子的吗？"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「噂をすればなんとやら」
    voice "voice/霧葉/krh_a1_0238.ogg"
    dinerowner 店长_私服_目閉じ "说曹操曹操就到呢"

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「わ——真冬ちやんだ——！！まふまふまふまふまふ」
    voice "voice/瑠那/lun_a1_0007.ogg"
    na 瑠那_私服_にっこり "哇——是真冬酱啊——！！嘛呼嘛呼嘛呼嘛呼嘛呼"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「まふまふまふまふまふ」
    show 心愛_制服_基本_もぐもぐ at love69_right with dissolve
    voice "voice/心愛/cca_a1_1437.ogg"
    ai 心愛_制服_基本_もぐもぐ "嘛呼嘛呼嘛呼嘛呼嘛呼"
    hide 心愛_制服_基本_真顔

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「るなちー、それ心愛ちゃんだよ」
    show アシュリー_私服_無表情 at love69_atri_leftest
    voice "voice/アシュリー/ash_a1_0043.ogg"
    atri アシュリー_私服_無表情 "瑠那亲——，这是心爱酱哦"
    hide アシュリー_私服_にっこり

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「まふ」
    voice "voice/瑠那/lun_a1_0008.ogg"
    na 瑠那_私服_にっこり "嘛呼"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「まふ」
    show 店长_私服_にっこり at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0239.ogg"
    dinerowner 店长_私服_にっこり "嘛呼"
    hide 店长_私服_目閉じ

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まふまふ」
    voice "voice/真冬/maf_a1_1129.ogg"
    dong 真冬_制服_基本_まったり "嘛呼嘛"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ぐぇ」
    voice "voice/想瑠/sol_a1_0175.ogg"
    liu 想瑠_スーツ_ぶわ "咕欸"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ぺち」
    show 真冬_制服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_1130.ogg"
    dong 真冬_制服_基本_無表情 "啪唧"
    hide 真冬_制服_基本_まったり

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ぐぇ」
    voice "voice/想瑠/sol_a1_0176.ogg"
    liu 想瑠_スーツ_ぶわ "咕欸"

    # nil 「流石に6人は画面に入り切りませんでした。」
    "果然还是没办法让6个人进入画面同框啊"

    # 移出想瑠喵
    $ sideimagesize.SideImageXalign = 40.08
    $ sideimagesize.SideImageYalign = -40.35
    $ sideimagesize.SideImageZoom = 0.95

    # 想瑠 「って私がフレームアウトかよ！」
    voice "voice/想瑠/sol_a1_0177.ogg"
    liu "欸我要被挤出画面外了啊！"

    # 移出店长
    $ sideimagesize.SideImageXalign = 40.08
    $ sideimagesize.SideImageYalign = -40.35
    $ sideimagesize.SideImageZoom = 0.95

    # 店长 「私もですよ。まぁ、正直出番多かったですしね」
    hide 店长_私服_にっこり
    show 店长_私服_にっこり:
        zoom 1.5
        xalign 0.11
        yalign 0.015
        linear 0.2 xalign 2.0
    voice "voice/霧葉/krh_a1_0240.ogg"
    dinerowner "我也是。嘛，说实话出场的人还真多"

    # 移出瑠那
    $ sideimagesize.SideImageXalign = 40.08
    $ sideimagesize.SideImageYalign = -40.35
    $ sideimagesize.SideImageZoom = 0.95

    # 瑠那 「ボクも画面外だよー！」
    # L:这附近把人物的小头像做出去比较好呢，用ATL把人故意做到画面外就OK！
    hide 瑠那_私服_にっこり
    show 瑠那_私服_にっこり:
        zoom 1.5
        xalign 1.27
        yalign -0.01
        linear 0.2 xalign 3.27
    voice "voice/瑠那/lun_a1_0009.ogg"
    na "我也在画面外哦——！"

    # 移出亚十礼
    $ sideimagesize.SideImageXalign = 40.08
    $ sideimagesize.SideImageYalign = -40.35
    $ sideimagesize.SideImageZoom = 0.95

    # 亚十礼 「…あ、私も画面の外でるね！」
    hide アシュリー_私服_無表情
    show アシュリー_私服_無表情:
        zoom 1.5
        xalign -0.135
        yalign -0.295
        linear 0.2 xalign 1.865
    voice "voice/アシュリー/ash_a1_0044.ogg"
    atri "…啊，我也跑到画面外面了呢！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「無理にでなくてもいのに…」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1438.ogg"
    ai 心愛_制服_基本_真顔 "明明不用勉强也可以的……"
    hide 心愛_制服_基本_もぐもぐ

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「二人っきり…だね、心愛ちゃん」
    hide 真冬_制服_基本_無表情
    show 真冬_制服_基本_嬉しい:
        zoom 1.5
        xalign 0.5
        yalign -0.09
        linear 0.3 xalign 0.13
    voice "voice/真冬/maf_a1_1131.ogg"
    dong 真冬_制服_基本_嬉しい "只有我们两个人了……是吗，心爱酱"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「な…何その目！？　二人きりじゃないよ！？　みんないるし！」
    show 心愛_制服_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1439.ogg"
    ai 心愛_制服_基本_驚き "什…这是什么眼神！？不是只有两个人哦！？大家都在啊！"
    hide 心愛_制服_基本_真顔

    # 画面切换到看戏四人组
    image bg sdcg04a = "images/ev/sdcg04a.png"
    scene sdcg04a with dissolve

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「んー？いやね、こうやって改めて心愛ちゃんの向かいに座ると…可愛いなぁって」
    voice "voice/真冬/maf_a1_1132.ogg"
    dong 真冬_制服_基本_ニタァ "嗯？真好啊，像这样坐在心爱酱的对面…好可爱啊"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「い、いきなりなんだね！？　ちょっとちょっと！？　流石にはーずかしいよー！？」
    voice "voice/心愛/cca_a1_1440.ogg"
    ai 心愛_制服_基本_驚き "突，突然这是这么了！？等下等下！？果然还是有点不好意思呢！？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「別に大丈夫じゃない？　私達が付き合ってる事みんな知ってるんだしさー」
    voice "voice/真冬/maf_a1_1133.ogg"
    dong 真冬_制服_基本_微笑み "不是也没什么嘛？大家都知道我俩在交往的事情"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「そ、そーいう問題じゃなくて！　さ！　ほら！」
    voice "voice/心愛/cca_a1_1441.ogg"
    ai 心愛_制服_基本_驚き "不，不是这个问题！那个！你看！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「くすくす。可愛い心愛ちゃん」
    voice "voice/真冬/maf_a1_1134.ogg"
    dong 真冬_制服_基本_にっこり "嘿嘿。真可爱呢，心爱酱"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はぁぅ～…みんなのノリにあてられたんでしょー…？」
    voice "voice/心愛/cca_a1_1442.ogg"
    ai 心愛_制服_基本_不機嫌 "哈呜~……是被大家的节奏带过去了吧…？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そういえばさ、私達、付き合ってるってことは…チューしてもいんだよね？」
    voice "voice/真冬/maf_a1_1135.ogg"
    dong 真冬_制服_基本_無表情 "说起来啊，我们在交往……所以可以“啾——”一下吗？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「は、はい！？　え、えーとえーと…」
    voice "voice/心愛/cca_a1_1443.ogg"
    ai 心愛_制服_基本_驚き "哈、啊！？那、那个——那个——……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「エッチの時は沢山してるじゃん」
    voice "voice/真冬/maf_a1_1136.ogg"
    dong 真冬_制服_基本_ジト目 "H的时候不是做了很多吗？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぶえええ！　やだよーはずいよー！　みんなに知られちゃうよー！」
    voice "voice/心愛/cca_a1_1444.ogg"
    ai 心愛_制服_基本_ぶわー "呜欸欸欸！不要啊——好害羞啊——！会被大家知道的啊——！"

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「大丈夫だよー！　ボクらだってよくやってるよー！」
    voice "voice/瑠那/lun_a1_0010.ogg"
    na 瑠那_私服_にっこり "没关系的哟！我们也经常这么做的哟！"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「たまに相手を交換したり、みんなでもやりますよー！」
    voice "voice/霧葉/krh_a1_0241.ogg"
    dinerowner 店长_私服_ニヤリ "偶尔还会换下人，大家都会这么做的哦~！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あんたら価値観おかしいよ！？　アシュリーちゃんなんとかして！」
    voice "voice/心愛/cca_a1_1445.ogg"
    ai 心愛_制服_基本_驚き "真的是很奇怪的价值观哦！？亚十礼酱你也是这么想的吧！"

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「私も最初そう思ってたんだけどね…まぁ、みんな大好きだし、いかなって」
    voice "voice/アシュリー/ash_a1_0045.ogg"
    atri アシュリー_私服_にっこり "我一开始也是这么想的呢…嘛，我最喜欢大家了，所以就这样吧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「せんせーい！」
    voice "voice/心愛/cca_a1_1446.ogg"
    ai 心愛_制服_基本_ぶわー "老师！"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「勤務時間外でーす」
    voice "voice/想瑠/sol_a1_0178.ogg"
    liu 想瑠_スーツ_ニヤリ "现在是工作时间以外"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ひぎい…あぅー」
    voice "voice/心愛/cca_a1_1447.ogg"
    ai 心愛_制服_基本_ぶわー "好——吧……哈呜"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「嫌なら…しないよ…？」
    voice "voice/真冬/maf_a1_1137.ogg"
    dong 真冬_制服_基本_無表情 "如果讨厌的话…就不做了…？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「もぉー…ばかぁ…嫌なわけ…ない…じゃん…」
    voice "voice/心愛/cca_a1_1448.ogg"
    ai 心愛_制服_基本_不機嫌 "哈啊……笨蛋……讨厌……怎么可能……嘛"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「じゃぁ、心愛ちゃん。チューしよっか」
    voice "voice/真冬/maf_a1_1138.ogg"
    dong 真冬_制服_基本_微笑み "那么，心爱酱，我们来啾一下吧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「…はぁぃ。ちゅー」
    voice "voice/心愛/cca_a1_1449.ogg"
    ai 心愛_制服_基本_キス "……好，啾——"

    # 四人组瞎激动
    image bg sdcg04b = "images/ev/sdcg04b.png"
    scene sdcg04b with dissolve

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「んっ…ちゅぅ…」
    voice "voice/真冬/maf_a1_1139.ogg"
    dong 真冬_制服_基本_キス "嗯……啾…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ちゅぅ…んむっ…ちゅぅ…」
    voice "voice/心愛/cca_a1_1450.ogg"
    ai 心愛_制服_基本_キス "啾…嗯…啾……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ちゅ…んふっ…ちゅぅ…舌…出して…」
    voice "voice/真冬/maf_a1_1140.ogg"
    dong 真冬_制服_基本_キス "啾……嗯…啾……舌头…伸出来…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぁっ…やぁ…ちゅぅ…あーむ…ちゅぅ…」
    voice "voice/心愛/cca_a1_1451.ogg"
    ai 心愛_制服_基本_キス "啊…呀…呜……呜…呜……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「れる…ちゅぅ…んはぁ…ちゅぅ…んっ」
    voice "voice/真冬/maf_a1_1141.ogg"
    dong 真冬_制服_基本_キス "嗯……啾……嗯……啾……嗯"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぁぅ、んっ…ちゅぅ…は、ちゅ…んむぅ…」
    voice "voice/心愛/cca_a1_1452.ogg"
    ai 心愛_制服_基本_キス "哈呜，嗯……啾……嗯、啾……嗯……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ちゅっ…ちゅりゅ…れる…ぷはっ」
    voice "voice/真冬/maf_a1_1142.ogg"
    dong 真冬_制服_基本_キス "啾……啾……哈……啾"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「んっ…ぁ…んぅ…ぁ…ぷはぁ…はぁ…」
    voice "voice/心愛/cca_a1_1453.ogg"
    ai 心愛_制服_基本_キス "嗯…啊…嗯…啊…呜哈啊…哈啊…"

    # 心爱 「はぁ…はぁ…」
    voice "voice/心愛/cca_a1_1454.ogg"
    ai 心愛_制服_基本_キス "哈啊…哈啊…"

    # 心爱 「はぁ…ぁぅ…どうしよう…みんなに見られてるのに…こんな…」
    voice "voice/心愛/cca_a1_1455.ogg"
    ai 心愛_制服_基本_キス "啊…哈呜…怎么办…明明大家都在看…这样的…"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「この前のお返し…かな」
    voice "voice/真冬/maf_a1_1143.ogg"
    dong 真冬_制服_基本_キス "之前的回礼…对吧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「うぅ…もしかして…真冬ちゃん、興奮してる…の？」
    voice "voice/心愛/cca_a1_1456.ogg"
    ai 心愛_制服_基本_キス "呜…难道…真冬酱，在兴奋着吗？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「んー？　さぁ、どうでしょう？　くすくす」
    voice "voice/真冬/maf_a1_1144.ogg"
    dong 真冬_制服_基本_ジト目 "嗯？那么，到底是怎么回事儿？嘿嘿"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「いじわるなんだからぁ…はぁぅ…」
    voice "voice/心愛/cca_a1_1457.ogg"
    ai 心愛_制服_基本_不機嫌 "太坏心眼了啊……哈呜……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ドキドキすると、しおらしくなる心愛ちゃん可愛いよ。なでなで」
    voice "voice/真冬/maf_a1_1145.ogg"
    dong 真冬_制服_基本_微笑み "dokidoki的时候，会变得温柔的心爱酱很可爱哦。抚摸抚摸"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あー…あー…もぉ…知らないからね！」
    voice "voice/心愛/cca_a1_1458.ogg"
    ai 心愛_制服_基本_不機嫌 "啊——……哈呜……真是的……那种事情我不知道的啦！"

    # 心爱 「ちゅー！」
    voice "voice/心愛/cca_a1_1459.ogg"
    ai 心愛_制服_基本_キス "啾——！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「んっ…はぁっ…ぁんっ」
    voice "voice/真冬/maf_a1_1146.ogg"
    dong 真冬_制服_基本_キス "嗯…哈…啊"

    # 画面切回
    scene 霧葉ちゃんのお店
    show 真冬_制服_基本_キス at love69_left
    show 心愛_制服_基本_キス at love69_right
    with dissolve

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「はいそこまです」
    show 店长_私服_目閉じ at love69_wuye_center with dissolve
    voice "voice/霧葉/krh_a1_0242.ogg"
    dinerowner 店长_私服_目閉じ "好，到此为止~！"

    # nil 「パンッと手拍子が鳴って、私達二人は我に返った。」
    "击掌的声音响起，我们两个人都回过神来"

    # 店长 「マジでエッチする五秒前だったので、こでストップです」
    show 店长_私服_無表情 at love69_wuye_center with dissolve
    voice "voice/霧葉/krh_a1_0243.ogg"
    dinerowner 店长_私服_無表情 "因为真的是要到H前的5秒了，所以就到此为止了！"
    hide 店长_私服_目閉じ
    hide 店长_私服_無表情 with dissolve

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「なんだよー！　最後まで見せろよー！　あと酒！」
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0179.ogg"
    liu 想瑠_スーツ_見下し "什么啊！让我看到最后吧！酒还没喝完呢！"
    hide 想瑠_スーツ_見下し with dissolve

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「いやー…これがプライベート空間だったら、是非最後まで見たいんですけど…一人、既に暴走寸前の人がいるんで…お店が壊れちゃあれなのでー」
    show 店长_私服_目閉じ at love69_wuye_center with dissolve
    voice "voice/霧葉/krh_a1_0244.ogg"
    dinerowner 店长_私服_目閉じ "呀……如果这是私人空间的话，我一定要看到最后……有一个人，已经快要暴走了…店里会坏掉的"
    hide 店长_私服_目閉じ with dissolve

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 定义瑠那在中间的参数
    transform love69_liuna_center:
        zoom 1.5
        xalign 0.49
        yalign -0.01

    # 瑠那 「…じゅ、じゅるり…これは上物だぜ…。あしゅりん！　ちょっと唇貸して！」
    show 瑠那_私服_きらきら at love69_liuna_center with dissolve
    voice "voice/瑠那/lun_a1_0011.ogg"
    na 瑠那_私服_きらきら "……啾、啾哩哩……这可是上等货啊……啊！把嘴唇借给我！"
    hide 瑠那_私服_きらきら with dissolve

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 定义亚十礼在中间的参数
    transform love69_atri_center:
        zoom 1.5
        xalign 0.49
        yalign -0.295

    # 亚十礼 「やーめーてー！　こじゃ床も硬いし落ち着かないからだめー！」
    show アシュリー_私服_驚き at love69_atri_center with dissolve
    voice "voice/アシュリー/ash_a1_0046.ogg"
    atri アシュリー_私服_驚き "不——可——以——！因为地板又硬又冷所以不行——！"
    hide アシュリー_私服_驚き with dissolve

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「あばれんなよー！」
    show 瑠那_私服_にっこり at love69_liuna_center with dissolve
    voice "voice/瑠那/lun_a1_0012.ogg"
    na 瑠那_私服_にっこり "别乱来的啦——！"
    hide 瑠那_私服_にっこり with dissolve

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「はいはい。るなちーもうちょっと我慢してくださいねー」
    show 店长_私服_目閉じ at love69_wuye_center with dissolve
    voice "voice/霧葉/krh_a1_0245.ogg"
    dinerowner 店长_私服_目閉じ "好啦好啦，瑠那亲也请再稍微忍耐一下啦~"

    # 店长 「と、言う事で、二人とも、胸がどきどきしてたり、熱くなってたりしませんか？」
    show 店长_私服_無表情 at love69_wuye_center with dissolve
    voice "voice/霧葉/krh_a1_0246.ogg"
    dinerowner 店长_私服_無表情 "欸，这么说来，你们两个是不是都觉得dokidoki，心潮澎湃呢？"
    hide 店长_私服_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「そ、それはなるよー！　だって、みんなの前でちゅーなんかしたら、ドッキドキだよ！」
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1460.ogg"
    ai 心愛_制服_基本_不機嫌 "那，那是当然的！因为，在大家面前啾——的话，心都快跳出来了！"
    hide 心愛_制服_基本_キス

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「チューする前に、ドキドキしませんでした？」
    show 店长_私服_ニヤリ at love69_wuye_center with dissolve
    voice "voice/霧葉/krh_a1_0247.ogg"
    dinerowner 店长_私服_ニヤリ "在啾——之前，没有感觉到dokidoki嘛？"
    hide 店长_私服_無表情

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「した…かも」
    show 真冬_制服_基本_泣き at love69_left with dissolve
    voice "voice/真冬/maf_a1_1147.ogg"
    dong 真冬_制服_基本_泣き "可能……也有吧"
    hide 真冬_制服_基本_キス

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「まふまふちゃん！？」
    show 心愛_制服_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1461.ogg"
    ai 心愛_制服_基本_驚き "嘛呼嘛呼酱！？"
    hide 心愛_制服_基本_不機嫌

    # nil 「実際、私の頭は既にボルテージが上昇していました。どうやら、さっきのキスでスイッチが完全に入ってしまったようです。」
    "实际上，我的头已经升温了。显然，刚才的吻完全打开了开关"

    # nil 「なんとか、消えそうな理性をたぐり寄せて考えます。そして…一つの記憶を思い出しました。」
    "想办法思考，把快要消失的理智拉回来。然后……我想起了一段记忆"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「…あっ！　もしかして…さっきのアイス…あむっ」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1148.ogg"
    dong 真冬_制服_基本_無表情 "…啊！难道…刚才的冰淇淋…啊嗯"
    hide 真冬_制服_基本_泣き

    # nil 「私はまだ食べ残してあった、アイスクリームを口に運びます。」
    "我把还没吃完的冰淇淋送到嘴里"

    # nil 「そして思い出しました。」
    "然后我想起来了"

    # 真冬 「ラブポーション…シクスティナイン…！」
    voice "voice/真冬/maf_a1_1149.ogg"
    dong 真冬_制服_基本_無表情 "LOVEPOTION…SIXTYNINE……！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぬあ！？　あ、あのアイスがこにあるの！？」
    voice "voice/心愛/cca_a1_1462.ogg"
    ai 心愛_制服_基本_驚き "哇！？那，那个冰淇淋在这里！？"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「あちゃー、バレちゃいましたか」
    voice "voice/霧葉/krh_a1_0248.ogg"
    dinerowner 店长_私服_ニヤリ "啊，被发现了吗？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「だから…こんなに胸がどきどきするんだ…」
    show 真冬_制服_基本_嬉しい at love69_left with dissolve
    voice "voice/真冬/maf_a1_1150.ogg"
    dong 真冬_制服_基本_嬉しい "所以……我的心才会如此dokidoki的…"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「まふまふちゃんもなの！？　私もさっきから…キスする前からまふまふちゃんの事が、凄く気になって…」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1463.ogg"
    ai 心愛_制服_基本_嬉しい "嘛呼嘛呼酱也是！？我的话在刚才……开始kiss之前就对嘛呼嘛呼酱的事情，非常的在意了……"
    hide 心愛_制服_基本_驚き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「あれ、でも…これって、恋を叶えるアイスじゃ…」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1151.ogg"
    dong 真冬_制服_基本_無表情 "咦，但是…这不是实现恋爱的冰淇淋吗…"
    hide 真冬_制服_基本_嬉しい

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「バージョンエクストリームです。端的に言いますと、大好きな人と一つになりたくなる効果に改良しました。あと効果が、ゆっくりと出るように調整してありますから、お二人でラブラブデートでもしてきたらどうですか？」
    voice "voice/霧葉/krh_a1_0249.ogg"
    dinerowner 店长_私服_ニヤリ "这是Version Extreme。直截了当地说，改良成了想和喜欢的人成为一体的效果。还有，效果正在慢慢调整，所以两个人去甜蜜约会怎么样？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そう…しようかな…家に水着も置きに行かないと…だし…。心愛ちゃん、どうする？」
    voice "voice/真冬/maf_a1_1152.ogg"
    dong 真冬_制服_基本_無表情 "这样啊……怎么办呢…还得回家放泳衣才行……哎…心爱酱，怎么办呢？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ん…だって、このアイス、満足するまで効果切れないんだよね…？なら、もう楽しむしかない…じゃん？」
    show 心愛_制服_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1464.ogg"
    ai 心愛_制服_基本_泣き "嗯…但是，这个冰淇淋在满足之前效果是不会消失的吧…？那就只有享受了吧…不是吗？"
    hide 心愛_制服_基本_嬉しい

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「思ったより理解が早いですね…あんなに恥ずかしがってたのに…」
    voice "voice/霧葉/krh_a1_0250.ogg"
    dinerowner 店长_私服_ニヤリ "比想象中理解得还要快呢…明明刚才还那么害羞…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「だってー！　このアイスには良い思い出も恥ずかしい思い出もあるんだもの！」
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1465.ogg"
    ai 心愛_制服_基本_不機嫌 "但是！这个冰淇淋有美好的回忆和令人害羞的回忆！"
    hide 心愛_制服_基本_泣き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「感謝はしてるけど…。あー…確かに、私もこれは…我慢できそうにないかなー」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1153.ogg"
    dong 真冬_制服_基本_微笑み "虽然很感谢……啊…的确，我也忍不住了"
    hide 真冬_制服_基本_無表情
    hide 店长_私服_ニヤリ with dissolve

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「おうお～う！　我慢は身体にも心にも毒だぜぇ～！」
    show 想瑠_スーツ_ニヤリ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0180.ogg"
    liu 想瑠_スーツ_ニヤリ "哦哦~！忍耐对身体和心灵都是有害的说~！"
    hide 想瑠_スーツ_ニヤリ with dissolve

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「と、言う事で、お楽しみに家に帰ったらどうでしょう。この事務所を貸してあげてもいですけど、落ち着かないでしょう？　通販で買った輸入物のマットレスで事に至りたいなら話は別ですが」
    show 店长_私服_目閉じ at love69_wuye_center with dissolve
    voice "voice/霧葉/krh_a1_0251.ogg"
    dinerowner 店长_私服_目閉じ "那，这么说来，就高高兴兴地回家去吧。虽然也可以借给你这个事务所，但是在这里会坐立不安的吧？除非你喜欢在邮购的进口床垫上做就另当别论了"
    hide 店长_私服_目閉じ with dissolve

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「ぬぁあもー我慢できないぞー！」
    show 瑠那_私服_真顔 at love69_liuna_center with dissolve
    voice "voice/瑠那/lun_a1_0013.ogg"
    na 瑠那_私服_真顔 "啊真是的——我已经忍不住了——！"
    hide 瑠那_私服_真顔 with dissolve

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「きぃちゃあん、もう私も抑えきれない」
    show アシュリー_私服_にっこり at love69_atri_center with dissolve
    voice "voice/アシュリー/ash_a1_0047.ogg"
    atri アシュリー_私服_にっこり "叶酱，我也控制不住了"
    hide アシュリー_私服_にっこり with dissolve

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「それに、アレに巻き込まれるのも厄介でしょうしね」
    ## 修改一下以符合剧情
    show 店长_私服_無表情 at love69_wuye_center with dissolve
    voice "voice/霧葉/krh_a1_0252.ogg"
    dinerowner 店长_私服_無表情 "而且，被卷进来也很麻烦吧"
    hide 店长_私服_無表情 with dissolve

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ね、真冬ちゃん…かえろ？　もしあれなら私の家でもいし」
    voice "voice/心愛/cca_a1_1466.ogg"
    ai 心愛_制服_基本_不機嫌 "喂，真冬酱…回去吧？如果是那样的话，去我家也可以"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そう…だね。もうスイッチ入っちゃってるんでしょ？　心愛ちゃん」
    voice "voice/真冬/maf_a1_1154.ogg"
    dong 真冬_制服_基本_微笑み "是...的啊。已经打开开关了吧？心爱酱"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「う、うん…まだ、我慢できるけど…結構ギリ…かも…」
    voice "voice/心愛/cca_a1_1467.ogg"
    ai 心愛_制服_基本_不機嫌 "嗯，嗯……我还可以忍耐…可能有点…勉强呢…"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「私も…。じゃぁ、かえろっか、心愛ちゃん。帰って…うん…」
    voice "voice/真冬/maf_a1_1155.ogg"
    dong 真冬_制服_基本_微笑み "我也是……那么，回去吧，心爱酱，回去吧…嗯…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「…う、うん…えへ、なんか、三人より、二人のが、変な感じしちゃうね…」
    ## 修改一下以符合剧情
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1468.ogg"
    ai 心愛_制服_基本_笑顔 "嗯，嗯…欸嘿，总觉得，比起三个人，两个人的感觉更奇怪呢…"
    hide 心愛_制服_基本_不機嫌

    # nil 「心愛ちゃんは、ぎゅっと私の手を握って来ました。私も静かに握り替えします。」
    "心爱酱紧紧地握着我的手，我也安静地回握回去"

    # nil 「この繋いだ手が離される事は、当分ありませんでした。」
    "这只牵着我的手，暂时不会松开"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 霧葉ちゃんのお店 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「最近アシュリーにばっか手を出してるんだよなあいつ…」
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0181.ogg"
    liu 想瑠_スーツ_見下し "最近总是对亚十礼出手啊…这家伙……"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「じゃぁ、私が貴方に手を出せばいのでは？」
    show 店长_私服_無表情 at love69_wuye_right with dissolve
    voice "voice/霧葉/krh_a1_0253.ogg"
    dinerowner 店长_私服_無表情 "那我是不是可以对你出手呢"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「お願いできる？」
    show 想瑠_スーツ_ニヤリ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0182.ogg"
    liu 想瑠_スーツ_ニヤリ "可以拜托你吗？"
    hide 想瑠_スーツ_見下し

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「喜んで。るなちー、想瑠にゃん借りますね」.
    show 店长_私服_微笑み at love69_wuye_right with dissolve
    voice "voice/霧葉/krh_a1_0254.ogg"
    dinerowner 店长_私服_微笑み "乐意之至，瑠那亲，想瑠喵我借用一下"
    hide 店长_私服_無表情

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    transform love69_liuna_left:
        zoom 1.5
        xalign 0.05
        yalign -0.01

    # 瑠那 「はいよー！　はい、アシュリー、力抜いてー」
    show 瑠那_私服_にっこり at love69_liuna_left with dissolve
    voice "voice/瑠那/lun_a1_0014.ogg"
    na 瑠那_私服_にっこり "好的哦——！来，亚十礼，放松一下"

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「もー…はぁう…」
    show アシュリー_私服_にっこり at love69_atri_leftest with dissolve
    voice "voice/アシュリー/ash_a1_0048.ogg"
    atri アシュリー_私服_にっこり "真是的——……哈……"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「じゃぁほら、想瑠にゃんも、奥いきましょうね」
    show 店长_私服_にっこり at love69_wuye_right with dissolve
    voice "voice/霧葉/krh_a1_0255.ogg"
    dinerowner 店长_私服_にっこり "那么，来，想瑠喵也去里面吧"
    hide 店长_私服_微笑み

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「…ぅん」
    show 想瑠_スーツ_悲しみ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0183.ogg"
    liu 想瑠_スーツ_悲しみ "…嗯"
    hide 想瑠_スーツ_ニヤリ

    # scene11 场景1 【6人大集合，现在是女子会时间！】 结束

    # Scene11 结束！

    # 过场：心爱（常服）

    $ quick_menu = False

    play sound "voice/effect/moosehead honk (stinger).ogg"
    stop music fadeout 4.0
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)
    scene アイキャッチ心愛 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)

    $ renpy.pause(1.5, hard=True)
    $ renpy.end_replay()

    jump scene12

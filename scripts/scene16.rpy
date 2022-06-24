# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene16 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：
# 版本 NightBuild "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年6月24日

# 当前流程：All Done!

# 本脚本为二周目的第一一幕，从Scene16开始就是二周目内容了

label scene16:
    # scene16 开始

    # scene16 场景1 【世界线于此变动！】 开始

    # 地点：街道
    # 人物：莲 里昂
    # BGM：
    # 可变标题
    # Scene 序号
    $ sceneNo =  " scene16"
    # 存档名称和 Scene 大标题
    $ sceneName = " 里昂线 意料外的选择"
    # 小场景的名称
    $ partName = " 【世界线于此变动！】"
    $ changeTitleName()

    # 选择肢 「リオンに食べさせる。」
    # "给里昂吃"

    # 莲 「よし、じゃぁリオン。食べなよ」
    lian "好吧，那么里昂，你恰了吧"

    # 里昂 「…はい？」
    show リオン_基本_杖_無表情 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0001.ogg"
    lion リオン_基本_杖_無表情 "……啥？"
    hide リオン_基本_杖_微笑み

    # nil 「俺は、リオンから受け取ったアイスを、そのまリオンへ向ける。」
    "我从里昂手里接过收到的冰淇淋，把它递给里昂"

    # nil 「その回答が想定外だったのか、リオンは先ほどまでの余裕のある表情から一変して、戸惑った表情をこちらに向ける。」
    "也许是这个回答出乎意料，里昂从刚才为止从容的表情完全变了，以困惑的表情看向这边"

    # 里昂 「え…？　え？　な、なんで…私…？」
    show リオン_基本_杖_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0002.ogg"
    lion リオン_基本_杖_驚き "诶…？诶？为什么…我…？"
    hide リオン_基本_杖_無表情

    # 莲 「なんでってそりゃ…見るからに暑そうだからだ」
    lian "该怎么说呢……感觉你看上去很热"

    # 莲 「さっきもフラフラしてたし。俺よりアイスが必要なのはどうみてもあんただろ」
    lian "刚才也是摇摇晃晃的，比我更需要冰淇淋的人，怎么看都是你吧"

    # 里昂 「そ、そりゃそうかもしんないけど、で、でも…！　こ、恋が叶うアイスだよ！？　食べれば恋が叶っちゃうかもしれないんだよ？」
    show リオン_基本_杖_悲しい2 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0003.ogg"
    lion リオン_基本_杖_悲しい2 "虽，虽然也许是这样，但是，但是…！这是能实现恋爱的冰淇淋哦！？吃了也许就能实现恋爱吧？"
    hide リオン_基本_杖_驚き

    # 莲 「じゃぁ、アンタの恋を叶えるとい。それもそれで面白いじゃないか。それとも、自分で作っておいて、味も効果も眉唾かい？」
    lian "那就用来实现你的恋爱吧，这不是很有趣嘛。还是说，自己做的东西，不管味道和效果都令人怀疑呢？"

    # 里昂 「ぐっ…その挑発は卑怯だ…」
    show リオン_基本_杖_ジト目 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0004.ogg"
    lion リオン_基本_杖_ジト目 "呃啊…这种挑衅是卑鄙的…"
    hide リオン_基本_杖_悲しい2

    # 莲 「まぁほら、食えよ。暑いんだろ？」
    lian "好啦，来恰吧，你很热吧？"

    # 里昂 「わかったよ、もう、た、食べるよ！！ど、どうなっても知らないからなっ！！」
    show リオン_基本_杖_見下し at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0005.ogg"
    lion リオン_基本_杖_見下し "我知道了，我恰就是了！！不、不过，会发生什么我就不知道了啊！！"
    hide リオン_基本_杖_ジト目

    # 莲 「どうにかなるなら、むしろ見てみたいねぇ」
    lian "如果有可能的话，我倒是想看看呢"

    # 里昂 「君そんなＳっ気ある人だったっけ…た、食べるよ！　食べるからな！　イタダキマス！」
    show リオン_基本_杖_ジト目_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0006.ogg"
    lion リオン_基本_杖_ジト目_1 "你原来是个这么S的人啊……我、我要吃了啊！我要吃了昂！我开动了！"
    hide リオン_基本_杖_見下し

    # 里昂小跳
    play sound "voice/effect/17_フヒ.ogg"
    hide リオン_基本_杖_ジト目_1
    show リオン_基本_杖_ジト目_1:
        zoom 1.5
        yalign 0.07
        xalign 0.5
        linear 0.15 yalign 0.15
        linear 0.15 yalign 0.07

    # 莲 「何も一気にたべんでも…」
    lian "怎么一口气解决掉了啊…"

    # 里昂 「…もぐもぐ…おいしい…」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0007.ogg"
    lion リオン_基本_杖_微笑み "……嗯嗯……好次……"
    hide リオン_基本_杖_ジト目_1

    # 莲 「…………」
    lian "…………"

    # 里昂 「…ふにゃー…」
    show リオン_基本_杖_微笑み_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0008.ogg"
    lion リオン_基本_杖_微笑み_1 "…呼喵~…"
    hide リオン_基本_杖_微笑み

    # 莲 「…めっちゃ美味しそうだけど、食べるとあなっちゃうのか…」
    lian "…看起来特别好吃呢，但是吃了之后就变成那样了吗…"

    # nil 「食べなくて良かったと思う心と、あんなに表情ゆるむ程美味しいなら食べたかったと、半分安心、半分後悔。」
    "如果刚才恰了就好了呢，我这样想到，从这样的表情来看的话一定是非常好吃吧，一半的心情是安心，一半的心情是后悔"

    # nil 「まぁ、リオンが美味しそうにしてるから良いか。」
    "好吧，让里昂吃了这么好吃的东西也挺好"

    # 里昂 「…ふにゃー…」
    show リオン_基本_杖_にっこり_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0009.ogg"
    lion リオン_基本_杖_にっこり_1 "…呼喵~…"
    hide リオン_基本_杖_微笑み_1

    # 莲 「…ふにゃー…」
    lian "呼喵~…"

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「ヴイイイイイイイイイ」
    # 这里的MJ也少了小图标，回头加上
    voice "voice/その他/mjf_a1_0001.ogg"
    mj MJ_通常 "呜欸欸欸欸欸欸欸欸欸"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「はっ！　私、今何を…」
    show リオン_基本_杖_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0010.ogg"
    lion リオン_基本_杖_驚き "啊！我，现在在做什么啊……"
    hide リオン_基本_杖_にっこり_1

    # 莲 「あ、俺の携帯だ」
    lian "啊，是我的手机震了"

    # 里昂 「だから何でや！？」
    show リオン_基本_杖_見下し at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0011.ogg"
    lion リオン_基本_杖_見下し "所以怎么了！？"
    hide リオン_基本_杖_驚き

    # nil 「今度は着信だった。」
    "这次是来电"

    show screen callscr
    # 动画：CALL

    # 来电声
    play sound "voice/effect/主人公着信_送信.ogg"

    # nil 「電話の主は心愛。」
    "来电的人是心爱"
    hide screen callscr

    play sound "voice/effect/18_携帯電話操作音1.ogg"

    # 莲 「はいこちら葛城ピザ配達」
    lian "你好这里是葛城披萨的配送"

    # 这个语句是针对电话里的心爱设计的参数，能够调整电话里的心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.04
    $ sideimagesize.SideImageYalign = 1.04
    $ sideimagesize.SideImageZoom = 0.6

    # 心爱（电话） 「『マルゲリータとアンチョビを２００枚ずつ頼む』」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%9E%E3%83%AB%E3%82%B2%E3%83%AA%E3%83%BC%E3%82%BF_(%E3%83%94%E3%83%83%E3%83%84%E3%82%A1)
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%AB%E3%82%BF%E3%82%AF%E3%83%81%E3%82%A4%E3%83%AF%E3%82%B7%E7%A7%91
    voice "voice/心愛/cca_a1_0001.ogg"
    # ai 心愛_通話中 "『请给我２００份玛格丽特披萨和鳀鱼（L:Margherita，是意大利的一种披萨饼，也是那不勒斯披萨的代表，名字来自意大利王妃玛格丽特；鳀鱼是海水鱼、饵料鱼，通常也被作为供油类鱼，广泛分布于全球各海域，但主要集中在温暖水域）』"
    if persistent.luckykeeperSay == "shutup":
        ai 心愛_通話中 "『请给我２００份玛格丽特披萨和鳀鱼』"
    else:
        ai 心愛_通話中 "『请给我２００份玛格丽特披萨和鳀鱼（L:Margherita，是意大利的一种披萨饼，也是那不勒斯披萨的代表，名字来自意大利王妃玛格丽特；鳀鱼是海水鱼、饵料鱼，通常也被作为供油类鱼，广泛分布于全球各海域，但主要集中在温暖水域）』"

    # 莲 「ご一緒にぃグァバジュースはいかがですか？」
    # 参考资料：https://smashop.jp/subcategory/408198/special
    lian "一起再来点番石榴饮料如何？"

    # 心爱（电话） 「『ピンク色のハイビスカスが刺さってるなら是非…じゃなくて！　本当にごめんなさいなんだけど、今から温泉掘らされるハメに…ほげぇ…』」
    voice "voice/心愛/cca_a1_0002.ogg"
    ai 心愛_通話中 "『如果插着粉色的扶桑花的话那就一定要…才不是啊！真的很抱歉，现在开始要去挖温泉了…呜欸…』"

    # 莲 「真冬も一緒か？」
    lian "真冬也在一起吗？"

    # 心爱（电话） 「『うん…。『私が決して断れない申し出』をされまして…』」
    voice "voice/心愛/cca_a1_0003.ogg"
    # ai 心愛_通話中 "『嗯……她提出了一个「我绝对拒绝不了的提议」』"
    # ai 心愛_通話中 "『嗯……她提出了一个「无法拒绝的条件」』（L:这里neta之前提到的电影『教父』名台词“我将给他一个他无法拒绝的条件。”）"
    if persistent.luckykeeperSay == "shutup":
        ai 心愛_通話中 "『嗯……她提出了一个「无法拒绝的条件」』"
    else:
        ai 心愛_通話中 "『嗯……她提出了一个「无法拒绝的条件」』（L:这里neta之前提到的电影『教父』名台词“我将给他一个他无法拒绝的条件”）"

    # 莲 「ゴットファーザーかよ。お前の事だ、終わったらアイスをトリプルで奢ってやるとでも言われたんだろう」
    # lian "是教父啊。是你的话，我才是不是说结束之后请你份冰淇淋（L:这里应该是neta之前提到的电影『教父』，没康过所以不知道捏）"
    lian "是教父梗啊。说起来你啊，我不是说过结束之后要请你吃一份冰淇淋的嘛"

    # 心爱（电话） 「『私はそんな安くねぇよぉ！正確には、好きなだけ壺をかき回す権利をくれるって言われて…つい…』」
    # かき回す Stir 搅动; 搅和; 搅拌; (使)微动; (使)行动，活动; 打动; 开始感到; 拨弄是非;
    voice "voice/心愛/cca_a1_0004.ogg"
    # ai 心愛_通話中 "我才没有那么便宜啊！准确地说，她给了我在壶里随意搅动的权利……这样的……（L:这个壶指的是想放蜂蜜这样的壶，一周目有提到，心爱说过『我的兴趣是…玩弄小洞…是我的兴趣』，心爱你好涩啊）"
    # ai 心愛_通話中 "我才没有那么便宜啊！准确地说，她给了我在壶里随意搅拌的权利……之类的……（L:这个壶指的是像放蜂蜜这样的壶，一周目有提到，心爱说过『我的兴趣是…玩弄小洞…是我的兴趣』，心爱你好涩啊）"
    if persistent.luckykeeperSay == "shutup":
        ai 心愛_通話中 "『我才没有那么便宜啊！准确地说，她给了我在壶里随意搅拌的权利……之类的……』"
    else:
        ai 心愛_通話中 "『我才没有那么便宜啊！准确地说，她给了我在壶里随意搅拌的权利……之类的……（L:这个壶指的是像放蜂蜜这样的壶，一周目有提到，心爱说过『我的兴趣是…玩弄小洞…是我的兴趣』，心爱你好涩啊）』"

    # 莲 「身体を許しちまった…というわけか。まぁいよ。お前穴掘るの好きだもんな」
    lian "是身体没有办法拒绝啊……是这样吗。嘛，算了，你好像喜欢挖洞来着"

    # 心爱（电话） 「『ほんとにごめんねー！　今度みんなで一緒にご飯いこうね！』」
    voice "voice/心愛/cca_a1_0005.ogg"
    ai 心愛_通話中 "『真的很抱歉！下次再一起吃饭吧！』"

    # 莲 「へいへい。じゃぁアルバイト頑張ってな」
    lian "好的好的，那祝你打工顺利"

    # 电话挂断声
    play sound "voice/effect/18_携帯電話操作音1.ogg"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ふにゃー…」
    show リオン_基本_杖_微笑み_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0012.ogg"
    lion リオン_基本_杖_微笑み_1 "…呼喵~…"
    hide リオン_基本_杖_見下し

    # 莲 「リオン。余韻に浸ってるところ悪いんだが…」
    lian "里昂，抱歉打断正在沉浸在余韵的你"

    # 里昂 「は、はいはい！　なんだい！？　あ、もしかして、タイムリミット？ごめんね！　時間とらせちゃって！」
    show リオン_基本_杖_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0013.ogg"
    lion リオン_基本_杖_驚き "啊，在在！什么事！？啊，难道是，时间来不及了？对不起！占用了你的时间"
    hide リオン_基本_杖_微笑み_1

    # 莲 「その逆だ。この先の予定がなくなっちまった。つーことで、リオンの仕事を手伝わせて欲しいと思うんだが、どうだろう」
    lian "恰恰相反，之前的预定取消了。因此，我想给里昂的工作帮忙，怎么样？"

    # 里昂 「えっ！？　えっ！？　いのかい？　暑いし、そんな楽しいもんでもないと思うけど…」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0014.ogg"
    lion リオン_基本_杖_微笑み "诶！？诶！？可以的嘛？又热，而且我觉得也不是那么开心的事……"
    hide リオン_基本_杖_驚き

    # 莲 「俺としてはこのま暇を潰すのもそれはそれでダルいんでな…。リオンがよければ…だが…」
    lian "对我来说不过是消磨一下时间罢了……如果里昂你不介意的话……"

    # 里昂 「…えと…えっと…私は…えと…」
    show リオン_基本_杖_悲しい2 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0015.ogg"
    lion リオン_基本_杖_悲しい2 "……那个……那个……我……那个……"
    hide リオン_基本_杖_微笑み

    # 莲 「シンキングターイム…スタート！」
    # 参考资料：https://meaning-book.com/blog/20190805143633.html
    # lian "Thinking time……Start！（L:Thinking time是在智力竞赛等问答型TV节目中的常用语）"
    if persistent.luckykeeperSay == "shutup":
        lian "Thinking time……Start！"
    else:
        lian "Thinking time……Start！（L:Thinking time是在智力竞赛等问答型TV节目中的常用语）"

    # 文本框隐藏，倒计时
    # 得稍微想想怎么隐藏文本框呢

    $ quick_menu = False # 隐藏 quick_menu
    window hide # 隐藏对话框等其它窗口

    play sound "<to 2.0>voice/effect/木魚.ogg"
    queue sound "voice/effect/レジスター.ogg"
    pause 3.0
    # $ renpy.pause(3.0, hard=True)

    $ quick_menu = True
    window show

    # 里昂 「蓮くんがその…良ければ…是非、お願いしたいかな！」
    voice "voice/リオン/ron_a1_0016.ogg"
    lion リオン_基本_杖_悲しい2 "莲君……如果可以的话那就……务必，拜托你了！"

    # 莲 「喜んで。せっかく知り合えたんだし、もうちょっと一緒にいたいもんな」
    lian "我很乐意。好不容易认识了，我希望我们能多在一起一会儿"

    # 里昂 「う、うんっ…！　もうちょっと…一緒に居たい…かも。じゃぁ、蓮くんが言ってた場所…案内してもらってもいかな？」
    show リオン_基本_杖_微笑み_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0017.ogg"
    lion リオン_基本_杖_微笑み_1 "嗯，嗯……！那就再稍微多……呆会儿……那莲说的那个地方…可以带我去吗？"
    hide リオン_基本_杖_悲しい2

    # 莲 「合点承知」
    # 参考资料：https://ja.wikipedia.org/wiki/%E6%B1%9F%E6%88%B8%E6%99%82%E4%BB%A3
    # lian "我明白了（L:原文「合点承知」来源江户时代（1603-1868）描述一个人对某件事情的理解或接受，意思是“我已经明白了”）"
    if persistent.luckykeeperSay == "shutup":
        lian "我明白了"
    else:
        lian "我明白了（L:原文「合点承知」来源江户时代（1603-1868）描述一个人对某件事情的理解或接受，意思是“我已经明白了”）"

    # nil 「ということで、本日の予定を変更して、リオンのアイス屋のバイトをすることになりました。」
    "因此，改变了今天的计划，在里昂的冰淇淋店打工"

    # nil 「何でこんな事になったのか。」
    "为什么会变成这样呢？"

    # nil 「勿論、心愛と真冬にドタキャンされたのもあるが、それよりも「リオンと一緒に居たい」という気持ちが強かったからだ。」
    "当然，也有被心爱和真冬放鸽子的原因，但是比起这个，「想和里昂在一起」的心情更加强烈"

    # nil 「何故、そんな気持ちになったのかはわからないが…。」
    "虽然，不知道为什么会有这样的心情…"

    # nil 「もし、運命とやらが存在しているのなら、俺はその存在をにわかに感じていた。」
    "如果，命运真的存在的话，我会突然感觉到它的存在"

    # scene16 场景1 【世界线于此变动！】 结束

    # Scene16 结束

    # 过场：里昂（常服）

    # 之前用了这个方法，二周目需要手动控制
    window hide # 隐藏对话框等其它窗口

    # 隐藏 quick_menu
    $ quick_menu = False

    play sound "voice/effect/moosehead honk (stinger).ogg"
    image bg アイキャッチリオン = "images/bg/アイキャッチリオン.png"
    # hide screen quick_menu
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)
    scene アイキャッチリオン with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)

    $ renpy.pause(1.5, hard=True)
    $ renpy.end_replay()

    jump scene17

# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene17 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：
# 版本 NightBuild "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年5月1日

# 当前流程：All Done!

label scene17:
    # scene17 开始

    # scene17 场景1 【今天是在里昂冰淇淋店的打工】 开始
    play music bgmtwentyeight fadeout 2.0 fadein 2.0

    # 地点：街道
    # 人物：莲 里昂 孩子A 孩子B 孩子C 亚十礼
    # BGM：
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)
    scene 通学路c_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    $ quick_menu = True

    # 里昂 「よし、こはアレを使おう。あたかも瞬間移動したかのように思える奴」
    show リオン_基本_杖_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0073.ogg"
    lion リオン_基本_杖_ニタァ "好，这里就用那个吧。就像瞬间移动似的那个家伙"

    # 莲 「せーのっでジャンプするアレか！」
    lian "就是那个会跳的东西嘛！（L:电视制作常用过场特效，主持人跳起来然后切换场景，如果日综或者片儿看多了应该知道）"

    # 里昂 「せーのっ」
    show リオン_基本_杖_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0074.ogg"
    lion リオン_基本_杖_驚き "3——2"
    hide リオン_基本_杖_ニタァ

    # 场景切换：通学路街道->拉斯维加斯
    # 为拉斯维加斯专门设计的 ATL
    transform vegas:
        zoom 1.5
        xalign 0.5
        yalign 0.5
    scene ラスベガス at vegas with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)

    # 原作这里不光没有配音还没有写人物
    # 里昂 「はい」
    # voice "voice/リオン/ron_a1_0075.ogg"
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    lion リオン_基本_杖_にっこり "好（L:这里原作就没有配音）"

    # 里昂 「ということで、やってきました」
    voice "voice/リオン/ron_a1_0075.ogg"
    lion リオン_基本_杖_にっこり "就是这样，我们到啦"

    # 莲 「ラスベガァス！！」
    lian "拉斯维加斯！！"

    # 里昂 「あ、間違えた」
    show リオン_基本_杖_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0076.ogg"
    lion リオン_基本_杖_驚き "啊，搞错了"
    hide リオン_基本_杖_にっこり

    # 莲 「……」
    lian "……"

    # 拉斯维加斯->街道
    scene black at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 通学路d_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 里昂 「ということで、やってきました」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0077.ogg"
    lion リオン_基本_杖_にっこり "就是这样，我们到啦"
    hide リオン_基本_杖_驚き

    # 莲 「はい。我らが学園前の大通りです」
    lian "好，是在我们学园前的大街上"

    # nil 「流石に放課から若干時間が経っているので、下校ラッシュこそ逃しているが、部活動とかそういうので人は残っているようだ。」
    "因为放学已经过了一段时间，所以错过了放学的高峰期，但是因为社团活动留下来的人好像还有"

    # nil 「あとは、もう少し小さなお友達がボールとかキュウリとかを追いかけて走り回っている。」
    "还有，稍微有点小的朋友在追逐着球或者是黄瓜之类的东西跑来跑去（L:所以为什么会有黄瓜啊喂！）"

    # 莲 「どうでしょう、立地の方は。日当たりは良好、人通りもそれなりで、公園も近いし墓地もある」
    lian "怎么样？选址良好、日照充足，行人如潮，公园临边，墓地迫近（L:所以墓地又是什么鬼啊喂！）"

    # 里昂 「いねー！　繁華街を狙っていこうかと思ってたけど、存外有りかも！一定数の若者が毎日通るわけだし」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0078.ogg"
    lion リオン_基本_杖_微笑み "真好——！我本来想去闹市区的，没想到这里居然有这么好的地方！每天都有一定数量的年轻人经过这里呢"
    hide リオン_基本_杖_にっこり

    # 莲 「繁華街は治安も悪いし、競合になっちまうからな…」
    lian "闹市区治安不好，会引起竞争的…"

    # 里昂 「さて、どうやって宣伝していこうかな」
    voice "voice/リオン/ron_a1_0079.ogg"
    lion リオン_基本_杖_微笑み "那么，该怎么宣传呢？"

    # 莲 「まだサンプルはあんの？」
    lian "你还有样品吗？"

    # 里昂 「んーとね、さっきのラブポーション・シクスティナインはあれ一個だけだけど…。他のアイスならちょっとは持って来てるよ！」
    voice "voice/リオン/ron_a1_0080.ogg"
    lion リオン_基本_杖_微笑み "那个啊——刚才的『LOVEPOTION・SIXTYNINE』只有那一个……其它的冰淇淋倒是也带来了一些"

    # nil 「リオンがひゅっとマントを翻すと、よくキャンプとかに持って行くサイズのクーラーボックスが姿を現した。」
    "里昂嗖地一掀斗篷，经常带去野营的尺寸的冷藏箱就出现了"

    # 莲 「ほう、どんなアイスがあんの？」
    lian "哦，你这都有什么样的冰淇淋捏？"

    # 里昂 「まず『食べれるアイス』でしょ？」
    voice "voice/リオン/ron_a1_0081.ogg"
    lion リオン_基本_杖_微笑み "首先是『能吃的冰淇淋』对吧？"

    # 莲 「まぁそりゃそうだろうな…」
    lian "嘛，我想是吧…"

    # nil 「俺はリオンのクーラーボックスをあける。」
    "我打开里昂的冷藏箱"

    # nil 「中には大量のドライアイスと色とりどりのアイスクリームが入ったタッパーが収められていた。」
    "里面放着大量的干冰和放着五颜六色冰淇淋的Tupperware（L:特百惠，一个以其代表产品塑料食品容器知名于全球的美国家居用品品牌）"

    # 莲 「ふむ…」
    lian "呼姆……"

    # nil 「俺はリオンのクーラーボックスをあける。」
    "我关上冷藏箱，蹲下来思考"

    # 里昂 「シンキングターイム？　レディ？」
    show リオン_基本_杖_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0082.ogg"
    lion リオン_基本_杖_ニタァ "Thinking Time？Ready？"
    hide リオン_基本_杖_微笑み

    # 莲 「スタートォ！」
    lian "Start！"

    # 和前面一样的⏲特效

    $ quick_menu = False # 隐藏 quick_menu
    window hide # 隐藏对话框等其它窗口

    play sound "<to 2.0>voice/effect/木魚.ogg"
    queue sound "voice/effect/レジスター.ogg"
    pause 3.0
    # $ renpy.pause(3.0, hard=True)

    $ quick_menu = True
    window show

    # 莲 「思い付いた」
    lian "我想到了"

    # 里昂 「はやっ」
    show リオン_基本_杖_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0083.ogg"
    lion リオン_基本_杖_驚き "好快"
    hide リオン_基本_杖_ニタァ

    # nil 「俺は立ち上がって、リオンの方を振り向いた。」
    "我站起来，回头看向里昂"

    # 莲 「なぁ、リオン。日本の伝統芸能に『紙芝居』っつーもんがあるんだが、知ってるか？」
    # 参考资料：https://ja.wikipedia.org/wiki/%E7%B4%99%E8%8A%9D%E5%B1%85
    lian "呐，里昂。日本的传统艺术中有『纸芝居』这样的东西，你知道吗？（L:『纸芝居』是诞生在昭和初期，主要以孩子为对象，一边给孩子看画书，一边给孩子讲故事进行表演的一种剧种。在很多作品都能看到捏，我印象最深的是夏娃年代记里面有提到，感兴趣的话阔以去玩玩）"

    # 里昂 「カミシバイ…？　キネティックタイポグラフィーみたいな感じ？」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%AD%E3%83%8D%E3%83%86%E3%82%A3%E3%83%83%E3%82%AF%E3%83%BB%E3%82%BF%E3%82%A4%E3%83%9D%E3%82%B0%E3%83%A9%E3%83%95%E3%82%A3
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0084.ogg"
    lion リオン_基本_杖_微笑み "纸·芝·居……？感觉像Kinetic typography的感觉？（L:动力学排版，是一种动画技术，将运动和文本混合在一起，Adobe Flash、Adobe After Effects和Motion等软件都支持这种特效）"
    hide リオン_基本_杖_驚き

    # 莲 「いや全然違うな。要は、何枚かの止め絵をお客さんに見せながら、キャラになりきったりして喋るパフォーマンスでな」
    lian "不，完全不一样。主要是一边给客人看几张静止画，一边扮成角色说话的表演"

    # 里昂 「なるほど！　日本の美少女ゲームみたいな感じだね！」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0085.ogg"
    lion リオン_基本_杖_にっこり "原来如此！感觉就像日本的美少女游戏呢！（L:emmm……雀食有点道理捏）"
    hide リオン_基本_杖_微笑み

    # 莲 「ちょっとスレスレな事を言うのはやめろ！」
    lian "不要说这么刺耳的话！（L:破防了破防了233）"

    # 莲 「そんで、紙芝居をする人は、近所の子供達に水飴とかの駄菓子を売ったり配ったりしてたんだよ」
    # 駄菓子=粗点心
    lian "然后，演纸芝居的人，会向附近的孩子们出售或者发放糖水和粗点心"

    # 莲 「やっぱ甘い物を食いながらの方が、子供達は楽しいだろうしね」
    lian "果然还是一边吃甜食一边观赏，孩子们会更开心吧"

    # 莲 「何より、こういうのって口コミで広がるもんだろ？　なら、子供達のニーズを抑えた方が効率がい。子供は欲求に率直だからな」
    lian "最重要的是，这种东西是通过口碑传播的吧？那么，控制孩子们的需求更有效率，因为孩子对欲望很坦率呢"

    # 里昂 「つまり…アイスのサンプルを配りながら、紙芝居を演じる…ということだね！でも、アイスはあっても紙芝居なんてもってないよ？」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0086.ogg"
    lion リオン_基本_杖_微笑み "也就是说…一边分发冰淇淋的样品，一边演纸芝居…这样的吧！但是，就算我有冰淇淋，也没有纸芝居哟？"
    hide リオン_基本_杖_にっこり

    # 莲 「心配ない。こんな事もあろうかと、持ち歩いている」
    lian "不用担心。我想着会发生这样的事，随身带着呢"

    # nil 「俺は鞄から紙芝居を取り出す。朝は空だったとか、そういう無粋な事は聞かない事だ。」
    "我从包里拿出纸芝居。不要问我明明早上包里还是空的，这种乱七八糟的问题"

    # 里昂 「何者なんだね君は」
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0087.ogg"
    lion リオン_基本_杖_悲しい "你是什么人？"
    hide リオン_基本_杖_微笑み

    # 莲 「語ると長くなるから今度な。後はキャストだが…リオン、演じるのは得意か？」
    lian "说起来太长了，下次吧。然后就是演员…里昂，你擅长表演吗？"

    # 里昂 「うん。小さい頃に一度ブロードウェイを目指したことがあるよ。マイケルもやれば出来る子だと思う」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0088.ogg"
    lion リオン_基本_杖_微笑み "嗯。我小时候曾以百老汇为目标去过一次。我觉得迈克尔也是个能干的孩子"
    hide リオン_基本_杖_悲しい

    # nil 「コンコンとリオンは、帽子を杖の頭で叩いた。」
    "里昂用拐杖头咚咚地敲了敲帽子"

    # 里昂 「ゲットアップマイコォ」
    voice "voice/リオン/ron_a1_0089.ogg"
    lion "Get up Michael！（L:这里原作把里昂的上一句重复了，没有配这句呢……）"

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「この俺の眠りを妨げるとはな…良いぜ。死にてぇやつからかってこい」
    voice "voice/その他/mjf_a1_0014.ogg"
    mj MJ_通常 "没想到你会妨碍我的睡眠…好啊，去死吧你这个可笑的家伙"

    # 莲 「上出来だ」
    lian "做得很好"

    # MJ 「てめェ…こで何してやがる」
    voice "voice/その他/mjf_a1_0015.ogg"
    mj MJ_通常 "你这家伙……你在这里干什么？"

    # 莲 「バイトだ」
    lian "打工啊"

    # MJ 「そうか」
    voice "voice/その他/mjf_a1_0016.ogg"
    mj MJ_通常 "是吗"

    # nil 「役者は揃った。」
    "演员都到齐了"

    # 莲 「あとは子供達を集めて、アイスを配るだけだな」
    lian "剩下的就是把孩子们召集起来，分发冰淇淋了"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「えーっと、どうやって子供達を集める…？」
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0090.ogg"
    lion リオン_基本_杖_悲しい "那个，怎么把孩子们聚集起来呢…？"
    hide リオン_基本_杖_微笑み

    # 莲 「まぁ見てろって」
    lian "嘛，来看我的"

    # nil 「俺は鞄からパから貰ったクラリネットを取り出して、一吹きする。」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%AF%E3%83%A9%E3%83%AA%E3%83%8D%E3%83%83%E3%83%88
    "我从包里拿出爸爸给我的单簧管，吹了起来（L:单簧管又称竖笛、黑管，是一种木管乐器）"

    # 莲 「オーパッキャラマードパッキャラマードパオパオパッパッパー！」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%AF%E3%83%A9%E3%83%AA%E3%83%8D%E3%83%83%E3%83%88%E3%82%92%E3%81%93%E3%82%8F%E3%81%97%E3%81%A1%E3%82%83%E3%81%A3%E3%81%9F
    lian "オーパッキャラマードパッキャラマードパオパオパッパッパー！（L:嘛，这里是演奏的拟声，不翻了，疑似neta童谣「クラリネットをこわしちゃった」），这个童谣也有葡萄牙语、西班牙语和瑞典语的版本"

    # 莲 「子供たちー！　美味しいアイスクリームとかーみしばいの時間だよー！」
    lian "孩子们！现在是吃美味冰淇淋的时间！"

    # 子供Ａ（孩子A） 「ヒャッハァアアアア！！」
    # 人物表++++++++++++++++
    # 好像没有配音？
    childa "哈哈哈哈哈哈哈！！"

    # 子供B（孩子B） 「アイスだァアアア！！！」
    # 人物表++++++++++++++++
    voice "voice/その他/ot7_a1_0001.ogg"
    childb "是冰淇淋啊！！！"

    hide リオン_基本_杖_悲しい
    show リオン_基本_杖_微笑み:
        zoom 1.5
        yalign 0.07
        xalign 0.5
        linear 0.3 xalign 0.89

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼在左的参数
    transform love69_atri_left:
        zoom 1.5
        xalign 0.14
        yalign -0.295

    # 子供C（孩子C）（亚十礼） 「ケツを拭く紙にもなりゃしねぇ～！！！」
    # 人物表++++++++++++++++
    show アシュリー_私服_にっこり at love69_atri_left with dissolve
    voice "voice/その他/ot8_a1_0001.ogg"
    childc アシュリー_私服_にっこり "这里甚至连擦屁股的纸都没有啊~！！！"

    # nil 「俺が叫ぶと、子供達が路地裏や公園から飛び出してきて、俺達の前に整列した。」
    "我一喊，孩子们就从巷子和公园里跑出来，排在我们面前"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「まるでハーメルンの笛吹きだね…」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%8F%E3%83%BC%E3%83%A1%E3%83%AB%E3%83%B3%E3%81%AE%E7%AC%9B%E5%90%B9%E3%81%8D%E7%94%B7
    show リオン_基本_杖_驚き at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0091.ogg"
    lion リオン_基本_杖_驚き "简直就像是在吹Hameln的笛子啊…（L:花衣魔笛手(德文：Rattenfänger von Hameln)是个源自德国的民间故事，最有名的版本收在格林兄弟的「德国传说」中，名为「哈梅尔的孩子」）"
    hide リオン_基本_杖_微笑み

    # 是Luckykeeper的讲故事时间！
    luckykeeper "故事是这样的：1284年，德国有个村落名叫哈默尔恩（Hameln），那里鼠满为患。某天来了个外地人自称捕鼠能手，村民向他许诺 —— 能除去鼠患的话会给付重酬。"

    luckykeeper "于是他吹起笛子，鼠群闻声随行至威悉河而淹死。事成后，村民违反诺言不付酬劳，吹笛人便饮怒离去。过了数周，正当村民在教堂聚集时，吹笛人就回来吹起笛子，众孩子亦闻声随行，结果被诱到山洞内活活困住"

    # 莲 「よし、じゃぁ後はアイスを配るだけだ。頼むぜリオン」
    lian "好，之后就只需要分发冰淇淋了。拜托你了里昂"

    # 里昂 「らじゃ！」
    show リオン_基本_杖_ニタァ at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0092.ogg"
    lion リオン_基本_杖_ニタァ "了解！"
    hide リオン_基本_杖_驚き

    # nil 「リオンはクーラーボックスから、ミニサイズのアイスを取り出して、子供達に配り始めた。」
    "里昂从冷藏箱里拿出了迷你型的冰淇淋，开始分发给孩子们"

    # 里昂 「はい、どーぞ」
    show リオン_基本_杖_にっこり at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0093.ogg"
    lion リオン_基本_杖_にっこり "来。请吃"
    hide リオン_基本_杖_ニタァ

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「わーい！」
    voice "voice/アシュリー/ash_a1_0014.ogg"
    atri "好——"

    # nil 「子供達もリオンも、輝くような笑顔で、アイスの受け渡しをしている。やはり暑い日には渡りに船というやつだろう。」
    "孩子们和里昂都带着灿烂的笑容，交接着冰淇淋。果然在炎热的日子里，他们还是会随波逐流"

    # nil 「リオンが子供達にアイスを配り終えるタイミングを見計らいながら、紙芝居の準備をする。」
    "一边等待里昂给孩子们发完冰淇淋的时机，一边准备纸芝居"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「蓮くん！　配り終えたよ！」
    show リオン_基本_杖_微笑み at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0094.ogg"
    lion リオン_基本_杖_微笑み "莲君！发完了哟！"
    hide リオン_基本_杖_にっこり

    # 莲 「こっちも準備ＯＫだ。いけるぜ」
    lian "我这边也准备ＯＫ了，可以的"

    # nil 「俺はお手製の紙芝居を子供達に見せながら、親指を立てる。」
    "我一边给孩子们看自制的纸芝居，一边竖起大拇指"

    # nil 「リオンも商売モードにスイッチが切り替わったようで、俄然やる気な営業スマイルをこちらに向けて来た。」
    "里昂似乎也切换到了商业模式，突然向这边露出了充满干劲的营业微笑"

    # 里昂 「はいはーい！　みなさーんこんにちはー！」
    show リオン_基本_杖_にっこり at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0095.ogg"
    lion リオン_基本_杖_にっこり "好好——！大家吼哇——！"
    hide リオン_基本_杖_微笑み

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「こーんにちはー！」
    voice "voice/アシュリー/ash_a1_0015.ogg"
    atri "你好呀——！"

    # 子供Ａ（孩子A） 「声がちいさーい！」
    # 好像没有配音？
    childa "声音太小了！"

    # 子供B（孩子B） 「もういっちょ！！！！！」
    # 人物表++++++++++++++++
    voice "voice/その他/ot7_a1_0002.ogg"
    childb "再来一点！！！！！"

    # 亚十礼 「オイーッス！」
    voice "voice/アシュリー/ash_a1_0016.ogg"
    atri "好耶！"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「じゃぁねー、いまからぁ、私、リオンお姉さんと」
    show リオン_基本_杖_微笑み at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0096.ogg"
    lion リオン_基本_杖_微笑み "那这样啊——，从现在开始，我，里昂姐姐、"
    hide リオン_基本_杖_にっこり

    # 莲 「葛城です」
    lian "我，葛城哥哥"

    # 里昂 「そして、帽子のマイケル君と一緒に、紙芝居をやります！本日の演目はなんでしょう！」
    voice "voice/リオン/ron_a1_0097.ogg"
    lion リオン_基本_杖_微笑み "然后，还有帽子的迈克尔君一起演纸芝居！今天的节目是什么呢！"

    # 莲 「じゃじゃーん！　『吸血鬼さんと神父さん！』」
    lian "锵锵！『吸血鬼先生和神父先生！』（L:去康了一下，似乎本作发售的时候好像还没有这个标题的东西，不过后来pixiv上好像有人画了这样标题的BL本）"

    # 里昂 「え？」
    show リオン_基本_杖_驚き at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0098.ogg"
    lion リオン_基本_杖_驚き "诶？"
    hide リオン_基本_杖_微笑み

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「我等は神の代理人…神罰の地上の代行者。我等の指名は、我が神に逆らう愚者を…」
    voice "voice/その他/mjf_a1_0017.ogg"
    mj MJ_通常 "我等是神的代理人……神罚在地上的代行者。我等的使命，是让违抗我神的愚者…………"

    # MJ 「その肉の最後の一片までも絶滅させる事…」
    voice "voice/その他/mjf_a1_0018.ogg"
    mj MJ_通常 "连肉体的最后一片肉也要将其灭绝"

    # MJ 「エ゛イ゛ィイメ゛ェン！！！」
    voice "voice/その他/mjf_a1_0019.ogg"
    mj MJ_通常 "阿——门！！！"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ばきゅーん！」
    show リオン_基本_杖_ニタァ at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0099.ogg"
    lion リオン_基本_杖_ニタァ "啪嗒——！"
    hide リオン_基本_杖_驚き

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「ホギャア！」
    voice "voice/その他/mjf_a1_0020.ogg"
    mj MJ_通常 "喝啊啊啊啊啊啊！"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 通学路d_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「続いては…『女の子とおじさん』」
    lian "接下来是…『女孩和叔叔』（L:和上面的一样，也没有玩梗）"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ちょっとまとうか！？」
    show リオン_基本_杖_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0100.ogg"
    lion リオン_基本_杖_驚き "稍微等一哈！？"
    hide リオン_基本_杖_ニタァ

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「さぁお嬢さん…怖くないから触ってごらん…ほら、こだよ…こにチョコレートがあるよ…」
    voice "voice/その他/mjf_a1_0021.ogg"
    mj MJ_通常 "来吧，小姐…不要害怕，摸摸看…看，就是这里…这里有巧克力哦…"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「わ…すごく熱いね…おじさん！」
    show リオン_基本_杖_微笑み_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0101.ogg"
    lion リオン_基本_杖_微笑み_1 "哇……好烫啊……叔叔！"
    hide リオン_基本_杖_驚き

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「あ…凄く熱くなってる…さぁ、溶ける前に食べてしまいなさい…」
    voice "voice/その他/mjf_a1_0022.ogg"
    mj MJ_通常 "啊…变得非常热了…来吧，在融化之前把它吃掉吧…"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「はーい。いただきまーす♪」
    show リオン_基本_杖_にっこり_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0102.ogg"
    lion リオン_基本_杖_にっこり_1 "好————我开动了！"
    hide リオン_基本_杖_微笑み_1

    hide リオン_基本_杖_にっこり_1
    show リオン_基本_杖_にっこり_1:
        zoom 1.5
        yalign 0.07
        xalign 0.5
        linear 0.3 xalign 0.89

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「ばきゅーん！」
    show アシュリー_私服_微笑み at love69_atri_left with dissolve
    voice "voice/アシュリー/ash_a1_0017.ogg"
    atri アシュリー_私服_微笑み "花Q——！"

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「ホギャア！」
    voice "voice/その他/mjf_a1_0023.ogg"
    mj MJ_通常 "喝啊！"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 通学路d_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「さて続いては『結婚して年の中間管理職さんとその奥さん』」
    lian "接下来是『一位结婚一年的中层管理人员和他的妻子』（L:这个标题嘛，就……）"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「だから！」
    show リオン_基本_杖_ジト目 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0103.ogg"
    lion リオン_基本_杖_ジト目 "所以啊！"

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「また…学校に呼び出されたよ…。息子さんと過ごす時間が足りてないんじゃないかとな…」
    voice "voice/その他/mjf_a1_0024.ogg"
    mj MJ_通常 "我又…被学校叫去了……和儿子一起度过的时间不够啊…"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「息子だけじゃないわ。貴方、いつも仕事ばかりで私にも構ってくれないじゃない。最後に抱いてくれたの、もういつだったか思い出せすらしないわよ！」
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0104.ogg"
    lion リオン_基本_杖_悲しい "不光是儿子。你总是忙于工作，对我也不关心。我甚至都想不起你上次抱我是什么时候了！"
    hide リオン_基本_杖_ジト目

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「こんなタイミングで何を言い出すんだよ！　こっちは仕事で疲れてるんだ！」
    voice "voice/その他/mjf_a1_0025.ogg"
    mj MJ_通常 "在这种时候说什么啊！我工作太累了！"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「こっちは本気よ！　いつも仕事仕事って、そうやって言い訳して！　一時間や二時間ぐらい、時間を割いてくれたっていじゃない！」
    show リオン_基本_杖_ジト目 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0105.ogg"
    lion リオン_基本_杖_ジト目 "我是认真的！你总是找借口说要工作要工作的！为什么不从你一天的时间里面抽出一两个小时呢！"
    hide リオン_基本_杖_悲しい

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「うるせぇうるせぇ！　そんなに喚くなら抱いてやるよ！　全部脱げ、今すぐだ！」
    voice "voice/その他/mjf_a1_0026.ogg"
    mj MJ_通常 "吵死了，吵死了！那么大喊大叫我现在就抱你！全部脱掉，现在马上！"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「きゃーっ☆」
    show リオン_基本_杖_にっこり_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0106.ogg"
    lion リオン_基本_杖_にっこり_1 "呀————☆"
    hide リオン_基本_杖_ジト目

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 通学路d_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「さて続きましては『酒とタバコと俺とバイク』」
    lian "接下来是…『酒、烟、我和摩托车』（L:依旧没有玩梗，不知道是不是玩累了所以暂时不玩了）"

    # 里昂 「ちょっとちょっと葛城お兄さん！」
    show リオン_基本_杖_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0107.ogg"
    lion リオン_基本_杖_驚き "等下等下葛城哥哥！"

    # 莲 「なんでしょう、リオンお姉さん」
    lian "什么事呢，里昂姐姐"

    # 里昂 「さっきから、若干お題目がアダルティ過ぎないかなぁ！もうちょっと可愛らしい…こう、小動物が出てくる奴とかないの？」
    # 参考资料：https://en.wiktionary.org/wiki/%E3%82%A2%E3%83%80%E3%83%AB%E3%83%86%E3%82%A3
    show リオン_基本_杖_ジト目 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0108.ogg"
    lion リオン_基本_杖_ジト目 "从刚才开始，我就觉得这一个个题目都太成人向了啊！就没有再可爱一点……emmm，有小动物出现这样的之类吗？"
    hide リオン_基本_杖_驚き

    # 莲 「そうは言っても、今の子供達だって舌肥えて、多少の刺激はスパイスだって」
    lian "话是这么说，现在的孩子们的口味都叼了，需要来点刺激的"

    # 里昂 「生々しいコンテンツ論はいからぁ…！」
    # コンテンツ=contents
    show リオン_基本_杖_見下し at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0109.ogg"
    lion リオン_基本_杖_見下し "不想要这种低俗的内容可以嘛……！"
    hide リオン_基本_杖_ジト目

    # 莲 「『熊のぬいぐるみとお兄さん』とかはどうよ」
    lian "『熊的布偶和哥哥』怎么样？"

    # 里昂 「私、それに近しい映画を最近見た気がするよ…」
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0110.ogg"
    lion リオン_基本_杖_悲しい "我最近好像看过类似的电影……（L:电影看的少，不知道说的是啷个，不过倒是想到了玩具熊的五夜后宫）"
    hide リオン_基本_杖_見下し

    # 莲 「じゃぁ、『仔猫と僕』」
    lian "那么，『小猫和我』"

    # 里昂 「あ、よさそう」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0111.ogg"
    lion リオン_基本_杖_微笑み "啊，好像不错"
    hide リオン_基本_杖_悲しい

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 通学路d_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「僕はおもむろに仔猫を取り出して、一気に吸い込みました」
    lian "我慢慢地把小猫拿出来，一口气吸了进去"

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「すーっ…はーっ…すーっ…ハァー！」
    voice "voice/その他/mjf_a1_0027.ogg"
    mj MJ_通常 "嗯——……哈…哇…哈——！"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ニャー」
    show リオン_基本_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0112.ogg"
    lion リオン_基本_杖_嬉しい "喵呜——"

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # 这里没HOOK出来，内容基本一致，就是Michael模仿吸猫的声音，我就不手打了
    # MJ 「すーっ…はーっ…すーっ…ハァー！」
    voice "voice/その他/mjf_a1_0028.ogg"
    mj MJ_通常 "嗯——……啊——…嗯——…啊——！！"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ニャー」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0113.ogg"
    lion リオン_基本_杖_微笑み "喵呜——"
    hide リオン_基本_杖_嬉しい

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「やっぱり、仔猫は最高だ！」
    voice "voice/その他/mjf_a1_0029.ogg"
    mj MJ_通常 "果然小猫最棒了！"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ニャー♪」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0114.ogg"
    lion リオン_基本_杖_にっこり "喵呜♪"
    hide リオン_基本_杖_微笑み

    hide リオン_基本_杖_にっこり
    show リオン_基本_杖_にっこり:
        zoom 1.5
        yalign 0.07
        xalign 0.5
        linear 0.3 xalign 0.89

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「ニャー♪」
    show アシュリー_私服_にっこり at love69_atri_left with dissolve
    voice "voice/アシュリー/ash_a1_0018.ogg"
    atri アシュリー_私服_にっこり "喵呜♪"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「なんですかこれは」
    show リオン_基本_杖_ジト目 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0115.ogg"
    lion リオン_基本_杖_ジト目 "是什么啊这个"
    hide リオン_基本_杖_にっこり

    # 莲 「でも受けてるぞ」
    lian "但是有效果了啊"

    # 仔猫達（小猫们） 「ニャー♪」
    # 人物表+++++
    voice "voice/その他/cat_a1_0001.ogg"
    nekos "喵呜♪"

    # 里昂 「いつのまに夥しい数の仔猫たちが集まってきている…」
    show リオン_基本_杖_驚き at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0116.ogg"
    lion リオン_基本_杖_驚き "数量庞大的小猫们不知什么时候聚集过来了……"
    hide リオン_基本_杖_ジト目

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「アー！　仔猫だァア！　つかまえた！」
    voice "voice/アシュリー/ash_a1_0019.ogg"
    atri アシュリー_私服_にっこり "哇啊！是只小猫啊！我抓到它了！"

    # 仔猫（小猫） 「ニャー」
    # 人物表+++++
    voice "voice/その他/cat_a1_0002.ogg"
    neko "喵呜！"

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「すうーはぁー！」
    voice "voice/アシュリー/ash_a1_0020.ogg"
    atri アシュリー_私服_にっこり "哈——哇——！"

    # 仔猫（小猫） 「ニャー♪」
    # 人物表+++++
    voice "voice/その他/cat_a1_0003.ogg"
    neko "喵呜♪"

    # 莲 「な？」
    lian "蛤？"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「不思議の国ニッポンだね…」
    show リオン_基本_杖_悲しい at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0117.ogg"
    lion リオン_基本_杖_悲しい "真是不可思议的日本啊……"
    hide リオン_基本_杖_驚き

    # 里昂 「葛城お兄さん。犬ネタはないのかな？」
    show リオン_基本_杖_微笑み at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0118.ogg"
    lion リオン_基本_杖_微笑み "葛城哥哥，有没有狗的素材？"
    hide リオン_基本_杖_悲しい

    # 莲 「お、乗ってきたな。無い事はないよ」
    # lian "哦，你越来越上道了，没有什么是不可以的"
    lian "哟，越来越上道了，那必须安排上"

    # 里昂 「どんな？」
    show リオン_基本_杖_驚き at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0119.ogg"
    lion リオン_基本_杖_驚き "是什么呢？"
    hide リオン_基本_杖_微笑み

    # 莲 「『政府の犬』」
    lian "『政府的狗』"

    # 里昂 「それは違う犬かなぁ…熊は？」
    show リオン_基本_杖_ジト目 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0120.ogg"
    lion リオン_基本_杖_ジト目 "那是另一种狗了……熊呢？"
    hide リオン_基本_杖_驚き

    # 莲 「『ヒゲと熊』」
    lian "『胡须和熊』"

    # 里昂 「それも違う熊かなぁ…」
    show リオン_基本_杖_悲しい at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0121.ogg"
    lion リオン_基本_杖_悲しい "也不是这个熊吧……"
    hide リオン_基本_杖_ジト目

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 通学路d_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「睡眠時無呼吸症候群について、お話します」
    # 参考资料：https://ja.wikipedia.org/wiki/%E7%9D%A1%E7%9C%A0%E6%99%82%E7%84%A1%E5%91%BC%E5%90%B8%E7%97%87%E5%80%99%E7%BE%A4
    lian "来谈谈睡眠呼吸中止症的话题吧（L:是一种在睡眠期间，暂停呼吸或呼吸减弱症状导致的睡眠紊乱，在一般情况下，这个症状会产生吵杂的打鼾声）"

    # 里昂 「睡眠時無呼吸症候群とは、睡眠中に呼吸が停止してしまう病気で、いびきをかいてる人は、この病気の恐れがあります」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0122.ogg"
    lion リオン_基本_杖_微笑み "睡眠呼吸中止症是睡眠中呼吸停止的疾病，打鼾的人有可能患上这种疾病"
    hide リオン_基本_杖_悲しい

    # 里昂 「なお、症状が重いと死に至る病なので、もし心配なら医師の診断を受け、適切な治療を受けるとよいでしょう」
    show リオン_基本_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0123.ogg"
    lion リオン_基本_杖_嬉しい "另外，如果症状严重，就会出现致死的疾病，所以如果担心，最好去看医生，接受适当的治疗"
    hide リオン_基本_杖_微笑み

    # 莲 「尚、スマートフォンアプリなどで、睡眠中の音を録音する物などもありますので、自分の呼吸が止まっている等は調べる事も出来ます」
    lian "另外，还有用智能手机应用等记录睡眠中声音的方法，可以调查自己呼吸停止等情况"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 通学路d_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「お姉さん、アイスおかわりー！」
    show アシュリー_私服_にっこり at love69_atri_left with dissolve
    voice "voice/アシュリー/ash_a1_0021.ogg"
    atri アシュリー_私服_にっこり "姐姐，再来一杯冰淇淋——"

    # 里昂 「はいはーい♪　どんなアイスがいかなー？」
    show リオン_基本_杖_にっこり at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0124.ogg"
    lion リオン_基本_杖_にっこり "好的好的♪什么样的冰淇淋好呢？"

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「んとねー！　食べれる奴！」
    show アシュリー_私服_微笑み at love69_atri_left with dissolve
    voice "voice/アシュリー/ash_a1_0022.ogg"
    atri アシュリー_私服_微笑み "那个啊！能吃的那个！"
    hide アシュリー_私服_にっこり

    # 莲 「まぁ、そりゃそうだろうな」
    lian "嘛，那是当然的"

    # 莲 「クイズ！　５．１ｃｈサラウンドとは、どこにスピーカーがある事でしょう！」
    lian "猜谜！５．１ｃｈ的所谓环绕，是指哪里有扬声器呢！"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ピンポーン！」
    show リオン_基本_杖_微笑み at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0125.ogg"
    lion リオン_基本_杖_微笑み "叮咚！"
    hide リオン_基本_杖_にっこり

    # 莲 「はいイギリスからお越しのマクスウェルさん」
    lian "好，来自英国的麦克斯韦选手"

    # 里昂 「わかりません！」
    # 126
    show リオン_基本_杖_驚き at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0126.ogg"
    lion リオン_基本_杖_驚き "我不知道！"
    hide リオン_基本_杖_微笑み

    # 莲 「正解！！」
    lian "正解！！！"

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「正面、右前、左前、右後ろ、左後ろ。これでチャンネル。サブウーファーで１だよ」
    # 参考资料：https://zh.wikipedia.org/wiki/5.1%E8%81%B2%E9%81%93
    show アシュリー_私服_無表情 at love69_atri_left with dissolve
    voice "voice/アシュリー/ash_a1_0023.ogg"
    atri アシュリー_私服_無表情 "前面、右前、左前、右后、左后。这些是Channel，.1是重低音扬声器"
    hide アシュリー_私服_微笑み

    # 莲 「はい」
    lian "是这样的"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 通学路d_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「お爺さんは、山へしばかれに行きました」
    lian "爷爷到山上去了"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ほらほら、強く叩いて欲しかったら求めてごらんよ！　この田舎の種なし爺が！」
    show リオン_基本_杖_ニタァ at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0127.ogg"
    lion リオン_基本_杖_ニタァ "来吧，来吧，如果你想让我狠狠地打你，尽管开口！你这个乡下的老母猪！"

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「あんっ！　もっと！　もっと叱ってください！　こんな辺境の農民にお慰みを！」
    voice "voice/その他/mjf_a1_0030.ogg"
    mj MJ_通常 "啊蛤！再多，再多骂一点！请这样给边境的农民们慰藉！"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ほうら！　お尻が桃みたいに腫れてきたよ！　このま川へ流してやろうか！」
    show リオン_基本_杖_見下し at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0128.ogg"
    # lion リオン_基本_杖_見下し "你看！你的屁股肿得像桃子一样！我要把你冲到河里去！"
    lion リオン_基本_杖_見下し "你看！你的屁股肿得像桃子一样！我要把你扔到河里去！"
    hide リオン_基本_杖_ニタァ

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「ありがとうございまあっす！！」
    voice "voice/その他/mjf_a1_0031.ogg"
    mj MJ_通常 "十分感谢万分感激！！"

    # 莲 「そして、お婆さんは川で洗濯中、どんぶらこ、どんぶらこと流れるおじいさんをそっと見送りました」
    lian "然后，老奶奶在河里洗衣服的时候，悄悄地目送着被流水冲走的老爷爷"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 通学路d_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「うんこちんちん」
    lian "大便金金（L:emmmm，莲你在淦神魔？！）"
    # 关于问题：日语的チンポ，おちんちん和汉语的jb，xjj是发音巧合还是有接触关系？答案：有多种来源说法，其中之一就是可能源自汉语
    # 参考知乎回答：https://www.zhihu.com/question/273798677/answer/370294195

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ついにネタが切れたようです」
    # 129
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0129.ogg"
    lion リオン_基本_杖_悲しい "这是终于没有素材了"

    # 场景切换到黄昏街道
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 通学路d_夕 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 定义瑠那在右的参数
    transform love69_liuna_right:
        zoom 1.5
        xalign 0.92
        yalign -0.01

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「ほらほらアシュリー、こんな所にいたのね」
    show 瑠那_私服_微笑み at love69_liuna_right with dissolve
    voice "voice/瑠那/lun_a1_0001.ogg"
    na 瑠那_私服_微笑 "这边这边，亚十礼，原来你在这里"

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「わー！　ほらほら！　アイス貰ったんだよー！　すっごく美味しいの！」
    show アシュリー_私服_にっこり at love69_atri_left with dissolve
    voice "voice/アシュリー/ash_a1_0024.ogg"
    atri アシュリー_私服_にっこり "哇——！你看你看！我拿到冰淇淋了！太好吃了！"

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「よしよし。ほら、お姉ちゃんのおうちに帰ろ」
    show 瑠那_私服_にっこり at love69_liuna_right with dissolve
    voice "voice/瑠那/lun_a1_0002.ogg"
    na 瑠那_私服_にっこり "好孩子好孩子，来，和姐姐回家去"
    hide 瑠那_私服_微笑み

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「はーい！　ばいばーい！　紙芝居のお兄さん、お姉さん！　アイスすっごくおいしかったよー！　あとすっごく楽しかった！」
    voice "voice/アシュリー/ash_a1_0025.ogg"
    atri "好——！ByeBye！纸芝居的哥哥，姐姐！冰淇淋非常好吃哦！还有玩的非常开心哦！"

    # 仔猫（小猫） 「ニャー♪」
    # 人物表+++++
    voice "voice/その他/cat_a1_0004.ogg"
    neko "喵呜♪"

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「うわァア仔猫だァアアアアア！」
    voice "voice/アシュリー/ash_a1_0026.ogg"
    atri "哇哦小猫咪啊啊啊啊！！"

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「仔猫だァアアアアアアアアア!!!」
    show 瑠那_私服_はう at love69_liuna_right with dissolve
    voice "voice/瑠那/lun_a1_0003.ogg"
    na 瑠那_私服_はう "小猫啊啊啊啊！！！"
    hide 瑠那_私服_にっこり

    # 仔猫（小猫） 「ニャー♪」
    # 人物表+++++
    voice "voice/その他/cat_a1_0005.ogg"
    neko "喵呜♪"

    # 亚十礼与瑠那离场，里昂出现
    hide アシュリー_私服_にっこり with dissolve
    hide 瑠那_私服_はう with dissolve
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve

    # nil 「夕焼け小焼けの帰宅メロディが鳴り響く。真夏ゆえ、まだ日は明るいが、よい子は帰る時間だ。」
    "晚霞渐微的回家旋律响起。因为是盛夏，天还很亮，但是已经是乖孩子该回家的时间了"

    # nil 「それぞれ、よい子達は家族に手を引かれて自分達の家へ帰っていく。」
    "乖孩子被他们各自的家人牵回了家"

    # 子供Ａ（孩子A） 「えっとねー私ねーおっきくなったらパみたいなお相撲さんになるのー！」
    # 好像没有配音？
    childa "那个啊——我啊——长大了之后会像爸爸一样成为相扑运动员！"

    # 母親Ａ（母亲A） 「ならまずはこの私を倒してからにするんだな」
    # 人物表++++++
    voice "voice/その他/ot3_a1_0001.ogg"
    mothera "那就先来把我打倒吧"

    # 子供Ａ（孩子A） 「よかろう」
    # 好像没有配音？
    childa "好吧"

    # 子供Ｂ（孩子B） 「ねぇマ。赤ちゃんはどこからくるの？」
    voice "voice/その他/ot7_a1_0003.ogg"
    childb "那妈妈，宝宝是从哪里来的？"

    # 母親Ｂ（母亲B） 「こからやで」
    # 人物表++++++
    voice "voice/その他/ot4_a1_0001.ogg"
    # motherb "从这里开始"
    motherb "从这里呦"

    # 子供Ｂ（孩子B） 「Oh sexy……」
    voice "voice/その他/ot7_a1_0004.ogg"
    childb "哦，赛克西……"

    # 移出小头像
    $ sideimagesize.SideImageXalign = 69.0
    $ sideimagesize.SideImageYalign = -69.0
    $ sideimagesize.SideImageZoom = 1.0

    # 子供Ｃ（孩子C） 「ねぇマ。いつか、酒とタバコとバイクしたいな！」
    voice "voice/その他/ot8_a1_0002.ogg"
    childc "呐妈妈，我想有一天能喝上酒，抽上烟，骑上摩托车啊！"

    # 母親Ｃ（母亲B） 「酒と女は許す。あとギターもだ。ただし、バイクとタバコはゆるさん」やで」
    # 人物表++++++
    voice "voice/その他/ot5_a1_0001.ogg"
    motherb "酒和女人可以，吉他也可以，不过摩托车和香烟不行"

    # 子供Ｃ（孩子C） 「ドラッグは？」
    voice "voice/その他/ot8_a1_0003.ogg"
    childc "Drug呢？"

    # 母親Ｃ（母亲B） 「…ちょっとだけなら」
    # 人物表++++++
    voice "voice/その他/ot5_a1_0002.ogg"
    motherc "……就一点点的话"

    # 子供Ｃ（孩子C） 「わはーい！」
    voice "voice/その他/ot8_a1_0004.ogg"
    childc "哇——耶！"

    # nil 「注・ダメです。」
    # 这是原作写的
    "注・不行！"

    # luckykeeper的吐槽
    luckykeeper "喂喂！你们都给孩子们灌输了什么奇奇怪怪的东西啊喂！"

    # nil 「このように、子供達はそれぞれ今日の感想をにこやかに母親達に話している。」
    "就这样，孩子们各自笑嘻嘻地向母亲们讲述着今天的感想"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「あはは…サンプル全部配っちゃったね…調子乗っちまった…」
    show リオン_基本_杖_悲しい2 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0130.ogg"
    lion リオン_基本_杖_悲しい2 "啊哈哈……样品全发出去了……我太兴奋了……"
    hide リオン_基本_杖_悲しい

    # 莲 「それだけ美味しかったって事だ。評判は上々。良い仕事したんじゃない？」
    # lian "这说明它很好吃，评价很好。不是做的很好吗？"
    lian "这说明味道很棒，评价很好。不是做的很好吗？"

    # 里昂 「うんうん。こんな風なやり方なんて全然考えてなかったから、すっごく新鮮で楽しかったよ！」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0131.ogg"
    lion リオン_基本_杖_にっこり "是啊是啊，我从来没有想过这样的方法，所以我觉得很新鲜，很有趣！"
    hide リオン_基本_杖_悲しい2

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「……」
    voice "voice/その他/mjf_a1_0032.ogg"
    mj MJ_通常 "……"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「マイケルもお疲れ様、よしよし」
    show リオン_基本_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0132.ogg"
    lion リオン_基本_杖_嬉しい "迈克尔也辛苦了，好孩子好孩子"
    hide リオン_基本_杖_にっこり

    # nil 「疲れて眠ってしまった帽子をなでながら、リオンはごそごそとクーラーボックスの中を漁っている。」
    "里昂一边抚摸着因疲劳而睡着的帽子，一边在冷藏箱里啪嗒啪嗒地翻来翻去"

    # 莲 「どうしたんだ？」
    lian "怎么了？"

    # 里昂 「うーんうーん…せっかくだから、蓮くんにお礼をしたいんだけど…」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0133.ogg"
    lion リオン_基本_杖_微笑み "嗯——嗯……难得来一次，我想谢谢你的说……"
    hide リオン_基本_杖_嬉しい

    # 莲 「気にするなよ。俺からすれば、今日の予定が埋まっただけでも―」
    lian "别在意。在我看来，今天的预定被取消了所以没关系"

    # 莲 「……」
    # 肚子叫了……
    play sound "voice/effect/13_お腹が鳴る.ogg"
    lian "……"

    # 里昂 「お腹…すいてるでしょ？」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0134.ogg"
    lion リオン_基本_杖_にっこり "肚子……已经饿了吧？"
    hide リオン_基本_杖_微笑み

    # 莲 「そういえば何も食ってない事を忘れていたよ…」
    lian "这么说来我都忘记了什么都还没吃呢…"

    # 里昂 「にやにや。あわ…マジで無いか…どうしよ…」
    show リオン_基本_杖_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0135.ogg"
    lion リオン_基本_杖_ニタァ "哎呀哎呀……啊……真的吗……怎么办……"
    hide リオン_基本_杖_にっこり

    # 莲 「大丈夫大丈夫。腹は適当に家帰って膨らますからさ」
    lian "没关系没关系，肚子会适当地回家充气的"

    # 里昂 「んー…やだ！」
    show リオン_基本_杖_無表情 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0136.ogg"
    lion リオン_基本_杖_無表情 "嗯——不要！"
    hide リオン_基本_杖_ニタァ

    # 莲 「やだっつってもな…」
    lian "虽然你说不要……"

    # 里昂 「うーん…うーん…よし…」
    show リオン_基本_杖_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0137.ogg"
    lion リオン_基本_杖_ニタァ "嗯……嗯……好……"
    hide リオン_基本_杖_無表情

    # 里昂 「蓮くん蓮くん、ちょっと…目を閉じてくれる…？」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0138.ogg"
    lion リオン_基本_杖_微笑み "莲君莲君，可以稍微……闭下眼睛吗……？"
    hide リオン_基本_杖_ニタァ

    # 莲 「…はい？」
    lian "……啊？"

    # 里昂 「いから！」
    show リオン_基本_杖_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0139.ogg"
    lion リオン_基本_杖_驚き "快点啦！"
    hide リオン_基本_杖_微笑み

    # to black！眼睛闭上！
    scene black with ComposeTransition(ImageDissolve("images/tr/ysr007.png", 0.3, ramplen=8, reverse=False, alpha=True, time_warp=None),before=None,after=Pause(0.3))

    # nil 「言われるがまに俺は目を閉じる。」
    "按照里昂说的那样闭上眼睛"

    # 里昂 「…よし、そのまで居て…ね？」
    voice "voice/リオン/ron_a1_0140.ogg"
    lion リオン_基本_杖_にっこり "……好，就这样呆着……好吗？"

    # 莲 「あ、ああ…」
    lian "啊，啊啊…"

    # nil 「女の子から目を閉じて…と言われる時は…。」
    "被女孩子说让闭上眼睛的时候…"

    # nil 「正直、経験はなかったが、大体相場ってもんがある。」
    "老实说，虽然没有经验，但大致上还是有数的"

    # nil 「まさかな…。」
    "不会吧…"

    # nil 「とはいえ、一日バイトを手伝ったぐらいでそういうことするか？」
    "话虽如此，只是帮忙打工一天就这么做了吗？"

    # nil 「まぁ、外人さんだし、そのぐらいは挨拶みたいなもんか。」
    "嘛，外国人的话，这种程度的问候也没什么"

    # nil 「俺個人としても、美人さんにお礼として貰うのは勿論悪い気はしない。」
    "于我个人而言，得到美女的感谢当然也不会觉得不好"

    # nil 「腹は膨らまんが…そんなことどうでもいぐらいだ。」
    "虽然不能填饱肚子…不过那种事怎么样都无所谓"

    # nil 「と、このように考えを張り巡らせながら、待っておりましたが…。」
    "我一边这样反复思考，一边等着…"

    # 里昂 「よし、目を開けていよ」
    voice "voice/リオン/ron_a1_0141.ogg"
    lion リオン_基本_杖_嬉しい "好，可以睁开眼睛了哦"

    # 眼睛睁开了
    scene 通学路d_夕 at love69_bg1440 with ComposeTransition(ImageDissolve("images/tr/ysr007.png", 0.3, ramplen=8, reverse=True, alpha=True, time_warp=None),before=None,after=Pause(0.3))

    # 莲 「へ？」
    lian "欸？"

    # 里昂 「くすっ。何を期待してたの？」
    show リオン_基本_杖_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0142.ogg"
    lion リオン_基本_杖_ニタァ "欸嘿，你在期待什么呢？"

    # 莲 「いやぁ…お礼にキッスでもしてくれるのかなって」
    lian "没有……我在想你会不会吻我以示感谢"

    # 里昂 「んー？　キスのがよかった？　いけどお腹膨らまないよー？」
    show リオン_基本_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0143.ogg"
    lion リオン_基本_杖_嬉しい "嗯——？想要我吻你嘛？虽然可以，但是肚子可是没法填饱的哦——？"
    hide リオン_基本_杖_ニタァ

    # nil 「リオンは微笑みながら、俺に何かを手渡した。」
    "里昂微笑着把什么东西递给了我"

    # 里昂 「じゃーん♪」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0144.ogg"
    lion リオン_基本_杖_にっこり "锵——♪"
    hide リオン_基本_杖_嬉しい

    # 莲 「ビ、ビニール袋だ…！　（ゴシゴシ）ビニール袋だ！！！」
    lian "塑、塑料袋……！（捏捏）是塑料袋！！！"

    # 里昂 「中身も入ってるよ！？　ただの嫌がらせじゃないか、それじゃぁさ」
    show リオン_基本_杖_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0145.ogg"
    lion リオン_基本_杖_驚き "里面也是有东西的哦！？只是这样的话不就是骚扰了嘛，这样的"
    hide リオン_基本_杖_にっこり

    # 莲 「…アイス？　バカな…全て配り終えたはずなのに…！」
    lian "……冰淇淋？真假……明明刚才已经全部都发完了……！"

    # 里昂 「全てと言ったな…あれは嘘だ」
    show リオン_基本_杖_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0146.ogg"
    lion リオン_基本_杖_ニタァ "所说的一切……都是谎言"
    hide リオン_基本_杖_驚き

    # 莲 「貴様ァア！　一体どこにこの量を隠しもっていたんだ！」
    lian "你这家伙！到底把这么多的冰淇淋都藏在什么地方了！"

    # 里昂 「秘密ー！　だから目をつぶってっていったのさ！」
    voice "voice/リオン/ron_a1_0147.ogg"
    lion "是秘密——！所以我才叫你闭上眼睛的啦！"

    # 莲 「もう一度言ってみろ」
    lian "再说一遍"

    # 里昂 「秘密ー！　だから目をつぶってっていったのさ！」
    voice "voice/リオン/ron_a1_0148.ogg"
    lion "是秘密——！所以我才叫你闭上眼睛的啦！"

    # 莲 「なるほど」
    lian "原来如此"

    # nil 「リオンから受け取った可愛らしい手提げ部分のついたビニール袋には、カップに入ったアイスクリームが複数詰め込まれていた。あと大量のドライアイス。」
    "从里昂那里收到了一个可爱的手提袋，里面装着多个装在杯子里的冰淇淋。还有大量的干冰"

    # 里昂 「家族みんなで食べてよ！　結局蓮くん、私のアイス食べてないしさ！美味しいよ？」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0149.ogg"
    lion リオン_基本_杖_にっこり "全家一起吃吧！毕竟莲君还没吃过我的冰淇淋呢！很好吃的哦？"
    hide リオン_基本_杖_ニタァ

    # 莲 「恋が叶うってやつか？」
    lian "你是说实现恋爱的那个？"

    # 里昂 「あはー、あれは作るのに時間がかるし、色々大変なのだよ…だから、これは普通の美味しいアイスだよー」
    show リオン_基本_杖_悲しい2 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0150.ogg"
    lion リオン_基本_杖_悲しい2 "啊哈哈，那个做起来很费时间，也很辛苦……所以，这些只是普通的好吃的冰淇淋哟——"
    hide リオン_基本_杖_にっこり

    # 莲 「そ、そうか…なんか作るの大変なのに自分で食べさせちまってすまないな」
    lian "是、是这样吗…明明做的很辛苦，却让你自己吃，真是对不起啊"

    # 里昂 「いよいよ。だからこそ…かどうかはわからないけど、こうして、蓮くんと一緒に楽しい事できたし…」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0151.ogg"
    lion リオン_基本_杖_微笑み "没事没事，所以才……虽然不知道是不是这个的原因，我才能和莲君一起做这样快乐的事情……"
    hide リオン_基本_杖_悲しい2

    # 里昂 「あは、マジで私の恋が叶っちゃう系…かな？」
    show リオン_基本_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0152.ogg"
    lion リオン_基本_杖_嬉しい "啊哈，如果我的爱情真的会实现的……话？"
    hide リオン_基本_杖_微笑み

    # 莲 「おいおい恥ずかしい事を言うなよ」
    lian "好啦好啦别说害羞的话了"

    # 里昂 「照れちゃってかわいー！」
    show リオン_基本_杖_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0153.ogg"
    lion リオン_基本_杖_ニタァ "害羞了好可爱——！"
    hide リオン_基本_杖_嬉しい

    # 莲 「ぐぬぬ」
    lian "咕奴奴"

    # nil 「オレンジ色の陽光が降り注ぐ中、なんとも若者らしいきゃっきゃうふを楽しむ。」
    "在橙色的阳光倾泻下来的时候，享受着年轻人特有的乐趣"

    # nil 「普段、真冬や心愛とも仲良くはしているが、こう、他人とこんな風に触れあうのは…はじめてかもしれない。」
    "平时和真冬、心爱的关系都很好，但是像这样和别人接触……可能还是第一次"

    # nil 「だから余計に気恥ずかしい。」
    "所以更害羞了"

    # 莲 「で、キスはしてくれないのか」
    lian "那么，你不吻我吗？"

    # 里昂 「ぶっ！　さりげなく忘れてはいなかったのね…。この雰囲気になってから言うのは…ちょっと…ずるい…よ…？」
    show リオン_基本_杖_ジト目 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0154.ogg"
    lion リオン_基本_杖_ジト目 "噗！还是念念不忘啊……在这样的气氛下说的话……有点……太狡猾了……哦……？"
    hide リオン_基本_杖_ニタァ

    # 莲 「ははは、仕返しってやつだ」
    lian "哈哈哈，这是报复哦"

    # nil 「リオンは赤くなって、照れたように視線をそらした。やはり、外人さんとはいえ、こういう時は恥ずかしいのだろう。」
    "里昂脸红了，害羞地移开了视线。虽说是外国人，但在这种时候还是觉得不好意思吧"

    # nil 「さて、あいつらのバイトも終わってるし、帰るとするか。」
    "那么，这里的打工也结束了，回去吧"

    # 莲 「じゃ、俺はそろそろ帰るよ。今日は本当に楽しかった。ありがとな、リオン」
    lian "那么，我差不多该回去了。今天真的很开心。谢谢你，里昂"

    # 里昂 「えっ…あっ、待って、待って蓮くん！」
    show リオン_基本_杖_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0155.ogg"
    lion リオン_基本_杖_驚き "欸……啊，等等，等等，莲君！"
    hide リオン_基本_杖_ジト目

    # 莲 「ん？」
    lian "嗯？"

    # 里昂 「これこれ、私の連絡先！　こまできて、連絡先を教えないっていうのは、ちょっと寂しいじゃんか！」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0156.ogg"
    lion リオン_基本_杖_微笑み "这个这个，我的联系方式！都到现在了，还不告诉我联系方式的话，不是会觉得有点寂寞吗！"
    hide リオン_基本_杖_驚き

    # nil 「そういながら、リオンはスマートフォンの画面にＱＲコードを表示させて、こちらに見せてくる。」
    "这样说着，里昂的智能手机的画面上显示了二维码，让我来扫"

    # nil 「なるほど、これを読み取るだけで、連絡先が交換できるのか。ハイテクな世の中だな…。」
    "原来如此，只要扫描这个，就能交换联系方式吗，真是高科技的世界啊…"

    # nil 「俺はスマフォを取り出して、カメラをリオンのスマフォに近づける。」
    "我拿出智能手机，把相机靠近里昂的手机屏幕"

    # nil 「ピッと音が鳴って、読み取りの完了を告げる。」
    "哔的一声，提示读取完成"

    # 莲 「これで…よしっと―」
    lian "这样就…好了——"

    # 里昂接近
    transform love69_lion_bg_center:
        zoom 1.5
        xalign 0.455
        yalign 0.165

    # 里昂 「…ちゅっ」
    hide リオン_基本_杖_微笑み
    show リオン_大_基本_杖_キス at love69_lion_bg_center
    with dissolve
    voice "voice/リオン/ron_a1_0157.ogg"
    lion リオン_基本_杖_キス "……啾"

    # 莲 「っ！」
    lian "嗯！"

    # nil 「瞬間、俺は頬に温かくしめった感触を受けた。」
    "瞬间，我感受到了脸颊上温暖的触感"

    # nil 「キッス…。」
    "Kiss……"

    # 里昂离开
    hide リオン_大_基本_杖_キス
    show リオン_基本_杖_にっこり at love69_lion_center
    with dissolve

    # 里昂 「えへへ。ありがとうの…ちゅー♪　ほっぺだけどね！」
    voice "voice/リオン/ron_a1_0158.ogg"
    lion リオン_基本_杖_にっこり "欸嘿嘿，谢谢的……啾——♪虽然是脸颊呢！"

    # 莲 「お、おう…なんか、こっちも、ありがとう（？）」
    lian "哦，哦…总觉得，这边也谢谢了（？）"

    # 里昂 「えへん！　じゃぁ、またね！　暫くはこにいるから、気軽に連絡してね！」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0159.ogg"
    lion リオン_基本_杖_微笑み "嗯哼！那，再见啦！我会在这里待一段时间，请随时联系我哦！"
    hide リオン_基本_杖_にっこり

    # 莲 「あ。今夜あたり電話するわ」
    lian "啊，那今晚就给你打电话"

    # 里昂 「はえーなおい。で、でも、いよ！　待ってる！　じゃぁねー！アイスが溶ける前に帰るんだぞー！」
    show リオン_基本_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0160.ogg"
    lion リオン_基本_杖_嬉しい "好快啊你这。但，但是，好的！我会等着的哦！再见喽！在冰淇淋融化之前回家吧——！"
    hide リオン_基本_杖_微笑み

    # 莲 「おうよ。リオンもマイケルも気をつけてな」
    lian "喔，里昂和迈克尔也要路上小心啊"

    # 里昂 「アディオスアミーゴ！！」
    show リオン_基本_杖_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0161.ogg"
    lion リオン_基本_杖_ニタァ "Adiós・amigo！！"
    hide リオン_基本_杖_嬉しい

    # 莲 「アディオースセニョリータ」
    lian "Adiós Señorita（L:意思是「再见,小姐」依然是西班牙语）"

    # nil 「俺はリオンに背を向けて、右手を高くあげて別れを告げる。」
    "我背向里昂，举起右手告别"

    # 场景切换到通学路街道
    play music bgmfifty fadeout 2.0 fadein 2.0
    scene 通学路c_夕 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # scene17 场景1 【今天是在里昂冰淇淋店的打工】 结束

    # scene17 场景2 【偶遇挖洞洞回来的三人组】 开始

    # BGM 变得非常符合夕阳捏

    # nil 「西日が眩しい。」
    "西斜的太阳很是刺眼"

    # ？？？ 「みーちゃったみーちゃったーせーんせーいにいっちゃおー♪」
    # 这里还是用 unknown 表示吧
    voice "voice/想瑠/sol_a1_0019a.ogg"
    unknown404 "看——到——了——看——到——了——我——要——告——诉——老——师——了♪"

    # 莲 「あん？」
    lian "啊？"

    # nil 「リオンと別れてから少した頃だろうか。帰り道を歩く俺に、車道から声をかける不届き者がいるようだ。」
    "大概是和里昂分别不久的时候吧。我走在回家的路上，好像有人从车道上向我打招呼"

    # 莲 「先生もなにも、アンタが先生だろうが」
    lian "老师你怎么了，你就是老师吧"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ちゅーされてやんの。なーにがほっぺにちゅー♪だよ。あちーあちー」
    # 参考资料：あちー https://www.weblio.jp/content/%E3%81%82%E3%81%A1%E3%83%BC
    show 想瑠_スーツ_目閉じ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0020.ogg"
    liu 想瑠_スーツ_目閉じ "啾——是怎么回事啊，为什么被啾——脸颊了啊，好热好热（L:最后的好热好热「あちーあちー」是但马方言，但马位于现在的兵库县北部，也就是兵库北！）"

    # nil 「声の主は担任だった。」
    "声音的主人是班主任"

    # 莲 「ＢＭＷの四人乗りのオープンカー…ガブリオレか…良い車乗ってやがるな、パートのくせに」
    lian "ＢＭＷ的4人座的Open Car……Cabriolet吗…开的车不戳啊，明明是兼职的（L:前面的Open Car和后面的Cabriolet都是敞篷车的意思）"

    # 想瑠 「この車買っちまったからパートしてんだよ！　ホットドック屋だけじゃ食えなくなったからな！」
    show 想瑠_スーツ_本気 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0021.ogg"
    liu 想瑠_スーツ_本気 "就是因为我买了这辆车，所以才打零工的啊！因为我没法只靠卖热狗吃上饭了！（L:还记得一周目迪士尼乐园的热狗嘛）"
    hide 想瑠_スーツ_目閉じ

    # 莲 「ホットドッグでも食ってろよ…」
    lian "那就去吃热狗啊……"

    # 想瑠 「そ、その手があったかァー！」
    show 想瑠_スーツ_驚き at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0022.ogg"
    liu 想瑠_スーツ_驚き "原、原来有这招啊！"
    hide 想瑠_スーツ_本気

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「蓮くんやっほー！　ねぇねぇ、さっきのもしかして彼女？」
    show 心愛_制服_基本_ニタァ at love69_right with dissolve
    voice "voice/心愛/cca_a1_0137.ogg"
    ai 心愛_制服_基本_ニタァ "莲君Yahoo——！呐呐，刚才那个莫非是女朋友？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ほっぺにキスした所までは見たけど、どこまで行ったの？」
    show 真冬_制服_基本_ニタァ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0139.ogg"
    dong 真冬_制服_基本_ニタァ "看到你被亲吻脸颊了，到哪一步了？"

    # nil 「後部座席から、にょきっ　にょきっと心愛と真冬が顔を出す。」
    "从后排座位上，心爱和真冬探出头来"

    # 莲 「よう、お前らも一緒か。温泉掘りのバイトお疲れさん」
    lian "哟，你们一起的吗？挖温泉的打工辛苦了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「いぇい！　ガンガン掘ってきたぜ…ドリルでな…」
    show 心愛_制服_基本_微笑み at love69_right with dissolve
    voice "voice/心愛/cca_a1_0138.ogg"
    ai 心愛_制服_基本_微笑み "Yeah！挖了好多呢……用钻头……"
    hide 心愛_制服_基本_ニタァ

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そして、今から帰りに銭湯にいくのです」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0140.ogg"
    dong 真冬_制服_基本_無表情 "然后，现在回去的路上要去澡堂"
    hide 真冬_制服_基本_ニタァ

    # 莲 「なんだよ羨ましいな。俺も一緒に連れてってくれよ」
    lian "什么啊，好羡慕啊。也一起带我去吧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「えー…でも、女湯には入れないよー？」
    show 心愛_制服_基本_無表情 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0139.ogg"
    ai 心愛_制服_基本_無表情 "嗯……但是，你不能进女浴池哦？"
    hide 心愛_制服_基本_微笑み

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「お兄ちゃんに彼女がいなかったら入れてあげてもよかったのにね」
    show 真冬_制服_基本_にっこり at love69_left with dissolve
    voice "voice/真冬/maf_a1_0141.ogg"
    dong 真冬_制服_基本_にっこり "如果欧尼酱没有女朋友的话，我倒是也可以让你进来"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「おいやめろ。ついでに私まで裸見られちまうじゃないか」
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0023.ogg"
    liu 想瑠_スーツ_見下し "喂快停下来，这样的话我的裸体会被顺带看到的"
    hide 想瑠_スーツ_驚き

    # 莲 「いじゃねぇないですか！」
    lian "有什么不好的啊！"

    # 想瑠 「だめだ！　今回は絶対に脱がないって決めたんだからな！」
    show 想瑠_スーツ_驚き at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0024.ogg"
    liu 想瑠_スーツ_驚き "不可以！我已经决定这次绝对不会脱衣服了！"
    hide 想瑠_スーツ_見下し

    # 想瑠 「私の裸が見たければ1年ほど時を遡ってくれよな！！」
    show 想瑠_スーツ_ニヤリ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0025.ogg"
    liu 想瑠_スーツ_ニヤリ "如果你想看我的裸体，你就得回到一年前！！（L:指12年发布的S.I.S.T.A.R.S:KISS OF TRINITY）"
    hide 想瑠_スーツ_驚き

    # 想瑠 「な！」
    show 想瑠_スーツ_にっこり at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0026.ogg"
    liu 想瑠_スーツ_にっこり "呐！"
    hide 想瑠_スーツ_ニヤリ

    # 莲 「うるせえ」
    lian "无路赛"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「と、いうことで、銭湯にいってきます」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0142.ogg"
    dong 真冬_制服_基本_微笑み "所以，就是这样，我们要去澡堂了"
    hide 真冬_制服_基本_にっこり

    # 莲 「え！？　そこは乗せてくれないのかよ！」
    lian "诶！？不载我去那里吗！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「どーしよっかなー？　今私達汗臭いしなー」
    show 心愛_制服_基本_ニタァ at love69_right with dissolve
    voice "voice/心愛/cca_a1_0140.ogg"
    ai 心愛_制服_基本_ニタァ "怎么办呢？我们现在浑身都是汗味……"
    hide 心愛_制服_基本_無表情

    # 莲 「いよ気にしないし」
    lian "我不介意"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「私達が気にするんだけど…まぁいや、ほら、心愛ちゃん助手席いって」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0143.ogg"
    dong 真冬_制服_基本_無表情 "我们很在意……算了，来，心爱酱坐副驾驶座"
    hide 真冬_制服_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ほーい」
    show 心愛_制服_基本_にっこり at love69_right with dissolve
    voice "voice/心愛/cca_a1_0141.ogg"
    ai 心愛_制服_基本_にっこり "好~"
    hide 心愛_制服_基本_ニタァ

    # nil 「心愛は後部座席からぴょーんとハンドスプリングで助手席に乗り移った。相変わらず凄まじい運動神経だ。」
    "心爱从后座嗖的一声用Handspring跳到副驾驶座，依旧是惊人的运动神经（L:Handspring，前手翻腾越，体操名词，就我个人感觉就是前空翻）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「じゃぁほら、私の隣どうぞ」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0144.ogg"
    dong 真冬_制服_基本_微笑み "那么，来，请坐在我旁边"
    hide 真冬_制服_基本_無表情

    # 莲 「うっす、お邪魔しまーす」
    lian "嗯，打扰了"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「少しは君ら私に、許可をとろうと思った事はないのかい！？」
    show 想瑠_スーツ_真顔 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0027.ogg"
    liu 想瑠_スーツ_真顔 "你们难道就没有稍微想过一下请求我的允许吗？"
    hide 想瑠_スーツ_にっこり

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「いよな？」
    show 心愛_制服_基本_ニタァ at love69_right with dissolve
    voice "voice/心愛/cca_a1_0142.ogg"
    ai 心愛_制服_基本_ニタァ "可以的吧？"
    hide 心愛_制服_基本_にっこり

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「は、はい」
    show 想瑠_スーツ_悲しみ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0028.ogg"
    liu 想瑠_スーツ_悲しみ "嗯，是的"
    hide 想瑠_スーツ_真顔

    # 莲 「ほら、お土産のアイスあげるから。全員分あるぞ」
    lian "来，给你们特产冰淇淋，所有人都有哦"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「わーい」
    # 这里虽然是几个人的 声音，但是原文没有用引用括号，也没有标，还是就按照真冬来好了
    show 想瑠_スーツ_にっこり at love69_xiangliu_center
    show 真冬_制服_基本_にっこり at love69_left
    show 心愛_制服_基本_きらきら at love69_right
    with dissolve
    voice "voice/真冬/maf_a1_0145.ogg"
    dong 真冬_制服_基本_にっこり "哇——咿"
    hide 想瑠_スーツ_悲しみ
    hide 心愛_制服_基本_ニタァ

    # 莲 「あんたは運転したまえ」
    lian "你开车吧"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「びええええええ」
    show 想瑠_スーツ_ぶわ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0030.ogg"
    liu 想瑠_スーツ_ぶわ "呜欸欸欸欸欸"
    hide 想瑠_スーツ_にっこり

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「じゃぁ私があーんしてあげるよ！」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0144.ogg"
    ai 心愛_制服_基本_笑顔 "那我来帮你“啊——”吧"
    hide 心愛_制服_基本_きらきら

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ぅん」
    show 想瑠_スーツ_照れ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0031.ogg"
    liu 想瑠_スーツ_照れ "嗯"
    hide 想瑠_スーツ_ぶわ

    # nil 「……」
    "……"

    # 莲 「あ、ごめん、スプーン貰ってないから素手で食って」
    lian "啊，对不起，我没拿勺子，空着手吃吧（L:莲拿到的冰淇淋是装在杯子里面的那种）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まふ。まふまふまふ…あ…おいし…まふまふ」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0146.ogg"
    dong 真冬_制服_基本_無表情 "嘛呼，嘛呼嘛呼嘛呼……哈，真好吃……嘛呼嘛呼"
    hide 真冬_制服_基本_にっこり

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「じゃぁあ～んってできないじゃんかよぉ！」
    show 想瑠_スーツ_驚き at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0032.ogg"
    liu 想瑠_スーツ_驚き "那不是就不能“啊”的恰了嘛"
    hide 想瑠_スーツ_照れ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「いや、素手でやってみせるさ！　…つめてぇっ！」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0145.ogg"
    ai 心愛_制服_基本_真顔 "咿呀，我也要空手来干了！……冷死了！"
    hide 心愛_制服_基本_笑顔

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「当たり前だ！」
    voice "voice/想瑠/sol_a1_0033.ogg"
    liu "那不是当然的嘛！"

    # nil 「ちなみに、アイスは本当に美味しかったです。ありがとうリオン。」
    "随便一提，冰淇淋真的很好吃。谢谢你，里昂"

    # 场景切换：通学路街道->澡堂（黄昏）
    image bg 銭湯_夕 = "images/bg/銭湯_夕.png"
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 銭湯_夕 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # nil 「銭湯にて。」
    "在澡堂里"

    # 这之后涉及不大能放出来的部分捏

    # 稍微 Check 了一下，把对话框的小人物头像改成穿比基尼的好了

    # 去稍微康了一下目前已经完成的内容，用 MS Word 统计了一下，发现 Scene1-16 全部内容已经肝了中英文 296012 字了，用五号字统计了一下，发现用 A4 纸打印的话居然需要打 523 页！！！
    # 我这么能肝的嘛！看到这么能肝的我，这不呼朋唤友来给我个 Star 嘛~
    # 然后又去提前 C 了一下还没做的内容，发现二周目似乎比一周目短不少
    # 感觉离做完越来越近了捏

    # 另外，这个月的百度翻译 API 20 万字的免费翻译字数马上就用完了捏……
    # 因为这个原因，可能后面的进度要稍微慢一点点了，这个期间的进度就要靠 DeepL 和 彩云小译 喽~

    # 接着肝，今天（2022年1月17日）做完 Scene 17！

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「おひょおうケロリンを食らえ－！」
    voice "voice/心愛/cca_a1_0146.ogg"
    ai 心愛_水着_基本_ニタァ "呼喵，给我吃掉ケロリン吧——！！！（L:一周目莲、真冬、心爱和好之后独自回家的莲君就差点儿被ケロリン的陷阱坑了，回想起来ケロリン是什么了嘛）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「心愛ちゃんヘイパース！」
    voice "voice/真冬/maf_a1_0147.ogg"
    dong 真冬_水着_基本_ニタァ "心爱酱Hey Pass！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「パーッス！」
    voice "voice/心愛/cca_a1_0147.ogg"
    ai 心愛_水着_基本_もぐもぐ "PASS！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「アターック！」
    voice "voice/真冬/maf_a1_0148.ogg"
    dong 真冬_水着_基本_本気 "Attack！"

    # nil 「スコーンッ！」
    # 这里可不是说司康饼（Scone）哦 https://ja.wikipedia.org/wiki/%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%B3
    "嘶咣！"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # L:这里的想瑠被打马赛克了2333
    # 想瑠 「ギャァーッ！！」
    voice "voice/想瑠/sol_a1_0034.ogg"
    liu 想瑠_風呂_ぐるぐる "嘎——！！"

    # 莲 「お前ら少しは静かに風呂入れや！」
    lian "你们稍微安静点洗澡吧！"

    # 场景切换：澡堂->商店（酒店）街（晚上了）
    image bg 商店街_夜 = "images/bg/商店街_夜.png"
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 商店街_夜 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # nil 「帰りは送ってもらいました。」
    "她们送我回家了"

    # nil 「でも、心愛ちゃんがケロリンをパクってきたので、返しにいきました。」
    "但是，因为心爱酱顺走了ケロリン，所以我就去还了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あ私のケロリンがァッ！」
    show 心愛_制服_基本_ポカーン at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0148.ogg"
    ai 心愛_制服_基本_ポカーン "哇我的ケロリン啊！"

    # 莲 「今度買ってあげるから今日は我慢しなさい」
    lian "下次回去会给你买一个的，今天就先忍耐一下吧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ほんとだな！？　約束したからな！？」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0149.ogg"
    ai 心愛_制服_基本_真顔 "真的吗！？约定好了啊！？"
    hide 心愛_制服_基本_ポカーン

    # nil 「ちなみに、ケロリンとは、あの黄色いプラスチック製の桶の事です。お土産に最適！」
    "顺便说一下，所谓的「ケロリン」是指那个黄色塑料桶，最适合当纪念品了！"

    # nil 「流石に想瑠にゃんは送ってくれなかったので、徒歩で帰宅です。」
    "因为想瑠喵没有送我去，所以我得步行回家"

    # nil 「銭湯で買った瓶のコーラを飲みながら、湯気を立てながら帰宅。」
    "一边喝在澡堂买的瓶装可乐，一边冒着热气回家"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    hide 心愛_制服_基本_真顔
    show 心愛_制服_基本_真顔:
        zoom 1.5
        xalign 0.53
        yalign -0.09
        linear 0.3 xalign 0.8918

    # 真冬 「あ、そうだ。お兄ちゃん。私ら、これから行く所あるから」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0149.ogg"
    dong 真冬_制服_基本_無表情 "啊，对了，欧尼酱，我们还有别的地方要去"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はわ！　そうそう言い忘れてました！　ちょっと真冬ちゃんとデートしてきてもいですかお兄さん！」
    show 心愛_制服_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0150.ogg"
    # ai 心愛_制服_基本_驚き "呼哇！对了对了，忘了告诉你了！我可以稍微和真冬酱约会一下吗，大哥？"
    ai 心愛_制服_基本_驚き "呼哇！对了对了，忘了告诉你了！我可以稍微和真冬酱约会一下吗，哥哥？"
    hide 心愛_制服_基本_真顔

    # 莲 「んお？　いや、全然いけど、どっかいくの？　今から？」
    lian "嗯？没事，完全可以的，要去哪里？现在开始？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「えへーそれは秘密－！」
    show 心愛_制服_基本_ニタァ at love69_right with dissolve
    voice "voice/心愛/cca_a1_0151.ogg"
    ai 心愛_制服_基本_ニタァ "欸嘿嘿——这个是秘密啦！"
    hide 心愛_制服_基本_驚き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「秘密ー♪　ねー？」
    show 真冬_制服_基本_にっこり at love69_left with dissolve
    voice "voice/真冬/maf_a1_0150.ogg"
    dong 真冬_制服_基本_にっこり "秘密啦♪呐？"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ねー！」
    show 心愛_制服_基本_にっこり at love69_right with dissolve
    voice "voice/心愛/cca_a1_0152.ogg"
    ai 心愛_制服_基本_にっこり "呐！"
    hide 心愛_制服_基本_ニタァ

    # 莲 「言えよ」
    lian "说吧"

    # 心爱 「ぐふっ！　い、言わぬ…これだけは言わぬ…！」
    show 心愛_制服_基本_ぶわー at love69_right with dissolve
    voice "voice/心愛/cca_a1_0153.ogg"
    ai 心愛_制服_基本_ぶわー "咕哇！不、不会说的……只有这个不会说的……！"
    hide 心愛_制服_基本_にっこり

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まぁ、いずれわかるから、ちょっと待ってね」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0151.ogg"
    dong 真冬_制服_基本_微笑み "嘛，稍微等一等，早晚会知道的"
    hide 真冬_制服_基本_にっこり

    # 莲 「そうか。じゃぁ待ってる」
    lian "是吗？那我等着"

    # nil 「…そして、その夜、二人はホテル街へと消えていきました。」
    "…然后，是夜，两个人消失在酒店街上（L:嗯，就是酒店街，不是一般的商店街呢）"

    hide 真冬_制服_基本_微笑み
    hide 心愛_制服_基本_ぶわー
    with dissolve

    # nil 「ホテル街へと…。」
    "去酒店街…"

    # scene17 场景2 【偶遇挖洞洞回来的三人组】 结束

    # scene17 场景3 【再次和里昂演纸芝居】 开始

    # 画面：SEND ，和 CALL 再做一个 Screen 就 OK
    show screen send
    play sound "voice/effect/18_携帯電話操作音1.ogg"

    # 莲 「…もしもし、リオン？」
    lian "喂，里昂？"

    # 里昂的电话
    hide screen send

    # 这个语句是针对电话里的里昂设计的参数，能够调整电话里的里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.04
    $ sideimagesize.SideImageYalign = 1.04
    $ sideimagesize.SideImageZoom = 0.6

    # 里昂 「『お、やっほー！　電話待ってたよ！　今日はお疲れ様！』」
    voice "voice/リオン/ron_a1_0162.ogg"
    lion リオン_通話中 "哦哦，Yahoo——！我一直在等你的电话！今天辛苦了！"

    # 莲 「おっす。今、暇か？」
    lian "哦，现在有空吗？"

    # 里昂 「『んー？　ルービックキューブと格闘してる事以外は暇だけど？』」
    voice "voice/リオン/ron_a1_0163.ogg"
    lion "嗯？除了和魔方格斗以外，还有时间吗？"

    # 莲 「じゃぁ、ちょっと話できないか？　妹と幼馴染みが夜のデートにでかけちまって暇なんだよ」
    lian "那么，可以稍微来聊聊天儿嘛？妹妹还有幼驯染晚上出去约会了所以我很闲"

    # 里昂 「『おう！？　いよ！　通話料もったいないから、アプリの方で折り返してかけ直すね！』」
    voice "voice/リオン/ron_a1_0164.ogg"
    lion "哦！？好啊！这样太浪费电话费了，我去应用程序那边再打给你！"

    # nil 「その夜。俺は真冬と心愛の件は話さず、リオンと、どうでもいような事をひたすら話し続けた。ケロリンの事とか。」
    "那晚，我没有谈及真冬和心爱的事情，只是一个劲地和里昂聊着无关紧要的事情，比如ケロリン的事情"

    # 莲 「なぁ、リオン…言い忘れてたんだが…」
    lian "啊，里昂…我忘记说了…"

    # 里昂 「『はいはい、なにかな！』」
    voice "voice/リオン/ron_a1_0165.ogg"
    lion "『嗯嗯，什么事情呢！』"

    # 莲 「今日のさ…紙芝居だけど、また一緒にやらないか？」
    lian "今天的……纸芝居，还要再一起演嘛？"

    # 里昂 「『え！？　い、いの？　でもほんと、お礼とかはできないけど…』」
    # lion "『啊？真、真的吗？不过，说真的，我实在没办法谢你……』"
    voice "voice/リオン/ron_a1_0166.ogg"
    lion "『啊？真、真的吗？不过，说真的，我实在没有什么礼物来谢谢你……』"

    # 莲 「いんだよ。リオンと一緒に居るのが楽しかったんだ。もっと仲良くなろうぜ」
    lian "是啊，和里昂在一起很开心，我们应该更亲密一点"

    # 里昂 「『っ…！！　…うん…わかった。じゃぁ…明日…またあの場所で』」
    voice "voice/リオン/ron_a1_0167.ogg"
    lion "『呃……！！嗯……知道了。那……明天……那个地方见！』"

    # 莲 「おう」
    lian "嗯"

    # 场景切换到街道（第二天白天）
    play music bgmfourteen fadeout 2.0 fadein 2.0
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 通学路d_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # nil 「そして翌日。」
    "然后第二天"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「やったぁあ！　仔猫だァアアアア！！」
    show リオン_基本_杖_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0168.ogg"
    lion リオン_基本_杖_ニタァ "好耶！是小猫咪啊啊啊啊！！"

    # 仔猫（小猫） 「ニャー♪」
    voice "voice/その他/cat_a1_0006.ogg"
    neko "喵呜♪"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ニャー♪」
    show 真冬_制服_基本_にっこり at love69_left with dissolve
    voice "voice/真冬/maf_a1_0152.ogg"
    dong 真冬_制服_基本_にっこり "喵呜♪"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ニャー♪」
    show 心愛_制服_基本_にっこり at love69_right with dissolve
    voice "voice/心愛/cca_a1_0154.ogg"
    ai 心愛_制服_基本_にっこり "喵呜♪"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「なんですかこれは」
    show 想瑠_スーツ_本気 at love69_xiangliu_rightest with dissolve
    voice "voice/想瑠/sol_a1_0035.ogg"
    liu 想瑠_スーツ_本気 "这是什么啊"

    # scene17 场景3 【再次和里昂演纸芝居】 结束

    # Scene17 结束！

    # 过场：里昂（常服）

    # 之前用了这个方法，需要手动控制
    window hide # 隐藏对话框等其它窗口

    # 隐藏 quick_menu
    $ quick_menu = False

    play sound "voice/effect/moosehead honk (stinger).ogg"
    # hide screen quick_menu
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)
    scene アイキャッチリオン with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)

    $ renpy.pause(1.5, hard=True)
    $ renpy.end_replay()

    jump scene18

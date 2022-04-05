# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene18 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：
# 版本 0.9 "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年4月5日

# 当前流程：编写脚本AIO Process

label scene18:
    # scene18 开始

    # scene18 场景1 【和里昂一起奇迹般的春夏秋冬】 开始

    # 地点：街道
    # 人物：莲 真冬 心爱 里昂 MJ 想瑠
    # BGM：
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)
    # scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 通学路d_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    $ quick_menu = True

    show リオン_基本_杖_驚き at love69_lion_center with dissolve
    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「そして、幾星霜の月日が流れた…」
    # 参考资料：https://ko-to-ba.com/ikuseisou/
    voice "voice/その他/mjf_a1_0033.ogg"
    mj MJ_通常 "然后，几星霜的岁月流逝了……（L:幾星霜の月日形容非常非常长的时间）"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「一週間ぐらいだよ！？」
    voice "voice/リオン/ron_a1_0169.ogg"
    lion リオン_基本_杖_驚き "也就大概一个星期吧！？"

    # nil 「という事で、俺はあの日から、リオンと一緒に紙芝居とかのパフォーマンスを交えたアイス販売を行っていた。」
    "就是这样，从那天开始，我和里昂一起进行了纸芝居的表演和冰淇淋销售"

    # nil 「即ち、心愛と真冬と過ごす時間よりも、リオンと過ごす時間のが増えている事を意味している。」
    "也就是说，相比与心爱和真冬相处的时间，现在与里昂相处的时间更多"

    # 切换到晴天

    # nil 「晴れの日も。」
    "晴朗的日子"

    # 莲 「『アータタタタタタタタタタタタ温めますかァア！！？』」
    lian "『还要再热一点嘛！！？』"

    # 里昂 「『あ、そのまでいです』」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0170.ogg"
    lion リオン_基本_杖_微笑み "『啊，现在这样就可以了』"
    hide リオン_基本_杖_驚き

    # nil 「雨の日も。」
    image bg 通学路d_雨 = "images/bg/通学路d_雨.png"
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 通学路d_雨 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    "下雨的日子"

    # 莲 「『はい私は今「リオンズマジカルアイスクリームファクトリー」の屋台の前にきています！！！　どうですか売上の方は！！！』」
    lian "『是的，我现在正在「Lion Magical Ice Cream Factory」的摊位前面！！！销售情况怎么样！！！』"

    # 切换到雨天

    # 里昂 「『さっぱり全然です！！！！！　ていうか帰っていですか！！』」
    show リオン_基本_杖_ぶわー at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0171.ogg"
    lion リオン_基本_杖_ぶわー "『完全没有！！！！！！话说可以回去了吗！！』"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「『風邪引くよ…？』」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0155.ogg"
    dong 真冬_制服_基本_無表情 "『会感冒的哟…？』"

    # 切换到大风天气
    image bg 通学路d_曇 = "images/bg/通学路d_曇.png"
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 通学路d_曇 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # nil 「風の日も。」
    "刮风的日子"

    # 循环播放大风声
    play hawaii "voice/effect/02_うなる風_編集.ogg"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「『布団が吹っ飛んできたぞー！！！』」
    show リオン_基本_杖_ニタァ at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0172.ogg"
    lion リオン_基本_杖_ニタァ "『被子都被吹跑了哦！！！』"

    # 莲 「『やったー！！！』」
    lian "『好耶！！！』"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「『あん私のパンツがー！』」
    show 心愛_制服_基本_ぶわー at love69_xinai_left with dissolve
    voice "voice/心愛/cca_a1_0295.ogg"
    ai 心愛_制服_基本_ぶわー "『啊我的胖次啊』"

    # 切换到大雪天气
    stop hawaii
    image bg 通学路d_雪 = "images/bg/通学路d_雪.png"
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 通学路d_雪 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # nil 「雪の日も。」
    "下雪的日子"

    # 莲 「『こさああああああああああきいいいいいいいいいい！！』」
    lian "『好冷冷冷冷冷冷冷冷冷啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊！！』"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「『…なんで真夏に雪が降るんだろう、この国は』」
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0173.ogg"
    lion リオン_基本_杖_悲しい "『……为什么盛夏的时候会下雪呢，这个国家』"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「『どこかで、奇跡が起こったんだよ』」
    show 真冬_制服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0156.ogg"
    dong 真冬_制服_基本_目閉じ "『哪里发生了奇迹啊』"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「『世界が祝福してやがるな…どっかの誰かにおめでとうってな』」
    show 想瑠_スーツ_照れ at love69_xiangliu_right with dissolve
    voice "voice/想瑠/sol_a1_0037.ogg"
    liu 想瑠_スーツ_照れ "『整个世界都在祝福呢……不知道是谁的某个人，祝贺你了啊』"

    # nil 「近所が火事の日も。」
    "附近失火的日子"

    # 切换到晴天
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 通学路d_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「『蓮くん！　だめだって危ないよ！』」
    show リオン_基本_杖_驚き at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0174.ogg"
    lion リオン_基本_杖_驚き "『莲君！不行不行太危险了！』"

    # 莲 「『うるせえ！　中には子供が残ってんだよ！！！』」
    lian "『闭嘴！里面还有孩子呢！！！』"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「『お兄ちゃん…！！！』」
    show 真冬_制服_基本_見下し4 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0157.ogg"
    dong 真冬_制服_基本_見下し4 "『欧尼酱……！！！』"

    # 莲 「『うおー！』」
    lian "『呜哦——！』"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「『っ…！　蓮くん、私もいくよ！！』」
    show リオン_基本_杖_無表情 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0175.ogg"
    lion リオン_基本_杖_無表情 "『呃……！莲君，我也要去！！』"
    hide リオン_基本_杖_驚き

    # 原作又又又出错了
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 通学路d_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 子供Ｄ（孩子D） 「『ママー！！』」
    # 人物表++++++++++++++++
    voice "voice/その他/ex3_a1_0001.ogg"
    childd "妈妈——！！！"

    # 母亲Ｄ（孩子D） 「『ケヴィン…！　あ…ありがとう、ありがとうございます！！』」
    # 人物表++++++++++++++++
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%B1%E3%83%93%E3%83%B3
    voice "voice/その他/ot9_a1_0001.ogg"
    motherd "凯文（L:Kevin，很多架空人物用这个名字，主要英语圈使用，意思是“高贵的出身”或“高贵的教养”）……！啊……谢谢你，谢谢你！！"

    # 莲&里昂 「『よっしゃぁ！！』」
    # 人物表++++++++++++++++++
    # 这俩也开始组CP了233
    show リオン_基本_杖_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0176.ogg"
    lian_lion リオン_基本_杖_ニタァ "『好耶！！』"

    # 特效：樱花飞舞（桜）
    # 这个大概做不了……
    # YU-RIS 引擎封包的原因+600张图显示又会卡的鸭皮

    # nil 「桜舞い散る日も。」
    "樱花飞舞的日子"
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 通学路d_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「『突然ですが、真冬ちゃんとお付き合いしたいと思います』」
    # L:所以一周目心爱&真冬的组合是必然的嘛……只有莲君受伤的世界……
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0296.ogg"
    ai 心愛_制服_基本_笑顔 "『虽然很突然，但是我想和真冬交往』"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「『ということで、お兄ちゃんに許可を貰おうかと思って』」
    show 真冬_制服_基本_嬉しい at love69_left with dissolve
    voice "voice/真冬/maf_a1_0158.ogg"
    dong 真冬_制服_基本_嬉しい "『所以，我想得到欧尼酱的许可』"

    # 莲 「『そうか。お幸せにな』」
    lian "『这样啊，祝你们幸福』"

    # 真冬 「『はーい♪　これからも、宜しくお願いします♪』」
    show 真冬_制服_基本_にっこり at love69_left
    show 心愛_制服_基本_にっこり at love69_right
    with dissolve
    voice "voice/真冬/maf_a1_0159.ogg"
    dong 真冬_制服_基本_にっこり "『好♪今后也请多多关照♪』"
    hide 心愛_制服_基本_笑顔
    hide 真冬_制服_基本_嬉しい

    # 画面切到粉红色的天空
    play music bgmfifty fadeout 2.0 fadein 2.0
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 空_夕a at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「まさか…あの二人が付き合うとはな…」
    lian "没想到…那两个人会交往…"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「……」
    voice "voice/リオン/ron_a1_0177.ogg"
    lion リオン_基本_杖_悲しい "……"

    # nil 「俺とリオンは、ベンチに座りながら、桜吹雪でピンク色に染まる空を見上げていた。」
    "我和里昂坐在长椅上，仰望着被樱吹雪染成粉红色的天空"

    # nil 「この一週間で、リオンのアイスは近所の子供達や学園の生徒達の心を順調に捉え、今では、時間帯によっては行列が出来るほどにまでになった。」
    "在这一周里，里昂的冰淇淋很好地抓住了附近的孩子们和学校的学生们的心，现在，在某些时间段甚至需要排队"

    # nil 「こ最近の異常気象の原因はイマイチ解明されていない。世間ではそれを『奇跡』と呼んでいる。」
    "最近异常气象的原因还没有弄清楚。世人称之为『奇迹』"

    # 莲 「……」
    lian "……"

    # 里昂 「…蓮くん…」
    voice "voice/リオン/ron_a1_0178.ogg"
    lion "…莲君…"

    # nil 「俺はただ、空を見上げながら、何か言葉を発する事もなく。ただ…風だけが目の前を通り過ぎていく。」
    "我只是，仰望着天空，一言不发，只是…只有风从眼前吹过"

    # nil 「リオンは、俺を憂うような表情で見つめてくる。彼女の膝では仔猫が心地よさそうに眠っている。」
    "里昂用忧郁的表情看着我，一只小猫舒服地睡在她的膝盖上"

    # 莲 「きっと…」
    lian "一定…"

    # 里昂 「うん…」
    voice "voice/リオン/ron_a1_0179.ogg"
    lion "嗯…"

    # 莲 「俺の知らない所で…何かあったんだろうな…」
    lian "在我不知道的地方…发生了什么事吧…"

    # 里昂 「そうだね…私達の知らない場所で、二人は関係を育んでいたんだと思う」
    voice "voice/リオン/ron_a1_0180.ogg"
    lion "是啊…我想她们两个人是在我们不知道的地方建立了关系"

    # 莲 「そう…だな…」
    lian "是……的啊……"

    # nil 「俺は言葉を失う。胸が痛いとか、ショックだとか、嫉妬だとか、そういう感情ではなく…。」
    "我说不出话来。不是胸痛、震惊、嫉妒、打击之类的感情…"

    # 里昂 「好きだったの…？　二人の事」
    voice "voice/リオン/ron_a1_0181.ogg"
    lion "喜欢吗……？那两个人"

    # 莲 「んー…」
    lian "嗯——……"

    # nil 「恋愛感情が傷ついたとか。そういう痛みはなかった。二人を素直に祝福してあげたい気持ちはある。」
    "没有失恋那样的伤痛，只是坦率地祝福两个人"

    # nil 「二人が交際しているからって、別に二人との関係はいつも通り、何かが変わる事はない。」
    "即使她们两个开始交往，但我和两个人的关系还是和往常一样，不会有什么变化"

    # nil 「ただ…。」
    "只是…"

    # 莲 「…寂しい…のかな…。こうして変わっていく事が…。一人、取り残されてしまうようで…」
    lian "…感到寂寞……了吗……像这样改变的事情……好像就只有我一个人被留下了……"

    # 里昂 「…一人じゃぁ…ないよ」
    voice "voice/リオン/ron_a1_0182.ogg"
    lion リオン_基本_杖_微笑み "……你不是……一个人哦"

    # nil 「リオンは静かに、穏やかな口調でそう言った。」
    "里昂用平静的语调说着"

    # 里昂 「あの二人が、蓮くんの知らない場所で関係を育んでいたように、蓮くんも、あの二人の知らない場所で…私と…」
    voice "voice/リオン/ron_a1_0183.ogg"
    lion "就像那两个人在莲君不知道的地方培养关系一样，莲君也在那两个人不知道的地方…和我……"

    # 莲 「リオンと？」
    lian "和里昂？"

    # nil 「リオンはそう言って、言葉をつぐんだ。」
    "里昂这样说着，接着又把剩下的话咽了回去"

    # 里昂 「いや…なんでもないよ。でも、蓮くんがよければさ、いつでも連絡してよ。
    voice "voice/リオン/ron_a1_0184.ogg"
    lion "不，没什么。不过，只要莲君愿意的话，可以随时联系我"

    # L:怎么说捏，总是有种，这个莲好像是因为被心爱&真冬抛弃了才选了里昂线，里昂一直都是想白给的，但是又不大好意思抢走心爱&真冬的莲，二周目因为心爱&真冬单独组了CP，才稍稍提起了勇气……这样的感觉

    # 里昂 「私が居る限り、一人になんてさせないから」
    voice "voice/リオン/ron_a1_0185.ogg"
    lion リオン_基本_杖_嬉しい "只要我在，就不会只让你一个人呆着"

    # 莲 「ありがとう、リオン。優しいな」
    lian "谢谢你，里昂，你真是温柔"

    # 里昂 「そっくりそのまお返しするよ。いつもありがとう、蓮くん。お陰様で、アイスの評判も良いし、自信がもてたよ」
    voice "voice/リオン/ron_a1_0186.ogg"
    lion リオン_基本_杖_にっこり "我会原封不动地奉还给你的。一直以来谢谢你，莲君。托你的福，冰淇淋的评价也很好，我也更有自信"

    # 这个注释写于2022年1月18日
    # L：感觉这里是对接了一周目的剧情以及大家并不知道的里昂之前来过的剧情（二周目后面有说，一周目暗示有转校生，应该是莲以前就用亚撒西打动了里昂，所以来报恩来了？）
    # L：如果你还没推完，这里先剧透一下里昂有着让人忘记她的存在的被动技能，一周目真冬和心爱也经常说看到里昂有“既视感”“感觉是朋友&熟人”

    # nil 「リオンはニッコリと笑顔を向けた。」
    "里昂看着小猫微微一笑"

    # nil 「その表情を見た俺は、胸が締め付けられるような、少しだけ苦しい、けど、嫌いじゃない。」
    "看到那个表情的我，胸口像被勒紧一样，稍微有点痛苦，但是，并不讨厌"

    # 里昂 「……」
    voice "voice/リオン/ron_a1_0187.ogg"
    lion リオン_基本_杖_微笑み "……"

    # 莲 「……」
    lian "……"

    # nil 「俺とリオンは言葉もなく見つめ合う。似たような事が、リオンと初めて出会った時にあったっけ…。」
    "我和里昂无言地对视着，我第一次遇到里昂的时候也发生了相似的事情吧…"

    # nil 「あの時と同じように、リオンはにっこりと笑顔を向けつづけてくれている。」
    "和那时一样，里昂一直微笑着"

    # nil 「その笑顔が、隙間あいた心を満たしていくかのように。」
    "那个笑容，仿佛填满了我空洞的心"

    # 画面切回
    scene 通学路d_夕 at love69_bg1440 with dissolve

    # 里昂 「じゃぁ、今日はそろそろ帰るね」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0188.ogg"
    lion リオン_基本_杖_にっこり "那么，今天差不多该回去了"

    # 莲 「ん？　あ、何か予定があるのか？」
    lian "嗯？啊，是有什么预定吗？"

    # 里昂 「うん。ちょっと、やる事があるんだ」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0189.ogg"
    lion リオン_基本_杖_微笑み "嗯，我有点事要做"
    hide リオン_基本_杖_にっこり

    # nil 「リオンはベンチから立ち上がって、屋台を片付けた。」
    "里昂从长椅上站了起来，收拾了路边摊"

    # 仔猫（小猫） 「ニャー♪」
    voice "voice/その他/cat_a1_0007.ogg"
    neko "喵呜♪"

    # nil 「仔猫はリオンの膝からピョコッと降りると、迎えに来ていた母猫の元に駆け寄った。」
    "小猫从里昂的膝盖上一跃而下，跑到迎接它的母猫身边"

    # nil 「別に、毎日過ごしてるし、会おうと思えば会えるのだが、何故か今日は、リオンと別れるのが辛かった。」
    "但是，虽然每天都过着想见面就能见面的日子，但是不知为什么今天和里昂分别很痛苦"

    # nil 「『もっと一緒に居たい』」
    "『想和你多呆一会儿』"

    # nil 「引き留めるわけにはいかないが、そう言えたらどんなに楽だろう。」
    "虽然不能挽留，但如果我能这么说出来的话该多好"

    # 里昂 「…もー、寂しそうな顔しないでよ、また明日会えるじゃんか」
    voice "voice/リオン/ron_a1_0190.ogg"
    lion "……哎，不要摆出一副寂寞的表情嘛，明天不是还能再见面嘛"

    # 莲 「明日、会える…よな？」
    lian "明天，能见面……的吧？"

    # 里昂 「うん。会えるよ。私はまだ…どこにもいかないよ…」
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0191.ogg"
    lion リオン_基本_杖_悲しい "嗯。能见面的。我暂时还……哪儿都不会去……"
    hide リオン_基本_杖_微笑み

    # 莲 「まだ…か…」
    lian "暂时……吗……"

    # 里昂 「うん。まだ…ね」
    voice "voice/リオン/ron_a1_0192.ogg"
    lion "嗯，暂时……"

    # nil 「リオンは意味ありげに”まだ”を強調した。よく考えれば当然の事だ。」
    "里昂意味深长地强调了“暂时”。仔细想想这是理所当然的事情"

    # nil 「リオンは外国人で、アイス屋になるために日本に来ているだけだし、もし事業が成功すれば、日本にずっと居るかもしれないが…世間はそんなに甘くない。」
    "里昂是外国人，只是为了开冰淇淋店才来日本的，如果事业成功的话，也许会一直呆在日本…但是世界没有那样天真的事"

    # nil 「今でこそ順調とはいえ…。」
    "虽说现在很顺利…"

    # nil 「つかは、離れてしまうのか…でもそれは、俺にも言える事だ。俺だって、いつまでもこのまで居られるというわけではない。」
    "话说，会离开的吗……但是，这也不是我能确信的事，就算是我，也不是能肯定一直会呆在这个地方的"

    # 里昂 「…蓮くん」
    show リオン_基本_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0193.ogg"
    lion リオン_基本_杖_嬉しい "…莲君"
    hide リオン_基本_杖_悲しい

    # nil 「リオンは不安げに俺の名前を呼んだ。そして、何かをしようと俺に手を差し伸べるが、途中で引っ込めた。」
    "里昂不安地叫了我的名字。然后，伸出了手想要做些什么，但中途又缩回去了"

    # nil 「一段と強く、風が桜を舞い上げる。」
    "一阵强风，把樱花吹得飞舞起来"

    # nil 「まったく…なんて…」
    "真是的…怎么了啊"

    # nil 「甘酸っぱい夏…なんだ…！」
    "酸甜的夏天…这样的……！"

    # 里昂 「じゃぁ私、帰るから…また明日…ね？」
    voice "voice/リオン/ron_a1_0194.ogg"
    lion "那我回去了…明天见…好吗？"

    ########################################################################################################################################################################################################
    # 以下注释来自2022年1月18日，寒假……
    # L:emmmm………………翻到这里总是也感觉到些许心酸，W等到22年6月之后就不能见面了呢……在线下可能可以和W一起玩的时间大概也就只剩1-2个月了……就像这里莲担心的那样，W也将要前往里昂所在的嘤国留学了……不知道什么时候，会不会回国捏……
    # L:嘛，想到这里，就把本作作为W的饯别礼好了，希望他能够早日平安的从海外归来吧（虽然他现在还没出去而且天天还在一边原一边摸鱼）
    # L:W你要是康到了这里的话，等去了那边之后记得多来找我聊天哦~
    # L:W打算在本行的下一行说点儿什么嘛
    # （L给W预留的位置，如果要写的话记得加上日期哦）
    ########################################################################################################################################################################################################

    # 莲 「なぁ、リオン！」
    lian "呐，里昂！"

    # nil 「俺に背を向けたリオンに声をかける。」
    "向背向我的里昂打招呼"

    # 里昂 「は、はいっ！」
    show リオン_基本_杖_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0195.ogg"
    lion リオン_基本_杖_驚き "哈，是！"
    hide リオン_基本_杖_嬉しい

    # nil 「ちょっとテンパった様子で、背筋を伸ばして硬直した。」
    "稍微有点慌张的样子，挺直腰板僵硬在那里"

    # 莲 「俺が夏休み入ったらさ、どっか遊びにいかないか？」
    lian "等我放暑假的时候，一起去哪里玩吧？"

    # 里昂 「…っ！　え、え？　遊びに…？　わ、私と…？」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0196.ogg"
    lion リオン_基本_杖_微笑み "哦！欸、欸？出去玩……？和、和我……？"
    hide リオン_基本_杖_驚き

    # 莲 「あ。一日ぐらい休んでさ。他のアイス屋とかも視察もかねて…どうよ」
    lian "嗯，休息个一天左右吧。同时也去考察考察其他的冰淇淋店…怎么样？"

    # 里昂 「…い、い、いけど、わ、私でいの？」
    show リオン_基本_杖_驚き_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0197.ogg"
    lion リオン_基本_杖_驚き_1 "……可、可、可以的说，是、是我可以吗？"
    hide リオン_基本_杖_微笑み

    # 莲 「妙にテンパってるな…。むしろ、俺はリオンと遊びにいきたいんだが。せっかくだしな、と思って…」
    lian "真是奇怪的说法啊…倒不如说，我想和里昂一起去玩。毕竟好不容易才来的，我是这么觉得的……"

    # 里昂 「だ、だってだってっ…ふ、二人…だ、よね？　デートになっちゃうよ！？」
    show リオン_基本_杖_無表情_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0198.ogg"
    lion リオン_基本_杖_無表情_1 "但、但是但是……两、两个人……去，对吧？会变成约会的哦！？"
    hide リオン_基本_杖_驚き_1

    # 莲 「あ、あ…デートになっちゃうな…。　俺は…まぁ、正直歓迎なんだが、リオンがよければ…だが」
    lian "啊，啊……变成去约会了吗……就我来说……嘛，老实说我很欢迎，如果里昂你觉得可以的话……"

    # 里昂 「私だって大歓迎だよ！」
    show リオン_基本_杖_驚き_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0199.ogg"
    lion リオン_基本_杖_驚き_1 "我也是大欢迎哟！"
    hide リオン_基本_杖_無表情_1

    # 莲 「は、はいっ！」
    lian "好，好！"

    # nil 「今度は俺がテンパる番だった。」
    "这次轮到我慌张了"

    # nil 「リオンは柄にもなく、語気を強めて俺に自分の意志をぶつけてきた。思わず背筋がピンとなる。」
    "里昂没有拐弯抹角，而是语气强硬地向我表达了自己的意志，我不由得脊梁发直"

    # 莲 「じゃ、じゃぁ、なんだ、俺と一緒に遊びにいってくれるのかい？」
    lian "那么，那个，你愿意一起和我一起去玩吗？"

    # 里昂 「い、いともー！」
    show リオン_基本_杖_にっこり_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0200.ogg"
    lion リオン_基本_杖_にっこり_1 "当、当然啦——！"
    hide リオン_基本_杖_驚き_1

    # nil 「リオンは相変わらず小刻みに震えていたが、とりあえず了承はしてくれた。」
    "里昂还是在微微的颤抖着，但还是同意了"

    # nil 「デートに誘うのがこんなに緊張するものだとは…。」
    "没想到约你出去玩居然会这么紧张……"

    # 莲 「と、とりあえず、じゃぁ、予定が決まったら連絡するから…」
    lian "嗯，总之，那么，等我安排好了，我再联系你……"

    # 里昂 「う、う、ん。待ってる…！今日はとりあえず帰るね！　ばいばい！」
    show リオン_基本_杖_驚き_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0201.ogg"
    lion リオン_基本_杖_驚き_1 "呃、嗯、嗯。等着你……！今天总、总、总、总之就先回去了！Byebye！"
    hide リオン_基本_杖_にっこり_1

    # 莲 「あ、またな」
    lian "啊，再见"

    # 里昂消失
    hide リオン_基本_杖_驚き_1 with dissolve

    # nil 「リオンは屋台を片付け終わると、クーラーボックスを肩に掛けて、ピューと音が鳴るような勢いで視界からフレームアウトしていった。」
    "里昂收拾完摊子后，肩上扛着冷藏箱，以“咻——”的声音和气势从我视野中消失了"

    # 莲 「…ぜぇ…はぁ…まったく…緊張するじゃねぇか…まぁこれも、一夏の思い出ってやつ…だよな…」
    lian "…呜…哈…真是的……这不是很紧张吗…嘛，这也是一个夏天的回忆…吧……"

    # 飞过特效
    stop music fadeout 1.0
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 0.2, ramplen=256, reverse=False, alpha=True, time_warp=None)
    scene 通学路d_夕 at love69_bg1440 with ImageDissolve("images/tr/縦ブラインド.png", 0.2, ramplen=256, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「…なるほど…この桜…そういうことか…」
    show 想瑠_スーツ_目閉じ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0038.ogg"
    liu 想瑠_スーツ_目閉じ "……原来如此……这樱花……原来是这样的嘛……"
    # liu 想瑠_スーツ_目閉じ "……原来如此……这樱花……原来如此……"

    # 飞过特效
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 0.2, ramplen=256, reverse=False, alpha=True, time_warp=None)

    # 黑屏
    # L:这里的里昂本来就不是果体，这里可不是我改了昂！

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「はぁ、はぁ…ぁぅ…んっ…やだ…溢れてきちゃ…ぁ、もうだめっ…とまんなぃ…蓮く…蓮くぅん…んっ…」
    voice "voice/リオン/ron_a1_0202.ogg"
    lion リオン_下着_基本_悲しい2_1 "哈，哈……呜……呜…呜…呜……溢出来了…啊，已经不行了…不要停下来…莲君……莲君…嗯…"

    # 里昂 「蓮くぅ…んっ…わたし…ひ、んぅ…すきぃ…んっ、ひぁぅうっ…！」
    voice "voice/リオン/ron_a1_0203.ogg"
    lion リオン_下着_基本_悲しい2_1 "莲君……嗯……我……喜、喜欢……呀啊……！"

    # scene18 场景1 【和里昂一起奇迹般的春夏秋冬】 结束

    # scene18 场景2 【班主任的考验和莲的真心】 开始
    play music bgmfourteen fadein 2.0
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene sdcg01a with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # nil 「翌日。」
    "第二天"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まふまふまふまふまふまふまふ」
    voice "voice/真冬/maf_a1_0160.ogg"
    dong 真冬_制服_基本_無表情 "嘛呼嘛呼嘛呼嘛呼嘛呼嘛呼嘛~"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「まふまふまふまふまふまふまふ」
    voice "voice/心愛/cca_a1_0298.ogg"
    ai 心愛_制服_基本_もぐもぐ "嘛呼嘛呼嘛呼嘛呼嘛呼嘛呼嘛~"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「れでぃー…」
    voice "voice/真冬/maf_a1_0161.ogg"
    dong 真冬_制服_基本_目閉じ "Ready——……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「まふまふー！」
    voice "voice/心愛/cca_a1_0299.ogg"
    ai 心愛_制服_基本_ニタァ "嘛呼嘛呼——！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    scene sdcg01b with dissolve

    # 真冬 「びよーん」
    voice "voice/真冬/maf_a1_0162.ogg"
    dong 真冬_制服_基本_ニタァ "Biang——"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「うにー」
    voice "voice/心愛/cca_a1_0300.ogg"
    ai 心愛_制服_基本_ぶわー "呼捏——"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ぺち」
    voice "voice/真冬/maf_a1_0163.ogg"
    dong 真冬_制服_基本_無表情 "啪唧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ＰＯＷ！」
    voice "voice/心愛/cca_a1_0301.ogg"
    ai 心愛_制服_基本_ポカーン "ＰＯＷ！"

    # 场景切回教室
    scene 教室_昼 at love69_bg1220 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # 莲 「なぁ君たち」
    lian "呐，你们啊"

    # nil 「本日は前期授業最後の日。つまり終業のベルが鳴ったら夏休みだ。」
    "今天是前期课程的最后一天，也就是说下课铃响了就是暑假了"

    # nil 「俺はお隣さんがぽっかりと空いた席に、座りながら、スマフォのブラウザで、デートプランを調べていた。」
    "我坐在旁边空荡荡的座位上，用我的智能手机浏览器调查约会计划"

    # nil 「前の席では、昨日俺に交際を告げた二人の百合っぷるが、いつも通りにイチャイチャしている。」
    "在前面的座位上，昨天告诉我开始交往的两朵百合花，正在像往常一样亲热着"

    # 心爱 「ほいほい、なんですかお兄ちゃん」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0302.ogg"
    ai 心愛_制服_基本_笑顔 "喂喂，什么事啊，欧尼酱"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「んー？　なんだい蓮くん」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0164.ogg"
    dong 真冬_制服_基本_無表情 "嗯？什么事，莲君？"

    # 莲 「呼び名を入れ替えるなよ。で、単刀直入に聞くけど、女の子がデートに連れてかれて喜ぶ所ってどこよ」
    lian "不要互换身份叫我哟。然后，我就直截了当地问了，女孩子被约会带到哪里会高兴呢？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「寄席」
    # 参考资料：https://ja.wikipedia.org/wiki/%E5%AF%84%E5%B8%AD
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0303.ogg"
    ai 心愛_制服_基本_真顔 "寄席（L:可以理解成曲艺场、说书场、杂技场，可以去这里康落语之类的表演）"
    hide 心愛_制服_基本_笑顔

    # 莲 「うるせえ」
    lian "闭嘴"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「んー？　もしかして、リオンちゃん？」
    show 真冬_制服_基本_嬉しい at love69_left with dissolve
    voice "voice/真冬/maf_a1_0165.ogg"
    dong 真冬_制服_基本_嬉しい "嗯？难道说是，里昂酱？"
    hide 真冬_制服_基本_無表情

    # 莲 「…まぁ、隠してもしょーがないよな。その通りだ」
    lian "…嘛，就算想隐瞒起来也没什么用啊。就是那样"

    # 真冬 「好きなの？」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0166.ogg"
    dong 真冬_制服_基本_微笑み "你喜欢吗？"
    hide 真冬_制服_基本_嬉しい

    # 莲 「うるせえ」
    lian "无路赛"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「おひょー！　蓮くん、外人に手を出しましたか！」
    show 心愛_制服_基本_ニタァ at love69_right with dissolve
    voice "voice/心愛/cca_a1_0304.ogg"
    ai 心愛_制服_基本_ニタァ "呜呼——！莲君，你对外国人下手了吗！"
    hide 心愛_制服_基本_真顔

    # 莲 「てめぇは人の妹に手を出したけどな」
    lian "你不也是对别人的妹妹下手了嘛"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「先に手を出したのは私だよ」
    show 真冬_制服_基本_ニタァ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0167.ogg"
    dong 真冬_制服_基本_ニタァ "先下手的可是我哦"
    hide 真冬_制服_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「きゃー☆」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_0305.ogg"
    ai 心愛_制服_基本_嬉しい "呀——☆"
    hide 心愛_制服_基本_ニタァ

    # 莲 「うるせえ」
    lian "闭嘴"

    # nil 「やべぇ、話がすまねぇ。」
    "牙白，说错话了"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    play sound "voice/effect/03_引戸2～あける.ogg"

    # 想瑠 「よーしお前ら夏休みの挨拶するぞー」
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0039.ogg"
    liu 想瑠_スーツ_見下し "哟——暑假前打个招呼吧——"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「想瑠にゃん想瑠にゃーん！　蓮くんが女の子デートに誘うのどこがいって聞いてきたよ！　どこがいかなぁ！」
    show 心愛_制服_基本_ニタァ at love69_right with dissolve
    voice "voice/心愛/cca_a1_0306.ogg"
    ai 心愛_制服_基本_ニタァ "想瑠喵想瑠喵！莲君问我邀请女生约会该去哪里了！去哪里好呢！"
    hide 心愛_制服_基本_嬉しい

    # 莲 「おいばかやめろ恥ずかしいだろ」
    lian "喂，笨蛋，快住口，好害羞啊"
    # lian "喂，笨蛋，快住手，好害羞啊"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「あん？　そりゃー…お前…横浜あたり街ブラして、フィニッシュは遊園地の観覧車って相場が決まってるだろ…」
    # 参考资料：http://cosmoworld.jp/attraction/wonder/cosmoclock21/
    show 想瑠_スーツ_真顔 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0040.ogg"
    liu 想瑠_スーツ_真顔 "啊？那个啊……你这家伙……在横滨一带到处逛逛街，终点定在游乐园的摩天轮不就好了嘛……（L:横滨有着世界最大的摩天轮）"
    hide 想瑠_スーツ_見下し

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「意外とまともな提案だった…」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0168.ogg"
    dong 真冬_制服_基本_無表情 "真是意外的体面的提案呢……"
    hide 真冬_制服_基本_ニタァ

    # 莲 「な…」
    lian "啊……"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「なんだね君たちは。私の事をなんだと思っているんだ」
    show 想瑠_スーツ_本気 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0041.ogg"
    liu 想瑠_スーツ_本気 "什么呀，你们这帮家伙以为我是什么啊？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「おやつ」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0307.ogg"
    ai 心愛_制服_基本_笑顔 "零食"
    hide 心愛_制服_基本_ニタァ

    # 莲 「ポリバケツ」
    lian "聚乙烯水桶"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まふ」
    show 真冬_制服_基本_にっこり at love69_left with dissolve
    voice "voice/真冬/maf_a1_0169.ogg"
    dong 真冬_制服_基本_にっこり "嘛呼"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「人ですらねぇ！　っていうか生き物ですらねぇ！　あんまりいじめられると泣くからな私」
    show 想瑠_スーツ_驚き at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0042.ogg"
    liu 想瑠_スーツ_驚き "甚至不是人啊！甚至不是生物啊！你们这样欺负我，我会哭的"
    hide 想瑠_スーツ_本気

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「いよ」
    show 心愛_制服_基本_無表情 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0308.ogg"
    ai 心愛_制服_基本_無表情 "可以的哦"
    hide 心愛_制服_基本_笑顔

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ふえ」
    show 想瑠_スーツ_ぶわ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0043.ogg"
    liu 想瑠_スーツ_ぶわ "呜欸"
    hide 想瑠_スーツ_驚き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ぺち」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0170.ogg"
    dong 真冬_制服_基本_無表情 "啪唧"
    hide 真冬_制服_基本_にっこり

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ぐぇ」
    show 想瑠_スーツ_驚き at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0044.ogg"
    liu 想瑠_スーツ_驚き "咕欸"
    hide 想瑠_スーツ_ぶわ

    # nil 「横浜で街ブラして観覧車か…悪くないな。」
    "在横滨街上到处逛逛，摩天轮什么的…还不错呢"

    # nil 「凡そ５秒に及ぶ会議の結果、デートプラン決定しました。」
    "经过5秒钟的会议的结果，决定了约会计划"

    # nil 「ありがとう想瑠にゃん先生。恥ずかしいので、心の声だけでお送り致します。」
    "谢谢你想瑠喵老师。因为很不好意思，所以我只用心声传达给你"

    # 想瑠 「つーことで、まぁ今日から夏休みなんでね、みなさんそれぞれ大人の階段登るとおもいますが…何があっても先生は連帯保証人のハンコは押しませんので、そのつもりで！」
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0045.ogg"
    liu 想瑠_スーツ_見下し "话说，从今天开始就放暑假了，我想大家都会登上大人的阶梯…不管发生什么事，老师都不会盖连带保证人的印章，所以要做好准备！"
    hide 想瑠_スーツ_驚き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「せんせー！　赤ちゃんはどこからきますか！」
    show 真冬_制服_基本_嬉しい at love69_left with dissolve
    voice "voice/真冬/maf_a1_0171.ogg"
    dong 真冬_制服_基本_嬉しい "老师——！小孩子是从哪里来的啊！"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「そういう事はお兄ちゃんに聞こうか！」
    show 想瑠_スーツ_本気 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0046.ogg"
    liu 想瑠_スーツ_本気 "这种事情就去问哥哥吧！"
    hide 想瑠_スーツ_見下し

    # 想瑠 「えーこほん。つーことで。以上で、前期授業を終わりにします！皆さんよい夏休みを！」
    show 想瑠_スーツ_目閉じ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0047.ogg"
    liu 想瑠_スーツ_目閉じ "嗯——咳咳，就这样吧。前期课程到此结束！祝大家暑假愉快！"
    hide 想瑠_スーツ_本気

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あーなーつやすみー！」
    show 心愛_制服_基本_もぐもぐ at love69_right with dissolve
    voice "voice/心愛/cca_a1_0309.ogg"
    ai 心愛_制服_基本_もぐもぐ "啊——暑——假——啊——！"
    hide 心愛_制服_基本_無表情

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    hide 心愛_制服_基本_もぐもぐ with dissolve
    show 真冬_制服_基本_にっこり at love69_left with dissolve
    # 真冬 「あ、ほらほら、勝手にどっかいかないの」
    voice "voice/真冬/maf_a1_0172.ogg"
    dong "啊，过来过来，不要自己去别的地方啊"
    hide 真冬_制服_基本_嬉しい
    hide 真冬_制服_基本_にっこり with dissolve
    stop music fadeout 2.0

    # BGM 停

    # nil 「担任の宣言と同時に、生徒達は蜘蛛の子散らすように、教室から飛び出していった。」
    # 参考资料：https://kotobank.jp/word/%E8%9C%98%E8%9B%9B%E3%81%AE%E5%AD%90%E3%82%92%E6%95%A3%E3%82%89%E3%81%99-485168
    # 参考资料：https://study-z.net/100099827
    "在班主任这样宣布的同时，学生们像蜘蛛的孩子一样从教室里冲了出去（L:蜘蛛の子散らす来自寓言，如果打破装着小蜘蛛的袋子，小蜘蛛就会向四面八方散开，形容大量的东西四散逃跑）"

    # nil 「気づいたら、教室には心愛も真冬も、誰も残っておらず、書類を片付ける担任と、俺だけになっていた。」
    "回过神来，教室里无论是心爱还是真冬，都没有人留下，只有我和整理文件的班主任还在"

    # 莲 「さて、帰るか。アンタも良いバカンスをな」
    lian "那么，回家吧。也祝你假期愉快"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「あーすまん、ちょっと、待ってもらおうか葛城くん」
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0048.ogg"
    liu 想瑠_スーツ_見下し "啊，对不起，等一下，葛城君"
    hide 想瑠_スーツ_目閉じ

    # 莲 「あん？　温泉掘りのバイトならお断りですよ」
    lian "嗯？如果是挖温泉的工作我拒绝"

    # 想瑠 「いやいや。ちょいと、確認しておきたい事があってだね…」
    show 想瑠_スーツ_目閉じ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0049.ogg"
    liu 想瑠_スーツ_目閉じ "不不，有件事我想稍微确认一下……"
    hide 想瑠_スーツ_見下し

    # nil 「担任が、まっすぐと俺の目を見つめる。表情こそ柔らかだったが、有無を言わせない威圧感があった。」
    "班主任直视着我的眼睛，虽然表情很柔和，却有一种不容置疑的威慑感"

    # nil 「まるで金縛りのように身体が動かない。」
    "身体简直像鬼压床一样动弹不得"

    # 心爱恰冰淇淋 BGM 再现，这里用的应该是 Full ver. 可能加变奏了，写脚本的时候需要再确认一下，歌词似乎有提到里昂
    # 确认是循环播放的
    play music bgmthree

    # 想瑠 「単刀直入に聞こう」
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0050.ogg"
    liu 想瑠_スーツ_見下し "我就单刀直入的说了"
    hide 想瑠_スーツ_目閉じ

    # 莲 「あ…あ…」
    lian "啊…啊…"

    # 想瑠 「リオン＝マクスウェル…君は、彼女の事をどう思っている？」
    show 想瑠_スーツ_本気 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0051.ogg"
    liu 想瑠_スーツ_本気 "里昂·麦克斯韦……你觉得她怎么样？"
    hide 想瑠_スーツ_見下し

    # 莲 「あ？　どうって…？　リオンは友達だし、良い奴だと思ってるよ」
    lian "啊？怎么说呢…？里昂是朋友，我觉得她是个好人"

    # 想瑠 「周りくどい表現は良い。好き…なのか？　彼女の事を…」
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0052.ogg"
    liu 想瑠_スーツ_見下し "我不想拐弯抹角，喜欢……吗？她的话……"
    hide 想瑠_スーツ_本気

    # 莲 「なんだよいきなり。第一、茶化すにしたってタチがわりいな」
    lian "什么嘛，这么突然。首先，这不是一个很适合的开玩笑的事情"

    # 想瑠 「答えろ」
    show 想瑠_スーツ_本気 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0053.ogg"
    liu 想瑠_スーツ_本気 "回答我"
    hide 想瑠_スーツ_見下し

    # 莲 「っ…！」
    lian "嗯…！"

    # nil 「刹那。心臓が止まるような視線が俺を射貫いた。」
    "刹那间，令人心脏停止般的目光穿透了我。"

    # nil 「なんだよ…好きかどうかって…。」
    "搞什么啊……突然问喜不喜欢……"

    # nil 「担任は黙ったま、鋭いまなざしで俺を見つめている。」
    "班主任沉默着，用锐利的目光注视着我"

    # nil 「俺はリオンの事を…。」
    "我对里昂的事…"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「『えへへ。ありがとうの…ちゅー♪　ほっぺだけどね！』」
    # 这里的里昂没有配音
    # voice "voice/リオン/ron_a1_0204.ogg"
    lion リオン_基本_杖_にっこり_1 "『欸嘿嘿，谢谢你……啾——♪虽然是脸颊呢』"

    # 里昂 「『あの二人が、蓮くんの知らない場所で関係を育んでいたように、蓮くんも、あの二人の知らない場所で…私と…』」
    # voice "voice/リオン/ron_a1_0205.ogg"
    lion リオン_基本_杖_微笑み "『就像那两个人在莲君不知道的地方培养关系一样，莲君也在那两个人不知道的地方…和我……』"

    # 里昂 「『私が居る限り、一人になんてさせないからさ』」
    # voice "voice/リオン/ron_a1_0206.ogg"
    lion リオン_基本_杖_嬉しい "『只要我在，就不会只让你一个人呆着』"

    # nil 「こんな事を言われて…」
    "你是这样对我说的……"

    # 莲 「俺は…」
    lian "我是……"

    # nil 「答えは出ていた。」
    "答案已经有了"

    # 莲 「…好きだよ。まだ会って一週間ぐらいしか経ってねぇけど、もっと仲良くなりたいし、ずっと一緒にいれたら楽しいなと思ってる」
    lian "喜欢她的，虽然见面才过了一周左右，但是我想变得更亲密，如果能一直在一起的话，我会很开心的"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「妹と幼馴染みが自分の知らない所で関係を変えてしまい、その穴埋めに彼女を頼ろうとしてるだけじゃないのか？」
    show 想瑠_スーツ_目閉じ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0054.ogg"
    liu 想瑠_スーツ_目閉じ "你妹妹和青梅竹马在自己不知情的情况下改变了关系，你不就是想依靠她来填补这个空缺吗？"
    hide 想瑠_スーツ_本気

    # L:我在翻到这里的时候其实也是这么觉得的，参考上面2022年1月18日的注释

    # 莲 「なんだと…！」
    lian "你说什么啊…！"

    # nil 「だが、担任の言う事は間違っていなかった。」
    "但是，班主任说的话没有错"

    # nil 「リオンの事を本格的に意識しはじめたのは、真冬と心愛が付き合うという事を知ってからだった。」
    "真正开始意识到里昂的事是在知道了和真冬和心爱交往之后"

    # nil 「そのぽっかり空いた穴を、リオンは埋めてくれようとしている。」
    "里昂打算努力填补这个空缺"

    # nil 「それを…嬉しく思って何が悪い。」
    "为此…觉得开心有什么不好"

    # 莲 「だとしてもだ…それがきっかけで、アイツの事を好きになっちまったらしょうがねぇだろ。俺だって、あいつの事を幸せにしてあげたいと思ってるよ」
    lian "就算是这样……以此为契机，喜欢上那家伙也没办法吧。我也想让那家伙幸福"

    # 想瑠 「そうか。じゃぁ問うが。君は彼女の何を知っているんだね？」
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0055.ogg"
    liu 想瑠_スーツ_見下し "是吗？那我问你，你对她了解多少？"
    hide 想瑠_スーツ_目閉じ

    # 莲 「どういうことだ？」
    lian "怎么说？"

    # 想瑠 「彼女が何者で。どこから来たのか。何故こにいるのか」
    show 想瑠_スーツ_本気 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0056.ogg"
    liu 想瑠_スーツ_本気 "她是谁？从哪里来？为什么会在这里？"
    hide 想瑠_スーツ_見下し

    # 莲 「あいつは、日本でアイス屋を開くために、イギリスからやってきたんだ」
    lian "那家伙是为了在日本开冰淇淋店，从英国来的"

    # 想瑠 「それが本当に真実だと思ってるのか？　彼女が嘘をついていたり、隠し事をしている事は考えた事ないのか？」
    show 想瑠_スーツ_真顔2 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0057.ogg"
    liu 想瑠_スーツ_真顔2 "你真的认为这是真的吗？你有没有想过她在撒谎，或者有所隐瞒？"
    hide 想瑠_スーツ_本気

    # 莲 「……」
    lian "……"

    # nil 「なんだ…担任は俺に何を聞こうとしている。いや、こまできたら、恐らくリオンには何かがある。」
    "搞什么啊…班主任想问我什么。不，要是这么说的话，恐怕里昂隐瞒了什么东西"

    # nil 「それはもう明白だった。」
    "这已经很明显了"

    # nil 「だが…そんなの…」
    "但是……那样的话…"

    # 莲 「だったら…」
    lian "那么…"

    # 想瑠 「なんだ」
    show 想瑠_スーツ_真顔 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0058.ogg"
    liu 想瑠_スーツ_真顔 "什么？"
    hide 想瑠_スーツ_真顔2

    # 莲 「だったらなんなんだ」
    lian "那又怎样"

    # 想瑠 「ほう？」
    show 想瑠_スーツ_本気 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0059.ogg"
    liu 想瑠_スーツ_本気 "嗬？"
    hide 想瑠_スーツ_真顔

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「『えへへ。ありがとうの…ちゅー♪　ほっぺだけどね！』」
    # voice "voice/リオン/ron_a1_0207.ogg"
    lion "『欸嘿嘿，谢谢你……啾——♪虽然是脸颊呢』"

    # nil 「確かに、俺はリオンの事を何も知らないかもしれない。あいつの住んでる場所も、あいつの過去も。あいつの素性も、何もかもな！」
    "确实，我可能对里昂一无所知。那家伙住的地方，那家伙的过去，那家伙的身份，一切都是！"

    # 莲 「だが例え…リオンが嘘をついていたとしても、隠し事をしていたとしても！俺はそれでも、リオンの事が好きになっちまったんだよ！」
    lian "但是就算……里昂说谎也好，即使隐瞒了也好！我还是喜欢上了里昂！"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「……」
    show 想瑠_スーツ_真顔2 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0060.ogg"
    liu 想瑠_スーツ_真顔2 "……"
    hide 想瑠_スーツ_本気

    # 莲 「だから、例え傷つく事になったとしても、俺はリオンを好きになった結果なら、俺は後悔したりしねぇ！」
    lian "所以，就算受了伤，如果这是我喜欢上里昂的结果的话，我也不会后悔的！"

    # 想瑠 「何が…あってもか？彼女が、本来君の手の届くはずの無い存在だったとしてもか？」
    show 想瑠_スーツ_本気 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0061.ogg"
    liu 想瑠_スーツ_本気 "即使……即使发生任何事？即使她本来就是你无法企及的存在？"
    hide 想瑠_スーツ_真顔2

    # 莲 「だったら届かせるまでだ。例え、届かなくても、はいそうですかと、諦めるわけにはいかねぇなぁ！」
    lian "那也要把心情传达到。即使传达不到，也不能放弃啊！"

    # 想瑠 「…そうか…わかった」
    show 想瑠_スーツ_目閉じ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0062.ogg"
    liu 想瑠_スーツ_目閉じ "……好吧……我明白了"
    hide 想瑠_スーツ_本気

    # nil 「担任は目を閉じる。」
    "班主任闭上眼睛"

    # nil 「そして、ゆっくりと目を開き直すと、そこにはいつものニヒルな笑みを浮かべる担任に戻っていた。」
    "然后，慢慢地再次睁开眼睛，回到了往常含笑的班主任"

    # 想瑠 「驚かせてごめんな。こまで来たら、君も察しがついているだろうが…一筋縄じゃいかないぞ、あの子はな」
    # 参考资料：一筋縄 https://www.weblio.jp/content/%E4%B8%80%E7%AD%8B%E7%B8%84
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0063.ogg"
    liu 想瑠_スーツ_見下し "吓到你了抱歉啊，这样一来，你现在可能已经猜到了……用一般的办法可是不行的哦，那孩子啊"
    hide 想瑠_スーツ_目閉じ

    # L：相比一周目的莲，二周目的莲嘴炮还行嘛，不需要别人代打了

    # 想瑠 「いや…あの子は…というか、彼女の抱える業というべきか…」
    # 参考资料：https://dictionary.goo.ne.jp/word/%E6%8A%B1%E3%81%88%E3%82%8B/
    show 想瑠_スーツ_真顔 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0064.ogg"
    liu 想瑠_スーツ_真顔 "不……那孩子的话……应该说是，和她做女朋友的话会是负担"
    hide 想瑠_スーツ_見下し

    # 莲 「余計なお世話だ。何があっても受け止めてやればい。そのぐらいの覚悟はある」
    lian "别多管闲事，不管发生什么都要接受。我有这样的觉悟"

    # 想瑠 「その覚悟が、一夏の思い出にならん事を祈るよ。じゃぁな。良いバカンスを過ごせよ」
    show 想瑠_スーツ_ニヤリ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0065.ogg"
    liu 想瑠_スーツ_ニヤリ "希望你的觉悟不会成为一夏的回忆。再见，祝你度过愉快的假期"
    hide 想瑠_スーツ_真顔

    # 莲 「待てよ」
    lian "等一下"

    # 想瑠 「あん？　お説教は終わりだよ、君の気持ちはわかったし、これ以上深入りする気はないさ。あとは二人の問題だ。せいぜいお幸せにな」
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0066.ogg"
    liu 想瑠_スーツ_見下し "啊？说教已经结束了哟，我理解你的心情，也不想再深入下去了。剩下就是两个人的问题啦，请尽量幸福哦"
    hide 想瑠_スーツ_ニヤリ

    # 莲 「横浜のデートスポットぐらい教えてやがれ」
    lian "告诉我横滨的约会地点吧"

    # 想瑠 「ふっ…しょうがないにゃぁ…いよ」
    show 想瑠_スーツ_照れ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0067.ogg"
    liu 想瑠_スーツ_照れ "哈……没办法喵……可以哦"
    hide 想瑠_スーツ_見下し

    stop music fadeout 1.0

    # BGM 停，原地tp，莲离开
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 0.2, ramplen=256, reverse=False, alpha=True, time_warp=None)
    scene 教室_昼 at love69_bg1220 with ImageDissolve("images/tr/縦ブラインド.png", 0.2, ramplen=256, reverse=False, alpha=True, time_warp=None)

    # 想瑠 「ラブポーション・シクスティナイン…運命すらもねじ曲げやがるとはな…。まったく、なんつーものを作り出しやがったんだよ…」
    show 想瑠_スーツ_目閉じ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0068.ogg"
    liu 想瑠_スーツ_目閉じ "LOVEPOTION·SIXTININE…连命运都扭曲了啊…真是的，居然做出了这样的东西……"

    # 想瑠 「あーあ、世界が変わっちまうか…。まぁ、それも面白い。だったら、今夜は派手にお祝いといこうじゃないか。なぁ？」
    show 想瑠_スーツ_ニヤリ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0069.ogg"
    liu 想瑠_スーツ_ニヤリ "啊——啊，世界要改变了嘛……嘛，那也很有趣。那今晚就华丽地庆祝一下吧"
    hide 想瑠_スーツ_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あ、想瑠にゃんだ！　何一人でぶつぶつぶやいてるの？」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0310.ogg"
    ai 心愛_制服_基本_笑顔 "啊，是想瑠喵！你一个人在嘟囔什么呢？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ご飯」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0173.ogg"
    dong 真冬_制服_基本_無表情 "恰饭"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「おやつ」
    show 心愛_制服_基本_無表情 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0311.ogg"
    ai 心愛_制服_基本_無表情 "零食"
    hide 心愛_制服_基本_笑顔

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「……ふえ」
    show 想瑠_スーツ_ぶわ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0070.ogg"
    liu 想瑠_スーツ_ぶわ "……呜欸"
    hide 想瑠_スーツ_ニヤリ

    # 想瑠 「あ、君ら、今夜友達の家に泊まりにいくけど、君らも来る？」
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0071.ogg"
    liu 想瑠_スーツ_見下し "啊，你们，我今晚要去朋友家过夜，你们也要来吗？"
    hide 想瑠_スーツ_ぶわ

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「あらあら、それはどういうお誘いなんでしょうね？」
    show 真冬_制服_基本_ニタァ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0174.ogg"
    dong 真冬_制服_基本_ニタァ "啊啦啊啦，这是什么的邀请呢？"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「きゃー☆　襲われちゃう☆」
    show 心愛_制服_基本_にっこり1 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0312.ogg"
    ai 心愛_制服_基本_にっこり1 "呀ー☆会被袭击的☆"
    hide 心愛_制服_基本_無表情

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「…いつも襲うの君らじゃないか…」
    show 想瑠_スーツ_真顔 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0072.ogg"
    liu 想瑠_スーツ_真顔 "……经常袭击的不都是你们吗？"
    hide 想瑠_スーツ_見下し

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「嫌じゃないくせに…」
    show 真冬_制服_基本_嬉しい at love69_left with dissolve
    voice "voice/真冬/maf_a1_0175.ogg"
    dong 真冬_制服_基本_嬉しい "明明不讨厌……"
    hide 真冬_制服_基本_ニタァ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ニヤー」
    show 心愛_制服_基本_ニタァ at love69_right with dissolve
    voice "voice/心愛/cca_a1_0313.ogg"
    ai 心愛_制服_基本_ニタァ "咿呀——"
    hide 心愛_制服_基本_にっこり1

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ふえ……」
    show 想瑠_スーツ_ぶわ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0073.ogg"
    liu 想瑠_スーツ_ぶわ "呜欸欸……"
    hide 想瑠_スーツ_真顔

    # scene18 场景2 【班主任的考验和莲的真心】 结束！

    # 离全部翻译完成只剩 4 个 Scene ！

    #  过场：里昂（常服）

    # Scene18 结束！

    # 隐藏 quick_menu
    $ quick_menu = False

    play sound "voice/effect/moosehead honk (stinger).ogg"
    # hide screen quick_menu
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)
    scene アイキャッチリオン with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)

    $ renpy.pause(1.5, hard=True)
    $ renpy.end_replay()

    jump scene19

    # 2022年1月19日备注
    # 正式版发布前一定要先把音乐鉴赏做出来，这么好的歌没有地方听可惜了

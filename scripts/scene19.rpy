# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene19 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：
# 版本 NightBuild "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年5月1日

# 当前流程：All Done!

label scene19:
    # scene19 开始
    play music bgmfourteen fadeout 2.0 fadein 2.0

    # scene19 场景1 【和里昂的初次约会】 开始
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)
    scene 自室a_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    $ quick_menu = True

    # nil 「そして、デート当日。」
    "然后，约会当天"

    # nil 「心愛と真冬は担任と一緒に”友達の家”にお泊まりに行っているので、誰も起こしてくれませんでした。」
    "因为心爱、真冬和班主任一起去“朋友的家”过夜去了，所以今天没人来叫我起床"

    # nil 「でも、時間通りに起きました。」
    "但是，我准时起床了"

    # 莲 「ねぇ褒めて褒めて！！」
    lian "哈，快来表扬表扬我吧！！"

    # nil 「家には誰もいません。しょんぼり。」
    "然而家里谁都没在，我很沮丧"

    # 动画：CALL
    # 电话呼入声
    play sound "voice/effect/主人公着信_送信.ogg"
    show screen callscr

    # nil 「と思ったら電話です。」
    "我觉得是电话"
    hide screen callscr

    # 莲 「はいもしもしお兄ちゃんです」
    lian "喂，我是哥哥"

    # 这个语句是针对电话里的真冬&心爱设计的参数，能够调整电话里的真冬&心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.04
    $ sideimagesize.SideImageYalign = 1.04
    $ sideimagesize.SideImageZoom = 0.6

    # 真冬 「『お、ちゃんと起きれたじゃん。偉いぞお兄ちゃん。デート楽しんでおいで』」
    voice "voice/真冬/maf_a1_0182.ogg"
    dong 真冬_通話中 "哦，不是好好的起床了吗？真了不起，欧尼酱，祝你约会愉快"

    # 心爱 「『大好きな彼女のためなら早起きする蓮くん偉いぞー！』」
    voice "voice/心愛/cca_a1_0662.ogg"
    ai 心愛_通話中 "为了最喜欢的女朋友早起的莲君真了不起呢——！"

    # nil 「…情報は全部筒抜けなんだな。まだ彼女じゃねぇけど」
    "…情报全都泄露出去了啊，虽然还不是女朋友"

    # 心爱 「『想瑠にゃんが全部吐いたよ…』」
    voice "voice/心愛/cca_a1_0663.ogg"
    ai "『想瑠喵全部说出来了哦……』"

    # 莲 「そうか…。お前らもお泊まり会楽しんでな」
    lian "是吗……你们也好好享受寄宿吧"

    # 心爱 「『はーい。今日はみんなでよこはモゴゴゴゴ！』」
    voice "voice/心愛/cca_a1_0664.ogg"
    ai "『好——今天大家一起呜呜呜呜……！』"

    play sound "voice/effect/18_携帯電話操作音1.ogg"

    # nil 「…前言撤回。やはり家族は良いものだ。」
    "…撤回前言，果然家人就是好"

    # nil 「ていうか…横浜…？　まじで？　まぁいや。」
    "话说回来…横滨…？真的吗？嘛，不管了"

    # 动画：CALL
    # 电话呼入声
    play sound "voice/effect/主人公着信_送信.ogg"
    show screen callscr

    # nil 「と思ったらまたしても電話です。」
    "这么想着又来电话了"

    hide screen callscr
    # 莲 「はいもしもし葛城お兄さんです」
    lian "喂，我是葛城哥哥"

    # 里昂 「『や、やほー！　蓮くん！　楽しみ過ぎちゃってついうっかり電話しちゃったよあは…』」
    # 208
    voice "voice/リオン/ron_a1_0208.ogg"
    lion リオン_通話中 "『Ya、Yahoo——！莲君！我实在是太开心了，不小心把电话打过去了……啊哈哈哈』"

    # 莲 「お、おう…」
    lian "哦，哦…"

    # nil 「なんだこいつ可愛いな…。リオンの事を好きだと決めてから、ついつい意識しちゃう感やばい。」
    "天啊怎么能这么可爱啊…在决定喜欢里昂之后，不知不觉就意识到了"

    # 里昂 「『で、デートって正直初めてだから、その、どうやっていかわかんないけど、が、頑張るから！　うん！』」
    voice "voice/リオン/ron_a1_0209.ogg"
    lion "『说实话，这是我第一次约、约会，所以，呃，我不知道该怎么办，但我会尽力的！嗯！』"

    # 莲 「そんなきばらんくても…自然体でいんだぞ…？というか無駄にテンション高いな？」
    lian "不必那么紧张，可以自然一点嘛，为什么这么兴奋捏？"

    # 里昂 「『そ、そーんな事ないよー？』」
    voice "voice/リオン/ron_a1_0210.ogg"
    lion "『没、没这回事哟——？』"

    # 莲 「徹夜か」
    lian "通宵了？"

    # 里昂 「『ギクゥッ！？　す、すみません全然眠れなくて…』」
    # 211
    voice "voice/リオン/ron_a1_0211.ogg"
    lion "『嘎呜！？对、对不起，根本睡不着……』"

    # 莲 「いや、いけど、大丈夫なん？　バイクで迎えにいくつもりだけど」
    lian "不用道歉，不过你没问题吧？我打算骑摩托车去接你"

    # 里昂 「『だ、大丈夫！　マクスウェル家秘伝のショートスリーパーホールドがあるから！』」
    voice "voice/リオン/ron_a1_0212.ogg"
    lion "『没，没关系! 我有麦克斯韦家族秘制的Short sleeper hold！』（L:Short sleeper hold应该是本作虚构的东西，应该是类似红牛的饮料，而sleeper hold是一种关节技）"

    # 莲 「関節技と混ざってんぞ。　まぁとりあえず、一時間後に駅集合な」
    lian "和关节技混在一起了，总之，一个小时后在车站集合吧"

    # 里昂 「『はーい！』」
    voice "voice/リオン/ron_a1_0213.ogg"
    lion "『好——！』"

    play sound "voice/effect/18_携帯電話操作音1.ogg"

    # 莲 「幸せもんだなぁ、俺ってやつは。」
    lian "真是幸福啊，我这家伙"

    # 场景切换到葛城家客厅
    scene リビングa_朝 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # 莲 「あ、朝飯が…作られている…一体…誰が…！」
    lian "啊，早饭……做好了…是谁…做的呢…！"

    # nil 「……」
    "……"

    # 莲 「昨日の夜作り置きしたの忘れてました」
    lian "我忘记昨天晚上已经提前做好了"

    # 场景切换到洗漱间
    scene 自宅洗面所_昼 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「シャワーを浴びて、ヘアイロンを決めて、ワックスで髪の毛を立てる。」
    "洗完澡，烫烫头发，用发胶把头发竖起来"

    # nil 「こまでするのは吧何ヶ月ぶりだろう…。」
    "已经好几个月没这么做了……"

    # nil 「おっと、ヒゲをそるのを忘れていたゾ。」
    "哦，差点忘记刮胡子了"

    # 莲 「アゥッ！　キレテナーイ」
    # 参考资料：https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q146373159?__ysp=44Kt44Os44OG44OK44O844KkIOS9lQ%3D%3D
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%9E%E3%82%A4%E3%82%AF%E3%83%BB%E3%83%99%E3%83%AB%E3%83%8A%E3%83%AB%E3%83%89
    # 参考视频：https://www.youtube.com/watch?v=zGOm-4hnDvw
    lian "啊呜！キレテナーイ（L:画面这句话来自00年Schick FxDIA剃须刀电视广告，演员是Michael Shawn Bernardo (1969年7月28日-2012年2月14 日)来自开普敦的南非跆拳道运动员和拳击手）"

    # nil 「ネタが古かったとです。さすがは五枚刃。」
    "虽然段子很老，但是不愧是五刃刀（L:上面提到的剃须刀是五刃刀）"

    # 场景切换到蔚蓝天空
    scene 空 with dissolve
    play music bgmthirtysix fadein 2.0 fadeout 2.0

    # 发动声
    play sound "voice/effect/02_発進走り去る／高速.ogg"

    # nil 「後部座席にメットを搭載して、バイクを走らせる。純正マフラーの静かな排気音が、夏の朝靄の中に木霊する。」
    "带上后排要用的头盔，发动摩托车出发，纯正消声器的安静排气声在夏季的晨雾中回荡"

    # 摩托车发动机声（单遍播放）
    play sound "voice/effect/05_巡航／高速.ogg"

    # nil 「ガソリンは昨日満タンにした。これで、今日はどこでもいける。リオンを連れて。行きたいところにつれてってあげよう。」
    "汽油昨天全加满了，这样的话，今天去哪儿都行，带着里昂，去想去的地方"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「『バイクでいくんだろ？だったら、港の見える公園周辺の町並みは異国情緒溢れて雰囲気いよ』」
    voice "voice/想瑠/sol_a1_0076.ogg"
    liu 想瑠_スーツ_見下し "『你不是骑摩托车去吗？ 那么，可以看到港口公园周围充满了异国情调的街道』"

    # 想瑠 「『昼飯なら中華街の時間無制限食い放題あたりがお勧めかな。でも食い歩きでも悪くないかもね』」
    voice "voice/想瑠/sol_a1_0077.ogg"
    liu 想瑠_スーツ_照れ "『如果是午饭的话，我建议你在唐人街大吃一顿，不过到处走走也不错』"

    # 想瑠 「『山下公園は、デートスポットだけど、実際コンビニと船以外何もないから気をつけるんだ』」
    voice "voice/想瑠/sol_a1_0078.ogg"
    liu 想瑠_スーツ_真顔 "『虽然山下公园看起来很适合约会，但实际上除了便利店和船什么都没有，所以要注意』"

    # 想瑠 「『夜になったら、みなとみらいの夜景散策だなぁ。バイク用の駐車場なら赤レンガ倉庫の近くに無料があるからそこを使うとい』」
    # 参考资料：https://ja.wikipedia.org/wiki/%E6%A8%AA%E6%B5%9C%E3%81%BF%E3%81%AA%E3%81%A8%E3%81%BF%E3%82%89%E3%81%8421
    # 参考资料：https://ja.wikipedia.org/wiki/%E6%A8%AA%E6%B5%9C%E8%B5%A4%E3%83%AC%E3%83%B3%E3%82%AC%E5%80%89%E5%BA%AB
    voice "voice/想瑠/sol_a1_0079.ogg"
    liu 想瑠_スーツ_見下し "『到了晚上，就到港未来散步去看夜景吧，摩托车停车场的话，红砖仓库附近有免费停车场，所以就停那里吧』（L:港未来是位于日本横滨市西区及中区交界水岸的都市再开发区，又称港未来21，MM21，21世纪未来港，曾获选入日本国土交通省主办的“都市景观100选”）"

    # 续一下

    luckykeeper "续，横滨红砖仓库是位于日本神奈川县横滨市中区横滨港的一处历史建筑物，原做为保税仓库使用，1号馆、2号馆分别竣工于1913年（大正2年）和1911年（明治44年），"
    luckykeeper "是港未来地区具有代表性的观光、游憩景点之一，2004年获第45届BCS赏特别奖，2010年获得日本首个联合国教科文组织亚太区文物古迹保护奖的杰出项目奖，很多Gal都会提到这里"

    # 想瑠 「『観覧車に乗った以上はしっかり告白するんだぞ。女の子は期待するからな？　チキんじゃねーぞ男の子！』」
    voice "voice/想瑠/sol_a1_0080.ogg"
    liu 想瑠_スーツ_ニヤリ "『既然已经上了摩天轮，之后就要好好表白，因为女孩子会这样期待的，对吧？别胆怯，男孩！』"

    # 莲 「（何だかんだで、応援してくれてるみたいだな…）」
    lian "（不知怎么的，好像很支持我啊…）"

    # nil 「昨日脅されたのは正直びっくりしたが…。」
    "说实话，昨天被那样可是被吓了一大跳…"

    # nil 「…ん？　このデートプランを、担任から聞いてる場合、俺がそれに従うとしよう。そして、奴らがマジで横浜に来てるとしたら…。」
    "……嗯？既然班主任这么安排好了，我就按照这个来吧。不过，如果那些家伙真的跟来了横滨的话…"

    # nil 「読めたぞ。奴らの腹が…！　」&协力请求，似乎不是梗，不大懂……感觉是读心术的感觉
    "用读心术发现了…！　"

    # nil 「いぜ…追ってくるなら上等だ、逃げもかくれもしねぇぞ！」
    "好啊…追过来的话就太好了，我不会逃跑，也不会躲起来！"

    # 刹车声
    play sound "voice/effect/15_ブレーキ2.ogg"

    # 场景切换到车站前
    image bg 駅前_昼 = "images/bg/駅前_昼.png"
    scene 駅前_昼 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「ということで、駅前に到着しました。」
    "话说，到达了车站前"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「やっ、おはよー！　おー13年モデルじゃーん！　私これ本国で欲しかったんだよー！」
    show リオン_私服_基本_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0214.ogg"
    lion リオン_私服_基本_にっこり "呀，早上好！哦——这不是13年的摩托吗！我在本国就一直想买这个了啊！（L:一周目也有提到里昂特别喜欢这款摩托）"

    # 莲 「うお…」
    lian "噢……"

    # nil 「リオンが楽しそうにぴょこぴょこ跳ねるように、ロータリーの脇に停車したバイクに近づいてくる。」
    "里昂开心的蹦蹦跳跳的向停在转盘旁边的摩托车走来"

    # nil 「ついついその姿に目がいってしまう。」
    "我不由自主地看呆了"

    # 里昂 「あれ？　みえてる？　大丈夫？　おーい」
    show リオン_私服_基本_ジト目 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0215.ogg"
    lion リオン_私服_基本_ジト目 "啊咧？能看到吗？没事吧？喂——"
    hide リオン_私服_基本_にっこり

    # nil 「リオンは俺の目の前で手を振る。」
    "里昂在我面前挥手"

    # 莲 「あ、あ…みえてる、みえてる。服、可愛いなと思って見とれてたんだよ」
    lian "啊，啊…看到了，看到了，衣服很可爱，所以看得入迷了"

    # 里昂 「っ！　わーい！蓮くんの好みがわからなかったから、割と趣味で選んじゃったんだけど…」
    show リオン_私服_基本_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0216.ogg"
    lion リオン_私服_基本_にっこり "啊！哇！我不知道莲君喜欢什么样的，所以特意挑了一件……"
    hide リオン_私服_基本_ジト目

    # 莲 「あ。よく似合ってるよ。アヴリルみたいだな」
    # 参考资料：https://www.avril-kyoto.com/
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%A2%E3%83%B4%E3%83%AA%E3%83%AB%E3%83%BB%E3%83%A9%E3%83%B4%E3%82%A3%E3%83%BC%E3%83%B3
    # L:这里应该是下面那个而不是牌子
    lian "啊，很适合你。好像Avril啊（L:Avril Ramona Lavigne，加拿大歌手、词曲作家及演员。1984年9月27日－，2007年12月，《福布斯》杂志将其列为“25 岁以下最赚钱的人”，年收入为 1200 万美元）"

    # 里昂 「それは褒めすぎかなー？　でも、嬉しいよ！　えへへー♪」
    show リオン_私服_基本_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0217.ogg"
    lion リオン_私服_基本_嬉しい "那是不是夸奖过头了？但是，很开心哦！诶嘿嘿♪！"
    hide リオン_私服_基本_にっこり

    # 莲 「なんか、いつもと雰囲気違うな？　まだ深夜テンション？」
    lian "怎么，感觉气氛和平时不一样呢？是通宵情绪高涨吗？"

    # 里昂 「ち…違う違う！普通に舞い上がってるだけだから、そこは察してくれたまえ！あとは、今日はプライベートで来てるからっ！」&&协力请求
    show リオン_私服_基本_驚き_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0218.ogg"
    # lion リオン_私服_基本_驚き_1 "不……不对不对！只是普通的兴奋而已，相信你也能理解的吧！还有啊，今天我是作为私人来的！"
    lion リオン_私服_基本_驚き_1 "不……不对不对！只是非常的兴奋而已，相信你也能理解的吧！还有啊，今天我是作为私人来的！"
    hide リオン_私服_基本_嬉しい

    # 莲 「ってわけ！　さーて、それじゃぁ、後ろ、失礼してもよろしいかな？」
    # 这里被下面的盖住了，懒得再去提取一次了，请原谅我这里咕了……
    lian "脱了制服就是普通的女孩子了"

    # 里昂 「ってわけ！　さーて、それじゃぁ、後ろ、失礼してもよろしいかな？」
    # 参考资料：https://hinative.com/ja/questions/16610578
    # 参考资料：https://hinative.com/ja/questions/561991
    show リオン_私服_基本_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0219.ogg"
    lion リオン_私服_基本_にっこり "这样啊！那么，我要坐到后面去了，可以吗？"
    hide リオン_私服_基本_驚き_1

    # 莲 「はいよ」
    lian "好嘞"

    hide リオン_私服_基本_にっこり with dissolve

    # nil 「俺がギアをニュートラルに入れたのを確認してから、リオンはひょいっと飛び上がって、後部座席に飛び乗った。」
    "看到我把摩托车挂在空档，里昂咻地跳了起来，坐到了后座上"

    # 莲 「バイクの乗り方は知ってる風だな」
    lian "你好像知道骑摩托车的方法啊"

    # 里昂 「イギリスの女はスノボーとバイクは義務教育だよ！」
    voice "voice/リオン/ron_a1_0220.ogg"
    lion リオン_私服_基本_ニタァ "对英国女人来讲单板滑雪和摩托车是义务教育！"

    # 莲 「空飛ぶ箒は？」
    lian "骑扫帚飞呢？"

    # 里昂 「あれは小説だけだよ…生身で空を飛ぶのは危険だってことで、結構前に規制されたんだ」
    voice "voice/リオン/ron_a1_0221.ogg"
    lion リオン_私服_基本_微笑み "那只不过是小说而已……因为活人在空中飞行是很危险的，所以很早以前就被限制了"

    # 莲 「なんかごもっともな理由だな…」
    lian "好像是很合理的理由啊…"

    # 里昂 「想像してごらんよ、信号もないのに、時速８０マイルで人が生身で飛ぶなんてさ」
    voice "voice/リオン/ron_a1_0222.ogg"
    lion リオン_私服_基本_悲しい "想象一下，在没有信号灯的情况下，一个活人以每小时８０英里的速度飞行"

    # 莲 「そいつは確かに危険だな」
    lian "那的确很危险啊"

    # nil 「時速８０マイルとは、凡そ時速１３０キロメートルです。」
    "时速80英里，大约是时速130公里（L：这个速度是128.74752km/h）"

    # nil 「リオンがメットをしっかりと被ったのを確認して、クラッチを握ったまギアをローに落として、スロットルを回す。」
    "确认里昂牢牢地戴上了头盔，我把离合挂到前进档，转动油门"

    # 莲 「よし、じゃぁいくぞ、リオン」
    lian "好，那开动了，里昂"

    # 里昂 「おー！」
    voice "voice/リオン/ron_a1_0223.ogg"
    lion リオン_私服_基本_にっこり "哦——！"

    # nil 「二人乗りで発進する時は、デリケートなクラッチワークが…」
    "两个人一起出发的时候，要控制好离合……"

    # 戳戳
    play sound "voice/effect/17_フヒ.ogg"

    # 莲 「……」
    lian "……"

    # 里昂 「？」
    voice "voice/リオン/ron_a1_0224.ogg"
    lion リオン_私服_基本_微笑み "？"

    # 莲 「…なぁ、リオンって…」
    lian "…呐，里昂的…"

    # 里昂 「んー？」
    voice "voice/リオン/ron_a1_0225.ogg"
    lion リオン_私服_基本_嬉しい "嗯——？"

    # 莲 「胸、でかいよな」
    lian "欧派，好大啊"

    # 里昂 「ちょっとー！　このタイミングでそういうこと言う！？あれかい？　蓮くんは後ろに女の子乗せる時も、抱きつかれない方が趣味かい？」
    voice "voice/リオン/ron_a1_0226.ogg"
    lion リオン_私服_基本_驚き_1 "喂！这个时候说这种话！？那个啊？有女孩子坐在莲君后面的时候，不应该也是喜欢被抱住吗？"

    # 莲 「いや、そのまで、たのむ」
    lian "不，就这样，拜托了"

    # 里昂 「らじゃ！　それじゃ改めてしゅっぱーつ♪」
    voice "voice/リオン/ron_a1_0227.ogg"
    lion リオン_私服_基本_にっこり "了解！那么再来一次咯~♪"

    # 画面切换到蔚蓝天空
    play sound "voice/effect/02_発進走り去る／高速.ogg"
    scene 空 with dissolve

    # nil 「人の気持ちも知ってか知らずか、リオンにとってはいつも通りなのか。外人さんらしいアグレッシブで、グイグイにイニシアチブをもっていってくれるじゃないか。」
    "不知道别人是怎么样的，但是对里昂来像就和平时一样的感觉吗。这是外国人特有的积极吗，会给人以积极主动的感觉呢"

    # nil 「恵まれた陽光に照らされて、俺とリオンを乗せた２５０ｃｃのバイクは、デートスポットＹＯＫＯＨＡＭＡに向けて走り出した。」
    "在天赐的阳光照耀下，搭载着我和里昂的250ｃｃ摩托车，朝着约会地点YOKOHAMA出发了（L:YOKOHAMA，前面提到的横滨港）"

    # 摩托车引擎声（单次）
    play sound "voice/effect/05_巡航／高速.ogg"

    # nil 「押し当てられたナイスおっぱいに意識がどうしてもいってしまうが…。」
    "无论如何都会意识到的压在后背的好欧派…"

    # 里昂 「あ、蓮くん。玉川から第三京浜で港北インターで降りると高速料金安いよ」
    voice "voice/リオン/ron_a1_0228.ogg"
    lion リオン_私服_基本_微笑み "啊，莲君，从玉川到第三京滨到港北高速公路出口，高速公路过路费会便宜些哦"

    # 莲 「詳しすぎるだろ！？」
    lian "太详细了吧！？"

    # 画面快速切换，心爱Side！
    stop sound
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 0.2, ramplen=128, reverse=True, alpha=True, time_warp=None)

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ターゲット、動きました。これより追跡を開始します」
    voice "voice/心愛/cca_a1_0665.ogg"
    ai 心愛_私服_基本_無表情 "目标已经移动，现在开始追踪"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「君が運転するのか…」
    voice "voice/想瑠/sol_a1_0081.ogg"
    liu 想瑠_スーツ_驚き "是你开车吗……"

    # 刹车声
    play sound "voice/effect/15_ブレーキ2.ogg"
    play music bgmsixteen fadeout 0.8 fadein 1.0

    # 场景切换到横滨港
    image bg 横浜_山下公園 = "images/bg/横浜_山下公園.png"
    scene 横浜_山下公園 with ImageDissolve("images/tr/縦ブラインド.png", 0.2, ramplen=128, reverse=True, alpha=True, time_warp=None)

    # nil 「リオンの指示通り、第三京浜で港北インターに降りて、横浜に来ました。」
    "按照里昂的指示，在第三京滨下到港北高速公路出口，来到了横滨"

    # nil 「まずは、みなとみらいです。」
    "首先是港未来"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「わー！　綺麗な町並みだねー！　近未来感あるよ！」
    show リオン_私服_基本_驚き_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0229.ogg"
    lion リオン_私服_基本_驚き_1 "哇！好漂亮的街道啊！很有未来感！"

    # 莲 「あ。この辺は綺麗だよな、横浜はじめてか？」
    lian "啊。这附近很漂亮啊，是第一次来横滨吗？"

    # 里昂 「うん！　ていうか、観光そのものが初めて！　前日本に来た時はそんな余裕なくて…本当は今回も観光なんてするつもりはなかったからすっごく嬉しいよー！」
    show リオン_私服_基本_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0230.ogg"
    lion リオン_私服_基本_嬉しい "嗯！话说回来，这是我第一次来观光！之前来日本的时候没那么多空闲…其实这次本来也没打算去观光，所以非常开心！"
    hide リオン_私服_基本_驚き_1

    # 莲 「よし、じゃぁデートコースは俺に任せてくれていんだよな」
    lian "好的，那么约会路线就交给我吧"

    # 里昂 「All right！期待してるぜー？」
    show リオン_私服_基本_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0231.ogg"
    lion リオン_私服_基本_ニタァ "All right！我很期待哦——？"
    hide リオン_私服_基本_嬉しい

    # 莲 「あれ？　そういえばマイケルは？」
    lian "咦？这么说来迈克尔呢？"

    # 里昂 「預けてきたよ！　家に留守番させると、ボンベとか吸い出しちゃうんだ」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%9C%E3%83%B3%E3%83%99
    show リオン_私服_基本_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0232.ogg"
    lion リオン_私服_基本_微笑み "把它寄放出去了！如果让他看家的话，他会把气瓶吸干的"
    hide リオン_私服_基本_ニタァ

    # 莲 「預けるあてがあるのか…喋る帽子を…」
    lian "有寄存的地方吗…会说话的帽子……"

    # nil 「と、いうことで、リオンちゃんとデートの様子をダイジェストでお送り致します。」
    "那么，把和里昂约会的情况做个摘要来讲述一下吧"

    # 场景切换到山丘公园
    image bg 横浜_港の見える丘公園 = "images/bg/横浜_港の見える丘公園.png"
    scene 横浜_港の見える丘公園 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「デートスポットNo,1」
    "约会地点No,1（L:原作这里就是逗号，后面打的是NO.，只有这里是No,）"

    # nil 「港の見える丘公園及びその周辺にやってきました。」
    "来到了能看到港口的山丘公园及其周边地方"

    # 里昂 「とうちゃーく！」
    show リオン_私服_基本_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0233.ogg"
    lion リオン_私服_基本_にっこり "到咯——！"

    # 莲 「この辺は、景色もそうなんだけど、異国情緒溢れる建物とか多いよな。リオン、そういうの好きかとおもって」
    lian "这附近风景也不错，有很多充满异国风情的建筑。里昂，我觉得你会很喜欢"

    # 里昂 「好きだよ！　母国に帰ったみたいでさ！」
    show リオン_私服_基本_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0234.ogg"
    lion リオン_私服_基本_嬉しい "喜欢啊！就像回到祖国一样！"
    hide リオン_私服_基本_にっこり

    # 莲 「あっそういえば異国の人そのものでした」
    lian "啊，这么说来，我在这里就是外国人呢"

    # 里昂 「ビアガーデン発見！」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%93%E3%82%A2%E3%82%AC%E3%83%BC%E3%83%87%E3%83%B3
    show リオン_私服_基本_驚き_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0235.ogg"
    lion リオン_私服_基本_驚き_1 "Biergarten发现！（L:Biergarten，啤酒花园，是一个提供啤酒和食物的户外区域，起源19世纪德国慕尼黑，简单来说就是在外面摆上桌椅，可以在那里喝酒吃东西）"
    hide リオン_私服_基本_嬉しい

    # 莲 「真っ昼間っから酒はダメだ。というか未成年はダメだ」
    lian "大白天不能喝酒，或者说未成年是不行的"

    # 里昂 「イギリス人は５歳から飲んでもいのだよ…。ちなみに私は１８だから購入もできるよ！」
    show リオン_私服_基本_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0236.ogg"
    lion リオン_私服_基本_ニタァ "英国人从5岁开始就可以喝酒了……顺便说一句，我18岁了，可以买酒了！"
    hide リオン_私服_基本_驚き_1

    # 莲 「一応日本の法は守ってくれ！」
    # 参考资料：https://www.gmosign.com/media/trend/post-0053/
    lian "姑且还是遵守日本的法律吧！（日本《民法》第4条规定20岁为成年年龄，不过最近的最新修正案把这个年龄修改到了18岁，但是喝酒仍然是要20岁）"

    # 场景切换到横滨唐人街
    image bg 横浜_中華街 = "images/bg/横浜_中華街.png"
    scene 横浜_中華街 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「デートスポットNO.2」
    "约会地点NO.2"

    # nil 「中華街で食べ歩きです。」
    "在唐人街里边走边吃"

    # 里昂 「中華街といえば、炎の料理人がプロデュースした肉まんがありますよね」
    # 参考资料：https://ja.wikipedia.org/wiki/%E5%91%A8%E5%AF%8C%E5%BE%B3
    show リオン_私服_基本_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0237.ogg"
    lion リオン_私服_基本_微笑み "说到唐人街，不是有炎之料理人的肉包嘛（L:这里说的是周富徳(1943年3月11日 - 2014年4月8日)广东菜厨师，出身横滨唐人街，爱称「炎の料理人」，父母出身广东，父亲在横滨唐人街做厨师，90年代常出现在电视上，后因涉嫌性骚扰逐渐淡出公众视野）"

    # 莲 「なぁお前本当にイギリス人か？　日本人ですら忘れかけてるぞそれ」
    lian "你真的是英国人吗？连日本人都快忘记他了"

    # 里昂 「甦れ！　周とみと―」
    # 参考资料：https://ja.wikipedia.org/wiki/%E4%B8%AD%E8%8F%AF%E4%B8%80%E7%95%AA!
    show リオン_私服_基本_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0238.ogg"
    lion リオン_私服_基本_ニタァ "惊醒吧！周富——（L:前半句“甦れ！”是中華一番!(中华小当家第17话标题的前半)）"
    hide リオン_私服_基本_微笑み

    # 莲 「死んでねぇよ！！」
    # 参考资料：https://vndb.org/v14082/releases
    lian "还没死啊！！（L:本作发售于13年12月31日，然而本作实体版发行之后的第98天，本作下载版发行之后的第92天，他就……甚至没到100天，这……因果律武器没跑了）"

    # nil 「……」
    "……"

    # 里昂 「杏仁ソフトクリーム…これは…いける！」
    show リオン_私服_基本_無表情_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0239.ogg"
    lion リオン_私服_基本_無表情_1 "杏仁软雪糕……这……可以的！"
    hide リオン_私服_基本_ニタァ

    # 莲 「お、リオンが本気モードだ」
    lian "哦，里昂切换到认真模式了"

    # 里昂 「はい、蓮くん。あーん」
    show リオン_私服_基本_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0240.ogg"
    lion リオン_私服_基本_微笑み "来，莲君，啊——嗯"
    hide リオン_私服_基本_無表情_1

    # 莲 「あーん」
    lian "啊——嗯"

    # nil 「ずるっ」
    "咬"

    # 里昂 「あっ」
    show リオン_私服_基本_驚き_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0241.ogg"
    lion リオン_私服_基本_驚き_1 "啊"
    hide リオン_私服_基本_微笑み

    # 莲 「ほげぇ」
    lian "呜欸"

    # 里昂 「まぁいや、あーん」
    show リオン_私服_基本_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0242.ogg"
    lion リオン_私服_基本_微笑み "嘛，算了，啊——"
    hide リオン_私服_基本_驚き_1

    # 莲 「平然とリテイクするなよ！？」
    lian "不要泰然自若地重演啊！？"

    # 里昂 「あーん」
    show リオン_私服_基本_ジト目_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0243.ogg"
    lion リオン_私服_基本_ジト目_1 "啊——嗯"
    hide リオン_私服_基本_微笑み

    # 莲 「あーん」
    lian "啊——嗯"

    # 场景切换到横滨大栈桥国际客轮码头
    image bg 横浜_大桟橋 = "images/bg/横浜_大桟橋.png"
    scene 横浜_大桟橋 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「デートスポットNO.3」
    "约会地点NO.3"

    # nil 「横浜大さん橋国際客船ターミナル」
    # 参考资料：https://ja.wikipedia.org/wiki/%E5%A4%A7%E3%81%95%E3%82%93%E6%A9%8B
    # 官方网站：https://osanbashi.jp/
    # Live Camera：https://osanbashi.jp/english/floor/arrival.php
    "横滨大栈桥国际客轮码头"

    # 里昂 「あ、これさっき遠くから見た時に、巨大空母かと思ってたんだけど、違うんだね」
    show リオン_私服_基本_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0244.ogg"
    lion リオン_私服_基本_微笑み "啊，刚才从远处看的时候，我还以为是巨大的航空母舰，原来不是啊"

    # 莲 「あーん」
    lian "雀食，颜色和形状都没有桥的感觉"

    # 里昂 「ねぇ、蓮くん！巨大空母ってどこにあるのかな！」
    show リオン_私服_基本_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0245.ogg"
    lion リオン_私服_基本_嬉しい "呐，莲君，巨型航空母舰在哪里？"
    hide リオン_私服_基本_微笑み

    # 莲 「空母は見たことねぇけど、原潜なら隣町の横須賀にあるな」
    # 参考资料：https://www.kanaloco.jp/news/social/article-798925.html
    # 较新参考资料：https://www.pref.kanagawa.jp/docs/bz3/cnt/f417274/index.html
    lian "没见过航空母舰，不过如果是核潜艇的话就在邻町的横须贺（L:横须贺的美军基地有停靠核动力潜艇，翻译时最近一次是在2022年3月20日）"

    # 里昂 「行こう！　行こう！　行こう！」
    show リオン_私服_基本_驚き_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0246.ogg"
    lion リオン_私服_基本_驚き_1 "去看吧！去看吧！去看吧！"
    # lion リオン_私服_基本_驚き_1 "快去吧！快去吧！快去吧！"
    hide リオン_私服_基本_嬉しい

    # 莲 「…まじすか」
    lian "…真的吗？"

    # 场景切换到横须贺
    image bg 横須賀 = "images/bg/横須賀.png"
    scene 横須賀 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「デートスポットNO.4」
    "约会地点NO.4"

    # 里昂 「やったー！　ほらほらみえる？　あれ！　イージス艦だよ！　あの六角形のレーダーがイージス艦の特徴なんだ！」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%A4%E3%83%BC%E3%82%B8%E3%82%B9%E8%89%A6
    show リオン_私服_基本_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0247.ogg"
    lion リオン_私服_基本_嬉しい "好耶！那个那个，看到了吗？那个就是宙斯盾舰！六边形的雷达就是宙斯盾舰的特征！（L:搭载宙斯盾的有巡洋舰、驱逐舰和巡防舰，美国汉军、日本海上自卫队、大韩民国海军、西班牙海军、挪威皇家海军、澳大利亚皇家海军和加拿大皇家海军均在使用宙斯盾系统，分为海基与陆基两种）"

    # 莲 「ほう」
    lian "哦"

    # 里昂 「キャー☆　原子力潜水艦だー☆　あのすべすべ感たまらないよねぇ…欲しいなぁ…」
    show リオン_私服_基本_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0248.ogg"
    lion リオン_私服_基本_にっこり "呀哦☆是原子能潜水艇啊☆那个滑溜溜的感觉真让人受不了……真想要啊……"
    hide リオン_私服_基本_嬉しい

    # 莲 「ほう」
    lian "哦"

    # 里昂 「一個ぐらい買っちゃおうかな…」
    show リオン_私服_基本_ジト目_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0249.ogg"
    lion リオン_私服_基本_ジト目_1 "买一个吧……"
    hide リオン_私服_基本_にっこり

    # 莲 「その前にアイス屋作れよ…」
    lian "在那之前先开个冰淇淋店吧…"

    # 里昂 「ぎくぅ！　で、でも、どこかの車メーカーの社長は、若い頃外車を買って運営資金なくしちゃったけど頑張ったみたいなエピソードもあるし！」
    show リオン_私服_基本_驚き_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0250.ogg"
    lion リオン_私服_基本_驚き_1 "啊这！但是，某汽车制造商的社长年轻的时候买了外国车，失去了运营资金，但是也有努力过的轶事！（L:找了一圈，真没找到，这都什么阴间梗……）"
    hide リオン_私服_基本_ジト目_1

    # 莲 「外車とかそういう単位で買えるもんじゃねぇぞ！？こっちの、ふわふわ潜水艦ストラップなら買ってあげるから、しばらくはこれで我慢するんだ」
    lian "这可不是以外国车做单位就能买得起的！？我会给你买潜水艇挂饰的，暂时就用这个将就一下吧"

    # 里昂 「！！！　れ、蓮くんから初めてプレゼントもらっちゃった…。ありがとう！　宝物にするね！」
    show リオン_私服_基本_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0251.ogg"
    lion リオン_私服_基本_にっこり "！！！这，这是莲君第一次送我礼物……谢谢！我要把它当成宝物！"
    hide リオン_私服_基本_驚き_1

    # 莲 「…もうちょっとマシなもんにしておけばよかったな」
    lian "…要是再稍微好一点就好了"

    # 里昂 「ぷにぷにすると燃料が漏れ出すギミックがついてるよ！」
    # 参考资料：https://dictionary.goo.ne.jp/word/%E3%81%B7%E3%81%AB%E3%81%B7%E3%81%AB/
    show リオン_私服_基本_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0252.ogg"
    lion リオン_私服_基本_微笑み "噗腻噗腻的（L:形容有柔软弹力），如果对着它吹气，燃料就会漏出来！"
    hide リオン_私服_基本_にっこり

    # 莲 「それヤバくねぇかな」
    lian "那不是很糟糕吗"

    # 里昂 「昔あったよね、動物の形して、ぷにって押すとウンチが飛び出るキーホルダー」
    show リオン_私服_基本_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0253.ogg"
    lion リオン_私服_基本_嬉しい "以前我有一个动物形状的钥匙圈，一按就会大便冒出来"
    hide リオン_私服_基本_微笑み

    # 莲 「それと一緒にしちゃまずい気がするんだよな…潜水艦の燃料って」
    lian "和那个放在一起的话感觉不太好啊…潜水艇的燃料"

    # 场景切换到横滨红砖仓库
    image bg 横浜_赤煉瓦 = "images/bg/横浜_赤煉瓦.png"
    scene 横浜_赤煉瓦 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「デートスポットNO.5」
    "约会地点NO.5"

    # nil 「横浜に戻ってくるまでに、夕方になりました。」
    "在回到横滨之前，已经是傍晚了"

    # nil 「担任の言う通り、赤レンガ倉庫付近のバイク駐輪場に駐車します。」
    "正如班主任说的那样，把车停在红砖仓库附近的摩托车停车场"

    # nil 「こからは徒歩です。」
    "从这儿开始步行"

    # 里昂 「赤レンガ倉庫…これ、中身なんなの？」
    show リオン_私服_基本_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0254.ogg"
    lion リオン_私服_基本_微笑み "红砖仓库……这个，里面是什么东西呢"

    # 莲 「倉庫じゃね？」
    lian "不是仓库吗？"

    # 里昂 「入ってみようよ！」
    show リオン_私服_基本_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0255.ogg"
    lion リオン_私服_基本_ニタァ "进去康康吧！"
    hide リオン_私服_基本_微笑み

    # 画面切换为 Black
    scene black with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # 里昂 「ショッピングセンターだ…」
    show リオン_私服_基本_驚き_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0256.ogg"
    lion リオン_私服_基本_驚き_1 "购物中心啊……"

    # 莲 「ほんとだ、ショッピングセンターだ…」
    lian "真的，是购物中心啊……"

    # 莲 「ちなみに、冬になるとアイスケートリンクが出現します」
    lian "顺带一提，到冬天就会出现溜冰场"

    # 里昂 「まじで！来よう！」
    show リオン_私服_基本_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0257.ogg"
    lion リオン_私服_基本_嬉しい "真的！来吧！"
    hide リオン_私服_基本_驚き_1

    # 莲 「そうだな」
    lian "是啊"

    # nil 「リオンが冬まで日本に居るかは…別だが…。」
    "里昂到冬天为止是否还在日本…不好说啊…"

    # 里昂 「ん？　どしたの？」
    show リオン_私服_基本_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0258.ogg"
    lion リオン_私服_基本_微笑み "嗯？怎么了？"
    hide リオン_私服_基本_嬉しい

    # 莲 「いや、ちょっと考え事をな」
    lian "没什么，只是稍微想了点事情"

    # 里昂 「むー？　デート中に、相手に無断で考え事とは、看過できませんなぁ？」
    show リオン_私服_基本_ジト目 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0259.ogg"
    lion リオン_私服_基本_ジト目 "嗯？在约会的时候，不经对方允许就想其它事情，这可不能放过啊？"
    hide リオン_私服_基本_微笑み

    # 莲 「あ、あ…すまん。忘れてくれ」
    lian "啊，啊…对不起，忘了吧"

    # 里昂 「むしろ忘れさせてやるさ！」
    show リオン_私服_基本_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0260.ogg"
    lion リオン_私服_基本_ニタァ "我宁愿让你忘记！"
    hide リオン_私服_基本_ジト目

    # nil 「ぎゅっ」
    "贴"

    # 莲 「なっ…」
    lian "什么…"

    # 里昂 「これから歩いてぶらぶらするんでしょー？　だったら手ぐらい繋ごうよー！」
    show リオン_私服_基本_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0261.ogg"
    lion リオン_私服_基本_嬉しい "你接下来不是要走路去逛逛吗？那我们就牵手吧！"
    hide リオン_私服_基本_ニタァ

    # nil 「不意打ちで、お留守になっていた右手を左手で捕まれる。」
    "出其不意地，右手被里昂的左手抓住了"

    # 里昂 「だめー？　今まではバイクで身体くっついたからいけど、一緒に歩くのに離れてるの寂しいよぉ…」
    show リオン_私服_基本_ジト目_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0262.ogg"
    lion リオン_私服_基本_ジト目_1 "不可以吗？刚才都是骑摩托车来的，现在又不能一起走的话，实在是太寂寞了……"
    hide リオン_私服_基本_嬉しい

    # nil 「普段のアイス売りのリオンとは、全く様子が違う。まさに、普通の甘えん坊な女の子そのものだ。」
    "和平时卖冰淇淋的里昂完全不一样。现在是一个普通爱撒娇的女孩子"

    # nil 「というか、こまで甘えん坊なのか！？　」
    "或者说，本来就是爱撒娇的孩子吗！？"

    # nil 「オンオフの切り替え激しいな…。」
    "开关切换好激烈啊…"

    # nil 「こまできて「リオンが良いなら」なんて問うのは愚問だ。」
    "事到如今问「里昂这样可以吗」是愚蠢的问题"

    # 莲 「よし、行くか」
    lian "好，走吧"

    # nil 「リオンの手を握り返す。」
    "握住里昂的手"

    # 里昂 「うんっ！　えへへ…デート、デート♪」
    show リオン_私服_基本_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0263.ogg"
    lion リオン_私服_基本_にっこり "嗯！欸嘿嘿……约会，约会♪"
    hide リオン_私服_基本_ジト目_1

    # nil 「本格的に、恋人ライクなデートの開始だ。」
    "正式开始，恋人般的约会"

    # nil 「言葉での確認こそしなかったが、こういう中途半端な距離感。悪くない。」
    "虽然没有口头确认，但是这种半吊子的距离感，还不错"

    # nil 「リオンの手を引いて、デートの第二ラウンドといこう。」
    "牵着里昂的手，去开始第二轮的约会吧"

    # 场景并没有切换

    # nil 「デートスポットNO.6」
    "约会地点NO.6"

    # nil 「カップヌードルミュージアム」
    "杯面博物馆"

    # 场景在这里切换到杯面博物馆
    image bg 横浜_カップヌードルミュージアム = "images/bg/横浜_カップヌードルミュージアム.png"
    scene 横浜_カップヌードルミュージアム with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # 里昂 「閉館時間でした」
    show リオン_私服_基本_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0264.ogg"
    lion リオン_私服_基本_悲しい "闭馆时间到了"

    # 莲 「……」
    lian "……"

    # 场景在这里切换到横滨皇后广场
    image bg 横浜_クイーンズスクエア = "images/bg/横浜_クイーンズスクエア.png"
    scene 横浜_クイーンズスクエア with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「デートスポットNO.7」
    "约会地点NO.7"

    # nil 「クイーンズスクエア」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%AF%E3%82%A4%E3%83%BC%E3%83%B3%E3%82%BA%E3%82%B9%E3%82%AF%E3%82%A8%E3%82%A2%E6%A8%AA%E6%B5%9C
    "横滨皇后广场（L:是港未来的一座大型设施，由三栋高层建筑和购物中心、饭店、音乐厅等设施构成。开业于1997年7月18日。A栋高172米、地上36层、地下5层；B栋高138米、地上28层、地下5层；C栋高109米、地上21层、地下5层）"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 花盆君在左的参数
    transform love69_huapen_left:
        zoom 0.89
        xalign 0.245
        yalign -18.0

    # 热狗 「はぁい、では今からぁこの植木鉢にーバレーボールをぶつけます！」
    show 想瑠_hot_ニヤリ at love69_xiangliu_right
    show 花盆君_通常 at love69_huapen_left
    with dissolve
    voice "voice/想瑠/sol_a1_0082.ogg"
    hotdog 想瑠_hot_ニヤリ "好的，那么现在我要用排球砸这个花盆了！"

    # 这个语句是针对花盆君设计的参数，能够调整花盆君在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.15
    $ sideimagesize.SideImageYalign = 1.21
    $ sideimagesize.SideImageZoom = 0.5

    # 花盆君 「…！？」
    hide 花盆君_通常
    show 花盆君_通常:
        zoom 0.89
        xalign 0.245
        yalign -18.0
        linear 0.15 yalign -15.0
        linear 0.15 yalign -18.0
    voice "voice/アシュリー/ash_a1_0029.ogg"
    pen 花盆君_通常 "…！？"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 热狗 「それではみなさん！　無事成功しましたら盛大な拍手をお願いします！」
    voice "voice/想瑠/sol_a1_0083.ogg"
    hotdog "那么，米娜桑！如果顺利成功了，就请大家热烈鼓掌！"

    # 这个语句是针对花盆君设计的参数，能够调整花盆君在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.15
    $ sideimagesize.SideImageYalign = 1.21
    $ sideimagesize.SideImageZoom = 0.5

    # 花盆君 「…（ふるふる）」
    hide 花盆君_通常
    show 花盆君_通常:
        zoom 0.89
        xalign 0.245
        yalign -18.0
        linear 0.15 yalign -14.5
        linear 0.15 yalign -18.0
    voice "voice/アシュリー/ash_a1_0030.ogg"
    pen 花盆君_通常 "…（颤抖颤抖）"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 热狗 「カウントダウンいきまーす！」
    show 想瑠_hot_見下し at love69_xiangliu_right with dissolve
    voice "voice/想瑠/sol_a1_0084.ogg"
    hotdog 想瑠_hot_見下し "开始倒计时！"
    hide 想瑠_hot_ニヤリ

    # 热狗 「ワン！」
    show 想瑠_hot_ニヤリ at love69_xiangliu_right with dissolve
    voice "voice/想瑠/sol_a1_0085.ogg"
    hotdog 想瑠_hot_ニヤリ "One！"
    hide 想瑠_hot_見下し

    # 热狗 「ツー！」
    voice "voice/想瑠/sol_a1_0086.ogg"
    hotdog "Two——！"

    # 这个语句是针对花盆君设计的参数，能够调整花盆君在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.15
    $ sideimagesize.SideImageYalign = 1.21
    $ sideimagesize.SideImageZoom = 0.5

    # 花盆君 「！！！」
    hide 花盆君_通常
    show 花盆君_通常:
        zoom 0.89
        xalign 0.245
        yalign -18.0
        linear 0.15 yalign -12.0
        linear 0.15 yalign -18.0
    voice "voice/アシュリー/ash_a1_0031.ogg"
    pen 花盆君_通常 "！！！"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 热狗 「ギャァー！」
    show 想瑠_hot_驚き at love69_xiangliu_right with dissolve
    voice "voice/想瑠/sol_a1_0087.ogg"
    hotdog 想瑠_hot_驚き "呀——！"
    hide 想瑠_hot_ニヤリ

    # 花盆君退场，亚十礼登场
    hide 花盆君_通常
    show アシュリー_私服_驚き at love69_atri_left
    with dissolve

    # nil 「ポロッ」
    "啵咯"

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # L:似乎花盆君的音就是亚十礼的CV配的
    # 亚十礼 「あ」
    voice "voice/アシュリー/ash_a1_0032.ogg"
    atri アシュリー_私服_驚き "啊"

    # 莲 「あ」
    lian "啊"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「あ」
    voice "voice/リオン/ron_a1_0265.ogg"
    lion リオン_私服_基本_驚き "啊"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 热狗 「あ」
    voice "voice/想瑠/sol_a1_0088.ogg"
    hotdog "啊"

    # 热狗 「中身でちゃった」
    show 想瑠_hot_ぶわ at love69_xiangliu_right with dissolve
    voice "voice/想瑠/sol_a1_0089.ogg"
    hotdog 想瑠_hot_ぶわ "在里面啊"
    hide 想瑠_hot_驚き

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「……」
    voice "voice/アシュリー/ash_a1_0033.ogg"
    atri "……"

    hide アシュリー_私服_驚き
    show 花盆君_通常 at love69_huapen_left
    with dissolve

    # 这个语句是针对花盆君设计的参数，能够调整花盆君在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.15
    $ sideimagesize.SideImageYalign = 1.21
    $ sideimagesize.SideImageZoom = 0.5

    # nil 「モゾッ」
    "哗啦"

    # 花盆君 「……」
    voice "voice/アシュリー/ash_a1_0034.ogg"
    pen 花盆君_通常 "……"

    # 莲 「いやいやいやいや」
    lian "呀呀呀呀"

    # 场景切换到山下公园
    image bg 横浜_山下公園_夜 = "images/bg/横浜_山下公園_夜.png"
    scene 横浜_山下公園_夜:
        truecenter
        zoom 1.0
        xalign 0.5
        yalign 0.5
    with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「デートスポットNO.8」
    "约会地点NO.8"

    # nil 「山下公園まで歩いてきました。」
    "一路走到了山下公园"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「わ…この時間はほんとカップルばっかだね…どのベンチもカップルしか座ってないよ…ドキドキするよ…」
    show リオン_私服_基本_悲しい2_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0266.ogg"
    lion リオン_私服_基本_悲しい2_1 "哇哦……这个时候真的到处都是情侣呢……每张长椅上坐的都是……真是让人dokidoki呢……"

    # 莲 「ちょうど、本日のデートの反省会な時間帯だよな」
    lian "正好，是今天约会反省会的时间了呢"

    # 里昂 「は、反省会！？　ま、まだデートは終わりじゃないよね！？」
    show リオン_私服_基本_驚き_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0267.ogg"
    lion リオン_私服_基本_驚き_1 "哈，反省会！？约，约会还没结束吧！？"
    hide リオン_私服_基本_悲しい2_1

    # 莲 「何言ってんだよ、これからが本番だろ」
    lian "你在说什么呢，从现在才是正式演出哦"

    # 里昂 「うん！　でもこの公園、船とコンビニしかないね…あとベンチ」
    show リオン_私服_基本_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0268.ogg"
    lion リオン_私服_基本_微笑み "嗯！不过这个公园只有船和便利店……还有长椅"
    hide リオン_私服_基本_驚き_1

    # 莲 「ベンチ座っちゃう？」
    lian "要坐在长椅上吗？"

    # 里昂 「座っちゃう－？」
    show リオン_私服_基本_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0269.ogg"
    lion リオン_私服_基本_嬉しい "要坐下嘛？"
    hide リオン_私服_基本_微笑み

    # nil 「……」
    "……"

    # 里昂 「満員でした」
    show リオン_私服_基本_ぶわー at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0270.ogg"
    lion リオン_私服_基本_ぶわー "人满为患了"
    hide リオン_私服_基本_嬉しい

    # 莲 「次いこか」
    lian "下次吧"

    # 里昂 「はーい♪」
    show リオン_私服_基本_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0271.ogg"
    lion リオン_私服_基本_にっこり "好♪"
    hide リオン_私服_基本_ぶわー

    play music bgmthirtysix fadeout 2.0 fadein 2.0
    image bg 横浜_観覧車 = "images/bg/横浜_観覧車.png"
    scene 横浜_観覧車 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「デートスポットNO.⑨」
    "约会地点NO.⑨"

    # nil 「大さん橋リターンズ」
    "回到了大栈桥"

    # 里昂 「なんか、青いＬＥＤが、より一層最先端空母感を出してるね…」
    show リオン_私服_基本_驚き_1 at love69_lion_center with dissolve
    # voice "voice/リオン/ron_a1_0272.ogg"
    lion リオン_私服_基本_驚き_1 "怎么说呢，蓝色的LED灯亮了之后更让人觉得是最先进的航空母舰了呢…（L:这里也莫得配音……）"

    # 莲 「やっぱ、こういうスベスベ感って興奮すんの？」
    lian "果然，这种滑溜溜的感觉会让人兴奋吗？"

    # 里昂 「する！　い、今更だけど…私、最先端兵器みたいな角張ったデザイン好きなんだよね…。あとはつや消しのマットな質感とか…」
    show リオン_私服_基本_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0273.ogg"
    lion リオン_私服_基本_微笑み "对！现、现在才知道……我喜欢最先进武器那种棱角分明的设计……还有就是那种磨砂的质感……"
    hide リオン_私服_基本_驚き_1

    # 莲 「まぁ、あんな原潜見て興奮してたぐらいだしな…」
    lian "嘛，看到那样的核潜艇还真是兴奋啊…"

    # 里昂 「そ、それよりも、今は…えと…別の事で興奮し、してるけどね？」
    show リオン_私服_基本_悲しい2_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0274.ogg"
    lion リオン_私服_基本_悲しい2_1 "那个，比起那个，现在……嗯…因为别的事情很兴奋吧？"
    hide リオン_私服_基本_微笑み

    # nil 「そう言いながら、リオンは辺りを指差した。」
    "这样说着，里昂指着周围"

    # 莲 「…こも、カップルばっかだな」
    lian "呃，都是情侣啊"

    # 里昂 「う、うん…どこ行ってもカップルがイチャイチャして…。うわーって思いながらも、私達も近しい事してるなーと考えて興奮しちゃって…」
    show リオン_私服_基本_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0275.ogg"
    lion リオン_私服_基本_嬉しい "嗯，嗯…不管去哪里都会有情侣在亲热…虽然想着“哇——”，但是想着我们也在做这样亲近的事情，所以很兴奋…"
    hide リオン_私服_基本_悲しい2_1

    # 莲 「あ、あんた、アレだよな…恋が叶う魔法のアイスとか作っておきながら、自分の恋愛には疎いのか」
    lian "啊，你，是那个吧……一边做着能实现恋爱的魔法冰淇淋，一边对自己的恋爱不了解吗？"

    # 里昂小跳

    # 里昂 「い、いーまーはそういうこといわないのー！　それとこれは別なんだからー！」
    hide リオン_私服_基本_嬉しい
    show リオン_私服_基本_ジト目_1:
        zoom 1.5
        yalign 0.07
        xalign 0.5
        linear 0.15 yalign 0.14
        linear 0.15 yalign 0.07
    voice "voice/リオン/ron_a1_0276.ogg"
    lion リオン_私服_基本_ジト目_1 "事、事到如今就不要说那种事情啦——！那个和这个是两码事！"

    # nil 「ぽかぽかぽかぽかぽか」
    "扑通扑通扑通扑通扑通"

    # 莲 「ごめんごめんて。今のは俺が悪かった」
    lian "对不起，对不起。刚才是我不好"

    # 里昂 「ぷっぷくぷー！」
    voice "voice/リオン/ron_a1_0277.ogg"
    lion "噗噗噗——！"

    # 莲 「ぷー」
    lian "噗"

    # 里昂 「ぷー」
    show リオン_私服_基本_にっこり_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0278.ogg"
    lion リオン_私服_基本_にっこり_1 "噗"
    hide リオン_私服_基本_ジト目_1

    # nil 「なんていうか…マジでリオン、イチャイチャスイッチがオンになってるな。」
    "怎么说呢…真的是，里昂的爱情开关开着的呢"

    # 里昂 「これじゃぁ本当にバカップルだね私達…」
    show リオン_私服_基本_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0279.ogg"
    lion リオン_私服_基本_微笑み "这样的话我们真的是笨蛋情侣呢…"
    hide リオン_私服_基本_にっこり_1

    # 莲 「急に素に戻るなよ」
    lian "不要突然变回来啊"

    # 里昂 「いやぁ、ちょっと気恥ずかしくて…一夏の思い出って奴かなー」
    show リオン_私服_基本_悲しい2 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0280.ogg"
    lion リオン_私服_基本_悲しい2 "呀，有点害羞……真是一夏的回忆啊"
    hide リオン_私服_基本_微笑み

    # nil 「リオンは手すりに両手をついて、夜景を眺めた。その後ろ姿が、何故か切なかった。」
    "里昂双手托在扶手上，眺望夜景。不知为何，她的背影让人心痛"

    # nil 「リオンの何気ない一言で、俺は担任に言われたことを思い出す。」
    "里昂不经意的一句话，让我想起了班主任对我说的话"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「『その覚悟が、一夏の思い出にならん事を祈るよ』」
    voice "voice/想瑠/sol_a1_0090.ogg"
    liu 想瑠_スーツ_目閉じ "『希望你的觉悟不会成为一夏的回忆』"

    # nil 「言うなれば、確かにリオンの事は何も知らなかった。」
    "说起来，我确实对里昂一无所知"

    # nil 「スベスベ質感が好きだとか、まさか原潜で興奮するとか、趣味や好みも知らないし、」
    "我不知道你喜欢光滑的质感，不知道你会因为核子动力潜艇而兴奋，也不知道你的爱好和喜好"

    # nil 「何より、リオンがいつまで日本に居るかも知らなかった。」
    "最重要的是，我甚至不知道里昂在日本待到什么时候"

    # nil 「知らないま…こうしてリオンと時間を過ごしていくと、どんどん好きになる。」
    "不知不觉……像这样和里昂一起度过时间的话，就会渐渐喜欢上"

    # nil 「リオンの態度がまんざらじゃないから、よけいに好きになっていく。」
    # 参考资料：https://www.weblio.jp/content/%E3%81%BE%E3%82%93%E3%81%96%E3%82%89
    "因为里昂的态度完全不差，所以更加喜欢了"

    # nil 「それが、でも怖くて…。」
    "但是，我很害怕…"

    # nil 「担任に言われたことを思い出す。あの担任だって、人の恋愛にとやかく口を出すほど無粋ではないはずだ。」
    "我想起了班主任说的话。那个班主任应该也不至于对别人的恋爱说三道四"

    # nil 「（追ってきているのは知ってるけど）」
    "（我知道你在追我）"

    # nil 「となれば、リオンの裏には何かある。」
    "这样的话，里昂的背后是什么呢"

    # nil 「それはリオンだってわかっているはずだ。」
    "这个就得去问里昂了"

    # nil 「なのに…。」
    "但是…"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ん？　突然黙っちゃってどうしたの？」
    show リオン_私服_基本_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0281.ogg"
    lion リオン_私服_基本_驚き "嗯？突然沉默了，是怎么了？"
    hide リオン_私服_基本_悲しい2

    # 莲 「あいや…」
    lian "哎呀……"

    # 里昂 「まーた考え事ですかー？　もー何を悩んでるんだね君は。ツーアウトですよ！辛い事があるなら、お姉さんに話してみるといのに！」
    show リオン_私服_基本_見下し at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0282.ogg"
    lion リオン_私服_基本_見下し "你又在想什么呢？你到底在烦恼什么呢。是第二次出局了！如果有痛苦的事情的话，就和姐姐说说看吧"
    hide リオン_私服_基本_驚き

    # 莲 「同い年じゃないか」
    lian "不是同龄吗？"

    # 里昂 「でもお酒は飲み慣れてるよ！　ギャンブルもするし」
    show リオン_私服_基本_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0283.ogg"
    lion リオン_私服_基本_ニタァ "但是我已经习惯喝酒了！还会赌博"
    hide リオン_私服_基本_見下し

    # 莲 「じゃぁ、そんなお姉さんに一つ相談しよう」
    lian "那么，和这样的姐姐商量一下吧"

    # 里昂 「はいなんでしょう」
    show リオン_私服_基本_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0284.ogg"
    lion リオン_私服_基本_にっこり "好，是什么呢？"
    hide リオン_私服_基本_ニタァ

    # 莲 「どうよ夜景は」
    lian "夜景怎么样？"

    # 里昂 「ぶー。そういう思わせぶりなのはツーストライクぐらいあげたいなぁ！　こは蓮くんを配慮して、その質問に答えましょう」
    # 参考资料：https://en.wikipedia.org/wiki/Glossary_of_baseball_terms
    show リオン_私服_基本_無表情_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0285.ogg"
    lion リオン_私服_基本_無表情_1 "噗——这种故弄玄虚的话，我想给你两个Two Strike！这里就照顾莲君，回答那个问题吧（L:Two Strike只棒球打出两个好球）"
    hide リオン_私服_基本_にっこり

    # nil 「リオンはもう一度夜景の方を眺める。」
    "里昂再一次眺望夜景"

    # 里昂 「そうだねぇめっちゃ綺麗だよねぇ…」
    show リオン_私服_基本_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0286.ogg"
    lion リオン_私服_基本_嬉しい "是的啊，好漂亮啊…"
    hide リオン_私服_基本_無表情

    # nil 「俺はその背中をゆっくりと抱きしめ…」
    "我慢慢地抱住她的背…"

    # 里昂 「やっぱあの観覧車はどうしても気になるかな！」
    show リオン_私服_基本_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0287.ogg"
    lion リオン_私服_基本_ニタァ "果然还是很在意那个摩天轮啊！"
    hide リオン_私服_基本_嬉しい

    # 莲 「お、おう！」
    lian "哦，哦！"

    # nil 「抱きしめクエストは失敗に終わりました。」
    "拥抱任务以失败告终"

    # nil 「ちょっと周りの視線が痛いです。」
    "周围的视线有点疼"

    # nil 「だが、リオンが観覧車の話題を出したら今がチャンスだ！」
    "但是，如果里昂说起摩天轮的话题的话，现在正是机会！"

    # 莲 「あれ、乗るか？」
    lian "咦，要去坐嘛？"

    # 里昂 「え、いの！？　だ、男女二人っきりで観覧車乗るって、それは…もう、完全にカップルですよ…」
    show リオン_私服_基本_驚き_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0288.ogg"
    lion リオン_私服_基本_驚き_1 "可、可以吗！？只有男女两个人坐摩天轮？那已经完全是情侣了……"
    hide リオン_私服_基本_ニタァ

    # 莲 「なんだ嫌なのか？」
    lian "不愿意吗？"

    # 里昂 「い、嫌じゃないよ！　乗ろう！　めっちゃ乗ろう！　二周ぐらいしよう！」
    show リオン_私服_基本_見下し at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0289.ogg"
    lion リオン_私服_基本_見下し "不，我不讨厌！我们去坐吧！多坐两圈吧！"
    hide リオン_私服_基本_驚き_1

    # 莲 「二周でいのか？」
    lian "两圈可以吗？"

    # 里昂 「いや三周はちょっと…」
    show リオン_私服_基本_悲しい2 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0290.ogg"
    lion リオン_私服_基本_悲しい2 "不，三圈有点…"
    hide リオン_私服_基本_見下し

    # 莲 「そこは現実的かよ」
    lian "那样是现实的吗？"

    # 里昂 「えへへー…でも、観覧車は…締めくりには最高だねー」
    show リオン_私服_基本_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0291.ogg"
    lion リオン_私服_基本_にっこり "欸嘿嘿——……但是，摩天轮……收尾是最棒的——"
    hide リオン_私服_基本_見下し

    # 莲 「あ、そうだな…」
    lian "啊，是啊…"

    # nil 「締めくりか…それは少し寂しいな。皮肉で返してやろうかと思ったが…雰囲気に邪魔された。」
    "结束了吗…那有点寂寞呢。我本想这样说的，但是被气氛打断了"

    # nil 「でも、観覧車に向かう俺達は、いつしか、指と指を絡め合う恋人繋ぎに変わっていった。」
    "但是，前往摩天轮的我们，不知什么时候变成了手指和手指相互缠绕的恋人关系"

    # 场景切换到摩天轮
    image bg 横浜_観覧車2 = "images/bg/横浜_観覧車2.png"
    scene 横浜_観覧車2 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「デートスポットNO.10」
    "约会地点NO.10"

    # nil 「コスモランド　観覧車」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%88%E3%81%93%E3%81%AF%E3%81%BE%E3%82%B3%E3%82%B9%E3%83%A2%E3%83%AF%E3%83%BC%E3%83%AB%E3%83%89
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%B3%E3%82%B9%E3%83%A2%E3%82%AF%E3%83%AD%E3%83%83%E3%82%AF21
    "Cosmo World 摩天轮（L:横滨太空世界(Cosmo World)的Cosmo_Clock21摩天轮修建于1989年，最初是横滨博览会内的游乐设施之一。本来摩天轮预计将在博览会后拆除，但因人气高涨而得以保存，从1989年到1992年，它的直径和全长（包括底座的高度）都是世界上最大的）"

    # 里昂 「うひょー！　間近で見上げると迫力あるねー！」
    show リオン_私服_基本_驚き_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0292.ogg"
    lion リオン_私服_基本_驚き_1 "哇哦！近距离仰望的话很有魄力呢！"

    # 莲 「イギリスにはこういうのはないのか？」
    lian "英国没有这种东西吗？"

    # 里昂 「あるよー。ロンドン・アイっていう世界最大の観覧車がね！カメラにハマってた時、長時間露光で写真をとりにいったりしてたよ！」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%AD%E3%83%B3%E3%83%89%E3%83%B3%E3%83%BB%E3%82%A2%E3%82%A4
    # 参考资料：https://zh.wikipedia.org/wiki/%E6%96%B0%E5%8A%A0%E5%9D%A1%E6%91%A9%E5%A4%A9%E8%A7%82%E6%99%AF%E8%BD%AE
    show リオン_私服_基本_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0293.ogg"
    lion リオン_私服_基本_嬉しい "有啊。伦敦眼是世界上最大的摩天轮呢！沉迷于相机的时候，会长时间在室外拍照哦！（L:135m的高度在开业时是世界最高的，06年被中国南昌之星取代，目前最大的是美国内华达州天堂市赌城大道的High Roller，毫客摩天轮167.6m）"
    hide リオン_私服_基本_驚き_1

    # 里昂 「でも、外から撮るだけで、乗ったりはしてないから…」
    show リオン_私服_基本_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0294.ogg"
    lion リオン_私服_基本_微笑み "但是，只是从外面拍，没有坐过…"
    hide リオン_私服_基本_嬉しい

    # 莲 「そっか、地元民だもんな。わざわざ乗ったりはしないか」
    lian "这样啊，因为是本地人啊，所以不特意乘坐吗？"

    # 里昂 「小さい頃ぐらいだよー。だから、観覧車に乗るなんて久々だし…蓮くんと一緒なんて…わくわくしちゃうよね！」
    show リオン_私服_基本_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0295.ogg"
    lion リオン_私服_基本_嬉しい "大概是小时候吧。所以，好久没坐摩天轮了。和莲君在一起…好兴奋啊！"
    hide リオン_私服_基本_微笑み

    # 莲 「あ、俺も…ん？」
    lian "啊，我也是…嗯？"

    # 2022年1月19日的1000行更新达成，提交代码，开原，过几天就能抽甘雨了捏！

    # 风行迷踪真好玩~
    # 快给我常驻啊Kora！！！

    # nil 「俺は遠くに、あるものを見つけて、立ち止まる。」
    "我在远处，看到某样东西，停下脚步"

    # nil 「アイス屋の屋台か…。」
    "是冰淇淋店的摊子吗…"

    # nil 「リオンは怒るかな？」
    "里昂会生气吗？"

    # nil 「でも…。」
    "但是…"

    # 莲 「リオン、ちょっと先に並んでてくれないか？」
    lian "里昂，你能在前面先排一会儿吗"

    # 里昂 「ほ？　すぐ戻る？」
    show リオン_私服_基本_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0296.ogg"
    lion リオン_私服_基本_驚き "哦？马上回来？"
    hide リオン_私服_基本_嬉しい

    # 莲 「あ、すぐ戻る」
    lian "啊，马上回来"

    # 里昂 「わかった。じゃぁ乗るまえに戻って来てね」
    show リオン_私服_基本_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0297.ogg"
    lion リオン_私服_基本_微笑み "知道了，那在上车之前回来吧"
    hide リオン_私服_基本_驚き

    # 莲 「問題ない」
    lian "萌大奶（L:flag立起来了哦）"

    # nil 「リオンが不安げに問いかけてくるのが可愛らしい。」
    "里昂不安地问我真可爱"

    # nil 「観覧車の待ち時間を見る。１０分か…ぴったりかもな。」
    "看摩天轮的等待时间。10分钟啊…可能正好"

    # nil 「リオンに並ぶのを頼んで、俺は、アイス屋の屋台へと走った。」
    "我拜托里昂排队，跑到了冰淇淋店的摊子上"

    # 画面切换到远处
    scene 横浜_観覧車 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「しかし、こで計算外のイレギュラーが発生する。アイス屋にちょうど行列が出来てしまっていた。」
    "但是，这里发生了计算外的异常情况。冰淇淋店正好排起了队"

    # 莲 「（くそ…なんつータイミングで…）」
    lian "（可恶……这种时机就……）"

    # 女子学生A 「えーどうしよー、どれが美味しいと思う－？」
    play sound "voice/その他/o11_a1_0001.ogg"
    wsa "哎，怎么样，你觉得哪个好吃——？"

    # 女子学生B 「白い方かな」
    play sound "voice/その他/o12_a1_0001.ogg"
    wsb "会是白的那个吗"

    # nil 「……」
    "……"

    # 子供Ｅ（孩子Ｅ） 「うーん、どっちにしようかなぁ～。どっちがいかなぁ？」
    # 人物表++++++++++++++++
    play sound "voice/その他/o14_a1_0001.ogg"
    childe "嗯——，选哪个好呢~选哪个好呢？"

    # 母親Ｅ（妈妈E） 「白いのにしなさい」
    # 人物表++++++++++++++++
    play sound "voice/その他/o13_a1_0001.ogg"
    mothere "选白的那个吧"

    # nil 「……」
    "……"

    # 仔猫（小猫） 「ニャー（白い方で）」
    # 人物表+++++
    voice "voice/その他/cat_a1_0008.ogg"
    neko "喵呜——（白的那个）"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 横浜_観覧車 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # nil 「時間にしては３分も立ってないが、俺は苛立ってしまっていた。リオンを待たせるのは忍びない。」
    "就时间而言，我才站了不到三分钟，但我很焦躁，我不忍心让里昂等着"

    # nil 「やっと俺の番がまわってきた。」
    "终于轮到我了"

    # アイス屋さん（冰淇淋店） 「お待たせいたしました。いらっしゃいませー」
    # 人物表+++++
    # L:感觉是雾叶的声音捏
    # Scene13 一周目在夏威夷定义了冰淇淋店
    voice "voice/霧葉/krh_a1_0056.ogg"
    icecreamroom "让您久等了。欢迎光临"

    # 莲 「すいません、アイス２つ下さい！」
    lian "不好意思，请给我两个冰淇淋！"

    # アイス屋さん（冰淇淋店） 「はいはい、どれに致しましょう。当店では白いのが大体売れますけど…」
    voice "voice/霧葉/krh_a1_0057.ogg"
    icecreamroom "好的好的，您要哪一种呢？本店的话白色的大体上卖得很好……"

    # 莲 「この、緑色のチョコの奴とピンクと白と茶色の奴で」
    lian "这个，绿色巧克力的还有这个粉色、白色和茶色的这个"

    # アイス屋さん（冰淇淋店） 「白いのじゃなくていんですね…」
    voice "voice/霧葉/krh_a1_0058.ogg"
    icecreamroom "不点白色的可以吗……"

    # 莲 「白いのってバニラじゃないすか」
    lian "白色的不是香草吗"

    # アイス屋さん（冰淇淋店） 「コナッツです」
    voice "voice/霧葉/krh_a1_0059.ogg"
    icecreamroom "是椰子哦"

    # 莲 「あ、ちょっと美味そう。でも、緑の奴とピンクの奴を、コーンで」
    lian "啊，好像有点好吃的样子。不过，我要绿色的和粉色的，用玉米做的那个"

    # アイス屋さん（冰淇淋店） 「かしこまりましたー。少々お待ち下さい」
    voice "voice/霧葉/krh_a1_0060.ogg"
    icecreamroom "遵命，请稍等"

    # nil 「アイス屋さんは、こっちの急いでる様子を察してか、二割増しぐらいの作業スピードで、アイスをコーンに乗せてくれた。」
    "冰淇淋店老板也许是察觉到了我着急的样子，以快了大约二成的速度把冰淇淋放在了玉米上"

    # nil 「俺は代金を支払って、二つのアイスクリームを両手に受け取った。」
    "我付了钱，双手拿了两个冰淇淋"

    # アイス屋さん（冰淇淋店） 「さ、どうぞお幸せに。あ、あと、頑張って下さいね」
    voice "voice/霧葉/krh_a1_0061.ogg"
    icecreamroom "好了，祝您幸福。啊，还有，请加油"

    # 莲 「え？　あ、はい、ありがとうございます」
    lian "欸？啊，好的，谢谢"

    # nil 「アイス屋さんの台詞に質問を返したかったが、時間がないので、急いでリオンの元へ戻る事にした。」
    "我很想回答冰淇淋店老板的问题，但是时间紧迫，所以决定急忙回到里昂的身边"

    # 场景切回摩天轮下
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 横浜_観覧車2 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「くそっ…リオン…どこだ！」
    lian "可恶…里昂…你在哪里！"

    # nil 「戻ったら、リオンの姿はその場では見えなかった。」
    "回来后，在那里看不到里昂的身影"

    # 莲 「となれば…！」
    lian "那么…！"

    # nil 「俺は、列の横の階段を一気に駆け上る。」
    "我一口气跑上了队伍旁边的楼梯"

    # 莲 「…ビンゴ」
    lian "……Bingo"

    # nil 「リオンは、今まさに列の最前列に立っていた。俺が来ないのを不安げに、辺りを見渡している。」
    "里昂现在正站在队伍的最前列。不安地环视着周围，寻找着我"

    # 莲 「させるか！」
    lian "在这里啊！"

    # nil 「フェンスを飛び越して、リオンの隣に着地する。」
    "越过栅栏，在里昂的旁边着陆"

    # 莲 「ギリギリセェーフ！」
    lian "千钧一发！"

    # 里昂 「おそいよー！　何してたのさー！」
    show リオン_私服_基本_見下し at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0298.ogg"
    lion リオン_私服_基本_見下し "好慢哦——！你在干什么啊——！"

    # 莲 「いやーほら、これを…さ…」
    lian "呀，你看，这个……"

    # 里昂 「え…アイス…どうして？」
    show リオン_私服_基本_驚き_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0299.ogg"
    lion リオン_私服_基本_驚き_1 "诶…冰淇淋…为什么？"
    hide リオン_私服_基本_見下し

    # 莲 「こういうのはリオンは怒るか？　ほら、元はといえば、俺とリオンが仲良くなれたのは、アイスがきっかけだったからさ…記念に、とおもって！」
    lian "不知道这样的话里昂会生气吗？你看，原来我和里昂关系变好是因为以冰淇淋为契机……所以作为纪念！"

    # 里昂 「っ！　怒らないよ！　嬉しいなぁ！　本当は私のアイスを食べさせてあげたいけど…こういう計らい、粋で好きだよ！」
    show リオン_私服_基本_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0300.ogg"
    # lion リオン_私服_基本_嬉しい "呃！我不会生气的！好开心啊！我真的想让你吃我的冰淇淋……这样的安排，很漂亮，我很喜欢！"
    # lion リオン_私服_基本_嬉しい "呃！我不会生气的！好开心啊！我本来打算想让你吃我的冰淇淋……这样的安排，很漂亮，我很喜欢！"
    lion リオン_私服_基本_嬉しい "呃！我不会生气的！好开心啊！我本来就打算想让你吃我的冰淇淋……这样的安排，很漂亮，我很喜欢！"
    hide リオン_私服_基本_驚き_1

    # 莲 「喜んでくれたならよかった。ちなみに、リオンがいつも持ってる杖のアイスに似てる奴を選んでみたんだよ」
    lian "你要是高兴就好了。顺便一提，我给你选了和里昂平时拿着的拐杖冰淇淋相似的那个"

    # 里昂 「よ、よく見てるね…ちょっと、うるってきた…よ…」
    show リオン_私服_基本_ジト目_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0301.ogg"
    # lion リオン_私服_基本_ジト目_1 "看、看得真仔细啊……稍微，有点湿润了……"
    lion リオン_私服_基本_ジト目_1 "看、看得真仔细啊……稍微，眼睛有点湿润了……"
    hide リオン_私服_基本_嬉しい

    # 莲 「まぁほら、観覧車乗ろうぜ」
    lian "好了，我们上摩天轮吧"

    # 里昂 「うん！」
    show リオン_私服_基本_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0302.ogg"
    lion リオン_私服_基本_にっこり "嗯！"
    hide リオン_私服_基本_ジト目_1

    # nil 「リオンにはピンク色の方を私、観覧車に二人で乗り込んだ。」
    "我们两个人坐上了摩天轮"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「『観覧車に乗った以上はしっかり告白するんだぞ。女の子は期待するからな？　チキんじゃねーぞ男の子！』」
    voice "voice/想瑠/sol_a1_0091.ogg"
    liu 想瑠_スーツ_ニヤリ "『既然已经上了摩天轮，之后就要好好表白，因为女孩子会这样期待的，对吧？别胆怯，男孩！』"

    # 莲 「（もちろんだ。まぁせいぜい見てるんだな…）」
    lian "（当然了。嘛，老师你看好了…）"

    # 场景切换到摩天轮独间
    image bg rcg01_4_0 = "images/ev/rcg01_4_0.png"
    scene rcg01_4_0 with dissolve

    # BGM 停
    stop music fadeout 2.0

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「……」
    voice "voice/リオン/ron_a1_0303.ogg"
    lion リオン_私服_基本_にっこり "……"

    # 莲 「……」
    lian "……"

    # nil 「二人で、アイスクリームを舐めながらゆっくりと高度をあげていくゴンドラの中で、景色を眺める。」
    "两个人在一边舔冰淇淋一边慢慢提升高度的缆车中，眺望景色"

    # nil 「というか…単純に、気恥ずかしくて目を合わせづらい。」
    "也就是说…单纯地因为害羞而难以对视"

    # nil 「くそっ…チキってんじゃねぇ…いけよ俺！」
    "该死…我才不是胆小鬼！"

    # 里昂 「このアイス…美味しいね…」
    voice "voice/リオン/ron_a1_0304.ogg"
    lion リオン_私服_基本_微笑み "这个冰淇淋…很好吃呢…"

    # 莲 「あ、あ…」
    lian "啊，啊…"

    # nil 「はっきりいって、アイスの味なんて入ってこない。」
    "坦白说，冰淇淋的味道根本吃不出来"

    # nil 「いざ観覧車に二人きりとなると、こまで難易度高いとは…。」
    "真的只有两个人坐摩天轮的时候，难度竟然这么高……"

    # nil 「だが…」
    "但是…"

    # 里昂 「隣、いい？」
    voice "voice/リオン/ron_a1_0305.ogg"
    # lion リオン_私服_基本_嬉しい "旁边的，在吗？"
    lion リオン_私服_基本_嬉しい "坐在你身边，可以吗？"

    # 莲 「あ、ああ…」
    lian "啊，啊啊…"

    # nil 「しまったァー！　第一ラウンド敗北！」
    "糟了！第一回合败北！"

    # 里昂 「くすっ…じゃぁ、隣、失礼しまーす」
    voice "voice/リオン/ron_a1_0306.ogg"
    # lion リオン_私服_基本_微笑み "欸嘿…那，旁边的，失礼啦"
    lion リオン_私服_基本_微笑み "欸嘿…那，旁边的位置，失礼啦"

    # nil 「向かいの席から、リオンが立ち上がって、俺の隣に腰を下ろした。」
    "从对面的座位上，里昂站了起来，坐在我旁边"

    # 里昂 「よいしょー。向かい合わせは寂しいもんね」
    voice "voice/リオン/ron_a1_0307.ogg"
    lion リオン_私服_基本_嬉しい "好嘞。对面很寂寞呢"

    # 莲 「なぁ…リオン…」
    lian "呐……里昂"

    # 里昂 「んー？」
    voice "voice/リオン/ron_a1_0308.ogg"
    lion リオン_私服_基本_にっこり "嗯——？"

    # nil 「観覧車の駆動音と、町並みが織りなす多種多様の騒音、そしてゴンドラを煽る音が、耳の中に響き渡る。」
    "摩天轮的驱动声和街道交织而成的各种各样的噪音，还有煽动凤尾船的声音，在耳边回响"

    # nil 「しかしそんなアンビエントすらかき消すぐらいに、二つ分の鼓動の音が鼓膜を震わせた。」
    # "但是两个心跳的声音震动着耳膜，几乎盖过了背景的声音"
    "但是我们两人心跳的声音震动着耳膜，几乎盖过了背景的声音"

    # nil 「俺も、リオンも、緊張している。そんなことはわかっている。だがしかし、既にリオンに先手を打たせてしまった。」
    # "我和里昂都很紧张。我知道那件事。但是，已经让里昂先下手了"
    "我和里昂都很紧张。我知道那件事。但是，已经被里昂先下手了"

    # nil 「だからこれからは、俺が…！」
    "所以从现在开始，我要…！"

    # nil 「リオンの手をそっと握る。リオンは嫌がる素振りは見せない。」
    "轻轻握着里昂的手，里昂没有表现出讨厌的样子"

    # 莲 「今日はその…一日ありがとうな」
    # lian "今天是那个…一天谢谢了"
    lian "今天那个…今天一天谢谢了"

    # 里昂 「それは、こちらの台詞だよー？　素敵な一日をプレゼントしてくれてありがとう」
    voice "voice/リオン/ron_a1_0309.ogg"
    lion リオン_私服_基本_微笑み "这个啊，是我的台词哦？谢谢你给我这么棒的一天"

    # 莲 「いやこちらこそ…」
    lian "不，我才是……"

    # 莲 「……」
    lian "……"

    # 里昂 「くすっ」
    voice "voice/リオン/ron_a1_0310.ogg"
    lion リオン_私服_基本_嬉しい "嘿嘿"

    # 莲 「俺が、何を考えていたのかを…知りたい…よな…」
    lian "你想知道……我在想什么……对吗？"

    # nil 「俺はそうやって切り出した。」
    # "我是这样开口的"
    "我这样开口了"

    # nil 「早くも答えを聞くのが怖くて、心が痛む。」
    "我害怕早点听到答案而心痛"

    # 里昂 「んー…無理に聞こうとは思わないよ？だって、考えごとしてる時の蓮くん、ちょっと辛そうだった」
    voice "voice/リオン/ron_a1_0311.ogg"
    lion リオン_私服_基本_微笑み "嗯……我不想勉强问你啊？因为，在思考问题的时候，莲君看起来有点痛苦"

    # nil 「リオンは、俺の手をゆっくりとまるで頭にするように撫でてくれる。」
    # "里昂慢慢地抚摸着我的手，就像把手放在头上一样"
    "里昂慢慢地抚摸着我的手，就像是在轻轻抚摸我的脑袋一般"

    # 里昂 「でも、もし、私に話して、それで君の苦しみが和らぐなら…聞かせて欲しいな」
    voice "voice/リオン/ron_a1_0312.ogg"
    lion リオン_私服_基本_嬉しい "但是，如果你告诉我，然后你的痛苦就会缓和下来的话…我希望你能告诉我"

    # 莲 「リオンの事なんだ」
    # lian "是里昂的事"
    lian "是关于里昂你的事"

    # 里昂 「っ…！　私…の？　…い、いや…とぼけるのもアレだよね。う、うん…どうしたの？　私の何を悩んでたの？」
    voice "voice/リオン/ron_a1_0313.ogg"
    lion リオン_私服_基本_無表情_1 "呃…！我…的？…不，不是……装傻也是那个吧。嗯、嗯…怎么了？你在烦恼我的什么？"

    # nil 「リオンは、俺の気持ちを察してくれたようだった。」
    "里昂似乎察觉到了我的心情"

    # nil 「言葉にするのは怖かった。けど、俺の気持ちは決まっている。」
    "我害怕说出来，但我心意已决"

    # 莲 「リオンはさ…いつまで、日本に居るのかなって…」
    # lian "里昂…到底在日本待到什么时候呢……"
    lian "里昂…到底会在日本待到什么时候呢……"

    # 里昂 「へ…？　ど、どうして…？」
    voice "voice/リオン/ron_a1_0314.ogg"
    lion リオン_私服_基本_驚き_1 "欸？为、为什么？"

    # 莲 「だって、リオンは外国人だし…アイス屋になるために日本に来たといっても…ずっといるとは限らないじゃん」
    lian "因为，里昂是外国人……虽说是为了开冰激凌店才来日本的……但也不一定一直都在啊"

    # 里昂 「あ、そうじゃなくて、どうして、私が日本に居る期間を知りたいの？」
    voice "voice/リオン/ron_a1_0315.ogg"
    # lion リオン_私服_基本_微笑み "啊，不是那样的，为什么想知道我在日本的时间？"
    lion リオン_私服_基本_微笑み "啊，不是那样的，为什么想知道我在日本停留的时间？"

    # 莲 「それは…」
    # lian "那是……"
    lian "那是因为……"

    # nil 「リオンは核心を突くコメントに、俺は言葉を詰まらせる。」
    "对于里昂直击核心的问题，我语塞了"

    # nil 「その様子を見て、リオンは申し訳なさそうな表情を浮かべた。」
    "看到那个样子的我，里昂露出了抱歉的表情"

    # 里昂 「…ごめん、今のは卑怯だったね」
    voice "voice/リオン/ron_a1_0316.ogg"
    # lion リオン_私服_基本_ジト目 "…对不起，刚才那是卑鄙啊"
    lion リオン_私服_基本_ジト目 "…抱歉，刚刚的说法有点卑鄙呢"

    # 里昂 「でも…できれば、君の口から聞かせて欲しい」
    voice "voice/リオン/ron_a1_0317.ogg"
    lion リオン_私服_基本_にっこり "但是…如果可以的话，我希望你亲口告诉我"

    # nil 「リオンは、俺の手をぎゅっと握る。」
    "里昂紧紧握着我的手"

    # nil 「きっとリオンなりの事情があるんだろう。」
    "一定有里昂的原因吧"

    # nil 「俺は…どんな事情でも、受け止めると、覚悟したはずだ。」
    "我…不管遇到什么事情，我都会接受的，已经做好了心理准备"

    # nil 「それを見せてみろ！」
    "让我看看觉悟到了什么地步吧！"

    # 莲 「リオンの事が…好き…なんだ」
    lian "我……喜欢……里昂……"

    # 里昂 「…っ！」
    voice "voice/リオン/ron_a1_0318.ogg"
    lion リオン_私服_基本_驚き_1 "……！"

    # 表情差分：泪珠打转
    image bg rcg01_4_1 = "images/ev/rcg01_4_1.png"
    scene rcg01_4_1 with dissolve

    # nil 「俺の覚悟はなんとか、その言葉を紡ぎ出した。リオンは言葉を発しなかったが、その代わりに、大粒の涙をその赤色の瞳から零れ出させた。」
    # "我的觉悟总算是编织出了那句话。里昂没有说话，取而代之的是，大颗的眼泪从那红色的眼睛里流了出来"
    "我的觉悟总算是编织出了那句话。里昂没有说话，取而代之的是，大颗的泪珠从那红瞳的眼睛里流了出来"

    # nil 「今のがきっかけとなったのか、俺の口からは面白いように言葉が流れ出していく。」
    "也许是因为现在的契机吧，我的话像小溪一样从我口中流淌而出"

    # 莲 「まだ、会って一週間ぐらいしか経ってないけど、リオンの事が好きになっちまった」
    lian "虽然见面才一周左右，但是我还是喜欢上了里昂"

    # 莲 「アイス屋を真剣に目指す姿勢もそうだし、今日みたいに甘えん坊な所も可愛いと思う」
    lian "认真的以冰淇淋店为目标的姿态也是，像今天这样撒娇的地方也很可爱"

    # 莲 「まだ…俺はリオンの住んでる家も知らないし、過去も知らないけど…それでも、俺はリオンとずっと一緒に居たいって、そう思ったんだ」
    lian "我还……我不知道里昂住的家，也不知道你的过去…但是，我还是想和里昂一直在一起"

    # 莲 「リオンが嬉しそうにしているだけで、どんどん好きになっていく反面、リオンがいつか日本から離れてしまう事が怖かった…」
    lian "光是看着里昂起来高兴的样子，就渐渐喜欢上了，但另一方面，我害怕里昂总有一天会离开日本…"

    # 莲 「だから…いつまで日本に居るのかを教えて欲しいんだ…。出来れば俺は…ずっと一緒に居たい」
    lian "所以…希望你能告诉我你在日本待到什么时候……如果可以的话，我……想一直在一起"

    # nil 「付き合ってくれ。とは言わなかった。別に付き合えなくてもい。せめて一緒に居たい。」
    # "请和我交往”这样的话，我没有说，不必特别交往，但是至少想呆在一起"
    "“请和我交往”这样的话，我没有说，不必特别强调交往，但是至少想待在一起"

    # 里昂 「…私は…」
    voice "voice/リオン/ron_a1_0319.ogg"
    lion リオン_私服_基本_悲しい2 "…我……"

    # nil 「リオンは大粒の涙を流しながら、言葉を詰まらせた。」
    "里昂流着大颗的眼泪，哽咽着"

    # nil 「その涙の色を、俺はわからなかった。」
    # "我不知道那眼泪的颜色"
    "我不知道那眼泪代表的"

    # nil 「嬉しさなのか、それとも、悲しさなのか。」
    # "是高兴呢，还是悲伤呢"
    "是高兴，还是悲伤呢"

    # nil 「それともその両方なのか…。」
    "还是两者兼而有之……"

    # 里昂 「…私は…嘘つき…だよ…」
    voice "voice/リオン/ron_a1_0320.ogg"
    lion リオン_私服_基本_悲しい "…我…是个骗子……"

    # 莲 「何…？」
    lian "什么……？"

    # nil 「リオンが吐き出した言葉は、ＹＥＳでもＮＯでもない、まったく別の言葉だった。」
    "里昂说的话既不是YES也不是NO，而完全是别的话"

    # 里昂 「私も…蓮くんの事が好き…。でも、でも…この好きって気持ちは…君とは違う…」
    voice "voice/リオン/ron_a1_0321.ogg"
    lion リオン_私服_基本_悲しい "我也……喜欢莲君…但是……这种喜欢的心情…和你不一样……"

    # 莲 「友達としてって…事…？」
    lian "作为朋友…的…？"

    # 里昂 「違う！！　違うよ！！　それは違う！！」
    voice "voice/リオン/ron_a1_0322.ogg"
    lion リオン_私服_基本_驚き "不是的！！不对！！那不对！！"

    # 里昂 「私だって！　蓮くんとずっと一緒に居たいって！　そう思ってるから！」
    voice "voice/リオン/ron_a1_0323.ogg"
    lion リオン_私服_基本_微笑み "我也是！想一直和莲君在一起！我是这么想的！"

    # nil 「リオンはさらに涙の量を増やし、ゴンドラの中で叫んだ。リオンの気持ちは、俺と同じだと聞いて、安心感が広がる。」
    "里昂哭得更厉害了，在缆车里大喊。听到里昂的心情和我一样，安心感就扩大了"

    # nil 「しかし、やはり、その背後にある可能性に恐怖する。」
    # "但是，果然还是害怕背后的可能性"
    "但是，果然还是害怕在那背后的可能性"

    # nil 「だが…俺は…！　」
    "但是…我…！　"

    # 里昂 「でも…でも…！」
    voice "voice/リオン/ron_a1_0324.ogg"
    lion リオン_私服_基本_悲しい2 "但是…但是…！"

    # 莲 「リオン！」
    lian "里昂！"

    # 里昂 「っ！」
    voice "voice/リオン/ron_a1_0325.ogg"
    lion リオン_私服_基本_驚き "啊！"

    # nil 「俺はリオンの手を強く握る。」
    "我用力握住里昂的手"

    # 莲 「教えてくれ。お前が抱えてる物を。どんなに辛い事でも、俺は受け止めるし。
    lian "告诉我吧。你背负的东西。无论是多么痛苦的事，我都会接受"

    # 莲 「だからといって、お前への気持ちは変わらないだろう」
    lian "但是无论如何，我不会改变对你的感情"

    # 莲 「いや、絶対に変えない」
    lian "不，我是绝对不会改变的"

    # 莲 「だから、教えてくれ、リオン」
    lian "所以，请告诉我，里昂"

    # 里昂 「…君の…となりの席…ずっと、空いてるよね…？」
    voice "voice/リオン/ron_a1_0326.ogg"
    lion リオン_私服_基本_悲しい "……你的…旁边的座位…一直空着吧…？"

    # 莲 「…？　リオンが何故それを…？」
    lian "…？里昂为什么要…？"

    # nil 「リオンが発した言葉は、さらに俺の予想外だった。俺の隣の席？　それがどうした？」
    "里昂说的话，更让我意料之外。我旁边的座位？那是怎么回事？"

    # 里昂 「…となりに誰が座ってたか、覚えてる？」
    voice "voice/リオン/ron_a1_0327.ogg"
    lion リオン_私服_基本_悲しい "……还记得旁边坐着谁吗？"

    # 莲 「いや…それが思い出せないんだよ…記憶がすっぽり抜け落ちてる感じで…」
    # lian "不，我想不起来那个……感觉记忆完全脱落了……"
    lian "不，我想不起来……感觉关于这个的记忆完全是空白的……"

    # nil 「思いだそうにも、頭がそれを拒否する。」
    # "虽然似乎回想起来了，但是脑子里还是拒绝了"
    "虽然似乎回想起来了什么，但是脑袋里还是拒绝了进一步的回想"

    # 莲 「それが…どうしたんだ…」
    lian "那个…怎么了……"

    # 里昂 「…こから先を話してしまうと…君は…この世界に居られなくなってしまうかもしれない…」
    voice "voice/リオン/ron_a1_0328.ogg"
    # lion リオン_私服_基本_悲しい "……如果再往下说的话……你…可能无法再在这个世界上呆下去……"
    # lion リオン_私服_基本_悲しい "……如果再往下说的话……你…可能无法再在这个世界上待下去……"
    # lion リオン_私服_基本_悲しい "……如果再往下说的话……你…可能无法再在这个世界上待下去……"@@
    lion リオン_私服_基本_悲しい "……如果再往下说的话……你…可能就不能继续存在于这个世界上了……"


    # 莲 「…そんな、規模のデカい話なのか…？」
    lian "……是那么大规模的事情吗…？"

    # nil 「だから、あの担任が本気で脅しにきたのか。そして今もどこかで俺達を監視している。」
    "所以，那个班主任是真的来威胁我的吗。而且现在也在某处监视着我们"

    # nil 「なるほど合点がいった。」
    "原来如此，我明白了"

    # nil 「この世界には何かある。」
    # "这个世界是怎么回事"
    "这个世界有什么问题"

    # 里昂 「もし…こから先を知ってしまって、蓮くんの心が壊れてしまったりしたら…そう考えて、ずっと話せなかった…話せないま、こまできてしまった…」
    voice "voice/リオン/ron_a1_0329.ogg"
    # lion リオン_私服_基本_悲しい "如果…在这里知道了，莲的心就坏了的话……这样想着，一直不能说话…不能说话，就走到这一步了……"
    lion リオン_私服_基本_悲しい "如果…提前在这里知道了，莲的内心就崩溃了的话……这样想着，就一直不能说话…不能说话，就走到这一步了……"

    # 里昂 「そして…”もう一度”君の事を好きになってしまった」
    voice "voice/リオン/ron_a1_0330.ogg"
    lion リオン_私服_基本_悲しい "然后…“再一次”喜欢上了你"

    # 里昂 「だから…」
    voice "voice/リオン/ron_a1_0331.ogg"
    lion リオン_私服_基本_にっこり "所以…"

    # 莲 「リオン…逆に聞くが…もしこから先を聞いて、世界が変わってしまっても…その先に、リオンは居るのか？」
    lian "里昂…反过来问你…如果从这里开始，世界发生了变化…在那之时，里昂还会在吗？"

    # 里昂 「…それは…約束するよ」
    voice "voice/リオン/ron_a1_0332.ogg"
    lion リオン_私服_基本_微笑み "…这点…我保证"

    # 莲 「なら何も問題ない。さぁ、教えてくれ。お前が抱える物を」
    lian "那就没问题了。来，告诉我吧。你背负的东西"

    # 里昂 「…わかった、信じられないかもしれないけど、今から話す事は、全部本当の事だから、聞いて欲しい」
    voice "voice/リオン/ron_a1_0333.ogg"
    lion リオン_私服_基本_にっこり "我知道了，也许你不相信，但我要告诉你的都是真的，希望你能听我说"

    # nil 「リオンは俺の手を強く握る。」
    "里昂紧握着我的手"

    # nil 「その瞬間、まるで何かの波動が、身体を突き抜けた。」
    "那个瞬间，好像有什么波动穿透了身体"

    # 世界变成黑白！
    image bg rcg01t_4_1 = "images/ev/rcg01t_4_1.png"
    scene rcg01t_4_1 with dissolve

    # nil 「滴ったアイスの滴が空中で停止する。」
    # "冰淇淋滴下的冰滴在空中停止"
    "冰淇淋融化的滴落停止在了半空中"

    # nil 「それだけじゃない。全ての音が泊まって、俺たちの呼吸音と鼓動だけがゴンドラの中で木霊する。」
    # "不仅如此，所有的声音都停留在那里，只有我们的呼吸声和心跳声在缆车里回响"
    "不仅如此，所有的声音都停了下来，只有我们的呼吸声和心跳声在缆车里回响"

    # nil 「まさか…」
    "难道…"

    # 莲 「時間が…止まった…？」
    lian "时间…停止了…？"

    # 开场 BGM 起！
    play music bgmeight fadein 2.0

    # 里昂 「この世界には、魔法というものが存在するんだよ。今、私と蓮くん以外の時間を止めた。正確には、通常の時間の流れから、私と蓮くんを除外した…かな」
    voice "voice/リオン/ron_a1_0334.ogg"
    # lion リオン_私服_基本_微笑み "这个世界上存在着魔法。现在，我和莲君以外的时间都停止了。正确地说，是从通常的时间流中，把我和莲君除外了"
    lion リオン_私服_基本_微笑み "这个世界上存在着魔法。现在，我和莲君以外的时间都停止了。正确地说，是从正常的时间流中，把我和莲君除外了"

    # 莲 「おいおいまじかよ。それってすげぇ事じゃねぇのか…？」
    lian "喂喂，真的吗？那不是很了不起的事情吗…？"

    # 里昂 「うん。私、リオン＝マクスウェルはこの世界の魔法使いの中でもトップクラスの力を持つ『マクスウェル家』の一人娘なんだ」
    voice "voice/リオン/ron_a1_0335.ogg"
    lion リオン_私服_基本_嬉しい "嗯。我，里昂·麦克斯韦是这个世界上魔法使中拥有顶级力量的『麦克斯韦家』的独生女"

    # 里昂 「基本的に、私達の世界と蓮くん達の世界は交わらないルールが暗黙の了解になってるんだけど…私は、どうしてもこっちの世界に興味が沸いて…」
    voice "voice/リオン/ron_a1_0336.ogg"
    # lion リオン_私服_基本_悲しい2 "基本上，我们的世界和莲君你们的世界是不相交是默认的规则…但是，我无论如何都对这个世界产生了兴趣…"
    lion リオン_私服_基本_悲しい2 "基本上，我们的世界和莲君你们的世界永不相交是默认的规则…但是，我无论如何都对这个世界抱有着兴趣…"

    # 里昂 「それで、君の担任の先生…の双子のお姉さんも魔法使いなんだけど、お願いして、君達のクラスに留学させてもらったんだよ」
    voice "voice/リオン/ron_a1_0337.ogg"
    lion リオン_私服_基本_微笑み "因此，你的班主任老师……的双胞胎姐姐也是魔法师，所以我拜托她，让我去你们班留学了"

    # 里昂 「そして…その時となりの席だったのが…葛城蓮くん。君だ」
    voice "voice/リオン/ron_a1_0338.ogg"
    lion リオン_私服_基本_にっこり "然后……当时坐在我旁边的就是……葛城莲，就是你"

    # nil 「頭の中の、抜け落ちたピースがハメ込まれていくようだった。その時の様子を思い出す事はできなかったが…。」
    # "脑袋里掉下来的那块碎片好像被人紧紧抓住了一样，虽然没能想起那时的样子…"
    "记忆中掉下来的那块碎片好像被人紧紧抓住了一样，虽然没能想起那时的样子…"

    # 里昂 「勿論、真冬ちゃんと心愛ちゃんの事も知ってるよ。二人と仲良しな事もね。だって、私は君とあの二人に沢山遊んでもらったからね…」
    voice "voice/リオン/ron_a1_0339.ogg"
    lion リオン_私服_基本_にっこり "当然，我也知道真冬酱和心爱酱的事，也知道你和两个人关系很好，因为我和你还有那两个人玩了很多……"

    # 里昂 「それを君らが覚えていないのは、君達の記憶を『封印』したから。それが出来るかどうかは、これをご覧頂いてる通りだけど…」
    voice "voice/リオン/ron_a1_0340.ogg"
    # lion リオン_私服_基本_にっこり "你们之所以不记得这些，是因为你们的记忆被『封印』了。能不能做到这点，正如你所看到的那样……"
    lion リオン_私服_基本_にっこり "你们之所以不记得这些，是因为你们的记忆被『封印』了。至于能不能做到这点，正如你现在所看到的那样……"

    # 莲 「あ、別に疑っちゃいないさ。続けてくれ」
    lian "啊，我没有怀疑，请继续说"

    # nil 「リオンに感じていた既視感の正体が、今ならわかる気がする。」
    # "我觉得我现在知道了我对里昂的感觉——既视感的真面目"
    "我觉得我现在知道了我对里昂的那种感觉——既视感的真面目"

    image bg rcg01t_1_2 = "images/ev/rcg01t_1_2.png"
    scene rcg01t_1_2 with dissolve

    # 里昂 「勿論、真冬ちゃんと心愛ちゃんの事も知ってるよ。二人と仲良しな事もね。だって、私は君とあの二人に沢山遊んでもらったからね…」
    voice "voice/リオン/ron_a1_0341.ogg"
    lion リオン_私服_基本_悲しい2 "其实是不应该的事情…那个时候，我爱上了你"

    # 里昂 「でも、留学の期間は決まっていたし、その恋は実らない事は覚悟していたよ。それに、その時の蓮くんには、真冬ちゃんと心愛ちゃんがいたからね」
    voice "voice/リオン/ron_a1_0342.ogg"
    lion リオン_私服_基本_悲しい2 "但是，留学的时间已经定下来了，我已经做好了这份恋爱不会有结果的觉悟。而且，那个时候的莲君身边，还有真冬酱和心爱酱呢"

    # 莲 「二人の気持ちはわかっていた…ということか？」
    lian "知道那两人的心情…是这样吗？"

    # 里昂 「卑怯だとは思ったけど。私の恋が実らないなら、せめて、君達を幸せにしてあげたいと…そう強く思ったんだ」
    voice "voice/リオン/ron_a1_0343.ogg"
    # lion リオン_私服_基本_悲しい2 "我知道这样做很卑鄙，但我坚信，如果我的爱情没有结果，至少我会让你们幸福……"
    lion リオン_私服_基本_悲しい2 "我知道这样做也许很卑鄙，但我一直坚信着，如果我们的爱情不会有结果，至少我想尽力让你们能够获得幸福……"

    # 里昂 「そして、私は帰国後…君らを幸せに…君らを結ばせるためにはどうしたらいかと考えた」
    voice "voice/リオン/ron_a1_0344.ogg"
    # lion リオン_私服_基本_にっこり "然后，我回国后……为了让你们幸福……我想怎么做才好，这样的思考了"
    lion リオン_私服_基本_にっこり "然后，我回国后……为了让你们能够幸福……该怎么做才好，就开始这样的思考了"

    # 莲 「その結果が…ラブポーション・シクスティナイン…か」
    lian "那个结果就是……LOVEPOTION・SIXTYNINE…吗？"

    # 里昂 「その通り。流石、私が好きになった蓮くんだ」
    voice "voice/リオン/ron_a1_0345.ogg"
    lion リオン_私服_基本_にっこり "没错。不愧是我喜欢的莲君啊"

    # nil 「リオンの話と同時に俺の中でも話がまとまっていく。」
    # "在里昂谈论这个问题的同时，我也在接受这个事实"
    "在里昂谈论这个问题的同时，我也在逐渐接受这个事实"

    # nil 「隔絶された時間の中で、手から伝わってくるリオンの体温をしかと感じていた。」
    # "在与世隔绝的时间里，真切地感受到了从手传来的里昂的体温"
    "在与世隔绝的这段时间里，真切地感受到了从手中传来的里昂的体温"

    # 里昂 「元々アイスは大好きで…魔法のアイス屋になりたいっていう夢は元からあったんだけど…これと、君らへの”恩返し”を両立できないかと考えたんだ」
    voice "voice/リオン/ron_a1_0346.ogg"
    # lion リオン_私服_基本_微笑み "我本来就很喜欢冰淇淋……我本来就有想开一间魔法冰淇淋店的梦想……但是我想，这和对你们的“报恩”是不能两立的"
    lion リオン_私服_基本_微笑み "我本来就很喜欢冰淇淋……从一开始就有着想开一间魔法冰淇淋店的梦想……但是我想，这和对你们的“报恩”是不能归为一谈的"

    # 里昂 「君達を結ぶ事で、私の恋もスッキリ終わりがつくとも思ってたしね。だから、私は、あの”恋が叶う魔法のアイス”を開発した…結構大変だったけど」
    voice "voice/リオン/ron_a1_0347.ogg"
    # lion リオン_私服_基本_嬉しい "我还以为只要把你们结合在一起，我的爱情就会顺利结束。所以，我开发了那个能实现恋爱的魔法冰淇淋…虽然很辛苦"
    lion リオン_私服_基本_嬉しい "我还以为只要让你们结合在一起，我的爱情就会顺利结束。所以，我开发了那个能实现恋爱的魔法冰淇淋…虽然很辛苦"

    # 里昂 「そして、その話をパにしたらめちゃくちゃ怒られて…まぁ、当たり前だよね。小娘一人の恋で、世界の理をねじ曲げようなんざ…」
    voice "voice/リオン/ron_a1_0348.ogg"
    # lion リオン_私服_基本_嬉しい "我还以为只要把你们结合在一起，我的爱情就会顺利结束。所以，我开发了那个能实现恋爱的魔法冰淇淋…虽然很辛苦"
    lion リオン_私服_基本_微笑み "然后，我把这件事告诉了爸爸，他非常生气……啊，这是理所当然的啊，因为一个小女孩的恋情，竟然就想歪曲世界的规律什么的……"

    # nil 「リオンは皮肉に微笑んだ。」
    # "里昂带着讽刺的微笑"
    "里昂有些讽刺的笑着"

    # 里昂 「でも、マはこっそり応援してくれて…後でパと喧嘩したらしいけど。結局、私は家を追い出されちゃったけど『愛する人一人を幸せに出来ないで、何が魔法だ。お前の出した答えが正しいかどうか確かめてこい』って、日本に来る事は許可してくれたんだ」
    voice "voice/リオン/ron_a1_0349.ogg"
    # lion リオン_私服_基本_嬉しい "但是，妈妈悄悄地为我加油……之后好像和爸爸吵架了。结果，我被赶出了家门，她说『如果不能让我爱的人幸福，那魔法是什么呢。你给出的答案是不是正确的，你亲自来确认一下』，就这样，她允许我来日本了"
    lion リオン_私服_基本_嬉しい "但是，妈妈悄悄地为我加油……之后好像和爸爸吵架了。结果，我被赶出了家门，她说『如果不能让所爱的人幸福，那还叫什么魔法。你所坚持答案的正确与否，就由你亲自去确认一下吧』，就这样，她允许我来日本了"

    # 里昂 「あとは、想瑠にゃんの友達が日本でお店をやってるらしく…その人と『本当に人の恋を叶えさせる力があるなら、店を貸してもい』という契約というか、約束をして…蓮くんに、もう一度出会ったんだ」
    voice "voice/リオン/ron_a1_0350.ogg"
    # lion リオン_私服_基本_微笑み "还有，想瑠喵的朋友好像在日本开了一家店……和那个人订了一个契约，说是『如果真的有能实现别人的恋爱的力量的话，就把店借给我吧』，就这样约定好了…再一次和莲君相遇了"
    lion リオン_私服_基本_微笑み "还有，想瑠喵的朋友好像在日本开了一家店……我和那个人签订了一个契约，说是『如果我真的有能够实现恋爱的力量的话，就把你的店借给我卖冰淇淋吧』，就这样约定好了…于是再一次和莲君相遇了"

    # 莲 「だが。その開発したアイスを俺に食わせる予定が、俺に食わされてしまい、計画が狂った…ということか」
    # lian "但是，计划开发出来让我吃的那个冰淇淋，结果被我让你吃了……计划打乱了"
    lian "但是，计划开发出来让我吃的那个冰淇淋，结果被我让你吃了……计划被打乱了"

    # 里昂 「そう。だから、私は食べる時に躊躇ったんだよね…。勿論、他の理由もあるけど…」
    voice "voice/リオン/ron_a1_0351.ogg"
    lion リオン_私服_基本_ジト目_1 "是的。所以我在吃的时候犹豫了一下……当然，也有其他理由……"

    # 莲 「他の理由…？」
    lian "其他的理由…？"

    # 里昂表情改变
    image bg = "images/ev/rcg01t_2_1.png"
    scene rcg01t_2_1 with dissolve

    # 里昂 「そ…それは…ちょっと今話すのは恥ずかしいから…後で良い…？」
    voice "voice/リオン/ron_a1_0352.ogg"
    lion リオン_私服_基本_ジト目_1 "那…那是……现在说这个有点不好意思…可以等以后吗…？"

    # nil 「一瞬だけ、リオンは、先ほどデートしていた普通の女の子に戻った。淡々と事情を話すリオンには面食らったが、やはり、リオンはリオンだった。」
    "有那么一瞬间，里昂变回了刚才约会的普通女孩。我对于淡然地讲述事情的里昂突然感到不知所措，但里昂果然还是里昂"

    # 莲 「あ、後でいよ」
    lian "啊，之后吧"

    # 里昂表情改变
    image bg = "images/ev/rcg01t_1_1.png"
    scene rcg01t_1_1 with dissolve

    # 里昂 「ありがとう…。でね。本当はあの場で、蓮くんにアイスを渡して立ち去る予定だったんだけど…」
    voice "voice/リオン/ron_a1_0353.ogg"
    lion リオン_私服_基本_微笑み_1 "谢谢啦……然后呢。我本来打算当场把冰淇淋交给莲君然后离开的……"

    # 莲 「俺に…誘われちまって、断れなかった」
    lian "被我…那样邀请了，没能拒绝"

    # 里昂 「そう。結局さ、そこから、君への気持ちが熱を持っちゃったんだよね…。だから、嬉しくて…」
    voice "voice/リオン/ron_a1_0354.ogg"
    # lion リオン_私服_基本_悲しい2_1 "是的。结果呢，从那以后，对你的感情就发烧了呢…。所以，很开心……"
    lion リオン_私服_基本_悲しい2_1 "是的。结果呢，从那以后，对你的感情就一发不可收拾了呢…。所以，很开心……"

    # 莲 「そのま、流されるように俺と一緒に時を過ごしてしまった…」
    # lian "就这样，我和你一起度过了时光…"
    lian "就这样，我和你一起度过了那段时光…"

    # 里昂 「うん…だって…だって…一度は諦めてた恋なのに…大好きな人と、こんなに近くに過ごせるなんて…例え、嘘をついていたとしても、やっぱり幸せだよ」
    voice "voice/リオン/ron_a1_0355.ogg"
    # lion リオン_私服_基本_微笑み "嗯…可是…因为…明明已经放弃了一次的恋爱……竟然能和最喜欢的人在这么近的地方度过……即使是说谎，也还是很幸福的啊"
    lion リオン_私服_基本_微笑み "嗯…可是…因为…明明已经放弃了一次的恋爱……竟然还能和最喜欢的人在这么近的地方待在一起……即使是说谎，果然也还是很幸福的啊"

    # 莲 「まぁ、リオンは普通の甘えん坊な女の子だもんな」
    lian "嗯，里昂只是个普通的爱撒娇的女孩子"

    # 里昂 「う…ちょっと、自分でも恥ずかしいなって思ってるけど…甘え癖あるよね…」
    voice "voice/リオン/ron_a1_0356.ogg"
    lion リオン_私服_基本_悲しい2_1 "嗯……虽然我自己也觉得不好意思…但是有爱撒娇的习惯呢…"

    # 莲 「そこが可愛いんだろ」
    # lian "那里很可爱吧"
    lian "这样很可爱吧"

    # 里昂 「はぅ…はぁ、はぁ…ん…だめ、ドキドキしちゃう…もうちょっとだけ…」
    voice "voice/リオン/ron_a1_0357.ogg"
    lion リオン_私服_基本_悲しい2_1 "哈…哈呜，哈…嗯…不行，dokidoki的…再稍微……"

    # 里昂 「えと…それで、トドメになったのは…心愛ちゃんと真冬ちゃんが付き合った事かな…これは完全に読めてなかった」
    voice "voice/リオン/ron_a1_0358.ogg"
    # lion リオン_私服_基本_微笑み "那个…然后，最糟糕的是……大概是心爱酱和真冬酱交往的事情…这个完全没能读出来"
    lion リオン_私服_基本_微笑み "那个…然后，最糟糕的是……大概是心爱酱和真冬酱交往的事情…这个完全没能预料到"

    # 莲 「つまり、この時点で、俺とあいつらを結ぶ必要性が失われた…か」
    lian "也就是说，在这个时候，我和她们之间的联系失去了必要性…吗？"

    # 里昂 「そう。そうなると…もう、君への気持ちがあふれ出しちゃって…そのタイミングでデートにも誘うし…はぁ、はぁ…」
    voice "voice/リオン/ron_a1_0359.ogg"
    lion リオン_私服_基本_悲しい2_1 "是的。这样的话……对你的感情已经满溢出来了…这个时候被你邀请去约会…哈，哈…"

    # 莲 「大丈夫か…？」
    lian "没事吧…？"

    # 里昂 「う、うん…それで…今日はもう、なんか、ずっと変な感じになっちゃって…私、もう、蓮くんと恋してもいのかな…って…」
    voice "voice/リオン/ron_a1_0360.ogg"
    lion リオン_私服_基本_悲しい2_1 "嗯，嗯…然后……今天已经，总觉得，一直有种很奇怪的感觉…我想，已经可以和莲君恋爱了吧…"

    # nil 「リオンがまた涙を流しはじめた。」
    "里昂又开始流泪了"

    # 里昂表情改变
    image bg = "images/ev/rcg01t_4_2"
    scene rcg01t_4_2 with dissolve

    # 里昂 「ねぇ…蓮くん…こんな私でも…本当に、好き…でいてくれる…？」
    voice "voice/リオン/ron_a1_0361.ogg"
    lion リオン_私服_基本_悲しい2_1 "呐…莲君…即使是这样的我……也真的，能喜欢我吗…？"

    # 莲 「そんなん、聞くまでもないだろ…思ったより理解できる領域で、ほっとしている」
    lian "没必要问吧…是比我想象中更能理解的领域啊，松了一口气"

    # 里昂 「…！　だ、だってだって！　私、人間じゃないんだよ！？　君達の過去だって変えてるし…！」
    voice "voice/リオン/ron_a1_0362.ogg"
    lion リオン_私服_基本_驚き_1 "……！可、可是！我不是人类！？我改变了你们的过去…！"

    # 莲 「もう、俺の記憶を消す事はないのか？」
    lian "你不会再抹去我的记忆了吧？"

    # 里昂 「う、うん。こまで話しちゃったら、例え蓮くんにフラれても、消す事はないよ」
    voice "voice/リオン/ron_a1_0363.ogg"
    lion リオン_私服_基本_悲しい2_1 "嗯、嗯。这个的话，即使莲君甩了我，我也不会抹去的"

    # 莲 「じゃぁ、何も心配いらねぇだろ。人間じゃねぇつったら…心愛なんてどうやって説明すんだよ。あいつWi-fiの電波飛んでるんだぞ、身体から。転ぶとラジオ流れるし」
    # L:正确的写法是Wi-Fi 参考：https://zh.wikipedia.org/wiki/Wi-Fi
    # lian "那就没什么好担心的了。如果你不是人类的话……那可以麻烦你说明一下心爱的事情吗，那孩子可以发射Wi-Fi信号，从她的身体里面。摔倒的时候收音机会播放"
    lian "那就没什么好担心的了。如果你不是人类的话……那可以麻烦你说明一下心爱的事情吗，那孩子可以发射Wi-Fi信号，从她的身体里面。摔倒的时候收音机也会开始播放"

    # 里昂 「心愛ちゃんは…実は、無自覚な魔法使いなんだ…たまにそういう才能を持って生まれてくる人がいる…両親は普通の人だけど」
    voice "voice/リオン/ron_a1_0364.ogg"
    # lion リオン_私服_基本_嬉しい "心爱酱的话……其实是一个没有自觉的魔法使…偶尔会有人拥有这种才能……虽然父母只是普通人"
    lion リオン_私服_基本_嬉しい "心爱酱的话……其实是一个还没有自我认知到的魔法使…偶尔会有人拥有这种才能……虽然父母只是普通人"

    # 莲 「思う存分悪用してる感じもあるけどな…あいつお菓子食べ放題じゃん」
    # lian "虽然也有种在尽情滥用的感觉…那家伙不是随便吃点心吗？"
    lian "虽然也有种在尽情滥用的感觉…那家伙不是能随便吃点心吗？"

    # 里昂 「あれは、食べたお菓子を身体の中で再生成してもう一度生み出してるんだよ」
    voice "voice/リオン/ron_a1_0365.ogg"
    # lion リオン_私服_基本_微笑み_1 "那是把吃过的点心在身体里再生成，然后再生产出来的"
    lion リオン_私服_基本_微笑み_1 "那是把吃过的点心在身体里再生成，然后再创造出来的"

    # 莲 「んーと、それは君ら側としては管理したほうがいんじゃないのか？」
    # lian "嗯，那个作为你们方面不是应该管理吗？"
    lian "嗯，这种事件不是更应该由你们那方面管理吗？"

    # 里昂 「んー。あの子は性格が凄く優しいしね。私と蓮くんが出会ったあの日、心愛ちゃんは蓮くんの家にたどり着く前に、電車の脱線事故を防いで、トラックの事故から子供を助けてるんだよ」
    voice "voice/リオン/ron_a1_0366.ogg"
    lion リオン_私服_基本_にっこり_1 "嗯——那个孩子性格很温柔呢。我和莲君相遇的那天，心爱酱就在到达莲君家之前，阻止了电车脱轨事故，在卡车事故中救了孩子"

    # 莲 「…なんだ、すげぇな心愛。今度褒めてやるか」
    lian "…什么啊，好厉害啊心爱。下次要表扬她啊"

    # 里昂 「だから、あの子は無害だって事でデータベースには登録されてるよ」
    voice "voice/リオン/ron_a1_0367.ogg"
    lion リオン_私服_基本_微笑み_1 "所以说，那个孩子是无害的，所以在数据库里那样录入了"

    # 莲 「なんかありがとう。日頃の疑問が一つ解決した。ていうか、他の女の話してごめんな？」
    # lian "这样啊，谢谢。平时的疑问解决了一个。话说回来，提到了其它女人对不起啊？"
    lian "这样啊，谢谢。平时的疑问解决了一个。话说回来，提到了其它女孩对不起啊？"
    # lian "这么说呢，谢谢。平时的疑问解决了一个。话说回来，提到了其它女人对不起啊？"

    # 里昂 「へ？　あ、嫉妬とかしてないから大丈夫！…っていうか、気にしてないの？」
    voice "voice/リオン/ron_a1_0368.ogg"
    lion リオン_私服_基本_嬉しい_1 "咦？啊，我没有嫉妒所以没关系！…或者说，你不在意吗？"

    # 莲 「別に。だって、過去がどうだろうと、リオンはリオンだろ。魔法とか、ルールとかそういうのわかんねぇけど、だからといって、住む世界が変わるもんじゃねぇだろ」
    # lian "什么。因为不管过去是怎么样的，里昂就是里昂吧。虽然我不知道魔法、规则之类的，但这并不能改变我们生活的世界"
    lian "当然不介意。因为不管过去是怎么样的，里昂就是里昂吧。虽然我不知道魔法、规则之类的，但这并不能改变我们生活的世界"

    # 里昂 「…な、なんか、予想以上にあっさりして…ビックリというか…拍子抜けというか…」
    voice "voice/リオン/ron_a1_0369.ogg"
    # lion リオン_私服_基本_驚き_1 "…啊，怎么说呢，比预想的还要清淡……与其说是吃惊，不如说是失望……"
    lion リオン_私服_基本_驚き_1 "…啊，怎么说呢，比预想的还要平淡……与其说是吃惊，不如说是失望……"

    # 莲 「でも、リオンの親父さんに挨拶するときは大変かもな」
    lian "但是，和里昂的父亲打招呼的时候可能会很辛苦"

    # 里昂 「あいさ…っ！？　え、それって…えっと…」
    voice "voice/リオン/ron_a1_0370.ogg"
    lion リオン_私服_基本_微笑み_1 "打招呼…！？啊，你是说……那个……"

    # 莲 「なんだ、そこまで考えちゃいかんのか？」
    lian "什么啊，不能考虑到那种程度吗？"

    # 里昂 「…ぜ、ぜんぜんだいじょうぶだけど…だ、だって私は蓮くんのこと、ずっと好きだったし…。ぱ、パは…なんとかする…大丈夫…」
    voice "voice/リオン/ron_a1_0371.ogg"
    # lion リオン_私服_基本_嬉しい_1 "……虽然完全没关系…但是，因为我一直喜欢着莲君……那么，爸爸……总会有办法的…没关系…"
    lion リオン_私服_基本_嬉しい_1 "……虽然完全没关系…但是，因为我一直喜欢着莲君……那么，爸爸那边……总会有办法的…没关系…"

    # nil 「リオンは、ぷしゅーと緊張をといて脱力した。その瞬間、周りの止まっていた時間が動き出した。」
    # "里昂放松了一下。那一瞬间，周围停止的时间开始流动了"
    "里昂放松了下来。那一瞬间，周围停止的时间开始流动了"

    # 背景变回彩色！
    image bg rcg01_4_2 = "images/ev/rcg01_4_2.png"
    scene rcg01_4_2 with dissolve

    # 里昂 「はぁー…あ、安心はしたけど…」
    voice "voice/リオン/ron_a1_0372.ogg"
    lion リオン_私服_基本_悲しい2_1 "哈…啊，虽然安心了……"

    # 莲 「いや、俺も安心したよ。もっとヤバい事情が絡んでて、結ばれる事のない運命だったら悲しいからな」
    # lian "不，我也放心了。如果命中注定有更糟糕的情况，不能结合，那就太可悲了"
    lian "不，我也放心了。如果命中注定有更糟糕的情况，不能让我们在一起，那就太可悲了"

    # 里昂 「本当はその運命だったんだけど…どこかで運命が変わったんだろうか…」
    voice "voice/リオン/ron_a1_0373.ogg"
    lion リオン_私服_基本_微笑み_1 "其实是命中注定的……但是命运在哪里发生变化了呢…"

    # 莲 「そりゃ…簡単だろ…」
    # lian "那倒是…很简单吧…"
    lian "答案…很明显吧…"

    # 里昂 「え？」
    voice "voice/リオン/ron_a1_0374.ogg"
    lion リオン_私服_基本_驚き_1 "诶？"

    # nil 「俺は、時間が動き出して、また溶け始めたアイスクリームを見つめた。」
    "我凝视着，随着时间的流逝又开始融化的冰淇淋"

    # 莲 「ほら、あのアイスをリオンに食わせる前に言った事覚えてるか？」
    lian "你看，还记得我在给里昂吃冰淇淋之前说过的话吗？"

    # 里昂 「自分で作っておいて味も効果も眉唾かい？　…て？」
    # L:按照文法加个括号
    voice "voice/リオン/ron_a1_0375.ogg"
    lion リオン_私服_基本_ニタァ_1 "『自己做的东西，不管味道和效果都令人怀疑呢？』……欸？"

    # 莲 「そこ気にしてたのか…ごめん」
    lian "你是在意那个吗…对不起"

    # 里昂 「いや、気にしてるわけじゃないよ！　それで…えっと…あ…私の…恋…」
    voice "voice/リオン/ron_a1_0376.ogg"
    lion リオン_私服_基本_嬉しい_1 "不，我并不是在意！所以……那个…我的…恋爱…"

    # 莲 「うむ。アンタの恋が叶うのも面白い。そう言ったよな。つまり、あのアイスが、リオンの恋を叶えたんだ」
    lian "嗯，能实现你的恋爱也很有趣，我是这么说的。也就是说，那个冰淇淋实现了里昂的恋爱"

    # 里昂 「ま…まじか…そんな事が…」
    voice "voice/リオン/ron_a1_0377.ogg"
    lion リオン_私服_基本_驚き_1 "真的吗…这种事情…"

    # 不知道为啥，这里当时写重了一堆

    # # 莲 「だってそういう事だろ？　それとも、自分で作っておいて味も効果も眉唾ってのか？」
    # lian "嗯，能实现你的恋爱也很有趣，我是这么说的。也就是说，那个冰淇淋实现了里昂的恋爱"
    # 莲 「だってそういう事だろ？　それとも、自分で作っておいて味も効果も眉唾ってのか？」
    lian "是因为这样吗？还是说，自己做的东西，不管味道和效果都令人怀疑呢？"

    # # 里昂 「ま…まじか…そんな事が…」
    # voice "voice/リオン/ron_a1_0378.ogg"
    # lion "真的吗…这种事情…"

    # # 莲 「だってそういう事だろ？　それとも、自分で作っておいて味も効果も眉唾ってのか？」
    # lian "是因为这样吗？还是说，自己做的东西，不管味道和效果都令人怀疑呢？"

    # 里昂 「で、でも！　でも！　蓮くんはそれでいの！？　魔法で制御された恋だとか、そんな風に思わない！？」
    voice "voice/リオン/ron_a1_0378.ogg"
    lion リオン_私服_基本_ジト目_1 "可、可是！可是！莲君觉得这样可以吗！？你不觉得这是被魔法控制的恋爱吗！？"

    # 莲 「は、何いってんだよ」
    lian "你在说什么啊？"

    # 莲 「恋っつーのは、最初から魔法みたいなもんだろ」
    lian "所谓恋爱，从一开始就是魔法吧"

    # 里昂 「れ、れんく…んっ…うわああああ！」
    # L:牙白，句子又不全，努力听一下吧
    # 看来是CV看台本看差行了23333
    voice "voice/リオン/ron_a1_0379.ogg"
    lion リオン_私服_基本_悲しい2_1 "…莲、莲君……呜啊啊啊啊啊……好高兴，好高兴啊……能得到这样的幸福……真的是……莲君……喜欢……最喜欢你了啊！"

    # 莲 「おいっリオンっ！？」
    lian "喂，里昂！"

    # nil 「リオンは、思い切り、飛び込むように、俺に抱きついた。」
    "里昂尽情地跳入我的怀抱，像是要跳下去一样"

    # 里昂 「うれしい、うれしいよぉ、こんな、こんな幸せになれるなんて、ほんとうに…れんくぅん…すきぃ、大好きだよぉ…！」
    voice "voice/リオン/ron_a1_0380.ogg"
    lion リオン_私服_基本_にっこり_1 "好高兴，好高兴啊，能得到这样的幸福，真的是……莲君……喜欢，最喜欢你了啊！"

    # 莲 「お、おう…俺も大好きだよ、リオン…」
    # lian "哦，哦…我也最喜欢了，里昂…"
    lian "哦，哦…我也最喜欢你了，里昂…"

    # 里昂 「うれしい、うれしいよぉ、こんな、こんな幸せになれるなんて、ほんとうに…れんくぅん…すきぃ、大好きだよぉ…！」
    voice "voice/リオン/ron_a1_0381.ogg"
    lion リオン_私服_基本_嬉しい_1 "哈呜！嗯！最喜欢……"

    # 莲 「だが、一つ悲しいニュースが」
    lian "但是，有一个悲伤的消息"

    # 里昂 「え…？」
    voice "voice/リオン/ron_a1_0382.ogg"
    lion リオン_私服_基本_微笑み_1 "诶…？"

    # 莲 「アイスが…な…」
    lian "冰淇淋…它…"

    # 里昂 「あ゛…」
    voice "voice/リオン/ron_a1_0383.ogg"
    lion リオン_私服_基本_驚き_1 "啊…"

    # nil 「……」
    "……"

    # 里昂 「えーこほん。取り乱しました」
    voice "voice/リオン/ron_a1_0384.ogg"
    # lion リオン_私服_基本_キス "啊——咳咳，我慌了手脚"
    lion リオン_私服_基本_キス "啊——咳咳，我有点慌了手脚"

    # 莲 「いえいえこちらこそ」
    lian "不不，我才是"

    # nil 「アイスは、リオンが魔法で直しました。」
    "冰淇淋是里昂用魔法修好的"

    # nil 「もう何でもありだな…。」
    "已经什么都有了呢……"

    # 里昂 「あんま無闇に魔法を使うのは良くないんだけど…さっきのは内密に…」
    voice "voice/リオン/ron_a1_0385.ogg"
    lion リオン_私服_基本_悲しい2_1 "胡乱使用魔法是不好的…刚才的事情还请保密的说……"

    # 莲 「ていうか、魔法って何なの？　単純に言うとスーパーパワーみたいなもんなの？」
    lian "话说，魔法是什么？简单来说，就像超能力一样吗"

    # 里昂 「んー…人って生まれながらに才能ってあるじゃない？　それのひとつって思ってくれるとわかりやすいかなぁ」
    voice "voice/リオン/ron_a1_0386.ogg"
    lion リオン_私服_基本_微笑み_1 "嗯……人不是天生就有才能吗？如果你认为这是其中之一的话，应该很容易理解吧"

    # 莲 「なるほど」
    lian "原来如此"

    # 里昂 「でも、さっきの時間を止めたり、人の記憶を封印したりするのは、さらに高度で複雑だよ。世界でも、多分、使えるのは私を含むごく一部の人しかできないと思う」
    voice "voice/リオン/ron_a1_0387.ogg"
    # lion リオン_私服_基本_にっこり "但是，刚才的时间停止啊，把人的记忆封印啊，这就更加高度复杂了。世界上，大概只有包括我在内的极少数人才能使用"
    lion リオン_私服_基本_にっこり "但是，刚才的时间停止啊，把人的记忆封印啊，这就更加高级复杂了。世界上，大概只有包括我在内的极少数人才能使用"

    # 莲 「まぁつまり、リオンは最強クラスってことね…」
    lian "也就是说，里昂是最强的Class（L:Class，阶级）呢……"

    # 里昂 「漫画やアニメみたいに戦ったりはしないから、強さはわからないけど…」
    voice "voice/リオン/ron_a1_0388.ogg"
    lion リオン_私服_基本_微笑み "我不会像漫画和动画那样战斗，所以我不知道自己有多强…"

    # 里昂 「でも、我々の信念として、『決して自らの私利私欲のためには使ってはならない。誰をも傷付けず、ただ、幸せにするために使え』ていうのがあって」
    voice "voice/リオン/ron_a1_0389.ogg"
    lion リオン_私服_基本_にっこり "但是，我们的信念是『决不能为了自己的私利私欲而使用。不要伤害任何人，只是为了幸福而使用』这样的"

    # 里昂 「私もそれを遵守しているから…役に立ったのは初めてだよ」
    voice "voice/リオン/ron_a1_0390.ogg"
    lion リオン_私服_基本_嬉しい "我也遵守了那个…这是第一次派上用场"

    # 莲 「やっぱり心愛は規制した方がいんじゃねぇのか？　あいつお菓子食べ放題だぞ」
    lian "果然还是要限制一下心爱吧？那家伙可是在随便吃点心啊（L:好强的怨念啊……）"

    # 里昂 「いやほら、心愛ちゃんはただお菓子を食べてるだけだから…」
    voice "voice/リオン/ron_a1_0391.ogg"
    lion リオン_私服_基本_微笑み "不，你看，心爱酱只是吃点心而已…"

    # 莲 「いのか…」
    lian "是吗…"

    # 里昂 「貢献度も凄いしね。そのぐらいは誰も悲しまないでしょう」
    voice "voice/リオン/ron_a1_0392.ogg"
    lion リオン_私服_基本_にっこり "贡献也很大呢，这点小事谁都不会悲伤的吧"

    # 莲 「あいつ俺にお菓子くれるの渋るんだぜ」
    lian "那家伙不愿意给我点心"

    # 里昂 「それは…一応あの子、ベースになってるお菓子には自腹払ってるから…」
    voice "voice/リオン/ron_a1_0393.ogg"
    lion リオン_私服_基本_微笑み "这个嘛……那个孩子，基本上都是从自己的肚子里面拿的点心的……"

    # 莲 「あ、そうか、ウンコしたら元になってるお菓子が出ちゃうのか」
    lian "啊，这样啊，大便后就会拿出原来的点心吗？"

    # 里昂 「…そ、それは、心愛ちゃんが可哀想だからノーコメントで」
    voice "voice/リオン/ron_a1_0394.ogg"
    lion リオン_私服_基本_悲しい2 "那，那个，因为心爱酱太可怜了，所以无可奉告"

    # nil 「観覧車の中には随分長く居た気もするが、時間が止まっていたので、まだ前半戦だった。リオンとぴったりと身体を寄せ合って、景色を眺める。」
    # "虽然在摩天轮上呆了很久，但是时间停止了，所以还是上半场。和里昂紧紧地靠在一起，眺望景色"
    "虽然在摩天轮上待了很久，但是时间停止了，所以还是上半场。和里昂紧紧地靠在一起，眺望景色"

    # nil 「俺の知ってる世界から、その様相を変えてしまったそとの世界。でも、だからといって、何かが変わる事はなかった。」
    # "外面的世界已经与我所知道的那个世界不同了，但这并不意味着有什么变化"
    "外面的世界已经与我所知道的那个世界不同了，但这并不意味着有什么本质的改变"

    # 里昂 「今更だけど…やっと、心起きなく蓮くんとデートできるね…」
    voice "voice/リオン/ron_a1_0395.ogg"
    lion リオン_私服_基本_嬉しい "事到如今……终于可以和毫无顾忌地莲君约会了……"

    # 莲 「あ、そうだな」
    lian "啊，是啊"

    # 里昂 「……」
    voice "voice/リオン/ron_a1_0396.ogg"
    lion リオン_私服_基本_微笑み "……"

    # 莲 「……」
    lian "……"

    # 里昂 「……」
    voice "voice/リオン/ron_a1_0397.ogg"
    lion リオン_私服_基本_にっこり "……"

    # 莲 「……」
    lian "……"

    # nil 「改めて沈黙。」
    "再次沉默"

    # nil 「結局、世界は変わっても、変わる前の世界とやってることは同じだった。」
    # "结果，即使世界改变了，但我们和改变前的世界做的事情是一样的"
    "结果，即使世界改变了，但我们现在在做的，和我们在改变前的世界做的事情还是相同的"

    # nil 「だけど、もう、リオンの気持ちはわかったし、これからは攻めてみるか。」
    # "但是，我已经明白了里昂的心情，现在要进攻吗"
    "但是，我已经明白了里昂的心情，现在要主动出击吗"

    # 莲 「よし、リオン。キスしよう」
    lian "好，里昂，我们来接吻吧"

    # 里昂 「！　き、きす…！？」
    voice "voice/リオン/ron_a1_0398.ogg"
    lion リオン_私服_基本_驚き_1 "！K、Kiss……？"

    # 莲 「なんでそんな驚くんだよ…恋人同士だろ」
    # lian "为什么会这么吃惊呢…是恋人吧"
    lian "为什么会这么吃惊呢…我们是恋人吧"

    # 里昂 「そそそそ、そうだけど！！　え！？　こでキスしちゃうの！？　まじで！？」
    voice "voice/リオン/ron_a1_0399.ogg"
    lion リオン_私服_基本_驚き_1 "虽虽虽虽、虽然是这样！！欸！？要在这里接吻吗！？真的吗！？"

    # 莲 「なんだ、こでキスしちゃまずい理由でもあるのか？　ダメだぞ、恋人に隠し事は」
    lian "什么嘛，你有什么不该在这里接吻的理由吗？不要对你的恋人有所隐瞒哦"

    # 莲 「ていうか、キスしてからが恋人本番じゃね？」
    lian "话说，接吻之后才是真正的恋人吧？"

    # 里昂 「ぐ…わかった…わかったよ…口では蓮くんには勝てないよ…。わかってる…そう言うところを好きになったんだもん…」
    voice "voice/リオン/ron_a1_0400.ogg"
    # lion リオン_私服_基本_ジト目_1 "嗯…我知道了…我知道了……嘴上是赢不了莲君的……我知道的…我就是喜欢上了这样的地方…"
    lion リオン_私服_基本_ジト目_1 "嗯…我知道了…我知道了……嘴上是赢不了莲君的……我知道的…我就是喜欢上了你这样的地方…"

    # 莲 「ということで、そのお口で、改めて…」
    lian "这么说来，你的嘴，再一次……"

    # 里昂 「わー！　わー！　ちょっとタンマ！　お願いだから３秒待って！」
    voice "voice/リオン/ron_a1_0401.ogg"
    lion リオン_私服_基本_悲しい2_1 "哇！哇！请等一下！拜托了，给我3秒钟！"

    # 莲 「３」
    lian "３"

    # 里昂 「え！？　まじでカウントダウンしちゃうの！？　すーはーすーはー」
    voice "voice/リオン/ron_a1_0402.ogg"
    lion リオン_私服_基本_驚き_1 "诶！？真的在倒计时了！？哈—啊—哈—啊—"

    # 莲 「２」
    lian "２"

    # 里昂 「すーはーすーはー…ベルはボタン…スイカはお弁当…リプレイは青春…」
    voice "voice/リオン/ron_a1_0403.ogg"
    lion リオン_私服_基本_無表情_1 "哈—啊—哈—啊—……Bell是Button……西瓜是便当……Replay是青春"

    # nil 「なんでスロットの絵柄を…しかもその図柄の組み合わせは…。番長だ…。」
    # 参考资料：https://ja.wikipedia.org/wiki/%E6%8A%BC%E5%BF%8D!%E7%95%AA%E9%95%B7
    "为什么是老虎机的图案…而且那个图案的组合是…番長…（L:这里说的是「押忍!番長」的图案，「押忍!番長」是大都技研于2005年6月发售的老虎机）"

    # nil 「こいつ本当にイギリス人かよ…魔法使いとかそういうの関係無しに、微妙な所詳しすぎるだろ。」
    "这家伙真的是英国人吗？和魔法使什么的没有关系，微妙的地方知道的也太详细了吧"

    # 莲 「１」
    lian "１"

    # 里昂 「よ、よしこーい！」
    voice "voice/リオン/ron_a1_0404.ogg"
    lion リオン_私服_基本_驚き_1 "好，好啊冲鸭——！"

    # 莲 「いくよ、リオン」
    lian "要上了哦，里昂"

    # 里昂 「んっ…」
    voice "voice/リオン/ron_a1_0405.ogg"
    lion リオン_私服_基本_キス_1 "嗯…"

    # 差分背景
    image bg rcg01_5_2 = "images/ev/rcg01_5_2.png"
    scene rcg01_5_2 with dissolve

    # nil 「俺は、リオンのアゴを持ち上げる。リオンは肩を強張らせたが、硬く目を閉じて俺のキスを待った。」
    "我抬起了里昂的下巴。里昂绷紧了肩膀，但还是紧紧闭上眼睛等待我的吻"

    # nil 「そして…」
    "然后…"

    # nil 「ちゅっ」
    "啾"

    # 里昂 「んぅ…ちゅぅ…んっ、んぅうっっっっっっっっっっっっ！」
    voice "voice/リオン/ron_a1_0406.ogg"
    lion リオン_私服_基本_嬉しい_1 "嗯……啾…嗯，嗯嗯嗯嗯嗯嗯嗯嗯嗯！"

    # 莲 「！？」
    lian "！？"

    # nil 「リオンは俺と唇を合わせながら、ぎゅっと俺の肩を掴んで、身体を震わせた。」
    "里昂和我嘴唇合在一起，紧紧抓住我的肩膀，身体颤抖着"

    # nil 「もしかして…リオン…。」
    "难道…里昂…"

    # 里昂 「ぅ…んぅ…」
    # L:HOOK提取不全不动手打了
    voice "voice/リオン/ron_a1_0407.ogg"
    lion リオン_私服_基本_悲しい2_1 "哈……哈……哈啊……哈啊……呜……呜……"

    # 莲 「もしかして…リオン、今ので…」
    lian "莫非…里昂，刚才的……"

    # 里昂 「はぅ…んぅ…はあぅ…」
    voice "voice/リオン/ron_a1_0408.ogg"
    lion リオン_私服_基本_嬉しい_1 "哈…嗯…哈啊…"

    # nil 「リオンは、くてっと身体の支えを失って、俺にすがるように倒れ込んできた。俺はその身体を抱き留める。」
    # "里昂突然失去了身体的支撑，依靠着我倒了下来。我抱住了那个身体"
    "里昂突然失去了支撑身体的力气，依靠着我倒了下来。我抱住了她的身体"

    # nil 「リオンの身体は、ぴくぴくと痙攣し、目は焦点を失っている。」
    "里昂的身体抽搐着，眼睛失去了焦点"

    # 里昂 「イっちゃ…た…ぁう…ゃぁ…」
    voice "voice/リオン/ron_a1_0409.ogg"
    lion リオン_私服_基本_悲しい2_1 "哈啊……去……去了……呀……"

    # nil 「恐らく…リオンは、俺とキスした事で絶頂を迎えてしまったようだ。」
    "恐怕…里昂因为和我接吻而迎来了高潮"

    # nil 「ど…どうしよう。」
    "怎…怎么办"

    # 里昂 「ぅ…はずかしぃ…ぅ…はぅ…」
    voice "voice/リオン/ron_a1_0410.ogg"
    lion リオン_私服_基本_悲しい2_1 "呜……好羞耻啊……哈呜……"

    # nil 「俺が黙っていると。リオンは今にも泣きそうな顔になってしまう。」
    # "如果我保持沉默，里昂马上就要哭了"
    "如果我保持沉默，估计里昂马上就要哭了"

    # nil 「なんとか安心させてあげなくては。」
    # "一定要想办法让她安心"
    "一定要想办法让她安心下来"

    # 莲 「可愛いよ、リオン」
    lian "好可爱啊，里昂"

    # 里昂 「れんくぅん…もっと、もっとキス…したぃ…」
    voice "voice/リオン/ron_a1_0411.ogg"
    lion リオン_私服_基本_嬉しい_1 "莲君……还想、还想……再吻你……"

    # 莲 「で、でも、リオン、お前、身体は大丈夫なのか？」
    lian "但是，里昂，你的身体没问题吗？"

    # 里昂 「イっちゃってもいよぉ…ね、キス、キスぅ…」
    voice "voice/リオン/ron_a1_0412.ogg"
    lion リオン_私服_基本_微笑み_1 "去了也可以啦……呐，Kiss、Kiss……"

    # nil 「あ。これは。どうにでもなれってパターンだ！　教科書で読んだ！」
    "啊。这是、这是随心所欲的模式！我在教科书上看到过！"

    # 里昂 「んぅ…ちゅぅ…ん、んぅう、はぁあうっ！」
    voice "voice/リオン/ron_a1_0413.ogg"
    lion リオン_私服_基本_にっこり_1 "呜…啾…嗯、嗯、呜、哈啊啊啊！"

    # nil 「舌を絡ませてもいないのに、リオンはまたキスだけでイってしまう。」
    "明明连舌头都没缠在一起，里昂只是接吻而已"

    # nil 「その様子を見ているだけで、俺は痛いほど興奮してしまっている。」
    "光是看到那个样子，我就兴奋得不得了"

    # 里昂 「はぁ、はぁ…ぁぅ…やだ…もう…とまんないよぉ…蓮くんと…一つになりた…い…」
    voice "voice/リオン/ron_a1_0414.ogg"
    # lion リオン_私服_基本_嬉しい_1 "哈，哈…讨厌…已经…停不下来了…我想……和莲君…成为一体了……啊…"
    lion リオン_私服_基本_嬉しい_1 "哈，哈…讨厌…已经…停不下来了…我想……和莲君…合为一体了……啊…"

    # 莲 「リオン…」
    lian "里昂……"

    # nil 「リオンはすがるように、甘えてくる。もうこのま流されてもいか！」
    "里昂如饥似渴地撒娇，就这样随波逐流吧！"

    # nil 「とおもったが、いつのまにか、ゴンドラは地上へと近づいていた。」
    "但是，不知什么时候，摩天轮已经接近地面了"

    # 莲 「なぁ、リオン。続き…しにいくか…？　とりあえず、観覧車おりないと…」
    lian "呐，里昂。要继续吗……？总之，得先下去，从摩天轮上……"

    # 里昂 「ぅん…本当に続きしてくれる…？　私もう、帰りたくないよ…？」
    voice "voice/リオン/ron_a1_0415.ogg"
    lion リオン_私服_基本_悲しい2_1 "嗯……真的可以继续吗…？我已经不想回去了…？"

    # 莲 「あ、あ。沢山しにいこう」
    # lian "啊，啊。去很多地方吧"
    lian "啊，啊。一起去很多地方吧"

    # 里昂 「わーい…♪　えへへ…優しい蓮くん、だーいすき…♪」
    voice "voice/リオン/ron_a1_0416.ogg"
    lion リオン_私服_基本_にっこり_1 "哇……♪诶嘿嘿…温柔的莲君，最喜欢了…♪"

    # 莲 「お、おう。立てるか、リオン」
    lian "哦，哦，你能站起来吗，里昂"

    # 里昂 「う、うん、ちょっと…むずむずするけど…だいじょぶ…」
    voice "voice/リオン/ron_a1_0417.ogg"
    lion リオン_私服_基本_嬉しい_1 "嗯，嗯，有点……痒痒的…没关系…"

    # nil 「そりゃそうだろう。二回もイってしまったのだから。リオンはよたよたとしながら、なんとか立ち上がり、ゴンドラから下りた。」
    "那是当然的。因为已经去了两次了。里昂摇摇晃晃地站了起来，从缆车上下来"

    # nil 「人生で最強に長い観覧車だった…。」
    # "是我一生做过的最厉害最漫长的摩天轮……"
    "这是我一生中做过的最厉害最漫长的摩天轮……"

    # nil 「完全にラブラブモードがオンになってしまったリオンは、くてっと俺の身体に力なく抱きついている。」
    "完全开启了恋爱模式的里昂，紧紧地抱住了我的身体"

    # nil 「なんとか…近くのホテルまでつれてかないと…。」
    "如果……不赶紧带去附近的酒店的话…"

    # 莲 「（っとその前に…）」
    lian "（在那之前…）"

    # nil 「俺はランドマークタワーの、頂上にむかって、指で作った銃を向けた。」
    # "我对着地标塔的山顶，用手指比的枪对准了那里"
    "我对着地标塔的顶部，用手指比的枪对准了那里"

    # 莲 「ここから先はR指定だ」
    # 参考资料：https://ja.wikipedia.org/wiki/R-%E6%8C%87%E5%AE%9A_(%E3%83%A9%E3%83%83%E3%83%91%E3%83%BC)
    # 参考资料：https://dic.nicovideo.jp/a/%E3%83%80%E3%83%B3%E3%83%86
    # 参考资料：https://dic.nicovideo.jp/a/r%E6%8C%87%E5%AE%9A
    lian "从这里开始就是R指定了（L:这里用的是鬼泣4中但丁的经典句“ここから先はR指定だ”，“R指定”指动画等作品的年龄分级，即接下来的内容就不是全年龄向的意思）"

    scene black with ImageDissolve("images/tr/縦ブラインド.png", 0.2, ramplen=128, reverse=True, alpha=True, time_warp=None)

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「気づいていたか…存外、勘の良い…」
    voice "voice/想瑠/sol_a1_0092.ogg"
    liu 想瑠_スーツ_目閉じ "你注意到了吗……没想到你的直觉……"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 雾叶？？？ 「それで、歯車は動き出しましたか？」
    voice "voice/霧葉/krh_a1_0062.ogg"
    # hei 黑_私服_無表情 "那么，齿轮开动了吗？"
    hei 黑_私服_無表情 "那么，齿轮开始转动了吗？"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「思ってたよりもスムーズにな。嬉しい誤算だ」
    voice "voice/想瑠/sol_a1_0093.ogg"
    liu 想瑠_スーツ_ニヤリ "比我想象的要顺利，真是令人高兴的失算啊"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 雾叶？？？ 「それはよかった。これから先が楽しみですね」
    voice "voice/霧葉/krh_a1_0063.ogg"
    # hei 黑_私服_目閉じ "那太好了，我很期待接下来的事"
    hei 黑_私服_目閉じ "那太好了，我很期待接下来的事呢"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「あ。さて、私達も戻ろうか」
    voice "voice/想瑠/sol_a1_0094.ogg"
    liu 想瑠_スーツ_見下し "啊，好了，我们也回去吧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぶえー想瑠にゃんこ寒いよー！」
    voice "voice/心愛/cca_a1_0666.ogg"
    ai 心愛_私服_基本_ぶわー "呜欸，想瑠喵好冷喔！（L:这里也莫得配音……）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「アイス食べる？　美味しいよ？」
    voice "voice/真冬/maf_a1_0183.ogg"
    dong 真冬_私服_基本_無表情 "吃冰淇淋吗？很好吃哦？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「死んじゃうよ！？」
    voice "voice/心愛/cca_a1_0667.ogg"
    ai 心愛_私服_基本_ポカーン "会死的哦！？"

    # scene19 场景1 【和里昂的初次约会】 圆满结束！

    # 离全部翻译完成只剩 3 个 Scene ！

    # 过场：里昂（常服）

    # Scene19 结束！
    # 隐藏 quick_menu
    $ quick_menu = False
    stop music fadeout 2.0
    play sound "voice/effect/moosehead honk (stinger).ogg"
    # hide screen quick_menu
    # scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)
    scene アイキャッチリオン with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)

    $ renpy.pause(1.5, hard=True)

    $ renpy.end_replay()

    jump scene20

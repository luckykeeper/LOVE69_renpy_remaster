# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene13 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：
# 版本 0.5 "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年3月7日

# 当前流程：编写脚本AIO Process

label scene13:
    # scene13 开始

    # scene13 场景1 【期待已久的夏威夷之行与最终的婚礼】 开始
    # L我也期待已久了，一周目终于要结束了！！！

    # 地点：机场/夏威夷高空（飞机上）
    # 人物：心爱 真冬 莲
    # BGM：bgm38

    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)
    image bg ハワイg = "images/bg/ハワイg.png"
    scene ハワイg with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)

    # 显示 quick_menu
    $ quick_menu = True

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ハーーーーワーーーーイーだーーーーー！！」
    ## 1501-1583 跳过
    voice "voice/心愛/cca_a1_1584.ogg"
    ai 心愛_私服_基本_笑顔 "是夏——————威——夷——哒————————————！！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まだ空港だよ」
    ## 1187-1269 跳过
    voice "voice/真冬/maf_a1_1270.ogg"
    dong 真冬_私服_基本_無表情 "还在机场呢"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「気持ちだけ先走りました」
    voice "voice/心愛/cca_a1_1585.ogg"
    ai 心愛_私服_基本_ぶわー "我的心情已经先出去了"

    # 场景切换：机场->Waikiki Beach
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene ハワイc with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「…いやー…暑いね」
    show 心愛_私服_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1586.ogg"
    ai 心愛_私服_基本_泣き "……呀……真热啊"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うん、もう夏だから暑いのは当たり前なんだけど、大概暑いよね」
    show 真冬_私服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1271.ogg"
    dong 真冬_私服_基本_無表情 "嗯，已经是夏天了，当然很热了，大概平时也很热吧"

    # 莲 「なんか、海外にきたみてぇだな」
    lian "好像，是来到海外了捏"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ね、外国みたいだねー」
    show 心愛_私服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1587.ogg"
    ai 心愛_私服_基本_笑顔 "欸，好像是国外呢——"
    hide 心愛_私服_基本_泣き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「葛城さん、こハワイだよ」
    show 真冬_私服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_1272.ogg"
    dong 真冬_私服_基本_目閉じ "葛城兄，这里是夏威夷哦"
    hide 真冬_私服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ハーーーーワーーーイーーーだーーーー！！」
    show 心愛_私服_基本_にっこり at love69_right with dissolve
    voice "voice/心愛/cca_a1_1588.ogg"
    ai 心愛_私服_基本_にっこり "是夏——————威————夷————哒——————！！"
    hide 心愛_私服_基本_笑顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「飛行機のシーンはすっとばしたね、お兄ちゃん」
    show 真冬_私服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1273.ogg"
    dong 真冬_私服_基本_無表情 "你跳过了飞机上的场景呢，欧尼酱"
    hide 真冬_私服_基本_目閉じ

    # 莲 「寝てたからな」
    lian "因为我睡着了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「いやっほおおおおおう！　Ｆｏｏｏｃｏ↑！！」
    hide 心愛_私服_基本_にっこり
    show 心愛_私服_基本_笑顔:
        zoom 1.5
        xalign 0.8918
        yalign -0.09
        linear 0.15 yalign -0.02
        linear 0.15 yalign -0.09
    voice "voice/心愛/cca_a1_1589.ogg"
    ai 心愛_私服_基本_笑顔 "耶！Yahoooooooooo！Ｆｏｏｏｃｏ↑！！"

    # nil 「ということで、やって参りました。ハワイ。」
    "所以我们来到了夏威夷"

    # nil 「新東京国際空港から時間。エコノミークラスでしたが、比較的快適でした。」
    # TechnoBrain官网：https://www.technobrain.com/ 
    "从新东京国际机场（L:就是成田国际机场）出发到这里要8小时。虽然是经济舱，但相对来说还算舒服（L:这里我来给大家推一下TechnoBrain的ぼくは航空管制官系列，非常非常好玩，是阔以对成田机场、夏威夷机场等机场进行模拟管制的非常非常好玩的游戏，搜ATC2、3、4就能找到）"

    # nil 「そのま飛行機を降りて、ワイキビーチへやってきました。」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%AF%E3%82%A4%E3%82%AD%E3%82%AD
    "然后我们下了飞机，来到了Waikiki Beach（L:Waikiki，夏威夷语，意思为“喷涌的淡水。Waikiki Beach是怀基基/威基基地区的著名海滩）"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「海だァア！　しかもそんじょそこらのオイルと洗剤で濁った海じゃないぜ…ハワイの海だァア！」
    hide 心愛_私服_基本_笑顔
    show 心愛_私服_基本_笑顔:
        zoom 1.5
        xalign 0.8918
        yalign -0.09
        linear 0.15 yalign -0.02
        linear 0.15 yalign -0.09
    voice "voice/心愛/cca_a1_1590.ogg"
    ai 心愛_私服_基本_笑顔 "是海啊！而且不是到处都是油和洗涤剂的海啊…是夏威夷的海啊！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「この…透明感…！　この、透明感！」
    voice "voice/真冬/maf_a1_1274.ogg"
    dong 真冬_私服_基本_無表情 "这种…透明感…！这种，透明感！"

    # nil 「真冬は語彙が乏しかった。」
    "真冬这属于是语死早了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「よぉーし！　まふまふちゃんいっくよー！」
    voice "voice/心愛/cca_a1_1591.ogg"
    ai 心愛_私服_基本_笑顔 "好耶——！嘛呼嘛呼酱冲呀——！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「おっしゃ」
    # 参考资料：https://www.weblio.jp/content/%E3%81%8A%E3%81%A3%E3%81%97%E3%82%83 这是大阪方言
    show 真冬_私服_基本_ニタァ at love69_left with dissolve
    voice "voice/真冬/maf_a1_1275.ogg"
    dong 真冬_私服_基本_ニタァ "好呀"
    hide 真冬_私服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「わん」
    voice "voice/心愛/cca_a1_1592.ogg"
    ai 心愛_私服_基本_笑顔 "One"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「つー」
    show 真冬_私服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1276.ogg"
    dong 真冬_私服_基本_無表情 "Two——"
    hide 真冬_私服_基本_ニタァ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「すりー！」
    show 心愛_私服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1593.ogg"
    ai 心愛_私服_基本_笑顔 "Three——！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 心爱&真冬 「『Ｆｏｏｏｏｏｕ！』」
    voice "voice/真冬/maf_a1_1277.ogg"
    ai_dong 真冬_私服_基本_無表情 "『Ｆｏｏｏｏｏｕ！』"

    # 莲 「なんで中途半端な数なんだよ！っておいおい、何故脱ぐ！」
    lian "为什么是半吊子的数啊！喂喂，为啥开始脱衣服了啊！"

    # nil 「真冬と心愛は、女の子特有の脱衣スキルで、一気に着ていた衣服を脱ぎ捨てた。」
    "真冬和心爱发动了女孩子特有的脱衣技能，一口气脱掉了身上的衣服"

    # nil 「そして…。」
    "然后…"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「てーれってー」
    hide 真冬_私服_基本_無表情
    show 真冬_水着_基本_まったり at love69_left
    with dissolve
    voice "voice/真冬/maf_a1_1278.ogg"
    dong 真冬_水着_基本_まったり "锵——锵——锵"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ばっこぉーん！」
    hide 心愛_私服_基本_笑顔
    show 心愛_水着_基本_にっこり at love69_right
    with dissolve
    voice "voice/心愛/cca_a1_1595.ogg"
    ai 心愛_水着_基本_にっこり "轰——！"

    # 莲 「Wow！」
    lian "Wow！"

    # nil 「真冬と心愛が衣服を脱いだら、そこには、新調されたビキニスタイルの水着と、瑞々しい肌の肢体がお披露目された。」
    "真冬和心爱脱下衣服后，露出了新的比基尼泳衣和鲜嫩的皮肤"

    # nil 「真冬と心愛はドヤ顔で、こちらを見つめてくる。」
    "真冬和心爱是一副得意的表情，凝视着这边。"

    # nil 「つい感嘆のため息をもらしてしまった。」
    "不由得叹了一口气"

    # nil 「二人と結ばれてから、彼女達の肌は割と眺めている方だが、やはり日の下で、こうやって拝むと、来るものがある。」
    "自从我和他们在一起后，我经常能看到她们的肌肤，但像这样在阳光下看到它，又是一种别样的感觉"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「どうどう？　蓮くん！」
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1596.ogg"
    ai 心愛_水着_基本_笑顔 "怎么样？怎么样？莲君！"
    hide 心愛_水着_基本_にっこり

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「私達似合ってる？」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1279.ogg"
    dong 真冬_水着_基本_微笑み "我们这身合适吗？"
    hide 真冬_水着_基本_まったり

    # 莲 「まさか、家からずっと着てきたのか？」
    lian "难道说，从家里就一直这么穿过来的？"

    # 真冬 「余計な事は聞かないの」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1280.ogg"
    dong 真冬_水着_基本_無表情 "不要问多余的事"
    hide 真冬_水着_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「人生でこれほどまでにパンチラを気にしたのは初めてです。で、どうです？　彼氏くんの好みに合いましたか？　私達の水着姿ァ！」
    voice "voice/心愛/cca_a1_1597.ogg"
    ai 心愛_水着_基本_笑顔 "人生中第一次这么在意穿着胖次。怎么样？符合男朋友的喜好了吗？我们的泳装造型！"

    # 莲 「いや、素晴らしいよ、よく似合ってるし、二人ともやっぱり可愛いな」
    lian "不能说很好，只是说是太棒了，很适合你俩，两个人都很可爱呢"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「えへへー」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1281.ogg"
    dong 真冬_水着_基本_微笑み "欸嘿嘿——"
    hide 真冬_水着_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「にゃはー褒められると素直に嬉しいにゃー」
    show 心愛_水着_基本_にっこり at love69_right with dissolve
    voice "voice/心愛/cca_a1_1598.ogg"
    ai 心愛_水着_基本_にっこり "呀哈，被夸奖的话真的很开心喵"
    hide 心愛_水着_基本_笑顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「と、言う事で、今日一日はこの格好でいます」
    show 真冬_水着_基本_まったり at love69_left with dissolve
    voice "voice/真冬/maf_a1_1282.ogg"
    dong 真冬_水着_基本_まったり "那，这么说的话，今天一整天都穿这身衣服吧"
    hide 真冬_水着_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「なっ…オラそげな話は聞いてねぇぞ！？」
    show 心愛_水着_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1599.ogg"
    ai 心愛_水着_基本_不機嫌 "啥…那个，我可没听过这种事！？"
    hide 心愛_水着_基本_にっこり

    # 莲 「頼むわ…」
    lian "拜托了…"

    # 心爱 「お、おう…そんなマジな顔されたら…仕方ないにゃぁ…いよ」
    show 心愛_水着_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1600.ogg"
    ai 心愛_水着_基本_嬉しい "哦，哦…看到你这么认真的表情…那就没办法了……可以的哦"
    hide 心愛_水着_基本_不機嫌

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「お兄ちゃんも素直でよろしい」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1283.ogg"
    dong 真冬_水着_基本_微笑み "欧尼酱这么坦率我很高兴"
    hide 真冬_水着_基本_まったり

    # nil 「正直な所、二人の水着姿は刺激的で最高だった。ハワイの陽気に当てられて、テンションがついあがっちまう。」
    "说实话，两人穿泳衣的样子很刺激，是坠吼的。夏威夷的阳光让我兴奋不已"

    # 莲 「せっかくの旅行だ。俺もハメを外すとすっか」
    # 参考资料：https://www.weblio.jp/content/%E7%BE%BD%E7%9B%AE%E3%82%92%E5%A4%96%E3%81%99 http://fanblogs.jp/linushas/archive/2819/0
    # 这是用了马术用语捏
    lian "真是难得的旅行，我也要脱掉衣服了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「そうだそうだ！　そんなアロハなんて脱いでしまえ！」
    # 参考资料：https://diamond.jp/articles/-/224634
    show 心愛_水着_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1601.ogg"
    ai 心愛_水着_基本_不機嫌 "就是就是！把那样的ALOHA脱下来吧！（L:ALOHA，夏威夷语，可以表示非常多的意思，比如：嗨、早上好、你好、晚上好、欢迎、再见、我爱你，还意味着还意味着爱、亲情、同情、恩惠、善良、怜悯、怜悯、同情、爱人。这五个字母分别代表同情、协调、喜悦、谦逊、耐心，这里这么用是因为这个词意思太多了就放在这里罢）"
    hide 心愛_水着_基本_嬉しい

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ついでにそのデニムのショーパンも脱いじゃいなさいよ」
    voice "voice/真冬/maf_a1_1284.ogg"
    dong 真冬_水着_基本_微笑み "既然如此，就把牛仔短裤也脱掉吧"

    # 莲 「アロハは許すが、デニムはだめだ。貴様らと違って下に何も履いてない」
    lian "ALOHA是可以的，但是牛仔裤不行。不像你们，我里面没有穿任何东西"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ま…まじですか…パンツもですか…」
    show 心愛_水着_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1602.ogg"
    ai 心愛_水着_基本_泣き "真……真的吗……胖次没在里面吗……"
    hide 心愛_水着_基本_不機嫌

    # 莲 「だって真冬ちゃんが俺のトランクス捨てちゃったんだもん」
    lian "因为真冬酱把我的平角内裤扔掉了（L:前面有提到心爱酱问真冬酱这个龙纹的平角内裤是什么，真冬给扔了233）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ハイビスカス柄だけは残しておいたじゃないの」
    show 真冬_水着_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_1285.ogg"
    dong 真冬_水着_基本_目閉じ "不是留下了扶桑花图案的吗？"
    hide 真冬_水着_基本_微笑み

    # 莲 「アロハもハイビスカスで、パンツもハイビスカスって…ハイビスカスのトータルコーディネートかよ！」
    lian "ALOHA是扶桑花，裤子也是扶桑花…是扶桑花的全套搭配吗！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「そのまんまだよ！？でも、ハメを外すのは賛成！　えーい！　蓮くんの好きなＯＰＰＡＩだぞー！」&&ハメを外すのは賛成 协力请求
    # 参考资料：https://zh.hinative.com/questions/19601280 http://fanblogs.jp/linushas/archive/2819/0
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1603.ogg"
    ai 心愛_水着_基本_笑顔 "就是这样的哦！？但是，我完全赞成脱衣服！欸——！是莲君喜欢的ＯＰＰＡＩ哦——！"
    hide 心愛_水着_基本_泣き

    # 音效：戳戳
    play sound "voice/effect/17_フヒ.ogg"

    # nil 「心愛が俺の右腕を掴むように突進してくる。」
    "心爱冲过来抓住我的右臂"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「心愛ちゃんだけの好きにはさせないわ」
    voice "voice/真冬/maf_a1_1286.ogg"
    dong 真冬_水着_基本_目閉じ "我不会只让心爱酱一个人随心所欲的"

    # nil 「真冬も俺の左腕に、谷間で腕を挟むようにしてしがみついた。」
    "真冬也在我的左边，用山谷夹住了我的左臂"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぷにぷにぷにぷに！」
    voice "voice/心愛/cca_a1_1604.ogg"
    ai 心愛_水着_基本_笑顔 "噗腻噗腻噗腻噗腻！"
    
    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ぷにぷにぷにぷに！」
    show 真冬_水着_基本_まったり at love69_left with dissolve
    voice "voice/真冬/maf_a1_1287.ogg"
    dong 真冬_水着_基本_まったり "噗腻噗腻噗腻噗腻！"
    hide 真冬_水着_基本_目閉じ

    # 莲 「こら、お二人ともおやめなすってー！　周りの視線集めまくりで恥ずかしいからぁ！」
    lian "喂，你们两个都住手吧！周围的视线都看向这边了很是害羞啊！"

    # 外人さん（外国人先生） 「Oh... It's so Awesome！」
    # 这里就叫老外A吧 ForeignerA foreignera
    foreignera "Oh... It's so Awesome！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「せんきゅー！」
    voice "voice/心愛/cca_a1_1605.ogg"
    ai 心愛_水着_基本_笑顔 "Thank you——！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ゆーあーうぇるかむ！」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1288.ogg"
    dong 真冬_水着_基本_微笑み "You're welcome！"
    hide 真冬_水着_基本_まったり

    # nil 「と、言う事で、本日よりもテンション増し増しでお送りします。」
    "因此，就像这样，今天的紧张兴奋程度真是蹭蹭地往上涨呢"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「全力全開で楽しませてもらうよ！　しっかりついて来てね！」
    show 心愛_水着_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1606.ogg"
    ai 心愛_水着_基本_嬉しい "会全力全开地让你开心的哟！请好好跟上哦！"
    hide 心愛_水着_基本_笑顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「れっつろっく！　ハナっから飛ばしていくぜミスターブラザー」
    show 真冬_水着_基本_ジト目 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1289.ogg"
    dong 真冬_水着_基本_ジト目 "Let's rock！用把花吹走的气势上啊Mr.brother桑"
    hide 真冬_水着_基本_微笑み

    # 莲 「上等！」
    # L:前面有提到过这个用法
    lian "来吧！"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene ハワイc with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「カメハメハ大王！！　私にアロ波の打ち方を教えてください！」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%AB%E3%83%A1%E3%83%8F%E3%83%A1%E3%83%8F1%E4%B8%96
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1607.ogg"
    ai 心愛_水着_基本_笑顔 "卡美哈梅哈大帝！！请教给我ALOHA波的打法！（L:卡美哈梅哈大帝是夏威夷王国的开创者。其名字全称为Kalani Paiʻea Wohi o Kaleikini Kealiʻikui Kamehameha o ʻIolani i Kaiwikapu kaui Ka Liholiho Kūnuiākea。他原是夏威夷岛的一个酋长，经过多年征战，于1810年统一了夏威夷群岛）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「あー…ろー…」
    show 真冬_水着_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_1290.ogg"
    dong 真冬_水着_基本_目閉じ "A——LO——……"

    # 心爱&真冬 「『波ァー！』」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1291.ogg"
    ai_dong 真冬_水着_基本_微笑み "『HA——！』"
    hide 真冬_水着_基本_目閉じ

    # 莲 「こらこら、変なビームを打つのやめなさい」
    lian "喂，别再打出奇怪的光束了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「三倍だァーーー！」
    voice "voice/心愛/cca_a1_1609.ogg"
    ai 心愛_水着_基本_笑顔 "是三倍啊——！（L:红有三？）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ちなみに、その像はデューク・カハナモクの像で、カメハメハ大王は他の所にいるよ」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%87%E3%83%A5%E3%83%BC%E3%82%AF%E3%83%BB%E3%82%AB%E3%83%8F%E3%83%8A%E3%83%A2%E3%82%AF
    show 真冬_水着_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_1292.ogg"
    dong 真冬_水着_基本_目閉じ "顺带一提，那个像是杜克·卡哈纳莫库的雕像，卡美哈梅哈大帝的在其它地方哦（L:杜克·保阿·卡西努·莫科埃·胡利科霍拉·卡哈纳莫库 Duke Paoa Kahinu Mokoe Hulikohola Kahanamoku，1890年8月24日－1968年1月22日），美国夏威夷族游泳运动员。他在奥林匹克运动会游泳比赛中共获得3枚金牌和2枚银牌）"
    hide 真冬_水着_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「デューク…あれですか、ウォーキング健康法の…」
    show 心愛_水着_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1610.ogg"
    ai 心愛_水着_基本_真顔 "杜克…是那个吗，步行健康法的…"
    hide 心愛_水着_基本_笑顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「残念だけどサーフィンかな」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1293.ogg"
    dong 真冬_水着_基本_無表情 "虽然很遗憾，是冲浪吧"
    hide 真冬_水着_基本_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「サーフィンかー…無念」
    show 心愛_水着_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1611.ogg"
    ai 心愛_水着_基本_不機嫌 "冲浪啊…遗憾"
    hide 心愛_水着_基本_真顔

    # 场景切换：Waikiki Beach->夏威夷市内
    image bg ハワイa = "images/bg/ハワイa.png"
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene ハワイa with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    
    # 心爱 「ということで一発目。ハワイに来たらやっぱ！」
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1612.ogg"
    ai 心愛_水着_基本_笑顔 "那么第一次，来夏威夷的话果然是！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うん」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1294.ogg"
    dong 真冬_水着_基本_微笑み "嗯"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「出雲大社でしょう！」
    show 心愛_水着_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1613.ogg"
    ai 心愛_水着_基本_嬉しい "是出云大社吧！（L:前面莲和心爱最初约会的时候有提过）"
    hide 心愛_水着_基本_笑顔

    # 莲 「海じゃねぇのかよ！　結構歩いて来ちゃったぞ！」
    lian "原来不是大海啊！真是走了不少路呢！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「本日のロケは海禁です」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%AD%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E6%92%AE%E5%BD%B1
    show 真冬_水着_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_1295.ogg"
    dong 真冬_水着_基本_目閉じ "今天的外景拍摄是海禁哦（L:ロケ ロケーション撮影 location shooting 外景拍摄）"
    hide 真冬_水着_基本_微笑み

    # 莲 「この番組を考えたディレクター出てこい」
    lian "想出这个节目的导演给我出来一下"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「こんにちは」
    hide 心愛_水着_基本_嬉しい
    show 心愛_水着_基本_真顔:
        zoom 1.5
        xalign 0.8918
        yalign -0.09
        linear 0.15 yalign -0.02
        linear 0.15 yalign -0.09
    voice "voice/心愛/cca_a1_1614.ogg"
    ai 心愛_水着_基本_真顔 "你好"

    # 莲 「海入りたいです」
    lian "我想去海边"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「よかろう」
    voice "voice/心愛/cca_a1_1615.ogg"
    ai 心愛_水着_基本_真顔 "好吧"

    # 莲 「許可でました！」
    lian "得到许可了！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「では、先にお参りしましょう」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1296.ogg"
    dong 真冬_水着_基本_無表情 "那么，我们就先去这边吧"
    hide 真冬_水着_基本_目閉じ

    # 莲 「やっぱいくんすね…」
    lian "果然还是要去啊…"

    # 场景切换：夏威夷市内->夏威夷出云大社
    ## For Background 2600*1800
    # transform love69_bg1800:
    #     truecenter
    #     # zoom 0.89
    #     # xalign 1.1
    #     # yalign 0.5
    ## truecenter 即可

    image bg ハワイ_出雲大社 = "images/bg/ハワイ_出雲大社.png"
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene ハワイ_出雲大社 at truecenter with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
 
    # ナレーション（旁白） 「つーことで、ハワイ出雲大社にやってきたみたいですよ。やっぱ好きなんすねぇ」
    # 这个旁白好像是想瑠喵，音声文件应该在想瑠喵的文件夹那边
    # 14nm+++++++++ 人物表++++++++ 人物表就像14nm一样捏
    # 来康鬼畜：https://www.bilibili.com/video/av79908163/
    ## 没有跳过
    voice "voice/想瑠/sol_a1_0184.ogg"
    aside "话说回来，好像来到去了夏威夷出云大社。果然很喜欢呢"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はいこで問題です」
    show 心愛_水着_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1616.ogg"
    ai 心愛_水着_基本_真顔 "这里，这边有问题！"

    # 莲 「商品はでますか」
    lian "是新产品上市了吗"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「チューしてあげるよ、比較的濃厚に」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1297.ogg"
    dong 真冬_水着_基本_無表情 "我要一个“啾——”（给答对的人），比较浓厚那种"

    # 莲 「乗った」
    lian "上车了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「正しいお参りの手順を答えなさい」
    voice "voice/心愛/cca_a1_1617.ogg"
    ai 心愛_水着_基本_真顔 "请回答正确的参拜步骤"

    # 莲 「そんなん簡単だな。二拝二拍手一拝つってな」
    lian "这个简单啊，二拜二拍手一拜"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まず二回お辞儀して、次に二回拍手します。そして、深くお辞儀します」
    show 真冬_水着_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_1298.ogg"
    dong 真冬_水着_基本_目閉じ "先鞠两次躬，然后再拍两次手，最后深深鞠一躬"
    hide 真冬_水着_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「まふまふちゃん正解！　心愛の唇はまふまふちゃんが獲得しまんた！」
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1618.ogg"
    ai 心愛_水着_基本_笑顔 "嘛呼嘛呼酱正解！心爱的嘴唇由嘛呼嘛呼酱获得！"
    hide 心愛_水着_基本_真顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「わーい」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1299.ogg"
    dong 真冬_水着_基本_微笑み "哇——咿"
    hide 真冬_水着_基本_目閉じ

    # 莲 「先に言ったの俺なのに！」
    lian "明明是我先说的！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「相手を殺す時は余計なおしゃべりなどせず、引き金を引くことだ…」
    show 心愛_水着_基本_ゴルゴ at love69_right with dissolve
    voice "voice/心愛/cca_a1_1619.ogg"
    ai 心愛_水着_基本_ゴルゴ "杀人的时候不要多嘴，要扣扳机…（L:反派死于话多，就是这个道理）"
    hide 心愛_水着_基本_笑顔

    # 莲 「殺し屋かお前は」
    lian "你是杀手吗？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「心愛ちゃん…ちゅー」
    hide 真冬_水着_基本_微笑み
    show 真冬_水着_基本_キス:
        zoom 1.5
        xalign 0.13
        yalign -0.09
        linear 0.3 xalign 0.255
    voice "voice/真冬/maf_a1_1300.ogg"
    dong 真冬_水着_基本_キス "心爱酱……啾——"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ちゅー…♪」
    hide 心愛_水着_基本_ゴルゴ
    show 心愛_水着_基本_キス:
        zoom 1.5
        xalign 0.8918
        yalign -0.09
        linear 0.3 xalign 0.7518
    voice "voice/心愛/cca_a1_1620.ogg"
    ai 心愛_水着_基本_キス "啾——……♪"

    # 旁白 「でも、結局後でキスしてもらったみたいっすよ。やったね彼氏くん」
    voice "voice/想瑠/sol_a1_0184a.ogg"
    aside "不过，最后还是kiss了呢，真是太好了，男朋友君"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ヌシカンさん居なかった…」
    # 参考资料：https://www.youtube.com/watch?v=4GglKdpTX6A
    show 心愛_水着_基本_泣き:
        zoom 1.5
        xalign 0.7518
        yalign -0.09
    with dissolve
    voice "voice/心愛/cca_a1_1621.ogg"
    ai 心愛_水着_基本_泣き "天野大也先生不在呢……（L:天野大也是夏威夷出云大社的宫司(神社的最高神官)）"
    hide 心愛_水着_基本_キス

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「アジカンなら居たね」
    show 真冬_水着_基本_無表情:
        zoom 1.5
        xalign 0.255
        yalign -0.09
    with dissolve
    voice "voice/真冬/maf_a1_1301.ogg"
    dong 真冬_水着_基本_無表情 "如果是亚细亚功夫世代的话就在那边（L:ASIAN KUNG-FU GENERATION，1996- ，是日本四人组成的摇滚乐团，以厚重的吉他以及高度抽象的歌词为特征）"
    hide 真冬_水着_基本_キス

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「消してぇえ！」
    show 心愛_水着_基本_驚き:
        zoom 1.5
        xalign 0.7518
        yalign -0.09
    with dissolve
    voice "voice/心愛/cca_a1_1622.ogg"
    ai 心愛_水着_基本_驚き "消失吧！"
    hide 心愛_水着_基本_泣き

    # 场景切换：夏威夷出云大社->夏威夷市内
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene ハワイa with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「もぐもぐもぐもぐ」
    show 心愛_水着_おやつ_もぐもぐ at love69_right with dissolve
    voice "voice/心愛/cca_a1_1623.ogg"
    ai 心愛_水着_おやつ_もぐもぐ "咀嚼咀嚼咀嚼咀嚼"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「もぐもぐもぐもぐ」
    show 真冬_水着_基本_おやつ at love69_left with dissolve
    voice "voice/真冬/maf_a1_1302.ogg"
    dong 真冬_水着_基本_おやつ "咀嚼咀嚼咀嚼咀嚼"

    # 莲 「結局ハワイにきてもキャラメルアップルかよ」
    lian "结果来到夏威夷也还是奶糖苹果啊"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「食べる？」
    show 心愛_水着_おやつ_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1624.ogg"
    ai 心愛_水着_おやつ_笑顔 "要恰吗？"
    hide 心愛_水着_おやつ_もぐもぐ

    # 莲 「食べる」
    lian "恰"

    # 心爱 「あい」
    voice "voice/心愛/cca_a1_1625.ogg"
    ai 心愛_水着_おやつ_笑顔 "给"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene ハワイa with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 旁白 「今度は、シェイブアイス屋さんにやってきたみたいですよ。シェイブアイスのシェイブって何なんすかね？」
    voice "voice/想瑠/sol_a1_0185.ogg"
    aside "这次好像去了Shave Ice店了哦。Shave Ice的Shave是什么呢？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「シェイブアイスとは英語でいう所のかき氷の事を言います」
    show 心愛_水着_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1626.ogg"
    ai 心愛_水着_基本_真顔 "Shave Ice 指的是英语里面所说的刨冰"

    # 旁白 「なるほど」
    voice "voice/想瑠/sol_a1_0186.ogg"
    aside "原来如此"

    # 莲 「誰に話してるんだね」
    lian "你在和谁说话呢？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「真冬ちゃん」
    voice "voice/心愛/cca_a1_1627.ogg"
    ai 心愛_水着_基本_真顔 "真冬酱"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まふ」
    show 真冬_水着_基本_まったり at love69_left with dissolve
    voice "voice/真冬/maf_a1_1303.ogg"
    dong 真冬_水着_基本_まったり "嘛呼"

    # 莲 「そうか…で、どれにすんの？色々フレーバーあるけど…」
    lian "是吗…那么，要选哪一个呢？虽然有各种各样的味道……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「綿菓子かな」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1304.ogg"
    dong 真冬_水着_基本_無表情 "棉花糖吧"
    hide 真冬_水着_基本_まったり

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「じゃぁ私はバブルガム」
    voice "voice/心愛/cca_a1_1628.ogg"
    ai 心愛_水着_基本_真顔 "那么我要泡泡糖"

    # 莲 「また得体の知れないものを…」
    lian "又是莫名其妙的东西呢……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「お兄ちゃんは何にするの？」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1305.ogg"
    dong 真冬_水着_基本_微笑み "欧尼酱要点什么捏？"
    hide 真冬_水着_基本_無表情

    # 莲 「このリヒムイってやつ」
    # 参考资料：https://www.lanilanihawaii.com/column/honto_hawaii/li-hing-mui-is-loved-by-loco.html
    lian "这个叫Li Hing Mui的家伙（L:夏威夷一种口味和外观多种多样的食物，也是一种调味品）"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「名前で選ぶと後悔するよ？」
    voice "voice/心愛/cca_a1_1629.ogg"
    ai 心愛_水着_基本_真顔 "用名字选择的话会后悔的哦？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「プラムを塩でつけた、梅干しみたいな味だよ」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1306.ogg"
    dong 真冬_水着_基本_無表情 "梅子涂上盐，就像梅干一样的味道"
    hide 真冬_水着_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「知ってるのかよぉ！？　負けた…お菓子マスターの私が…！　お菓子マスターの私が！」
    show 心愛_水着_基本_ぶわー at love69_right with dissolve
    voice "voice/心愛/cca_a1_1630.ogg"
    ai 心愛_水着_基本_ぶわー "你原来知道的吗！？我输了…作为点心大师的我…！作为点心大师的我！"
    hide 心愛_水着_基本_真顔

    # 莲 「じゃぁこのピナコラダってやつは？」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%94%E3%83%8B%E3%83%A3%E3%83%BB%E3%82%B3%E3%83%A9%E3%83%BC%E3%83%80
    lian "那这个piña colada是什么（L:凤梨可乐达，是来自西班牙语的词，一款甜鸡尾酒，一般由兰姆酒、椰浆和凤梨汁混合搅拌或者加冰块摇晃调制，通常装饰凤梨角、马拉斯奇诺樱桃或二者兼具。该饮品有两种配方，一般认为均起源于波多黎各）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「カクテルのひとつだね」
    show 真冬_水着_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_1307.ogg"
    dong 真冬_水着_基本_目閉じ "是一种鸡尾酒吧"
    hide 真冬_水着_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「むー…じゃぁ、ピザって１０回言って？」
    show 心愛_水着_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1631.ogg"
    ai 心愛_水着_基本_不機嫌 "呜——…那么，说10次披萨？"
    hide 心愛_水着_基本_ぶわー

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ピザ、ピザ、ピザ、ピザ、ピザ、ピザ、ピザ、ピザ、ピザ、ピザ」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1308.ogg"
    dong 真冬_水着_基本_無表情 "披萨、披萨、披萨、披萨、披萨、披萨、披萨、披萨、披萨、披萨"
    hide 真冬_水着_基本_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「これは？」
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1632.ogg"
    ai 心愛_水着_基本_笑顔 "那这个是？"
    hide 心愛_水着_基本_不機嫌

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ＶＩＳＡ」
    show 真冬_水着_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_1309.ogg"
    dong 真冬_水着_基本_目閉じ "ＶＩＳＡ（L:这是诱导提问233，之前看月曜就有诱导提问熊猫的，有趣的很，xswl）"
    hide 真冬_水着_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「畜生！」
    show 心愛_水着_基本_ぶわー at love69_right with dissolve
    voice "voice/心愛/cca_a1_1633.ogg"
    ai 心愛_水着_基本_ぶわー "可恶！"
    hide 心愛_水着_基本_笑顔

    # 莲 「何か関係あんのかよ！？」
    lian "有什么关系吗！？"

    # 旁白 「で、結局グアバにしちゃったみたいっすよ。冒険とかしないんですかねぇ？」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%B0%E3%82%A2%E3%83%90 グアバ=番石榴
    voice "voice/想瑠/sol_a1_0187.ogg"
    aside "然后，结果好像变成了番石榴。不去冒险吗？（L:番石榴可以指“不好的”或是手榴弹的昵称(形似)）"

    # 莲 「余計なお世話だ！」
    lian "多管闲事！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「グァバを…グアバッ！」
    # 参考资料：https://zh.wikipedia.org/wiki/%E9%97%9C%E5%B3%B6
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1310.ogg"
    dong 真冬_水着_基本_無表情 "番石榴…关岛！（L:谐音梗）"
    hide 真冬_水着_基本_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぶふっ！」
    # L:原作跳错人了啦，这里是心爱跳为啥真冬跳了啊！改！
    hide 心愛_水着_基本_ぶわー
    show 心愛_水着_基本_笑顔:
        zoom 1.5
        xalign 0.8918
        yalign -0.09
        linear 0.15 yalign -0.02
        linear 0.15 yalign -0.09
    voice "voice/心愛/cca_a1_1634.ogg"
    ai 心愛_水着_基本_笑顔 "噗噗！"

    # 莲 「一体それは何だ！」
    lian "那到底是什么啊！"

    # 场景切换：夏威夷市内->近海边
    # 背景音加上海水音 https://www.renpy.cn/doc/audio.html?highlight=music#renpy.music.register_channel
    # https://www.reddit.com/r/vndevs/comments/9a7kit/how_do_i_assign_a_new_audio_channel_to_the_sound/
    # gui.rpy:27

    image bg ハワイf = "images/bg/ハワイf.png"
    play hawaii "voice/effect/02_砂浜に寄せる細かな波.ogg" fadein 2.0
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene ハワイf with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「結局戻って来てしまいました。常夏の…ビーチに…！」
    show 心愛_水着_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1635.ogg"
    ai 心愛_水着_基本_真顔 "结果还是回来了。在常夏的……海滩上…！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「誘惑には勝てないよね」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1311.ogg"
    dong 真冬_水着_基本_無表情 "抵挡不住诱惑吧？"

    # 莲 「まぁ、海に入らなきゃ、なんのための水着だかわからんしな」
    lian "嘛，不进入大海的话，不知道是为了什么而穿的泳衣嘛"

    # 真冬 「そりゃーもちろん、お兄ちゃんを誘惑するためのですよ」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1312.ogg"
    dong 真冬_水着_基本_微笑み "那当然是为了诱惑欧尼酱"
    hide 真冬_水着_基本_無表情

    # 莲 「だとしたら効果は抜群だな」
    lian "那这么说的话效果拔群"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「だがしかし、そのムードに入るにはまだ早いですぞ～！」
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1636.ogg"
    ai 心愛_水着_基本_笑顔 "然而但是，现在要进入那种气氛还太早了呢～！"
    hide 心愛_水着_基本_真顔

    # 旁白 「という事で、ワイキビーチに戻ってきたみたいっすよ。やっぱ好きなんすねぇ。」
    voice "voice/想瑠/sol_a1_0188.ogg"
    aside "那么，好像又回到了Waikiki Beach，果然很喜欢呢"

    # 心爱 「またあったな…デューク…」
    voice "voice/心愛/cca_a1_1637.ogg"
    ai 心愛_水着_基本_笑顔 "又来了…杜克…"

    # 莲 「恨みでもあんのかよ」
    lian "你是和他有仇嘛"

    # 心爱 「あ！　一発ネタ思い付いた！」
    show 心愛_水着_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1638.ogg"
    ai 心愛_水着_基本_嬉しい "啊！我想到了一个段子！"
    hide 心愛_水着_基本_笑顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「どうぞ」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1313.ogg"
    dong 真冬_水着_基本_無表情 "您请"
    hide 真冬_水着_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ココア１３（サーティーン）」
    show 心愛_水着_基本_ゴルゴ at love69_right with dissolve
    voice "voice/心愛/cca_a1_1639.ogg"
    ai 心愛_水着_基本_ゴルゴ "这里是１３（Thirteen）（L:原文「ココア１３」杜克的签名写成假名是13个字，前面的发音和心爱cocoa一样，前面用过这个梗，和core冰核也很像，和可可也是一个音）"
    hide 心愛_水着_基本_嬉しい

    # 莲 「デューク繋がりかよ！　しかもちょろっとさっき使ったじゃねぇか！」
    lian "杜克关联啊！而且之前不是用过吗！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「チョップ」
    # L:音声应该是和scene01一样的，原版估计制作的时候scene01没有这个，是临时加上去的
    hide 真冬_水着_基本_無表情
    show 真冬_水着_基本_目閉じ:
        zoom 1.5
        xalign 0.13
        yalign -0.09
        linear 0.3 xalign 0.507
    voice "voice/真冬/maf_a1_1314.ogg"
    dong 真冬_水着_基本_目閉じ "我劈！（L:开场的时候在教室里两人也这么搞过捏）"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「コアァッ！」
    hide 心愛_水着_基本_ゴルゴ
    show 心愛_水着_基本_ぐるぐる:
        zoom 1.5
        xalign 0.8918
        yalign -0.09
        linear 0.15 yalign -0.02
        linear 0.15 yalign -0.09
    voice "voice/心愛/cca_a1_1640.ogg"
    ai 心愛_水着_基本_ぐるぐる "哇！"

    # 莲 「しかも弱いし」
    lian "这不是很弱嘛"

    # 心爱 「べ、ベッドの上ならつよいぞ…多分…」
    show 心愛_水着_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1641.ogg"
    ai 心愛_水着_基本_泣き "呃，床上的话很厉害…大概…"
    hide 心愛_水着_基本_ぐるぐる

    # 莲 「うるせえ」
    lian "无路赛"

    # 场景切换：近海边->Waikiki Beach
    # 背景音还是有海水音
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene ハワイc with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 心爱 「うーーーーーーー」
    show 心愛_水着_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1642.ogg"
    ai 心愛_水着_基本_真顔 "大——————"

    # 心爱 「みーーーーーーー」
    show 心愛_水着_基本_にっこり at love69_right with dissolve
    voice "voice/心愛/cca_a1_1643.ogg"
    ai 心愛_水着_基本_にっこり "海——————"
    hide 心愛_水着_基本_真顔

    # 心爱 「だーーーーーーー」
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1644.ogg"
    ai 心愛_水着_基本_笑顔 "啊——————"
    hide 心愛_水着_基本_にっこり

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「コナッツを食らえ！」
    show 真冬_水着_基本_ジト目:
        zoom 1.5
        xalign 0.13
        yalign -0.09
        linear 0.15 yalign -0.02
        linear 0.15 yalign -0.09
    with dissolve
    voice "voice/真冬/maf_a1_1315.ogg"
    dong 真冬_水着_基本_ジト目 "恰椰子吧！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 掷物声
    # 心爱向右闪躲！
    play sound "voice/effect/空振り4～ヒュンッ.ogg"

    # 心爱 「遅すぎんだよぉ！」
    hide 心愛_水着_基本_笑顔
    show 心愛_水着_基本_不機嫌:
        zoom 1.5
        xalign 0.8918
        yalign -0.09
        linear 0.3 xalign 1.19
    voice "voice/心愛/cca_a1_1645.ogg"
    ai 心愛_水着_基本_不機嫌 "太慢了！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「じゃぁお兄ちゃん、食らえ！　真冬しゅーと！」
    hide 真冬_水着_基本_ジト目
    show 真冬_水着_基本_微笑み:
        zoom 1.5
        xalign 0.13
        yalign -0.09
        linear 0.15 yalign -0.02
        linear 0.15 yalign -0.09
    voice "voice/真冬/maf_a1_1316.ogg"
    dong 真冬_水着_基本_微笑み "那欧尼酱，恰吧！真冬Shoot！"

    # 莲君闪躲！
    play sound "voice/effect/空振り4～ヒュンッ.ogg"

    # 莲 「やめろ！　毎年、コナッツで頭を打って死ぬ人は、サメに食われて死ぬ人より多いんだぞ！」
    lian "住手！每年因为被椰子砸到脑袋死的人比被鲨鱼吃掉而死的人还多！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「きゃーっち！」
    hide 心愛_水着_基本_不機嫌
    show 心愛_水着_基本_笑顔:
        zoom 1.5
        xalign 1.19
        yalign -0.09
        linear 0.3 xalign 0.8918
    voice "voice/心愛/cca_a1_1646.ogg"
    ai 心愛_水着_基本_笑顔 "Catch！"

    # 心爱 「それをー親指でぇーファイア！」
    # 参考资料：https://www.youtube.com/watch?v=bLZAiKJNWmM
    # 参考资料：https://kyodonewsprwire.jp/release/201308274127
    hide 心愛_水着_基本_笑顔
    show 心愛_水着_基本_覚醒:
        zoom 1.5
        xalign 0.8918
        yalign -0.09
        linear 0.15 yalign -0.02
        linear 0.15 yalign -0.09
    voice "voice/心愛/cca_a1_1647.ogg"
    ai 心愛_水着_基本_覚醒 "这是——大拇指的——Fire！（L:这里玩的是13年的親指戦士的梗，感兴趣的可以搜一下，还有指相撲这样的游戏）"

    # 音效：惊
    play sound "voice/effect/クリティカルヒット2.ogg"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「素手でいった…」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1317.ogg"
    dong 真冬_水着_基本_無表情 "赤手空拳…（L:也该也是玩这个梗，不过我没看过所以不懂，有知道的老哥可以去GitHub提Issues）"
    hide 真冬_水着_基本_微笑み

    # 莲 「ゴールドフィンガーですかね…」
    lian "是金手指吧…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「そしてぇえコナッツ汁を…いただきまーす！」
    show 心愛_水着_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1648.ogg"
    ai 心愛_水着_基本_嬉しい "那么——椰子汁……我开动了！"
    hide 心愛_水着_基本_覚醒

    # 心爱 「ごくっ」
    show 心愛_水着_基本_もぐもぐ at love69_right with dissolve
    voice "voice/心愛/cca_a1_1649.ogg"
    ai 心愛_水着_基本_もぐもぐ "咕"
    hide 心愛_水着_基本_嬉しい

    # 心爱 「……」
    show 心愛_水着_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1650.ogg"
    ai 心愛_水着_基本_真顔 "……"
    hide 心愛_水着_基本_もぐもぐ

    # 心爱 「…ぶふっ」
    hide 心愛_水着_基本_真顔
    show 心愛_水着_基本_ぶわー:
        zoom 1.5
        xalign 0.8918
        yalign -0.09
        linear 0.3 yalign -3.0
    voice "voice/心愛/cca_a1_1651.ogg"
    ai 心愛_水着_基本_ぶわー "……噗欸"
    hide 心愛_水着_基本_ぶわー

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「倒れた」
    voice "voice/真冬/maf_a1_1318.ogg"
    dong 真冬_水着_基本_無表情 "倒下了"

    # 莲 「お、おい、大丈夫か！？」
    lian "喂，喂，没事吧！？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「じぇ、じぇんじぇん甘くにゃい…げろげろ…」
    show 心愛_水着_基本_ぐるぐる:
        zoom 1.5
        xalign 0.8918
        yalign -3.0
        linear 0.3 yalign -0.09
    voice "voice/心愛/cca_a1_1652.ogg"
    ai 心愛_水着_基本_ぐるぐる "完全、完全不甜啊…嘿呜嘿呜…"

    # 莲 「…ごく…ごく…ごく」
    lian "……咕……咕……咕"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「どうかしら」
    voice "voice/真冬/maf_a1_1319.ogg"
    dong 真冬_水着_基本_無表情 "怎么样？"

    # 莲 「…ぶふっ」
    lian "…噗噗"

    # 真冬 「不味いの…？」
    show 真冬_水着_基本_泣き at love69_left with dissolve
    voice "voice/真冬/maf_a1_1320.ogg"
    dong 真冬_水着_基本_泣き "不好喝吗…？"
    hide 真冬_水着_基本_無表情

    # 莲 「コナッツミルクの…コナッツ臭さだけ抽出した味だよ…」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%B3%E3%82%B3%E3%83%8A%E3%83%83%E3%83%84%E3%83%9F%E3%83%AB%E3%82%AF
    lian "这是Coconut milk的……只提取了椰子味的味道……（L:Coconut milk，椰浆，是从成熟的椰子的椰肉中榨出来的奶白色液体，椰浆加糖和水制作饮料才是平时喝的椰奶）"

    # 真冬 「ごく…ごく…ごく…」
    show 真冬_水着_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_1321.ogg"
    dong 真冬_水着_基本_目閉じ "咕……咕……咕"
    hide 真冬_水着_基本_泣き

    # 真冬 「…うん、その通りだけどまぁ、いけるよ」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1322.ogg"
    dong 真冬_水着_基本_無表情 "…嗯，的确如此，不过还是可以的（L:我也不了解，椰子水明明挺好喝的啊，不过椰子水是喝嫩椰子的，老椰子的水没有嫩的好喝，应该只是不习惯吧，或者，有没有一种可能，她们拿的是个坏椰子……）"
    hide 真冬_水着_基本_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「まじかよ…」
    show 心愛_水着_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1653.ogg"
    ai 心愛_水着_基本_真顔 "真的吗…"
    hide 心愛_水着_基本_ぐるぐる

    # 莲 「…えー」
    lian "……哎——"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ごく…はい、ごちそうさま」
    show 真冬_水着_基本_まったり at love69_left with dissolve
    voice "voice/真冬/maf_a1_1323.ogg"
    dong 真冬_水着_基本_まったり "咕…好，谢谢款待"
    hide 真冬_水着_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「やりおる」
    show 心愛_水着_基本_無表情 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1654.ogg"
    ai 心愛_水着_基本_無表情 "真能干"
    hide 心愛_水着_基本_真顔

    # 莲 「あいつ南国系フルーツ好きだからな」
    lian "那家伙喜欢南国水果啊"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まっふまふードライブ！」
    hide 真冬_水着_基本_まったり
    show 真冬_水着_基本_ジト目:
        zoom 1.5
        xalign 0.13
        yalign -0.09
        linear 0.15 yalign -0.02
        linear 0.15 yalign -0.09
    voice "voice/真冬/maf_a1_1324.ogg"
    dong 真冬_水着_基本_ジト目 "嘛呼嘛呼——drive"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「蹴った」
    show 心愛_水着_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1655.ogg"
    ai 心愛_水着_基本_真顔 "踢出去了"
    hide 心愛_水着_基本_無表情

    # 场景切换：Waikiki Beach->近海边
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene ハワイf with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 旁白 「海に入って遊ぶみたいっすよ」
    voice "voice/想瑠/sol_a1_0189.ogg"
    aside "好像是在海里玩呢"

    # 切换到开场02！标志性的一幕！一周目就快Over啦！！！
    # 这里雀食就不需要加头像了，如果有的话就ATL粗去！！
    # 写脚本的时居然候不知道当时的自己在上面写的是啥意思了233

    image bg 水着cgゲーム用 = "images/ev/水着cgゲーム用.png"
    scene 水着cgゲーム用 with dissolve

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「わはーい！　海底がみえるよー！」
    voice "voice/心愛/cca_a1_1656.ogg"
    ai 心愛_水着_基本_笑顔 "哇哈！可以看到海底哦！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ほら、お兄ちゃん。さっさと水に入っちゃいなさいよ」
    voice "voice/真冬/maf_a1_1325.ogg"
    dong 真冬_水着_基本_微笑み "喂，欧尼酱，快来下水啊（L:RA3直美“何不下水与我同乐”既视感）"

    # 莲 「おれは…今砂浜の感触を確かめている…」
    lian "我…现在正在确认沙滩的触感…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「せぇい！」
    voice "voice/心愛/cca_a1_1657.ogg"
    ai 心愛_水着_基本_驚き "哈！"

    # nil 「バシャァッ！」
    "啪嗒！"

    # 莲 「ぎゃあ！　塩水がァ！」
    lian "呀！盐水啊！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「沈めェ！」
    voice "voice/真冬/maf_a1_1326.ogg"
    dong 真冬_水着_基本_ジト目 "沉下去！"

    # 莲 「ぶおあっ！　やめろ！　俺は水中で呼吸できないんだぞ！」
    lian "呜啊！住手！我在水中没法呼吸啊！"

    # 真冬 「誰にもできないよそんな事」
    voice "voice/真冬/maf_a1_1327.ogg"
    dong 真冬_水着_基本_無表情 "这种事情谁也做不到啊"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「私はできるよ？　ほら！」
    voice "voice/心愛/cca_a1_1658.ogg"
    ai 心愛_水着_基本_真顔 "我可以的哦？你看！"

    # 心爱 「ぷー…」
    voice "voice/心愛/cca_a1_1659.ogg"
    ai 心愛_水着_基本_笑顔 "噗——……"

    # 心爱 「ね」
    voice "voice/心愛/cca_a1_1660.ogg"
    ai 心愛_水着_基本_にっこり "呐"

    # 莲 「息を吐いてるだけじゃないか！」
    lian "你这不只是在吐气吗！"

    # 心爱 「うるせぇー！」
    voice "voice/心愛/cca_a1_1661.ogg"
    ai 心愛_水着_基本_驚き "无路赛——！"

    # nil 「バシャァッ！」
    "啪叽！"

    # 莲 「ぎゃあ！　温水（ぬくみず）がァ！」
    # 括号里面是假名，不需要翻译
    lian "啊！温水啊！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「お、ほらほら、心愛ちゃん、お兄ちゃん、お魚さんが泳いでいるよ。えーっと…クマノミだよね、これ」
    voice "voice/真冬/maf_a1_1328.ogg"
    dong 真冬_水着_基本_微笑み "喂，快看快看，心爱酱，欧尼酱，鱼在游泳哦。那个，小丑鱼吧，这个"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「とっつかまえて糧にしよう」
    ## 这里原作没有表情，让我整个活
    voice "voice/心愛/cca_a1_1662.ogg"
    ai 心愛_水着_基本_ペコちゃん "赶紧抓起来做了恰了吧"

    # 莲 「野生児かお前は！　ていうか海のアイドルになんてことを！」
    lian "你是野生的孩子吗！你想对海洋偶像做什么！"

    # 心爱 「せいっ！　っちぃ…意外と素早いね！」
    ## 整活继续
    voice "voice/心愛/cca_a1_1663.ogg"
    ai 心愛_水着_基本_ゴルゴ "嘿！切……意外的很敏捷啊！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「よいしょ。お、捕まえたよ、イソギンチャク」
    voice "voice/真冬/maf_a1_1329.ogg"
    dong 真冬_水着_基本_無表情 "嘿咻。我抓住了哦，海葵"

    # 莲 「元からうごかねぇよ！　可哀想だから返してあげなさい」
    lian "它本来就不动啊！太可怜了，丢回去吧"

    # 真冬 「はい。ばいばい、ルガール」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%AB%E3%82%AC%E3%83%BC%E3%83%AB%E3%83%BB%E3%83%90%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A5%E3%82%BF%E3%82%A4%E3%83%B3
    # 参考资料：https://bgm.tv/character/64372
    voice "voice/真冬/maf_a1_1330.ogg"
    dong 真冬_水着_基本_目閉じ "好，拜拜，Rugal（L: 卢卡尔，SNK的拳皇系列中出现的虚构人物，最早出现在拳皇94）"

    # 莲 「なんて名前つけてるんだ」
    lian "为什么要给它取名字呢？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「私もギースが欲しい！」
    voice "voice/心愛/cca_a1_1664.ogg"
    ai 心愛_水着_基本_笑顔 "我也想要Geese！（L:吉斯，SNK的饿狼传说系列中出现的虚构人物，最早出现饿狼传说(一代,1991)）"

    # 莲 「なんでいちいち強そうで悪そうな名前つけるんだよ」
    lian "为什么每个都要起一个看上去很强大很坏的名字呢？"

    # 心爱 「レイジングストーーーーーム！」
    voice "voice/心愛/cca_a1_1665.ogg"
    ai 心愛_水着_基本_にっこり "RAZING STORM！（L:2009年万代南梦宫的街机光枪射击游戏）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ジェノサーイド・カッタァー！」
    # 参考资料：https://w.atwiki.jp/niconicomugen/pages/88.html
    voice "voice/真冬/maf_a1_1331.ogg"
    dong 真冬_水着_基本_ジト目 "Genocide·cutter！（L:前面真冬提到的卢卡尔的象征必杀技）"

    # nil 「バシャァッ！」
    "啪嗒！"

    # 莲 「ぐわあ！っていつも通りじゃないかよ！」
    lian "呜哇！这不是和普通攻击一样的嘛！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「来いよヤマザキ！」
    # 参考资料:https://ja.wikipedia.org/wiki/%E5%B1%B1%E5%B4%8E%E7%AB%9C%E4%BA%8C
    voice "voice/心愛/cca_a1_1666.ogg"
    ai 心愛_水着_基本_真顔 "来吧山崎！（L:指山崎龙二，“饿狼传说系列”与“拳皇系列”中的出场的虚构角色）"

    # 莲 「違うのがいです」
    lian "这不是一回事啊"

    # nil 「……」
    "……"

    # 心爱 「そういえば、イソギンチャクってなんなんだろうね」
    voice "voice/心愛/cca_a1_1667.ogg"
    ai 心愛_水着_基本_真顔 "这么说来，海葵到底是什么呢？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「珊瑚の仲間で、柔らかい無脊椎動物だよ。動かないと思われがちだけど、素早く動く種類も存在するんだよ」
    voice "voice/真冬/maf_a1_1332.ogg"
    dong 真冬_水着_基本_無表情 "是珊瑚的同类，是柔软的无脊椎动物。虽然经常被认为不会动，但是也有快速移动的种类"

    # 莲 「珊瑚なのかよ、詳しいな。イソギンチャク博士かよ」
    lian "是珊瑚吗？你知道的真多，你是海葵博士吗？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「いや、博士は私だ」
    voice "voice/心愛/cca_a1_1668.ogg"
    ai 心愛_水着_基本_真顔 "不，博士是我"

    # 莲 「そうか」
    lian "是吗"

    # 场景切换回沙滩
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene ハワイc with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 心爱 「ご飯にしましょう」
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1669.ogg"
    ai 心愛_水着_基本_笑顔 "去恰饭吧"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そうしましょう」
    show 真冬_水着_基本_まったり at love69_left with dissolve
    voice "voice/真冬/maf_a1_1333.ogg"
    dong 真冬_水着_基本_まったり "就这么办吧"

    # 莲 「あいよ。買って来るわ。何がい？」
    lian "好，我去买回来，你们想恰什么"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「イカ焼き」
    show 心愛_水着_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1670.ogg"
    ai 心愛_水着_基本_真顔 "烤鱿鱼"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「焼きそば」
    # 参考资料：https://zh.wikipedia.org/wiki/%E6%97%A5%E5%BC%8F%E7%82%92%E9%BA%B5
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1334.ogg"
    dong 真冬_水着_基本_無表情 "日式炒面（L:是日本的一种面食，其做法是将中华面和猪肉等肉类及卷心菜、胡萝卜、洋葱、豆芽等蔬菜类食物炒制而成。日式炒面一般多使用辣酱油调味，但近年来也有不少使用盐来调味的做法）"
    hide 真冬_水着_基本_まったり

    # 莲 「ハワイに有りそうなもんにしてくんねぇかな」
    lian "不整点儿像是在夏威夷才能恰的东西嘛"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene ハワイc with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「ごめん、パンケーキしかなかった」
    lian "对不起，只有薄煎饼"

    # L:又是人物框被盖住了捏，而且是写错地方了

    # 心爱&真冬 「『Change！』」
    ## L:“暗黑旅游”，不满意的时候也是这句捏
    show 真冬_水着_基本_無表情 at love69_left
    show 心愛_水着_基本_笑顔 at love69_right
    with dissolve
    voice "voice/真冬/maf_a1_1335.ogg"
    ai_dong 真冬_水着_基本_無表情 "『Change！』"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene ハワイc with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「イカ焼きと焼きそばは売ってました」
    lian "鱿鱼和日式炒面买回来了"

    # 旁白 「売ってました」
    voice "voice/想瑠/sol_a1_0189a.ogg"
    aside "买回来了捏"

    # 旁白 「パンケーキは蓮君が美味しく頂きました」
    voice "voice/想瑠/sol_a1_0189b.ogg"
    aside "莲君恰了薄煎饼而且觉得挺好吃"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene ハワイc with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「もうちょっと右ー！　もうちょっと左－！　はいまっすぐー！」
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1672.ogg"
    ai 心愛_水着_基本_笑顔 "再往右一点——！再往左一点——！就是现在——！"

    # 旁白 「スイカ割りをしてるみたいっすね」
    voice "voice/想瑠/sol_a1_0190.ogg"
    aside "好像在打西瓜呢"

    # 旁白 「でもスイカはなかったので、蓮君が砂に埋まってるっぽいすねぇ」
    voice "voice/想瑠/sol_a1_0191.ogg"
    aside "但是没有西瓜，莲君好像被埋在沙子里了呢"

    # 旁白 「いザマです」
    voice "voice/想瑠/sol_a1_0192.ogg"
    aside "这不大妙"

    # 莲 「おいうるせえぞナレーション！」
    lian "喂闭嘴旁白！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「はいはーい、お兄ちゃん動かないでねー」
    show 真冬_水着_基本_ジト目 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1336.ogg"
    dong 真冬_水着_基本_ジト目 "好~好——欧尼酱不要动啊"

    # 莲 「やめろー！　動かないどころか動けないんだから！」
    lian "住手！别说动了，完全动不了啊！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「いよいよー！　そのまあと前に三歩！　はい七時の方向に回頭！」
    voice "voice/心愛/cca_a1_1673.ogg"
    ai 心愛_水着_基本_笑顔 "好了好了——！再往前走三步！好，朝七点钟方向回头！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「んしょ…よいしょ…こかな…こからお兄ちゃんの気配がする…」
    show 真冬_水着_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_1337.ogg"
    dong 真冬_水着_基本_目閉じ "…嘿咻…嘿咻…这里…好像有欧尼酱的气息…"
    hide 真冬_水着_基本_ジト目

    # 莲 「ストーップストーップ！」
    lian "Stop！Stop！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「よーし！　まふまふちゃーん！　そっこだぁ！」
    show 心愛_水着_基本_にっこり at love69_right with dissolve
    voice "voice/心愛/cca_a1_1674.ogg"
    ai 心愛_水着_基本_にっこり "好——！嘛呼嘛呼酱！就是这里！"
    hide 心愛_水着_基本_笑顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「いっくよー」
    hide 真冬_水着_基本_目閉じ
    show 真冬_水着_基本_微笑み:
        zoom 1.5
        xalign 0.13
        yalign -0.09
        linear 0.1 xalign 0.3385 yalign 0.02
        linear 0.1 xalign 0.507 yalign -0.09
    voice "voice/真冬/maf_a1_1338.ogg"
    dong 真冬_水着_基本_微笑み "要上了哦——"

    # 莲 「アイエ！」
    lian "呀！"

    # 命中！
    play sound "voice/effect/なぐる3～バンッ.ogg"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぶへぇっ！」
    show 心愛_水着_基本_ぐるぐる at love69_right with dissolve
    voice "voice/心愛/cca_a1_1675.ogg"
    ai 心愛_水着_基本_ぐるぐる "咕欸！"
    hide 心愛_水着_基本_にっこり

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「あっ」
    show 真冬_水着_基本_無表情:
        zoom 1.5
        xalign 0.507
        yalign -0.09
    with dissolve
    voice "voice/真冬/maf_a1_1339.ogg"
    dong 真冬_水着_基本_無表情 "啊"
    hide 真冬_水着_基本_微笑み

    # 莲 「…なんで心愛を殴るんだよ」
    lian "…为什么打中心爱了啊"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「……」
    show 心愛_水着_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1676.ogg"
    ai 心愛_水着_基本_不機嫌 "……"
    hide 心愛_水着_基本_ぐるぐる

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱A 「にょきっ」
    # 14nm++++++++++++ 人物表++++++++++++++
    # 参考资料：https://dictionary.goo.ne.jp/word/en/%E3%81%AB%E3%82%87%E3%81%8D%E3%81%A3/
    show 心愛A_水着_基本_笑顔:
        zoom 1.5
        xalign 0.155
        yalign -1.0
        linear 0.15 yalign -0.09
    with dissolve
    voice "voice/心愛/cca_a1_1677.ogg"
    aia 心愛A_水着_基本_笑顔 "我冒"

    # 心爱酱在最左的参数
    transform love69_xinai_leftest:
        zoom 1.5
        xalign -0.142
        yalign -0.09

    # 心爱B 「にょきっょきっ」
    # 14nm++++++++++++ 人物表++++++++++++++
    show 心愛B_水着_基本_笑顔:
        zoom 1.5
        xalign -0.142
        yalign -1.0
        linear 0.15 yalign -0.09
    with dissolve
    voice "voice/心愛/cca_a1_1678.ogg"
    aib 心愛B_水着_基本_笑顔 "我冒我冒"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「増えた」
    voice "voice/真冬/maf_a1_1340.ogg"
    dong 真冬_水着_基本_無表情 "增加了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱AB 「『おっす』」
    # 14nm++++++++++++ 人物表++++++++++++++
    # 参考资料：https://kotobank.jp/word/%E3%81%8A%E3%81%A3%E3%81%99-220729
    show 心愛AB_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1679.ogg"
    play xinaiab "voice/心愛/cca_a1_1680.ogg"
    aiab 心愛AB_水着_基本_笑顔 "『在这里』"
    hide 心愛_水着_基本_不機嫌

    # 莲 「ハウス」
    lian "House（L:这里我没get到捏……应该是让心爱AB回去吧）"

    # 心爱AB 「『あい』」
    # 14nm++++++++++++ 人物表++++++++++++++
    voice "voice/心愛/cca_a1_1681.ogg"
    play xinaiab "voice/心愛/cca_a1_1682.ogg"
    aiab 心愛AB_水着_基本_笑顔 "『欸』"

    # 心爱AB依次消失
    hide 心愛A_水着_基本_笑顔 with dissolve
    hide 心愛B_水着_基本_笑顔 with dissolve

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「戻った」
    voice "voice/真冬/maf_a1_1341.ogg"
    dong 真冬_水着_基本_無表情 "回去了"

    # 场景切换：Waikiki Beach->岸边步道
    image bg = "images/bg/ハワイd.png"
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene ハワイd with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 旁白 「気づいたら、太陽が黄金色になっちまいましたね」
    voice "voice/想瑠/sol_a1_0193.ogg"
    aside "回过神来，太阳已经变成金黄色了"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ふー…海水浴なんて実は何年ぶりって感じだったね」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1342.ogg"
    dong 真冬_水着_基本_微笑み "嗯啊——都不知道海水浴是哪年的感觉了"

    # 莲 「成長するといかねぇからなぁ…」
    lian "长大了就⑧行了呢……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ねー。あーん、名残惜しいけど、他の所も回らなきゃー！」
    show 心愛_水着_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1683.ogg"
    ai 心愛_水着_基本_泣き "欸——哈啊——虽然有点舍不得，但是其他地方也要去转转啊！"

    # 莲 「ていうか、海から上がったのに水着なの？」
    lian "话说，都从海里上来了还是穿着泳衣吗？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「今日は終日、水着ーな心愛と真冬でーす」
    voice "voice/真冬/maf_a1_1343.ogg"
    dong 真冬_水着_基本_微笑み "今天一整天，都是穿着泳衣的心爱和真冬"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「勿論蓮くんの、貸し切りだよん♪」
    show 心愛_水着_基本_にっこり at love69_right with dissolve
    voice "voice/心愛/cca_a1_1684.ogg"
    ai 心愛_水着_基本_にっこり "当然是莲君的包场啦♪"
    hide 心愛_水着_基本_泣き

    # 莲 「よし…じゃぁあれだな、予てからの、式場探しといくか」
    lian "好吧……那么，我们先去找婚礼会场吧"

    # 心爱 「わーい！」
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1685.ogg"
    ai 心愛_水着_基本_笑顔 "哇——咿！"
    hide 心愛_水着_基本_にっこり

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うん！　楽しみ！」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1344.ogg"
    dong 真冬_水着_基本_無表情 "嗯！好期待！"
    hide 真冬_水着_基本_微笑み

    stop hawaii fadeout 2.0

    # 场景切换到私人海滩教堂
    image bg ハワイ_チャペル = "images/bg/ハワイ_チャペル.png"
    scene ハワイ_チャペル with dissolve

    # 旁白 「つーことで、プライベートビーチを併設してるっつーチャペルにやってきたみたいっすよ」
    voice "voice/想瑠/sol_a1_0194.ogg"
    aside "话说回来，好像找到了一个附设私人海滩的教堂哦"

    # 旁白 「ステンドグラスの代わりに、巨大なクリアガラスで、その向こう側に海…だなんてロマンチックすねぇ」
    voice "voice/想瑠/sol_a1_0195.ogg"
    aside "用巨大的玻璃代替彩色玻璃，在那对面就是大海…这是多么的浪漫啊"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「わはー☆　蓮くん、このビーチ欲しい！　あと椰子の木とベンチ！」
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1686.ogg"
    ai 心愛_水着_基本_笑顔 "哇哈哈~☆莲君，我想要这个海滩！还有椰子树和长椅！"

    # 莲 「少しは考えて物を言えよ！　脊髄任せか！」
    # 参考资料：https://dictionary.goo.ne.jp/word/%E4%BB%BB%E3%81%9B%E3%82%8B/
    lian "稍微考虑一下再说吧！脊髓就交给你了！"

    # 心爱 「月の土地は買える世の中なのに…」
    # 参考资料：https://www.ielove.co.jp/column/contents/03177/
    # 购买月球土地：https://lunarembassy.com/product/buy-land-on-the-moon/
    voice "voice/心愛/cca_a1_1687.ogg"
    ai 心愛_水着_基本_笑顔 "明明是可以买到月球土地的社会……（L:月球土地还真可以买？！查了一下，在The Lunar Embassy.LLC，$24.99 – $499.80一亩，我大为震惊，不过正经说，应该还是干不过国际公约和共识）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「私はトロピカルジュースかな」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1345.ogg"
    dong 真冬_水着_基本_無表情 "我想要一杯热带果汁"

    # 莲 「お前はもう少し欲しがれよ。ていうか、そんなにトロピカルジュース好きなんか。初めて知ったぞ」
    lian "你还想要啊。话说回来，我还是第一次知道你这么喜欢热带果汁"

    # 真冬 「グラスにお花をさすのは夢でした…ハングオーバーが全米ナンバーワンになった日から憧れてました」
    voice "voice/真冬/maf_a1_1346.ogg"
    dong 真冬_水着_基本_無表情 "把花插在玻璃杯里是我的梦想……从『The Hangover』成为美国第一的那天起（L:《宿醉》，2009-06-05，一部发生在赌城拉斯维加斯的喜剧电影，美国金球奖音乐喜剧类最佳影片）"

    # 莲 「そんなシーンあったっけ？」
    lian "有那样的场景吗？"

    # 真冬 「２本目でね」
    voice "voice/真冬/maf_a1_1347.ogg"
    dong 真冬_水着_基本_無表情 "Part II吧（L:The Hangover Part II，《宿醉2》，2011-05-26，和《宿醉》一样，都是以一场婚礼开始）"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ほらほら、蓮くん！　真冬ちゃん　こっちこっち！」
    voice "voice/心愛/cca_a1_1688.ogg"
    ai 心愛_水着_基本_笑顔 "快看快看，莲君！真冬酱！这边这边！"

    # 旁白 「心愛ちゃんが、何か見つけたみたいっすよ。二人の手を引っ張って教会の奥へと連れていっちゃいましたねぇ」
    voice "voice/想瑠/sol_a1_0196.ogg"
    aside "心爱酱好像找到了什么。牵着两个人的手带去了教堂的深处"

    # 心爱 「ね！　ね！　すごいでしょ！！」
    voice "voice/心愛/cca_a1_1689.ogg"
    ai 心愛_水着_基本_笑顔 "呐！呐！很厉害吧！！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「わ…ほんとだ、すごい…綺麗だねー」
    voice "voice/真冬/maf_a1_1348.ogg"
    dong 真冬_水着_基本_無表情 "哇…真的，好厉害…好漂亮啊"

    # 莲 「おー…流石、ハワイだな…」
    lian "哎……不愧是，夏威夷啊……"

    # 旁白 「お、これは確かに凄い眺めっすねぇ」
    voice "voice/想瑠/sol_a1_0197.ogg"
    aside "哦，这的确是很厉害的风景呢"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「海を眺めながら…永遠の愛を誓い合う…きゃぅ～…素敵ぃ…ふにゃー」
    show 心愛_水着_基本_キス at love69_right with dissolve
    voice "voice/心愛/cca_a1_1690.ogg"
    ai 心愛_水着_基本_キス "一边眺望大海……一边发誓永远的爱……呀呜……太棒了……呜喵——"
    hide 心愛_水着_基本_笑顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ん…本当にこで式を挙げれるかはわからないけど…すっごく楽しみ…」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1349.ogg"
    dong 真冬_水着_基本_微笑み "嗯…真的不知道能不能在这里举行仪式…非常期待…"
    hide 真冬_水着_基本_無表情

    # 莲 「…むしろ、今…誓ってもいけどな…」
    lian "倒不如说，现在…发誓也没关系…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「！！！」
    show 心愛_水着_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1691.ogg"
    ai 心愛_水着_基本_驚き "！！！"
    hide 心愛_水着_基本_キス

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ちょ…っと！？」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1350.ogg"
    dong 真冬_水着_基本_無表情 "等……一下！？"
    hide 真冬_水着_基本_微笑み

    # 莲 「えっ！？　なんでお前らそんな反応すんの！？」
    lian "诶！？你们为什么做出这样的反应？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ま、まさか…蓮君から言いだしてくれるとは…ふ、不覚をとられたにゃ…」
    voice "voice/心愛/cca_a1_1692.ogg"
    ai 心愛_水着_基本_驚き "真、真没想到…莲君会主动提出来……呜，我失神了喵…"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「恋人になってから、その辺のセンサー鈍ってると思ってたけど…」
    show 真冬_水着_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_1351.ogg"
    dong 真冬_水着_基本_目閉じ "我还以为成为恋人后，这方面的传感器就变钝了呢……"
    hide 真冬_水着_基本_無表情

    # 莲 「散々な言いようだな。　お前らが望んでる事ぐらいわかるつもりだ…まぁ、ちょっと改まると恥ずかしいけどな」
    lian "这话说得太离谱了。我想我至少还是明白你们想要什么的……嘛，不过和我想的稍微不同就尴尬了"

    # 真冬 「責任はとってもらいますよー？」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1352.ogg"
    dong 真冬_水着_基本_微笑み "你会负起责任的吧——？"
    hide 真冬_水着_基本_目閉じ

    # 莲 「お、おう…」
    lian "嗯，嗯……"

    # 旁白 「おやおや、これはこれは大変な事になりましたねぇ」
    voice "voice/想瑠/sol_a1_0197-8.ogg"
    aside "哎呀哎呀，这可不得了啊"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「むあ…でも、神父さん役が居ないね」
    show 心愛_水着_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1693.ogg"
    ai 心愛_水着_基本_泣き "啊…但是，没有神父的角色呢"
    hide 心愛_水着_基本_驚き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「それには心配を及ばないよ。ね？」
    voice "voice/真冬/maf_a1_1353.ogg"
    dong 真冬_水着_基本_微笑み "这个就不用担心了。对吧？"

    # 旁白 「しょうがないっすねぇ。じゃぁほら、台の前に並んで下さいよ」
    voice "voice/想瑠/sol_a1_0198.ogg"
    aside "真是没办法啊。那么，请到台子前面排队吧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「なーいす！　ありがとー！」
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1694.ogg"
    ai 心愛_水着_基本_笑顔 "Nice——！谢谢！"
    hide 心愛_水着_基本_泣き

    # 莲 「あ、有りか、そんなの」
    lian "啊，有吗？这样啊"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「はいはい、お兄ちゃんはこっち、心愛ちゃんはこっち」
    voice "voice/真冬/maf_a1_1354.ogg"
    dong 真冬_水着_基本_微笑み "来来，欧尼酱站这里，心爱酱在这里"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「えへへ…どきどきどきどき…」
    show 心愛_水着_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1695.ogg"
    ai 心愛_水着_基本_嬉しい "欸嘿嘿……dokidoki~dokidoki……"
    hide 心愛_水着_基本_笑顔

    # 莲 「ウエディングドレスじゃないけど…」
    lian "虽然不是婚礼礼服…"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「水着の方が、ハワイっぽくていと思うよ」
    voice "voice/真冬/maf_a1_1355.ogg"
    dong 真冬_水着_基本_微笑み "我觉得泳衣更符合夏威夷哦"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「うんっ！　さぁ…始めて下さいな！」
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1696.ogg"
    ai 心愛_水着_基本_笑顔 "嗯！来吧…请开始吧！"
    hide 心愛_水着_基本_嬉しい

    # 旁白 「えー…こほん。汝、あなたはこの二人を、健やかなる時も、病める時も、富める時も貧しい時も良い時も悪い時も、愛し合い、敬い、慰め助けて変わる事なく愛する事を誓いますか？」
    voice "voice/想瑠/sol_a1_0199.ogg"
    aside "额…咳咳。你发誓，你要爱这两个人，无论是健康的时候、生病的时候、富裕的时候、贫穷的时候、好的时候、坏的时候，相爱、尊敬、安慰、帮助她们，永不改变"

    # 莲 「…ち、誓います」
    lian "……我，我发誓"

    # 旁白 「はい。汝ら、あなた方はこの男性を…まぁ色々大変な事もありますが、二人で仲良く、ずっと一緒に愛する事を誓いますか？」
    voice "voice/想瑠/sol_a1_0200.ogg"
    aside "好。你……你们对这个男人……虽然也有各种各样的困难，但你们发誓要两个人好好相处，永远在一起爱他吗？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 这里也是只写了真冬，原作，⑧行！
    # 心爱&真冬 「『誓いまーす！』」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1356.ogg"
    ai_dong 真冬_水着_基本_無表情 "『我发誓！』"
    hide 真冬_水着_基本_微笑み

    # 莲 「なんか適当だったな…」
    lian "好像很合适呢…"

    # 旁白 「では、誓いのキスをどうぞ」
    voice "voice/想瑠/sol_a1_0201.ogg"
    aside "那么，请交换誓言之吻"

    # 莲 「二人とも、愛してるよ」
    lian "我爱你们两个"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ん…わたしも」
    show 心愛_水着_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1698.ogg"
    ai 心愛_水着_基本_嬉しい "嗯…我也是"
    hide 心愛_水着_基本_笑顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「はぁい、お兄ちゃん…」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1357.ogg"
    dong 真冬_水着_基本_微笑み "好，欧尼酱……"
    hide 真冬_水着_基本_無表情

    # 心爱&真冬 「『ちゅっ』」
    show 真冬_水着_基本_キス at love69_left
    show 心愛_水着_基本_キス at love69_right
    with dissolve
    voice "voice/真冬/maf_a1_1358.ogg"
    ai_dong 真冬_水着_基本_キス "『啾』"
    hide 真冬_水着_基本_微笑み
    hide 心愛_水着_基本_嬉しい

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「えへへへ…もらっちゃった…誓いの…キス…」
    show 心愛_水着_基本_にっこり at love69_right with dissolve
    voice "voice/心愛/cca_a1_1700.ogg"
    ai 心愛_水着_基本_にっこり "欸嘿嘿……我收到了……誓言的…Kiss……"
    hide 心愛_水着_基本_キス

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「キスは何回もしてるけど…やっぱり、こういうのは嬉しいね。ありがとう、お兄ちゃん」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1359.ogg"
    dong 真冬_水着_基本_微笑み "虽然接吻过很多次…果然，这样的很开心啊。谢谢你，欧尼酱"
    hide 真冬_水着_基本_キス

    # 莲 「改まられてもな…まぁ、なんとか幸せにするよ」
    lian "就算被改变了…嘛，我也要设法让你们幸福"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「うん！　一緒に支えあって生きていこうね！」
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1701.ogg"
    ai 心愛_水着_基本_笑顔 "嗯！一起支持着活下去吧！"
    hide 心愛_水着_基本_にっこり

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「さて…次は、私と心愛ちゃんの結婚式しましょうか」
    voice "voice/真冬/maf_a1_1360.ogg"
    dong 真冬_水着_基本_微笑み "那么…接下来是我和心爱酱的婚礼吧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「おー！　じゃぁもっかいおねがいしまーす！」
    voice "voice/心愛/cca_a1_1702.ogg"
    ai 心愛_水着_基本_笑顔 "哦！那就拜托你了！"

    # 旁白 「えー。彼氏にやってもらってもらってもいっすかねぇ？」
    voice "voice/想瑠/sol_a1_0202.ogg"
    aside "欸——这个交给男朋友做也可以的吧？"

    # 心爱 「蓮君は写真撮る人です！」
    show 心愛_水着_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1703.ogg"
    ai 心愛_水着_基本_嬉しい "莲君是摄影师！"
    hide 心愛_水着_基本_笑顔

    # 莲 「ええ！？」
    lian "诶诶！？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「使っていから」
    show 真冬_水着_基本_ジト目 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1361.ogg"
    dong 真冬_水着_基本_ジト目 "我正用着呢"
    hide 真冬_水着_基本_微笑み

    # 莲 「何にだよ！」
    lian "什么啊！"

    # 真冬 「言わせるつもり？」
    show 真冬_水着_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_1362.ogg"
    dong 真冬_水着_基本_目閉じ "你想让我说出来吗？"
    hide 真冬_水着_基本_ジト目

    # 莲 「…わかった、じゃぁお願いします」
    lian "我知道了，那就拜托你了"

    # 旁白 「まったく世話がやけるバカップルっすねぇ」
    voice "voice/想瑠/sol_a1_0203.ogg"
    aside "真是会照顾人的笨蛋CP呢"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene ハワイ_チャペル with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「べ、ベロチューされた…」
    show 心愛_水着_基本_キス at love69_right with dissolve
    voice "voice/心愛/cca_a1_1704.ogg"
    ai 心愛_水着_基本_キス "被、被湿吻了……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ごちそうさまでした」
    show 真冬_水着_基本_まったり at love69_left with dissolve
    voice "voice/真冬/maf_a1_1363.ogg"
    dong 真冬_水着_基本_まったり "谢谢款待"
    hide 真冬_水着_基本_目閉じ

    # 莲 「撮りまんた」
    lian "拍下来了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ネガを渡せ。さもなくばこの女の唇を奪うぞ」
    show 心愛_水着_基本_覚醒 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1705.ogg"
    ai 心愛_水着_基本_覚醒 "把底片给我，不然我就把这个女的的嘴唇夺走"
    hide 心愛_水着_基本_キス

    # 莲 「すきにしろよ」
    lian "随你喜欢吧"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「じゃぁいただきまーす！」
    hide 真冬_水着_基本_まったり
    show 真冬_水着_基本_微笑み:
        zoom 1.5
        xalign 0.13
        yalign -0.09
        linear 0.3 xalign 0.507
    voice "voice/真冬/maf_a1_1364.ogg"
    dong 真冬_水着_基本_微笑み "那我就开动了——！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「んぅう！？　ちゅぅうっ…んっ…んぅ…んちゅぅ…」
    show 心愛_水着_基本_キス at love69_right with dissolve
    voice "voice/心愛/cca_a1_1706.ogg"
    ai 心愛_水着_基本_キス "嗯呜！？嗯呜……嗯……嗯啾……"
    hide 心愛_水着_基本_覚醒

    # 莲 「奪われとるやんけ」
    lian "被抢走了"

    # 场景切换出来
    # BGM停
    stop music fadeout 3.0
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene ハワイd with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 旁白 「それからというもの、お三方は、まったりイチャイチャムードに入っちゃったので、こでをMC蓮くんにお返しまーす」
    # 参考资料：MC https://ja.wikipedia.org/wiki/MC
    voice "voice/想瑠/sol_a1_0204.ogg"
    aside "在那之后，三位就一直沉浸在一种悠闲的无拘无束的气氛中，所以我把MC还给了莲君（L:MC在这里指主持人、司仪）"

    # 莲 「お疲れ様でした」
    lian "辛苦了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ばいばーい！」
    show 心愛_水着_基本_にっこり at love69_right with dissolve
    voice "voice/心愛/cca_a1_1707.ogg"
    ai 心愛_水着_基本_にっこり "Bye——Bye！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「またね」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1365.ogg"
    dong 真冬_水着_基本_微笑み "再会啦"

    # 莲 「また…？　まぁいか」
    lian "再……？不管了"

    # BGM上
    play music bgmthirtyseven fadein 8.0

    # nil 「結婚式の真似事を終えて、俺達はビーチに座ってオレンジ色の巨大な太陽が沈む海を眺めていた。」
    "婚礼的仿真结束后，我们坐在沙滩上眺望着橙色的巨大太阳西沉的大海"

    # nil 「流石は真夏のハワイ。夕方でも全く寒くない。」
    "不愧是盛夏的夏威夷。傍晚也完全不冷"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ん…」
    show 真冬_水着_基本_まったり at love69_left with dissolve
    voice "voice/真冬/maf_a1_1366.ogg"
    dong 真冬_水着_基本_まったり "嗯…"
    hide 真冬_水着_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「にゃー…」
    show 心愛_水着_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1708.ogg"
    ai 心愛_水着_基本_嬉しい "喵——……"
    hide 心愛_水着_基本_にっこり

    # 莲 「……」
    lian "……"

    # nil 「真冬は右隣、心愛は左隣で、俺を挟んでぴったりと肩を寄せ合っている。」
    "真冬在右边，心爱在左边，夹着我紧紧地靠在一起"

    # nil 「結構な距離を歩いたし、はしゃぎまくったので、流石に疲れたのだろう。」
    "走了相当远的距离，又闹得天翻地覆，果然还是累了吧"

    # nil 「直射日光に当てられて、二人の露出した肌からは、汗の一筋が浮き出ては、すっと、軌跡を描いた。」
    "在阳光的直射下，两人裸露的皮肤上冒出一缕汗珠，划出一条轨迹"

    # nil 「俺は二人と硬く手を繋ぎながら、温かい風を浴びていた。」
    "我和两个人紧紧牵着手，沐浴在温暖的风中"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まったりー」
    voice "voice/真冬/maf_a1_1367.ogg"
    dong 真冬_水着_基本_まったり "真悠闲啊——"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ちーず…毎日が特売日…」
    show 心愛_水着_基本_きらきら at love69_right with dissolve
    voice "voice/心愛/cca_a1_1709.ogg"
    ai 心愛_水着_基本_きらきら "切…每天都是特价日…"
    hide 心愛_水着_基本_嬉しい

    # nil 「二人とテンションに身を任せて騒ぐのも好きだが、こうして、二人とゆっくりとした時間を過ごすのも好きだ。」
    "我喜欢和两个人在一起兴奋地吵吵闹闹，但我也喜欢这样和两个人悠闲地度过时光"

    # 莲 「あ」
    lian "啊"

    # nil 「俺は一つ、大切な事を忘れていた。」
    "我忘记了一件重要的事情"

    # nil 「そしてそれを思い出した。」
    "然后我想起了那个"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「む！」
    show 心愛_水着_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1710.ogg"
    ai 心愛_水着_基本_真顔 "嗯！"
    hide 心愛_水着_基本_きらきら

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「んー？　どした？」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1368.ogg"
    dong 真冬_水着_基本_無表情 "嗯？怎么了？"
    hide 真冬_水着_基本_まったり

    # 莲 「いや、お前らに言い忘れてた事があってな」
    lian "那个，我有件事忘记对你们说了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「それは、真剣な話？」
    show 心愛_水着_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1711.ogg"
    ai 心愛_水着_基本_嬉しい "那是认真的话吗？"
    hide 心愛_水着_基本_真顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「それとも、割とどうでも良いお兄ちゃんの秘密？」
    show 真冬_水着_基本_ジト目 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1369.ogg"
    dong 真冬_水着_基本_ジト目 "还是说，相对无关紧要的欧尼酱的秘密？"
    hide 真冬_水着_基本_無表情

    # 莲 「どちらかというと真剣な話」
    lian "要说的是认真的话"

    # 真冬 「ん…じゃぁ、聞くよ。よいしょっと」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1370.ogg"
    dong 真冬_水着_基本_無表情 "嗯…那我听你说，是什么呢？"
    hide 真冬_水着_基本_ジト目

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「うんうん。何かな？あ、辛い事とかでも、私はいつでも受け入れるからね、蓮くんのこと…大好きだし」
    voice "voice/心愛/cca_a1_1712.ogg"
    ai 心愛_水着_基本_嬉しい "嗯嗯，是什么呢？啊，就算是痛苦的事情，我也会接受的，因为我……最喜欢莲君了"

    # 莲 「そう力むな。前向きな話だ」
    lian "别这么过度用力，是积极的事情"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「早とちりさん」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1371.ogg"
    dong 真冬_水着_基本_微笑み "那就快说吧"
    hide 真冬_水着_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぶえ…えへへ、まだ、ちょっと、蓮くんと真冬ちゃんと付き合ってるっていう実感、掴みきれてないからさー」
    voice "voice/心愛/cca_a1_1713.ogg"
    ai 心愛_水着_基本_嬉しい "咕欸……欸嘿嘿，还有点，没有完全掌握莲君还有真冬酱在交往的实感"

    # 莲 「よしよし」
    lian "好啦好啦"

    # 心爱 「あぅ…えと、それで…蓮君は何を言おうとしたの？」
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1714.ogg"
    ai 心愛_水着_基本_笑顔 "啊呜……那个，然后…莲君到底想说什么？"
    hide 心愛_水着_基本_嬉しい

    # 莲 「えっとな」
    lian "那个啊"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うん…わくわく」
    voice "voice/真冬/maf_a1_1372.ogg"
    dong 真冬_水着_基本_微笑み "嗯…好兴奋"

    # nil 「俺は一度二人の事を見つめてから、切り出した。」
    "我看了他们一眼，然后开口了"

    # 莲 「結婚式の真似事をしてから言う台詞じゃねぇけども…。心愛、真冬…卒業したらさ、結婚してくれないか？」
    lian "虽然不是结婚典礼仿真之后说的台词……但是心爱，真冬…毕业后，能和我结婚吗？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「っ…！」
    show 心愛_水着_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1715.ogg"
    ai 心愛_水着_基本_驚き "啊……！"
    hide 心愛_水着_基本_笑顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「おにいちゃ…んっ…！」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1373.ogg"
    dong 真冬_水着_基本_無表情 "欧尼…酱…！"
    hide 真冬_水着_基本_微笑み

    # 莲 「あんま高いもんは用意できなかったけど…」
    lian "虽然没有准备那么贵的东西…"

    # nil 「俺はそう言いながら、海パンの中から二つのエンゲージリングが入った箱を取り出した。」
    # 参考资料：https://ntwmachine.com/swim-suit#toc2
    "我一边这样说着，一边从泳装里拿出了装有两个订婚戒指的盒子（L:海パン，就是男士穿的泳装的一个类型，类似游泳短裤）"

    # 真冬 「どこから取り出してるのよ…」
    show 真冬_水着_基本_ジト目 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1374.ogg"
    dong 真冬_水着_基本_ジト目 "你从哪里拿出来的啊…"
    hide 真冬_水着_基本_無表情

    # 莲 「仕方なかったんだ。お前らに隠して持ち運ぶのはこしかねぇだろ」
    lian "没办法，我不可能把它藏起来变给你们吧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ふ…ふえ！？　いつのまに！　私、朝、蓮くんの荷物全部のぞき見したのに！　パンツもその中も全部！」
    voice "voice/心愛/cca_a1_1716.ogg"
    ai 心愛_水着_基本_驚き "啊…呜欸！？什么时候！我早上都偷看了莲君的行李！内裤和里面全部都看过了！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「心愛ちゃんも何やってるのよ…」
    voice "voice/真冬/maf_a1_1375.ogg"
    dong 真冬_水着_基本_ジト目 "心爱酱也是在做什么呢……"

    # 莲 「…で、まぁ、そういうわけで、良かったら受け取ってくれないか？」
    lian "……那么，嘛，就是这样，如果愿意的话，可以收下吗？"

    # nil 「そう言って、俺は蓋を開いて二人に中の指輪を見せつけた。」
    "这样说着，我打开盖子给两个人看了里面的戒指"

    # nil 「心愛にはルビーが、真冬にはアクアマリンがあしらわれたシルバーのリングだ。」
    "给心爱的是红宝石戒指，而给真冬则是海蓝宝石点缀的银色戒指"

    # nil 「ちなみに、この前心愛と真冬が、二人で出かけた日に、寝たふりをして買ってきた物だ。」
    "顺便一提，这是前一天心爱和真冬两个人出门的时，假装睡觉买回来的"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「うっ…うっ…」
    show 心愛_水着_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1717.ogg"
    ai 心愛_水着_基本_泣き "呜……呜……"
    hide 心愛_水着_基本_驚き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「…うっ…」
    show 真冬_水着_基本_泣き at love69_left with dissolve
    voice "voice/真冬/maf_a1_1376.ogg"
    dong 真冬_水着_基本_泣き "……呜……"
    hide 真冬_水着_基本_ジト目

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「うわああああああああ」
    show 心愛_水着_基本_号泣 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1718.ogg"
    ai 心愛_水着_基本_号泣 "哇啊啊啊啊啊啊啊啊"
    hide 心愛_水着_基本_泣き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「おにいちゃああああああん」
    show 真冬_水着_基本_号泣 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1377.ogg"
    dong 真冬_水着_基本_号泣 "欧尼酱——"
    hide 真冬_水着_基本_泣き

    # nil 「ボスッ」
    "啪"

    # nil 「二人は、指輪を受け取らずに、強く強く、泣きながら抱きついてきた。」
    "两个人没有接过戒指，而是紧紧地抱在一起，哭泣着"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ずるいよぉ、さっきの結婚式だって、泣きそうだったのにさー」
    voice "voice/心愛/cca_a1_1719.ogg"
    ai 心愛_水着_基本_号泣 "太狡猾了，刚才的婚礼，明明都快要哭出来了"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「えぐっ、えぐっ、うれしいよぉ…私にもちゃんと結婚相手として見てくれてるなんて…」
    voice "voice/真冬/maf_a1_1378.ogg"
    dong 真冬_水着_基本_号泣 "呜、呜，好开心啊…竟然也把我当成结婚对象来看待……"

    # 莲 「お、おう、と、とりあえず良いって事なんだよな…ゆ、指輪受け取ってくれ…」
    lian "哦，嗯，总、总之是好事吧……你们，把戒指收下吧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぐすんっ…あい…」
    show 心愛_水着_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1720.ogg"
    ai 心愛_水着_基本_泣き "呜……嗯……"
    hide 心愛_水着_基本_号泣

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「…うんっ…」
    show 真冬_水着_基本_泣き at love69_left with dissolve
    voice "voice/真冬/maf_a1_1379.ogg"
    dong 真冬_水着_基本_泣き "…嗯…"
    hide 真冬_水着_基本_号泣

    # nil 「二人は俺から離れて、それぞれの指輪を指に…」
    "两个人离开我，戴上各自的戒指…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「……」
    show 心愛_水着_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1721.ogg"
    ai 心愛_水着_基本_真顔 "……"
    hide 心愛_水着_基本_泣き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「……」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1380.ogg"
    dong 真冬_水着_基本_無表情 "……"
    hide 真冬_水着_基本_泣き

    # 莲 「あれ、気に入らなかった？」
    lian "咦，不喜欢吗？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「…まふまふちゃん、こっち」
    voice "voice/心愛/cca_a1_1722.ogg"
    ai 心愛_水着_基本_真顔 "……嘛呼嘛呼酱，这边"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うん…はい」
    voice "voice/真冬/maf_a1_1381.ogg"
    dong 真冬_水着_基本_無表情 "嗯……好"

    # 莲 「え？」
    lian "欸？"

    # nil 「目の前で、心愛と真冬は、指輪を交換して、それぞれ左手の薬指にはめた。」
    "在眼前，心爱和真冬交换了戒指，分别戴在了对方左手的无名指上"

    # 真冬 「…お兄ちゃんの事は大好きだし、愛してるけど、一つ、忠告しておこう」
    voice "voice/真冬/maf_a1_1382.ogg"
    dong 真冬_水着_基本_無表情 "…我最喜欢欧尼酱了，虽然我爱你，不过，我给你一个忠告"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「気持ちはすっごく嬉しいし、今めちゃくちゃ幸せで泣きそうだけど、一つ」
    show 心愛_水着_基本_無表情 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1723.ogg"
    ai 心愛_水着_基本_無表情 "心情非常开心，现在非常幸福，都要哭了，但是只有一件事"
    hide 心愛_水着_基本_真顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 心爱&真冬 「『サイズ。間違ってるよ』」
    show 心愛_水着_基本_真顔 at love69_right with dissolve
    voice "voice/真冬/maf_a1_1383.ogg"
    ai_dong 真冬_水着_基本_無表情 "『尺寸，你弄错了』"
    hide 心愛_水着_基本_無表情

    # 莲 「…はい」
    lian "…是的"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「でも、心愛ちゃんの指にはぴったりだったね」
    show 真冬_水着_基本_嬉しい at love69_left with dissolve
    voice "voice/真冬/maf_a1_1384.ogg"
    dong 真冬_水着_基本_嬉しい "但是，很适合心爱酱的手指呢"
    hide 真冬_水着_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「私も、まふまふちゃんのはピッタリだった」
    show 心愛_水着_基本_微笑み at love69_right with dissolve
    voice "voice/心愛/cca_a1_1725.ogg"
    ai 心愛_水着_基本_微笑み "我的也是，很适合嘛呼嘛呼酱的呢"
    hide 心愛_水着_基本_真顔

    # 莲 「じゃぁ、その、なんだ、二人だと思ってそれぞれつけてくれ…」
    lian "那么，那个，那什么，就把它当作是自己，戴到对方的手指上吧…"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そういう事にしときまーす」
    show 真冬_水着_基本_ジト目 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1385.ogg"
    dong 真冬_水着_基本_ジト目 "就这么定了吧"
    hide 真冬_水着_基本_嬉しい

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「えへへー、じゃぁこうやって、真冬ちゃんに…ちゅっ」
    hide 心愛_水着_基本_微笑み
    show 心愛_水着_基本_キス:
        zoom 1.5
        xalign 0.8918
        yalign -0.09
        linear 0.15 xalign 0.76
    voice "voice/心愛/cca_a1_1726.ogg"
    ai 心愛_水着_基本_キス "欸嘿嘿，那么，就像这样，给真冬酱……啾"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「私も。心愛ちゃんにー…ちゅっ」
    hide 真冬_水着_基本_ジト目
    show 真冬_水着_基本_キス:
        zoom 1.5
        xalign 0.13
        yalign -0.09
        linear 0.15 xalign 0.268
    voice "voice/真冬/maf_a1_1386.ogg"
    dong 真冬_水着_基本_キス "我也是，给心爱酱……啾"

    # nil 「それぞれ、自分の指にはめた互い違いの宝石にキスをした。」
    "分别亲吻了戴在各自手指上的互不相同的宝石"

    # nil 「まぁ、そんなやり方もあるか。とりあえず二人は喜んでくれたようだ。」
    "嘛，也有这样的做法吗。总之两个人好像很开心"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「じゃぁ…改めて、私達から、誓いのキス、しよっか」
    show 心愛_水着_基本_嬉しい:
        zoom 1.5
        xalign 0.76
        yalign -0.09
    with dissolve
    voice "voice/心愛/cca_a1_1727.ogg"
    ai 心愛_水着_基本_嬉しい "那么…我们再来一次誓言之吻吧"
    hide 心愛_水着_基本_キス

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そだね。大好きなお兄ちゃんに、私達を捧げます」
    show 真冬_水着_基本_微笑み:
        zoom 1.5
        xalign 0.268
        yalign -0.09
    with dissolve
    voice "voice/真冬/maf_a1_1387.ogg"
    dong 真冬_水着_基本_微笑み "是的呢，把我们献给最喜欢的欧尼酱"
    hide 真冬_水着_基本_キス

    # 心爱&真冬 「『『ちゅー♪』』」
    show 心愛_水着_基本_笑顔:
        zoom 1.5
        xalign 0.76
        yalign -0.09
    show 真冬_水着_基本_無表情:
        zoom 1.5
        xalign 0.268
        yalign -0.09
    with dissolve
    voice "voice/真冬/maf_a1_1388.ogg"
    ai_dong 真冬_水着_基本_無表情 "『啾——♪』"

    # nil 「夕日に見つめられながらの、二人のキスは、どんな宝石よりも宝物だった。」
    "在夕阳的凝视下，两个人的吻比任何宝石都珍贵"

    # 外人さん（外国人先生） 「They got marrrrrrried！」
    # 这里就叫老外B吧 ForeignerB foreignerb
    foreignerb "They got marrrrrrried！"

    # 外人さん（外国人先生） 「Congratulation！！！EeeeeeeeHaaaaaaa！！！！」
    # 这里就叫老外C吧 ForeignerC foreignerc
    foreignerc "Congratulation！！！EeeeeeeeHaaaaaaa！！！！"

    # 外人さん（外国人先生） 「Here come's shuffle time！！！！Come on Dejay！！！」
    # 这里就叫老外D吧 ForeignerD foreignerd
    foreignerd "Here come's shuffle time！！！！Come on Dejay！！！（L:shuffle，(笨拙或尴尬地)把脚动来动去; 坐立不安；Dejay：DJ）"

    # DJ 「Okay boys and girls！Live,Love,Laugh,and be happy！！Check it out！」
    # LTT视频康这里：https://www.bilibili.com/video/BV1d5411E7ua 06:52
    # 精准空降：https://www.bilibili.com/video/BV1d5411E7ua?t=404.7
    dj "Okay boys and girls！Live,Love,Laugh,and be happy！！Check it out！（L:看到Live,Love,Laugh，想到LTT的Dennis的Live，Laugh，Liao了，活，笑，廖2333）"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「…めっちゃみんなに見られてましたね…」
    show 心愛_水着_基本_泣き:
        zoom 1.5
        xalign 0.76
        yalign -0.09
    with dissolve
    voice "voice/心愛/cca_a1_1729.ogg"
    ai 心愛_水着_基本_泣き "…呜欸，大家都在看这边呢…"
    hide 心愛_水着_基本_笑顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「あーあ…なんか勝手にパーティはじめちゃったみたいだし…」
    show 真冬_水着_基本_目閉じ:
        zoom 1.5
        xalign 0.268
        yalign -0.09
    with dissolve
    voice "voice/真冬/maf_a1_1389.ogg"
    dong 真冬_水着_基本_目閉じ "啊——啊…好像自己开始开派对了……"
    hide 真冬_水着_基本_無表情

    # 莲 「言葉通じなくても…指輪渡してちゃ…まぁ、わかるわな…」
    lian "就算语言不通…也不能把戒指给他们昂……嘛，知道吗……"

    # nil 「どこからもってきたのか、サラウンドシステムを積んだスピーカーが重低音と共にアップチューンを奏で始める。」
    "不知从哪里拿来的，装载了环绕系统的扬声器与重低音一起开始奏响"

    # 莲 「よし、踊るか！」
    lian "好，跳舞吧！"

    # 真冬 「ワルツにしては少し激しすぎるようですけど、しっかりリードして頂けますかしら？」
    hide 真冬_水着_基本_目閉じ
    show 真冬_水着_基本_微笑み:
        zoom 1.5
        xalign 0.268
        yalign -0.09
    with dissolve
    voice "voice/真冬/maf_a1_1390.ogg"
    dong 真冬_水着_基本_微笑み "就华尔兹来说好像有点太激烈了，能好好带领我吗？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あろーはあー！」
    show 心愛_水着_基本_にっこり:
        zoom 1.5
        xalign 0.76
        yalign -0.09
    with dissolve
    voice "voice/心愛/cca_a1_1730.ogg"
    ai 心愛_水着_基本_にっこり "ALO——HA——！"
    hide 心愛_水着_基本_泣き

    # nil 「心愛と真冬の手を引いて立ち上がり、浜辺で広げられるパーティに、歓声をあげて飛び込む。」
    "拉着心爱和真冬的手站起来，欢呼着冲进在海滩上举行的派对"

    # nil 「心愛と真冬は、それぞれもう片方の手でシャカ（アロハの手）を作った。」
    # 参考资料：https://www.lanilanihawaii.com/column/sharing-my-hawaii/shaka-sign.html
    "心爱和真冬分别用另一只手做了Shaka的手势(ALOHA的手势）（L:对原作注释补充一下，Shaka的手势除了是ALOHA的手势和意思之外，还可以表示对他人的同情和相互尊重的感觉）"

    # nil 「それぞれの指には、婚約指輪に埋め込まれた宝石が、イルミネーションと太陽に照らされ虹色に輝いていた。」
    "在各自的手指上，订婚戒指中嵌入的宝石，在灯光和阳光的照耀下闪耀着彩虹色的光芒"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene ハワイd with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # nil 「パーティは日が暮れるまで続き、流石にへとへとになったので、パーティから抜けでてきました。相変わらず外人さん達は踊りつづけています。」
    "派对一直持续到天黑，果然还是筋疲力尽了，所以从派对里溜了出来。外国人还是一如既往地在跳舞"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ふにゃー…へとへと…もうあるけにゃい…」
    show 心愛_水着_基本_ぐるぐる at love69_right with dissolve
    voice "voice/心愛/cca_a1_1731.ogg"
    ai 心愛_水着_基本_ぐるぐる "呼喵呼喵……那个那个……已经走不动了喵……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「はいはーい。なでなで」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1391.ogg"
    dong 真冬_水着_基本_無表情 "好啦好啦，摸呼摸呼"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「にゃー…」
    show 心愛_水着_基本_もぐもぐ at love69_right with dissolve
    voice "voice/心愛/cca_a1_1732.ogg"
    ai 心愛_水着_基本_もぐもぐ "喵——…"
    hide 心愛_水着_基本_ぐるぐる

    # nil 「重い足を引きずって、予約してあるホテルへ向かっている。」
    "拖着沉重的脚步，朝着预约好的酒店走去"

    # nil 「が、流石に疲れたので、ベンチに座って休憩中。」
    "但是，因为实在是太累了，所以坐在长椅上休息"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ふひー…暑い…日が暮れてもあつし…」
    show 心愛_水着_基本_ぐるぐる at love69_right with dissolve
    voice "voice/心愛/cca_a1_1733.ogg"
    ai 心愛_水着_基本_ぐるぐる "呼欸——……好热……即使天黑了也很热呢…"
    hide 心愛_水着_基本_もぐもぐ

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「止まると余計に暑いね…」
    show 真冬_水着_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_1392.ogg"
    dong 真冬_水着_基本_目閉じ "停下来就更热了呢…"
    hide 真冬_水着_基本_無表情

    # 莲 「アイスとかたべてぇな…」
    lian "好想吃冰淇淋啊…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「わかる…アイス…アイスたべたひ…」
    voice "voice/心愛/cca_a1_1734.ogg"
    ai 心愛_水着_基本_ぐるぐる "我知道…冰淇淋…想吃冰淇淋…"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「あ、私も…アイスたべたい…」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1393.ogg"
    dong 真冬_水着_基本_無表情 "啊，我也是…想吃冰淇淋…"
    hide 真冬_水着_基本_目閉じ

    # 莲 蓮「大抵、ハワイにゃアイスの屋台がそこかしこにあるってテレビでやってたんだけどな…」
    lian "好像，在电视上看到夏威夷到处都有卖冰淇淋的摊子呢……"

    # nil 「ベンチに座りながら、辺りを見渡す。」
    "坐在长椅上，环视四周"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # アイス屋（冰淇淋店）（里昂） 「アイス屋だよー！　素敵な魔法のアイスはいらんかねー！」
    voice "voice/リオン/ron_a1_1040.ogg"
    icecreamroom リオン_基本_杖_微笑み "是冰淇淋店！想来一个很棒的魔法冰淇淋吗？"

    # 莲 「ビンゴ。あったぜアイス屋さん。ちょっちいってくるわ」
    lian "Bingo，找到冰淇淋店啦，我去一下"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「私も行くよ…心愛ちゃん、動ける？」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1394.ogg"
    dong 真冬_水着_基本_微笑み "我也去……心爱酱，还能动吗？"
    hide 真冬_水着_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「アイスのためなら…余裕っ…！」
    show 心愛_水着_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1735.ogg"
    ai 心愛_水着_基本_嬉しい "如果是为了冰淇淋的话…就很从容了…！"
    hide 心愛_水着_基本_ぐるぐる

    # nil 「真冬も心愛も重い腰を上げた。」
    "真冬和心爱都抬起了沉重的腰"

    # nil 「どうやら日本人向けのアイス屋らしい。日本語で客引きをしていたので、ついつい吸い込まれるように引き寄せられる。」
    "好像是面向日本人的冰淇淋店，因为是在用日语招揽客人，不知不觉就被吸引了过去"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「へいらっしゃい！」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1041.ogg"
    lion リオン_基本_杖_微笑み "欢迎光临！"

    # 莲 「江戸っ子かよ！　つーか随分流暢な日本語だなって…お前は！」
    lian "是江户人啊！话说你的日语真流利啊！"

    # 里昂 「あろーはー！　ハネムーンかい旦那ァ」
    show リオン_基本_杖_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1042.ogg"
    lion リオン_基本_杖_ニタァ "ALO——HA——！在度蜜月的先生啊"
    hide リオン_基本_杖_微笑み

    # 莲 「リオン…何でこんな所に…」
    lian "里昂…为什么会在这种地方……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あれ？　知り合い？」
    show 心愛_水着_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1736.ogg"
    ai 心愛_水着_基本_驚き "咦？认识吗？"
    hide 心愛_水着_基本_嬉しい

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「私達以外に女の子がいたなんて…プロポーズしたくせに…」
    show 真冬_水着_基本_本気 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1395.ogg"
    dong 真冬_水着_基本_本気 "除了我们以外还有别的女孩子…明明都求婚了……"
    hide 真冬_水着_基本_微笑み

    # 莲 「違う違う誤解だ誤解！　話せば長くなるけど、簡単に表現すると友達だよ！」
    lian "不是的不是的是误会是误会！说来话长，简单的来说就是朋友！"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「お！　もしかして、噂の彼女達かーい？　へーいわっつあっぷ！」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1043.ogg"
    lion リオン_基本_杖_にっこり "哦！难道是传说中的女朋友们吗？Hey What's up！"
    hide リオン_基本_杖_ニタァ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あろは！　わっつあーっぷ！どうも、蓮君の彼女やってます、心愛です。ぺこり」
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1737.ogg"
    ai 心愛_水着_基本_笑顔 "ALOHA！What's up！那么，我就是莲君的女朋友，心爱的说，就是这样"
    hide 心愛_水着_基本_驚き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「心愛ちゃん、彼女じゃないでしょ、もう、フィアンセでしょ」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1396.ogg"
    dong 真冬_水着_基本_微笑み "心爱酱，不是女朋友，已经是未婚妻了吧"
    hide 真冬_水着_基本_本気

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はっ、そうでした！」
    show 心愛_水着_基本_まふまふ at love69_right with dissolve
    voice "voice/心愛/cca_a1_1738.ogg"
    ai 心愛_水着_基本_まふまふ "啊，是这样的呢！"
    hide 心愛_水着_基本_笑顔

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ヒューゥ！　こいつぁーアッツアツだねぇ。沈んだはずの太陽がまーた昇っちまったかぁ？　売り物のアイスを溶かさないでおくれよー？」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1044.ogg"
    lion リオン_基本_杖_微笑み "这些家伙真是热闹呢。本应沉没的太阳又升上来了吗？请不要溶化商品的冰淇淋哦？"
    hide リオン_基本_杖_にっこり

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「溶かすのはフィアンセのプッシーだけにしとくんだな」
    # 这里的MJ也少了小图标，回头加上
    voice "voice/その他/mjf_a1_0057.ogg"
    mj MJ_通常 "只要能确保融化你未婚夫的辣里就可以了……"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「黙れマイケル」
    show リオン_基本_杖_見下し at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1045.ogg"
    lion リオン_基本_杖_見下し "闭嘴迈克尔"
    hide リオン_基本_杖_微笑み

    # 莲 「あ、あ…しかし、どうして」
    lian "啊，啊…但是，为什么？"

    # 里昂 「そりゃーお仕事だよ！　場所を変えるって言ったじゃんか！正確には旅行という名のバカンスだけどね！　旅先での小銭稼ぎってやつですよ！」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1046.ogg"
    lion リオン_基本_杖_微笑み "那当然是工作啦！不是说过要换地方吗！正确地说是以旅行为名的休假！就是在旅行中赚点零钱这样"
    hide リオン_基本_杖_見下し

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「で…お兄ちゃん、この人との関係について説明してくれる？」
    voice "voice/真冬/maf_a1_1397.ogg"
    show 真冬_水着_基本_本気 at love69_left with dissolve
    dong 真冬_水着_基本_本気 "那么…欧尼酱，能说明一下和这个人的关系吗？"
    hide 真冬_水着_基本_微笑み

    # 莲 「睨むなよ！どうする、リオン。どこから説明しようか」
    lian "别瞪着我啊！怎么办，里昂。从哪里开始说明呢？"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ラブポーション・シクスティナインを作りました。と、言えば話は早いんじゃないかな？」
    voice "voice/リオン/ron_a1_1047.ogg"
    lion リオン_基本_杖_微笑み "LOVEPOTION·SIXTYNINE是我做的。这么说的话，不是能很快讲完故事吗？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あー！　あのすっごく美味しいアイス屋さん！」
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1739.ogg"
    ai 心愛_水着_基本_笑顔 "啊！那家超好吃的冰淇淋店！"
    hide 心愛_水着_基本_まふまふ

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そして、エッチな成分入りの…」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1398.ogg"
    dong 真冬_水着_基本_無表情 "还有，加入了瑟琴成分的……"
    hide 真冬_水着_基本_本気

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「どんな風に話が行ってるのだね…蓮くん…」
    voice "voice/リオン/ron_a1_1048.ogg"
    lion リオン_基本_杖_微笑み "你和她们说了什么……莲君……"

    # 莲 「いや、俺はしっかり説明したんだけどな…」
    lian "不，我已经好好说明过了…"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「この前、霧葉さんに食べさせられた時に…ね？」
    voice "voice/真冬/maf_a1_1399.ogg"
    dong 真冬_水着_基本_無表情 "之前雾叶姐姐让我吃的时候…是吧？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「エ、エクストリームバージョンだって言ってました」
    voice "voice/心愛/cca_a1_1740.ogg"
    ai 心愛_水着_基本_笑顔 "E、Extreme Version那个，好像是这么说的来着"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「Dude！　あれは試作品なんだけど早くも他人に食べさせたのかー…。でも…ほんと、お陰様で、製品化にこぎつけそうですよ！　自分のお店を持つには、まだまだ時間はかるけど…」
    voice "voice/リオン/ron_a1_1049.ogg"
    lion リオン_基本_杖_微笑み "Dude！那是试作品，但是这么快就让别人吃了吗？不过……真的，托您的福，就快要把它产品化了。要拥有自己的店，还需要一点时间…"

    # 莲 「おー、そいつは良かったな」
    lian "哦，那太好了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あ、でもそっか。私達がこうして蓮くんと真冬ちゃんと婚約出来てるのは」
    voice "voice/心愛/cca_a1_1741.ogg"
    ai 心愛_水着_基本_笑顔 "啊，原来如此。我们之所以能和莲君还有真冬订婚"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「貴方のおかげって事…ですね」
    voice "voice/真冬/maf_a1_1400.ogg"
    dong 真冬_水着_基本_無表情 "是托你的福……吧"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「んな、大げさな！　二人が十分に蓮くんの事を愛していただけの話だよ！」
    voice "voice/リオン/ron_a1_1050.ogg"
    lion リオン_基本_杖_微笑み "什么啊，太夸张了！只不过是因为两个人十分爱着莲君而已！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「えへ、蓮くんに対する愛情は誰にも負けないもんね！」
    voice "voice/心愛/cca_a1_1742.ogg"
    ai 心愛_水着_基本_笑顔 "欸嘿嘿，我对莲君的爱是不会输给任何人的！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「私にも？」
    voice "voice/真冬/maf_a1_1401.ogg"
    dong 真冬_水着_基本_無表情 "对我也是？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「同じくらいかな！　そして同じぐらい真冬ちゃんも愛してる！」
    voice "voice/心愛/cca_a1_1743.ogg"
    ai 心愛_水着_基本_笑顔 "差不多一样吧！而且我也同样爱着真冬酱！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うんっ。私も愛してるよ」
    voice "voice/真冬/maf_a1_1402.ogg"
    dong 真冬_水着_基本_無表情 "嗯，我也爱你"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「へいへい。主よ、このもの達に永遠の祝福あれ…っと」
    voice "voice/リオン/ron_a1_1051.ogg"
    lion リオン_基本_杖_微笑み "嘿嘿。主啊，请给这些人以永远的祝福"

    # nil 「リオンは呆れながら、胸で十字架を切った。」
    "里昂惊讶地在胸前画了一个了十字架"

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「おいブラザー。俺にも愛してるって言ってくれないか」
    # 这里的MJ也少了小图标，回头加上
    voice "voice/その他/mjf_a1_0058.ogg"
    mj MJ_通常 "喂，Brother——。能不能也对我说“我爱你”？"

    # 莲 「黙れマイケル」
    lian "闭嘴迈克尔"

    # MJ 「Fxxk you！」
    # 这里的MJ也少了小图标，回头加上
    voice "voice/その他/mjf_a1_0059.ogg"
    mj MJ_通常 "花Q！"

    # 莲 「でも嫌いじゃないぞ」
    lian "但是我不讨厌你"

    # MJ 「きゅん…」
    # 这里的MJ也少了小图标，回头加上
    voice "voice/その他/mjf_a1_0060.ogg"
    mj MJ_通常 "Q……"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「そんな、幸せな三人に、良いニュースと悪いニュースがあります。どっちから聞きたいです？」
    show リオン_基本_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1052.ogg"
    lion リオン_基本_杖_嬉しい "对那么幸福的三个人，我有一个好消息和一个坏消息。你想从哪一个开始听？"
    hide リオン_基本_杖_微笑み

    # 莲 「良いニュースから聞こうか」
    lian "从好消息开始吧"

    # 里昂 「おっけー！　じゃぁ、まぁ、婚約祝いに、アイスを三本無料でプレゼントしましょう」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1053.ogg"
    lion リオン_基本_杖_にっこり "OK——！那么，为了庆祝订婚，我免费送三支冰淇淋作为订婚礼物吧"
    hide リオン_基本_杖_嬉しい

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「わーい！」
    voice "voice/心愛/cca_a1_1744.ogg"
    ai 心愛_水着_基本_笑顔 "哇——咿！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そっか、アイス買いに来たの忘れてたね…」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1403.ogg"
    dong 真冬_水着_基本_微笑み "这样啊，我都忘记是来买冰淇淋的了…"
    hide 真冬_水着_基本_無表情

    # 莲 「で、悪いニュースとは？」
    lian "那么，坏消息是什么？"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「在庫が、エクストリームしか無いってことさ。食べたらもれなくエッチな気分になれます。そういう仕様です」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1054.ogg"
    lion リオン_基本_杖_微笑み "目前库存有的，只有Extreme Version的冰淇淋了，恰了之后会有瑟琴的感觉，就是这样的坏消息捏"
    hide リオン_基本_杖_にっこり

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「お、おう…ご、ごくり…」
    show 心愛_水着_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1745.ogg"
    ai 心愛_水着_基本_真顔 "哦，哦……咽口水……"
    hide 心愛_水着_基本_笑顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「な、なんか、改めて言われると迫力あるね…」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1404.ogg"
    dong 真冬_水着_基本_無表情 "怎、怎么说呢，再次听到这样的话，还是好有魄力啊……"
    hide 真冬_水着_基本_微笑み

    # 莲 「ど、どうするよ…」
    lian "怎、怎么办呢…"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「くすくす。日本の諺に、旅の恥はかきすてってのがあるよね♪」
    # 参考资料：https://kotobank.jp/word/%E6%97%85%E3%81%AE%E6%81%A5%E3%81%AF%E6%8E%BB%E3%81%8D%E6%8D%A8%E3%81%A6-562202
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1055.ogg"
    lion リオン_基本_杖_にっこり "嘿嘿嘿，日本有句谚语，旅行的时候就把羞耻丢掉吧♪（L:旅行的时候身边没有认识的人，所以任何尴尬都只限于当下。 此外，旅行带来的自由感使人感到解放）"
    hide リオン_基本_杖_微笑み

    # nil 「リオンは余裕の表情を崩さないが、心愛も真冬も、そして俺も、正直恥ずかしかった。」
    "里昂保持着从容不迫的表情，但是心爱，真冬，还有我，说实话，都觉得很害羞"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「で、で、でもさ…！」
    show 心愛_水着_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1746.ogg"
    ai 心愛_水着_基本_泣き "但、但、但是啊……！"
    hide 心愛_水着_基本_真顔

    # nil 「最初に沈黙を破ったのは心愛だった。」
    "最初打破沉默的是心爱"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # L:人物名又写到里面去了捏，原作写脚本的那位就是逊啦~
    # 记得加人物表
    # 莲・真冬「『は、はい』」
    show 真冬_水着_基本_泣き at love69_left with dissolve
    voice "voice/真冬/maf_a1_1405.ogg"
    lian_dong 真冬_水着_基本_泣き "『嗯、嗯』"
    hide 真冬_水着_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぶ、ぶっちゃけ！　ホテルいったら、エッチ…す、するよね！」
    voice "voice/心愛/cca_a1_1747.ogg"
    ai 心愛_水着_基本_泣き "直，直截了当地说！去酒店的话，会H的吧！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 莲・真冬「『そ…そうだと思います』」
    voice "voice/真冬/maf_a1_1406.ogg"
    lian_dong 真冬_水着_基本_泣き "『我……我想是这样的』"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「じゃ、じゃぁ、どうせするなら、気分はノっていた方が、楽しいんじゃないかな！」
    show 心愛_水着_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1748.ogg"
    ai 心愛_水着_基本_嬉しい "那么，那么，反正要做的话，有瑟琴的气氛的话，不是会更开心吗！"
    hide 心愛_水着_基本_泣き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 莲・真冬「『た、確かに！』」
    voice "voice/真冬/maf_a1_1407.ogg"
    lian_dong 真冬_水着_基本_泣き "『雀，雀食』"

    # nil 「ていうか、それを心愛が切り出すとは。流石に、毎日のようにしていると、価値観も変わるのか？」
    "话说回来，这居然是心爱提出的。果然，每天都这样做的话，价值观也会改变吗？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぶええええはずかしいよー」
    show 心愛_水着_基本_ぶわー at love69_right with dissolve
    voice "voice/心愛/cca_a1_1749.ogg"
    ai 心愛_水着_基本_ぶわー "呜欸欸欸欸——好害羞啊——"
    hide 心愛_水着_基本_嬉しい

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「Exactly！　よく言えました！」
    voice "voice/リオン/ron_a1_1056.ogg"
    lion リオン_基本_杖_にっこり "Exactly！说得很好！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「と、ということで、リオンさん！　３個！　下さい！」
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1750.ogg"
    ai 心愛_水着_基本_笑顔 "就是这样，里昂小姐！请给我！３个！"
    hide 心愛_水着_基本_ぶわー

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「はいよー！　もってけ泥棒！」
    voice "voice/リオン/ron_a1_1057.ogg"
    lion リオン_基本_杖_にっこり "好哒——！拿着吧小偷！（L:没大看懂，个人感觉可能和二周目剧情有关）"

    # nil 「リオンはニッコリと微笑んで心愛と俺と真冬に例のアイスを手渡した。」
    "里昂微笑着把那份冰淇淋交给了我和心爱还有真冬"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「さぁ、召し上がれ」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1058.ogg"
    lion リオン_基本_杖_微笑み "来，恰吧"
    hide リオン_基本_杖_にっこり

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「イタダキマス！　ほら、蓮くんも真冬ちゃんも！」
    voice "voice/心愛/cca_a1_1751.ogg"
    ai 心愛_水着_基本_笑顔 "我开动了！来，莲君和真冬酱也来！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「もごっ」
    show 真冬_水着_基本_まったり at love69_left with dissolve
    voice "voice/真冬/maf_a1_1408.ogg"
    dong 真冬_水着_基本_まったり "嗯呜"
    hide 真冬_水着_基本_泣き

    # 莲 「ふがっ」
    lian "咕嘎"

    # nil 「未だに呆気にとられてる俺達の口に、無理矢理アイスを突っ込む心愛。」
    "在我们还在因为惊呆而张大了的嘴里，心爱硬把冰淇淋插了进去"

    # nil 「口の中に冷たくて優しい味が広がっていく。」
    "冷而柔和的味道在口中扩散开来"

    # nil 「やはり、味は安定の上手さだった。」
    "果然味道很还是一如既往的好"

    # nil 「そして、身体の温度が急上昇していき、今までの疲れを忘れていく。」
    "然后，身体的温度急速上升，忘记了至今为止的疲劳"

    # nil 「流石はエクストリーム版とでも言おうか。この前食べたオリジナルとは効果が違うようだ。」
    "果然是Extreme版的啊，和之前吃的原版的效果好像不大一样捏"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「言い忘れてたけど、疲労回復効果もあるからね、思う存分楽しんでおいでよ」
    show リオン_基本_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1059.ogg"
    lion リオン_基本_杖_嬉しい "虽然忘记说了，但是也有恢复疲劳的效果捏，请尽情享受吧"
    hide リオン_基本_杖_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「う、うん…！　えと、えと、あ、ありがとうリオンさん！」
    show 心愛_水着_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1752.ogg"
    ai 心愛_水着_基本_嬉しい "嗯，嗯……！那个、那个，谢，谢谢里昂小姐！"
    hide 心愛_水着_基本_笑顔

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「気にしないでいさ－。どうか末永くお幸せに…だよ！」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1060.ogg"
    lion リオン_基本_杖_微笑み "别放在心上，祝你们永远幸福……"
    hide リオン_基本_杖_嬉しい

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「うん。私達を幸せにしてくれて、ありがとうございました。ぺこり」
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1753.ogg"
    ai 心愛_水着_基本_笑顔 "嗯，谢谢你让我们幸福，谢谢你"
    hide 心愛_水着_基本_嬉しい

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「私も。　お兄ちゃんと心愛ちゃんと結ばれるきっかけをつくってくれて、本当にありがとう。おかげで、私達、すごく幸せです」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1409.ogg"
    dong 真冬_水着_基本_微笑み "我也是。谢谢你给我制造了和欧尼酱还有心爱酱结婚的机会。托你的福，我们非常幸福"
    hide 真冬_水着_基本_まったり

    # 莲 「あ…ありがとう、リオン」
    lian "啊…谢谢，里昂"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「にゃははは！　いえいえ、こちらこそありがとう！　本当に嬉しいよ！」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1061.ogg"
    lion リオン_基本_杖_にっこり "呀哈哈哈！没有没有，我才要谢谢你！真的很开心呢！"
    hide リオン_基本_杖_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ねぇねぇ、リオンさん、私達、また会えるかなぁ」
    show 心愛_水着_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1754.ogg"
    ai 心愛_水着_基本_真顔 "呐呐，里昂小姐，我们还能再见面吗？"
    hide 心愛_水着_基本_笑顔

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 真冬 「うん。こでお別れなのは、なんだか凄くもったいない気がする。友達になれたら嬉しいよね」
    show 真冬_水着_基本_にっこり at love69_left with dissolve
    voice "voice/真冬/maf_a1_1410.ogg"
    dong 真冬_水着_基本_にっこり "嗯。在这里分别，总觉得太可惜了。如果能成为朋友的话就很开心了"
    hide 真冬_水着_基本_微笑み

    # 莲 「大丈夫…だろ」
    lian "没关系的……对吧"

    # nil 「何故か、リオンではなく、俺が答えた。なんとなく、そんな気がしたからだ。」
    "不知道为什么，不是里昂，是我回答的，因为不知怎么的总觉得是这样"

    # 莲 「ハワイにまできて、こうして巡り会えたんだから…きっと…」
    lian "我们来到夏威夷，就这样相遇了……一定……"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「くすくす。そうだね。きっとまた会えるよ。楽しみにして」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1062.ogg"
    lion リオン_基本_杖_微笑み "嘿嘿，就是啊，一定会再见的，期待吧"
    hide リオン_基本_杖_にっこり

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はーい！　じゃぁ、待ってればいのかな？」
    show 心愛_水着_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1755.ogg"
    ai 心愛_水着_基本_嬉しい "好哒！那，我们就等着吧？"
    hide 心愛_水着_基本_真顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うん。いつまでも待ってるからね」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1411.ogg"
    dong 真冬_水着_基本_微笑み "嗯，一直都会等着你的哦"
    hide 真冬_水着_基本_にっこり

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ありがとう。君らの優しさは、なんだか凄く心地良いよ。幸せのお裾分けを、ごちそうさまです」
    show リオン_基本_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1063.ogg"
    lion リオン_基本_杖_嬉しい "谢谢。你们的温柔，让我觉得很舒服，谢谢你们和我分享幸福"
    hide リオン_基本_杖_微笑み

    # 莲 「あ。こっちも、美味しいアイスをごちそうさま」
    lian "啊，我也要谢谢你的美味冰淇淋"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はーい！　じゃぁ、待ってればいのかな？」
    show 心愛_水着_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1756.ogg"
    ai 心愛_水着_基本_泣き "哈呜…这个，比之前吃的那个效果更好…dokidoki地要停不下来了…"
    hide 心愛_水着_基本_嬉しい

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「はぁ…はぁ…ね…覚悟していた分、まだ…大丈夫だけど…」
    show 真冬_水着_基本_泣き at love69_left with dissolve
    voice "voice/真冬/maf_a1_1412.ogg"
    dong 真冬_水着_基本_泣き "哈啊……呜哈…呐……我已经做好觉悟了，现在……还没关系……"
    hide 真冬_水着_基本_微笑み

    # nil 「二人とも、恥ずかしそうに太もをすり合わせている。」
    "两个人都害羞地互相摩擦着大腿"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「うん。二人のためにも、早くホテルにチェックインしておいで」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1064.ogg"
    lion リオン_基本_杖_にっこり "嗯。为了这两个人，也早点去酒店登记入住吧"
    hide リオン_基本_杖_嬉しい

    # 莲 「あ、あ。そうするつもりだ。またな、リオン」
    lian "啊，啊，我会的，再见，里昂"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ばいばい！　リオンちゃん！」
    show 心愛_水着_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1757.ogg"
    ai 心愛_水着_基本_笑顔 "ByeBye！里昂酱！"
    hide 心愛_水着_基本_泣き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うん、またね、リオン」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1413.ogg"
    dong 真冬_水着_基本_微笑み "嗯，回头见，里昂"
    hide 真冬_水着_基本_泣き

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「アディオス・アミーゴ！aloha！」
    voice "voice/リオン/ron_a1_1065.ogg"
    lion リオン_基本_杖_にっこり "Adiós・amigo！ALOHA！（L:前面是之前提到的西班牙语“再会，朋友”，后面是刚才提到的夏威夷语ALOHA）"

    # nil 「俺達は溢れ出る幸福感の中で、リオンに向けてシャカマークを振って、ホテルへと走りだした。」
    "我们在满溢的幸福感中，朝着里昂挥动着Shaka的手势，向酒店跑去（L：刚才也提到过，Shaka的手势表示ALOHA的意思）"

    # 场景暂时切回沙滩
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene ハワイd with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「なんか、初めて会う感じゃなかったなーリオンちゃん」
    show 心愛_水着_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1758.ogg"
    ai 心愛_水着_基本_真顔 "总感觉，不像是第一次见面的感觉呢，里昂酱"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ね。昔から友達だった感じ」
    show 真冬_水着_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1414.ogg"
    dong 真冬_水着_基本_微笑み "是啊。感觉以前就是朋友了"

    # 莲 「お前達も感じてたか…俺もあいつに会ったときから感じてたわ」
    lian "你们也有这种感觉吗……我从见到那家伙开始就有这种感觉"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あと、帽子が喋ってたね」
    voice "voice/心愛/cca_a1_1759.ogg"
    ai 心愛_水着_基本_真顔 "还有，帽子在说话呢"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「たまーに居るよね。喋る帽子」
    show 真冬_水着_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1415.ogg"
    dong 真冬_水着_基本_無表情 "偶尔会有的吧？会说话的帽子"
    hide 真冬_水着_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ね。たまーに居るよね」
    show 心愛_水着_基本_無表情 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1760.ogg"
    ai 心愛_水着_基本_無表情 "呐，偶尔会有的吧"
    hide 心愛_水着_基本_真顔

    # 莲 「俺他のやつ見たことねぇわ…」
    lian "我从来没见过其它这样的……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ひとつ友達になった帽子がいるから、紹介するね」
    show 心愛_水着_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1761.ogg"
    ai 心愛_水着_基本_嬉しい "我有一个已经成为了朋友的帽子，回头介绍给你认识一下吧"
    hide 心愛_水着_基本_無表情

    # 莲 「お、おう…」
    lian "哦，哦…"

    # scene13 场景1 【期待已久的夏威夷之行与最终的婚礼】 结束！

    # Scene13 结束！！！

    # 过场：心爱&真冬（常服）
    ## 稍微改改
    image bg アイキャッチ心愛＆真冬水着 = "images/bg/アイキャッチ心愛＆真冬水着.png"

    $ quick_menu = False

    play sound "voice/effect/moosehead honk (stinger).ogg"
    stop music fadeout 2.0
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)
    scene アイキャッチ心愛＆真冬水着 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)

    $ renpy.pause(1.5, hard=True)

    jump scene14
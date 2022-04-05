# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene22 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：
# 版本 0.9 "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年4月5日

# 当前流程：编写脚本AIO Process

label scene22:
    # scene22 开始

    # scene22 场景2 【二周目_尾声】 开始
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)
    scene 空 at love69_bg1440 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)

    # 这就是最后一幕喽~

    # 场景：蔚蓝天空
    $ quick_menu = True

    # nil 「そして、決戦は金曜日。」
    "然后，是决战的星期五"

    # nil 「れから、最終追い込みで、リオンの神がかったチューニングで、なんとか即効性は抑えられました。」
    "之后，在最后的紧要关头，经过里昂的神奇调整，总算是抑制了速效性"

    # nil 「恐ろしい事に、体力も回復するようで、食べたら最後ヤるか抜くまでギンギン物語になるようです。」
    # 参考资料（略微NSFW内容）https://trip-partner.jp/15157
    # 这里的内容就写到注释里不写进去了吧
    "可怕的是，它似乎也能恢复体力，吃了之后，直到最后体力完全耗尽都不会停下来"

    # nil 「そのアイスは、『ラブポーション・シクスティナイン』を引き継ぎ『ラブポーション・エクストリーム』と名付けられた。」
    "那个冰淇淋继承了『LOVEPOTION・SIXTYNINE』的名字，被命名为『LOVEPOTION・EXTREME』"

    # nil 「ちなみに『シクスティナイン』は69番目の試作品というナンバリングだそうです。」
    "顺带一提『SIXTYNINE』是这批第69个原型的编号"

    # nil 「クーラーボックスに完成した『ラブポーションＥＸ』を詰め込んで、俺達は、決戦会場であるダイナーへと向かった。」
    "我们在冷藏箱里放入了完成品的『LOVEPOTIONＥＸ』朝着决战会场的Diner出发"

    # 场景切换到通学路街道
    scene 通学路c_昼 at love69_bg1440 with dissolve

    # 里昂 「よし…行こう、蓮くん」
    show リオン_基本_杖なし_無表情 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1066.ogg"
    lion リオン_基本_杖なし_無表情 "好…走吧，莲君"

    # 莲 「しかし…あの効果は健在なんだよな…恥ずかしいな…」
    lian "但是…那个效果还健在啊…真是害羞…"

    # 里昂 「それは私もだけど…この際、なるようになれだよ！」
    show リオン_基本_杖なし_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1067.ogg"
    lion リオン_基本_杖なし_微笑み "虽然我也是这样…但是在这个时候，变成这样就这样了吧！"
    hide リオン_基本_杖なし_無表情

    # 莲 「それもそうか。じゃ、いくぞ」
    lian "也是啊，那出发吧"

    # 莲&里昂 「『Let’s Rock！！』」
    # Scene18 已经定义人物
    show リオン_基本_杖なし_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1068_x.ogg"
    lian_lion リオン_基本_杖なし_ニタァ "『Let's Rock！！』"
    hide リオン_基本_杖なし_微笑み

    # nil 「二人揃ってドアをあける。」
    "两个人一起打开门"

    # 场景切69thStreetDiner
    scene 霧葉ちゃんのお店 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # 进 Diner BGM
    play music bgmfifteen fadeout 2.0 fadein 2.0

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬在右的参数
    transform love69_dong_right:
        zoom 1.5
        yalign -0.09
        xalign 0.91

    # 真冬 「はい、心愛ちゃん10万ドルね」
    show 真冬_私服_基本_目閉じ at love69_dong_right with dissolve
    voice "voice/真冬/maf_a1_1479.ogg"
    dong 真冬_私服_基本_目閉じ "好，心爱酱10万美元是吧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ほげー！　スポーツ選手には酷だよ！」
    show 心愛_私服_基本_ぶわー at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1820.ogg"
    ai 心愛_私服_基本_ぶわー "呜欸——！对运动员太残酷了啊！"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「はい、姉さん。貴様の好きなドリアンの香りですよ」
    show 店长_私服_にっこり at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0256.ogg"
    dinerowner 店长_私服_にっこり "给，姐姐，这是你最喜欢的榴莲"

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼在最右的参数
    transform love69_atri_rightest:
        zoom 1.5
        xalign 1.107
        yalign -0.295

    # 亚十礼 「好きって言ったつもりはないんだけど…くせぇし」
    show アシュリー_私服_困り at love69_atri_rightest with dissolve
    voice "voice/アシュリー/ash_a1_0049.ogg"
    atri アシュリー_私服_困り "我没说过喜欢……而且"

    # 瑠那在最左的参数
    transform love69_liuna_leftest:
        zoom 1.5
        xalign -0.303
        yalign -0.01

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「まふまふまふまふ」
    show 瑠那_私服_はう at love69_liuna_leftest with dissolve
    voice "voice/瑠那/lun_a1_0015.ogg"
    na 瑠那_私服_はう "嘛呼嘛呼嘛呼嘛"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「まふまふまふまふ」
    voice "voice/想瑠/sol_a1_0205.ogg"
    liu 想瑠_スーツ_照れ "嘛呼嘛呼嘛呼嘛呼（L:可怜的想瑠喵又没有地方放了捏233）"

    # 莲 「全員集合してる…」
    lian "大家都集合了啊…"

    # BGM 切！
    play music bgmtwentyseven fadeout 1.0 fadein 2.0

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「レディース＆ガールズ！　さぁやって参りました、リオンちゃんのアイス大試食大会！　司会は私、霧葉＝ブラックフェザーでお送りいたしまァす！」
    # 名字就定雾叶黑羽好了，看起来很Cool不是嘛
    show 店长_私服_本気 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0257.ogg"
    dinerowner 店长_私服_本気 "Ladies&Girls！终于来了，里昂的冰淇淋大品尝大会！主持人是我，雾叶黑羽 参上！"
    hide 店长_私服_にっこり

    # 莲 「あんたがMCかよ！」
    lian "你是主持啊！"

    # 店长 「それでは早速ルールをご説明致しましょう！　審査員はこに集まってくれた、私含め六人が順番に食事し、全員のが出たら、ミッションクリアとなります！」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0258.ogg"
    dinerowner 店长_私服_無表情 "那么，马上说明规则吧！评委们已经在这里集合了，包括我在内的六个人依次试吃，如果全员都通过了，任务就完成了！"
    hide 店长_私服_本気

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「いえーい！　お兄ちゃんみてるー！」
    show 真冬_私服_基本_にっこり_1 at love69_dong_right with dissolve
    voice "voice/真冬/maf_a1_1480.ogg"
    dong 真冬_私服_基本_にっこり_1 "Yeah——！欧尼酱看得到嘛！"
    hide 真冬_私服_基本_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「将来の夢は配管工になることです」
    show 心愛_私服_基本_微笑み at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1821.ogg"
    ai 心愛_私服_基本_微笑み "我的梦想是成为一名水管工！"
    hide 心愛_私服_基本_ぶわー

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「これ、ハワイ土産のバナのネックレスです」
    # 参考资料：https://store.shopping.yahoo.co.jp/clara-hawaii/islandheritage77.html?__ysp=44OP44Ov44Kk5Zyf55SjIOODkOODiuOBruODjeODg%2BOCr%2BODrA%3D%3D
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0206.ogg"
    liu 想瑠_スーツ_見下し "这个，是夏威夷特产的贝壳项链！"

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「リッター８キロってぇー！　タマつぶれちまうよぉ！」
    show 瑠那_私服_驚き at love69_liuna_leftest with dissolve
    voice "voice/瑠那/lun_a1_0016.ogg"
    na 瑠那_私服_驚き "一升8公斤！蛋蛋要碎掉了！"
    hide 瑠那_私服_はう

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「ジャイアント…パンダ…」
    show アシュリー_私服_幸せ at love69_atri_rightest with dissolve
    voice "voice/アシュリー/ash_a1_0050.ogg"
    atri アシュリー_私服_幸せ "巨人……熊猫……"
    hide アシュリー_私服_困り

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「尚、あらかじめ審査員の方々にはお酒を飲んで頂いております」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0259.ogg"
    dinerowner 店长_私服_目閉じ "还有，评委们事先已经喝过酒了"
    hide 店长_私服_無表情

    # 莲 「フリーダムかよ」
    lian "是自由泳吗？"

    # nil 「カウンター席に座った審査員達が騒ぎ出す。」
    "坐在吧台的评委们开始骚动"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「それでは早速ですが、リオンちゃん！準備はよろしいですか？　勝負下着は着けてきてますか？　ちなみに何色ですか？」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0260.ogg"
    dinerowner 店长_私服_微笑み "那我就直说了，亲爱的里昂酱！你准备好了吗？穿好决胜内衣了吗？顺便问一下，是什么颜色的？"
    hide 店长_私服_目閉じ

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「えーこほん。この服、ブラじゃなくてパットいれてます」
    show リオン_基本_杖なし_キス at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1068.ogg"
    lion リオン_基本_杖なし_キス "啊，这件衣服是No-bra，是直接这样穿的"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「やったーパットだあ！」
    show 心愛_私服_基本_笑顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1822.ogg"
    ai 心愛_私服_基本_笑顔 "好耶！啪嗒嗒！"
    hide 心愛_私服_基本_微笑み

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「なんとノーブラ参戦です。なかなかに挑発的な姿勢で素晴らしいと思います。さぁでは、れっつぱーりーたぁーいむ！　ヒャッホウ！」
    show 店长_私服_本気_1 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0261.ogg"
    dinerowner 店长_私服_本気_1 "竟然是No-bra来参战。是非常具有挑衅性的姿态，非常棒。来，那么，It's Party Time！WO——HOO！！"
    hide 店长_私服_微笑み

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 心爱&真冬 「『いえーい！』」
    # play xinaiab "voice/心愛/cca_a1_1823.ogg"
    show 真冬_私服_基本_微笑み at love69_dong_right with dissolve
    voice "voice/真冬/maf_a1_1481.ogg"
    ai_dong 真冬_私服_基本_微笑み "『Yeah——！！』"
    hide 真冬_私服_基本_にっこり_1

    # nil 「パァン！　両端に座っていた真冬と心愛が、示し合わせたようにクラッカーを鳴らす。」
    "啪！坐在两端的真冬和心爱，非常默契地击了掌"

    # 莲 「もうただのパーティじゃねぇか」
    lian "已经不是普通的派对了吗？"

    # 依次隐藏，里昂登场
    hide 心愛_私服_基本_笑顔 with dissolve
    hide リオン_基本_杖なし_キス with dissolve
    hide 店长_私服_本気_1 with dissolve
    hide 真冬_私服_基本_微笑み with dissolve
    hide 想瑠_スーツ_見下し with dissolve
    hide 瑠那_私服_驚き with dissolve
    hide アシュリー_私服_幸せ with dissolve

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    show リオン_基本_杖なし_ニタァ at love69_lion_center with dissolve

    # 里昂 「It's Show time！」
    voice "voice/リオン/ron_a1_1069.ogg"
    lion リオン_基本_杖なし_ニタァ "It's Show time！"

    # 莲 「お前もノリノリかよ！」
    lian "你也很兴奋啊！"

    # nil 「リオンはくるっと空中でクーラーボックスをまわしてから、タイルの床にダンッ！とたきつけるように設置して、」
    "里昂在空中转动冷藏箱，然后砰——的一声放在瓷砖地板上！"

    # nil 「浮き上がった蓋を、脚で蹴り開けた。」
    "用脚踢开微微开口的盖子"

    # nil 「浮まばゆい光がクーラーボックスからあふれ出す。」
    "耀眼的光芒从冷藏箱中溢出"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「わはー☆　ぴっかぴか！」
    voice "voice/心愛/cca_a1_1824.ogg"
    ai 心愛_私服_基本_きらきら "哇哈ー☆亮闪闪的！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「じゅるり…」
    voice "voice/真冬/maf_a1_1482.ogg"
    dong 真冬_私服_基本_居眠り "流口水……"

    # nil 「掴みは上々。」
    "整的不戳"

    # nil 「リオンは審査員にウインクして、しゃがみこみ、谷間からアイス用のディッシャーを取り出した。」
    "里昂对评委眨了眨眼，蹲下身，从胸前的山谷拿出了冰淇淋勺"

    # nil 「巨乳専用のパフォーマンスだ。」
    "这是巨乳专属的表演"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「う、羨ましくなんてないんだからねっ！」
    voice "voice/想瑠/sol_a1_0207.ogg"
    liu 想瑠_スーツ_目閉じ "咕呜，我一点都不羡慕你呢！"

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「ボクはできるよ？」
    voice "voice/瑠那/lun_a1_0017.ogg"
    na 瑠那_私服_微笑 "我的话能做到哦？"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ぷー！」
    voice "voice/想瑠/sol_a1_0208.ogg"
    liu 想瑠_スーツ_悲しみ "呜——"

    # nil 「さて、続いてディッシャーでクーラーボックス内のアイスを球状にすくい上げて、中空に６つ放り投げた。」
    "接着，用冰淇淋勺把冷藏箱内的冰淇淋舀成球状，然后向空中抛出6个"

    # nil 「さて、続いてディッシャーでクーラーボックス内のアイスを球状にすくい上げて、中空に６つ放り投げた。」
    "接着，用冰淇淋勺把冷藏箱内的冰淇淋舀成球状，然后向空中抛出6个"

    # nil 「放り投げられたアイスクリームの球は空中で空中を漂うように停止した。」
    "被扔出去的冰淇淋球在空中像飘浮一样停止了"

    # nil 「そしてリオンはすぐさま立ち上がり、何かを唱えると、リオン愛用のアイスクリーム状の杖が召喚された。」
    "然后里昂马上站了起来，咏唱了什么咒语，里昂爱用的冰淇淋状的拐杖被召唤了出来"

    # nil 「バトンのようにくるくると回転させたあと、自分の真正面に浮かぶアイスクリームに向けて、ビリヤードを打つかのような構えを向けた。」
    "像接力棒一样转了一圈后，面向自己正前方的冰淇淋，做出了像打台球一样的姿势"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「Break down！」
    show リオン_基本_杖_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1070.ogg"
    lion リオン_基本_杖_ニタァ "Break down！"
    hide リオン_基本_杖なし_ニタァ

    # nil 「リオンが正面のアイスクリームを、杖でショットすると、そのアイスを起点に、アイスとアイスが空中でぶつかり合ってはじけ飛ぶ。」
    "里昂用手杖击中了正前方的冰淇淋，以那个冰淇淋为起点，冰淇淋和冰淇淋在空中相互碰撞互相弹开"

    # nil 「そして、それぞれ審査員の正面に置かれていたグラスの上に飛び込んだ。」
    "然后，各自落进了放在评委面前的玻璃杯上"

    # nil 「ぱちぱちぱちぱちぱち」
    "噼哩啪啦噼哩啪啦"

    # nil 「審査員から拍手が巻き起こる。」
    "评委们热烈鼓掌"

    # 莲 「（このパフォーマンス必要だったのかな…）」
    lian "（这个表演是必要的吗…）"

    # nil 「無粋な事はさておき、これで審査員全員にアイスが行き渡ったようだ。」
    "姑且抛开这个表演不谈，这样一来，现在所有评委都有冰激凌了"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「さぁ、ちょいと小粋なパフォーマンスを経て、全員にアイスが行き渡りました！　これより試食会開始です！　まずはぁあ！　真冬ちゃんからどうぞ！」
    show 店长_私服_ニヤリ_1 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0262.ogg"
    dinerowner 店长_私服_ニヤリ_1 "那么，经过一场精彩的表演，所有人都有冰淇淋了！现在开始试吃会了！首先是——！请从真冬酱开始！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うん。じゃぁ、お兄ちゃん、リオンちゃん、頂きます」
    show 真冬_私服_基本_微笑み at love69_dong_right with dissolve
    voice "voice/真冬/maf_a1_1483.ogg"
    dong 真冬_私服_基本_微笑み "嗯，那么，欧尼酱，里昂酱，我开动了"

    # 真冬 「もぐ」
    show 真冬_私服_基本_目閉じ at love69_dong_right with dissolve
    voice "voice/真冬/maf_a1_1484.ogg"
    dong 真冬_私服_基本_目閉じ "emmm"
    hide 真冬_私服_基本_微笑み

    # 真冬 「……」
    voice "voice/真冬/maf_a1_1485.ogg"
    dong 真冬_私服_基本_目閉じ "……"

    # 真冬 「まふ」
    show 真冬_私服_基本_まったり at love69_dong_right with dissolve
    voice "voice/真冬/maf_a1_1486.ogg"
    dong 真冬_私服_基本_まったり "嘛呼"
    hide 真冬_私服_基本_目閉じ

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「早くも第一関門クリアです！」
    show 店长_私服_本気 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0263.ogg"
    dinerowner 店长_私服_本気 "这么快就通过第一关了！"
    hide 店长_私服_ニヤリ_1

    # 莲 「いのか…」
    lian "是吗…"

    hide 真冬_私服_基本_まったり with dissolve

    # nil 「続いては、想瑠にゃんの双子の姉「るなちー」さんだ。」
    "接下来是想瑠喵的双胞胎姐姐「瑠那」"

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「うん。ボクは好きなタイプだと思う！例えるならジェイソン・ステーサムのフルチンぐらいに」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%B8%E3%82%A7%E3%82%A4%E3%82%BD%E3%83%B3%E3%83%BB%E3%82%B9%E3%83%86%E3%82%A4%E3%82%B5%E3%83%A0
    # 参考资料：https://www.weblio.jp/content/%E3%83%95%E3%83%AB%E3%83%81%E3%83%B3
    show 瑠那_私服_にっこり at love69_liuna_right with dissolve
    voice "voice/瑠那/lun_a1_0018.ogg"
    na 瑠那_私服_にっこり "嗯，我觉得我是喜欢的那种！就像Jason Statham的金棒……（L:杰森·斯坦森，1967年7月26日－，是一位英国男演员、制片人和前模特，活跃于《两杆大烟枪》和《偷拐抢骗》、《宇宙追缉令》、《非常人贩》、《意大利工作室》、《快克杀手》、《机械师》、《速度与激情》系列电影）"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「中々の高評価です！」
    voice "voice/霧葉/krh_a1_0264.ogg"
    dinerowner 店长_私服_本気 "评价相当高的说！"

    # 莲 「…高評価なのか…」
    lian "…是很高的评价吗…"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ジェイソンのフルチン…じゅるり」
    show リオン_基本_杖_驚き_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1071.ogg"
    lion リオン_基本_杖_驚き_1 "杰森的果胶…黏糊糊的"
    hide リオン_基本_杖_ニタァ

    # 莲 「お前が釣られるなよ！ていうか、ねぇリオンちゃんボクだけを見てよ！」
    # 来玩个梗——但是我还没抽到神里呜呜呜呜呜呜
    lian "你别被钓到了！话说回来，里昂，请好好的看着我！"

    hide 瑠那_私服_にっこり with dissolve

    # nil 「続いて、店長さん。」
    "接下来是店长"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「あ、はい、思ってたより、良い感じですね…」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0265.ogg"
    dinerowner 店长_私服_微笑み "啊，嗯，感觉比我想象的要好……"
    hide 店长_私服_本気

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「案外まともなコメントでした」
    show リオン_基本_杖_無表情 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1072.ogg"
    lion リオン_基本_杖_無表情 "意外的是很认真的评论"
    hide リオン_基本_杖_驚き_1

    # nil 「続いては、想瑠にゃん先生。」
    "接下来是想瑠喵老师"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「は、飛ばしまして」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0266.ogg"
    dinerowner 店长_私服_目閉じ "喔，飞起来了"
    hide 店长_私服_微笑み

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「酷くない！？　ちゃんと食べさせてよ！」
    show 想瑠_スーツ_驚き at love69_xiangliu_right with dissolve
    voice "voice/想瑠/sol_a1_0209.ogg"
    liu 想瑠_スーツ_驚き "好过分啊！？就不能让我正常的恰嘛！"

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「はい、あ～ん」
    show 瑠那_私服_にっこり at love69_liuna_rightest with dissolve
    voice "voice/瑠那/lun_a1_0019.ogg"
    na 瑠那_私服_にっこり "好，啊~嗯"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「あ～ん」
    show 想瑠_スーツ_照れ at love69_xiangliu_right with dissolve
    voice "voice/想瑠/sol_a1_0210.ogg"
    liu 想瑠_スーツ_照れ "啊~嗯"
    hide 想瑠_スーツ_驚き

    # 想瑠 「あむ」
    show 想瑠_スーツ_目閉じ at love69_xiangliu_right with dissolve
    voice "voice/想瑠/sol_a1_0211.ogg"
    liu 想瑠_スーツ_目閉じ "啊嗯"
    hide 想瑠_スーツ_照れ

    # 想瑠 「む！」
    show 想瑠_スーツ_真顔 at love69_xiangliu_right with dissolve
    voice "voice/想瑠/sol_a1_0212.ogg"
    liu 想瑠_スーツ_真顔 "嗯！"
    hide 想瑠_スーツ_目閉じ

    # 想瑠 「……」
    show 想瑠_スーツ_目閉じ at love69_xiangliu_right with dissolve
    voice "voice/想瑠/sol_a1_0213.ogg"
    liu 想瑠_スーツ_目閉じ "……"
    hide 想瑠_スーツ_真顔

    # 想瑠 「えーこのぉ、口に入れた瞬間広がる優しい甘みといますか―」
    show 想瑠_スーツ_照れ at love69_xiangliu_right with dissolve
    voice "voice/想瑠/sol_a1_0214.ogg"
    liu 想瑠_スーツ_照れ "啊——这个——放进嘴里的瞬间散发出来的温柔的甜味嘛——"
    hide 想瑠_スーツ_目閉じ

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「では続いて、姉さんの番です」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0267.ogg"
    dinerowner 店长_私服_微笑み "那么，接下来轮到姐姐了"
    hide 店长_私服_目閉じ

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「全部言わせろよ！　美味しかったよ！」
    show 想瑠_スーツ_ぶわ at love69_xiangliu_right with dissolve
    voice "voice/想瑠/sol_a1_0215.ogg"
    liu 想瑠_スーツ_ぶわ "让我全部说完啊！很好吃！"
    hide 想瑠_スーツ_照れ

    hide 想瑠_スーツ_ぶわ with dissolve
    hide 瑠那_私服_にっこり with dissolve

    hide 店长_私服_微笑み
    show 店长_私服_にっこり:
        zoom 1.5
        xalign 0.11
        yalign 0.015
        linear 0.3 xalign 0.52

    hide リオン_基本_杖_無表情
    show リオン_基本_杖_無表情:
        zoom 1.5
        yalign 0.07
        xalign 0.5
        linear 0.3 xalign 0.89

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「はい姉さん。あーん」
    voice "voice/霧葉/krh_a1_0268.ogg"
    dinerowner 店长_私服_にっこり "来，姐姐，啊~嗯"

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「あ～ん♪」
    show アシュリー_私服_にっこり at love69_atri_left with dissolve
    voice "voice/アシュリー/ash_a1_0051.ogg"
    atri アシュリー_私服_にっこり "啊~嗯♪"

    # 亚十礼 「…もぐもぐ…うみゃい！」
    show アシュリー_私服_驚き at love69_atri_left with dissolve
    voice "voice/アシュリー/ash_a1_0052.ogg"
    atri アシュリー_私服_驚き "……emm……真不戳！"
    hide アシュリー_私服_にっこり

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「くすくす。姉さん、可愛いですよ」
    show 店长_私服_ニヤリ at love69_wuye_center with dissolve
    voice "voice/霧葉/krh_a1_0269.ogg"
    dinerowner 店长_私服_ニヤリ "啊哈哈，姐姐好可爱哦"
    hide 店长_私服_にっこり

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「わはーい！」
    show アシュリー_私服_にっこり at love69_atri_left with dissolve
    voice "voice/アシュリー/ash_a1_0053.ogg"
    atri アシュリー_私服_にっこり "哇——咿！"
    hide アシュリー_私服_驚き

    hide 店长_私服_ニヤリ with dissolve
    hide アシュリー_私服_にっこり with dissolve

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「じー」
    show 想瑠_スーツ_真顔 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0216.ogg"
    liu 想瑠_スーツ_真顔 "盯——"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「…よしよし」
    show リオン_基本_杖_にっこり_1 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_1073.ogg"
    lion リオン_基本_杖_にっこり_1 "……好孩子好孩子"
    hide リオン_基本_杖_無表情

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「わーい」
    show 想瑠_スーツ_にっこり at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0217.ogg"
    liu 想瑠_スーツ_にっこり "哇——咿！"
    hide 想瑠_スーツ_真顔

    hide 想瑠_スーツ_にっこり with dissolve

    # nil 「さて、最後。俺的には最高の難関。心愛だ。」
    "那么，最后。在我看来是最难的一关。心爱"

    # 心爱觉醒！

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「……」
    show 心愛_私服_基本_覚醒03 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1825.ogg"
    ai 心愛_私服_基本_覚醒03 "……"

    # nil 「甘い物が大好きな心愛ちゃんだが、やはり戦慣れをしているだけあって、評価は厳しい物になるだろう。」
    "虽然是非常喜欢甜食的心爱酱，但正因为习惯了战斗，所以评价会很严苛吧"

    # nil 「今まで見たことない表情してるし。」
    "至今为止都没有见过的表情"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ご、ごくり…」
    show リオン_基本_杖_無表情_1 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_1074.ogg"
    lion リオン_基本_杖_無表情_1 "咽口水……"
    hide リオン_基本_杖_にっこり_1

    # BGM 停！
    stop music fadeout 2.0

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「では…頂きます」
    show 心愛_私服_基本_無表情 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1826.ogg"
    ai 心愛_私服_基本_無表情 "那么……我开动了"
    hide 心愛_私服_基本_覚醒03

    # nil 「心愛は両手を合わせたのち、スプーンを拾い上げる。残光が銀色の軌跡を描く。」
    "心爱双手合十后，把勺子拿起来，余辉勾勒出银色的轨迹"

    # nil 「店内は静寂につまれ、心愛の持ったスプーンが空を裂く音すら聞こえてくるようだ。」
    "店内寂静无声，甚至可以听到心爱手里的勺子划破天空的声音"

    # nil 「ざくっ」
    "嚓"

    # nil 「心愛のスプーンがアイスクリームに差し込まれる。」
    "心爱的勺子插进冰淇淋里"

    # nil 「そして、ゆっくりと、心愛は表情を変えぬま、アイスクリームを口に運んだ。」
    "然后，慢慢地，心爱面不改色地把冰淇淋送到嘴边"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぁむ」
    show 心愛_私服_基本_もぐもぐ at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1827.ogg"
    ai 心愛_私服_基本_もぐもぐ "啊呜"
    hide 心愛_私服_基本_無表情

    # 心爱 「……」
    voice "voice/心愛/cca_a1_1828.ogg"
    ai 心愛_私服_基本_もぐもぐ "……"

    # 心爱 「…………」
    show 心愛_私服_基本_覚醒04 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1829.ogg"
    ai 心愛_私服_基本_覚醒04 "…………"
    hide 心愛_私服_基本_もぐもぐ

    # nil 「心愛の動きが固まる。」
    "心爱的动作凝固了"

    # nil 「心愛の表情は険しいま、ピクリとも動かない。」
    "心爱表情严肃，纹丝不动"

    # nil 「リオンと俺の頬には冷や汗が走った。」
    "里昂和我的脸上冒出了冷汗"

    # 心爱 「…リカバリーモードを起動します、各セクションのバックアップを開始」
    voice "voice/心愛/cca_a1_1830.ogg"
    ai 心愛_私服_基本_覚醒04 "…………Recovery Mode启动中，各部分Backup开始（L:Recovery Mode是Linux系统的恢复模式，举例来说，基于Linux的Android就有，一般关机状态按住电源键+音量键+就能进入Recovery Mode，可以恢复出厂）"

    # 心爱 「ぷるるるるるる！　ぷるるるるるるる！！ぷるるるるるるるる！！　ちっ、留守電か…」
    # 参考资料：https://www.ymobile.jp/support/faq/view/23550
    show 心愛_私服_基本_覚醒03 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1831.ogg"
    ai 心愛_私服_基本_覚醒03 "噗噜噜噜噜噜噜！噗噜噜噜噜噜噜！！噗噜噜噜噜噜噜噜噜！！切，答录机吗……（L:答录机是很有日本特色的手机功能，来电长时间无人接听自动接听电话并转入录音机，可以留言给电话的主人，中国手机有这个功能的不多，中兴手机有这个功能）"
    hide 心愛_私服_基本_覚醒04

    # 心爱 「天井から…夥しい数のメラニン色素が降り注いで…夥しい数のメラニン…」
    show 心愛_私服_基本_覚醒04 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1832.ogg"
    ai 心愛_私服_基本_覚醒04 "从天花板上……大量的黑色素雨点般落下……大量的黑色素……"
    hide 心愛_私服_基本_覚醒03

    # 心爱 「心愛ちゃんスイッチ！！！　イグニッション！！！」
    show 心愛_私服_基本_覚醒03 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1833.ogg"
    ai 心愛_私服_基本_覚醒03 "心爱酱switch！！！Ignition！！！（L:switch，开关；Ignition，点火）"
    hide 心愛_私服_基本_覚醒04

    # nil 「カチッ」
    "咔嗒"

    # 心爱 「…………」
    show 心愛_私服_基本_覚醒04 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1834.ogg"
    ai 心愛_私服_基本_覚醒04 "…………"
    hide 心愛_私服_基本_覚醒03

    # 心爱发射
    play sound "voice/effect/05_爆発3～ダイナマイト.ogg"

    hide 心愛_私服_基本_覚醒04
    show 心愛_私服_基本_覚醒04:
        zoom 1.5
        xalign 0.53
        yalign -0.09
        linear 0.15 yalign 3.0

    # 挪走小头像
    $ sideimagesize.SideImageXalign = 99.99
    $ sideimagesize.SideImageYalign = 99.99
    $ sideimagesize.SideImageZoom = 1.0

    # 心爱 「ぷしゅー！」
    voice "voice/心愛/cca_a1_1835.ogg"
    ai "咻——————！"

    # nil 「心愛は、天井を突き破り、遥か上空へと発射した。」
    "心爱冲破了天花板，向遥远的高空发射"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「…くすっ。合格…ですね…おめでとうございます」
    show 店长_私服_目閉じ at love69_wuye_center with dissolve
    voice "voice/霧葉/krh_a1_0270.ogg"
    dinerowner 店长_私服_目閉じ "……欸嘿。合格了呢……恭喜你"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 『Juck pot！！Yeah baby！！』
    hide リオン_基本_杖_無表情_1
    show リオン_基本_杖なし_にっこり at love69_lion_right
    with dissolve
    voice "voice/リオン/ron_a1_1075.ogg"
    lion リオン_基本_杖なし_にっこり "Juck pot！！Yeah baby！！（L:这里原作前面的英文打错了，应该是Jackpot！，前面一周目心爱和真冬一起说过，Jackpot是正中头奖的意思，霓虹的英语水平……）"

    # nil 「パシィン！」
    "啪唧！"

    # nil 「俺とリオンのハイタッチの音が店内に響き渡る。」
    "我和里昂的击掌声响彻店内"

    # 心爱在最右的参数
    transform love69_xinai_rightest:
        zoom 1.5
        xalign 1.19
        yalign -0.09

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「やあ」
    show 心愛_私服_基本_ニタァ at love69_xinai_rightest with dissolve
    voice "voice/心愛/cca_a1_1836.ogg"
    ai 心愛_私服_基本_ニタァ "呀"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「おかえりおん」
    show リオン_基本_杖なし_微笑み at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_1076.ogg"
    lion リオン_基本_杖なし_微笑み "欢迎回来（L:这句和下面真冬那句都玩了名字的梗）"
    hide リオン_基本_杖なし_にっこり

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ただいまふゆ」
    show 真冬_私服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1487.ogg"
    dong 真冬_私服_基本_無表情 "我回来啦"

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「おめでとう」
    voice "voice/アシュリー/ash_a1_0054.ogg"
    atri アシュリー_私服_にっこり "恭喜你们"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「おめでとう」
    voice "voice/想瑠/sol_a1_0218.ogg"
    liu 想瑠_スーツ_にっこり "恭喜你们"

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「おめでとう」
    voice "voice/瑠那/lun_a1_0020.ogg"
    na 瑠那_私服_微笑 "恭喜你们"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「おめでとう」
    show 真冬_私服_基本_嬉しい at love69_left with dissolve
    voice "voice/真冬/maf_a1_1488.ogg"
    dong 真冬_私服_基本_嬉しい "恭喜你们"
    hide 真冬_私服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「おめでとう」
    show 心愛_私服_基本_にっこり at love69_xinai_rightest with dissolve
    voice "voice/心愛/cca_a1_1837.ogg"
    ai 心愛_私服_基本_にっこり "恭喜你们"
    hide 心愛_私服_基本_ニタァ

    # 鼓掌声
    play sound "voice/effect/05_拍手ホール.ogg"

    # nil 「俺盛大な拍手が響き渡る。ちょっと怖い。」
    "热烈的掌声响起，有点蛤人"

    hide 真冬_私服_基本_嬉しい with dissolve
    hide 心愛_私服_基本_にっこり with dissolve
    play music bgmfifteen fadein 2.0
    hide 店长_私服_目閉じ love69_wuye_left
    show 店长_私服_微笑み:
        zoom 1.5
        yalign 0.015
        xalign 0.52
        linear 0.3 xalign 0.11

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「じゃぁ…これで…店を…貸して貰えるってことですね…」
    show リオン_基本_杖なし_嬉しい at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_1077.ogg"
    lion リオン_基本_杖なし_嬉しい "那么…这样的话……就可以把店借给我了吧…"
    hide リオン_基本_杖なし_微笑み

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「そうですね。ただし、まずは私のお店をお手伝いしてもらう所から…になりますよ？」
    voice "voice/霧葉/krh_a1_0271.ogg"
    dinerowner 店长_私服_微笑み "是啊。不过，首先要从帮我开店开始"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「へ？」
    show リオン_基本_杖なし_驚き at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_1078.ogg"
    lion リオン_基本_杖なし_驚き "欸？"
    hide リオン_基本_杖なし_嬉しい

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「だって、アイス屋を開く前に彼氏が卒業しなきゃ…ですよ？せっかくなら一緒に始めたらどうですか？　家賃はこちらが負担しますし…ね、想瑠にゃん？」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0272.ogg"
    dinerowner 店长_私服_目閉じ "因为，在开冰淇淋店之前男朋友必须得先毕业…对吧？为什么不一起开始呢？房租由我来负担…对吧，想瑠喵？"
    hide 店长_私服_微笑み

    # 想瑠在最左的参数
    transform love69_xiangliu_leftest:
        zoom 1.5
        xalign -0.5
        yalign 0.07

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「うむ。あと半年ぐらい、うちのクラスで過ごしなよ。勝手はわかってるだろ…？」
    show 想瑠_スーツ_見下し at love69_xiangliu_leftest with dissolve
    voice "voice/想瑠/sol_a1_0219.ogg"
    liu 想瑠_スーツ_見下し "嗯，再在我们班上待半年吧，在班上再花一点时间吧，你知道自己要做什么吧……"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「それって…もしかして…もう一度…蓮くん達と…！」
    show リオン_基本_杖なし_微笑み at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_1079.ogg"
    lion リオン_基本_杖なし_微笑み "那个…难道……再一次…和莲他们…！"
    hide リオン_基本_杖なし_驚き

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「失った時間を取り戻すと良い。夢を叶えるのはそれからでも遅くはあるまい。るなちー？」
    show 想瑠_スーツ_ニヤリ at love69_xiangliu_leftest with dissolve
    voice "voice/想瑠/sol_a1_0220.ogg"
    liu 想瑠_スーツ_ニヤリ "把失去的时间找回来就好了。等到那时再实现梦想也不迟，瑠那亲"
    hide 想瑠_スーツ_見下し

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「親御さんへの連絡はボクからやっておくから、心配いらないよー」
    voice "voice/瑠那/lun_a1_0021.ogg"
    na 瑠那_私服_にっこり "我会联系你父母的，不用担心哦"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「つーことで、９月から仲良くやっていこうと思うんだけど、いかがだろう」
    show 想瑠_スーツ_見下し at love69_xiangliu_leftest with dissolve
    voice "voice/想瑠/sol_a1_0221.ogg"
    liu 想瑠_スーツ_見下し "顺便说一句，我想从9月份开始和你好好相处，怎么样？"
    hide 想瑠_スーツ_ニヤリ

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「は…はいっ！　是非そうさせてください！　宜しくお願いします！」
    show リオン_基本_杖なし_にっこり at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_1080.ogg"
    lion リオン_基本_杖なし_にっこり "哈…嗯！请一定让我这么做！请多关照！"
    hide リオン_基本_杖なし_微笑み

    hide 想瑠_スーツ_見下し with dissolve
    hide 店长_私服_目閉じ with dissolve
    hide リオン_基本_杖なし_にっこり
    show リオン_基本_杖なし_嬉しい:
        zoom 1.5
        yalign 0.07
        xalign 0.89
        linear 0.3 xalign 0.5

    # nil 「リオンは即決して、担任からの提案を受け入れた。」
    "里昂当场决定，接受了班主任的提案"

    # 莲 「良かったな、リオン。これで全て元通りだな」
    lian "太好了，里昂。这样就全部OK了"

    # 里昂 「えへ…じゃぁ…これからも…そして、これから、宜しくお願いします、蓮くん！」
    voice "voice/リオン/ron_a1_1081.ogg"
    lion リオン_基本_杖なし_嬉しい "欸嘿嘿嘿………那么…接下来也请多多关照，莲君！"

    # 莲 「あ、よろしくな」
    lian "啊，请多关照"

    # 里昂 「はーい！」
    show リオン_基本_杖なし_にっこり_1  at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1082.ogg"
    lion リオン_基本_杖なし_にっこり_1 "好~！"
    hide リオン_基本_杖なし_嬉しい

    # nil 「リオンは満面の笑みで、俺に応えた。」
    "里昂满脸笑容地回应了我"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「わーい！　リオンちゃん転校生なのー！　やったー！」
    show 心愛_私服_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1838.ogg"
    ai 心愛_私服_基本_驚き "哇——咿！里昂酱是转学生啊！好耶！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うん。私達からも、お手柔らかによろしくね」
    show 真冬_私服_基本_にっこり at love69_left with dissolve
    voice "voice/真冬/maf_a1_1489.ogg"
    dong 真冬_私服_基本_にっこり "嗯，我们也请你多多关照啦"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「はーい！　真冬ちゃん、心愛ちゃん！」
    show リオン_基本_杖なし_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1083.ogg"
    lion リオン_基本_杖なし_にっこり "好~！真冬酱、心爱酱！"
    hide リオン_基本_杖なし_にっこり_1

    # nil 「リオンは真冬と心愛と手を取り合って触れあっている。」
    "里昂和真冬还有心爱互相手牵着手"

    # 莲 「これで全ては一つに…めでたしめでたし…という事かな」
    lian "这样的话全部就变成一个大家了…是可喜可贺的事吧…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「めでたしめでたし！」
    show 心愛_私服_基本_もぐもぐ at love69_right with dissolve
    voice "voice/心愛/cca_a1_1839.ogg"
    ai 心愛_私服_基本_もぐもぐ "可喜可贺可喜可贺！"
    hide 心愛_私服_基本_驚き

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「あ！　蓮くん！　そろそろ時間だ！」
    show リオン_基本_杖なし_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1084.ogg"
    lion リオン_基本_杖なし_驚き "啊！莲君！差不多到时间了！"
    hide リオン_基本_杖なし_にっこり

    # 莲 「む、あ、そうか…忘れてたな」
    lian "嗯，啊，是吗…我忘了"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「なんでぇ、これからデートけ？」
    voice "voice/想瑠/sol_a1_0222.ogg"
    liu 想瑠_スーツ_ニヤリ "什么啊，现在开始约会吗？"

    # 莲 「あ、二人でお祝いをしようかなと思って」
    lian "啊，我想两个人一起庆祝一下"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「おやおや。勝負が決まる前から、パーティは予約済みとは…」
    voice "voice/霧葉/krh_a1_0273.ogg"
    dinerowner 店长_私服_目閉じ "哎呀哎呀，在决定胜负之前，派对就已经预定好了……"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「それだけ自信作だったってことで！」
    show リオン_基本_杖なし_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1085.ogg"
    lion リオン_基本_杖なし_ニタァ "就是这么自信的作品！"
    hide リオン_基本_杖なし_驚き

    # 莲 「それじゃ、みんな、今日はありがとう」
    lian "那么，今天就谢谢大家了"

    # nil 「俺とリオンは、審査員の方々に頭を下げる。」
    "我和里昂向评委们鞠躬"

    hide 真冬_私服_基本_にっこり with dissolve
    hide 心愛_私服_基本_もぐもぐ with dissolve

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「二人ともばいばーい！　またね－！」
    voice "voice/アシュリー/ash_a1_0055.ogg"
    atri アシュリー_私服_にっこり "再见了，你们俩！再会啦！"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「せいぜい、バカンスを楽しんでくるんだな」
    voice "voice/想瑠/sol_a1_0223.ogg"
    liu 想瑠_スーツ_見下し "活力满满地，好好享受假期吧"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「セックスもね」
    voice "voice/真冬/maf_a1_1490.ogg"
    dong 真冬_私服_基本_ニタァ "Sex也是"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「キャー☆　エッチー☆」
    voice "voice/心愛/cca_a1_1840.ogg"
    ai 心愛_私服_基本_ニタァ "呀——☆H——☆"

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「あでぃおーす！　何かあったら、帽子の世話は任せてね！」
    voice "voice/瑠那/lun_a1_0022.ogg"
    na 瑠那_私服_にっこり "Adiós！如果有什么需要，我可以帮忙照顾你的帽子！"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「しっかり手をつないで帰るんですよ」
    voice "voice/霧葉/krh_a1_0274.ogg"
    dinerowner 店长_私服_ニヤリ "要紧紧牵着手回去哦"

    # nil 「審査員の方々は、俺達を手を振って見送ってくれる。」
    "评委们会向我们挥手送行"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「あ、そだ、蓮くん蓮くん」
    show リオン_基本_杖なし_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1086.ogg"
    lion リオン_基本_杖なし_微笑み "啊，对了，莲君莲君"
    hide リオン_基本_杖なし_ニタァ

    # 莲 「はい、なんでしょう」
    lian "嗯，什么事呢"

    # # 大里昂在中间的参数
    # transform love69_lion_bg_center:
    #     zoom 1.5
    #     xalign 0.44
    #     yalign 0.164

    # 里昂 「だーいすき…ちゅっ」
    hide リオン_基本_杖なし_微笑み
    show リオン_大_基本_杖なし_キス at love69_lion_bg_center with dissolve
    voice "voice/リオン/ron_a1_1087.ogg"
    lion リオン_基本_杖なし_キス "最喜欢……啾"

    # みんな（大伙） 「『きゃー！』」
    # 因为是真冬头像，所以就ALL IN 真冬喽~aio_dong
    voice "voice/真冬/maf_a1_1491.ogg"
    # voice "voice/霧葉/krh_a1_0275.ogg"
    # voice "voice/心愛/cca_a1_1841.ogg"
    # voice "voice/アシュリー/ash_a1_0056.ogg"
    # voice "voice/瑠那/lun_a1_0023.ogg"
    # voice "voice/想瑠/sol_a1_0224.ogg"

    aio_dong 真冬_私服_基本_微笑み2_1 "『啊！』"

    # 莲 「お、おう…」
    lian "哦，嗯…"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「見せつけてくれますね…」
    voice "voice/霧葉/krh_a1_0276.ogg"
    dinerowner 店长_私服_目閉じ "全部都看到了哦……"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「よーし！　今日は飲むぞ！　酒を出せ！」
    voice "voice/想瑠/sol_a1_0225.ogg"
    liu 想瑠_スーツ_ニヤリ "好！今天我要喝酒！把酒都拿出来！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「心愛ちゃんもちゅー！」
    voice "voice/真冬/maf_a1_1492.ogg"
    dong 真冬_私服_基本_キス "心爱酱也来啾——"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ちゅー！」
    voice "voice/心愛/cca_a1_1842.ogg"
    ai 心愛_私服_基本_キス "啾——"

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「るなちーかわい」
    voice "voice/アシュリー/ash_a1_0057b.ogg"
    atri アシュリー_私服_にっこり "瑠那亲真可爱"

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「ギャラリーが騒ぎ出して、色々な物が宙を舞い始める。俺達は、それに追い出されるようにして、店の外に飛び出した。」
    voice "voice/瑠那/lun_a1_0024.ogg"
    na 瑠那_私服_はう "亚十礼也可爱"

    # nil 「ギャラリーが騒ぎ出して、色々な物が宙を舞い始める。俺達は、それに追い出されるようにして、店の外に飛び出した。」
    "画面开始骚动，各种各样的东西开始在空中飞舞。我们好像被那个赶出去一样，到了店外"

    # 场景切回通学路街道
    play music bgmfourteen fadeout 2.0 fadein 2.0
    scene 通学路c_昼 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ふう…騒がしかったね、随分と…」
    show リオン_基本_杖なし_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1088.ogg"
    lion リオン_基本_杖なし_微笑み "呼……真是吵闹呢……"

    # 莲 「そうだな…。上手く行って良かったよ」
    lian "是啊……一切顺利真是太好了"

    # 里昂 「ほんと、一重にこれは蓮くんのおかげだよ…。私の夢も、恋も叶えてくれて、本当にありがとう！」
    show リオン_基本_杖なし_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1089.ogg"
    lion リオン_基本_杖なし_驚き "真的，这多亏了莲君……我的梦想和恋爱都能实现，真的非常感谢！"
    hide リオン_基本_杖なし_微笑み

    # 莲 「違うな。俺とリオン一緒に叶えたんだ。だから、俺からもありがとうだ」
    lian "不是啊。是里昂和我一起实现的。所以，我也要谢谢你"

    # 里昂 「えへ…じゃぁ、ありがとうの…ちゅー…しよ？」
    show リオン_基本_杖なし_微笑み_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1090.ogg"
    lion リオン_基本_杖なし_微笑み_1 "欸嘿嘿……那么，谢谢的啾——……来吧？"
    hide リオン_基本_杖なし_驚き

    # 莲 「あ、そうだな。リオン、おいで」
    lian "啊，是啊。里昂，来吧"

    # 里昂 「ん…すーき…ん…っ！」
    show リオン_基本_杖なし_キス at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1091.ogg"
    lion リオン_基本_杖なし_キス "嗯…suki…呜…！"
    hide リオン_基本_杖なし_微笑み_1

    # 莲 「うおっ！」
    lian "喔哦！"

    # nil 「リオンと俺の唇が触れるその一歩手前で、リオンは首を振った。」
    "就在里昂和我的嘴唇接触的前一步，里昂摇了摇头"

    # 里昂 「時間だよ」
    show リオン_基本_杖なし_無表情_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1092.ogg"
    lion リオン_基本_杖なし_無表情_1 "时间到了哦"
    hide リオン_基本_杖なし_キス

    # nil 「リオンの視線は、先ほどのダイナーに向いている。」
    "里昂的视线转向了刚才的Diner"

    # nil 「店の奥から聞こえてくるのは…。」
    "从店里传来的是…"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「『心愛ちゃん…ほら、こ触って…』」
    voice "voice/真冬/maf_a1_1493.ogg"
    dong 真冬_私服_基本_ジト目3_1 "『心爱酱…来，摸摸这里…』"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「『ほげえ　まふまふちゃんが発情したー！』」
    voice "voice/心愛/cca_a1_1843.ogg"
    ai 心愛_私服_基本_ぐるぐる "『呜欸欸欸欸——嘛呼嘛呼酱发情了——！』"

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「『心愛ちゃんのおっぱいもみたい』」
    voice "voice/瑠那/lun_a1_0025.ogg"
    na 瑠那_私服_はう "心爱酱的欧派让我康康"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「『ゲェー！　次はるなちーだー！』」
    voice "voice/心愛/cca_a1_1844.ogg"
    ai 心愛_私服_基本_驚き "『欸——接着是瑠那亲吗——！』"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「『姉さん、ほら、口開けて…』」
    voice "voice/霧葉/krh_a1_0277.ogg"
    dinerowner 店长_私服_にっこり_1 "『姐姐，来，张开嘴……』"

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「『ぁ…んぅ…ま、マジで…こでする…の…？』」
    voice "voice/アシュリー/ash_a1_0058.ogg"
    atri アシュリー_私服_にっこり "『啊……嗯……真、真的……要在这里做……吗……？』"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「『こっちでは既におっぱじめてるよぉ…』」
    voice "voice/心愛/cca_a1_1845.ogg"
    ai 心愛_私服_基本_ポカーン "『这边已经都开始了吗……』"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「『くっくっく…はぁーっはっはっはっは！！』」
    voice "voice/想瑠/sol_a1_0226.ogg"
    liu 想瑠_スーツ_ニヤリ "『嘿嘿嘿嘿…啊哈哈哈哈哈！！』"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「『い、いつも通りだァー！！！』」
    voice "voice/心愛/cca_a1_1846.ogg"
    ai 心愛_私服_基本_ぶわー "『还、还是老样子！！！』"

    # 心爱 「『こ、この流れだと…私も…私も…ぁ、はぅう…んぅ…や、溢れちゃぁ…まふまふちゃぁん…』」
    voice "voice/心愛/cca_a1_1847.ogg"
    ai 心愛_私服_基本_号泣1 "『这、这样的话我……我也…啊，哈呜……嗯…呀，要溢出来了……嘛呼嘛呼酱』"

    # 莲 「…帰るか」
    lian "…回去吗？"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「そ、そだね…こら辺に居たら私達もどうにかなっちゃうもんね…」
    show リオン_基本_杖なし_悲しい2_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1093.ogg"
    lion リオン_基本_杖なし_悲しい2_1 "是啊，是啊…在这附近的话我们也会没办法的……"
    hide リオン_基本_杖なし_無表情_1

    # nil 「リオンは、俺の手をぎゅっと強く握ってくる。かなり熱く、ちょっとだけ汗ばんでいるようだ。」
    "里昂紧紧地握着我的手。相当热，好像有点出汗了"

    # 莲 「でもまぁ、帰ったら…これ、食うよな…」
    lian "但是，回去的话…先恰这个吧…"

    # 里昂 「…！　う、うん…一緒に食べよ…」
    show リオン_基本_杖なし_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1094.ogg"
    lion リオン_基本_杖なし_にっこり "…！嗯，嗯…一起恰吧…"
    hide リオン_基本_杖なし_悲しい2_1

    # nil 「リオンは赤面しながら、俺の肩に体重を預けてきた。俺はそのリオンの肩を抱きながら、」
    "里昂红着脸把体重寄放在了我的肩上。我抱着里昂的肩膀"

    # nil 「この不思議だけど優しくて可愛らしい彼女を、大事にしていこうと、改めて決意した。」
    "我再次下定决心要好好珍惜这个虽然不可思议但又温柔又可爱的她"

    # 里昂 「…だいすき…ちゅっ♪」
    show リオン_大_基本_杖なし_キス at love69_lion_bg_center with dissolve
    voice "voice/リオン/ron_a1_1095.ogg"
    lion リオン_基本_杖なし_キス "最喜欢…啾♪"
    hide リオン_基本_杖なし_にっこり

    # 画面切回 Diner
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 霧葉ちゃんのお店 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 进 OP（full ver.）
    play music bgmone fadeout 1.0

    # nil 「そして、少しの月日が流れた。」
    "然后，一段时间过去了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「リオンちゃーん！！　想瑠にゃんが私のパンケーキの上のアイス食べちゃったよー！！」
    show 心愛_私服_基本_ぶわー at love69_right with dissolve
    voice "voice/心愛/cca_a1_1848.ogg"
    ai 心愛_私服_基本_ぶわー "里昂酱！！想瑠喵把我的煎饼和冰淇淋都吃掉了啊——！！"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ウェヒヒヒ！　余所見をするからいけないのさ！」
    show 想瑠_スーツ_ニヤリ at love69_xiangliu_left with dissolve
    voice "voice/想瑠/sol_a1_0227.ogg"
    liu 想瑠_スーツ_ニヤリ "噫嘻嘻嘻嘻！你什么都没看见！！"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「お行儀良く食べなさい！」
    show リオン_基本_杖なし_ジト目 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1096.ogg"
    lion リオン_基本_杖なし_ジト目 "请规规矩矩地吃饭！"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ギャース！」
    show 想瑠_スーツ_ぶわ at love69_xiangliu_left with dissolve
    voice "voice/想瑠/sol_a1_0228.ogg"
    liu 想瑠_スーツ_ぶわ "嘎呜——！"
    hide 想瑠_スーツ_ニヤリ

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「もうっいっちょ！」
    show 瑠那_私服_笑顔 at love69_liuna_rightest with dissolve
    voice "voice/瑠那/lun_a1_0026.ogg"
    na 瑠那_私服_笑顔 "再来一次！"

    # 这个语句是针对亚十礼设计的参数，能够调整亚十礼在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 14.3
    $ sideimagesize.SideImageZoom = 1.0

    # 亚十礼 「させるか！」
    show アシュリー_私服_にっこり at love69_atri_leftest with dissolve
    voice "voice/アシュリー/ash_a1_0059.ogg"
    atri アシュリー_私服_にっこり "岂能让你得逞！"

    # 这个语句是针对瑠那设计的参数，能够调整瑠那在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.11
    $ sideimagesize.SideImageYalign = -10.46
    $ sideimagesize.SideImageZoom = 1.0

    # 瑠那 「ぶえ」
    show 瑠那_私服_悲しみ at love69_liuna_rightest with dissolve
    voice "voice/瑠那/lun_a1_0027.ogg"
    na 瑠那_私服_悲しみ "呜欸"
    hide 瑠那_私服_笑顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まふ」
    voice "voice/真冬/maf_a1_1494.ogg"
    dong 真冬_私服_基本_無表情 "嘛呼"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「まふ」
    voice "voice/霧葉/krh_a1_0278.ogg"
    dinerowner 店长_私服_目閉じ "嘛呼"

    hide リオン_基本_杖なし_ジト目
    show リオン_基本_杖なし_見下し at love69_lion_center
    with dissolve

    # nil 「カランコロンカラーン」
    "叮当叮当"

    hide 想瑠_スーツ_ぶわ with dissolve
    hide 心愛_私服_基本_ぶわー with dissolve
    hide アシュリー_私服_にっこり with dissolve
    hide 瑠那_私服_悲しみ with dissolve

    # 铃声
    play sound "/voice/effect/カウベル.ogg"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    hide リオン_基本_杖なし_見下し
    show リオン_基本_杖なし_微笑み at love69_lion_center
    with dissolve

    # 里昂 「あ、いらっしゃいま…えへ、こんにちは、蓮くん！」
    voice "voice/リオン/ron_a1_1097.ogg"
    lion リオン_基本_杖なし_微笑み "啊，欢迎光…欸嘿嘿，你好，莲君！"

    # 莲 「ようリオン。繁盛してるか？」
    lian "哟，里昂。生意好吗？"

    # 里昂 「ん♪　いつも通り、賑やかだよ！」
    show リオン_基本_杖なし_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1098.ogg"
    lion リオン_基本_杖なし_にっこり "嗯♪一如既往，热闹非凡！"
    hide リオン_基本_杖なし_微笑み

    # 莲 「厄介な常連客が居座ってる…てな」
    lian "麻烦的常客都在啊……"

    # 里昂 「そーいう事言わないの！」
    show リオン_基本_杖なし_ジト目 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1099.ogg"
    lion リオン_基本_杖なし_ジト目 "别这么说嘛！"
    hide リオン_基本_杖なし_にっこり

    # 莲 「ほらよ。イギリスの女王様からの注文書だ。そんで、あと南アフリカの少年からもな」
    lian "你看，这是英国女王发来的订单。还有一个南非少年发来的"

    # 里昂 「はーい！　いつもいつもお疲れ様！」
    show リオン_基本_杖なし_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1100.ogg"
    lion リオン_基本_杖なし_にっこり "哈！一直以来辛苦了！"
    hide リオン_基本_杖なし_ジト目

    # 莲 「お前のためならお安い御用だ」
    lian "如果是为了你的话都可以"

    # nil 「リオンのアイスは予想外のヒットを飛ばした。」
    "里昂的冰淇淋意外地大受欢迎"

    # nil 「俺達は学園を卒業後、世界各地を飛び回り、ありとあらゆる子供達にアイスを配ってまわった。」
    "我们从学园毕业后，在世界各地飞来飞去，给各种各样的孩子们分发冰淇淋"

    # nil 「その結果、子供達から口コミ的に広がり、やがて世界中の大人達は争う事より、このリオンのアイスを食べる事に集中しはじめた。」
    "结果，通过孩子们口口相传地传播开来，不久全世界的大人们停止争吵，集中精力吃里昂的这个冰淇淋"

    # nil 「同じカップのアイスを二人で食べる」という行為が世界中でブームとなり、そしていつしか、平和の象徴として国連に認定されるまでにもなった。」
    "「两个人一起吃同一个杯子里的冰淇淋」的行为在全世界掀起了热潮，然后不知不觉间，就被联合国认定为和平的象征"

    # nil 「現在の国連の旗は、アイスクリームを運ぶハトが描かれている。」
    "现在的联合国国旗上画着一只运送冰淇淋的鸽子"

    # nil 「そして、気づいたら、世界は戦争のない平和な世界になっていた。」
    "然后，回过神来，世界变成了没有战争的和平世界"

    # nil 「そんなこんなで、今では大忙し。制作に集中するリオンの代わりに、常に世界を飛び回る人生だ。」
    "就是这样，现在很忙。代替专心制作的里昂，我过上了经常在世界各地间飞行的人生"

    # 里昂 「ねぇねぇ、今日は、ずっと一緒に居られる？」
    show リオン_基本_杖なし_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1101.ogg"
    lion リオン_基本_杖なし_微笑み "呐呐，今天，能一直呆在一起嘛？"
    hide リオン_基本_杖なし_にっこり

    # 莲 「ん？　そうだな。今日は大丈夫だろ」
    lian "嗯？是啊。今天应该没问题吧"

    # 里昂 「じゃぁー…また、前みたいに…一緒にアイスたべよー？」
    show リオン_基本_杖なし_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1102.ogg"
    lion リオン_基本_杖なし_嬉しい "那么……再像以前那样…一起吃冰淇淋吧？"
    hide リオン_基本_杖なし_微笑み

    # 莲 「おう。そうだな」
    lian "哦，是啊"

    # nil 「リオンとゆっくり過ごすのは久しぶりだ。今日は沢山可愛がってあげよう。」
    "好久没和里昂悠闲地度过了。今天就好好地疼爱她吧"

    # nil 「リオンの頭を撫でながら、テラス席でたむろする常連客を横目で見る。」
    "一边抚摸着里昂的头，一边斜视着在露天座位上聚集的常客"

    # 莲 「あいつらどうするか…」
    lian "她们怎么办呢…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あ！　あのカップル二人だけでお楽しみするつもりですぞ！」
    voice "voice/心愛/cca_a1_1849.ogg"
    ai 心愛_私服_基本_不機嫌 "啊！那对CP打算单独享受一下呢！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そうはさせるか！　心愛ちゃん、捕まえよう！」
    voice "voice/真冬/maf_a1_1495.ogg"
    dong 真冬_私服_基本_本気2 "不能让他们得逞！心爱酱，抓住他们！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「がってん！」
    voice "voice/心愛/cca_a1_1850.ogg"
    ai 心愛_私服_基本_ニタァ "搞定！"

    # 莲 「げ、ばれた」
    lian "哎，暴露了"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「じゃぁー…また、前みたいに…一緒にアイスたべよー？」
    show リオン_基本_杖なし_キス at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1103.ogg"
    lion リオン_基本_杖なし_キス "啊，啊哈哈…那么，期待晚上吧…？"
    hide リオン_基本_杖なし_嬉しい

    # 莲 「たまには昼間っから、ゆっくりまったりたっぷりしたいんだがな…」
    lian "偶尔从白天开始，就想好好地享受一下…"

    # 里昂 「は、恥ずかしい事言わないの！」
    show リオン_基本_杖なし_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1104.ogg"
    lion リオン_基本_杖なし_驚き "不、不要说害羞的话嘛！"
    hide リオン_基本_杖なし_キス

    # nil 「そんな感じで、僕らは幸せです。」
    "就是这样，我们很幸福"

    # nil 「りがとう。ラブポーション・シクスティナイン。」
    "谢谢你。LOVEPOTION·SIXTYNINE"

    # scene22 场景2 【二周目_尾声】 结束

    # 全部翻译完成！

    # 画面回到主菜单！

    # Scene22 结束！

    stop music fadeout 3.0
    scene white with Dissolve(3.0)
    $ renpy.end_replay()

    # 周目处理函数
    $ persistent.two = True
    $ check_playthrough()

    # 2022年1月21日 By Luckykeeper ， Translate ALL DONE！！！
    # 2022年3月27日 By Luckykeeper ,  Story Script ALL DONE！！！

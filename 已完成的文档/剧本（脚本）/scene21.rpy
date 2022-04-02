# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene21 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：
# 版本 0.8 "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年4月2日

# 当前流程：编写脚本AIO Process

label scene21:
    # scene21 开始
    play music bgmtwentyeight fadeout 2.0 fadein 2.0

    # scene21 场景1 【梦想的第一战】 开始
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)
    scene 通学路c_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 地点：通学路街道
    $ quick_menu = True

    # 里昂 「さぁ、こだよ。例のお店は」
    # 参考资料：https://www.bilibili.com/video/BV1i64y1e7N9
    show リオン_私服_基本_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0739.ogg"
    lion リオン_私服_基本_にっこり "啊，就是这里，那家店（L:这是前面在摩天轮上提到的里昂要借的那家店铺，例のお店的这个表达很特殊，比如例のプール(那个泳池)、例のコンビニ(那个便利店)、例の電車(那个电车)等等，可以参考BV1i64y1e7N9）"

    # 莲 「ぬお…こは…」
    lian "这是……"

    # nil 「リオンと結ばれた日の翌々日。俺はリオンに連れられて『店舗を貸してくれる予定だったお店』にやってきた。」
    "和里昂结合后的第三天。我被里昂带到了『预定租借店铺给她的那家店』"

    # nil 「トレーラーハウス的な外観のお店の看板には「69thStreetDiner」のネオンサインが飾られている。」
    "商店的招牌看起来像拖车房，上面挂着『69thStreetDiner』的霓虹灯"

    # nil 「リオンと出会った（再会した）日に、本来の予定通りなら、真冬と心愛と食事に訪れていたであろう、ダイナー式のレストランだ。」
    "与里昂相遇（重逢）的那一天，如果按照原定计划的话，我会和真冬还有心爱一起去吃饭的那家diner式餐厅"

    # nil 「なんつー因果だ…。結局、あれから色々あって訪れる機会を失ってはいたが…。」
    "这就是命运啊……后来，由于各种原因，我一直没有机会去这里……"

    # 里昂 「すー…はー…すー…はー…あぅー…おなかいたい…」
    show リオン_私服_基本_ぶわー at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0740.ogg"
    lion リオン_私服_基本_ぶわー "呼啊——……呼啊——……啊呜——……感觉不大得劲啊……"
    show リオン_私服_基本_にっこり at love69_lion_center with dissolve

    # 莲 「なんだ、ウンコでも漏れそうなのか」
    lian "什么呀，大便都快漏出来了吗？"

    # 里昂 「そうそう、一週間溜まったのがついに…ってばか！緊張とかそういうのだよ！」
    show リオン_私服_基本_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0741.ogg"
    lion リオン_私服_基本_にっこり "对对，积攒了一个星期终于……真是笨蛋啊！紧张什么的！"
    hide リオン_私服_基本_ぶわー

    # 莲 「ウンコは？」
    lian "大便呢？"

    # 里昂 「でねぇよ！」
    show リオン_私服_基本_見下し at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0742.ogg"
    lion リオン_私服_基本_見下し "没有啊！"
    hide リオン_私服_基本_にっこり

    # 莲 「良いんだぞ無理しなくて」
    lian "好啦，不要勉强"

    # 里昂 「一週間出てないよ！　ちょっと辛いよ！」
    show リオン_私服_基本_ぶわー at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0743.ogg"
    lion リオン_私服_基本_ぶわー "一个星期没出来了！有点难受啊！"
    hide リオン_私服_基本_見下し

    # 莲 「腸のねじれが原因かもしれないな。仰向けになりながら、お腹をマッサージすると良いらしいぞ。毎朝やるとい」
    lian "可能是肠道扭曲引起的。听说一边仰着头，一边按摩肚子好像会比较好，每天早上都这么做"

    # 里昂 「わかった、やってみる。…なんか話が変な方向に…」
    show リオン_私服_基本_ジト目 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0744.ogg"
    lion リオン_私服_基本_ジト目 "知道了，我试试看……感觉话题朝着奇怪的方向……"
    hide リオン_私服_基本_見下し

    # 莲 「まぁいだろ、行くぞ」
    lian "不管了，先出发吧"

    # 里昂 「Whats a.」
    show リオン_私服_基本_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0745.ogg"
    lion リオン_私服_基本_驚き "Whats a……"
    hide リオン_私服_基本_ジト目

    # nil 「リオンは渋ったが、俺は無理矢理手を引いて、『OPEN』の札が下がったドアをくぐった。」
    "虽然里昂不情愿，但我还是强行拉着她的手，穿过挂着『OPEN』牌资子的门"

    # 铃铛声
    play sound "/voice/effect/カウベル.ogg"

    # BGM切店内英文歌
    play music bgmfifteen fadeout 2.0 fadein 2.0

    # 场景切换到雾叶店内
    scene 霧葉ちゃんのお店 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「カランコロンカラ～ン」
    "叮当叮当~"

    # 莲 「漫才の入りみたいなチャイムだな…」
    lian "像是漫才表演开始的铃声啊……（L:漫才是日本的一种喜剧表演形式）"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「はいどーもーいらっしゃいませー」
    show 店长_私服_無表情 at love69_wuye_center with dissolve
    voice "voice/霧葉/krh_a1_0064.ogg"
    dinerowner 店长_私服_無表情 "你好~欢迎光临~"

    # 莲 「漫才の入りみたいな挨拶だな！」
    lian "你打招呼的样子就像漫才表演一样！"

    # nil 「俺たちを出迎えてくれたのはどこかで見覚えのある、黒髪で長身の女性だった。」
    "迎接我们的是似乎在哪里见过的，黑发高个子的女性"

    # nil 「シルバーで出来た壺をひたすら磨いている。」
    "她不停地擦拭着银制的罐子"

    # nil 「店内にはアメリカンなグッズやネオンサインが、壁や天井に飾られていて、金属ごしらえのバーカウンターの前には、コーラのロゴが描かれた丸椅子が並べられている。」
    "店内装饰着美国的商品和霓虹灯，金属制的吧台前摆放着画有可乐标志的圆形椅子"

    # 店长 「お客様はー…えっと、二名様ですか。　カウンター席でよろしいですね？」
    show 店长_私服_見下し at love69_wuye_center with dissolve
    voice "voice/霧葉/krh_a1_0065.ogg"
    dinerowner 店长_私服_見下し "客人……请问是两位客人吗？坐在吧台可以吗？"
    hide 店长_私服_無表情

    # 莲 「テーブル席空いてますけど。ていうか、俺達以外お客さんいないような」
    lian "桌子那边有空位子，说起来，除了我们没有其他客人了吗"

    # 店长 「でも、カウンター席の方が用件は済まし易いのでは？」
    show 店长_私服_目閉じ at love69_wuye_center with dissolve
    voice "voice/霧葉/krh_a1_0066.ogg"
    dinerowner 店长_私服_目閉じ "不过，坐在吧台不是更方便办事吗？"
    hide 店长_私服_見下し

    # nil 「カウンターの中の女性は、俺の背後に恥ずかしそうに立っているリオンの事を指差した。」
    "吧台里的女性指着我背后羞涩地站着的里昂"

    # 莲 「ほら、リオン」
    lian "来，里昂"

    hide 店长_私服_目閉じ
    show 店长_私服_目閉じ:
        zoom 1.5
        yalign 0.015
        xalign 0.52
        linear 0.3 xalign 0.11

    show リオン_私服_基本_悲しい2 at love69_lion_right with dissolve

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「…うん。　お久しぶりです、霧葉さん」
    voice "voice/リオン/ron_a1_0746.ogg"
    lion リオン_私服_基本_悲しい2 "…嗯，好久不见，雾叶小姐"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「そうですね。二週間ぶりぐらいでしょうか。貴方がこに来た理由も、わかってはいますし、硬い挨拶も抜きにして、とりあえず座ったらどうでしょう」
    voice "voice/霧葉/krh_a1_0067.ogg"
    dinerowner 店长_私服_目閉じ "是啊。大概两周没见了吧。我知道你来这里的理由，打招呼就不用了，总之先坐下吧"

    # nil 「店主の女性が、そっと手でカウンター席を示した。」
    "店主的女性用手轻轻指了指吧台的座位"

    # nil 「俺達二人は促されるまに、席に腰を下ろした。」
    "我们俩在她的催促下，坐了下来"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「えっと…」
    voice "voice/リオン/ron_a1_0747.ogg"
    lion リオン_私服_基本_悲しい2 "那个……"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ご注文は？」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0068.ogg"
    dinerowner 店长_私服_無表情 "您要点什么？"
    hide 店长_私服_目閉じ

    # nil 「コーラフロートを２つ」
    # 参考资料：https://www.amazon.cn/dp/B01M28ZDMT/ref=redir_mobile_desktop/462-6190816-7378460?_encoding=UTF8&dsc=1
    "两杯Cola float（L:我说不上来是啥，想知道可以去百度查查，或者到游戏文件夹下找豆知识文档）"

    # 店长 「かしこまりました。アイスとホットどちらにしましょう」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0069.ogg"
    dinerowner 店长_私服_微笑み "好的，要冰的还是热的呢？"
    hide 店长_私服_無表情

    # 莲 「アイスで」
    lian "冰的"

    # nil 「女性は微笑んで、俺達に背中を向けた。」
    "女性微笑着，背向了我们"

    # 莲 「リオン。俺がしてやれるのはこれだけだ…」
    lian "里昂。我能做的只有这些……"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ありがと…蓮くん」
    show リオン_私服_基本_にっこり at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0748.ogg"
    lion リオン_私服_基本_にっこり "谢谢你…莲君"
    hide リオン_私服_基本_悲しい2

    # nil 「俺は緊張でガッチガチになっているリオンにそっと耳打ちする。まぁ、そりゃそうだろう。」
    "我轻轻地对紧张得要死的里昂耳语。嘛，这是当然的吧"

    # nil 「彼女らが交わした契約の全容は伺いしれないが、それの破綻を伝えにきたんだからな。」
    "虽然不知道她们签的协议是什么，但是我们是来传达约定失败了"

    # nil 「とはいえ、俺ができるのは本当にこまでだ。あとはリオンだけの戦い。」
    "话虽如此，我能做的真的只有这么多。接下来是只有里昂的战斗"

    # nil 「一つ気づいたのは、誰も触っていないのに、一人でにジュークボックスがＢＧＭを奏で始めていたことだ。」
    "我注意到了一点，明明谁都没有碰过，却自己开始弹奏BGM的点唱机"

    # nil 「とはいえ、俺ができるのは本当にこまでだ。あとはリオンだけの戦い。」
    "话虽如此，我能做的真的只有这么多。接下来是只有里昂的战斗"

    # nil 「まぁ、この世に魔法とやらが存在していて、リオンと繋がっているなら、この店もその類であってもおかしくない。」
    "嘛，如果这个世界上真的存在魔法，并且和里昂联系在一起的话，那么这家店也应该是属于这类的"

    # 里昂 「……」
    show リオン_私服_基本_微笑み at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0749.ogg"
    lion リオン_私服_基本_微笑み "……"
    hide リオン_私服_基本_にっこり

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「良い…彼氏さんですね」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0070.ogg"
    dinerowner 店长_私服_目閉じ "真不戳的……男朋友呢"
    hide 店长_私服_微笑み

    # 莲 「へっ？」
    lian "诶？"

    # nil 「俺達が無言で、コーラフロートを待っていると、カウンター後ろのサーバーからコーラをグラスに注ぎながら、店主の女性が話しかけてきた。」
    "我们一言不发地等着Cola float，当我从柜台后面的饮料机那里倒了一杯可乐时，这家餐馆的女店主对我说话了"

    # 店长 「彼女の緊張をほぐすための、コーラとアイス。素敵なチョイスですよ」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0071.ogg"
    dinerowner 店长_私服_微笑み "为了缓解她的紧张，可乐和冰块。真是不错的选择"
    hide 店长_私服_目閉じ

    # nil 「女性はこちらを向いて、静かに微笑んだ。」
    "女性转过身来，静静地微笑着"

    # nil 「表情の変化こそ乏しい人だったが、余裕をもった優しさを感じる。」
    "虽然表情变化不大，但却能感受到从容的温柔"

    # nil 「こちらの考えを見抜いてくるのは…どこかの俺の担任とそっくりだが…。」
    "能看穿我的想法.…和我的班主任一模一样…"

    # 莲 「へ…ありがとうございます…」
    lian "嗯…谢谢…"

    # 店长 「そんな彼氏の粋な計らいに、少しサービスしてあげましょう」
    show 店长_私服_ニヤリ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0072.ogg"
    dinerowner 店长_私服_ニヤリ "对于这样的男朋友，稍微服务一下吧"
    hide 店长_私服_微笑み

    # nil 「女性が、カウンターテーブルに置いたのは、三人分のコーラフロートだった。」
    "女性放在柜台桌上的是三人份的Cola float"

    # 莲 「え？　頼んじゃいないけど…」
    lian "诶？我没要…"

    # 店长 「いや、これは私のです」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0073.ogg"
    dinerowner 店长_私服_無表情 "不，这是我的"
    hide 店长_私服_ニヤリ

    # 莲 「サービスってそれかい！」
    lian "服务就是这个吗！"

    # 店长 「は、冗談ですよ。ほら、本日のケーキ。ブラウニーのラズベリーソースあえです」
    show 店长_私服_にっこり at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0074.ogg"
    dinerowner 店长_私服_にっこり "哈哈，我开玩笑的。来，今天的蛋糕。加了覆盆子酱做的巧克力蛋糕（L:覆盆子就是一般意义上说的树莓，国内又叫红桑子、野草莓、蛇头莓、桑莓等，一周目这款蛋糕也有出现）"
    hide 店长_私服_無表情

    # nil 「ひょこっと、カウンターテーブルの下から、白い皿に乗ったケーキを店主の女性は取り出した。」
    "突然，女性店主从吧台的桌子下，拿出了放在白色盘子上的蛋糕"

    # nil 「それも三皿。」
    "也是三盘"

    # 莲 「結局アンタも食べるんかい！」
    lian "于是你也要吃吗？"

    # 店长 「だって二人だけ食べてるのに寂しいじゃないですか」
    show 店长_私服_不満 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0075.ogg"
    dinerowner 店长_私服_不満 "但是只有你们两个人吃饭，不是很寂寞吗？"
    hide 店长_私服_にっこり

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「あ、あの…！」
    show リオン_私服_基本_驚き at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0750.ogg"
    lion リオン_私服_基本_驚き "啊，那个…！"
    hide リオン_私服_基本_微笑み

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「まぁまぁ。まずは食べましょう。美味しいですよ？」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0076.ogg"
    dinerowner 店长_私服_目閉じ "嘛嘛，先来吃吧，很好吃吧？"
    hide 店长_私服_不満

    # nil 「リオンの言葉を遮るように、女性はカトラリーを机の上に置いた。」
    "为了打断里昂的话，女性把餐具放在了桌子上"

    # nil 「銀色に輝く、フォーク、シンカー、チェンジアップだ。」
    "银色的叉子，闪烁着光芒，随着移动变换着光线"

    # 莲 「一個しか食器じゃねぇじゃねぇか！」
    lian "不是只有一个盘子吗！"

    # 店长 「どうです？　私の球種の多さは」
    # 参考资料：http://ja.wikipedia.org/wiki/%E7%90%83%E7%A8%AE_(%E9%87%8E%E7%90%83)
    show 店长_私服_ニヤリ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0077.ogg"
    dinerowner 店长_私服_ニヤリ "怎么样？我的球路多吧（L:原文球種，是棒球用语，指棒球投手投出的球路的类型和名称，有多种）"
    hide 店长_私服_目閉じ

    # 莲 「スライダーも欲しいかな」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%B9%E3%83%A9%E3%82%A4%E3%83%80%E3%83%BC_(%E7%90%83%E7%A8%AE)
    lian "你也想要一个Slider吗（L:滑球，投球时手指旋转并向下用力，球速介于曲球与快速球之间。又称作水平外曲球）"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「え、えと…頂いちゃっても…」
    show リオン_私服_基本_嬉しい at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0751.ogg"
    lion リオン_私服_基本_嬉しい "那、那个……我开懂了……"
    hide リオン_私服_基本_驚き

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「え、どうぞ。じゃぁみんなで…いただきまーす♪」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0078.ogg"
    dinerowner 店长_私服_目閉じ "嗯，请。那么，大家一起……开动啦♪"
    hide 店长_私服_ニヤリ

    # nil 「普段なら自分のペースを崩さないリオンがこまで動揺しているのも珍しい。俺からすれば、気さくな良い人なんだが…。」
    "平时不会打破自己节奏的里昂如此动摇也是很少见的。在我看来，她是个随和的好人…"

    # nil 「店主からはみえない位置で、そっと、リオンの身体を撫でる。「大丈夫、大丈夫」そう伝えるように。」
    "在店主看不到的位置，轻轻地抚摸着里昂的身体，告诉她「没事，没事的」"

    # 莲 「うひょぉーいただきまーす！」
    lian "我开动了！"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「い、いただきます…」
    show リオン_私服_基本_微笑み at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0752.ogg"
    lion リオン_私服_基本_微笑み "我、我开动了……"
    hide リオン_私服_基本_嬉しい

    # nil 「フォークをぶっさして、派手に平らげると、チョコレートが溶けるような食感が口の中に広がっていく。美味い。味は本物だ。」
    "用叉子叉开，大口大口地吃，巧克力融化的口感在嘴里蔓延开来，好吃，味道是真的不戳"

    # 莲 「これ…うまいすね…」
    lian "这个…很好吃啊…"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「くすっ。ありがとうございます。貴方の幼馴染み、心愛ちゃんも気に入ってくれたんですよ」
    show 店长_私服_にっこり at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0079.ogg"
    dinerowner 店长_私服_にっこり "欸嘿，谢谢你。你的幼驯染心爱酱也很喜欢呢"
    hide 店长_私服_目閉じ

    # 莲 「心愛を知ってるのか」
    lian "你认识心爱？"

    # 店长 「え。あの子、ディナータイムにピアノを弾きに来てくれるんですよ」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0080.ogg"
    dinerowner 店长_私服_微笑み "嗯，那孩子晚饭时间会来弹钢琴"
    hide 店长_私服_にっこり

    # 莲 「そういえばあいつ。昔ピアノ弾いてたもんな…」
    lian "这么说来那家伙，以前弹过钢琴呢"

    # 店长 「真冬ちゃんも、お兄ちゃんを連れて来たがってましたよ。たまには家に帰ってあげてくださいね」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0081.ogg"
    dinerowner 店长_私服_目閉じ "真冬酱也是，想带欧尼酱过来呢，请你偶尔带她回家吧"
    hide 店长_私服_微笑み

    # 莲 「た、確かに昨日は外泊したけど…真冬も友達の家に泊まりに行ってたよ」
    lian "啊，我昨天确实在外面过夜了……不过真冬也去朋友家过夜了"

    # 店长 「それ、私の家ですけどね」
    show 店长_私服_ニヤリ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0082.ogg"
    dinerowner 店长_私服_ニヤリ "那个，是去我家了哦"
    hide 店长_私服_目閉じ

    # 莲 「あ…妹がお世話になっております」
    lian "啊…妹妹承蒙您的关照了"

    # 店长 「いえいえ。新しい友達が増えて私も、私の姉も嬉しいですよ」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0083.ogg"
    dinerowner 店长_私服_微笑み "哪里哪里。有了新朋友，我和我姐姐都很高兴"
    hide 店长_私服_ニヤリ

    # nil 「せめて、リオンが話しやすいような空気作りをするためにも、店主の女性と話しを広げる。」
    "至少，为了制营造里昂更容易交谈的氛围，和店主的女性展开话题"

    # nil 「雰囲気的に、俺らとそう歳は変わらないようにみえるが…。」
    "从气氛上看，她和我们的年龄差不多…"

    # nil 「女性も女性で、俺の腹を読んでいるのか、笑顔を崩さないま、話に付き合ってくれる。」
    "女人就是女人，在可能读着我的心的同时，还保持着笑容，陪我聊天"

    # nil 「気づいたら、俺はケーキを全て食べ尽くしていた。」
    "回过神来，我已经把蛋糕全部吃完了"

    # 莲 「あ、ごちそうさま…美味しかったです」
    lian "啊，多谢款待…很好吃"

    # 店长 「はーい。リオンちゃん、さっきから全然食べてないけど、大丈夫ですか？」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0084.ogg"
    dinerowner 店长_私服_無表情 "好——里昂酱，从刚才开始就没吃东西，你没事吧？"
    hide 店长_私服_微笑み

    # nil 「さぁ、リオン。今がチャンスだ！」
    "来吧，里昂，现在是你的机会！"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「あの…霧葉さん…！」
    show リオン_私服_基本_無表情_1 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0753.ogg"
    lion リオン_私服_基本_無表情_1 "那个…雾叶小姐…！"
    hide リオン_私服_基本_微笑み

    # 店长 「はいはい」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0085.ogg"
    dinerowner 店长_私服_目閉じ "嗯嗯"
    hide 店长_私服_無表情

    # nil 「仕掛けた。」
    "抓住了"

    # nil 「とは成り行きを見守るだけだ。」
    "就等着看事态的发展吧"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「その…その…私…約束を…果たせませんでした…すみません…」
    show リオン_私服_基本_悲しい2 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0754.ogg"
    lion リオン_私服_基本_悲しい2 "那个…那个…我……没能实现我的约定…对不起…"
    hide リオン_私服_基本_無表情_1

    # 店长 「あ、それでそんな落ち込んでたんですね。いんですよ、貴方が選んだ結果ですから。その分彼氏さんを幸せにしてあげて下さいね」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0086.ogg"
    dinerowner 店长_私服_微笑み "啊，所以你才这么沮丧。没关系的哦，这是你自己选择的结果，希望你的男朋友能够幸福"
    hide 店长_私服_目閉じ

    # 莲 「ずーっ」
    lian "啊"

    # nil 「中々に出来るな、この女性。リオンの考えを読みながらも、先手を打ってこちらの手を封じてくる。これでは俺も口を出せない。」
    "这个女人真厉害，读懂里昂的想法，却先发制人封住我们的后手，这下我也插不上嘴了"

    # nil 「さて、どう出るか…。」
    "那么，怎么办呢…"

    stop music fadeout 2.0

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「で、でも、私…その…」
    voice "voice/リオン/ron_a1_0755.ogg"
    lion リオン_私服_基本_悲しい2 "但是，我…那个…"

    # 新 BGM 解锁
    play music bgmfortynine fadein 2.0

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「自分自身の恋を叶える事は出来たから、店を貸してくれ。なんて、甘い話は通りませんよ」
    show 店长_私服_不満 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0087.ogg"
    dinerowner 店长_私服_不満 "实现了自己的爱情，把店借给我吧。这种甜言蜜语是行不通的"
    hide 店长_私服_微笑み

    # 莲 「違う。そうじゃない！」
    lian "不是，不是那样的"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「蓮くんっ！」
    show リオン_私服_基本_驚き at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0756.ogg"
    lion リオン_私服_基本_驚き "莲君！"
    hide リオン_私服_基本_悲しい2

    # nil 「俺が打って出ようとする所を、リオンは俺の服の裾を引っ張って止める。」
    "当我准备出击时，里昂拽着我的衣服下摆阻止了我"

    # nil 「店主の女性は俺に視線を向けない。恐らく、計算の範囲内だろう。」
    "店主的女性没有把视线转向我，恐怕这都在她的计算范围内吧"

    # nil 「安い挑発に乗っかってしまった。」
    "我上了挑衅的当"

    # 里昂 「ありがとう…ごめんね…。えっと、霧葉さん…もう一度、チャンスを…貰いたいなって、思って…」
    show リオン_私服_基本_微笑み at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0757.ogg"
    lion リオン_私服_基本_微笑み "谢谢…对不起……呃，雾叶小姐……我想…我希望能再得到一次机会……"
    hide リオン_私服_基本_驚き

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「チャンスを…？　次はどんな恋を叶えるつもりですか？多分、ラブポーション・シクスティナインはもう作れないでしょうし」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0088.ogg"
    dinerowner 店长_私服_無表情 "Chance……？接下来你打算实现什么样的恋爱呢？大概，你已经再也做不出LOVEPOTION・SIXTYNINE了"
    hide 店长_私服_不満

    # 莲 「…どういう事だ？」
    lian "…这是怎么回事？"

    # 店长 「おや、知らなかったのですね。あのアイスは元々、リオンちゃんの『蓮くんへの恋心』が込められてるんですよ。今はそれが満たされてしまっているから…」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0089.ogg"
    dinerowner 店长_私服_目閉じ "啊，你不知道啊。那个冰淇淋原本就包含了里昂的『对莲君的恋慕之情』，但是现在已经得到满足了"
    hide 店长_私服_無表情

    # 店长 「同じものを作る事はできない。それに、作れたとしても、世界の運命すらねじ曲げてしまうような、強力な物は作れないでしょうね」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0090.ogg"
    dinerowner 店长_私服_無表情 "所以不可能制造出同样的东西。而且，就算制造出来了，也不可能制造出能扭曲世界的命运这样强大的东西吧"
    hide 店长_私服_目閉じ

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「それでも…！　私は…アイス屋を…開きたくて…」
    show リオン_私服_基本_悲しい2 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0758.ogg"
    lion リオン_私服_基本_悲しい2 "可是……！我……想开一家冰淇淋店"
    hide リオン_私服_基本_微笑み

    # nil 「リオンの声はさきほどから弱々しい。多分、この人の言っている事は恐らく本当だ。」
    "里昂的声音从刚才很微弱。大概，这个人说的话是真的"

    # nil 「だが、俺は一つこでリオンに聞いてみたいが浮かんだ。」
    "但是，我有一个想法我想问问里昂"

    # BGM 停
    stop music fadeout 2.0

    # 莲 「はい先生」
    lian "那个，老师"

    # 原 BGM 回
    play music bgmfifteen fadeout 2.0 fadein 2.0

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「はいどうぞ」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0091.ogg"
    dinerowner 店长_私服_微笑み "请说"
    hide 店长_私服_目閉じ

    # 莲 「なんでリオンはアイス屋作りたいの？」
    lian "为什么里昂想开冰淇淋店？"

    # nil 「特に今まで気にならなかったが、そういえば聞いていなかった。」
    "虽然到现在为止没有特别在意，但是关于这个的事情还没听说过"

    # nil 「単にアイスが大好きだからか…？　」
    "只是因为喜欢冰淇淋吗…？"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「それは…私が…アイスが大好きだから…」
    voice "voice/リオン/ron_a1_0759.ogg"
    lion リオン_私服_基本_悲しい2 "因为……我……喜欢冰淇淋……"

    # 莲 「うん。まぁそれはわかってる。他には？」
    lian "嗯。我知道。还有别的吗？"

    # 里昂 「あとは…私の力で、一人でも多くの人を…幸せにしたいから…！」
    voice "voice/リオン/ron_a1_0760.ogg"
    lion "还有……因为我想用我的力量，让尽可能多的人……幸福……！"

    # 莲 「つまり。アイスの力で幸せをお届けしたい。ということね…。それで、この人の契約にこだわる理由は…魔法だの何だの話が通りやすいから…か」
    lian "也就是说，想用冰淇淋的力量传递幸福。所以，拘泥于和这个人契约的理由是……因为和她谈论魔法之类的事情很容易…吗……"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「確かに察しのい彼氏ですね…」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0092.ogg"
    dinerowner 店长_私服_目閉じ "的确是个敏感的男朋友……"
    hide 店长_私服_微笑み

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「あとは…私の力で、一人でも多くの人を…幸せにしたいから…！」
    show リオン_私服_基本_驚き at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0761.ogg"
    lion リオン_私服_基本_驚き "嗯，是的，我自己也有点不在状态……"
    hide リオン_私服_基本_悲しい2

    # 莲 「そうでもしねぇと、未来のアイス屋さんの旦那には相応しくないだろ？」
    lian "如果看不出来的话，就配不上未来冰淇淋店老板的丈夫了吧？"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ぶふっ」
    show 店长_私服_にっこり at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0093.ogg"
    dinerowner 店长_私服_にっこり "噗"
    hide 店长_私服_目閉じ

    # 莲 「笑うなよ！」
    lian "别笑了！"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「それは、恥ずかしいよ、二つの意味で」
    show リオン_私服_基本_悲しい2_1 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0762.ogg"
    lion リオン_私服_基本_悲しい2_1 "这，不管从哪个方面来说，都太害羞了"
    hide リオン_私服_基本_驚き

    # 莲 「うるせえ！」
    lian "无路赛！"

    # nil 「少し、険悪なムードがほだされていくようだ。わざとクサい台詞いって良かった。」
    "稍微有点险恶的气氛在渐渐消失。故意说了些下流的台词真是太好了"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「さて、もう一度チャンスですか…どうしましょうね…」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0094.ogg"
    dinerowner 店长_私服_目閉じ "那么，再给一次机会吗……该怎么办呢……"
    hide 店长_私服_にっこり

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「お願いします！　どうしても、霧葉さんたちの協力が必要なんです！」
    show リオン_私服_基本_無表情_1 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0763.ogg"
    lion リオン_私服_基本_無表情_1 "拜托了！无论如何，需要雾叶小姐你们的协助！"
    hide リオン_私服_基本_悲しい2_1

    # ？？？（想瑠，没有头像）用灰 「へーい店長ォ～。からかうのはいけど、そこら辺にしてあげなヨー」
    # 记得得加人物表
    voice "voice/想瑠/sol_a1_0112a.ogg"
    unknown404 "嘿——店长~你可以取笑她，但是就让她试试吧"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「また厄介なのが来ましたね。お引き取りください」
    show 店长_私服_不満 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0095.ogg"
    dinerowner 店长_私服_不満 "又有麻烦的人来了，请离开我们"
    hide 店长_私服_目閉じ

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「客扱いしろよ！　ていうか、実はさっきから居たけどな！」
    show 想瑠_スーツ_ぶわ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0113.ogg"
    liu 想瑠_スーツ_ぶわ "把我当客人吧！话说回来，其实我从刚才开始就在这儿！"

    # nil 「例のアイツでした。」
    "是那个家伙（L:这里的原文例のアイツ，和最开始说的例のお店的用法是一样的）"

    # 想瑠 「てめぇもてめぇだ葛城兄！ぬわーにが『俺達以外客いない』とかつぶやきやがって！』
    show 想瑠_スーツ_本気 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0114.ogg"
    liu 想瑠_スーツ_本気 "就是你这家伙葛城哥哥！刚才还嘟囔了『除了我们没有其他客人了吗』之类的话吧！"
    hide 想瑠_スーツ_ぶわ

    # 莲 「店長。ペイントボールをあちらのお嬢さんに」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%9A%E3%82%A4%E3%83%B3%E3%83%88%E3%83%9C%E3%83%BC%E3%83%AB
    lian "店长。把paintball送给那边的小姐（L:paintball，漆弹，打真人CS用的那个）"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「かしこまりました」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0096.ogg"
    dinerowner 店长_私服_目閉じ "遵命"
    hide 店长_私服_不満

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「おうやめろ！　クリーニングからあがってきたばかりのスーツだぞ！そんなもんぶつけられたら、ピンク色のマークついちゃうじゃないか！」
    show 想瑠_スーツ_驚き at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0115.ogg"
    liu 想瑠_スーツ_驚き "别这样！这是刚从洗衣店出来的西装！要是碰上那种东西，不是会留下粉红色的标记吗！"
    hide 想瑠_スーツ_本気

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「食らえ！」
    show リオン_私服_基本_ニタァ at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0764.ogg"
    lion リオン_私服_基本_ニタァ "看招！"
    hide リオン_私服_基本_無表情_1

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「リオンてめぇ！」
    show 想瑠_スーツ_本気 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0116.ogg"
    liu 想瑠_スーツ_本気 "里昂你个混蛋！"
    hide 想瑠_スーツ_驚き

    # nil 「リオンがピンク色のボールを奴に投げつける。だが、奴は片腕でボールをキャッチした。」
    "里昂向那家伙投掷粉红色的漆弹。但是，那家伙用一只手接住了漆弹"

    # 想瑠 「まったく、味方してやろうというのに…やっぱやめようかな…」
    show 想瑠_スーツ_目閉じ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0117.ogg"
    liu 想瑠_スーツ_目閉じ "真是的，明明想站在你这边……果然还是算了吧……"
    hide 想瑠_スーツ_本気

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ごめん、つい」
    show リオン_私服_基本_微笑み at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0765.ogg"
    lion リオン_私服_基本_微笑み "对不起，我只是……"
    hide リオン_私服_基本_ニタァ

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「まったく、味方してやろうというのに…やっぱやめようかな…」
    show 想瑠_スーツ_ニヤリ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0118.ogg"
    liu 想瑠_スーツ_ニヤリ "哈啊、怎么办好捏……雾叶叶酱……"
    hide 想瑠_スーツ_目閉じ

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「何がです？」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0097.ogg"
    dinerowner 店长_私服_無表情 "什么事呢？"
    hide 店长_私服_目閉じ

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「そら、もう一度チャンス与えるとかそういう話よ」
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0119.ogg"
    liu 想瑠_スーツ_見下し "就是再给他一次机会之类的"
    hide 想瑠_スーツ_ニヤリ

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「あ。そうですね。まったく、大事な所で話の腰折らないでくださいよ。ほら、コーラあげるから」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0098.ogg"
    dinerowner 店长_私服_目閉じ "啊，是啊。真是的，不要在重要的地方打断我的话。来，我给你可乐"
    hide 店长_私服_無表情

    # nil 「店主の女性は、コーラの瓶を担任に投げつける。」
    "女店主把可乐瓶扔给了班主任"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「わーい♪」
    show 想瑠_スーツ_にっこり at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0120.ogg"
    liu 想瑠_スーツ_にっこり "哇~♪"
    hide 想瑠_スーツ_見下し

    # nil 「すると、嬉しそうに瓶を抱えて担任はテーブル席に戻った。」
    "于是，班主任高兴地抱着瓶子回到了桌旁"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「そうですねぇ。リオンちゃん」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0099.ogg"
    dinerowner 店长_私服_無表情 "是啊，里昂酱"
    hide 店长_私服_目閉じ

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「はい」
    show リオン_私服_基本_無表情_1 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0766.ogg"
    lion リオン_私服_基本_無表情_1 "嗯"
    hide リオン_私服_基本_微笑み

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「一応、貴方の考えを聞かせて貰えますか？」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0100.ogg"
    dinerowner 店长_私服_微笑み "姑且，你能告诉我你的想法吗？"
    hide 店长_私服_無表情

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「はい…えっと…」
    show リオン_私服_基本_微笑み at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0767.ogg"
    lion リオン_私服_基本_微笑み "那个……呃……"
    hide リオン_私服_基本_無表情_1

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ねーねー蓋あかないんだけど。栓抜きちょうだい」
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0121.ogg"
    liu 想瑠_スーツ_見下し "呐~呐~我打不开捏，把开瓶器给我一哈"
    hide 想瑠_スーツ_にっこり

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「…あ、ちょっと待って下さいね」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0101.ogg"
    dinerowner 店长_私服_目閉じ "……啊，请稍等一下"
    hide 店长_私服_微笑み

    # nil 「店主は胸の谷間から、オーソドックスな栓抜きを取り出した。」
    "店主从乳沟里拿出一个正统的开瓶器"

    # 莲 「ワーオ…」
    lian "哇哦…"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「むー…！」
    show リオン_私服_基本_ジト目 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0768.ogg"
    lion リオン_私服_基本_ジト目 "嗯——……！"
    hide リオン_私服_基本_微笑み

    # nil 「リオンが、俺の裾を引っ張って『それぐらい私も出来るから』みたいな目でみてくる。」
    "里昂拉着我的衣摆，用『这样的我也能做到』这样的眼神看着我"

    # nil 「今度やってもらおう。」
    "下次也让你这样做吧"

    # nil 「そして、店主の女性は一回中空に投げた栓抜きを捕まえて、担任の頭めがけて投げつけた。」
    "然后，女店主抓住了抛到空中的开瓶器，朝着班主任的狗头扔了过去"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「Suck on this！！」
    show 店长_私服_ニヤリ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0102.ogg"
    dinerowner 店长_私服_ニヤリ "Suck on this！！"
    hide 店长_私服_目閉じ

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「Oh shit！！」
    show 想瑠_スーツ_ぶわ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0122.ogg"
    liu 想瑠_スーツ_ぶわ "Oh shit！！"
    hide 想瑠_スーツ_見下し

    # nil 「まぁあとは説明は要るまい。」
    "接下来就不需要说明了"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「えーこほん。良いですか？」
    show リオン_私服_基本_キス_1 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0769.ogg"
    lion リオン_私服_基本_キス_1 "欸——嗯，可以吗？"
    hide リオン_私服_基本_ジト目

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「え、どうぞ」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0103.ogg"
    dinerowner 店长_私服_微笑み "嗯，请吧"
    hide 想瑠_スーツ_ニヤリ

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「最初。私も蓮くんと結ばれた時に、夢を諦めてしまってもいと、思ってはいたんです」
    show リオン_私服_基本_悲しい2 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0770.ogg"
    lion リオン_私服_基本_悲しい2 "一开始，我和莲君结合的时候，也觉得就算放弃梦想也没关系"
    hide リオン_私服_基本_キス_1

    # 里昂 「でも、蓮くんに励まされて…そして、一緒にやってきた事全ても無駄になってしまうのも嫌で…」
    show リオン_私服_基本_無表情_1 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0771.ogg"
    lion リオン_私服_基本_無表情_1 "但是，在莲君的鼓励下……而且，我也不想让一起经历的一切都白费……"
    hide リオン_私服_基本_悲しい2

    # 里昂 「それに、蓮くんが自分のせいで私が夢を諦めたとは思って欲しくない…」
    show リオン_私服_基本_悲しい2 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0772.ogg"
    lion リオン_私服_基本_悲しい2 "而且，我不希望莲君认为我因为他而放弃了梦想……"
    hide リオン_私服_基本_無表情_1

    # 里昂 「そして、彼が応援してくれる夢を…一緒に叶えたくて…！」
    show リオン_私服_基本_微笑み at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0773.ogg"
    lion リオン_私服_基本_微笑み "而且，我希望他支持着我的梦想……一起来实现它……！"
    hide リオン_私服_基本_悲しい2

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「…全部彼氏の話ですね」
    show 店长_私服_不満 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0104.ogg"
    dinerowner 店长_私服_不満 "……全部都是男朋友的事呢"
    hide 店长_私服_微笑み

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「あっ…」
    show リオン_私服_基本_悲しい2 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0774.ogg"
    lion リオン_私服_基本_悲しい2 "啊……"
    hide リオン_私服_基本_微笑み

    # nil 「図星を突かれてリオンは凍り付く。」
    "被戳中要害的里昂冻结住了"

    # nil 「確かにそれは俺も突っ込もうかと思った。先ほどの質問とは答えが全く違う。」
    "确实，我也想吐槽那个，和刚才问题的回答完全不同"

    # nil 「でもそれはそうかもしれない。」
    "但也许就是这样"

    # nil 「俺の質問に答えた時の理由は「俺と結ばれる前」そして、今答えたのは「俺と結ばれた後」の理由だ。」
    "刚才答我的问题时的理由是「和我结合之前」的理由，现在回答的是「和我结合之后」的理由"

    # nil 「コーラフロートのコーラのみをストローで飲み干して、女性は、グラスを置いた。」
    "把Cola float只用吸管喝干，女性放下了玻璃杯"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「だが、それがい」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0105.ogg"
    dinerowner 店长_私服_目閉じ "但是，这样也好"
    hide 店长_私服_不満

    # nil 「険しい表情から、にっこりと微笑んだ。」
    "严肃的表情一转，变成了微笑"

    # 店长 「世界だの幸せだの、そういう規模のでかい理想って、性に合わないんですよ。それだけの力を持っているのかもしれませんが、じゃぁアイス屋じゃなくてもい。世界ごと変えてしまえばい」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0106.ogg"
    dinerowner 店长_私服_無表情 "世界啦，幸福啦，这种规模宏大的理论根本不合我的性格。也许你有这个能力，就算不是冰淇淋店，也可以改变整个世界"
    hide 店长_私服_目閉じ

    # 店长 「でも、惚れた男のために信念を貫きたい。いじゃないですか！」
    show 店长_私服_ニヤリ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0107.ogg"
    dinerowner 店长_私服_ニヤリ "但是，想为你爱的男人坚持信念，有什么不好呢？"
    hide 店长_私服_無表情

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「じゃぁ…もう一度チャンスを…ありがとうございます！」
    show リオン_私服_基本_驚き_1 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0775.ogg"
    lion リオン_私服_基本_驚き_1 "那么……再给我一次机会……谢谢！"
    hide リオン_私服_基本_悲しい2

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「え。良いでしょう。さて、どんなチャレンジを与えてあげましょうか…そうですね…」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0108.ogg"
    dinerowner 店长_私服_目閉じ "嗯，好吧。那么，我该给你什么样的挑战呢……是啊…"
    hide 店长_私服_ニヤリ

    # 莲 「もう、あのアイスは作れないのか？」
    lian "已经做不出来那个冰淇淋了吗？"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「うん。あれは、本当に、蓮くんに片思いしてないと作れないから…」
    show リオン_私服_基本_悲しい2 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0776.ogg"
    lion リオン_私服_基本_悲しい2 "嗯，那个真的是，如果不是暗恋莲君，就做不出来……"
    hide リオン_私服_基本_驚き_1

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「じゃぁ二人じゃないと作れない素敵なアイスを作ってくりゃいんじゃん？」
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0123.ogg"
    liu 想瑠_スーツ_見下し "那就去做你们两个人才能做的冰淇淋不是也挺好嘛"
    hide 想瑠_スーツ_ぶわ

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「お、久々にまともな事言ってきましたね」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0109.ogg"
    dinerowner 店长_私服_微笑み "哦，好久没说过这么正经的话了"
    hide 店长_私服_目閉じ

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「じゃないとまたタンコブ作られちゃうもん…」
    show 想瑠_スーツ_ぶわ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0124.ogg"
    liu 想瑠_スーツ_ぶわ "不然我又要被砸了……"
    hide 想瑠_スーツ_見下し

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「よしよし泣かないの。あとで可愛がってあげますからね」
    show 店长_私服_にっこり at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0110.ogg"
    dinerowner 店长_私服_にっこり "好了好了，不哭了。以后我会疼爱你的"
    hide 店长_私服_微笑み

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ぅん…って、あぶねぇなおぃ！生徒の前で情けねぇ姿させんじゃねぇよぉ！」
    show 想瑠_スーツ_照れ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0125.ogg"
    liu 想瑠_スーツ_照れ "嗯……好险啊！不能在学生面前表现得这么可怜！"
    hide 想瑠_スーツ_ぶわ

    # 莲 「いや、心愛と真冬から聞いてる」
    lian "不，我从心爱和真冬那里就听说了"

    # 想瑠 「ひぎい！　いつのまに！」
    show 想瑠_スーツ_驚き at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0126.ogg"
    liu 想瑠_スーツ_驚き "嘿呀！什么时候！"
    hide 想瑠_スーツ_照れ

    # nil 「ちなみに、何がどうなのかは、想瑠にゃん先生の尊厳のために伏せておきます。」
    "顺带一提，到底是什么情况呢？为了想瑠喵老师的尊严，我会保密的"

    # 莲 「でも、良いかもな。二人じゃねぇと作れないアイスか…それなら、俺もリオンの力になれそうだ」
    lian "但是，也许可以，只有我们两个人才能做出来的冰淇淋吗…那样的话，我好像也能成为里昂的力量"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「蓮くんは、それでいの…？」
    show リオン_私服_基本_驚き at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0777.ogg"
    lion リオン_私服_基本_驚き "莲君，这样可以吗……？"
    hide リオン_私服_基本_悲しい2

    # 莲 「いもなにも。そのために俺はいるんだろ？」
    lian "没问题。这就是我在这里的原因，不是吗？"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ヒュゥー。あっついですねぇ。ま、いですよ。それもそれで私は面白そうですし」
    show 店长_私服_ニヤリ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0111.ogg"
    dinerowner 店长_私服_ニヤリ "咻——真好啊，嘛，而且我觉得也很有意思"
    hide 店长_私服_にっこり

    # nil 「店主の女性は意味ありげにニヤリと笑っている。少し、この状況を楽しんでないか？」
    "店主的女性意味深长地微笑着。是在稍微的享受这个状况吗？"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「じゃ、じゃぁ、蓮くんと一緒じゃないと作れないアイスを…作ってきます！」
    show リオン_私服_基本_微笑み at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0778.ogg"
    lion リオン_私服_基本_微笑み "那，那么，我要去做……不和莲君一起就做不了的冰淇淋！"
    hide リオン_私服_基本_驚き

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ただし期限付きですよ。いつまでにしましょうか」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0112.ogg"
    dinerowner 店长_私服_微笑み "不过是有期限的。什么时候结束呢？"
    hide 店长_私服_ニヤリ

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「私らがハワイ旅行から帰ってくるまでいんじゃない？」
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0127.ogg"
    liu 想瑠_スーツ_見下し "等我们去夏威夷旅行回来再说吧不是挺好的嘛？"
    hide 想瑠_スーツ_驚き

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「あ。そうですね。明日から５日間、ちょっとハワイに遊びにいくので、帰ってくるまでに開発しておいてください」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0113.ogg"
    dinerowner 店长_私服_無表情 "啊，是啊。从明天开始，我们要去夏威夷玩5天，所以请在回来之前开发好"
    hide 店长_私服_微笑み

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「あ、心愛とまふまふも借りるぞー」
    show 想瑠_スーツ_ニヤリ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0128.ogg"
    liu 想瑠_スーツ_ニヤリ "啊，我们还要借心爱和嘛呼嘛呼一起"
    hide 想瑠_スーツ_見下し

    # 莲 「え、まじかよ、何も聞いてねえぞ！？」
    lian "诶，真的吗？我什么都听说啊！？"

    # 想瑠 「にっしっし、女子の秘密のバカンスってやつさね！」
    voice "voice/想瑠/sol_a1_0129.ogg"
    liu 想瑠_スーツ_ニヤリ "捏嘿嘿，这可是女孩子的秘密度假！"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「という事で、リオンちゃん、蓮くん。五日の間に、二人でしか作れないアイスを作ってくる事。そして勿論、美味しいこと」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0114.ogg"
    dinerowner 店长_私服_微笑み "就是这样，里昂酱，莲君。在五天之内做出只有两个人才能做的冰淇淋。当然必须是好吃的"
    hide 店长_私服_無表情

    # 店长 「それがクリアできるなら、お話をしましょうか」
    show 店长_私服_にっこり at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0115.ogg"
    dinerowner 店长_私服_にっこり "如果可以搞定的话，我们再来谈谈吧"
    hide 店长_私服_微笑み

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「はい…！　ありがとうございます！　頑張ります！」
    show リオン_私服_基本_嬉しい at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0779.ogg"
    lion リオン_私服_基本_嬉しい "好……！谢谢！我会尽力的！"
    hide リオン_私服_基本_微笑み

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「期待してるぜー！」
    voice "voice/想瑠/sol_a1_0130.ogg"
    liu 想瑠_スーツ_ニヤリ "我很期待喔——！"

    # nil 「俺達二人は、二人の女性の笑顔に見送られて、店を後にした。」
    "我们俩在两位女性的微笑目送下，离开了店"

    # 莲 「よかったな。リオン。一緒に頑張ろう」
    lian "太好了，里昂。一起加油吧"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「うん！　蓮くんも本当にありがとう！」
    show リオン_私服_基本_にっこり at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_0780.ogg"
    lion リオン_私服_基本_にっこり "嗯！莲君真的太感谢你了！"
    hide リオン_私服_基本_嬉しい

    # 莲 「さぁ、これから五日間忙しいぞ！」
    lian "那么，接下来的5天就要忙起来了！"

    # 画面切到莲君卧室
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 自室a_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 进 ghs BGM
    play music bgmeight fadeout 2.0 fadein 2.0

    # nil 「そして…早くも四日の時間が経った。」
    "然后…已经过了4天了"

    # nil 「家が留守なのを良いことに、リオンは俺の家に泊まり込んで開発に勤しんで居た。何故なら、リオンの家にはネットがないからだ。」
    "趁家里没人，里昂住在我家致力于开发工作，因为里昂的家里没有网络"

    # 莲 「ぶへぇ…もうアイス食べられない…」
    lian "呜欸……已经不能再吃冰淇淋了……"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「何が…何が悪いんだろう…」
    show リオン_基本_杖_悲しい2 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0781.ogg"
    lion リオン_基本_杖_悲しい2 "有什么……有什么不对吗……"

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「ちくしょうめ、何で俺まで付き合わせるんだ…」
    voice "voice/その他/mjf_a1_0047.ogg"
    mj MJ_通常 "该死，为什么我也要跟着一起……"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ごめんねマイケル…」
    voice "voice/リオン/ron_a1_0782.ogg"
    lion リオン_基本_杖_悲しい2 "对不起，迈克尔……"

    # nil 「俺の部屋と真冬の部屋には、資料やアイスの材料の残骸やらが散乱している。」
    "我的房间和真冬的房间里，资料和冰淇淋的残骸散落在各处"

    # nil 「二人でしか作れないアイス。」
    "只有两个人才能做出的冰淇淋"

    # nil 「請け負ってみたもの、皆目検討つかない。」
    "我对冰淇淋完全没有研究，不知道我该做什么"

    # nil 「アイス自体を作るのは、台所と材料があればリオンは作り上げた。」
    "制作冰淇淋，只要有厨房和材料的话，里昂就做好了"

    # nil 「味も良いし、普通に商品として扱えるレベルだろう。」
    "味道也很好，可以当做普通商品来对待"

    # nil 「だが、決定的な何かが欠けている事は、試食を担当している俺も、作ったリオンもわかっている。」
    "但是，缺乏决定性的东西，负责吃的我和制作的里昂都知道"

    # nil 「二人で…という事でやれることは、ありとあらゆる事はやった。」
    "两个人…能做的事，已经把所有能在的事情都做了"

    # nil 「机の端と端をもって運んだり。」
    "端详着机器的面板"

    # nil 「二人で同時に乗らないと稼働しないパネルに乗ったり。」
    "如果两个人同时使用就没法做出来"

    # nil 「土手の上でキャッチボールしたり。」
    # 参考资料：https://www.weblio.jp/content/%E5%9C%9F%E6%89%8B
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%AD%E3%83%A3%E3%83%83%E3%83%81%E3%83%9C%E3%83%BC%E3%83%AB
    "尝试两个人用catchball的方法来做（L:日式英语，指两个人反复投掷和接住对方的球的动作）"

    # nil 「ピサの斜塔を手で支えるような写真を撮ったり。」
    "或者一起用手支撑着拍了比萨斜塔的照片"

    # nil 「だが…しっくりと来る手応えのある結果はでなかった。」
    "但是……并没有得到想要的结果"

    # nil 「流石にそんな悪戦苦闘を４日も続けた上で、その夜だ。」
    # "在持续了4天的恶战苦斗之后的那天晚上（L:这里我强烈怀疑原作的背景放错时间了）"
    "在持续了4天的恶战苦斗之后的那天晚上"

    # nil 「焦りと疲労で、バテてしまっていた。」
    "我又着急又疲惫，筋疲力尽"

    # nil 「部屋の片隅の小さなアイスボックスには、試作品のアイス達が詰め込まれている。」
    "房间一角的小冷藏箱里塞满了原型冰淇淋"

    # 里昂 「はぁ…はぁ…時間がないのに…私のバカっ…！」
    voice "voice/リオン/ron_a1_0783.ogg"
    lion リオン_基本_杖_悲しい2 "哈啊……哈啊……没时间了……我是笨蛋……！"

    # 莲 「そう落ち込むなよ。頑張ってやってるじゃねぇか」
    lian "别那么消沉，你已经尽力了"

    # 里昂 「でも、結果が出ないんじゃ意味ないよ！」
    show リオン_基本_杖_見下し at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0784.ogg"
    lion リオン_基本_杖_見下し "但是，如果没有结果，那就没有意义了！"
    hide リオン_基本_杖_悲しい2

    # nil 「リオンは苛立って語気を強める。」
    "里昂焦躁地加强语气"

    # nil 「しかし、自分の発言の意味に気づいて言葉を閉ざした。」
    "但是，注意到自己的发言的意思，就闭上了嘴"

    # 里昂 「ごめん…手伝って貰ってるのに、意味ないとか…言っちゃだめだよね…」
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0785.ogg"
    lion リオン_基本_杖_悲しい "对不起……有人帮忙，不能说是没有意义……"
    hide リオン_基本_杖_見下し

    # 里昂 「私、また蓮くんの事みえてなかった…ね…」
    show リオン_基本_杖_悲しい2 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0786.ogg"
    lion リオン_基本_杖_悲しい2 "我，又没有看到莲君的事情……呢……"
    hide リオン_基本_杖_悲しい

    # 莲 「いや、言う事は間違っていない」
    lian "不，你说的不对"

    # nil 「部俺は、床にへたりこんでしまったリオンをゆっくり後ろから抱きしめる。」
    "我慢慢地从后面抱住了瘫倒在地板上的里昂"

    # 莲 「これはもう、俺とお前の問題だ。俺だって結果が出ないんじゃ、努力した事にはならない派だぜ」
    lian "这是我和你的问题了。我觉得如果没有得到结果，并不意味着你没有努力"

    # 里昂 「んっ…」
    voice "voice/リオン/ron_a1_0787.ogg"
    lion リオン_基本_杖_悲しい2 "嗯……"

    # nil 「リオンの身体は弱々しく震えていた。」
    "里昂的身体虚弱地颤抖着"

    # nil 「か細い息を漏らすように、リオンは俺の身体に体重を預けてくる。」
    "里就像发出微弱的呼吸一样，昂把体重压在了我的身体上"

    # nil 「そういえば…こんな風にリオンと抱き合ってなかったな…。」
    "这么说来…还没有试过像这样和里昂拥抱呢…"

    # nil 「結局、エッチをしたのもリオンと結ばれた当日だけで、それ以来は忙しくて考えすらもしなかった。」
    "结果，做了H的事情也只有和里昂结合的当天，那之后忙得连想都没想过"

    # nil 「キスも。」
    "Kiss也是"

    # 莲 「久しぶりだな…こうやって抱き合うの」
    lian "好久没做了……像这样拥抱着"

    # 里昂 「ん…そだね…ぁう…どうしよ…私、時間ないのに…もっとして欲しいと思ってる…」
    show リオン_基本_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0788.ogg"
    lion リオン_基本_杖_嬉しい "是啊……嗯……怎么办……我，时间不够了……还想要更多……"
    hide nリオン_基本_杖_悲しい2

    # 莲 「それは奇遇だな…」
    lian "那真是奇怪啊…"

    # nil 「俺とリオンは、フローリングに敷かれたカーペットの上で身を寄せ合う。」
    "我和里昂，在铺着地板的地毯上互相依偎"

    # nil 「どうとも言えない安心感が身体を包み込む。」
    "无法形容的安心感包围着身体"

    # nil 「こんな状況だけど…いや、こんな状況だからこそか…リオンの事がより愛おしくなる。」
    "虽然是这样的状况…不，正因为是这样的状况…我更喜欢里昂了"

    # nil 「手が勝手に…といったら恥ずかしいが、自然に両手がリオンの身体を撫でるようにまさぐりはじめる。」
    "我的手自作主张……虽然这么说有点不好意思，但双手自然而然地开始摸索，抚摸着里昂的身体"

    # 里昂 「は、ぁん…」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0789.ogg"
    lion リオン_基本_杖_微笑み "哈、啊呜……"
    hide リオン_基本_杖_嬉しい

    # nil 「リオンも、躊躇い気味ではあるが、逆らおうとはしない。」
    "里昂也有点犹豫，但是不想反抗"

    # nil 「このま、流されるのは良くない…。とも思いながら、でも…身体が止まらない。」
    "就这样随波逐流是不好的…。但是…身体却停不下来"

    # nil 「いっその事リオンも拒否してくればよかった。」
    "干脆连把这些事都拒绝好了"

    # nil 「けど…。」
    "但是…"

    # 里昂 「はぁ…はぁ…れんく…ん…んぅ…」
    show リオン_基本_杖_悲しい2 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0790.ogg"
    lion リオン_基本_杖_悲しい2 "哈啊……哈啊……莲君……嗨……"
    hide リオン_基本_杖_微笑み

    # nil 「切なそうな息をもらして、くてっと脱力してしまう。」
    "痛苦地叹了口气，突然无力了"

    # 莲 「リオン…」
    lian "里昂……"

    # nil 「俺の手が、勝手にリオンのアゴをつかんで、くいっとこちら側に向ける。」
    "我的手随意抓住里昂的下巴，一下子转向这边"

    # nil 「もう、キスしてしまったら戻れない…。」
    "如果，在这里Kiss了的话，就再也回不来了…"

    # 里昂 「ぁっ…」
    voice "voice/リオン/ron_a1_0791.ogg"
    lion リオン_基本_杖_悲しい2 "啊……"

    # nil 「リオンは、ゆっくりと目を閉じる。」
    "里昂慢慢地闭上眼睛"

    # nil 「まぁ…いか…。」
    "嘛……做吧……"

    # nil 「もう、流されてしまえ。」
    "现在，就随波逐流吧"

    # nil 「俺はブレーキを解除して、リオンに唇を近づける…。」
    "我解除了刹车，把嘴唇靠近里昂…"

    # nil 「その時だった。」
    "就在那时"

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「そこまでだ。サカりのついた犬共」
    # 参考资料：https://www.weblio.jp/content/%E3%81%95%E3%81%8B%E3%82%8A
    voice "voice/その他/mjf_a1_0048.ogg"
    mj MJ_通常 "到此为止，发情的狗狗们"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「はうあっ！」
    show リオン_基本_杖_驚き_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0792.ogg"
    lion リオン_基本_杖_驚き_1 "哈呜啊！"
    hide リオン_基本_杖_悲しい2

    # 莲 「おっぷす！」
    lian "Oops！"

    # nil 「頭上から鋭い声が飛んでくる。」
    "一个尖锐的声音从头顶传来"

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「おっぱじめる前に、俺を解放してくれないか。てめぇらのファックを黙って眺めてるほどお人好しじゃねぇぞ」
    voice "voice/その他/mjf_a1_0049.ogg"
    mj MJ_通常 "你们开始之前，放了我吧。我可没法儿默默的当个好人看你们〇〇的"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「あー！　そ、そうだね！　よし、マイケル、ほら、遊んでおいで！今までありがとう！」
    show リオン_基本_杖_にっこり_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0793.ogg"
    lion リオン_基本_杖_にっこり_1 "啊——！是、是的啊！好了，迈克尔，去吧，去玩吧！谢谢你为我做的一切！"
    hide リオン_基本_杖_驚き_1

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「ちっ…最初からそうしてくれよな…とのデートをキャンセルした分。あとできっちり返してもらうぞ！」
    voice "voice/その他/mjf_a1_0050.ogg"
    mj MJ_通常 "呃啊……一开始就该这么做吧……和JK取消约会的份，之后要好好还给我啊"

    # 莲 「彼氏が出来たのか…」
    lian "有对象了……？"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「うん…この前預けたときに、意気投合したらしくて…」
    hide リオン_基本_杖_にっこり_1
    show リオン_帽子無し_杖_微笑み at love69_lion_center
    with dissolve
    voice "voice/リオン/ron_a1_0794.ogg"
    lion リオン_帽子無し_杖_微笑み "嗯……上次我把他留给她的时候，他们似乎很合得来……"

    # nil 「リオンが窓を開け放つと、ぱたぱたと羽ばたきながら、帽子は星空へと消えていった。」
    "里昂打开窗户，帽子啪嗒啪嗒地振翅高飞，消失在星空中"

    # 里昂 「ふう…さて…と…がんばろっか」
    show リオン_帽子無し_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0795.ogg"
    lion リオン_帽子無し_杖_にっこり "呼……接下来，加油吧"
    hide リオン_帽子無し_杖_微笑み

    # 莲 「あ、あ、そうだな…」
    lian "啊，啊，是啊…"

    # nil 「俺達二人は、先ほどの事が何もなかったように資料漁りを始める。」
    "我们俩就像刚才什么事都没有发生一样继续搜集资料"

    # nil 「しかし…。」
    "但是…"

    # 里昂 「生命の神秘…赤ちゃんはどこからくるの…？」
    show リオン_帽子無し_杖_無表情_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0796.ogg"
    lion リオン_帽子無し_杖_無表情_1 "生命的奥秘……婴儿从何而来……"
    hide リオン_帽子無し_杖_にっこり

    # 莲 「暗黒物質…ダークマター」
    # 参考资料：https://ja.wikipedia.org/wiki/%E6%9A%97%E9%BB%92%E7%89%A9%E8%B3%AA
    lian "暗物质…Dark Matter（L:Dark Matter，暗物质，是指不与电磁力产生作用的物质，也就是不会吸收、反射或发出光。人们目前只能透过重力产生的效应得知，而且已经发现宇宙中有大量暗物质的存在）"

    # 里昂 「愛の形…恋の行く末…」
    show リオン_帽子無し_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0797.ogg"
    lion リオン_帽子無し_杖_微笑み "爱的形式……恋的未来……"
    hide リオン_帽子無し_杖_無表情_1

    # 莲 「スカラー波とは。パナウェーブ研究所を追え」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%B9%E3%82%AB%E3%83%A9%E3%83%BC%E6%B3%A2
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%91%E3%83%8A%E3%82%A6%E3%82%A7%E3%83%BC%E3%83%96%E7%A0%94%E7%A9%B6%E6%89%80
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%B9%E3%82%AB%E3%83%A9%E3%83%BC%E9%9B%BB%E7%A3%81%E6%B3%A2
    lian "Scalar wave……Pana-Wave Laboratory（L:Scalar wave，标量波，在数学和物理学中，标量场或标量值函数将标量值与空间中的每个点相关联，比如物理上的整个空间的温度分布、流体中的压力分布，"
    luckykeeper "Pana-Wave Laboratory，日本的一个宗教团体，声称“标量电磁波对人体有害”，而标量电磁波专门用于伪科学。目前科学支持的电磁波是矢量波，而不是标量波）"

    # 里昂 「キス…それは誓いの証」
    show リオン_帽子無し_杖_悲しい2 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0798.ogg"
    lion リオン_帽子無し_杖_悲しい2 "Kiss……这是誓言的证明"
    hide リオン_帽子無し_杖_微笑み

    # 莲 「海に沈んだ文明。アトランティスの謎」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%A2%E3%83%88%E3%83%A9%E3%83%B3%E3%83%86%E3%82%A3%E3%82%B9
    lian "沉入大海的文明。亚特兰蒂斯之谜（L:意为“阿特拉斯的岛屿”，传说中拥有高度文明发展的古老大陆，最早的描述出现于古希腊哲学家柏拉图的著作《对话录》里，据称其在公元前一万年左右被大洪水所毁灭，沉入海底）"

    # 里昂 「……」
    show リオン_帽子無し_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0799.ogg"
    lion リオン_帽子無し_杖_微笑み "……"
    hide リオン_帽子無し_杖_悲しい2

    # 莲 「……」
    lian "……"

    # 里昂 「あもう！　集中できないよ！」
    show リオン_帽子無し_杖_ぶわー at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0800.ogg"
    lion リオン_帽子無し_杖_ぶわー "啊——真是的！完全无法集中注意力啊！"
    hide リオン_帽子無し_杖_微笑み

    # 莲 「リオンだってさっきから恋愛関係の文字列ばっか並べてるじゃねぇか！」
    lian "里昂不是从刚才开始就一直在排列恋爱关系的文字吗！"

    # 里昂 「だって！　だってだって！」
    show リオン_帽子無し_杖_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0801.ogg"
    lion リオン_帽子無し_杖_驚き "可！可是可是！"
    hide リオン_帽子無し_杖_微笑み

    # 里昂 「…うぅ～…あんな…ドキドキする事されたら…意識しちゃうよ…」
    show リオン_帽子無し_杖_悲しい2 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0802.ogg"
    lion リオン_帽子無し_杖_悲しい2 "……呜呜~……那种……dokidoki的事情……还是会意识到的……"
    hide リオン_帽子無し_杖_驚き

    # nil 「リオンは、ぺたんと床に座り込んだ。パサッと資料が足下に落ちた。」
    "里昂扑通一声坐在了地板上。资料啪嚓一声掉在了脚下"

    # 里昂 「意識しちゃうし…もう…ドキドキしちゃうし…うぅ…っ」
    show リオン_帽子無し_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0803.ogg"
    lion リオン_帽子無し_杖_悲しい "会意识到……已经……心跳加速……呜呜"
    hide リオン_帽子無し_杖_悲しい2

    # 莲 「な、泣くなよ。な」
    lian "呐，不要哭啊"

    # 里昂 「だって…だってぇ…」
    show リオン_帽子無し_杖_悲しい2 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0804.ogg"
    lion リオン_帽子無し_杖_悲しい2 "可是……可是……"
    hide リオン_帽子無し_杖_悲しい

    # nil 「甘えん坊スイッチ入っちゃった。」
    "打开了爱撒娇的开关"

    # nil 「俺はよたよたしながら、へたりこんだリオンを正面から抱きしめる。」
    "我从正面抱住摇摇晃晃地瘫软的里昂"

    # 里昂 「ん…れんくぅん…」
    show リオン_帽子無し_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0805.ogg"
    lion リオン_帽子無し_杖_嬉しい "嗯……莲君……"
    hide リオン_帽子無し_杖_悲しい2

    # nil 「甘えるように、ぎゅーっと抱きついてくる。」
    "她撒娇般地紧紧抱住我"

    # 莲 「なぁ…リオン…。まだ…明日まで時間…あるよな…」
    lian "呐…里昂……还有时间呢……到明天……"

    # 里昂 「うん…」
    show リオン_帽子無し_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0806.ogg"
    lion リオン_帽子無し_杖_微笑み "嗯……"
    hide リオン_帽子無し_杖_嬉しい

    # 莲 「なら、ちょっとぐらいその…イチャついても…大丈夫だよな…？」
    lian "那么就稍微亲热一下……没关系的吧…？"

    # nil 「俺はリオンの頭を撫でながら、唇に唇を重ねた。」
    "我抚摸着里昂的头，嘴唇重叠在了一起"

    # 里昂 「んぅ…ちゅぅ…ん…すき…すきぃ…」
    show リオン_帽子無し_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0807.ogg"
    lion リオン_帽子無し_杖_にっこり "嗯……啾……喜欢……喜欢……"
    hide リオン_帽子無し_杖_微笑み

    # 里昂 「れんくぅん…えっち…しよぉ…」
    show リオン_帽子無し_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0808.ogg"
    lion リオン_帽子無し_杖_嬉しい "莲君……H……来做吧……"
    hide リオン_帽子無し_杖_にっこり

    # 莲 「あ。先の事はしてから考えよっか」
    lian "啊，先做了再来考虑吧"

    # 里昂 「んぅ…ふぁ…あぃ…ちゅぅ…っ」
    show リオン_帽子無し_杖_にっこり_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0809.ogg"
    lion リオン_帽子無し_杖_にっこり_1 "嗯……嗯……嘿……啾……"
    hide リオン_帽子無し_杖_嬉しい

    # 里昂 HScene2 Skip~
    # 810-959
    image bg pixiv = "images/extra/luckykeeper/pixiv.webp"
    if persistent.hsceneG:
        scene pixiv with dissolve
        pause 2.0

    else:
        pass

    # 里昂的 HScene 比较少捏，从 HS 的质量来说感觉里昂的好一些，心爱和真冬的似乎有点画崩了……

    stop music fadeout 2.0
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 自室a_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # nil 「ポタッ」
    "啪嗒"

    # nil 「その瞬間だった。」
    "就在社保的那个瞬间"

    # nil 「ペカー！　」
    "噼咔！！"

    # nil 「リオンの足下に置かれていた、とサンプルの詰められたクーラーボックスが煌々と輝きはじめる。」
    "放在里昂脚下的装满样品的冷藏箱开始闪闪发光"

    # nil 「まさか…！」
    "难道…！"

    # 莲 「お、おい、リオンこれ…」
    lian "喂，喂，里昂这个……"

    # 里昂 「ふわ…ん…なぁに…？　ぁっ！」
    show リオン_帽子無し_杖なし_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0960.ogg"
    lion リオン_帽子無し_杖なし_驚き "哇…嗯……什么啊…？啊！"

    # nil 「エッチの余韻に浸っていたリオンだが、事態に気づいたのか、一気に素に戻り、衣服と表情を整えた。」
    "沉浸在H余韵中的里昂，可能是察觉到了事态，一下子恢复了正常，整理了衣服和表情"

    # nil 「俺もいそいでポコチンをしまう。」
    "我也赶紧把金棒收起来"

    # 里昂 「これは…。いや、そんなはずは…。とりあえず蓮くん！　しっかりしたものに掴まって　急いで！」
    show リオン_帽子無し_杖なし_無表情_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0961.ogg"
    lion リオン_帽子無し_杖なし_無表情_1 "这是……不，这不可能是……总之，莲君！抓住牢固的东西，快点！"
    hide リオン_帽子無し_杖なし_驚き

    # 莲 「了解！」
    lian "了解！"

    # nil 「そう言いながら俺はリオンの身体にしがみつく」
    "我一边这样说着一边紧紧抱住了里昂的身体"

    # 里昂 「…いやあの」
    show リオン_帽子無し_杖なし_ジト目 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0962.ogg"
    lion リオン_帽子無し_杖なし_ジト目 "…不，那个"
    hide リオン_帽子無し_杖なし_無表情_1

    # 莲 「だってこが一番安全じゃないかな」
    lian "所以这样不是最安全的吗？"

    # 里昂 「…そうやって抱きつかれてると、集中できないんだけど…」
    show リオン_帽子無し_杖なし_見下し at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0963.ogg"
    lion リオン_帽子無し_杖なし_見下し "……被这样抱住的话，就无法集中精神了…"
    hide リオン_帽子無し_杖なし_ジト目

    # 莲 「だめだ耐えろ」
    lian "不行，忍耐一下"

    # 里昂 「むぅ…よし、開けるよ！　せーのっ！」
    show リオン_帽子無し_杖なし_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0964.ogg"
    lion リオン_帽子無し_杖なし_微笑み "呜呜…好，打开吧！3——2"
    hide リオン_帽子無し_杖なし_見下し

    # nil 「リオンがクーラーボックスの蓋をあける。」
    "里昂打开冷藏箱盖"

    # nil 「BRAAAAAAAAZ！」
    "BRAAAAAAAAZ！"

    # 里昂 「くっ…！」
    show リオン_帽子無し_杖なし_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0965.ogg"
    lion リオン_帽子無し_杖なし_驚き "哇…！"
    hide リオン_帽子無し_杖なし_微笑み

    # 莲 「なんつー衝撃だ！」
    lian "多么震撼！"

    # nil 「蓋を開けた瞬間、眩しい程の光が視界を覆い尽くす。世界が歪んだのではないかと思う程の衝撃を受ける。」
    "打开盖子的瞬间，耀眼的光芒将视线覆盖殆尽。受到了让人觉得世界是不是扭曲了的冲击"

    # nil 「部屋の中の本や資料が巻き上げられて、やがて地面に落ちた。」
    "房间里的书和资料被卷飞起来，然后掉到了地上"

    # nil 「リオンにしがみついていたからよかったが、これ下手したら壁にたきつけられたんじゃないのか…。」
    "还好我紧紧抓着里昂不放，不然的话，不是就会撞到墙上吗…"

    # nil 「そして俺たち二人の視界が戻って来た時、煌々と輝くサンプルのアイス達がクーラーボックス内に鎮座していた。」
    "然后当我们两个人的视线恢复过来的时候，闪闪发光的样品冰淇淋正坐落在冷藏箱里"

    # nil 「それが明らかに凄い物だというのは、一般人の俺にもわかる。」
    "作为普通人的我也知道那明显是很厉害的东西"

    # 里昂 「そうか…私達二人でしか作れないアイス…。そういうことだったのか…」
    show リオン_帽子無し_杖なし_無表情_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0966.ogg"
    lion リオン_帽子無し_杖なし_無表情_1 "是吗…只有我们两个人才能做的冰淇淋……原来是这样啊…"
    hide リオン_帽子無し_杖なし_驚き

    # 莲 「…どういうことだね？」
    lian "…是怎么回事呢？"

    # nil 「さすがに察しのい彼氏な俺だが、今回ばかりはリオンに説明を願おう。」
    "我真是个没直觉的男朋友，这次就拜托里昂说明一下吧"

    # 里昂 「えーとね、説明するのは恥ずかしいから、そのま抱きしめて貰えるかな」
    show リオン_帽子無し_杖なし_悲しい2 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0967.ogg"
    lion リオン_帽子無し_杖なし_悲しい2 "那个啊，因为说明起来很不好意思，所以能请你抱着我吗？"
    hide リオン_帽子無し_杖なし_無表情_1

    # 莲 「わかった」
    lian "我知道了"

    # 里昂 「ありがとう。えっとね、まぁ要は…私と蓮くんの二人でしかできない事って…要は…私達二人でエッチする事…じゃん？」
    show リオン_帽子無し_杖なし_微笑み_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0968.ogg"
    lion リオン_帽子無し_杖なし_微笑み_1 "谢谢。那个啊，总之…只有我和莲两个人才能做的事…重要的事…是我们两个人的H不是吗？"
    hide リオン_帽子無し_杖なし_悲しい2

    # 莲 「…まぁ、それは…そうだな。俺達二人にしかできないな」
    lian "啊，那个……是啊。只有我们两个人才能做"

    # 里昂 「エッチっていうか…愛し合った結果…がエッチなわけで…。それで…えと…えと…私の…」
    show リオン_帽子無し_杖なし_悲しい2 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0969.ogg"
    lion リオン_帽子無し_杖なし_悲しい2 "说是H，其实是相爱的结果……所以……嗯……我的……"
    hide リオン_帽子無し_杖なし_微笑み_1

    # 莲 「察した」
    lian "我明白了"

    # 莲 「つまり、リオンの愛液と俺の精液が混じった物が、アイスに入っちゃった…ということか…」
    lian "也就是说，里昂的汁水和我的白浊液混合在一起的东西，居然进到了冰淇淋里面……"

    # 里昂 「うん。魔女の体液には魔力が秘められてるんだけど…」
    show リオン_帽子無し_杖なし_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0970.ogg"
    lion リオン_帽子無し_杖なし_微笑み "嗯，魔女的体液里隐藏着魔力"
    hide リオン_帽子無し_杖なし_悲しい2

    # 莲 「ちょっと待て。その理屈だと、前のラブポーション・シクスティナインは…？」
    lian "等一下，按照这个道理，之前的LOVEPOTION・SIXTYNINE是……？"

    # 里昂 「あ、あれは…私が蓮くんの事を考えて一人でした時の…その…！」
    show リオン_帽子無し_杖なし_悲しい2 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0971.ogg"
    lion リオン_帽子無し_杖なし_悲しい2 "啊，那是…我一个人想着莲君的事情的时候…那个…！"
    hide リオン_帽子無し_杖なし_微笑み

    # 莲 「ヒョエー！　ハズカシー！　でもそんなんだったら最初から言えよ！」
    lian "哈哈！好厉害！但是那样的话一开始就说出来啊！"

    # 里昂 「う、うるせーうるせー！　乙女の尊厳的な意味でトップシークレットだってばよ！」
    show リオン_帽子無し_杖なし_見下し at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0972.ogg"
    lion リオン_帽子無し_杖なし_見下し "无、无路赛无路赛！就少女的尊严而言，这可是顶级秘密哦！"
    hide リオン_帽子無し_杖なし_悲しい2

    # nil 「些か、ちょっと恥ずかしい理由に目を背けたくなるが、これは…確かに…凄そうだ…。」
    "稍微有点想避开那个不好意思的理由，但这…确实…很厉害…"

    # 里昂 「まぁでも…欠けていた最後のピース…は、私達二人の愛し合った証だったって事だね！」
    show リオン_帽子無し_杖なし_嬉しい_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0973.ogg"
    lion リオン_帽子無し_杖なし_嬉しい_1 "不过…欠缺的最后的一块……就是我们俩相爱的证据吧！"
    hide リオン_帽子無し_杖なし_見下し

    # 莲 「要するに俺とリオンの体液か」
    lian "总之就是我和里昂的体液吗？"

    # 里昂 「だめー！　要するにそういう事だけど、まだ口にするのは恥ずかしいからー！」
    show リオン_帽子無し_杖なし_驚き_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0974.ogg"
    lion リオン_帽子無し_杖なし_驚き_1 "哒咩~！总而言之就是这样，但是说出来还是很不好意思的！"
    hide リオン_帽子無し_杖なし_嬉しい_1

    # nil 「リオンが俺の口をもごもごと塞ぐ。」
    "里昂用手捂住我的嘴"

    # nil 「俺はその手を払いのける。」
    "我推开那只手"

    # 莲 「で、試食ぐらいはしないといけないだろ」
    lian "那么，至少要先试吃一下吧"

    # 里昂 「はっ！　そうだった…！」
    show リオン_帽子無し_杖なし_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0975.ogg"
    lion リオン_帽子無し_杖なし_驚き "啊！是这样…！"
    hide リオン_帽子無し_杖なし_驚き_1

    # nil 「二人して、光輝くアイスをのぞき込む。」
    "两个人一起，看了看闪闪发光的冰淇淋"

    # nil 「僅かながら、そのアイスには俺達の愛液と精液が混じっているわけだが…。」
    "虽然只有一点点，但是那个冰淇淋里混入了我们的体液…"

    # 莲 「…これを食べるのか」
    lian "……这个，真的要吃吗"

    # 里昂 「う…ま、まぁ人に食べさせる前に食べないと…ね…」
    show リオン_帽子無し_杖なし_悲しい2 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0976.ogg"
    lion リオン_帽子無し_杖なし_悲しい2 "嗯…嘛，在给别人吃之前自己没尝过的话……"
    hide リオン_帽子無し_杖なし_驚き

    # 莲 「ていうか人に食べさせるのか…」
    lian "话说这个是要给别人吃啊…"

    # 里昂 「でも、もう時間もネタもないよ！　これに賭けるしかない！」
    show リオン_帽子無し_杖なし_無表情_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0977.ogg"
    lion リオン_帽子無し_杖なし_無表情_1 "但是，已经没有时间和素材了！只能赌在这个上面了！"
    hide リオン_帽子無し_杖なし_悲しい2

    # 莲 「じゃぁ二人でせーので食うぞ！」
    lian "那么两个人一起吃吧！"

    # 里昂 「ばっちこーい！　せーの！」
    # 参考资料：https://jp.quora.com/%E9%87%8E%E7%90%83%E3%81%AE%E7%B7%B4%E7%BF%92%E3%81%A7%E5%8F%AB%E3%82%93%E3%81%A7%E3%81%84%E3%82%8B-%E3%83%90%E3%83%83%E3%83%81%E3%82%B3%E3%83%BC%E3%82%A4-%E3%81%A3%E3%81%A6%E3%81%A9%E3%81%86%E3%81%84%E3%81%86
    show リオン_帽子無し_杖なし_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0978.ogg"
    lion リオン_帽子無し_杖なし_ニタァ "Batch Koi！3——2！（L:前半原文ばっちこーい！是棒球用语，是自我激励用语）"
    hide リオン_帽子無し_杖なし_無表情_1

    # nil 「もぐ」
    "咀嚼"

    # 里昂 「もぐっ」
    show リオン_帽子無し_杖なし_キス at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0979.ogg"
    lion リオン_帽子無し_杖なし_キス "emm"
    hide リオン_帽子無し_杖なし_ニタァ

    # nil 「…」
    "……"

    # nil 「胸の中が…凄く温かい光に包まれていく…。」
    "心中…被非常温暖的光包围着…"

    # nil 「リオンへの愛情か…。これが…。」
    "是对里昂的爱吗…这个…"

    # 莲 「…これ、凄いぞ、リオン…今、俺お前のこと大好き感やべぇ出てる」
    lian "…这个好厉害啊，里昂…现在我有很喜欢你的感觉"

    # 莲 「リオン？」
    lian "里昂？"

    # 里昂 「…ふにゃー…蓮くぅん…すきぃ…えへ…にゃー…」
    show リオン_帽子無し_杖なし_嬉しい_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0980.ogg"
    lion リオン_帽子無し_杖なし_嬉しい_1 "…呼喵…莲君…喜欢…嗯…呼喵…"
    hide リオン_帽子無し_杖なし_キス_1

    # 里昂 「ね…ほら、身体があつくて…こが、きゅんきゅんって…してるの…」
    show リオン_帽子無し_杖なし_悲しい2_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0981.ogg"
    lion リオン_帽子無し_杖なし_悲しい2_1 "喂…你看，身体好热啊…来，想要抱抱……"
    hide リオン_帽子無し_杖なし_嬉しい_1

    # 里昂 「おねがぃ…いっぱいちょうだい…」
    voice "voice/リオン/ron_a1_0982.ogg"
    lion リオン_帽子無し_杖なし_悲しい2_1 "拜托了……再来做更多的……"

    # 莲 「…ごめん、リオン。俺も我慢できそうにない」
    lian "…对不起，里昂。我也忍不住了"

    # 里昂 「きゃー☆」
    show リオン_帽子無し_杖なし_にっこり_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0983.ogg"
    lion リオン_帽子無し_杖なし_にっこり_1 "呀☆"
    hide リオン_帽子無し_杖なし_悲しい2_1

    # nil 「…結果的に完成したのは、即効性の超強力な媚薬でした。（正しくは、二人の愛情を増幅するって事らしいですけど、要は媚薬です）」
    "……结果，最终完成的是速效性超强的媚药（正确地说，好像是能增幅两个人的爱情的效果，总之就是媚药）"

    # nil 「その後、俺とリオンがエッチしまくったおかげで、材料は沢山作れました。」
    "那之后，多亏了我和里昂的H，做了很多出来"

    # scene21 场景1 【梦想的第一战】 结束

    # 离全部翻译完成只剩最后 1 个 Scene ！

    # 过场：里昂（常服）

    # Scene21 结束！
    # 隐藏 quick_menu
    $ quick_menu = False
    play sound "voice/effect/moosehead honk (stinger).ogg"
    # hide screen quick_menu
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)
    scene アイキャッチリオン with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)

    $ renpy.pause(1.5, hard=True)

    $ renpy.end_replay()

    jump scene22

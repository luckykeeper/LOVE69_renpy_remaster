# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene06 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：WorldlineChanger（关于真冬哼的一句歌曲）
# 版本 0.5 "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年3月7日

# 当前流程：编写脚本AIO Process

label scene06:
    # scene06 开始

    # scene06 场景1 【这个莲君就是逊啦，这就病了？】 开始

    # 地点：莲卧室
    # 人物：莲 真冬 心爱
    # BGM：bgm13

    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)
    scene 自室a_朝 at love69_bg1620 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)

    # 显示 quick_menu
    $ quick_menu = True

    # 真冬 「お兄ちゃん、お兄ちゃん…」
    # 325-546 跳过
    show 真冬_制服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0547.ogg"
    dong 真冬_制服_基本_目閉じ "欧尼酱、欧尼酱……"

    # 莲 「ん、んああ…」
    lian "呼、呼嗯……"

    # 真冬 「…ふーむ、ご覧の有様ですよ。虫の息」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0548.ogg"
    dong 真冬_制服_基本_無表情 "......嗯姆，正如你所看到的那样。呼吸困难"
    hide 真冬_制服_基本_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はえー…ちょっとおでこ失礼！」
    # 没有中断
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_0690.ogg"
    ai 心愛_制服_基本_嬉しい "嘿咿呀...稍微用脑门失礼一下!"

    # nil 「ぴとっ」
    "啪的一声"

    # 心爱 「うわ、あっつ…まるで、着地ローダウン、ロンホイ、エアサス、イカリング仕様みたいだね！」
    # 参考资料（着地ローダウン）：https://www.youtube.com/watch?v=ieCNHxTLXqk https://ja.wikipedia.org/wiki/%E3%82%B7%E3%83%A3%E3%82%B3%E3%82%BF%E3%83%B3
    #           ロンホイ         https://www.youtube.com/watch?v=NrY_m42elho
    #           エアサス         https://www.weblio.jp/content/%E3%82%A8%E3%82%A2%E3%82%B5%E3%82%B9 https://www.youtube.com/watch?v=dacE6uz-mkg
    #          イカリング        https://ja.wikipedia.org/wiki/%E3%82%A4%E3%82%AB%E3%83%AA%E3%83%B3%E3%82%B0
    show 心愛_制服_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0691.ogg"
    ai 心愛_制服_基本_驚き "啊、好疼...简直就像底盘着地的LowDown、ロンホイ、エアサス、イカリング的样子呢!"
    hide 心愛_制服_基本_嬉しい

    # Luckykeeper 的豆知识时间到！
    luckykeeper "LowDown是上个世纪70-90年代11区汽车改装的一种潮流，通过替换弹簧等方法改造汽车，使车辆底盘距地面非常低（例如：5cm），能够通过降低视线，增加开车时的速度感，但会容易因不当改造导致安全系数下降，同时因为底盘里地面太近，在过减速带、上下坡等时候容易被卡住"

    luckykeeper "ロンホイ和LowDown类似，但是改的是摩托车，エアサス是指把空气悬挂的汽车也像LowDown那样改造，イカリング是最早出现在宝马车灯上那一圈的名字，这里应该是代指某款车"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ビッグスクーターのカスタムで例えるのはやめろ…」
    voice "voice/真冬/maf_a1_0549.ogg"
    dong 真冬_制服_基本_無表情 "不要拿摩托车的改装来比喻……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「すいませんつい！」
    show 心愛_制服_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0692.ogg"
    ai 心愛_制服_基本_泣き "私密马赛的说！"
    hide 心愛_制服_基本_驚き

    # 莲 「うるせえ」
    lian "闭嘴"

    # nil 「と、いうことで、日頃の不摂生がたり、風邪を引いてしまいました。」
    "于是，因为平时不注意身体健康，感冒了"

    # nil 「真冬が知らせたのか、心配して心愛もお見舞いにきてくれました。」
    "或许是真冬告诉的，很担心我的心爱来探望我了"

    # nil 「といっても、今日は平日なので、二人は学園にいかなきゃなりません。」
    "话虽如此，因为今天是工作日，所以两个人必须要去学校"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぷぅーん。でも、大丈夫なのー？おでこにゆで卵を置いたら目玉焼きになりそうだよね」
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0693.ogg"
    ai 心愛_制服_基本_不機嫌 "哼——不过，真的没关系吗? 在脑门上放的煮鸡蛋变成煎鸡蛋了呢"
    hide 心愛_制服_基本_泣き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「エアコン効いた部屋で全裸で寝るからそうなるのよ」
    show 真冬_制服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0550.ogg"
    dong 真冬_制服_基本_目閉じ "因为在开着空调的房间里裸睡，所以才会这个样子"
    hide 真冬_制服_基本_無表情

    # 莲 「仕方ねぇじゃん、暑いんだもん。あと心愛、ゆで卵は目玉焼きにはならない」
    lian "没办法啊，天气太热了。还有，心爱啊，煮鸡蛋是不能变成煎鸡蛋的哟"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「試してみるか」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0694.ogg"
    ai 心愛_制服_基本_真顔 "想试试看吗"
    hide 心愛_制服_基本_不機嫌

    # 莲 「やらんでいい！」
    lian "不要！！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ふーむ…」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0551.ogg"
    dong 真冬_制服_基本_無表情 "呼—姆……"
    hide 真冬_制服_基本_目閉じ

    # nil 「真冬は何か考え込んだ様子で、背中を向ける。」
    "真冬一副沉思的样子，背过身去"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ねぇねぇ、蓮くん」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_0695.ogg"
    ai 心愛_制服_基本_嬉しい "呐呐，莲君"
    hide 心愛_制服_基本_真顔

    # 莲 「なんだね心愛ちゃん」
    lian "怎么啦，心爱酱"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「どーしよっかなー」
    show 真冬_制服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0552.ogg"
    dong 真冬_制服_基本_目閉じ "该怎么办呢?——"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「この前ね、漫画で読んだんだけどね、なんか、指先一つで楽になるツボがあるらしくてね」
    voice "voice/心愛/cca_a1_0696.ogg"
    ai 心愛_制服_基本_嬉しい "之前在漫画里面看过，好像有一个用手指就能让人轻松起来的穴位呢"

    # 莲 「ほうほう」
    lian "嗬嗬"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「でもなー」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0553.ogg"
    dong 真冬_制服_基本_無表情 "但是——"
    hide 真冬_制服_基本_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「それを押すと、ピプーコリコリコリって音がして、苦しみから解放されるらしいんだ」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0697.ogg"
    ai 心愛_制服_基本_笑顔 "按一下那个地方，就会发出泊哩泊哩泊哩的声音，好像可以从痛苦中解脱出来的样子"
    hide 心愛_制服_基本_嬉しい

    # 莲 「あ？　なんかどっかで聞いた事あんなその効果音。世紀末あたりで」
    # 参考资料：https://ja.wikipedia.org/wiki/%E7%B5%8C%E7%B5%A1%E7%A7%98%E5%AD%94
    lian "啊？好像在哪里听到过那样的效果音的样子。应该是世纪末的时候吧（L:说的是『北斗の拳（1983-1988）』和『蒼天の拳（2001-2010）』两部漫画）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うーん」
    show 真冬_制服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0554.ogg"
    dong 真冬_制服_基本_目閉じ "嗯——"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「試してみてもい？」
    voice "voice/心愛/cca_a1_0698.ogg"
    ai 心愛_制服_基本_笑顔 "阔以来试试吗？"

    # 莲 「あ、思い出した。待て、だめだ、やめろ、秘孔を突くのはやめろ！」
    # 参考资料：https://ja.wikipedia.org/wiki/%E7%B5%8C%E7%B5%A1%E7%A7%98%E5%AD%94
    lian "啊，我想起来了。等等、不行、住手，不要刺秘孔啊！（L:这里的秘孔指经络秘孔，是刚才提到的漫画里面架空的人体要害）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「よし、お兄ちゃん、今日、私看病するよ」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0555.ogg"
    dong 真冬_制服_基本_微笑み "好吧，哥哥，今天我来看护你"
    hide 真冬_制服_基本_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「いっくよー！　念仏を唱えろ！」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_0699.ogg"
    ai 心愛_制服_基本_嬉しい "要上了哟！ 去念佛吧！"
    hide 心愛_制服_基本_笑顔

    # 莲 「アイエエエ！　まふゆちゃーん！」
    lian "啊呀呀呀！嘛呼哟酱（mafuyu，还是说的真冬）！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そこまでだ」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0556.ogg"
    dong 真冬_制服_基本_無表情 "到此为止"
    hide 真冬_制服_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ちっ、邪魔が入ったか…存外、鋭い妹を持っているようだな」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0700.ogg"
    ai 心愛_制服_基本_真顔 "切，有人来阻止我了......看来你的妹妹很是敏锐呢"
    hide 心愛_制服_基本_嬉しい

    # 莲 「あっぶねー！　お兄ちゃんすんでの所であべしする所だったよ」
    lian "太危险了! 哥哥我差点儿就寄了啊"

    # 心爱 「むー、その言いがかりはなんだねもう！」
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0701.ogg"
    ai 心愛_制服_基本_不機嫌 "哼，你这是什么意思嘛！"
    hide 心愛_制服_基本_真顔

    # 莲 「だって念仏を唱えろって言ってるんだもの！」
    lian "因为你说要让我去念佛啊"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「安心しろ、私なら神に祈る暇も与えん」
    show 真冬_制服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0557.ogg"
    dong 真冬_制服_基本_目閉じ "放心吧，我会让你连向神祈祷的时间都没有"
    hide 真冬_制服_基本_無表情

    # 莲 「なんだお前もそっち側か！バトル漫画に影響されたじゃれ合いは余所でやってくれ！」
    lian "什么嘛，你也是那边的啊！受战斗漫画影响的话就在别处去闹啊！"

    # 真冬 「看病しなくていの？」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0558.ogg"
    dong 真冬_制服_基本_無表情 "不需要看护吗？"
    hide 真冬_制服_基本_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「そーだよー！　真冬ちゃんが休むなら私も休んで看病するよー！ね！　まふまふちゃん！」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0702.ogg"
    ai 心愛_制服_基本_笑顔 "就是啊！如果真冬酱休息的话，我也要休息看护你哦！呐，嘛呼嘛呼酱！"
    hide 心愛_制服_基本_不機嫌

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うん。だからお兄ちゃんは安心して寝てなさい？」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0559.ogg"
    dong 真冬_制服_基本_微笑み "嗯，所以欧尼酱你就安心睡觉吧?"
    hide 真冬_制服_基本_無表情

    # 莲 「二人とも気持ちは嬉しいがな…お前らが二人揃って休んだら、寂しがる人もいるんだし…。だいち、騒がしくて寝てもいられねぇ」
    lian "你们两个人的想法都让我很开心。但是你们两个人一起在这里休息的话，有人会想你们的…再说，我被吵的都睡不着了"

    # 心爱 「つれないなぁ。これでも結構本気で心配なんだぞ？」
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0703.ogg"
    ai 心愛_制服_基本_不機嫌 "真是冷酷无情啊。我真的很担心你呢"
    hide 心愛_制服_基本_笑顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うん。あんまりお兄ちゃんが元気ない姿を見たくないかも」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0560.ogg"
    dong 真冬_制服_基本_無表情 "嗯，可能不太想看到欧尼酱你没精打采的样子"
    hide 真冬_制服_基本_微笑み

    # 莲 「しおらしくされてもな…。とにかくだ、どうせ半日なんだから、終わってから看病してくれ」
    lian "就算你这么说也……总之，反正是半天课，结束之后再来照顾我吧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「うーん。それじゃぁ、蓮君寂しくない？」
    show 心愛_制服_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0704.ogg"
    ai 心愛_制服_基本_泣き "嗯。但是，莲君不寂寞吗？"
    hide 心愛_制服_基本_不機嫌

    # 莲 「問題ねぇ、どうせ寝てるだけだから俺にとっちゃ一瞬だ」
    lian "没问题，反正也是在睡觉，对我来说就是一瞬间的功夫"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そっか、じゃぁ、ちょっと行ってくるね。終わったらすぐ戻ってくるから」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0561.ogg"
    dong 真冬_制服_基本_微笑み "这样啊，那我稍微去一下，一结束马上就回来"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「うんうん！　お土産とか色々買って来てあげるね！　代引きで！」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0705.ogg"
    ai 心愛_制服_基本_笑顔 "嗯嗯！我去给你买各种各样的纪念品！用货到付款！"
    hide 心愛_制服_基本_泣き

    # 这里也是两个人说话，但是标了两个人的名字……Scene01打脸了，正式版的时候按照这个修正一下吧
    # 人物表加个，下面的小人物按照原版只显示真冬即可，Scene01及其他地方修正一下吧
    # 人名缩写暂定“aidong”
    # 实际统一使用 ai_dong ，更好辨认，不用“&”是因为不支持
    # 心爱&真冬 『行ってきまーす！』

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0562.ogg"
    ai_dong 真冬_制服_基本_微笑み "我们出发啦!"
    hide 心愛_制服_基本_笑顔 with dissolve
    hide 真冬_制服_基本_微笑み with dissolve

    # 莲 「ああ、いってらっしゃい。あとお土産は直接届けてください」
    lian "啊，路上小心。之后请把纪念品直接送来不要货到付款啊"

    # nil 「真冬と心愛は顔を揃えて微笑むと、俺の部屋から出て行った。」
    "真冬和心爱都面带微笑，走出了我的房间"

    # 莲 「やれやれ…騒がしいったらありゃしない…」
    lian " 哎呀哎呀……真是吵死人了……"

    # nil 「俺はごろんと寝返りを打って、天井を眺めた。少し、世界がまわっているようだ。」
    "我翻了个身，望着天花板。感觉好像有点，世界都在旋转的感觉"

    # 莲 「とはいえ、仲良き事は美しきかな…」
    lian "话虽如此，关系亲密是美好的事情吧…"

    # nil 「心愛と真冬は仲良しだ。それもまぁ当然だろう。」
    "心爱和真冬是好朋友，那也是当然的吧"

    # nil 「実際、心愛にとって真冬も幼馴染みであるわけで、真冬にとっても、同性の姉妹のように仲がい。」
    "实际上，对于心爱来说，真冬也是青梅竹马，对真冬来说，她们的关系就像亲姐妹一样"

    # 莲 「はー…ちょっと、まずいよなぁ…」
    lian "哈…有点，不大妙啊…"

    # nil 「いくらアイスのおかげ（せい？）とはいえ、二人とそれぞれ身体を重ねて、愛を交わし合ってしまった。」
    "尽管（也许是因为）那个冰激凌，但是我和两个人已经互相重叠过身体，彼此相爱了"

    # nil 「おかげで、二人それぞれとはより一層親密になる事ができたが…。」
    "托这个的福，我和两个人变得更加亲密了…"

    # 开门声
    play sound "voice/effect/13_ドア4～あける.ogg"

    # 真冬先快后慢到屏幕中间
    show 真冬_制服_基本_無表情:
        zoom 1.5
        xalign -2.0
        yalign -0.09
        linear 1.0 xalign 0.0
        linear 0.2 xalign 0.3
        linear 0.1 xalign 0.4
        linear 0.1 xalign 0.45
        linear 0.1 xalign 0.485
        linear 0.1 xalign 0.5

    # nil 「ドアが開いて、真冬が入ってきた。」
    "门开了，真冬进来了"

    # 莲 「ん？　なんだ？　忘れ物か？」
    lian "嗯？怎么了？是忘了什么东西吗？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ん…そう、忘れ物」
    voice "voice/真冬/maf_a1_0563.ogg"
    dong 真冬_制服_基本_無表情 "嗯……对，忘了个东西"

    # nil 「そういって真冬はつかつかと、近寄って来て、そっと跪いて、俺の顔に自分の顔を近づけた。」
    "说着，真冬一下子走近，轻轻地跪下来，把自己的脸贴近了我的脸"

    # 真冬放大

    # 定义放大的真冬的参数
    transform love69_dong_bg_center:
        zoom 1.5
        xalign 0.48
        yalign 0.048

    # 真冬 「…ん…ちゅっ…」
    show 真冬_大_制服_基本_キス at love69_dong_bg_center with dissolve
    voice "voice/真冬/maf_a1_0564.ogg"
    dong 真冬_制服_基本_キス "…嗯……啾……"
    hide 真冬_制服_基本_無表情

    # 真冬 「えへ、お兄ちゃん。いってきます」
    show 真冬_大_制服_基本_微笑み at love69_dong_bg_center with dissolve
    voice "voice/真冬/maf_a1_0565.ogg"
    dong 真冬_制服_基本_微笑み "欸嘿嘿，欧尼酱。我出发了"
    hide 真冬_大_制服_基本_キス

    # 莲 「お、おう…」
    lian "啊，嗯…"
    hide 真冬_大_制服_基本_微笑み with dissolve

    # nil 「真冬は振り返らず、部屋を出て行った。」
    "真冬没有回头，走出了房间"

    # nil 「直後。」
    "紧接着"

    # 心爱进来的话和真冬比就比较慢了
    ## 来写动画
    show 心愛_制服_基本_嬉しい:
        zoom 1.5
        xalign -1.0
        yalign -0.09
        linear 0.8 xalign 0.1
        linear 0.1 xalign 0.25
        linear 0.1 xalign 0.35
        linear 0.1 xalign 0.43
        linear 0.15 xalign 0.5
    with dissolve

    # nil 「入れ替わりに心愛が入ってきた。」
    "这次换心爱进来了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「私も忘れ物でーす！！」
    voice "voice/心愛/cca_a1_0707.ogg"
    ai 心愛_制服_基本_嬉しい "我也是忘了东西！！"

    # 莲 「……お、おう」
    lian "……啊，额"

    # nil 「そういって心愛はぱたぱたと近寄って来て、腰を折曲げて、俺の顔に自分の顔を近づけた。」
    "说着，心爱啪嗒啪嗒地靠近，弯着腰，把自己的脸靠近了我的脸"

    # 心爱 「…ん…ちゅっ…」
    show 心愛_大_制服_基本_キス at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0708.ogg"
    ai 心愛_制服_基本_キス "…嗯……啾……"
    hide 心愛_制服_基本_嬉しい

    # 心爱 「にゃ、行ってきます、蓮くん♪」
    show 心愛_大_制服_基本_笑顔 at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0709.ogg"
    ai 心愛_制服_基本_笑顔 "喵，我出发啦，莲君♪"
    hide 心愛_大_制服_基本_キス
    hide 心愛_大_制服_基本_笑顔 with dissolve

    # 莲 「お、おう…」
    lian "啊，嗯…"

    # nil 「心愛もまた、俺の方を振り返らず、部屋を出て行った。」
    "心爱也没有回头，走出了房间"

    # 莲 「いっぺんに来いよ」
    lian "接下来一起来吧"

    # 场景切换：莲卧室->葛城家门口
    image bg 自宅_昼 = "images/bg/自宅_昼.png"
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=True, alpha=True, time_warp=None)
    scene 自宅_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=True, alpha=True, time_warp=None)

    # 心爱 「あー！！　携帯蓮くんの部屋に忘れた－！！」
    show 心愛_制服_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0710.ogg"
    ai 心愛_制服_基本_驚き "啊！！手机忘在莲君的房间里了！！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「あっ私も財布もってきてない。心愛ちゃん、私の携帯と財布を交換しよう」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0566.ogg"
    dong 真冬_制服_基本_無表情 "啊，我也把钱包忘了。心爱酱，用我的手机换你的钱包吧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「いよー！　って微妙に釣り合ってない気が！」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0711.ogg"
    ai 心愛_制服_基本_笑顔 "可以的哦！喂，感觉有点不妙的样子！"
    hide 心愛_制服_基本_驚き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「画像フォルダから好きなだけ画像持ってっていから」
    show 真冬_制服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0567.ogg"
    dong 真冬_制服_基本_目閉じ "图库里面的照片想拿多少拿多少"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「わーい！　じゃぁ、葛城家秘伝の思い出写真とか頂いちゃ…くそっ、なんで縄の写真しかないんだ…」
    show 心愛_制服_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0712.ogg"
    ai 心愛_制服_基本_泣き "好耶！那，我就把葛城家秘传的回忆照片拿走喽…可恶，为什么只有绳子的照片啊…"
    hide 心愛_制服_基本_笑顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「…ユーロ札しか入ってない…。あと同じ店のポイントカードが大量に…」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0568.ogg"
    dong 真冬_制服_基本_無表情 "……里面只有欧元纸钞……还有同一家店的大量积分卡"
    hide 真冬_制服_基本_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「返すね、これ」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0713.ogg"
    ai 心愛_制服_基本_真顔 "还给你，这个"
    hide 心愛_制服_基本_泣き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「私も」
    voice "voice/真冬/maf_a1_0569.ogg"
    dong 真冬_制服_基本_無表情 "我也是"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「後生だから、この荒縄の写真もらってい？　何かに使うかもしれない」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0714.ogg"
    ai 心愛_制服_基本_笑顔 "看在我是后生的份上，你能把这条绳子的照片发给我吗？我可能能用在什么地方"
    hide 心愛_制服_基本_真顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「じゃぁ私も、このポイントカード一枚貰うね…」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0570.ogg"
    dong 真冬_制服_基本_微笑み "那我也要一张这个积分卡…"
    hide 真冬_制服_基本_無表情

    # 场景切换：葛城家门口->莲卧室
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 自室a_朝 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「…あいつらバカだろ」
    lian "…那些家伙是笨蛋吧"

    # nil 「見事に置き忘れられた二人の私物を眺めながら、俺は目を閉じた。」
    "我一边看着完全被两个人遗忘的私人物品，一边闭上了眼睛"

    # 莲 「（なんとかしなきゃな…）」
    lian "（必须要想个办法…）"

    # nil 「何か、きっかけがあれば…。」
    "如果有什么契机的话…"

    # nil 「前も似たような事で悩んでた気がする。」
    "我觉得以前也为类似的事情而烦恼过"

    # 莲 「でも、俺のやった事は間違いじゃ…ないよな…」
    lian "但是我做的事情应该没有错......不是吗"

    # nil 「行為の後、二人はそれぞれ幸せだと伝えてくれた。」
    "H之后，两个人都告诉我说很幸福"

    # nil 「それだけは確かだった。」
    "这一点是肯定的"

    # nil 「唇に残った、二人分の唇の感触が、妙にリアルだった。」
    "残留在嘴唇上的两人嘴唇的触感，非常真实"

    # 原地tp（不是）
    # 下面有一堆歌，能听出歌名的话就去提个PR或者issues吧，顺带记得说下起始结束位置
    image bg 自室a_昼 = "images/bg/自室a_昼.png"
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 自室a_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「～♪」
    show 真冬_私服_基本_まったり at love69_center with dissolve
    voice "voice/真冬/maf_a1_0571.ogg"
    dong 真冬_私服_基本_まったり "～♪（L:真冬这里哼的歌是本作OP full ver.的02:52-03:03）"

    # nil 「歌が聞こえる。夢でも見てるんだろうか。」
    "听到了歌声，我是在做梦吗"

    # 真冬 「～♪」
    voice "voice/真冬/maf_a1_0572.ogg"
    dong 真冬_私服_基本_まったり "～♪（L:真冬这里哼的歌是本作OP full ver.的03:23-03:36，结尾接的是下一首曲子...）"

    # nil 「真冬の声だ。最近の真冬なりのヒットチューンなんだろう、機嫌が良いときは大体あの曲の鼻歌だ。」
    "是真冬的声音。这是最近真冬的热门歌曲吧，她心情好的时候基本上都是在哼唱那首歌"

    # 真冬 「～♪」
    voice "voice/真冬/maf_a1_0573.ogg"
    dong 真冬_私服_基本_まったり "～♪（L:这里没听出来...）"

    # nil 「鼻歌が変わった。」
    "哼的歌变了"

    # nil 「マジックショーとかでよく流れるあの曲だ。」
    # 参考资料1：https://magic.akiha-net.com/bgm.html
    # 参考资料2：https://www.mag2.com/p/news/236457
    # 参考资料3：https://www.bilibili.com/video/av32098616/
    "是在魔术表演中经常播放的那首曲子（L:根据这个描述，搜了一下，感觉应该是『オリーブの首飾り』，感兴趣的可以去B站av32098616听一下）"

    # 真冬 「～♪」
    voice "voice/真冬/maf_a1_0574.ogg"
    dong 真冬_私服_基本_まったり "～♪（L:这里也没听出来...）"

    # nil 「また曲が変わった。」
    "曲子又变了"

    # nil 「今度は、トイレでウンコしたときとかに流れるあの曲だ。」
    "这次是在厕所带薪拉屎（doge）时经常播放的曲子（L:这是什么奇奇怪怪的歌啊...这个就不找了）"

    # 真冬 「～♪」
    # L注：下面的歌词是我加的，原文莫得
    # 对应歌词（从Scene02抄过来的）：よかぜーにさらーわれたなみだー！　ゆきーのけーっしょおーにかーわるー！そのきーみーのよーこーがおだけはー！　なによーりもー！　まもりーたいからー！
    voice "voice/真冬/maf_a1_0575.ogg"
    dong 真冬_私服_基本_まったり "～♪【夜风中被夺走的泪水，化作雪的结晶。看着那样的你的侧脸，是我比任何都最想保护的】（L:这里和前面心爱唱的一样，也是『スターチス』里面1分16秒开始的歌词）"

    # nil 「今度は、何か懐かしい曲だ。去年の冬あたりにヒットした曲だったはず。」
    "这次是一首令人怀念的曲子，应该是去年冬天的热门歌曲"

    # 真冬 「～♪」
    voice "voice/真冬/maf_a1_0576.ogg"
    dong 真冬_私服_基本_まったり "～♪（L:我没听出来……这里W说“印象里叫迷雾森林，国内改编过好多，但疑似名字不对，scarsong和halloween theme是和它同类的，纪录片老演员了”，后来W又仔细听了一下，是X档案(X Files Theme)）"

    # nil 「これは…なんだかとても不安になる曲だ…。ぶっちゃけ怖い。」
    "这是…总觉得是非常不安的曲子…真可怕"

    # 真冬 「～♪」
    # 参考资料：https://zh.wikipedia.org/wiki/%E6%9C%89%E7%A9%BA%E5%8F%A9%E6%88%91
    # 参考资料：https://zh.wikipedia.org/wiki/%E5%8D%A1%E8%8E%89%C2%B7%E8%95%BE%C2%B7%E6%9D%B0%E6%99%AE%E6%A3%AE
    # 参考资料：https://www.zhihu.com/question/20322109/answer/14755575
    voice "voice/真冬/maf_a1_0577.ogg"
    dong 真冬_私服_基本_まったり "～♪（L：我还是没听出来，这里据W听是Call Me Maybe，2011年9月20日发行，卡莉·蕾·杰普森的一首歌曲，是2012年全球销量最高的歌曲，截止2015年7月，歌曲以1800万份全球销量成为了21世纪全球销量最高的由女子演唱的歌曲，并成为了有史以来第4畅销的歌曲）"

    # nil 「こんどは英語の曲だ。ていうかレパートリー広いな真冬。」
    "现在是英文歌，话说真冬你保留曲目真广啊"

    # 真冬 「よーいしょっと…」
    voice "voice/真冬/maf_a1_0578.ogg"
    dong 真冬_私服_基本_まったり "好—嘞…嘿"

    # nil 「ひんやりとした感覚が額に乗せられる。どうやら夢ではなく、現実世界らしい。」
    "额头上传来冰凉的感觉。好像不是梦，而是现实世界捏"

    # 莲 「ん…」
    lian "嗯…"

    # 真冬 「あ、起こしちゃった…かな？」
    show 真冬_私服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0579.ogg"
    dong 真冬_私服_基本_無表情 "啊，我把你吵醒了…是吗？"
    hide 真冬_私服_基本_まったり

    # 莲 「あ、あ…」
    lian "啊、嗯…"

    # nil 「俺がゆっくり目をあけると、学校に行ったはずの真冬が、こちらに顔を向けていた。」
    "我慢慢地睁开眼睛，本应该去学校的真冬，却把脸转向了这边"

    # 莲 「あれ、授業は終わったん？」
    lian "咦，已经下课了吗？"

    # 真冬 「んーん」
    show 真冬_私服_基本_微笑み at love69_center with dissolve
    voice "voice/真冬/maf_a1_0580.ogg"
    dong 真冬_私服_基本_微笑み "不是的哦"
    hide 真冬_私服_基本_無表情

    # nil 「真冬は横に首を振った。」
    "真冬摇了摇头"

    # 真冬 「ばっくれてきた」
    show 真冬_私服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0581.ogg"
    dong 真冬_私服_基本_無表情 "我给翘了"
    hide 真冬_私服_基本_微笑み

    # 莲 「心愛は？」
    lian "心爱呢？"

    # 真冬 「つかまった」
    show 真冬_私服_基本_目閉じ at love69_center with dissolve
    voice "voice/真冬/maf_a1_0582.ogg"
    dong 真冬_私服_基本_目閉じ "被抓住了"
    hide 真冬_私服_基本_無表情

    # 莲 「そうか…」
    lian "是吗…"

    # 真冬 「一部始終を話すと…」
    show 真冬_私服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0583.ogg"
    dong 真冬_私服_基本_無表情 "把其中一部分从头到尾说的话……"
    hide 真冬_私服_基本_目閉じ

    # tp到教室
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=True, alpha=True, time_warp=None)
    scene 教室_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=True, alpha=True, time_warp=None)

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「『ほう。私の授業をサボってお兄ちゃんの看病とは、殊勝な事だな』」
    # 113-13. 跳过
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0131.ogg"
    liu 想瑠_スーツ_見下し "『嗬~翘了我的课去照顾欧尼酱，真是勇气可嘉啊』"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「『お見送りってわけでもなさそうね…』」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0584.ogg"
    dong 真冬_制服_基本_無表情 "这又不是饯别……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「『そこをどいてもらおうか…想瑠！』」
    show 心愛_制服_基本_覚醒01 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0715.ogg"
    ai 心愛_制服_基本_覚醒01 "『请你让开…想瑠！』"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「『おいおい、私はこれでも教師だぞ。バックれようとする生徒がいりゃ、止めるのがスジなんだよ』」
    voice "voice/想瑠/sol_a1_0132.ogg"
    liu 想瑠_スーツ_見下し "『喂喂，我姑且还是老师啊喂，如果有学生想翘课，我就会阻止她』"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「『やはり…口でいっても無駄か…』」
    voice "voice/心愛/cca_a1_0716.ogg"
    ai 心愛_制服_基本_覚醒01 "『果然…用嘴说是没用的啊…』"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「『わかってんじゃねぇか…ナマってねぇだろうな』」
    voice "voice/想瑠/sol_a1_0133.ogg"
    liu 想瑠_スーツ_見下し "『你不是知道吗…不是在耍我吧』"

    # 动画：Rock（可能无法移植）
    ## 上了内存缓存之后就可以放各种各样的动画了
    ### 另外，发现用jpg的话加载就很轻松，多放一些也莫得问题，所以如果不涉及 Alpha 通道就用 jpg 吧！

    # 想瑠 「『上等だ…！』」
    show screen letsrockscr
    voice "voice/想瑠/sol_a1_0134.ogg"
    liu "『上等だ…！』（L:这句话是俗语，意思是“挑衅、真让人不愉快”）"
    hide screen letsrockscr

    # tp回来
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 自室a_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「で、心愛は捕まったと」
    lian "于是，心爱被抓住了"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「あ、いや、なんか二人でヒートアップしてたからこっそり帰ってきました」
    show 真冬_私服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0585.ogg"
    dong 真冬_私服_基本_無表情 "啊，不是这样，好像两个人打得热火朝天，于是我就悄悄溜回来了"

    # 莲 「心愛には一声かけたか？」
    lian "和心爱打招呼了吗？"

    # 真冬 「うん…そしたら…」
    voice "voice/真冬/maf_a1_0586.ogg"
    dong 真冬_私服_基本_無表情 "嗯…然后……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「『奴はこで食い止める。心配いらん、すぐ追いつくさ』」
    voice "voice/心愛/cca_a1_0717.ogg"
    ai 心愛_制服_基本_嬉しい "『我会在这里拦住她的。不用担心，我很快就会追上你的』（L:究极经典flag233）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「だって」
    show 真冬_私服_基本_目閉じ at love69_center with dissolve
    voice "voice/真冬/maf_a1_0587.ogg"
    dong 真冬_私服_基本_目閉じ "但是"
    hide 真冬_私服_基本_無表情

    # 莲 「フラグビンビンじゃねぇか」
    lian "这不是旗手嘛（L:指flag拉满）"

    # 真冬 「や、実際、心愛ちゃんが止めてくれたからこうして早く帰る事ができたんだけどね」
    show 真冬_私服_基本_微笑み at love69_center with dissolve
    voice "voice/真冬/maf_a1_0588.ogg"
    dong 真冬_私服_基本_微笑み "呀，实际上，正是因为心爱酱阻止了她，所以我才能这么早回来"
    hide 真冬_私服_基本_目閉じ

    # 莲 「じゃぁ、後で心愛にはしっかりお礼しないとな」
    lian "那么，回头一定要好好感谢心爱啊"

    # 真冬 「そだね。ケーキ焼いとくよ」
    voice "voice/真冬/maf_a1_0589.ogg"
    dong 真冬_私服_基本_微笑み "是这样的捏，我去烤个蛋糕吧"

    # nil 「俺があたりを見渡すと、俺の身の回りの整理どころか、部屋の掃除までされている事に気づく。」
    "我环视四周，别说是整理我身边的东西，就连房间也打扫的干干净净"

    # 莲 「掃除までしてくれたのか…」
    lian "连打扫都做了吗…"

    # 真冬 「なかなかお兄ちゃんの部屋でゆっくりする事ないからねー」
    voice "voice/真冬/maf_a1_0590.ogg"
    dong 真冬_私服_基本_微笑み "因为在欧尼酱的房间里很难平静地呆着呢"

    # 莲 「なんか、すまないな…」
    lian "总觉得，很对不起…"

    # 真冬 「気にしなくて大丈夫だよー？　病人は病人らしく、おとなしく寝てればいのです」
    voice "voice/真冬/maf_a1_0591.ogg"
    dong 真冬_私服_基本_微笑み "别在意，没关系的，病人就像病人一样，老老实实地睡觉就好了"

    # 莲 「そうさせて貰うよ」
    lian "就这么办吧"

    # nil 「心愛も真冬も、最近、目に見えて優しくなった。この俺も、何か二人のためにできないかと考える。」
    "心爱和真冬最近都明显变得亚撒西了起来，我也在考虑能不能为两个人也做点什么"

    # 莲 「なぁ…真冬」
    lian "呐…真冬"

    # 真冬 「んー？」
    show 真冬_私服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0592.ogg"
    dong 真冬_私服_基本_無表情 "嗯——？"
    hide 真冬_私服_基本_微笑み

    # 莲 「ハワイ…いかねぇか？」
    lian "夏威夷…你想去玩吗？"

    # 真冬 「…いくら熱が出てるからって、そのボケは脈絡なさすぎるかな…」
    show 真冬_私服_基本_ジト目 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0593.ogg"
    dong 真冬_私服_基本_ジト目 "……就算再怎么发烧，这种痴呆也太没有逻辑了吧…"
    hide 真冬_私服_基本_無表情

    # 莲 「ボケてねぇ！　そのジト目はやめろ！今からじゃなくて、夏休みにさ！　心愛が行きたがってたから、３人で行こうって」
    lian "我还没到这个地步呢！别用看关爱傻子的眼神看我啊喂！肯定不是现在，是暑假啊！因为心爱想去，所以想着要不要3个人一起去"

    # 真冬 「あ、いねー。じゃぁ、新しい水着買いに行かなきゃ」
    show 真冬_私服_基本_微笑み at love69_center with dissolve
    voice "voice/真冬/maf_a1_0594.ogg"
    dong 真冬_私服_基本_微笑み "啊，真好——那我得去买新泳衣了"
    hide 真冬_私服_基本_ジト目

    # 莲 「心愛と同じ事言うんだな」
    lian "心爱也是这么说的捏"

    # 真冬 「お兄ちゃんにはわからないと思うんだけど、水着も毎年流行があるからねー。うん、心愛ちゃんと一緒にいってくるよ」
    voice "voice/真冬/maf_a1_0595.ogg"
    dong 真冬_私服_基本_微笑み "欧尼酱应该不知道，泳衣每年都会有流行和淘汰的款式吧。嗯，我会和心爱酱一起去的"

    # 莲 「じゃぁ、ハワイ旅行には乗り気なんだな？」
    lian "那么，你愿意去夏威夷旅行喽？"

    # 真冬 「おふこーす。三人で旅行かー、絶対楽しくなるね！」
    show 真冬_私服_基本_まったり at love69_center with dissolve
    voice "voice/真冬/maf_a1_0596.ogg"
    dong 真冬_私服_基本_まったり "Of——Course，三个人一起旅行啊，一定会很开心的"
    hide 真冬_私服_基本_微笑み

    # 莲 「おう、楽しみにしてもらえたなら何よりだ」
    lian "嗯，如果你开心的话，那就比什么都好了"

    # 真冬 「そのためにも、今は風邪を治して貰わないと…だね♪」
    show 真冬_私服_基本_微笑み at love69_center with dissolve
    voice "voice/真冬/maf_a1_0597.ogg"
    dong 真冬_私服_基本_微笑み "为了这个，现在就必须要把感冒治好…对吧♪"
    hide 真冬_私服_基本_まったり

    # 莲 「んな大げさな」
    lian "这有点太夸张了"

    # nil 「ともあれ、安静にするしかやりようがないので、真冬の言いつけ通りに、ひたすら休息を続行する。」
    "不管怎么说，因为能够安静下来，所以按照真冬的嘱咐，一个劲儿地休息"

    # 真冬 「あ、そうだそうだ。はい、お兄ちゃん、これ、作ってきたよ」
    voice "voice/真冬/maf_a1_0598.ogg"
    dong 真冬_私服_基本_微笑み "啊，对了对了，给，欧尼酱，我做了这个"

    # 莲 「なにこれ」
    lian "这是什么？"

    # 真冬 「サムゲタン」
    # 参考资料：https://zh.wikipedia.org/wiki/%E8%94%98%E9%9B%9E%E6%B9%AF
    # 参考资料2：https://ja.wikipedia.org/wiki/%E3%82%B5%E3%83%A0%E3%82%B2%E3%82%BF%E3%83%B3
    show 真冬_私服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0599.ogg"
    dong 真冬_私服_基本_無表情 "参鸡汤（L:参鸡汤（韩语：삼계탕／蔘鷄湯）朝鲜半岛的传统名菜之一，以整只童子鸡，腹中塞入糯米、佐以红枣、姜、蒜和人参长时间炖煮制成，最早出现于上世纪60年代，在70年代以后逐渐家喻户晓）"
    hide 真冬_私服_基本_微笑み

    # 莲 「微妙にマニアックなネタはやめろ」
    lian "别把我当烧晕了的人啊喂！（L:参鸡汤里的人参，在因感冒等发热时食用会引起心悸）"

    # 真冬 「と、トッポギとマッコリ」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%88%E3%83%83%E3%83%9D%E3%83%83%E3%82%AD
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%9E%E3%83%83%E3%82%B3%E3%83%AA
    show 真冬_私服_基本_目閉じ at love69_center with dissolve
    voice "voice/真冬/maf_a1_0600.ogg"
    dong 真冬_私服_基本_目閉じ "给，辣炒年糕和马格利（L:辣炒年糕又称韩式炒年糕，是由水煮条状年糕、肉、菜及调味汁制成，上桌前会在上面加白果及核桃。马格利又称农酒，是朝鲜半岛一种用米发酵而制成的浊米酒）"
    hide 真冬_私服_基本_無表情

    # 莲 「本格的にするのもやめろ」
    lian "不要让我动真格啊！（L:马格利有添加人工甘味料阿斯巴甜，可能对人体有害，但是韩国食品和药物管理局表示“只要不超过每日摄入量就没有问题”）"

    # 真冬 「これはモッコリ」
    show 真冬_私服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0601.ogg"
    dong 真冬_私服_基本_無表情 "这个很搞笑"
    hide 真冬_私服_基本_目閉じ

    # 莲 「うるせえ」
    lian "闭嘴"

    # 真冬 「まぁ、ポカリとおかゆですよ」
    # 参考资料：https://zh.wikipedia.org/wiki/%E5%AF%B6%E7%A4%A6%E5%8A%9B%E6%B0%B4%E7%89%B9
    # 参考资料：https://www.wikiwand.com/ja/%E3%81%8A%E3%81%8B%E3%82%86
    # 参考资料：https://ja.wikipedia.org/wiki/%E7%B2%A5
    show 真冬_私服_基本_微笑み at love69_center with dissolve
    voice "voice/真冬/maf_a1_0602.ogg"
    dong 真冬_私服_基本_微笑み "嘛，这回是宝矿力和粥哦（L:宝矿力水特，简称宝矿力，是日本大冢制药株式会社于1980年研发的一种运动饮料）"
    hide 真冬_私服_基本_無表情

    # 真冬 「ふー……ふー……ふー……よし…はい、あーん」
    voice "voice/真冬/maf_a1_0603.ogg"
    dong 真冬_私服_基本_微笑み "呼……呼……呼……好啦…来，啊—嗯"

    # 莲 「あーん」
    lian "啊—嗯"

    # nil 「真冬が、れんげにおかゆを乗せて、俺の口へと運んでくれる。」
    "真冬把粥放在勺子上，再送到我的嘴里"

    # nil 「絶妙な熱加減まで調節されたおかゆが、風邪で消化器官の衰えた俺の内臓に染みこんでいく。」
    "被加热到绝妙的温度的粥，渗透到因感冒而导致消化器官衰弱的我的内脏里"

    # 真冬 「美味しい？」
    voice "voice/真冬/maf_a1_0604.ogg"
    dong 真冬_私服_基本_微笑み "好吃吗？"

    # 莲 「最高」
    # 很多人应该都知道这个表达吧，这里就不翻了（doge）
    lian "最高！"

    # 真冬 「よかった。じゃぁ次は…ん…くっ…んっ」
    show 真冬_私服_基本_目閉じ at love69_center with dissolve
    voice "voice/真冬/maf_a1_0605.ogg"
    dong 真冬_私服_基本_目閉じ "太好了，那么接下来…咕…咕…"
    hide 真冬_私服_基本_微笑み

    # 莲 「あ、それ俺のポカリじゃなかったのかよ」
    lian "啊，那不是我的宝矿力吗？"

    # 真冬 「んーん。んー、んぅーんー」
    voice "voice/真冬/maf_a1_0606.ogg"
    dong 真冬_私服_基本_目閉じ "嗯——嗯，嗯—，嗯——嗯"

    # nil 「あろうことか、真冬はペットボトルに入ったポカリを自分の口に含んでしまった。」
    "真不敢相信，真冬竟然把装在塑料瓶里的宝矿力含在了自己嘴里"

    # nil 「そして、何を意図しているのかは不明だが、首を振って、俺の口元を抑えた。」
    "然后，虽然我不知道她想做什么，但是她摇了摇头，捂住了我的嘴"

    # 莲 「んむっ！？」
    lian "嗯！？"

    # 真冬 「ん…ちゅぅ…んむ…」
    show 真冬_大_私服_基本_キス at love69_dong_bg_center with dissolve
    voice "voice/真冬/maf_a1_0607.ogg"
    dong 真冬_私服_基本_キス "嗯……嗯…嗯……"
    hide 真冬_私服_基本_目閉じ

    # nil 「真冬が俺にやろうとしたことに気づいたのは、真冬が事に及んでからだった。」
    "直到真冬和我的肌肤接触之后，我才意识到真冬想对我做什么"

    # nil 「真冬の口から、真冬の唾液と共にポカリが流れ込んでくる。」
    "从真冬的口中，宝矿力随着真冬的唾液流了进来"

    # 莲 「ぶはぁっ！」
    lian "噗哈！"

    # 真冬 「むー！」
    voice "voice/真冬/maf_a1_0608.ogg"
    dong 真冬_私服_基本_キス "哇啊！"

    # nil 「突然の事に、驚いた俺は、つい吹き出してしまった。」
    # つい吹き出してしまっ用法参考：https://curazy.com/archives/54150
    "突如其来的事情，让我大吃一惊，忍不住笑了出来"

    # 真冬 「もーこぼさないでもらえますー？」
    show 真冬_大_私服_基本_ジト目 at love69_dong_bg_center with dissolve
    voice "voice/真冬/maf_a1_0609.ogg"
    dong 真冬_私服_基本_ジト目 "真是的，可以请你不要洒出来吗？"
    hide 真冬_大_私服_基本_キス

    # 莲 「だ、だってお前これ、突然やられたらビるってば！」
    lian "可、可是如果我突然这么做的话，一定能吓到你吧"

    # 真冬 「えっちの時は…きす…上手かったのに…」
    show 真冬_大_私服_基本_目閉じ at love69_dong_bg_center with dissolve
    voice "voice/真冬/maf_a1_0610.ogg"
    dong 真冬_私服_基本_目閉じ "H的时候……Kiss……做的很好……"
    hide 真冬_大_私服_基本_ジト目

    # 莲 「は、恥ずかしい事を言うのをやめろ！」
    lian "啊这，别说让我丢人的话了！"

    # 真冬 「はいはいテイク２いきますよー…ん…くっ…」
    # テイク２参考资料：https://ja.wikipedia.org/wiki/Take2
    show 真冬_大_私服_基本_微笑み at love69_dong_bg_center with dissolve
    voice "voice/真冬/maf_a1_0611.ogg"
    dong 真冬_私服_基本_微笑み "好的好的，我们来第二轮(Take2)…嗯…呜…（L:Take2是11区的喜剧二人组的组合名字，1994年成立，由東貴博和深沢邦之组成，都是男的）"
    hide 真冬_大_私服_基本_目閉じ

    # 真冬 「ん…ちゅっ…ん…っ…」
    show 真冬_大_私服_基本_目閉じ at love69_dong_bg_center with dissolve
    voice "voice/真冬/maf_a1_0612.ogg"
    dong 真冬_私服_基本_目閉じ "嗯…啊……嗯…嗯……"
    hide 真冬_大_私服_基本_微笑み

    # 莲 「…んっ…」
    lian "…嗯…"

    # 真冬 「んぅ…んふっ…ぷはっ…はい、よくできました」
    show 真冬_大_私服_基本_微笑み at love69_dong_bg_center with dissolve
    voice "voice/真冬/maf_a1_0613.ogg"
    dong 真冬_私服_基本_微笑み "咕呜……嗯……呼……好，做得很好"
    hide 真冬_大_私服_基本_目閉じ

    # 莲 「ぜぇ…はぁ…まったく、病人には不健康な事をしやがるじゃないか…」
    lian "呼…哈…真是的，你这可是让病人不健康的事啊……"

    # 真冬 「…？」
    voice "voice/真冬/maf_a1_0614.ogg"
    dong 真冬_私服_基本_微笑み "……？"

    # nil 「真冬は、一瞬何の事かわからなかったようだが、俺の目線をゆっくりと追って、掛け布団すら持ち上げる、その存在に気づいた。」
    "真冬一瞬间不知道发生了什么，但她顺着我的视线向下面看去，注意到了它的存在，它甚至把被子都顶了起来"

    # 真冬 「はー…今ので、下半身だけ元気になられてもなー…」
    hide 真冬_大_私服_基本_微笑み with dissolve
    show 真冬_私服_基本_目閉じ at love69_center with dissolve
    voice "voice/真冬/maf_a1_0615.ogg"
    dong 真冬_私服_基本_目閉じ "哈啊…因为刚才的事情，所以只有下半身变得有精神了呢……"

    # 莲 「不可抗力です…」
    lian "这是不可抗力…"

    # 真冬 「やれやれ…妹にポカリ口移しされて、発情しちゃうなんざ…ほんとダメなお兄ちゃんですね」
    show 真冬_私服_基本_微笑み at love69_center with dissolve
    voice "voice/真冬/maf_a1_0616.ogg"
    dong 真冬_私服_基本_微笑み "哎呀哎呀…被妹妹嘴对嘴喂了宝矿力就发情…真是个达咩的欧尼酱啊"
    hide 真冬_私服_基本_目閉じ

    # nil 「なんか、この前と言ってる事が違うような気がするんですが…」
    "总感觉，和之前的态度好像差了很多的样子…"

    # nil 「それもそうか。今は例のアイスを食べてるわけでもなく、平常時の真冬だ。」
    "那也难怪，现在不是恰了那个冰淇淋的状态，而是平时的真冬"

    # 真冬 「今回は別に、誘ったわけじゃないし…」
    show 真冬_私服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0617.ogg"
    dong 真冬_私服_基本_無表情 "这次才不是，想要引诱你的呢……"
    hide 真冬_私服_基本_微笑み

    # 莲 「で、ですよね…いや、大丈夫、ほっときゃ収まるから」
    lian "是、是这样的吗…嘛，没关系，不管它，自己会好的"

    # 真冬 「興奮収まるまでスタンディングオベーションなんでしょ？　この方は」
    show 真冬_私服_基本_目閉じ at love69_center with dissolve
    voice "voice/真冬/maf_a1_0618.ogg"
    dong 真冬_私服_基本_目閉じ "直到兴奋平息为止都是会一直支着帐篷吧？这个家伙"
    hide 真冬_私服_基本_無表情

    # 莲 「誠に遺憾ながら、そういうことになっちゃいますね」
    lian "非常遗憾，事实就是这样的"

    # 真冬 「なっちゃいますか」
    show 真冬_私服_基本_微笑み at love69_center with dissolve
    voice "voice/真冬/maf_a1_0619.ogg"
    dong 真冬_私服_基本_微笑み "变成这样了吗"
    hide 真冬_私服_基本_目閉じ

    # 莲 「はい」
    lian "是的"

    # 真冬 「ふむー…」
    show 真冬_私服_基本_目閉じ at love69_center with dissolve
    voice "voice/真冬/maf_a1_0620.ogg"
    dong 真冬_私服_基本_目閉じ "呼姆…"
    hide 真冬_私服_基本_微笑み

    # nil 「真冬はそっと俺の膨らんだ下腹部に視線を向ける。」
    "真冬悄悄地将视线投向了我鼓胀的下腹部"

    # nil 「一度身体を重ねてるとはいえ、空気が空気なだけに妙に恥ずかしい。」&协力请求，【空気が空気なだけに妙】怪
    "虽说身体已经重叠过一次了，但正因为是这样，所以现在的气氛总让人觉得有点难为情捏"

    # 真冬 「うーん…」
    voice "voice/真冬/maf_a1_0621.ogg"
    dong 真冬_私服_基本_目閉じ "嗯—……"

    # nil 「真冬の手がゆっくり、股間へと向かう。」
    "真冬的手慢慢地向股间摸去"

    # nil 「まさか！」
    "不会吧！"

    # 真冬 「よし」
    show 真冬_私服_基本_微笑み at love69_center with dissolve
    voice "voice/真冬/maf_a1_0622.ogg"
    dong 真冬_私服_基本_微笑み "呦西"
    hide 真冬_私服_基本_目閉じ

    # nil 「ぐっ。　真冬が拳を握る。」
    "突然，真冬握紧拳头"

    # nil 「アカン方のまさかや！」
    "不是吧不是吧！"

    # 莲 「すいません！　それだけは勘弁してください！」
    lian "对不起！请务必饶了我"

    # 真冬 「？　何を期待したの？」
    show 真冬_私服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0623.ogg"
    dong 真冬_私服_基本_無表情 "？你在期待神魔？"
    hide 真冬_私服_基本_微笑み

    # 莲 「え、え？　いや、期待というか…警戒というか…。真冬ちゃんのトールハンマーが俺の避雷針に下るのかと…」
    # トールハンマー参考资料:https://ja.wikipedia.org/wiki/%E3%83%88%E3%83%BC%E3%83%AB%E3%83%8F%E3%83%B3%E3%83%9E%E3%83%BC
    lian "诶？诶？不，该说是期待吗？还是说是警戒呢……真冬的托尔之锤（L:Thor's Hammer，北欧神话的托尔是北欧神话中负责掌管战争与农业的神，锤子名叫Mjölnir）会落到我的避雷针（L:原文如此，懂辽，莲是金针菇）上呢…"

    # 真冬 「お兄ちゃんそっち側の人間なの？」
    show 真冬_私服_基本_ジト目 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0624.ogg"
    dong 真冬_私服_基本_ジト目 "哥哥你原来是那边的人吗？"
    hide 真冬_私服_基本_無表情

    # 莲 「今日なんかやたらジト目向けてこない！？割とその目、俺にとっちゃジャベリンなんですが！」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%B8%E3%83%A3%E3%83%99%E3%83%AA%E3%83%B3
    lian "你今天怎么老是盯着我看! ?或者说，我感觉你的眼神就像Javelin一样（L:Javelin，指标枪，运动会上掷的那个）"

    # 真冬 「ばーか」
    voice "voice/真冬/maf_a1_0625.ogg"
    dong 真冬_私服_基本_ジト目 "笨—蛋"

    # 莲 「はうっ！」
    lian "蛤？！"

    # 真冬 「…はぁ」
    show 真冬_私服_基本_目閉じ at love69_center with dissolve
    voice "voice/真冬/maf_a1_0626.ogg"
    dong 真冬_私服_基本_目閉じ "……哈啊"
    hide 真冬_私服_基本_ジト目

    # 莲 「あの…真冬ちゃん？」
    lian "那个啊…真冬酱？"

    # 真冬 「もー…せっかく人が決意したのに、邪魔しないの」
    show 真冬_私服_基本_微笑み at love69_center with dissolve
    voice "voice/真冬/maf_a1_0627.ogg"
    # dong 真冬_私服_基本_微笑み "害……人家好不容易才下了决心，你就不来搭个话嘛？"
    dong 真冬_私服_基本_微笑み "害……人家好不容易才下了决心，被你这个岔打的"

    # nil 「真冬は一瞬表情を曇らせてから、俺に真顔を向ける。」
    "一瞬间，真冬的表情黯淡了下来，然后，把脸转向了我"

    # 真冬 「これ…その…抜いてあげよっか…？」
    show 真冬_私服_基本_目閉じ at love69_center with dissolve
    voice "voice/真冬/maf_a1_0628.ogg"
    dong 真冬_私服_基本_目閉じ "这个…那个…要我帮你拔下来吗…？"
    hide 真冬_私服_基本_微笑み

    # 莲 「へ？」
    lian "嗯？"

    # 真冬 「だから…もー何度も言わせないでよ、恥ずかしいから！お兄ちゃんが辛いなら…これ…ね…？」
    show 真冬_私服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0629.ogg"
    dong 真冬_私服_基本_無表情 "所以……不要让我再说一遍了，因为我很害羞的啦！如果欧尼酱很痛苦的话……这个…对吧…？"
    hide 真冬_私服_基本_目閉じ

    # 莲 「い、いのか…？　真冬」
    lian "不是，现在吗…？真冬"

    # 真冬 「うん。だって、心愛ちゃんが居る時にこんな風にされてもアレだし…。別に、一回してるんだから、そこまで恥ずかしくない…でしょ？」
    show 真冬_私服_基本_微笑み at love69_center with dissolve
    voice "voice/真冬/maf_a1_0630.ogg"
    dong 真冬_私服_基本_微笑み "嗯。因为，心爱酱在的时候这样做应该也没什么…而且咱们已经都做过一次了，所以也不会觉得有什么不好意思吧…？"
    hide 真冬_私服_基本_無表情

    # 莲 「その、なんだ…お前の気持ちは嬉しいが…」
    lian "那、那啥……你有这样的心情我很高兴……"

    # nil 「おかしい。今回は例のアイスを食べさせたわけではないのに、こんな展開になるとは…。」
    "奇怪。这回明明没有让她吃那个冰淇淋，竟然也会有这样的展开…"

    # nil 「今度は、真冬は普通に発情…？　」
    "这次，真冬是普通的发情…？"

    # nil 「いや、というより、純粋に真冬の優しさか。」
    "与其说不是这样，不如说这纯粹是真冬的温柔吧"

    # 真冬 「…なんか、どんどん大きくなってるんですけど」
    show 真冬_私服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0631.ogg"
    dong 真冬_私服_基本_無表情 "……好像越来越大了呢"
    hide 真冬_私服_基本_微笑み

    # 莲 「すいませんつい！」
    lian "对不起！"

    # 真冬 「で、どうするの？　もっと手荒なのが趣味ならそっちでいくけど」
    show 真冬_私服_基本_ジト目 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0632.ogg"
    dong 真冬_私服_基本_ジト目 "那、那怎么办？如果你的想要更粗暴的话我就那样办"
    hide 真冬_私服_基本_無表情

    # 莲 「優しい方でお願いします。そして出来れば、真冬ちゃんも一緒に楽しめる方で」
    lian "请温柔的对待我，如果可以的话，希望真冬酱你也来和我一起享受"

    # 真冬 「注文が多いなぁ。でも…そーいう優しさ、嬉しいよお兄ちゃん」
    show 真冬_私服_基本_微笑み at love69_center with dissolve
    voice "voice/真冬/maf_a1_0633.ogg"
    dong 真冬_私服_基本_微笑み "要求相当的多捏。但是…这样的温柔，我很开心哦欧尼酱"

    # 真冬 「ちゅっ」
    show 真冬_大_私服_基本_キス at love69_dong_bg_center with dissolve
    voice "voice/真冬/maf_a1_0634.ogg"
    dong 真冬_私服_基本_キス "啾"
    hide 真冬_私服_基本_微笑み

    # nil 「真冬は軽く俺の額にキスをすると、にっこりと笑った。」
    "真冬轻吻了我的额头，微微一笑"

    # 真冬 「えへ…ダメな妹だね、私。お兄ちゃんが自分の行動で興奮してくれると…やっぱり嬉しくなっちゃうみたい」
    show 真冬_大_私服_基本_微笑み at love69_dong_bg_center with dissolve
    voice "voice/真冬/maf_a1_0635.ogg"
    dong 真冬_私服_基本_微笑み "诶嘿嘿……我啊，真是个⑧行的妹妹呢。欧尼酱要是因为我的行动而兴奋的话……果然会很开心"
    hide 真冬_大_私服_基本_キス

    # 莲 「真冬…」
    lian "真冬…"

    # nil 「俺は仰向けのま、真冬の後頭部に手をおいて、顔に近づけた。」
    "我仰着头，把手放在真冬的后脑勺上，靠近了她的脸"

    # 真冬 「ん…ちゅぅ…すき…」
    show 真冬_大_私服_基本_キス at love69_dong_bg_center with dissolve
    voice "voice/真冬/maf_a1_0636.ogg"
    dong 真冬_私服_基本_キス "嗯……啾…嗯"
    hide 真冬_私服_基本_微笑み

    # 莲 「ありがとう、真冬」
    lian "谢谢你，真冬"

    # 真冬 「うん…♪」
    show 真冬_大_私服_基本_目閉じ at love69_dong_bg_center with dissolve
    voice "voice/真冬/maf_a1_0637.ogg"
    dong 真冬_私服_基本_目閉じ "嗯…♪"

    # 真冬 HScene 02 Skip~
    ## 638-771 真冬HS02
    ## 这里到时候要加点料
    scene 自室a_昼 at love69_bg1440 with dissolve
    play music bgmtwentyfour fadeout 0.8 fadein 1.0

    # scene06 场景1 【这个莲君就是逊啦，这就病了？】 结束

    # scene06 场景2 【心爱酱晚来一步】 开始

    # 地点：莲卧室
    # 人物：莲 真冬 心爱 想瑠
    # BGM：

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「勝ったので、想瑠にゃん持って来ました」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_0718.ogg"
    ai 心愛_制服_基本_嬉しい "我赢啦，所以把想瑠喵也一起带过来啦"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ぶえ」
    show 想瑠_スーツ_ぶわ at love69_xiangliu_center
    voice "voice/想瑠/sol_a1_0135.ogg"
    liu 想瑠_スーツ_ぶわ "呜欸~"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「返しておいで」
    show 真冬_私服_基本_目閉じ at love69_left with dissolve
    # voice "voice/真冬/maf_a1_0638.ogg"
    ## 638-771 真冬HS02
    voice "voice/真冬/maf_a1_0771.ogg"
    dong 真冬_私服_基本_目閉じ "还给我"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぶえ」
    show 心愛_制服_基本_ぶわー at love69_right with dissolve
    voice "voice/心愛/cca_a1_0719.ogg"
    ai 心愛_制服_基本_ぶわー "呜欸~"
    hide 心愛_制服_基本_嬉しい

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ぶええ」
    voice "voice/想瑠/sol_a1_0136.ogg"
    liu 想瑠_スーツ_ぶわ "呜欸欸~"

    # 莲 「いじゃねぇかうちで飼おうぜ」
    lian "好耶！那就放在我们家里养吧"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「名前はカイくんがいな」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%AB%E3%82%A4%E3%81%8F%E3%82%93
    show 真冬_私服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0772.ogg"
    dong 真冬_私服_基本_微笑み "名字的话就叫カイくん好了（L:カイくん，2003.10.10-2018.6.28，常常出现在电视CM中的一条狗，名字来源于其出身北海道的“海”，最常出现在软银广告中，根据CM研究院2007年CM人才青睐度调查，它在软银CM的人物类别中排名第一）"
    hide 真冬_私服_基本_目閉じ

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「やめろ」
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0137.ogg"
    liu 想瑠_スーツ_見下し "别说了"
    hide 想瑠_スーツ_ぶわ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「よし、ほら、スタンエッジ！」
    # 参考资料：https://kakuge.com/wiki/pages/%E3%82%B9%E3%82%BF%E3%83%B3%E3%82%A8%E3%83%83%E3%82%B8
    # 参考资料：https://8982.memo.wiki/d/%A5%B9%A5%BF%A5%F3%A5%A8%A5%C3%A5%B8%A1%AA%A1%AA%A1%AA
    # 参考视频：https://www.nicovideo.jp/watch/sm4831502 6分37秒
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0720.ogg"
    ai 心愛_制服_基本_笑顔 "好，来，Stand Edge！（L:スタンエッジ是「幕末志士達のくにおくん時代劇」游戏里面的一种需要相当高超技术的必杀技）"
    hide 心愛_制服_基本_ぶわー

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「でるわけねぇだろ！」
    voice "voice/想瑠/sol_a1_0138.ogg"
    liu 想瑠_スーツ_見下し "怎么可能做得到啊!"

    # nil 「俺は仰向けのま、真冬の後頭部に手をおいて、顔に近づけた。」
    "但是因为我们四个人正好都齐了，所以大家一起打了麻将"

    # scene06 场景2 【心爱酱晚来一步】 结束

    # scene06 结束

    # 过场：心爱（常服）

    # 隐藏 quick_menu
    $ quick_menu = False

    play sound "voice/effect/moosehead honk (stinger).ogg"
    image bg アイキャッチ心愛 = "images/bg/アイキャッチ心愛.png"
    play music bgmfifteen fadeout 4.0 fadein 4.0 # 针对这里BGM的特点需要把 Scene07 的BGM提前到 Scene06 脚本的尾巴这里写，并增大 fadeout/in 的间隔
    scene black
    scene アイキャッチ心愛 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)
 
    $ renpy.pause(1.5, hard=True)

    jump scene07
# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene12 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：
# 版本 NightBuild "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年5月1日

# 当前流程：All Done!

label scene12:
    # scene12 开始

    # scene12 场景1 【心爱和真冬的秘密时间！】 开始

    # 地点：真冬卧室
    # 人物：真冬 心爱
    # BGM：无

    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)
    scene 真冬部屋_夜_消灯 at love69_bg1440 with dissolve

    # 显示 quick_menu
    $ quick_menu = True

    # nil 「真冬です。」
    "我是真冬"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「えー…こほん」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1469.ogg"
    ai 心愛_制服_基本_真顔 "欸……咳咳"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「…まふ」
    show 真冬_制服_基本_まったり at love69_left with dissolve
    voice "voice/真冬/maf_a1_1156.ogg"
    dong 真冬_制服_基本_まったり "……嘛呼"

    # nil 「シャワーは浴びてきました。」
    "去洗过了澡"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「歯も磨きました」
    voice "voice/心愛/cca_a1_1470.ogg"
    ai 心愛_制服_基本_真顔 "牙齿也刷过了"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「歯磨き粉も使いました」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1157.ogg"
    dong 真冬_制服_基本_無表情 "而且还用了牙膏"
    hide 真冬_制服_基本_まったり

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「口臭対策もばっちりです」
    show 心愛_制服_基本_無表情 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1471.ogg"
    ai 心愛_制服_基本_無表情 "口臭对策也做的很好"
    hide 心愛_制服_基本_真顔

    # nil 「シャワーを浴びた流れで、お互い下着姿のまベッドの上で正座して向かい合います。」
    "在快速淋浴之后，穿着内衣在床上面对面坐着"

    # nil 「お兄ちゃんは部屋で爆睡していたので、今回は私の部屋です。」
    "欧尼酱还在屋里爆睡，所以这次是在我的房间"

    # nil 「どうしよう。お兄ちゃん含めた三人でなら、何回もエッチしてるのに。もしかしたら、お兄ちゃんと初めてした時よりも緊張してる…かも…。」
    "怎么办。如果是包括欧尼酱在内的三个人的话，明明已经H过好几次了。也许，比起和欧尼酱第一次的时候还紧张…"

    # nil 「勿論、例のアイスの効果もあるのでしょうけど、心臓とかがドキドキと高鳴って、ちょっと苦しいくらいです。」
    "当然，也有那个冰淇淋的效果在内，但是心脏一直dokidoki的，有点痛苦呢"

    # nil 「エアコンの設定温度は27度にしました。除湿モードで、静かな稼働音を立ています。」
    "空调的温度设定在27度。在除湿模式下，发出安静的运转声"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「えーっと…他にすべき事は…あっ、ティッシュは？」
    voice "voice/真冬/maf_a1_1158.ogg"
    dong 真冬_制服_基本_無表情 "呃…还有其他要做的事吗…啊，纸巾呢？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「プリンター用のウェットティッシュならあるよ」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1472.ogg"
    ai 心愛_制服_基本_嬉しい "有打印机用的纸哦"
    hide 心愛_制服_基本_無表情

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「それは多分使うと大変な事になっちゃうから…とってくるね」
    show 真冬_制服_基本_泣き at love69_left with dissolve
    voice "voice/真冬/maf_a1_1159.ogg"
    dong 真冬_制服_基本_泣き "那个大概用起来会很麻烦……我去拿来吧"
    hide 真冬_制服_基本_無表情

    # nil 「私は、ベッドから立ち上がろうとします。」
    "我试着从床上站起来"

    # nil 「きゅっ」
    "拽拽"

    # 真冬 「……？」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1160.ogg"
    dong 真冬_制服_基本_無表情 "……？"
    hide 真冬_制服_基本_泣き

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「んーん…」
    show 心愛_制服_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1473.ogg"
    ai 心愛_制服_基本_泣き "嗯~嗯……"
    hide 心愛_制服_基本_嬉しい

    # nil 「心愛ちゃんは、ベッドに正座したま私のパンツのリボンの部分を掴んできました。ノールックで。」
    # 参考资料：https://www.weblio.jp/content/%E3%83%8E%E3%83%BC%E3%83%AB%E3%83%83%E3%82%AF
    "心爱酱在床上坐直了身体，抓住我的胖次上的带子，no-look（L:指用于描述一个人不看一个物体，这里是引申义，无视了我）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「大丈夫だよ、すぐ戻ってくるから」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1161.ogg"
    dong 真冬_制服_基本_微笑み "没关系的哦，我马上就回来"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「うぅ～…」
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1474.ogg"
    ai 心愛_制服_基本_不機嫌 "呜~……"
    hide 心愛_制服_基本_泣き

    # nil 「私はぽんぽんと心愛ちゃんの頭に手を乗せます。」
    "我把手放在心爱酱的头上摸呼摸呼"

    # nil 「まるで、お預けを食らった子犬のように、しょんぼりと髪の毛をしならせる心愛ちゃん。」
    "简直就像是被寄养的小狗一样，无精打采地梳理着头发的心爱酱"

    # nil 「付き合う事になったその日こそ、無理矢理押し切られましたが、本来のこの子は、甘えん坊さん…というか、誘い受け体質な気がします。」
    "在交往的那一天，虽然被强行推开了，但我觉得这个孩子是个爱撒娇的孩子……或者说是诱惑型体质（L:谭谈交通，诱惑型233）"

    # nil 「母性本能をくすぐるというか…。」
    "母性本能被激发了呢…"

    # nil 「ぎゅー…。」
    "抱~……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ひとりぼっちやーだ」
    voice "voice/心愛/cca_a1_1475.ogg"
    ai 心愛_制服_基本_不機嫌 "一个人不要嘛~"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「…まふ」
    show 真冬_制服_基本_まったり at love69_left with dissolve
    voice "voice/真冬/maf_a1_1162.ogg"
    dong 真冬_制服_基本_まったり "……嘛呼"
    hide 真冬_制服_基本_微笑み

    # nil 「どうやら、ティッシュはとりにいかせてもらえないそうです。」
    "显然，纸巾是不能拿了"

    # nil 「そして、この瞬間、リードするのは私だという事が、暗黙の了解で決定した事を悟りました。」
    "在这一瞬间，我明白了我们两个人之间默认应该是我来攻"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ただいまふゆ」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1163.ogg"
    dong 真冬_制服_基本_微笑み "我回来啦（L:这里把句尾改成了真冬的Mafuyu）"
    hide 真冬_制服_基本_まったり

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「おかえりこあ！」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1476.ogg"
    ai 心愛_制服_基本_笑顔 "欢迎回来！（L:同样的梗，句尾换成了Cocoa）"
    hide 心愛_制服_基本_不機嫌

    # nil 「私は、事後、プリンター用のウェットティッシュで身体を拭くことを覚悟しました。」
    "我做好了事后用打印机用纸擦拭身体的觉悟"

    # nil 「私が諦めてベッドの上に正座し直すと、嬉しそうにぴょこぴょこと髪を跳ねさせて、笑顔をこちらに向けて来ます。」
    # "当我放弃，重新在床上正坐的时候，她的头发高兴地上下舞动，脸上露出了笑容"
    "当我决定放弃，重新在床上正坐的时候，看见她的发丝随着身体高兴地上下舞动，脸上也展露了笑容"

    # nil 「可愛い。」
    "真阔耐"

    # nil 「私の両腕が勝手に、心愛ちゃんの両肩に伸びます。」
    "我的双臂随意地伸向心爱酱的两肩"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ご…ごくり」
    # 参考资料：https://dictionary.goo.ne.jp/word/%E3%81%94%E3%81%8F%E3%82%8A/
    show 心愛_制服_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1477.ogg"
    ai 心愛_制服_基本_泣き "（咽…咽口水）"
    hide 心愛_制服_基本_笑顔

    # nil 「心愛ちゃんは緊張こそすれど、嫌がる素振りは見せず、身体を硬直させながら、私の両腕にその両肩を触れさせました。」
    # "心爱酱虽然很紧张，但并没有表现出讨厌的样子，身体僵硬着，我的双臂触碰到了她的双肩"
    # "心爱酱虽然很紧张，但并没有表现出讨厌的样子，身体僵硬着，直到我的双臂触碰到了她的双肩"
    "心爱酱虽然很紧张，但并没有表现出讨厌的样子，身体僵硬着，我将双手慢慢放在她的肩上"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「…はい」
    show 心愛_制服_基本_無表情 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1478.ogg"
    ai 心愛_制服_基本_無表情 "……好"
    hide 心愛_制服_基本_泣き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「…はい」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1164.ogg"
    dong 真冬_制服_基本_無表情 "……好"
    hide 真冬_制服_基本_微笑み

    # nil 「その姿勢のま数秒間硬直。」
    "保持这个姿势僵硬了几秒钟"

    # nil 「無言のまにらめっこ開始です。」
    "开始无言地盯着对方"

    # L:这里文本框被遮住了，显示人物是(nil)空，但是又显示的小对话框的头像，这里就由我来合理处理一下~

    # 心爱&真冬 「『…』」
    show 心愛_制服_基本_笑顔 at love69_right
    show 真冬_制服_基本_ジト目 at love69_left
    with dissolve
    ai_dong 真冬_制服_基本_ジト目 "『…』"
    hide 真冬_制服_基本_無表情
    hide 心愛_制服_基本_無表情

    # 心爱&真冬 「『…』」
    show 心愛_制服_基本_ペコちゃん at love69_right
    show 真冬_制服_基本_無表情 at love69_left
    with dissolve
    ai_dong 真冬_制服_基本_無表情 "『…』"
    hide 真冬_制服_基本_ジト目
    hide 心愛_制服_基本_笑顔

    # 心爱&真冬 「『……』」
    show 心愛_制服_基本_きらきら at love69_right
    show 真冬_制服_基本_まったり at love69_left
    with dissolve
    ai_dong "『……』"
    hide 真冬_制服_基本_無表情
    hide 心愛_制服_基本_ペコちゃん

    # 心爱&真冬 「『……』」
    show 心愛_制服_基本_ゴルゴ at love69_right
    show 真冬_制服_基本_ジト目 at love69_left
    with dissolve
    ai_dong "『……』"
    hide 真冬_制服_基本_まったり
    hide 心愛_制服_基本_きらきら

    # 真冬 「ぷっ」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1165.ogg"
    dong 真冬_制服_基本_微笑み "噗"
    hide 真冬_制服_基本_ジト目

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ウィーーーーーーーーン！」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1479.ogg"
    ai 心愛_制服_基本_真顔 "WIN——————！"
    hide 心愛_制服_基本_ゴルゴ

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「卑怯者－！！」
    show 真冬_制服_基本_嬉しい at love69_left with dissolve
    voice "voice/真冬/maf_a1_1166.ogg"
    dong 真冬_制服_基本_嬉しい "这是作弊~！！"
    hide 真冬_制服_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぶわー！」
    show 心愛_制服_基本_ぶわー at love69_right with dissolve
    voice "voice/心愛/cca_a1_1480.ogg"
    ai 心愛_制服_基本_ぶわー "咕啊——！"
    hide 心愛_制服_基本_真顔

    # nil 「ぼすっ」
    "哈哈"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「押し倒されまんた」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1481.ogg"
    ai 心愛_制服_基本_嬉しい "被推倒了"
    hide 心愛_制服_基本_ぶわー

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「押し倒しまんた」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1167.ogg"
    dong 真冬_制服_基本_微笑み "推倒你了"
    hide 真冬_制服_基本_嬉しい

    # nil 「こまでくるのに所要時間、凡そ分とちょっと。押し倒すのって、度胸がいるんだなと思いました。（女の子並の感想）」
    "走到这步大概需要一点时间。我觉得推倒她是需要勇气的（和女孩子一样的感想）"

    # nil 「あとでお兄ちゃんに報告しましょう。」
    "之后再向欧尼酱报告吧"

    # 真冬 「さてと…あっ」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1168.ogg"
    dong 真冬_制服_基本_無表情 "接下来……啊"
    hide 真冬_制服_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ちゅーっ」
    show 心愛_制服_基本_キス at love69_right with dissolve
    voice "voice/心愛/cca_a1_1482.ogg"
    ai 心愛_制服_基本_キス "啾——"
    hide 心愛_制服_基本_嬉しい

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「んっ…」
    show 真冬_制服_基本_キス at love69_left with dissolve
    voice "voice/真冬/maf_a1_1169.ogg"
    dong 真冬_制服_基本_キス "嗯…"
    hide 真冬_制服_基本_無表情

    # nil 「次はどうしようか。と考えていたら、心愛ちゃんが下から両腕を伸ばしてきて、私の唇を奪いました。」
    "接下来该怎么办呢？这样想着，心爱酱从下面伸出双臂，夺走了我的嘴唇"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「んぅ…ちゅぅ…」
    voice "voice/心愛/cca_a1_1483.ogg"
    ai 心愛_制服_基本_キス "嗯……啾……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「はぁ、ん…んぅ…ちゅっ」
    voice "voice/真冬/maf_a1_1170.ogg"
    dong 真冬_制服_基本_キス "哈、嗯…嗯…啾"

    # nil 「そのま間髪いれずに、軽めの連続キスへと移行します。」
    "然后从有间隔的转向轻一点的连续接吻"

    # nil 「心愛ちゃんがついばむように、私の唇にちゅっちゅっとキスを浴びせてくれます。」
    "心爱酱就像啄食一样，在我的嘴唇上亲了一下"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ん、ちゅぅ…ちゅっ…ちゅぅっ」
    voice "voice/心愛/cca_a1_1484.ogg"
    ai 心愛_制服_基本_キス "嗯……啾……啾……啾……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ちゅぅ、んぅ…ちゅぅっ…ちゅっ…」
    voice "voice/真冬/maf_a1_1171.ogg"
    dong 真冬_制服_基本_キス "啾……嗯……啾……啾……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぷあ…えへ…」
    voice "voice/心愛/cca_a1_1485.ogg"
    ai 心愛_制服_基本_キス "呜哈……欸嘿嘿……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「エッチしちゃう…ね、女の子同士なのに」
    show 真冬_制服_基本_嬉しい at love69_left with dissolve
    voice "voice/真冬/maf_a1_1172.ogg"
    dong 真冬_制服_基本_嬉しい "来H吧……呐，明明是女孩子"
    hide 真冬_制服_基本_キス

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「付き合ってるんだし、問題ない…んじゃない…？」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1486.ogg"
    ai 心愛_制服_基本_嬉しい "我们在交往，所以没问题…不是吗…？"
    hide 心愛_制服_基本_キス

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「でも…ほんと、改めて…二人でするってなると…凄く…。ねぇ、心愛ちゃんも、興奮してる…？」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1173.ogg"
    dong 真冬_制服_基本_微笑み "但是…真的，再一次……两个人一起做的话……真的很…呐，心爱酱也很兴奋吗…？"
    hide 真冬_制服_基本_嬉しい

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「わ…は、ぁっ…」
    show 心愛_制服_基本_キス at love69_right with dissolve
    voice "voice/心愛/cca_a1_1487.ogg"
    ai 心愛_制服_基本_キス "哇…啊…"
    hide 心愛_制服_基本_嬉しい

    # nil 「聞かなくてもわかる質問ではありましたが、私は心愛ちゃんの身体に覆い被さりながら、そっとブラごしに左胸の内側に触れます。」
    "虽然是不用问也能明白的问题，但我一边覆盖着心爱酱的身体，一边轻轻地通过胸罩触摸她的左胸内侧"

    # nil 「どきどきどきどき。」
    "dokidoki~ dokidoki~"

    # nil 「私と同じくらい…もしくは、私よりも高鳴った鼓動を手のひらに感じます。」
    "可以感受到和我差不多……甚至，比我更快的心跳"

    # nil 「そのま、おっぱいの形に沿うように、ふくらみをなで回します。」
    "然后，按照欧派的形状，来回抚摸"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「は、ぁっ…んっ、手、あっつぃ…」
    voice "voice/心愛/cca_a1_1488.ogg"
    ai 心愛_制服_基本_キス "哈，啊…嗯，手，好烫…"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「んー…？　きもちいー？」
    voice "voice/真冬/maf_a1_1174.ogg"
    dong 真冬_制服_基本_微笑み "嗯——……？舒服吗？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぁ、んっ…きもちいけどー…私だけ触られるのは不本意なのでー…えい」
    show 心愛_制服_基本_ニタァ at love69_right with dissolve
    voice "voice/心愛/cca_a1_1489.ogg"
    ai 心愛_制服_基本_ニタァ "啊，嗯……虽然很舒服啊……但是我不想让别人碰我，所以……嘿"
    hide 心愛_制服_基本_キス

    # nil 「心愛ちゃんが、ちょっと強引に私の胸をわしづかみにしました。」
    "心爱酱有点强硬地抓住了我的欧派"

    # nil 「ピリッとした刺激が、快感となって襲いかってきます。」
    "有点疼痛的刺激，变成快感袭来"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「はぁぅ…んっ…どうしよ…なんか、いつもより、きもちくて…集中できない」
    show 真冬_制服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_1175.ogg"
    dong 真冬_制服_基本_目閉じ "哈啊…嗯…怎么了……总觉得，比平时更兴奋…无法集中精神"
    hide 真冬_制服_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ね…二人で一緒に気持ち良くなれる方法ないかな…」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1490.ogg"
    ai 心愛_制服_基本_嬉しい "呐…没有两个人能一起舒服的方法吗…"
    hide 心愛_制服_基本_ニタァ

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「えっと…」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1176.ogg"
    dong 真冬_制服_基本_無表情 "那个……"
    hide 真冬_制服_基本_目閉じ

    # nil 「こんな時どうすればいか。」
    "这种时候该怎么办"

    # nil 「……」
    "……"

    # 真冬 「思い付いた」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1177.ogg"
    dong 真冬_制服_基本_微笑み "我想到了"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「お」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1491.ogg"
    ai 心愛_制服_基本_笑顔 "哦？"
    hide 心愛_制服_基本_嬉しい

    # nil 「思い付いた」
    "我想到了"

    # nil 「でも…。」
    "但是…"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「思い付いておきながら、口に出すのは結構恥ずかしいパターンの奴です」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1178.ogg"
    dong 真冬_制服_基本_無表情 "虽然想到了，但是那种想到了却不好意思说出来的呢"
    hide 真冬_制服_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「…えー！　何、そんなえっちぃの？」
    show 心愛_制服_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1492.ogg"
    ai 心愛_制服_基本_驚き "……欸——！是什么是什么？这么H的吗？"
    hide 心愛_制服_基本_笑顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「かなり…。というか、私達二人でするから余計に…それでも良い？」
    show 真冬_制服_基本_泣き at love69_left with dissolve
    voice "voice/真冬/maf_a1_1179.ogg"
    dong 真冬_制服_基本_泣き "相当……或者说，我们两个人一起做，所以更加……这样的可以吗？"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぅ…ぅん…どんどんエッチになっていく覚悟は割としてるから…」
    show 心愛_制服_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1493.ogg"
    ai 心愛_制服_基本_泣き "呃…嗯……我已经做好了不断变H的觉悟…"
    hide 心愛_制服_基本_驚き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「じゃぁ…とりあえず、ちゅーしよっか、心愛ちゃん」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1180.ogg"
    dong 真冬_制服_基本_微笑み "那么…总之，先啾——一下吧，心爱酱"
    hide 真冬_制服_基本_泣き

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「まふ」
    show 心愛_制服_基本_もぐもぐ at love69_right with dissolve
    voice "voice/心愛/cca_a1_1494.ogg"
    ai 心愛_制服_基本_もぐもぐ "嘛呼"
    hide 心愛_制服_基本_泣き

    # nil 「想像ただけでも、顔面ファイアーしそうですけど、もうこまできたらしょうがないので、スイッチ切り替えていくことにします。」
    "光是想象一下，我就觉得脸上冒火，但是事情已经到了这个地步就没办法了，所以我决定切换开关"

    # nil 「お互いの身体を深く抱きしめあいながら、唇を重ね合います。」
    "互相深深地拥抱彼此的身体，嘴唇重叠在一起"

    image bg ycg_2_2_1_1 = "images/bg/ycg_2_2_1_1.png"
    scene ycg_2_2_1_1 with dissolve
    play music bgmeight fadein 2.0

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ん、ちゅ…ぁ…はぁ…ぁっ…んっ…れるぅ…」
    voice "voice/心愛/cca_a1_1495.ogg"
    ai 心愛_下着_基本_キス "嗯，啾……啊…啊…啊…嗯……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「は、んぅう…ちゅぅ…ちゅ、ぷっ…れる…んぅ」
    voice "voice/真冬/maf_a1_1181.ogg"
    dong 真冬_下着_基本_キス "哈、嗯……啾……啾……嗯……啊"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ん、ちゅ…ぁ…はぁ…ぁっ…んっ…れるぅ…」
    voice "voice/心愛/cca_a1_1496.ogg"
    ai 心愛_下着_基本_キス "啾，嗯……啊…啾……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ちゅ、んぅ…ぷはっ…心愛ちゃん…すき…」
    voice "voice/真冬/maf_a1_1182.ogg"
    dong 真冬_下着_基本_キス "啾……嗯……哈嗯……心爱酱……喜欢……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「わたしもすき…ちゅぅうっ」
    voice "voice/心愛/cca_a1_1497.ogg"
    ai 心愛_下着_基本_キス "我也是……喜欢…啾"

    # nil 「お兄ちゃんに好きと言われるのも心愛ちゃんに好きと言われるのも、同じぐらい胸が温かくなります。」
    "被欧尼酱说喜欢也好，被心爱酱说喜欢也好，内心都会变得温暖"

    image bg = "images/bg/ycg_1_2_2.png"
    scene ycg_1_2_2 with dissolve

    # 心爱 「は、ぁ…んっ…ん…しょ…」
    voice "voice/心愛/cca_a1_1498.ogg"
    ai 心愛_下着_基本_キス "哈，啊…嗯…嗯…来吧…"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ん…ぁっ…ふ…」
    voice "voice/真冬/maf_a1_1183.ogg"
    dong 真冬_下着_基本_キス "嗯…啊…嗯……"

    # nil 「キスをしながら、ブラのホックに手をかけると、心愛ちゃんも、同じように私の下着を脱がしてくれます。」
    "一边接吻，一边把手放在胸罩的挂钩上，心爱酱也同样脱下我的内衣"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はぁ…はぁ…ちゅぅ…」
    voice "voice/心愛/cca_a1_1499.ogg"
    ai 心愛_下着_基本_キス "哈…哈…啾……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ん…ぅ、ちゅぅ…」
    voice "voice/真冬/maf_a1_1184.ogg"
    dong 真冬_下着_基本_キス "嗯……啾……"

    # nil 「次はショーツの中に手を滑り込ませます。」
    "接下来把手滑进胖次里"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「んちゅっ、ちゅぅ、れるぅ…んむっ…ちゅっ」
    voice "voice/心愛/cca_a1_1500.ogg"
    ai 心愛_下着_基本_キス "嗯啾，啾，嗯，嗯…嗯…"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ちゅぅ…んっ、ぅ…ちゅぅっ…れりゅぅ…」
    voice "voice/真冬/maf_a1_1185.ogg"
    dong 真冬_下着_基本_キス "啾……嗯…啾…嗯…啾……"

    # 心爱&真冬 「『ぷは…』」
    voice "voice/真冬/maf_a1_1186.ogg"
    ai_dong 真冬_下着_基本_キス "『呼哈……』"

    # L:因为是LOVE69所以这里的HScene稍微翻了一点

    # 但是，就此打住！露点娇喘哒咩！

    # HScene 开始了一点但没有完全开始，Skip~
    # maf 1187-1269
    # cca 1501-1583

    # 心爱&真冬 HScene 02（百合） Skip~
    image bg 庸医锤佬指非官 = "images/extra/luckykeeper/庸医锤佬指非官.png"
    if persistent.hsceneG:
        $ quick_menu = False # 隐藏 quick_menu
        window hide
        scene 庸医锤佬指非官 at truecenter with dissolve
        pause 3.0

    else:
        pass

    # scene12 场景1 【心爱和真冬的秘密时间！】 结束

    # Scene12 结束！

    # 过场：心爱（常服），没有BGM，会加一个的

    $ quick_menu = False

    play sound "voice/effect/moosehead honk (stinger).ogg"
    play music bgmthirtyeight fadeout 4.0 fadein 2.0
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)
    scene アイキャッチ心愛 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)

    $ renpy.pause(1.5, hard=True)
    $ renpy.end_replay()

    jump scene13

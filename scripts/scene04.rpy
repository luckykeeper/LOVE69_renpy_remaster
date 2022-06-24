# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene04 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：
# 版本 NightBuild "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年6月24日

# 当前流程：All Done!

label scene04:
    # scene04 开始
    # 地点：Q版
    # 人物：心爱 真冬
    # BGM：bgm28

    image bg sdcg01a = "images/bg/sdcg01a.png"
    scene sdcg01a  at love69_bg1440 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)

    # 显示 quick_menu
    $ quick_menu = True

    # scene04 场景1 【集美间的愉快自习（雾）】 开始
    # 可变标题
    # Scene 序号
    $ sceneNo =  " scene04"
    # 存档名称和 Scene 大标题
    $ sceneName = " 真冬&心爱线 真冬酱的心意"
    # 小场景的名称
    $ partName = " 【集美间的愉快自习（雾）】"
    $ changeTitleName()

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まふまふまふまふまふまふ」
    # 182-183 跳过
    voice "voice/真冬/maf_a1_0184.ogg"
    dong 真冬_制服_基本_まったり "嘛呼嘛呼嘛呼嘛呼嘛呼嘛~"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「まふまふまふまふまふまふ」
    # 668 左右应该是二周目内容，可能是Scene18的内容
    voice "voice/心愛/cca_a1_0668.ogg"
    ai 心愛_制服_基本_もぐもぐ "嘛呼嘛呼嘛呼嘛呼嘛呼嘛~"

    # nil 「こんにちは、真冬です。」
    "你好，我是真冬~"

    # nil 「世間はそろそろ真夏に突入する頃合いですが、私は相変わらず真冬です。」
    # "世间已经差不多是进入盛夏的时候了，而我还是一如既往的真冬（L:真冬也有寒冬、隆冬的意思。另外，2021年的冬天是真的冷，11月初就下雪了）"
    if persistent.luckykeeperSay == "shutup":
        "世间已经差不多是进入盛夏的时候了，而我还是一如既往的真冬"
    elif persistent.luckykeeperSay == "meme":
        "世间已经差不多是进入盛夏的时候了，而我还是一如既往的真冬（L:真冬也有寒冬、隆冬的意思。）"
    else:
        "世间已经差不多是进入盛夏的时候了，而我还是一如既往的真冬（L:真冬也有寒冬、隆冬的意思。另外，2021年的冬天是真的冷，11月初就下雪了）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まふまふまふまふまふ」
    voice "voice/真冬/maf_a1_0185.ogg"
    dong 真冬_制服_基本_まったり "嘛呼嘛呼嘛呼嘛呼嘛~"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「まふまふまふまふまふ」
    voice "voice/心愛/cca_a1_0669.ogg"
    ai 心愛_制服_基本_もぐもぐ "嘛呼嘛呼嘛呼嘛呼嘛~"

    # nil 「今は学園で授業の真っ最中。といっても、自習なので暇です。」
    "现在正在学校上课。虽说如此，因为是自习所以很闲"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まふ」
    voice "voice/真冬/maf_a1_0186.ogg"
    dong 真冬_制服_基本_まったり "嘛呼~"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    image bg sdcg01b = "images/bg/sdcg01b.png"
    scene sdcg01b with dissolve

    # 心爱 「びよーん」
    voice "voice/心愛/cca_a1_0670.ogg"
    ai 心愛_制服_基本_もぐもぐ "呀~"

    # nil 「しかもあろうことか、半日授業のうち、最初の時間はＨＲ。残りの時間自習というとんでもないスケジュールです。」
    "而且，在半天的课程中，最开始是HR（班会）。剩下的时间全是自习，真是荒唐的课程安排"

    # nil 「仕方がないので、幼馴染みの心愛ちゃんのほっぺたをぷにぷにしつづけています。およそ1時間。」
    "因为太无聊了，所以只好把青梅竹马的心爱酱的脸蛋吹得鼓鼓的，大概过去了1个小时"

    # nil 「最初は心愛ちゃんも困惑していましたが、気持ち良くなってきたんでしょう。」
    "一开始心爱酱感觉很迷，但是现在心情好多了吧"

    # nil 「嫌がる素振りどころか、やめようとすると、もっとして欲しいと求めて来るようになりました。」
    "一点讨厌的样子都没有，而且当我想停下来的时候，心爱一副“还想要”的样子"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まふ」
    voice "voice/真冬/maf_a1_0187.ogg"
    dong 真冬_制服_基本_まったり "嘛呼"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ふにゃー」
    voice "voice/心愛/cca_a1_0671.ogg"
    ai 心愛_制服_基本_もぐもぐ "呼喵~"

    # nil 「ちなみに、双子の兄は隣の席が何故か空白の、後ろの席で心地よさそうに寝息を立ています。」
    "顺便一提，双胞胎哥哥的旁边不知为何空着一个位子，于是在后面的座位上舒服地躺着睡着了"

    # nil 「悪戯してやりたい所ですが、今は心愛ちゃんのほっぺたをぷにぷにするのが忙しいので、我慢します。」
    "虽然很想恶作剧，但是现在忙着要把心爱酱的脸蛋吹得鼓鼓的，所以就忍耐一下吧"

    # nil 「さて、この兄ですが、最近変です。私が起こさずとも、早起きしていやがるのです。」
    "对了，就是这个欧尼酱，他最近怪怪的。早上不用我叫醒，自己就早起了"

    # nil 「これでは、毎朝どうやって起こしてやろうかと悩む、毎朝の脳トレができません。」
    "这样的话，我每天早上就没法脑力锻炼了，因为不需要烦恼怎么把欧尼酱叫起来了"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ういいいいいいいん」
    voice "voice/真冬/maf_a1_0188.ogg"
    dong 真冬_制服_基本_まったり "呜诶诶诶诶诶诶——"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「むああああああ」
    voice "voice/心愛/cca_a1_0672.ogg"
    ai 心愛_制服_基本_真顔 "呜呜呜呜呜呜——"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ぺち」
    voice "voice/真冬/maf_a1_0189.ogg"
    dong 真冬_制服_基本_まったり "啪唧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ＰＯＷ！」
    # 673没有声音，需要注意一下用在哪儿了，原来是上面少了一句
    voice "voice/心愛/cca_a1_0673.ogg"
    ai 心愛_制服_基本_驚き "ＰＯＷ！"

    # nil 「今度、この心愛ちゃんをけしかけてみようかと思います。」
    "回头，我想要试着调教一下心爱酱呢"

    #场景切换
    # 地点：Q版->教室
    # 人物：心爱 真冬 莲 想瑠喵
    # BGM：bgm28

    scene 教室_昼 at love69_bg1220 with dissolve

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ぺち」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0190.ogg"
    dong 真冬_制服_基本_無表情 "呼姆"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「まふ…あれ？　やめちゃうの？　うぅ…」
    show 心愛_制服_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0674.ogg"
    ai 心愛_制服_基本_泣き "嘛呼…啊咧？不做了嘛？呜…"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「欲しがりさんですね」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0191.ogg"
    dong 真冬_制服_基本_微笑み "你很想要啊"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「だってー気持ちいんだもんー、まふまふ♪」
    # 675
    show 心愛_制服_基本_嬉しい1 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0675.ogg"
    ai 心愛_制服_基本_嬉しい1 "因为——很舒服的啦、嘛呼嘛呼♪"
    hide 心愛_制服_基本_泣き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「お兄ちゃんに、悪戯をしようかなーなんて思ってみたり」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0192.ogg"
    dong 真冬_制服_基本_無表情 "我在想,要不要对欧尼酱恶作剧呢"
    hide 真冬_制服_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あ！　それ私も考えてた！」
    show 心愛_制服_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0676.ogg"
    ai 心愛_制服_基本_驚き "啊! 这个我也想到了!"
    hide 心愛_制服_基本_嬉しい1

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ポリバルーンのストローを鼻に突っ込んだりしてみる？」
    show 真冬_制服_基本_ニタァ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0193.ogg"
    # dong 真冬_制服_基本_ニタァ "要不要也来做个鼻灯笼呢？（L:绝了，所以每个人体验一次呗）"
    if persistent.luckykeeperSay == "full":
        dong 真冬_制服_基本_ニタァ "要不要也来做个鼻灯笼呢？（L:绝了，所以每个人体验一次呗）"
    else:
        dong 真冬_制服_基本_ニタァ "要不要也来做个鼻灯笼呢？"

    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「もうそのネタは使い古されてるかな…私も、真冬ちゃんの知らない所でやられてるんだぜ…」
    show 心愛_制服_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0677.ogg"
    ai 心愛_制服_基本_泣き "这个段子已经过时了吧…我也在真冬不知道的地方被人这么淦了……"
    hide 心愛_制服_基本_驚き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「…コンテンツの消費速度には驚かされますね…えいえい」
    show 真冬_制服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0194.ogg"
    dong 真冬_制服_基本_目閉じ "…内容的消费速度真让人吃惊啊…嘿嘿"
    hide 真冬_制服_基本_ニタァ

    # nil 「ぷにぷに。兄のほっぺをつんつんしてみます。自分の兄ながら、可愛い寝顔です。」
    "噗噗，我要戳戳欧尼酱的脸颊。虽然是自己的哥哥，但是睡脸实在是太可爱了"

    # 莲 「……」
    lian "……"

    # 真冬 「…あれ？」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0195.ogg"
    dong 真冬_制服_基本_無表情 "啊嘞？"
    hide 真冬_制服_基本_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「どしたの？」
    show 心愛_制服_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0678.ogg"
    ai 心愛_制服_基本_驚き "怎么了呢？"
    hide 心愛_制服_基本_泣き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まふ」
    show 真冬_制服_基本_まったり at love69_left with dissolve
    voice "voice/真冬/maf_a1_0196.ogg"
    dong 真冬_制服_基本_まったり "嘛呼~"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はう」
    show 心愛_制服_基本_まふまふ at love69_right with dissolve
    voice "voice/心愛/cca_a1_0679.ogg"
    ai 心愛_制服_基本_まふまふ "哈呜~"
    hide 心愛_制服_基本_驚き

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ふにゃー」
    play sound "voice/effect/09_物陰から顔を出す.ogg"
    voice "voice/心愛/cca_a1_0680.ogg"
    ai 心愛_制服_基本_まふまふ "呼喵~"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ふむ…」
    show 真冬_制服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0197.ogg"
    dong 真冬_制服_基本_目閉じ "哈呜"
    hide 真冬_制服_基本_まったり

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「む…なんだよぅ、焦らしプレイかよぅ…もっとくれよぅ」
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0681.ogg"
    ai 心愛_制服_基本_不機嫌 "嗯…这是啥啊，是那种放置play嘛？…再给我一点吧"
    hide 心愛_制服_基本_まふまふ

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「いや…」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0198.ogg"
    dong 真冬_制服_基本_無表情 "呀…"
    hide 真冬_制服_基本_目閉じ

    # nil 「二人とも、妙に肌のハリが良いような…。」
    "两个人的皮肤都特别有弹性呢..."

    # 真冬 「心愛ちゃん、お兄ちゃんに、お気に入りのヒアルロン酸の化粧水でも貸した？」
    voice "voice/真冬/maf_a1_0199.ogg"
    dong 真冬_制服_基本_無表情 "心爱酱，你借给欧尼酱你最喜欢的玻尿酸化妆水了吗?"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「へ？　いきなりどうしたの？」
    show 心愛_制服_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0682.ogg"
    ai 心愛_制服_基本_驚き "咦？突然怎么了？"
    hide 心愛_制服_基本_不機嫌

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「二人とも妙に肌のツヤがいからさ。化粧水を炭酸で割って飲む心愛ちゃんならまだしも、お兄ちゃんなんてプロアクティブが関の山だし…」
    voice "voice/真冬/maf_a1_0200.ogg"
    # dong 真冬_制服_基本_無表情 "两个人的肌肤都有着奇妙的光泽。如果是用碳酸来兑化妆水喝的心爱倒还说得过去，欧尼酱这么积极主动的话好像就说不大过去了呢…"
    dong 真冬_制服_基本_無表情 "两个人的肌肤都有着奇妙的光泽。如果是用碳酸来兑化妆水喝的心爱酱倒还说得过去，欧尼酱这么圆润的话好像就说不大过去了呢…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ふ、ふえ！？　あ、あー…えと、えと…ね…」
    show 心愛_制服_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0683.ogg"
    ai 心愛_制服_基本_泣き "呜、呜欸! ? 啊，啊...... 呃...那、那个...啊..."
    hide 心愛_制服_基本_驚き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「……」
    voice "voice/真冬/maf_a1_0201.ogg"
    dong 真冬_制服_基本_無表情 "……"

    # nil 「心愛ちゃんが妙に狼狽えています。案の定、何か裏がありそうですね。」
    "心爱酱莫名其妙地惊慌失措，果然有什么内幕"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「えーと…真冬ちゃんには黙ってごめんなさいなんだけど…」
    voice "voice/心愛/cca_a1_0684.ogg"
    ai 心愛_制服_基本_泣き "那个……对不起我没告诉真冬……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「え？　いや、お兄ちゃんが女子力足りないのは知ってるから、そういうお手伝いは大歓迎だけど…」
    voice "voice/真冬/maf_a1_0202.ogg"
    dong 真冬_制服_基本_無表情 "欸？哦呀，我知道欧尼酱的女子力不够，你来帮忙我倒是大欢迎啦……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「これを…」
    voice "voice/心愛/cca_a1_0685.ogg"
    ai 心愛_制服_基本_泣き "这个……"

    # nil 「心愛ちゃんは、目線を泳がせながら、手のひらに置いた何かを見せてきました。」
    "心爱酱一边游移着视线，一边向我们展示了放在手掌上的东西"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「コラーゲンボール…」
    voice "voice/真冬/maf_a1_0203.ogg"
    dong 真冬_制服_基本_無表情 "胶原蛋白球…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「う、うん…。なんか、一個あげたら味をしめちゃったみたいで…」
    voice "voice/心愛/cca_a1_0686.ogg"
    ai 心愛_制服_基本_泣き "嗯、嗯…好像给了一个就尝到了甜头的样子……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「味無いと思うんだけど…」
    show 真冬_制服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0204.ogg"
    dong 真冬_制服_基本_目閉じ "我觉得这东西没有味道来着…"
    hide 真冬_制服_基本_無表情

    # nil 「また、兄が変な食べ物にハマってしまったようです。今度、「煮こごり」という美味しい食べ物を紹介してあげようと思います。」
    # 参考资料：https://ja.wikipedia.org/wiki/%E7%85%AE%E3%81%93%E3%81%94%E3%82%8A
    # "另外，哥哥好像也迷上了奇怪的食物。下次，我想给你介绍一种叫做「煮こごり」（L:指肉冻或者鱼冻，雀实非常好吃）的好吃的食物"
    # "另外，哥哥好像也迷上了奇怪的食物。下次，我想给你介绍一种叫做「煮こごり」（L:指肉冻或者鱼冻，雀食非常好吃）的好吃的食物"
    if persistent.luckykeeperSay == "shutup":
        "另外，哥哥好像也迷上了奇怪的食物。下次，我想给你介绍一种叫做「煮こごり」的好吃的食物"
    else:
        "另外，哥哥好像也迷上了奇怪的食物。下次，我想给你介绍一种叫做「煮こごり」（L:指肉冻或者鱼冻，雀食非常好吃）的好吃的食物"

    # 真冬 「まふまふまふ」
    show 真冬_制服_基本_まったり at love69_left with dissolve
    voice "voice/真冬/maf_a1_0205.ogg"
    dong 真冬_制服_基本_まったり "嘛呼嘛呼嘛~"
    hide 真冬_制服_基本_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「まふまふまふ」
    show 心愛_制服_基本_まふまふ at love69_right with dissolve
    voice "voice/心愛/cca_a1_0687.ogg"
    ai 心愛_制服_基本_まふまふ "嘛呼嘛呼嘛呼~"
    hide 心愛_制服_基本_泣き

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「で、いつ真冬ちゃんは心愛ちゃんを貸してくれるの？」
    # 76-94 跳过
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0095.ogg"
    liu 想瑠_スーツ_見下し "那么，什么真冬酱时候才会把心爱酱借给我呢？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「後で」
    show 真冬_制服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0206.ogg"
    dong 真冬_制服_基本_目閉じ "一会儿"
    hide 真冬_制服_基本_まったり

    # 莲 「ていうか働けよあんたは」
    lian "话说回来，你该上工了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「起きてたのか！」
    show 心愛_制服_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_0688.ogg"
    ai 心愛_制服_基本_驚き "睡醒了吗！"
    hide 心愛_制服_基本_まふまふ

    # 莲 「今起きた。そして寝る。あと真冬、ちゃんと先生にも心愛を貸してあげなさい」
    lian "我现在起来了，然后一会儿接着睡觉。还有真冬，要好好地把心爱借给老师哦"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「はーい。はい、どーぞ」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0207.ogg"
    dong 真冬_制服_基本_微笑み "好——的。来，请用"
    hide 真冬_制服_基本_目閉じ

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「わーい。まふまふまふ」
    show 想瑠_スーツ_ニヤリ at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0096.ogg"
    liu 想瑠_スーツ_ニヤリ "好嘞~嘛呼嘛呼嘛呼~"
    hide 想瑠_スーツ_見下し

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「脇をしめろ脇を！」
    # 参考资料：https://www.shige9.net/2019/07/31/%E9%87%8E%E7%90%83%E3%81%AE%E5%B8%B8%E8%AD%98-%E8%84%87%E3%82%92%E7%B7%A0%E3%82%81%E3%82%8D-%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6%E8%80%83%E3%81%88%E3%82%8B/
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_0689.ogg"
    # ai 心愛_制服_基本_真顔 "收紧腋窝啊、收紧！（L:棒球技巧，方便肘部和肩胛骨发力）"
    if persistent.luckykeeperSay == "shutup":
        ai 心愛_制服_基本_真顔 "收紧腋窝啊、收紧！"
    else:
        ai 心愛_制服_基本_真顔 "收紧腋窝啊、收紧！（L:棒球技巧，方便肘部和肩胛骨发力）"

    hide 心愛_制服_基本_驚き

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「押忍！」
    show 想瑠_スーツ_本気 at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0097.ogg"
    # liu 想瑠_スーツ_本気 "押忍！（L:是空手道、剑道、柔道等武术界人士之间使用的一种打招呼方式）"
    if persistent.luckykeeperSay == "shutup":
        liu 想瑠_スーツ_本気 "押忍！"
    else:
        liu 想瑠_スーツ_本気 "押忍！（L:是空手道、剑道、柔道等武术界人士之间使用的一种打招呼方式）"

    hide 想瑠_スーツ_ニヤリ

    # nil 「真冬です。」
    "现在是真冬视角"

    # nil 「兄の寝顔を眺めながらそっと、思います。」
    "一边看着哥哥的睡颜，一边思考着"

    # nil 「もっと、仲良くなればいのにな。」
    "我希望我们能更亲密一点"

    # nil 「そっと、兄の頭を撫でました。」
    "轻轻地抚摸了欧尼酱的头"

    # nil 「兄の寝顔が和らぎます。」
    "欧尼酱的睡脸平静了下来"

    # nil 「それを見て、胸の中に愛おしさがこみ上げます。」
    "看到那个，心中充满了爱意"

    # nil 「真冬です。」
    "我是真冬"

    # nil 「お兄ちゃんが大好きです。」
    "我最喜欢欧尼酱了"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 教室_昼 at love69_bg1220 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「起きまんた」
    lian "我起来了"

    # nil 「案の定、教室には誰もいませんでした。」
    "果然，教室里没有人"

    # nil 「額には、書き置きされた付箋が何枚か貼ってありました。」
    "额头上贴着几张写着东西的便签"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # nil 『＠mafumafu_winter　温泉掘ってきます。今日は早く帰ります』
    # 真冬Twitter：https://twitter.com/mafumafu_winter
    # "『@mafumafu_winter（L:这个是真冬，在Twitter能搜到【Mafumafu.K@Love69】） 我去挖温泉去啦，今天会早点回去的』"
    if persistent.luckykeeperSay == "shutup":
        "『@mafumafu_winter 我去挖温泉去啦，今天会早点回去的』"
    else:
        "『@mafumafu_winter（L:这个是真冬，在Twitter能搜到【Mafumafu.K@Love69】） 我去挖温泉去啦，今天会早点回去的』"

    # nil 『＠Cocoa_sweetcake　欲望が堪えきれないので、私も穴を掘ってきます』
    # 心爱Twitter：https://twitter.com/Cocoa_sweetcake
    # "『@Cocoa_sweetcake（L:这个是心爱，在Twitter能搜到【null】，但是里面没东西） 因为无法抑制欲望，所以我也去挖洞啦』"
    if persistent.luckykeeperSay == "shutup":
        "『@Cocoa_sweetcake 因为无法抑制欲望，所以我也去挖洞啦』"
    else:
        "『@Cocoa_sweetcake（L:这个是心爱，在Twitter能搜到【null】，但是里面没东西） 因为无法抑制欲望，所以我也去挖洞啦』"

    # nil 『＠solnyan_bot お尻を出した子一等賞。私は常に桜花賞』
    # 想瑠喵Twitter：https://twitter.com/Solnyan_bot
    # 参考资料：https://dic.pixiv.net/a/%E3%81%8A%E3%81%97%E3%82%8A%E3%81%A7%E5%87%BA%E3%81%97%E3%81%9F%E5%AD%90%E4%B8%80%E7%AD%89%E8%B3%9E
    # 参考资料：https://huaca.blog.fc2.com/blog-entry-1091.html
    # "『@solnyan_bot（L:这个是想瑠喵，在Twitter能搜到【想瑠にゃん_bot】） 露出屁股的孩子得一等奖，我经常得樱花奖（L:后半部分应该是编的，前半部分的来历有多种说法，一说是这句话出自『まんが日本昔ばなし』的ED曲『にんげんっていいな』，有暗示同性恋的意思）"
    if persistent.luckykeeperSay == "shutup":
        "『@solnyan_bot 露出屁股的孩子得一等奖，我经常得樱花奖"
    else:
        "『@solnyan_bot（L:这个是想瑠喵，在Twitter能搜到【想瑠にゃん_bot】） 露出屁股的孩子得一等奖，我经常得樱花奖（L:后半部分应该是编的，前半部分的来历有多种说法，一说是这句话出自『まんが日本昔ばなし』的ED曲『にんげんっていいな』，有暗示同性恋的意思）"
        luckykeeper "一说是“捉迷藏露出屁股的孩子得一等奖”,躲起来的孩子们不知道有熊，只注意着鬼的动向（露出脸看外面），完全没有注意到后方的熊，因为熊是杂食动物，所以一被发现就会被熊咬屁股，因为歌词整体是从熊的视角来叙述的，所以【一等奖】=【第一个猎物】的意思"

    # luckykeeper "一说是“捉迷藏露出屁股的孩子得一等奖”,躲起来的孩子们不知道有熊，只注意着鬼的动向（露出脸看外面），完全没有注意到后方的熊，因为熊是杂食动物，所以一被发现就会被熊咬屁股，因为歌词整体是从熊的视角来叙述的，所以【一等奖】=【第一个猎物】的意思"

    # nil 『＠Ashley_SW　アメリカと日本の音楽シーンの大きな違いは、ダウンロード販売の収益が、アーティストに還元されるか否かであるかだと私は考えている。
    # 亚十礼Twitter：https://twitter.com/ashley_sw
    # "『@Ashley_SW（L:这个是亚十礼，在Twitter能搜到【Ashley Ting】，我认为美国与日本音乐的主要区别在于数字发行的收益是否会回馈给艺术家』"
    if persistent.luckykeeperSay == "shutup":
        "『@Ashley_SW，我认为美国与日本音乐的主要区别在于数字发行的收益是否会回馈给艺术家』"
    else:
        "『@Ashley_SW（L:这个是亚十礼，在Twitter能搜到【Ashley Ting】），我认为美国与日本音乐的主要区别在于数字发行的收益是否会回馈给艺术家』"

    # nil 「余談だが、私はカーリー・レイ・ジェプセンは普通に可愛いと思う』」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%AB%E3%83%BC%E3%83%AA%E3%83%BC%E3%83%BB%E3%83%AC%E3%82%A4%E3%83%BB%E3%82%B8%E3%82%A7%E3%83%97%E3%82%BB%E3%83%B3
    # "说句题外话，我觉得卡莉·蕾·杰普森是普通的可爱呢（L:1985年11月21日－，加拿大歌手、词曲作家、演员，获得了包括朱诺奖、公告牌音乐奖与在内的多个奖项与提名，截至2015年3月，杰普森在全球唱片销量超过2000万）"
    # "说句题外话，我觉得卡莉·蕾·杰普森是非常的可爱呢（L:1985年11月21日－，加拿大歌手、词曲作家、演员，获得了包括朱诺奖、公告牌音乐奖与在内的多个奖项与提名，截至2015年3月，杰普森在全球唱片销量超过2000万）"
    if persistent.luckykeeperSay == "shutup":
        "说句题外话，我觉得卡莉·蕾·杰普森是非常的可爱呢"
    else:
        "说句题外话，我觉得卡莉·蕾·杰普森是非常的可爱呢（L:1985年11月21日－，加拿大歌手、词曲作家、演员，获得了包括朱诺奖、公告牌音乐奖与在内的多个奖项与提名，截至2015年3月，杰普森在全球唱片销量超过2000万）"

    # 莲 「（俺の額をツイッターかなにかと勘違いしてるんじゃないのか？）」
    lian "(绝了，这帮家伙是不是把我的额头当成推特了？)"

    # nil 「一人誰だかわからない人のもはっつけてあったが…。」
    "还有一个不知道是谁的人的贴纸..."

    # nil 「周りには、俺を起こそうと努力した痕跡が残されていた。」
    "周围还留有努力叫我起床的痕迹"

    # 莲 「（この名状しがたいバールのような物は一体…）」
    # 参考资料：https://dic.pixiv.net/a/%E5%90%8D%E7%8A%B6%E3%81%97%E3%81%8C%E3%81%9F%E3%81%84%E3%83%90%E3%83%BC%E3%83%AB%E3%81%AE%E3%82%88%E3%81%86%E3%81%AA%E3%82%82%E3%81%AE
    # 参考资料：https://acg.gamer.com.tw/acgDetail.php?s=52250
    # lian "（这个难以名状的棒状物体到底是…）（L:这个“难以名状的棒状物体”是「潜行吧！奈亚子」里面奈亚子的武器，就叫难以名状的棒状物体，形似物理学圣剑）"
    if persistent.luckykeeperSay == "shutup":
        lian "（这个难以名状的棒状物体到底是…）"
    else:
        lian "（这个难以名状的棒状物体到底是…）（L:这个“难以名状的棒状物体”是「潜行吧！奈亚子」里面奈亚子的武器，就叫难以名状的棒状物体，形似物理学圣剑）"

    # 莲 「ともあれ、真冬の奴も早く帰ってくるなら…」
    lian "不管怎样，如果真冬这家伙今天早点回来的话..."

    # nil 「俺は額から剥がした付箋を口の中に放り込んで、鞄を持って席を立つ。」
    "我把从额头剥下来的便签放进嘴里，拿着包离开座位"

    # nil 「授業が終了して凡そ一時間ぐらいか。思ったより時間も経ってない。心愛から貰いまくったコラーゲンボールのおかげで腹もそこまで減ってないし…。」
    "现在距离下课大概有一个小时左右吧，没我想象的那么久。多亏了心爱给我的那些胶原蛋白球，肚子倒也没那么饿..."

    # 莲 「帰るか」
    lian "要回去吗？"

    # nil 「帰ります。」
    "回去吧"

    # scene04 场景1 【集美间的愉快自习（雾）】 结束
    # scene04 场景2 【和里昂的再次相遇】 开始
    # 小场景的名称
    $ partName = " 【和里昂的再次相遇】"
    $ changeTitleName()

    # 场景切换
    # 地点：教室->校门口
    # 人物：莲
    # BGM不变

    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 校門_昼 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「暑いな…」
    lian "好热啊…"

    # nil 「時代は進んだもので、今じゃどこの学校も冷暖房完備が常識だ。俺が義務教育の頃は、図書室とパソコン室と職員室にしか無かったものだが。」
    "时代在进步呢，现在无论哪个学校都有完善的冷暖气设备。我在义务教育阶段的时候，只有图书室、电脑室和职员室才有这些设备"

    # nil 「一歩外にでると、真夏めいた日差しが照りつける。」
    "走出去一步，盛夏般的阳光就照射了下来"

    # nil 「校門をくぐって、家路を向かう。」
    "穿过校门，走向回家的路"

    # 场景切换
    # 地点：校门口->街道
    # 人物：莲 里昂 MJ
    # BGM不变

    image bg 通学路d_昼 = "images/bg/通学路d_昼/png"
    scene 通学路d_昼 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 不大想定义？？？了，用前面的“少女”吧
    # 里昂 「アイスー！　アイスはいりませんかぁー！」
    # 73-203 跳过
    # 本来应该是从204开始的，可是204-207文件直接就不存在……
    # 208-416 跳过
    voice "voice/リオン/ron_a1_0417a.ogg"
    ang 黄_基本_杖_微笑み "冰淇淋！ 要来点冰淇淋吗"

    # nil 「少し離れた場所で、アイスを売る屋台の声が聞こえる。」
    "在稍微远一点的地方，传来冰淇淋小摊叫卖的声音"

    # nil 「その声を聞いて、俺と似たような帰宅勢が振り向いて、一部は脚を向けている。」
    "听到这个声音，和我相似的回家的人不禁回头看去，一部分人转身向那边走去"

    # 莲 「そりゃーアイスも欲しくなる季節だわな」
    lian "这是个大家都想恰冰淇淋的季节啊"

    # nil 「アイスで思い出すのは勿論、例の「恋が叶う魔法のアイス」だ。」
    "说到冰淇淋，自然就想到了那个「能实现恋爱的魔法冰淇淋」"

    # nil 「あれ以来、心愛との関係は特に変わる事は無かったが、問題が起こったわけでもない。」
    "从那以后，虽然和心爱的关系没有什么特别的变化，但也没有发生什么问题"

    # nil 「もっと、心愛に優しくしてあげるべきなのだろうが、心のどこかで、真冬に対しての躊躇いも感じる。」
    "应该更加温柔地对待心爱，但在内心的某个地方，也有着对真冬的踌躇"

    # nil 「何故、真冬を…。」
    "真冬……为什么呢……"

    # nil 「いや、その感情の理由ぐらいわかっている。」
    "不，我知道那种感情的理由"

    # nil 「心愛と親しくなりたいと思う事と同じように、真冬ともっと親しくなりたいと考えている。」
    "就像我想和心爱亲近一样，我也想和真冬更亲近一些"

    # nil 「なんとも締まらない話だが…。」
    "这听起来有点牵强，但是..."

    # 莲 「（真冬にあのアイスを食べさせたらどうなるのだろうかな）」
    lian "（如果让真冬也恰这个冰淇淋会怎么样呢？）"

    # nil 「そんなことを考えてしまうあたり、俺もヤキが回っている。邪な考えは全部、夏の太陽のせいにしちまおう。」
    "每当我想到这些，我也会有种罪恶感。把所有邪恶的想法都归咎于夏日的阳光吧"

    # nil 「って、郷も歌ってたし。」&协力请求
    "说起来啊，镇上的人现在在唱歌呢"

    # nil 「そんな事を考えていたら、気づいたらアイスの屋台の目の前に吸い寄せられていた。」
    "这样想着，回过神来发现自己被已经吸引到了冰淇淋摊前"

    # 里昂 「はいはーい！　お買い上げありがとうございます！　そしてお幸せに！やっぱりこの場所取りは正解だったみたいだね！」
    show 黄_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0417b.ogg"
    ang 黄_基本_杖_にっこり "好的好的！谢谢惠顾！祝您幸福！果然选择这个地方是正确的！"

    # 莲 「おや…アンタは…」
    lian "哎呀…你是……"

    # nil 「近づいて見ると、妙に見覚えのあるシルエットと聞き覚えのある声を感じ取る。」
    "走近一看，惊奇地发现了眼熟的轮廓和耳熟的声音"

    # nil 「俺の前に訪れていた学生カップルが二つのアイスクリームを買って、道をあけると、案の定、つい先日、例のアイスを俺にくれたアイス売りの少女が屋台を設置していた。」
    "在我面前的一对学生cp买好了两个冰淇淋，让开了前面的道路，果然，前几天送给我那个冰淇淋的少女正在摆摊"

    # 里昂 「やっほー！　蓮君じゃーん！　また会えたねー！　嬉しいよ！」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0418.ogg"
    lion リオン_基本_杖_微笑み "哇! 这不是莲君嘛! 又见面了! 太高兴啦!"
    hide 黄_基本_杖_にっこり

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # 原作没有小头像，这里为了凸显MJ在说话，就加上吧
    # MJ 「よう、マザーファッカー。この間は世話になったな」
    voice "voice/その他/mjf_a1_0034.ogg"
    mj MJ_通常 "哟，妈的法克，上次多亏你照顾了"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「こらこらマイコ－！　蓮君に対してその口の利き方は良くないな！」
    show リオン_基本_杖_ジト目 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0419.ogg"
    lion リオン_基本_杖_ジト目 "喂喂，迈克尔！对莲君这样说话可不好啊！"
    hide リオン_基本_杖_微笑み

    # 莲 「おっす。なんだか繁盛してるようだな。ていうかお前、素だとそんなしゃべり方なのかよ」
    lian "哦，看起来生意兴隆啊。话说回来，你原来就是这么说话的"

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「あの時はヤクやって覚えちゃいねぇ！てめぇがあの時ちょっかいださなきゃ、今頃ガテンボーイズ達とドカタ＝レイヴの真っ最中だったというのにな！」
    # ドカタ：土方 レイヴ：RAVE ガテンボーイズ：GANT &&翻得很不行，协力请求
    voice "voice/その他/mjf_a1_0035.ogg"
    # mj MJ_通常 "我不记得我当时嗑了什么药!你那时不多管闲事的话，我现在正在和那些GANT BOY（L:neta GANT，总部位于瑞典斯德哥尔摩的国际服装品牌，于1949年在美国创立）玩泥巴呢!"
    if persistent.luckykeeperSay == "shutup":
        mj MJ_通常 "我不记得我当时嗑了什么药!你那时不多管闲事的话，我现在正在和那些GANT BOY玩泥巴呢!"
    else:
        mj MJ_通常 "我不记得我当时嗑了什么药!你那时不多管闲事的话，我现在正在和那些GANT BOY（L:neta GANT，总部位于瑞典斯德哥尔摩的国际服装品牌，于1949年在美国创立）玩泥巴呢!"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「MJ。静かにしないと施設に返すよ？」
    show リオン_基本_杖_無表情 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0420.ogg"
    lion リオン_基本_杖_無表情 "MJ，要是不安静的话就送回设施吧？"
    hide リオン_基本_杖_ジト目

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「っ！　そ、それだけはご勘弁を！　あんな所に返されたらタマ潰れちまうよ…」
    voice "voice/その他/mjf_a1_0036.ogg"
    mj MJ_通常 "啊! 饶了我吧! 如果我被送回那个地方，我的蛋蛋会碎的..."

    # nil 「リオンの頭の上の帽子は小刻みに震えながら静かになった。」
    "里昂头上的帽子微微颤抖着安静了下来"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「えへー！　蓮君に言われたとおり、このポイントに店を設置してみたのだ！あ！　ちゃんと自治体と当局の許可は受けてるし、衛生検査も通ってるよ！」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0421.ogg"
    lion リオン_基本_杖_にっこり "欸嘿嘿! 我照着莲君说的，在这个地方设立了摊位! 啊! 我已经得到了地方政府和当局的许可，卫生检查也通过了哟!"
    hide リオン_基本_杖_無表情

    # 莲 「ほう、そいつはおめでたいな。繁盛してるかい？」
    lian "哦，那真是可喜可贺啊。生意兴隆吗"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「おかげ様でホックホクですよー！　いやぁ…一日三食の生活ってのはぁ…いね…」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0422.ogg"
    lion リオン_基本_杖_微笑み "客人是“霍克霍克”地源源不断呢！哎呀，一天三餐的生活真是……不容易啊…"
    hide リオン_基本_杖_にっこり

    # 莲 「そこまで貧乏だったのかよ…」
    lian "你那么穷的嘛…"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「いや、ソシャゲに重課金しちまいまして」
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0423.ogg"
    # lion リオン_基本_杖_悲しい "不是，是我在社交网络游戏氪金太厉害了（L:你们氪金都不手软的嘛，在翻译君写下这句话的头一天听说W为了胡桃氪了300多...）"
    if persistent.luckykeeperSay == "full":
        lion リオン_基本_杖_悲しい "不是，是我在社交网络游戏氪金太厉害了（L:你们氪金都不手软的嘛，在翻译君写下这句话的头一天听说W为了胡桃氪了300多...）"
    else:
        lion リオン_基本_杖_悲しい "不是，是我在社交网络游戏氪金太厉害了"

    hide リオン_基本_杖_微笑み

    # 莲 「ダメじゃないか」
    lian "这可⑧行啊……"

    # 里昂 「だ、だってだって仕方ないじゃんかよぉ！　スタミナ回復するまで待ってられないもの！」
    show リオン_基本_杖_見下し at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0424.ogg"
    lion リオン_基本_杖_見下し "可、可是可是没办法啊! 恢复体力太慢了没法儿等啊!"
    hide リオン_基本_杖_悲しい

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「こっちに来てから寝ても覚めてもタッチパネルばっかしごいてやがるんだぜこのお嬢さん。他にしごくもんねぇのかよってな…俺が現役だった頃は、しごきながらしゃぶってたりも―もごっ」&协力请求
    voice "voice/その他/mjf_a1_0037.ogg"
    mj MJ_通常 "自从我们来到这里，你就一直盯着触摸屏，小姐啊，我不知道你还有没有其他的事情可以做...我在现役的时候，还可以——"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「三度目は言わないよ。黙れマイケル」
    show リオン_基本_杖_ジト目 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0425.ogg"
    lion リオン_基本_杖_ジト目 "我不会再说第三遍了。闭嘴，迈克尔"
    hide リオン_基本_杖_見下し

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「は…はい…」
    voice "voice/その他/mjf_a1_0038.ogg"
    mj MJ_通常 "啊…是…"

    # 莲 「なんつーか…そいつと暮らすのは大変そうだな…おっと」
    lian "怎么说呢…和那家伙一起生活好像很不容易啊…啊"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「はいはーい！　いらっしゃいませ！」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0426.ogg"
    lion リオン_基本_杖_にっこり "好的——好的！欢迎光临！"
    hide リオン_基本_杖_ジト目

    # nil 「またしても、男女一組のペアが客として屋台に訪れた。邪魔しちゃ悪いので、少し屋台から離れて、ベンチに座って屋台の様子を眺める。」
    "又有一对男女来到摊位。因为不想打扰到生意，所以我离开小摊，坐在长椅上观察小摊的情况"

    # nil 「訪れる客はカップルか女子の団体。リオンの服装からして、確かに独り身の男子では近寄りづらい雰囲気がある。」
    "来买东西的顾客大部分是情侣或是女子团体。从里昂的服装来看，确实有种单身男子有难以接近的气氛呢"

    # nil 「３０分ほど眺めていると、下校の流れも止まったようで、客足もまばらになってきた。」
    "看了30分钟左右，放学的人群似乎差不多都散去了，客人也就稀稀落落了"

    # nil 「俺はベンチから立ち上がり、自販機でビン入りのコーラを買って栓を開けると、服の袖で額の汗を拭いているリオンに近づいた。」
    "我从长椅上站了起来，在自动贩卖机买了瓶装可乐，打开瓶盖，靠近了正在用衣袖擦拭额头汗水的里昂"

    # 里昂 「ふいー…いくら制服とはいえ、あっついねぇ…どーも」
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0427.ogg"
    lion リオン_基本_杖_悲しい "呼欸...就算是制服，这也太热了...谢谢"
    hide リオン_基本_杖_にっこり

    # 莲 「ほれ、お疲れさん」
    lian "给，辛苦了"

    # 里昂 「はにゃ！　わー！　ありがとーう！」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0428.ogg"
    lion リオン_基本_杖_微笑み "呼喵！哇！谢谢！"
    hide リオン_基本_杖_悲しい

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「俺のは無いのか」
    voice "voice/その他/mjf_a1_0039.ogg"
    mj MJ_通常 "没有我的吗？"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「空き瓶でよければ突っ込んであげるよ」
    voice "voice/リオン/ron_a1_0429.ogg"
    lion リオン_基本_杖_微笑み "如果空瓶可以的话，我就给你塞进去"

    # 莲 「しかも太い方をな」
    lian "而且是粗的那边"

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「Ass hole！！」
    voice "voice/その他/mjf_a1_0040.ogg"
    mj MJ_通常 "Ass hole！！"

    # nil 「こは外人の笑い声でお願いします。」
    "这里请配上外国人的笑声"

    # nil 「リオンは俺が差し出したコーラを受け取ると、無邪気な笑顔を浮かべて、一気に飲み干した。」
    "里昂接受了我递过来的可乐，脸上露出天真无邪的笑容，一饮而尽"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「ごく…ごく…ぷはーっ！　かー！　うまい！　仕事終わり…ってわけじゃないけど、一息ついた時の瓶のコーラは最高だね！」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0430.ogg"
    lion リオン_基本_杖_にっこり "咕噜…咕噜…嗯…哇咿！超好喝！工作结……虽然工作还没结束，但休息的时候来瓶可乐真是太棒了！"
    hide リオン_基本_杖_微笑み

    # 莲 「おう、喜んでくれたなら何よりだ」
    lian "嗯，如果你高兴的话，那比什么都好"

    # 里昂 「にゃはー、その言葉、言い慣れてるっていうイントネーションだね！」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0431.ogg"
    lion リオン_基本_杖_微笑み "呀哈哈，这句话，是说惯了的语调呢！"
    hide リオン_基本_杖_にっこり

    # 莲 「そうか？」
    lian "是吗？"

    # 里昂 「うんうん！　自分の幸せよりも、他人の幸せを優先しちゃうタイプでしょ、君ぃ」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0432.ogg"
    lion リオン_基本_杖_にっこり "嗯嗯！你呀，是那种比起自己的幸福，更优先考虑他人幸福的类型吧"
    hide リオン_基本_杖_微笑み

    # 莲 「言われてみればそうかもしれないな」
    lian "这么说来也许是这样呢"

    # nil 「リオンは俺に瓶の蓋をつきつけて、ウインクを見せる。」
    "里昂拿瓶盖对着我，向我眨眼"

    # nil 「前屈みの姿勢になった隙に、つい胸元に目線を向けてしまう。やはり…心愛と真冬よりも…。」
    "趁着身体前倾的时候，不由自主地将视线投向胸前。果然... 比起心爱和真冬..."

    # 里昂 「どこを見ているんだねまったくー」
    show リオン_基本_杖_見下し at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0433.ogg"
    lion リオン_基本_杖_見下し "在看哪里啊，你这家伙"
    hide リオン_基本_杖_にっこり

    # 莲 「そういえばその服ノーブラか」
    lian "说起来啊，你那件衣服是No-bra吗？"

    # 里昂 「ばっ…！　そ、そーいうことは気づいてもノータッチでいこうよ！　ついでにノーブラじゃないから！　見せられないのが非常に残念ですがね！」
    show リオン_基本_杖_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0434.ogg"
    lion リオン_基本_杖_驚き "呃…！那、那个，即使注意到了这点也不要触碰哦！顺便说一下，我才不是No-bra呢！不能让你看到真是很遗憾呢！"
    hide リオン_基本_杖_見下し

    # 莲 「ていうか、おっぱいでかいよな」
    # lian "话说，欧派好大啊（L:莲你都有心爱了怎么还能这样呢！）"
    if persistent.luckykeeperSay == "full":
        lian "话说，欧派好大啊（L:莲你都有心爱了怎么还能这样呢！）"
    else:
        lian "话说，欧派好大啊"

    # 里昂 「なんだねいきなり！？　突然おっぱいばっかり褒めやがって…男って奴は…どこの国でも一緒かい…」
    voice "voice/リオン/ron_a1_0435.ogg"
    lion リオン_基本_杖_驚き "什么嘛，突然间！？突然一个劲地夸奖我的欧派……男人…不管在哪个国家都一样啊…"

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「リオンは尻も良いぞ」
    voice "voice/その他/mjf_a1_0041.ogg"
    mj MJ_通常 "里昂的屁股也很好哦"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「黙れマイケル」
    show リオン_基本_杖_見下し at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0436.ogg"
    lion リオン_基本_杖_見下し "闭嘴迈克尔"
    hide リオン_基本_杖_驚き

    # 莲 「美味しそうな食べ物があったら、つい目線を向けてしまうのが人間ってやつだろ？」
    lian "如果有看起来很好吃的食物的话，不知不觉就会把视线转向那边，这就是人类吧？"

    # 里昂 「はいはい、お褒め頂きありがとうございます。つっても、好きな人いるんでしょー？」
    # （L:原作这里也是没有配音...）
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    # voice "voice/リオン/ron_a1_0437.ogg"
    # lion リオン_基本_杖_微笑み "好的好的，谢谢您的夸奖。你也有喜欢的人吧？（L:原作这里没有配音...）"
    if persistent.luckykeeperSay == "shutup":
        lion リオン_基本_杖_微笑み "好的好的，谢谢您的夸奖。你也有喜欢的人吧？"
    else:
        lion リオン_基本_杖_微笑み "好的好的，谢谢您的夸奖。你也有喜欢的人吧？（L:原作这里没有配音...）"

    hide リオン_基本_杖_見下し

    # 莲 「あ、あ…その事についてなんだが…」
    lian "那，那个…关于那件事…"

    # 里昂 「おう、恋バナかね？　どーんとお姉さんに相談してきなさい！」
    # （L:原作这里也是没有配音...）
    # voice "voice/リオン/ron_a1_0438.ogg"
    # lion リオン_基本_杖_微笑み "哦，是恋爱话题吗？请务必和姐姐商量一下！（L:原作这里也是没有配音...）"
    if persistent.luckykeeperSay == "shutup":
        lion リオン_基本_杖_微笑み "哦，是恋爱话题吗？请务必和姐姐商量一下！"
    else:
        lion リオン_基本_杖_微笑み "哦，是恋爱话题吗？请务必和姐姐商量一下！（L:原作这里也是没有配音...）"

    # nil 「その事…？　まぁいや。」
    "那件事…？算了吧"

    # 莲 「この間貰ったアイスなんだが…なんていうか…効果は確かにあったよ」
    lian "之前收到的冰淇淋…怎么说呢…效果确实很好"

    # 里昂 「おう！　それは良かったにゃ！　ご覧頂いた通り、なかなか、独り身の子が訪れなくてねー！　実はあのアイスは、蓮くんだけにしか渡してないのだよ！」
    voice "voice/リオン/ron_a1_0439.ogg"
    lion リオン_基本_杖_微笑み "哇！那太好了喵！正如你所看到的那样，我这里没有什么单身的孩子过来呢！其实那个冰淇淋只给了莲君一个人哦！"

    # 莲 「効果はあったんだが…ちょっと、強すぎじゃないか？」
    lian "虽然有效果，但是这个效果实在是有点太强了吧？"

    # 里昂 「ほう…差し支えなければ、詳しく聞かせてくれないかな」
    voice "voice/リオン/ron_a1_0440.ogg"
    lion リオン_基本_杖_微笑み "哦......如果你不介意的话，能告诉我详细情况吗?"

    # nil 「一瞬にして、リオンの目付きが変わる。普段の猫のような無邪気な笑顔ではなく、自分の仕事と真剣に向き合う職人の目だ。」
    "一瞬间，里昂的眼神改变了。不是平时的像猫那样天真无邪的笑容，而是认真对待自己工作的工匠的眼神"

    # nil 「洗いざらい話すのは少し恥ずかしかったが、リオンの仕事のためだし…。」
    "我有点不好意思把事情全部都说出来，但这是为了里昂的工作..."

    # 里昂 「あ、大丈夫。安心して。無理に聞こうとは思わないから」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0441.ogg"
    lion リオン_基本_杖_にっこり "啊，没关系的。放心吧，我不会强迫你说出来的"
    hide リオン_基本_杖_微笑み

    # nil 「俺が話すのを躊躇っていると、リオンは表情を和らげて、にっこりと笑った。」
    "当我犹豫要不要说出来的时候，里昂表情缓和了，莞尔一笑"

    # 莲 「いや、話すよ。少し恥ずかしいが…」
    lian "不，我会告诉你的，就是有点不好意思…"

    # 里昂 「にゃは、ありがとう！」
    show リオン_基本_杖_にっこり:
        zoom 1.5
        yalign 0.07
        xalign 0.5
        linear 0.15 yalign 0.14
        linear 0.15 yalign 0.07
    voice "voice/リオン/ron_a1_0442.ogg"
    lion リオン_基本_杖_にっこり "呀哈哈，谢谢！"

    # nil 「実際、心愛との一日は、どこまでがアイスの効果だったかは定かではないので、とりあえず一日を通して（身体を重ねた事についても）話した。」
    "事实上，在与心爱的一天里，我并不确定到底有多少是冰激凌的效果，所以我暂且把一整天的事情都讲了出来（包括身体重叠的事情)"

    # nil 「リオンは真剣な表情のま、笑ったりはせずひたすら俺の話に耳を傾けていた。」
    "里昂表情严肃，没有笑，只是专心听我描述着"

    # 莲 「と、まぁこんな感じだ。勿論、あれから俺と心愛の関係は良くなっているし、だからといって問題だというわけではないんだが」
    lian "嗯，就是这样的感觉。当然，从那之后我和心爱的关系变好了，但这并不是问题的关键……"

    # 里昂 「ふむー…名前はラブポーションだけど…エロい効果があるようには設計してないんだけどなぁ…」
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0443.ogg"
    # lion リオン_基本_杖_悲しい "嗯...虽然名字叫“Lovepotion”（L:potion是“药水”的意思），但是没有设计成具有 H 效果的啊..."
    if persistent.luckykeeperSay == "shutup":
        lion リオン_基本_杖_悲しい "嗯...虽然名字叫“Lovepotion”，但是没有设计成具有 H 效果的啊..."
    else:
        lion リオン_基本_杖_悲しい "嗯...虽然名字叫“Lovepotion”（L:potion是“药水”的意思），但是没有设计成具有 H 效果的啊..."

    hide リオン_基本_杖_にっこり

    # 莲 「結果的に、俺と心愛の仲は良くなってるし、感謝はしているよ。ありがとう」
    lian "从结果来看，我和心爱的关系变好了，谢谢你"

    # 里昂 「おう、そう言って貰えると嬉しいよ！　そだ、ちょっとまってね」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0444.ogg"
    lion リオン_基本_杖_微笑み "哦，听到你这么说我就很高兴了！对了，稍等一下哦"
    hide リオン_基本_杖_悲しい

    # nil 「リオンは屋台の下からクーラーボックスを取り出すと、蓋をあけてカップのアイスを取り出した。」
    "里昂从摊位下面拿出冷藏箱，打开盖子，拿出了一杯冰淇淋"

    # 里昂 「中身は同じだけど、カップのサンプルがあるんだけど、もう一回試してみる？」
    voice "voice/リオン/ron_a1_0445.ogg"
    lion リオン_基本_杖_微笑み "虽然里面的东西是一样的，但是这个是装在杯子里面的样品，要再试一次吗？"

    # 莲 「え？　そんな何度も貰っちゃっていの？　貴重な試作品じゃないのか」
    lian "诶？要再次送给我吗？这不是很贵重的样品吗？"

    # 里昂 「いやいや、むしろ、蓮くんぐらいしか渡す人いなくてさ！エロい効果があるならあるで…夜のお楽しみに使ってくれてもいんだぜー？」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0446.ogg"
    lion リオン_基本_杖_にっこり "不不不，不如说，只有像莲这样的人才能交给你！如果有色情效果的话……也可以作为晚上的乐趣来使用吧？"
    hide リオン_基本_杖_微笑み

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「抜かずの６９発。なんつってな」
    voice "voice/その他/mjf_a1_0042.ogg"
    mj MJ_通常 "「不拔的69发」，怎么说呢"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「黙れマイケル」
    show リオン_基本_杖_見下し at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0447.ogg"
    lion リオン_基本_杖_見下し "闭嘴迈克尔"
    hide リオン_基本_杖_にっこり

    # 莲 「本来の目的とは違うような気がするが…まぁ、考えておくよ」
    lian "我觉得和本来的目的不大一样……算了，我会考虑的"

    # 里昂 「Oh Yeah！しばらくこら辺にお店出してるだろうから、効果があったら教えてね！」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0448.ogg"
    lion リオン_基本_杖_微笑み "Oh Yeah！我暂时在这附近开店，如果有效果的话请来告诉我！"
    hide リオン_基本_杖_見下し

    # nil 「奥手な心愛にはちょうどいかもしれない。むしろ、真冬に食べさせても…。」
    "对于晚熟的心爱也许正合适。不过，让真冬吃也…"

    # 莲 「そういえば、自分では食べた事はないのか？」
    lian "这么说来，你自己没吃过吗？"

    # nil 「俺はリオンから、運搬用のドライアイスを受け取りながら（３０分以内ならもつらしい）、つい浮かんだ疑問を投げかけた。」
    "我从里昂那里，一边接过防止融化用的干冰（好像是够30分钟的量），一边不由自主地提出了这样的一个问题"

    # 里昂 「む？　あるよー。　効果はともかく、美味しくないといけないからね！」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0449.ogg"
    lion リオン_基本_杖_にっこり "嗯？有的哦。不管效果如何，必须要好吃才行啊！"
    hide リオン_基本_杖_微笑み

    # 莲 「で、別にエロい効果は…」
    lian "那么，有工口的效果吗…"

    # 里昂 「そ、それを聞いちゃうかなー…ちょ、ちょーっと恥ずかしいなー！」
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0450.ogg"
    lion リオン_基本_杖_悲しい "要，要问这个问题吗……有、有点不好意思啊——！"
    hide リオン_基本_杖_にっこり

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「むぎゅっ…！　まだ何も言ってねぇだろ―もご！」
    voice "voice/その他/mjf_a1_0043.ogg"
    mj MJ_通常 "喂喂……!我还什么都没说呢!"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # nil 「リオンは凄まじいスピードで、帽子の頭を抑えた。」
    "里昂以惊人的速度压住了帽子的头"

    # 莲 「俺も恥ずかしい話をしたんだし、そこは引き替えという事で」
    lian "刚刚我也说了很不好意思的话，那么作为交换..."

    # 里昂 「それは俗に言う『決して断れない申し出』って奴だね…！」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0451.ogg"
    lion リオン_基本_杖_微笑み "这就是俗话所说的『绝对无法拒绝的提议』吧…！"
    hide リオン_基本_杖_悲しい

    # 莲 「ゴットファーザー好きなのか？」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%B4%E3%83%83%E3%83%89%E3%83%95%E3%82%A1%E3%83%BC%E3%82%B6%E3%83%BC_(%E6%98%A0%E7%94%BB)
    # lian "你喜欢『教父』吗？（L:是一部1972年的美国帮派电影，根据马里奥·普佐的同名畅销小说改编，一共三集。被称为『教父三部曲』，长年占据在互联网电影数据库（IMDb）的史上最佳250部电影名单前列）"
    if persistent.luckykeeperSay == "shutup":
        lian "你喜欢『教父』吗？"
    else:
        lian "你喜欢『教父』吗？（L:是一部1972年的美国帮派电影，根据马里奥·普佐的同名畅销小说改编，一共三集。被称为『教父三部曲』，长年占据在互联网电影数据库（IMDb）的史上最佳250部电影名单前列）"

    # 里昂 「１だけ見たよ。ふむー…。うぅ…誰にも言わない…？」
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0452.ogg"
    lion リオン_基本_杖_悲しい "我只看了1。嗯……那个、不要告诉其他人哦…？"
    hide リオン_基本_杖_微笑み

    # 莲 「まぁ、そりゃ言う相手もいねぇしな」
    lian "嘛，也没有可以说的对象啊"

    # 里昂 「じゃぁ…ごくり…」
    show リオン_基本_杖_ジト目 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0453.ogg"
    lion リオン_基本_杖_ジト目 "那...再来一点..."
    hide リオン_基本_杖_悲しい

    # nil 「リオンが息を呑む。恥ずかしがっているリオンも新鮮だ。見ているこっちも、少しドキドキしてしまう。」
    "里昂屏住呼吸。害羞的里昂也让我觉得很新鲜。看得我的心也稍微有点七上八下了"

    # 里昂 「まぁ、何も起こらなかったよ」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0454.ogg"
    lion リオン_基本_杖_にっこり "嘛，什么都没发生吧"
    hide リオン_基本_杖_ジト目

    # 莲 「なら引っ張るなよ！　ドキドキしたこっちがバカみてぇじゃねぇか！」
    lian "那就别扯着我啊喂！心跳加速的我真是笨蛋！"

    # 里昂 「ハッハァー！　おねーさんをからかおうなんて１０年早いんだぜー！」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0455.ogg"
    lion リオン_基本_杖_微笑み "哈哈！要捉弄姐姐我你还早10年呢！"
    hide リオン_基本_杖_にっこり

    # 莲 「まぁ、効果があったらあったで、その時点で直してるか」
    # lian "嘛，如果真的有这样效果的话，到时候再改好了（L:这两句话没看懂，感觉是和『教父』这个电影有关，但是我没看过。所以附原文「まぁ、効果があったらあったで、その時点で直してるか」）"
    if persistent.luckykeeperSay == "shutup":
        lian "嘛，如果真的有这样效果的话，到时候再改好了"
    else:
        lian "嘛，如果真的有这样效果的话，到时候再改好了（L:这两句话没看懂，感觉是和『教父』这个电影有关，但是我没看过。所以附原文「まぁ、効果があったらあったで、その時点で直してるか」）"

    # 里昂 「いんや、それはそれで、その方向で売り出してると思うよボロ儲けだね…じゅるり」
    show  リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0456.ogg"
    # lion リオン_基本_杖_にっこり "嗯，我觉得他们正朝着这个方向发展，赚得盆满钵满……吸溜（「いんや、それはそれで、その方向で売り出してると思うよボロ儲けだね…じゅるり」，会的大哥大姐快去Gayhub提issues让我爬！）"
    # lion リオン_基本_杖_にっこり "嗯，我觉得如果朝着这个方向开发，说不定能赚得盆满钵满呢……吸溜（「いんや、それはそれで、その方向で売り出してると思うよボロ儲けだね…じゅるり」，会的大哥大姐快去Gayhub提issues让我爬！）"
    if persistent.luckykeeperSay == "shutup":
        lion リオン_基本_杖_にっこり "嗯，我觉得如果朝着这个方向开发，说不定能赚得盆满钵满呢……吸溜"
    else:
        lion リオン_基本_杖_にっこり "嗯，我觉得如果朝着这个方向开发，说不定能赚得盆满钵满呢……吸溜（「いんや、それはそれで、その方向で売り出してると思うよボロ儲けだね…じゅるり」，会的大哥大姐快去Gayhub提issues让我爬！）"

    hide リオン_基本_杖_微笑み

    # 莲 「リオンの身に何も起こらないっていうのは、要するに、恋してる相手が居ないってことか…」
    lian "里昂的身上什么都没有发生，也就是说，没有恋爱的对象吗…"

    # 里昂 「ヘイカモォン！　ちょっと言い過ぎだよ君ぃー！その質問については黙秘権を行使させてもらいまーす」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0457.ogg"
    lion リオン_基本_杖_微笑み "哼！你这就说得有点过分了！关于这个问题我要行使沉默权"
    hide リオン_基本_杖_にっこり

    # 莲 「黙秘する時点で答えは出てるんだぜ」
    lian "当你沉默的时候答案就出来了"

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「正解！」
    voice "voice/その他/mjf_a1_0044.ogg"
    mj MJ_通常 "正解！"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「黙れマイケル」
    show リオン_基本_杖_ジト目 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0458.ogg"
    lion リオン_基本_杖_ジト目 "闭嘴迈克尔"
    hide リオン_基本_杖_微笑み

    # 莲 「可愛いなリオン」
    lian "里昂真可爱"

    # 里昂 「うるせーうるせー！　もー！　君は優しいけど、少し意地悪だね…」
    show リオン_基本_杖_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0459.ogg"
    lion リオン_基本_杖_ニタァ "无路赛——无路赛——！哼！你人很好，但是有点坏心眼…"
    hide リオン_基本_杖_ジト目

    # 莲 「人を無駄にドキらせた仕返しっつーことで一つ」
    lian "这是让我白白心动的报复"

    # 里昂 「好きな人いるんだから、他の女の子にドキドキしちゃだめだぞ！そういう悪い子は、めっめっだぞ！」
    show リオン_基本_杖_ジト目 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0460.ogg"
    lion リオン_基本_杖_ジト目 "因为有喜欢的人了，所以不能对其他女孩子心动！这样的坏孩子可⑧行啊！"
    hide リオン_基本_杖_ニタァ

    # 莲 「へいへい、すんません。ともあれ、またサンプルをありがとう。有効活用させて貰うよ」
    lian "好的，对不起。不管怎样，还是谢谢你的样品，我会好好利用的"

    # 里昂 「おっす！　寄り道しちゃだめだよー？」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0461.ogg"
    # lion リオン_基本_杖_微笑み "押忍！（L:是空手道、剑道、柔道等武术界人士之间使用的一种打招呼方式）可不要绕道哦？"
    if persistent.luckykeeperSay == "shutup":
        lion リオン_基本_杖_微笑み "押忍！可不要绕道哦？"
    else:
        lion リオン_基本_杖_微笑み "押忍！（L:是空手道、剑道、柔道等武术界人士之间使用的一种打招呼方式）可不要绕道哦？"

    hide リオン_基本_杖_ジト目

    # 莲 「気をつけるよ」
    lian "我会注意的"

    # nil 「リオンはもう一度前屈みになって指をさしてくる。」
    "里昂再次向前弯腰指着我"

    # 里昂 「あ、言い忘れた。お話を聞かせてくれてありがとう。また会えて嬉しかったよ」
    voice "voice/リオン/ron_a1_0462.ogg"
    lion リオン_基本_杖_微笑み "啊，我忘记说了，谢谢你告诉我你的故事。很高兴再次见到你"

    # 莲 「そうか。喜んで貰えたならなにより」
    lian "这样啊，如果能让你高兴的话就太好了"

    # 里昂 「あはっ！　ほら、また言った！」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0463.ogg"
    lion リオン_基本_杖_にっこり "哈哈，看，你又说这种话了"
    hide リオン_基本_杖_微笑み

    # 莲 「どうやら、確かに口癖らしいな…」
    lian "看来，确实是口头禅啊…"

    # 里昂 「それがきっと、君の良さってやつだね！　じゃあね、蓮くん！」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0464.ogg"
    lion リオン_基本_杖_微笑み "那一定是你的优点吧！再见，莲君！"
    hide リオン_基本_杖_にっこり

    # 莲 「またな」
    lian "再见"

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「あばよ。Mr優男サン。もし望むなら、ケツを可愛がってやってもいぜ」
    voice "voice/その他/mjf_a1_0045.ogg"
    mj MJ_通常 "再见，Mr.帅哥桑。如果你愿意的话，我可以疼爱你的屁股哟"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「黙れマイケル」
    # （L:这里原作也没有音声的样子，拉跨了）
    # voice "voice/リオン/ron_a1_0458.ogg"
    # voice "voice/リオン/ron_a1_0447.ogg"
    voice "voice/リオン/ron_a1_0436.ogg"
    lion リオン_基本_杖_微笑み "闭嘴迈克尔"

    # nil 「リオンとMJに別れを告げて、アイスの屋台を後にする。」
    "和里昂还有MJ告别后，我离开了冰激凌摊"

    # nil 「俺が去ると同時に、またアイス屋台には客足が戻りはじめた。」
    "我走的同时，又有客人来到了冰激凌摊"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「あーあ…嘘、ついちゃったなー…でも、仕方ないよ…こうでもしないと、こに来た目的が達成できないもんね…」
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0465.ogg"
    lion リオン_基本_杖_悲しい "啊—啊......我撒谎了呢...不过，也没办法呢...不这样的话，来这里的目的就达不到了..."
    hide リオン_基本_杖_微笑み

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「今更何いってやがる…元よりてめェが始めた事だろうが」
    voice "voice/その他/mjf_a1_0046.ogg"
    mj MJ_通常 "事到如今还说什么呢……这件事本来就是你挑起来的吧"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「うん。だから、もう大丈夫…大丈夫だから…」
    voice "voice/リオン/ron_a1_0466.ogg"
    lion リオン_基本_杖_悲しい "嗯，所以已经没关系了…没关系的说…"

    # 场景切换
    # scene04 场景2 【和里昂的再次相遇】 结束
    # scene04 场景3 【奇奇怪怪的冰淇淋又被人恰了，这次是真冬！】 开始
    # 地点：街道->葛城家客厅
    # 人物：莲
    # BGM不变
    # 小场景的名称
    $ partName = " 【奇奇怪怪的冰淇淋又被人恰了，这次是真冬！】"
    $ changeTitleName()

    image bg リビングa_夕 = "images/bg/リビングa_夕.png"
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene リビングa_夕 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「ただいまー」
    lian "我回来啦——"

    # nil 「真冬の奴はまだ帰って来ていないらしい。温泉の建設ご苦労様である。」
    "看来真冬这家伙还没回来。建设温泉真是辛苦了"

    # nil 「しかし、どこで温泉を掘っているのだろう。もしかして学園の敷地内か？」
    "但是，是在哪里挖温泉呢，难道是在学校内吗？"

    # nil 「だとしたら冬あたりはフィーバーだな。」
    # "如果是这样的话，等到冬天的时候会很狂热吧（L:是双重意义上的狂热捏）"
    if persistent.luckykeeperSay == "full":
        "如果是这样的话，等到冬天的时候会很狂热吧（L:是双重意义上的狂热捏）"
    else:
        "如果是这样的话，等到冬天的时候会很狂热吧"

    # nil 「静まりかえった我が家に、開け放ったカーテンから陽光が差し込む。」
    "在寂静的家里，阳光从敞开的窗帘照射了进来"

    # nil 「換気をしていなかったので、屋内でも暑い。むしろ外のが涼しいんじゃないの…？」
    "因为没有换气，所以在室内也很热。或者说现在外面凉快点儿吧…？"

    # nil 「急いで冷蔵庫の冷凍室に貰った「例のアイス」をしまうと、真冬が帰ってきた時に暑いのもアレだし、換気扇のスイッチを入れて、」
    "急忙把拿回来的「那个冰淇淋」放进冰箱的冷冻室，估计等真冬回来的时候应该还是会很热，所以就打开换气扇的开关"

    # nil 「一人でエアコンをかけるのもったいないので、外に出ておくとしよう。」
    "因为一个人开空调的话就太浪费了，所以在换气扇让室内温度降下来之前还是先出去吧"

    # 场景切换
    # 地点：葛城家客厅->葛城家外
    # 人物：莲
    # BGM不变

    image bg 自宅_夕 = "images/bg/自宅_夕.png"
    scene 自宅_夕 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「下駄箱の上段からシステムのヘルメットを取り出して、制服のま外に出る。」
    # "从鞋柜的上层取出 System 的头盔（L:这里neta宝马的System头盔系列，按照作品发售时间，应该是System6，现在的价格大概是5810元软妹币），穿着制服走了出去"
    if persistent.luckykeeperSay == "shutup":
        "从鞋柜的上层取出 System 的头盔，穿着制服走了出去"
    else:
        "从鞋柜的上层取出 System 的头盔（L:这里neta宝马的System头盔系列，按照作品发售时间，应该是System6，现在的价格大概是5810元软妹币），穿着制服走了出去"

    # nil 「車庫から250CCのバイクを引っ張り出して、キーを回す。」
    "把车库里250CC的摩托车推出来，转动钥匙"

    # nil 「スタータースイッチを押してエンジンをかけて、クラッチを切ってギアをローに落とした。」
    "按下启动开关，发动引擎，踩下离合器，降到低档"

    # 莲 「とりあえず飯だな」
    lian "总之先去恰饭吧"

    # nil 「そんなにお腹はすいていなかったが、空腹を放置すると大変な事になるので、バイクを転がしながら、どこで食うかを考えるとしよう。」
    "虽然没有那么饿，但是如果放任空腹不管的话会很麻烦，所以就一边骑摩托车一边考虑在哪里吃吧"

    # nil 「この前タダ飯を頂いてしまった、例のダイナーにしようかな。」
    "上次去那儿白嫖了饭，所以还是去那里吧"

    # nil 「そうしましょう。」
    "就这么办吧"

    # nil 「スロットルを捻って、クラッチをあけると、バイクはゆっくりと排気音を立てながら進み出した。」
    "扭动油门，踩下离合器，摩托车发出排气声缓缓地向前驶去"

    # 场景切换
    # 葛城家外->天空
    # 人物：真冬（真冬视角） 想瑠喵
    # BGM：英文歌 平缓 Music Through Love (ft. Admiral Bob)

    play music bgmnineteen fadein 4.0 fadeout 4.0
    image bg 空_夕a = "images/bg/空_夕a.png"
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 空_夕a at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ヒロシです」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%92%E3%83%AD%E3%82%B7
    voice "voice/真冬/maf_a1_0208.ogg"
    # dong 真冬_制服_基本_無表情 "我是ヒロシ（L:这个人本名齊藤健一，11区喜剧演员、Youtuber）"
    if persistent.luckykeeperSay == "shutup":
        dong 真冬_制服_基本_無表情 "我是ヒロシ"
    else:
        dong 真冬_制服_基本_無表情 "我是ヒロシ（L:这个人本名齊藤健一，11区喜剧演员、Youtuber）"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「懐かしいなそれ…」
    voice "voice/想瑠/sol_a1_0098.ogg"
    liu 想瑠_スーツ_見下し "好怀念啊，那个…"

    # nil 「ネタが古かったとです。」
    "这个段子已经过时了"

    # nil 「真冬です。」
    "现在是真冬视角"

    # nil 「想瑠にゃん先生の車に乗って我が家へと向かっています。調査も大詰め。」
    "调查已经接近尾声了，坐着想瑠喵的车回家"

    # nil 「順調に進めば、冬には温泉施設が学園の敷地内に作れるということで、今から冬が楽しみです。」
    "如果一切顺利的话，到了冬天，学园内就可以建起来温泉了，所以现在就开始期待着冬天的到来了捏"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # nil 「真冬が冬を楽しみにしています。真冬です。」
    # 真冬です 是真冬desu~ 这里并不好翻......
    "真冬期待着冬天的到来。真冬是这么想的"

    # nil 「想瑠にゃんの車は二人乗りのオープンカーで、開け放たれたルーフから流れてくる風が、私たちの髪を靡かせていました。」
    "想瑠的车是一辆双座敞篷车，敞开的车顶吹来的风让我们的头发随风飘动"

    # 真冬 「まふまふ……」
    voice "voice/真冬/maf_a1_0209.ogg"
    dong 真冬_制服_基本_まったり "嘛呼嘛……"

    # nil 「お土産に貰ったアイスクリーム味の宇宙食を食べながら、私は流れてくるラジオの音楽に耳を傾けています。」
    "我一边吃着作为礼物收到的冰淇淋味道的太空餐，一边听着收音机里传来的歌声"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「で、この後、大好きなお兄ちゃんにどんなアプローチをするんだい？」
    voice "voice/想瑠/sol_a1_0099.ogg"
    liu 想瑠_スーツ_ニヤリ "呐，接下来，你打算怎样接近你daisuki的欧尼酱捏?"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「っ！　…ごくっ…まふ。いきなりだね」
    voice "voice/真冬/maf_a1_0210.ogg"
    dong 真冬_制服_基本_ジト目 "咕! ...咕...哇哈...嘛呼...真是突然啊"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「あは、そりゃー気になるじゃないか。生徒の恋路を手助けするのもまた仕事のうちさー」
    voice "voice/想瑠/sol_a1_0100.ogg"
    liu 想瑠_スーツ_ニヤリ "哈哈哈，你不是挺在意吗？帮助学生恋爱也是工作的一部分呢"

    # nil 「想瑠にゃんに、私の気持ちは見抜かれていました。なので、ちょいちょい、自分はどうすべきかを相談しています。」
    "想瑠喵看穿了我的心情。所以，稍微和她商量一下自己应该怎么做吧"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「んー…特にコレといって決めてはないけど…。お兄ちゃんが喜ぶ事をしてあげてらなーって思ってるよ」
    voice "voice/真冬/maf_a1_0211.ogg"
    dong 真冬_制服_基本_微笑み "emmm……虽然我还没有什么特别的想法……但是我会做让欧尼酱开心的事情的说"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「献身的なのは結構だが、自分から歩み寄らんと得るものも得られんぞ」
    voice "voice/想瑠/sol_a1_0101.ogg"
    liu 想瑠_スーツ_真顔2 "献身固然是好的，但是如果不主动接近，最终也得不到什么"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うん。わかってはいるけど…今の関係を変えるのが怖いっていうか…。今更、兄妹だからとか、そういう事を言うつもりはないけど」
    voice "voice/真冬/maf_a1_0212.ogg"
    dong 真冬_制服_基本_泣き "嗯，我知道的，但是...或者说是害怕改变现在的关系...事到如今，我也不想说什么是兄妹之类的话了"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「まぁ…その言い分はわからんでもない。兄妹だと複雑だよな…」
    voice "voice/想瑠/sol_a1_0102.ogg"
    # liu 想瑠_スーツ_悲しみ "嘛，这个理由也不难理解。兄妹的话雀实是很复杂啊…"
    liu 想瑠_スーツ_悲しみ "嘛，这个理由也不难理解。兄妹的话雀食是很复杂啊…"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「似たような経験が…？」
    voice "voice/真冬/maf_a1_0213.ogg"
    # dong 真冬_制服_基本_無表情 "有类似的经验吗？（L:参考本作前作，这里不多剧透，虽然我还没推完但是有点头猪，有兴趣的话可以考虑去推一下）"
    if persistent.luckykeeperSay == "shutup":
        dong 真冬_制服_基本_無表情 "有类似的经验吗？"
    else:
        dong 真冬_制服_基本_無表情 "有类似的经验吗？（L:参考本作前作，这里不多剧透，虽然我还没推完但是有点头猪，有兴趣的话可以考虑去推一下）"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「それは秘密。君が欲しい物を手に入れたら、その時にでも教えてあげるよ」
    voice "voice/想瑠/sol_a1_0103.ogg"
    liu 想瑠_スーツ_ニヤリ "这个是秘密哦。等你得到想要的东西，到时候我再告诉你"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「楽しみにしておく。そのためにも、動かなきゃ…かー」
    voice "voice/真冬/maf_a1_0214.ogg"
    dong 真冬_制服_基本_微笑み "我很期待。为了这个，必须要行动起来……呢——"

    # nil 「想瑠にゃんは、「ふっ」と微笑んでラジオのボリュームを上げました。」
    "想瑠喵笑着「呼」地提高了收音机的音量"

    # nil 「私は、ため息をつきながら、景色を眺めました。」
    "我一边叹气一边眺望风景"

    # nil 「直射日光が目に入って眩しいです。」
    "阳光直射到眼睛里很是刺眼"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「あ、そだ、想瑠にゃん。ちょっと寄って欲しい所があるんだ」
    voice "voice/真冬/maf_a1_0215.ogg"
    dong 真冬_制服_基本_無表情 "啊，对了，想瑠喵。我有个地方想让你带我去"

    # 原地tp
    # BGM不变
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 空_夕a at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「しっかし君のお兄ちゃんはまた妙なモノに…」
    voice "voice/想瑠/sol_a1_0104.ogg"
    liu 想瑠_スーツ_悲しみ "话说你的哥哥又变成了奇怪的样子…"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うん。でも、お肌つやつやしてたから、良い傾向だと思う」
    voice "voice/真冬/maf_a1_0216.ogg"
    dong 真冬_制服_基本_微笑み "嗯。但是，因为皮肤变光滑了，所以我觉得这是好的倾向呢"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ついでにデトックスにでも連れてってやるとい」
    # 参考资料：https://www.adpkd.jp/yomoyama/vol08_04.html # 太有趣了
    voice "voice/想瑠/sol_a1_0105.ogg"
    liu 想瑠_スーツ_ニヤリ "顺便带他去排个毒吧"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そんな事したら、多分お兄ちゃんが全部おしっことして出ちゃう」
    # 参考资料：https://zh.wikipedia.org/wiki/%E8%A7%A3%E6%AF%92
    voice "voice/真冬/maf_a1_0217.ogg"
    # dong 真冬_制服_基本_無表情 "那样的话，大概哥哥会全部作为尿尿出来（L:这里说的是新陈代谢排毒法，就是利用人体自身的新陈代谢来排毒，通过药物、食物加快新陈代谢，比如恰个西瓜）"
    if persistent.luckykeeperSay == "shutup":
        dong 真冬_制服_基本_無表情 "那样的话，大概哥哥会全部作为尿尿出来"
    else:
        dong 真冬_制服_基本_無表情 "那样的话，大概哥哥会全部作为尿尿出来（L:这里说的是新陈代谢排毒法，就是利用人体自身的新陈代谢来排毒，通过药物、食物加快新陈代谢，比如恰个西瓜）"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ははは、そうかもな」
    voice "voice/想瑠/sol_a1_0106.ogg"
    liu 想瑠_スーツ_にっこり "哈哈哈，也许是这样吧"

    # nil 「コラーゲン中毒のお兄ちゃんのために、お土産を買いました。」
    "我给胶原蛋白上瘾的哥哥买了特产"

    # nil 「そうこうしてるうちに、我が家の前に到着。」
    "说着说着，就到了我家门口"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ほい到着。忘れ物は金目の物だけにしておいてくれよ」
    voice "voice/想瑠/sol_a1_0107.ogg"
    liu 想瑠_スーツ_ほほえみ "欸——到了。要忘东西的话就留下值钱的东西吧"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「じゃぁこの宇宙食の袋おいてくね」
    voice "voice/真冬/maf_a1_0218.ogg"
    dong 真冬_制服_基本_無表情 "那么把这个太空食品的袋子放在这里吧"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「わあい燃えないゴミ。想瑠にゃん燃えないゴミ大好き！　ってならねぇからな、ゴミは持ち帰れよ」
    voice "voice/想瑠/sol_a1_0108.ogg"
    liu 想瑠_スーツ_ニヤリ "哇，不可燃垃圾。想瑠喵最喜欢不可燃垃圾了! 把垃圾带回去吧"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「じゃぁ貴様を持ち帰ってやろうか」
    voice "voice/真冬/maf_a1_0219.ogg"
    dong "那就把你这家伙带回去吧"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「女性を誘う台詞にしてはワイルド過ぎるよ…しかもゴミ扱いじゃねぇか私…」
    voice "voice/想瑠/sol_a1_0109.ogg"
    liu 想瑠_スーツ_ぶわ "对于邀请女性的台词来说太狂野了......而且还把我当垃圾看待......"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「くすっ。想瑠にゃん、送ってくれてありがとね」
    voice "voice/真冬/maf_a1_0220.ogg"
    dong 真冬_制服_基本_微笑み "嘿嘿，想瑠喵，谢谢你送我"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「お安い御用でさぁ。じゃ、お兄ちゃんとお幸せにな」
    voice "voice/想瑠/sol_a1_0110.ogg"
    liu 想瑠_スーツ_ほほえみ "小事一桩，祝你和欧尼酱幸福"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うん。頑張る」
    voice "voice/真冬/maf_a1_0221.ogg"
    dong 真冬_制服_基本_微笑み "嗯，我会努力的"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「想いは言葉にしなきゃ相手に伝わらないぜ？　アディオスセニョリータ」
    voice "voice/想瑠/sol_a1_0111.ogg"
    # liu 想瑠_スーツ_ニヤリ "如果不把想法用语言表达出来的话，是无法传达给对方的哦？再见，小姐（L:Adiós Senorita，西班牙语）"
    if persistent.luckykeeperSay == "shutup":
        liu 想瑠_スーツ_ニヤリ "如果不把想法用语言表达出来的话，是无法传达给对方的哦？再见，小姐"
    else:
        liu 想瑠_スーツ_ニヤリ "如果不把想法用语言表达出来的话，是无法传达给对方的哦？再见，小姐（L:Adiós Senorita，西班牙语）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「アディオス、アミーゴ」
    voice "voice/真冬/maf_a1_0222.ogg"
    # dong 真冬_制服_基本_微笑み "再见，伙计（L:Adiós Amigos，也是西班牙语）"
    if persistent.luckykeeperSay == "shutup":
        dong 真冬_制服_基本_微笑み "再见，伙计"
    else:
        dong 真冬_制服_基本_微笑み "再见，伙计（L:Adiós Amigos，也是西班牙语）"

    # 场景切换
    # 天空->葛城家外
    # 人物：真冬（真冬视角）
    # BGM：无
    scene 自宅_夕 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「玄関先で想瑠にゃんを見送ります。」
    "在玄关目送想瑠喵"

    # nil 「車庫を除くと、お兄ちゃんのバイクが無い事に気づきました。」
    "瞄了眼车库，发现欧尼酱的摩托车不见了"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「（出かけてるのかな…）」
    show 真冬_制服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0223.ogg"
    dong 真冬_制服_基本_無表情 "（是出去了吗…）"

    # nil 「遠くに行ってはいないのでしょうけど、少し寂しくなりました。」
    "虽然知道你没去很远的地方，但是有点寂寞了呢"

    # 场景切换
    # 葛城家外->葛城家客厅
    # 人物：真冬（真冬视角）
    # BGM：bgmtwentyfour

    play music bgmtwentyfour fadeout 3.0 fadein 0.8
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene リビングa_夕 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ただいまー」
    show 真冬_制服_基本_微笑み at love69_center with dissolve
    voice "voice/真冬/maf_a1_0224.ogg"
    dong 真冬_制服_基本_微笑み "我回来了~"

    # nil 「遠くに行ってはいないのでしょうけど、少し寂しくなりました。」
    "果然，哥哥没有在家"

    # nil 「換気扇が回っている事に気づきました。朝、換気し忘れて家を出てきたので、きっとお兄ちゃんがスイッチを入れたのでしょう。」
    "我注意到换气扇叶在旋转，因为早上忘记开换气扇就出门了，欧尼酱一定是打开了换气扇的开关吧"

    # nil 「常識的に考えれば、当然の行為ですが、後に帰ってくる私の事を考えて…と妄想してしまうぐらい、末期症状です。」
    "从常识上来考虑，这是理所当然的行为，但是想到欧尼酱考虑到晚回来的我的时候...我就不由得开始幻想...看来已经到晚期了呢"

    # nil 「邪な考えは、夏の太陽のせいにしてしまおうって郷も歌っていましたし、きっと夏の太陽のせいです。」
    # "镇上的人现在在唱歌捏，把所有邪恶的想法都归咎于夏日的阳光吧（L:前面莲回来的时候也说到这个了捏）。一定是因为夏天的太阳"
    if persistent.luckykeeperSay == "shutup":
        "镇上的人现在在唱歌捏，把所有邪恶的想法都归咎于夏日的阳光吧。一定是因为夏天的太阳"
    else:
        "镇上的人现在在唱歌捏，把所有邪恶的想法都归咎于夏日的阳光吧（L:前面莲回来的时候也说到这个了捏）。一定是因为夏天的太阳"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「だがしかし、暑い」
    show 真冬_制服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0225.ogg"
    dong 真冬_制服_基本_無表情 "但是真的是，很热捏"
    hide 真冬_制服_基本_微笑み

    # nil 「換気扇は回っていましたが、暑いものは暑いのです。」
    "虽然换气扇在旋转，但是现在该是很热的时候所以还是非常热捏"

    # nil 「私一人しか家にいないのに、エアコンをかけるのはエコ的な視点でも電気代的な視点でもアレなので、なんとかしのぎましょう。」
    "因为只有我一个人在家，开空调无论是从环保的角度还是电费的角度来看都是不大好，所以还是想办法忍耐一下吧"

    # 真冬 「と、いうこーとーで…せいっ」
    show 真冬_制服_基本_目閉じ at love69_center with dissolve
    voice "voice/真冬/maf_a1_0226.ogg"
    dong 真冬_制服_基本_目閉じ "那、这么说来的话…嘿！"
    hide 真冬_制服_基本_無表情

    hide 真冬_制服_基本_目閉じ
    show 真冬_裸yシャツ_基本_無表情 at love69_center
    with dissolve
    # nil 「制服を脱いで下着姿になりました。」
    "脱下制服穿上了内衣"

    # nil 「そして、ブラを外して、洗濯物が折りたまれてる所から、お兄ちゃんのＹシャツを失敬しました。」
    "然后我脱下胸罩，从叠衣服的地方搞来了欧尼酱的衬衫"

    # 真冬 「くんくん…うん、お兄ちゃんの匂い…」
    show 真冬_裸yシャツ_基本_まったり at love69_center with dissolve
    voice "voice/真冬/maf_a1_0227.ogg"
    dong 真冬_裸yシャツ_基本_まったり "嗅嗅…嗯，欧尼酱的味道……"
    hide 真冬_裸yシャツ_基本_無表情

    # nil 「最初は単に「楽だから」という理由で、去年あたりからこっそりお兄ちゃんのＹシャツを借りてたのですが。」
    "最初只是因为「穿起来很轻松舒适」的原因，从去年开始偷偷地穿起了欧尼酱的衬衫"

    # nil 「なんだか、お兄ちゃんに包まれてる気がして、心が温かくなります。」
    "总觉得被欧尼酱包围着，心里变得暖暖的"

    # nil 「そんな幸せ気分でソファーに寝っ転がって、セミの声に耳を傾けています。」
    "怀着这样的幸福心情躺在沙发上，倾听蝉鸣"

    # nil 「リピートされる音をずっと聞いていると、どうしても考え事に頭がまわってしまいます。」
    "像这样一直听着重复的声音的话，很快就会因为思考问题而烦恼"

    # nil 「考える事と言えば、心愛ちゃんのほっぺたの感触についてか、お兄ちゃんの事についてです。」
    "说到思考的事，大概就是关于心爱酱的脸颊的触感吧，还有关于欧尼酱的事情"

    # 真冬 「心愛ちゃん…まふ」
    voice "voice/真冬/maf_a1_0228.ogg"
    dong 真冬_裸yシャツ_基本_まったり "心爱酱……嘛呼"

    # nil 「自分のほっぺたを両手で押して、（E）・ω・（ヾ）こんな感じになってみます。」
    "用双手按压自己的脸蛋，（E）・ω・（ヾ）试着变成这样的感觉"

    # 真冬 「まふまふまふまふ」
    voice "voice/真冬/maf_a1_0229.ogg"
    dong 真冬_裸yシャツ_基本_まったり "嘛呼嘛呼嘛呼嘛~"

    # nil 「私は何をやっているのでしょうか。」
    "我在做什么捏"

    # nil 「ただ、今回の件で発見したことは、ほっぺたを押されると、確かに「まふ」と鳴るようです。今度お兄ちゃんにもやってみましょう。」
    "不过，在这件事上我的发现是，当按压脸颊的时候，确实会发出「嘛呼」的声音。下次也在欧尼酱身上试试吧"

    # 真冬 「良い触り心地でした」
    show 真冬_裸yシャツ_基本_目閉じ at love69_center with dissolve
    voice "voice/真冬/maf_a1_0230.ogg"
    dong 真冬_裸yシャツ_基本_目閉じ "触感很好捏"
    hide 真冬_裸yシャツ_基本_まったり

    # nil 「お兄ちゃんに向ける感情とは少し路線が違いますが、心愛ちゃんに対しても、一線を越えた感情を抱いているようです。」
    "虽然和对欧尼酱的感情路线有点不同，但是我对心爱酱也有着超越界限的感情"

    # nil 「見ていると子犬というか、何らかの小動物みたいに可愛くて、つい、じゃれついてみたくなる。そんな可愛い生き物です。」
    "看着就像小狗，或者是某种小动物一样可爱，不知不觉就想和它玩耍，就是那样可爱的生物"

    # nil 「支配欲をくすぐります。」
    "激起了支配欲呢"

    # nil 「もっと…触れてみたい…。」
    "想更多地…摸摸…"

    # 真冬 「私、その気があるのかな…まぁ、いけど」
    show 真冬_裸yシャツ_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0231.ogg"
    dong 真冬_裸yシャツ_基本_無表情 "我是不是有这个意思呢……嘛，不管了"
    hide 真冬_裸yシャツ_基本_目閉じ

    # nil 「心愛ちゃんは、一線を越えても許してくれそう。」
    "心爱酱的话，即使越过了界线，也会原谅我的吧"

    # nil 「なんて。」
    "天啊"

    # 真冬 「まったく罪作りな季節ですね…夏ってやつは」
    show 真冬_裸yシャツ_基本_微笑み at love69_center with dissolve
    voice "voice/真冬/maf_a1_0232.ogg"
    # dong 真冬_裸yシャツ_基本_微笑み "真是个造孽的季节啊…夏天这家伙"
    dong 真冬_裸yシャツ_基本_微笑み "真是个罪孽深重的季节啊…夏天这家伙"
    hide 真冬_裸yシャツ_基本_無表情

    # nil 「いつか、心愛ちゃんを襲ってみようかと思います。」
    "我想，总有一天，会袭击心爱酱的吧"

    # nil 「さて、お兄ちゃん。」
    "那么，欧尼酱"

    # 真冬 「むー…どうすればいのかなー…」
    show 真冬_裸yシャツ_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0233.ogg"
    dong 真冬_裸yシャツ_基本_無表情 "emmm——…该怎么办才好呢……"
    hide 真冬_裸yシャツ_基本_微笑み

    # nil 「携帯電話を取りだして、前みたいに着信を連射してやろうかと思い立ちましたが、やっとの思いで我慢します。」
    "我想把手机拿出来，像之前那样不停地打电话过去，但最后还是忍住了"

    # nil 「そして、代わりに心愛ちゃん宛にアプリからメールを送ります。」
    "然后，取而代之，通过app发送电子邮件给心爱酱"

    # 真冬 「ぶち犯したい…と」
    show 真冬_裸yシャツ_基本_目閉じ at love69_center with dissolve
    voice "voice/真冬/maf_a1_0234.ogg"
    # dong 真冬_裸yシャツ_基本_目閉じ "想强暴..."
    dong 真冬_裸yシャツ_基本_目閉じ "想侵犯你..."
    hide 真冬_裸yシャツ_基本_無表情

    # nil 「すると、一瞬で『既読』マークがついて、返信が来ました。」
    "然后，一瞬间就有了『已读』标记，我收到了回复"

    # nil 「『マジすか』」
    "『真的吗?』"

    # 真冬 「うん」
    show 真冬_裸yシャツ_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0235.ogg"
    dong 真冬_裸yシャツ_基本_無表情 "嗯"
    hide 真冬_裸yシャツ_基本_目閉じ

    # nil 「『はい』」
    "『彳亍』"

    # nil 「しまった、やりとりが終わった。まぁ、実際こんなもんですよと。」
    "糟了，对话就这么结束了。嘛，实际上就是这样"

    # nil 「携帯を放り出して、天井を見上げると、昨日取り付けたシーリングファンがゆっくりと回っているのが見えます。」
    "放下手机，仰望天花板，就能看到昨天安装的吊扇在缓缓转动"

    # nil 「お兄ちゃん相手に、もう少し直接的なアピールが出来たらいんですけど…。」
    "以哥哥为对象，如果能更直球一点的话就好了…"

    # nil 「寝起きの耳ペロは、正直かなり勇気が要りました。マニュアル通りとはいえ、実際に行うのは緊張するものです。」
    "说实话，早上起床的耳朵pr需要相当大的勇气。虽说是按照手册来做的，但实际上去做的时候还是会很紧张的"

    # nil 「でも、今でも少しだけ、お兄ちゃんの耳の感触が、舌に残っているような気がします。」
    "但是，即使是现在，我觉得欧尼酱耳朵的触感还残留在舌头上"

    # 真冬 「押し倒してくれてもいのに」
    show 真冬_裸yシャツ_基本_目閉じ at love69_center with dissolve
    voice "voice/真冬/maf_a1_0236.ogg"
    dong 真冬_裸yシャツ_基本_目閉じ "明明可以推倒我的"
    hide 真冬_裸yシャツ_基本_無表情

    # nil 「ぼそっと本音が口からこぼれます。」
    "悄悄地说出真心话"

    # nil 「でも、私は知っています。」
    "但是，我知道"

    # nil 「お兄ちゃんは、良くも悪くも優しいので、『私が求めない限り押し倒さない』そういう人なのです。」
    "欧尼酱不管是在好的方面还是不好的方面都很温柔，是『只要我不要求就不会把我推倒』的人"

    # nil 「双子だと、そういう所がわかってしまう辺り不便だなとも思います。」
    "如果是双胞胎的话，这一点真是很不方便呢"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「『想いは言葉にしなきゃ相手に伝わらないぜ？』」
    voice "voice/想瑠/sol_a1_0112.ogg"
    liu 想瑠_スーツ_ニヤリ "『如果不把想法用语言表达出来的话，是无法传达给对方的哦』"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ごもっともですよ、先生」
    show 真冬_裸yシャツ_基本_微笑み at love69_center with dissolve
    voice "voice/真冬/maf_a1_0237.ogg"
    dong 真冬_裸yシャツ_基本_微笑み "你说得对，老师"
    hide 真冬_裸yシャツ_基本_目閉じ

    # nil 「別れ際の台詞をフラッシュバック。伝えれば、きっと…。」
    "脑海闪回和想瑠再见时候的话。如果能够传达的话，一定…"

    # 真冬 「まふ」
    show 真冬_裸yシャツ_基本_まったり at love69_center with dissolve
    voice "voice/真冬/maf_a1_0238.ogg"
    dong 真冬_裸yシャツ_基本_まったり "嘛呼……"
    hide 真冬_裸yシャツ_基本_微笑み

    # nil 「真冬です。」
    "现在是真冬视角"

    # nil 「考え事をしてたら何だか眠くなってきてしまいました。」
    "当我在想这些事情的同时，开始感到困倦了呢"

    # nil 「セミの声が、フェードアウトしていきます。」
    "蝉的声音，渐渐淡出"

    # 真冬 「…すー…すー…まふ…」
    show 真冬_裸yシャツ_基本_居眠り at love69_center with dissolve
    voice "voice/真冬/maf_a1_0239.ogg"
    dong 真冬_裸yシャツ_基本_居眠り "…哈—…哈—…嘛呼…"
    hide 真冬_裸yシャツ_基本_まったり

    # 原地tp（真冬睡了一觉）
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene リビングa_夕 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 真冬 「…あう…喉かわいた…」
    show 真冬_裸yシャツ_基本_目閉じ at love69_center with dissolve
    voice "voice/真冬/maf_a1_0240.ogg"
    dong 真冬_裸yシャツ_基本_目閉じ "…啊…口渴了…"

    # nil 「起きました。」
    "醒了过来"

    # nil 「オレンジ色の傾いた陽光が、窓から直射日光となって顔面に降り注ぎます。」
    "橙色倾斜的阳光从窗户直射下来，照射到脸上"

    # nil 「不用意に昼寝をすると、やたらと喉が渇くのはなんとかならないのでしょうか。」
    "不小心打了个盹，醒来的时候，喉咙就会很干，有什么解决口渴的好招捏？"

    # nil 「それどころか、水分不足で頭痛がします。」
    "而且，我现在开始因为水分不足而头痛了"

    # nil 「アイスとか無いのかな…。」
    "没有像冰淇淋这样的东西吗…"

    # nil 「小さい頃は、チューペット的なアイスを凍らせてストックしていたのですが、年を経るごとに、その風習は失われていきました。」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%81%E3%83%A5%E3%83%BC%E3%83%9A%E3%83%83%E3%83%88
    # "当我还是个小孩子的时候，我们经常囤积脆脆冰（L:原文是チューペット（前田产业，1935年创立）的なアイス（类似国内的脆脆冰，是一种饮料，装在和脆脆冰一样的塑料容器里面，可以和脆脆冰一样冻起来再吃）），但随着时间的推移，这个习惯就渐渐地消失了"
    if persistent.luckykeeperSay == "shutup":
        "当我还是个小孩子的时候，我们经常囤积脆脆冰，但随着时间的推移，这个习惯就渐渐地消失了"
    else:
        "当我还是个小孩子的时候，我们经常囤积脆脆冰（L:原文是チューペット（前田产业，1935年创立）的なアイス（类似国内的脆脆冰，是一种饮料，装在和脆脆冰一样的塑料容器里面，可以和脆脆冰一样冻起来再吃）），但随着时间的推移，这个习惯就渐渐地消失了"

    # nil 「ダメもとで冷凍室をあけてみました。」
    "试着打开冷冻室开始寻找"

    # 真冬 「おや、こいつは…」
    show 真冬_裸yシャツ_基本_ジト目 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0241.ogg"
    dong 真冬_裸yシャツ_基本_ジト目 "哦呀，这个是…"
    hide 真冬_裸yシャツ_基本_目閉じ

    # nil 「有りました。見たことのない銘柄ですが、カップに入ったアイスクリームです。」
    "有了。虽然是没见过的牌子，但它是杯装的冰淇淋"

    # 真冬 「らぶぽーしょん…しくすてぃないん…」
    show 真冬_裸yシャツ_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0242.ogg"
    dong 真冬_裸yシャツ_基本_無表情"LOVEPOTION……SIXTYNINE……"
    hide 真冬_裸yシャツ_基本_ジト目

    # nil 「蓋のロゴには、そう書いてあります。」
    "盖子的标志上是这样写的"

    # nil 「きっと、お兄ちゃんの物なんでしょう。」
    "肯定，是欧尼酱的东西吧"

    # 真冬 「我慢我慢…」
    show 真冬_裸yシャツ_基本_目閉じ at love69_center with dissolve
    voice "voice/真冬/maf_a1_0243.ogg"
    dong 真冬_裸yシャツ_基本_目閉じ "忍耐忍耐…"
    hide 真冬_裸yシャツ_基本_無表情

    # nil 「その誘惑は圧倒的でした。」
    "但是诱惑是压倒性的"

    # nil 「我ながら理性で感情を抑え込むのは得意な方だと思っていた物の、視線はもうアイスに釘付け。」
    "我认为是擅长用理性压抑感情的那类人，但是我的视线已经被冰淇淋牢牢吸引住了"

    # nil 「冷蔵庫の蓋を閉めても、すぐに開けてしまいます。」
    "关上了冰箱门，又马上打开"

    # nil 「蓋を開けては、閉める。」
    "打开了冰箱门，又关上"

    # nil 「開けては、閉める。」
    "打开、关上"

    # nil 「そんな空中戦を凡そ1分間繰り広げた後、私の頭の中に、ある考えが浮かびます。」
    "在这样激烈的空战展开的大约1分钟后，我的脑海中浮现出了一个想法"

    # 真冬 「食べた後、急いでもっと高いアイスを買ってくれば良いかな…」
    show 真冬_裸yシャツ_基本_まったり at love69_center with dissolve
    voice "voice/真冬/maf_a1_0244.ogg"
    dong 真冬_裸yシャツ_基本_まったり "吃完之后，马上去买更贵的冰淇淋就好了…"
    hide 真冬_裸yシャツ_基本_目閉じ

    # nil 「それなら、最初から高いアイスを買いに行けよ。っていう意見もあるとは思いますが、アイスを買いに行く活力があれば行っています。」
    "“那就一开始就去买更贵的冰淇淋啊喂！”我知道有人会这么说，但如果我还有活力去买冰淇淋，我会去的"

    # nil 「瀬戸際まで迫った交渉は、理性よりも、受け身を覚えた衝動が勝利を収めました。」
    # 参考资料：https://ja.wikipedia.org/wiki/%E7%80%AC%E6%88%B8%E9%9A%9B%E6%94%BF%E7%AD%96
    # "在边缘政策的压力下（L:原文“瀬戸際まで迫った交渉は”，边缘政策是指在冷战时期用来形容一个近乎要发动战争的情况，也就是到达战争边缘，从而说服对方屈服的一种战略术语），比起理性，身体的冲动获得了胜利"
    if persistent.luckykeeperSay == "shutup":
        "在边缘政策的压力下，比起理性，身体的冲动获得了胜利"
    else:
        "在边缘政策的压力下（L:原文“瀬戸際まで迫った交渉は”，边缘政策是指在冷战时期用来形容一个近乎要发动战争的情况，也就是到达战争边缘，从而说服对方屈服的一种战略术语），比起理性，身体的冲动获得了胜利"

    # 真冬 「お兄ちゃんごめん。そして、頂きます」
    show 真冬_裸yシャツ_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0245.ogg"
    dong 真冬_裸yシャツ_基本_無表情 "欧尼酱对不起，然后，我要恰了"
    hide 真冬_裸yシャツ_基本_まったり

    # nil 「食べると決意したからには、急いで食べてしまわねばなりません。」
    "既然决定要吃，就得赶快吃完"

    # nil 「食器入れからスプーンを取り出して、蓋を開けて、一気に大さじ一杯頂きます。」
    "从餐具盒中取出勺子，打开盖子，一口气恰了一大勺"

    # 真冬 「まふ…ん…あ、美味し…」
    show 真冬_裸yシャツ_基本_まったり at love69_center with dissolve
    voice "voice/真冬/maf_a1_0246.ogg"
    dong 真冬_裸yシャツ_基本_まったり "嘛呼…嗯…啊，好吃…"
    hide 真冬_裸yシャツ_基本_無表情

    # nil 「あまりのおいしさに感動しました。それと同時に、何か、とても温かい気持ちが胸の中に膨らんでいきます。」
    "我被它的美味感动了。与此同时，某种非常温暖的感觉在我心中膨胀起来"

    # 真冬 「あれ…？　ドキドキする…」
    show 真冬_裸yシャツ_基本_微笑み at love69_center with dissolve
    voice "voice/真冬/maf_a1_0247.ogg"
    dong 真冬_裸yシャツ_基本_微笑み "啊咧……？dokidoki的……"
    hide 真冬_裸yシャツ_基本_まったり

    # nil 「鼓動が高鳴っていくのを感じます。でも、不愉快な感じではなく。とても、優しくて温かい。」
    "我感觉到了心跳的声音。但是，不是不愉快的感觉。非常温柔温暖"

    # 真冬 「んむ…あむ」
    show 真冬_裸yシャツ_基本_まったり at love69_center with dissolve
    voice "voice/真冬/maf_a1_0248.ogg"
    dong 真冬_裸yシャツ_基本_まったり "嗯…啊"
    hide 真冬_裸yシャツ_基本_微笑み

    # nil 「ゆっくり食べたいという気持ちもありましたが、スプーンは矢継ぎ早にアイスクリームを私の口に運んでいきます。」
    "虽然也有着想要慢慢吃的心情，但是勺子一个接一个不停地把冰淇淋送到嘴里"

    # nil 「アイスが喉を通る度に、ひんやりとした食感と、ふわりと温かい幸福感に包まれていきます。」
    "每次冰淇淋通过喉咙，都会被清凉的口感和温暖的幸福感包围"

    # nil 「そして…。」
    "然后…"

    # nil 「アイスを食べきった瞬間、」
    "吃完冰淇淋的瞬间"

    # 真冬 「あいらぶゆー…だよ、お兄ちゃん」
    show 真冬_裸yシャツ_基本_微笑み2 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0249.ogg"
    dong 真冬_裸yシャツ_基本_微笑み2 "I love you哦—…欧尼酱"
    hide 真冬_裸yシャツ_基本_まったり

    # nil 「そんな言葉が口から零れました。」
    "这样的话从嘴里说出来了"

    # 同时：摩托车刹车音
    play sound "voice/effect/15_ブレーキ2.ogg"
    pause 2.0

    # 真冬 「げ」
    show 真冬_裸yシャツ_基本_見下し at love69_center with dissolve
    voice "voice/真冬/maf_a1_0250.ogg"
    dong 真冬_裸yシャツ_基本_見下し "额"
    hide 真冬_裸yシャツ_基本_微笑み2

    # nil 「聞き慣れた排気音が聞こえてきます。お兄ちゃんのご帰宅です。」
    "听到已经听惯了的排气声，是欧尼酱回来了"

    # nil 「嬉しさがこみ上げるのと同時に、計算が崩れた焦りも感じます。」
    "在感到高兴的同时，也有着计策失败的焦虑"

    # 真冬 「えーと…えーとえーと…」
    show 真冬_裸yシャツ_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0251.ogg"
    dong 真冬_裸yシャツ_基本_無表情 "那—个…那个那个…"
    hide 真冬_裸yシャツ_基本_見下し

    # nil 「とりあえず、アイスの空容器の蓋を閉めて冷凍室にしまうと、急いで玄関に向かいます。」
    "我先把空的冰淇淋杯的盖子盖上，放进冷冻室，然后快速走向玄关"

    # nil 「ごまかそう。　大義名分はそんな感じでしたが、それよりも、もっと強い感情がこの胸にありました。」
    "先蒙混过关吧，从冠冕堂皇的理由来看是这样的，但在我心中，有着更为强烈的感情"

    # nil 「その想いは…私の恐怖と躊躇いを忘れさせてくれる程に。」
    "那种感觉... 足以让我忘记我的恐惧和犹豫"

    # nil 「お兄ちゃんに近づきたい。」
    "我想接近欧尼酱"

    # 真冬 「あ、服…いや、もう。なんとかなるっしょ」
    show 真冬_裸yシャツ_基本_目閉じ at love69_center with dissolve
    voice "voice/真冬/maf_a1_0252.ogg"
    dong 真冬_裸yシャツ_基本_目閉じ "啊，衣服...不，已经没事了，总会有办法的"
    hide 真冬_裸yシャツ_基本_無表情

    # nil 「着替え忘れた私のその服装は、流石にちょっと恥ずかしかったのですが…。」
    "忘记换衣服了，穿着这身衣服总觉得有点不好意思..."

    # nil 「でも、頑張ります。」
    "但是，我会努力的"

    # nil 「真冬です。」
    "真冬参上"

    # scene04 场景3 【奇奇怪怪的冰淇淋又被人恰了，这次是真冬！】 结束
    # Scene04 结束！

    # 过场：真冬（校服）

    # 隐藏 quick_menu
    $ quick_menu = False

    play sound "voice/effect/moosehead honk (stinger).ogg"
    play music bgmfifty fadeout 4.0 fadein 4.0 # 针对这里BGM的特点需要把 Scene05 的 BGM 提前到 Scene04 脚本的尾巴这里写，并增大 fadeout/in 的间隔
    image bg アイキャッチ真冬 = "images/bg/アイキャッチ真冬.png"
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)
    scene アイキャッチ真冬 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)

    $ renpy.pause(1.5, hard=True)
    $ renpy.end_replay()

    jump scene05

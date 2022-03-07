# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene09 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：
# 版本 0.5 "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年3月7日

# 当前流程：编写脚本AIO Process

label scene09:
    # scene09 开始

    # scene09 场景1 【终于到了面对修罗场的时候了呢】 开始

    # 地点：真冬房间
    # 人物：真冬
    # BGM：无

    image bg 真冬部屋_夜_消灯 = "images/bg/真冬部屋_夜_消灯.png"

    scene 真冬部屋_夜_消灯 at love69_bg1440 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)

    # 显示 quick_menu
    $ quick_menu = True

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ん…ぁ…」
    ## 没有中断
    voice "voice/真冬/maf_a1_0779.ogg"
    dong 真冬_制服_基本_居眠り "嗯…呼…"

    # nil 「真冬です。」
    "现在是真冬视角"

    # nil 「変な時間に起きました。」
    "我在奇怪的时间醒来了"

    # nil 「どうやら、本を読んでたら寝落ちをかましてしまったらしいです。」
    "好像是，看着看着书就睡着了"

    # 真冬 「あれ…私…」
    voice "voice/真冬/maf_a1_0780.ogg"
    dong 真冬_制服_基本_居眠り "啊咧…我…"

    # nil 「こんなに準備して寝てたっけ。」
    "我不记得上一次我睡得这么香是什么时候了"

    # nil 「掛け布団はしっかり全身にかけられているし、枕もとに置いてある例のマニュアルは栞のような紙が挟んであります。」
    "被子被紧紧地盖在身上，放在枕边的那本手册夹着一张像书签一样的纸"

    # nil 「しかも、スマフォも充電コード差し込まれてるし…。電気も消えてるし。」
    "而且，智能手机也插上了充电线…电灯也关上了"

    # nil 「スマフォのバックライトを頼りに、マニュアルに挟んであるメモ用紙を読む。」
    "借助智能手机的背光，阅读手册中夹着的留言"

    # nil 「『冷蔵庫にお土産のケーキが入ってます。食べちゃっていですよ。兄。それと、お腹は冷やさないように』」
    "『冰箱里有一个给你的蛋糕，可以去恰，哥哥留。还有，别让肚子着凉了』"

    # 真冬 「おにいちゃん…」
    show 真冬_制服_基本_まったり at love69_center with dissolve
    voice "voice/真冬/maf_a1_0781.ogg"
    dong 真冬_制服_基本_まったり "欧尼酱……"

    # nil 「恐らく、私が風邪を引かないように気を遣ってくれたのでしょう。そう考えるだけで、胸の中に温かい気持ちが広がっていきました。」
    "恐怕是为了不让我感冒，你很用心了呢。只是想到这里，温暖的心情就在心中蔓延开来"

    # nil 「あ、こんなにも私、お兄ちゃんに…。」
    "啊，这样的我，对欧尼酱……"

    # 真冬 「お礼…しなくちゃ…」
    show 真冬_制服_基本_微笑み at love69_center with dissolve
    voice "voice/真冬/maf_a1_0782.ogg"
    dong 真冬_制服_基本_微笑み "不道谢……是⑧行的捏……"
    hide 真冬_制服_基本_まったり

    # nil 「特に何と言って考えてはいないけど…。」
    "虽然没什么特别的想法…"

    # nil 「起きてるかな？」
    "你还醒着吗？"

    # nil 「私はベッドから降りて、向かい側のお兄ちゃんの部屋へと向かいます。」
    "我从床上下来，向对面欧尼酱的房间走去"

    # 场景切换： 真冬房间->葛城家二楼玄关
    image bg 自宅二階廊下_夜_消灯 = "images/bg/自宅二階廊下_夜_消灯.png"
    scene 自宅二階廊下_夜_消灯 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「ドアの下の隙間から、光が漏れてます。どうやら電気はついているようです。」
    "光线透过门下的缝隙照在外面，看起来灯还亮着"

    # 真冬 「……！」
    show 真冬_制服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0783.ogg"
    dong 真冬_制服_基本_無表情 "……！"

    # nil 「そして、何やら二人分の人の声がドアの向こうから聞こえます。二人とも聞き慣れた声です。」
    "然后，从门的对面传来了两个人的声音，，两个人的声音都是我熟悉的"

    # nil 「でも、二人とも普段は聞かないような…そんな声と吐息です。」
    "但是，两个人的声音都是平时不会听到的……那样的声音和呼吸声"

    # nil 「全身がゾクゾクと震えはじめます。胸に広がっていた温かい気持ちが、一気に凍り付いた恐怖へと豹変します。」
    "全身开始颤抖。在胸口蔓延着的温暖的心情，一下子变成了冰冻的恐怖"

    # nil 「もう、確かめなくてもわかります。」
    "即使，不要去确认也知道了"

    # nil 「でも…。」
    "但是……"

    # nil 「そっと、ゆっくりドアを開けました。　」
    "轻轻地，慢慢地打开了门"

    # 真冬 「…っ！」
    show 真冬_制服_基本_見下し3 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0784.ogg"
    dong 真冬_制服_基本_見下し3 "……啊！"
    hide 真冬_制服_基本_無表情

    # nil 「私が、ドアの隙間から見たのは…。」
    "我从门缝里看到的是…"

    # nil 「幸せそうに繋がる、お兄ちゃんと心愛ちゃんでした。」
    "欧尼酱和心爱酱两个人，幸福地联系在一起"

    # nil 「私は、なんとか、二人に気づかれずにドアを閉めました。」
    "我轻轻地关上门，没让他们两个注意到"

    # 真冬 「私は…私は…なんてことを…」
    voice "voice/真冬/maf_a1_0785.ogg"
    dong 真冬_制服_基本_見下し3 "我……我……怎么会这样……"

    # nil 「足は力なく折れて、私は床に座り込みます。」
    "失去了支撑自己站立的力气，一屁股坐到了地板上"

    # nil 「吐き気がこみ上げて、口を覆います。」
    "恶心的感觉向上直冲，我不由得捂住了嘴"

    # nil 「私はただ、お兄ちゃんに幸せになって欲しかった。」
    "我，只是希望欧尼酱能够幸福"

    # nil 「なのに、ただ、お兄ちゃんを求めて…。」
    "但是，只是，只想要欧尼酱……"

    # nil 「心愛ちゃんとお兄ちゃんが結ばれていた事がショックだったんじゃない。」
    "心爱酱和欧尼酱结合的事情让我大为震惊"

    # nil 「二人が結ばれている事を知らずに、お兄ちゃんを求めてしまった。」
    "我不知道他们两个人的事情，就去追求欧尼酱了"

    # 真冬 「私…本当になんてことを…」
    show 真冬_制服_基本_号泣 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0786.ogg"
    dong 真冬_制服_基本_号泣 "我…到底是怎么回事…"
    hide 真冬_制服_基本_見下し3

    # nil 「お兄ちゃんにも、心愛ちゃんにも、最低な事をしてしまった。」
    "无论对欧尼酱，还是对心爱酱，都是做了最糟糕的事情呢"

    # nil 「本来なら、両手をあげて祝福出来る事だったはずなのに…。」
    "本来，我是可以举起双手祝福他们的…"

    # 场景切换
    # 葛城家二楼走廊->葛城家客厅
    image bg リビングa_夜_消灯 = "images/bg/リビングa_夜_消灯.png"
    scene リビングa_夜_消灯 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「ふらふらと立ち上がって、リビングに向かいます。」
    "摇摇晃晃地站起来，朝客厅走去"

    # nil 「気持ちを落ち着けるために、冷蔵庫を開ける。」
    "为了让心情平静下来，打开冰箱"

    # 真冬 「…っ！」
    show 真冬_制服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0787.ogg"
    dong 真冬_制服_基本_無表情 "……！"

    # nil 「冷蔵庫には、白い紙箱が目立つ位置に置かれていました。」
    "冰箱里，一个白色的纸盒放在非常显眼的位置"

    # 真冬 「やだ…やだよ…こんなの…」
    # 从这儿附近开始真冬酱的麦就有点问题了呢，稍微收录了一些线路噪声进去
    show 真冬_制服_基本_号泣 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0788.ogg"
    dong 真冬_制服_基本_号泣 "讨厌…讨厌啊…这样的…（L:从这句话附近开始，真冬酱的麦就有点问题了呢，稍微收录了一些线路噪声进去，原版如此）"

    # nil 「もし、知らなかったら、このケーキはきっと幸せに食べれたのかな…。」
    "如果，刚才的事情都不知道的话，这个蛋糕一定会幸福地吃下去吧…"

    # nil 「私はゆっくり紙箱を取り出して、蓋を開けます。」
    "我慢慢地取出纸盒，打开盖子"

    # nil 「中に入っていたのは、生クリームとラズベリーのソースであしらわれたチョコレートケーキでした。」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%A8%E3%83%BC%E3%83%AD%E3%83%83%E3%83%91%E3%82%AD%E3%82%A4%E3%83%81%E3%82%B4
    "里面是一个用新鲜奶油和覆盆子酱做成的巧克力蛋糕（L:覆盆子就是一般意义上说的树莓，国内又叫红桑子、野草莓、蛇头莓、桑莓等）"

    # 真冬 「うわ…うわあ…」
    voice "voice/真冬/maf_a1_0789.ogg"
    dong 真冬_制服_基本_号泣 "哇…哇啊——…"

    # nil 「私は、泣きました。」
    "我哭了"

    # nil 「泣きながら、お土産のケーキにスプーンを伸ばします。」
    "一边哭，一边把勺子伸向特产蛋糕"

    # nil 「もう涙が止まりません。」
    "眼泪止不住了"

    # nil 「大好きなのに。」
    "明明最喜欢你"

    # nil 「私は、二人のことが、大好きなのに…。」
    "我对，两个人都，最喜欢了…"

    # nil 「真冬です。」
    "我是真冬"

    # nil 「私は…。」
    "我……"

    # nil 「私は…。」
    "我……"

    # nil 「これから、どうすれば…。」
    "接下来，我该怎么办呢…"

    # 场景切换
    #   葛城家客厅（夜）->莲卧室
    # 视角切换
    #   真冬 -> 莲
    # BGM：bgm13
    # 人物： 心爱 莲

    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 自室a_朝 at love69_bg1620 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    play music bgmthirteen

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「むにゃ…この壺は高く売れる…ふにゃー…」
    # 这里的心爱也没有小对话框头像捏，原作就是逊啦，咱给补上
    ## 913-1044 跳过
    voice "voice/心愛/cca_a1_1045.ogg"
    ai 心愛_下着_基本_まふまふ "呼喵——………这个罐子卖得很好…呼呜…"

    # 画面震动，可参考 scene01 的实现
    scene black
    show 自室a_朝:
        zoom 0.89
        xalign 1.1
        yalign 0.5
        linear 0.05 xalign 0.1 yalign 0.1
        pause 0.05
        linear 0.05 xalign -0.1 yalign -0.1
        pause 0.05
        repeat
    # 动画结束，回归原先的
    # repeat 0.1s后回归正常
    pause 0.1
    scene 自室a_朝 at love69_bg1620

    # 莲 「がばぁっ！」
    lian "哇啊啊！"

    # 心爱 「はうあっ！？」
    # 这里的心爱上的是HS的小头像呢，得换！各位lsp对不住了！！
    voice "voice/心愛/cca_a1_1046.ogg"
    ai 心愛_下着_基本_ポカーン "哈哇啊！"

    # nil 「飛び起きた。」
    "跳起来了"

    # nil 「時計を見る。午前6時。やばい、真冬が起こしにくる。」
    "看了眼表。早上6点。糟了，真冬要来叫我起床了"

    # 心爱 「びっ…びっくりしたなーもー！　結構良いところだったのに！」
    # 这里的心爱上的也是HS的小头像呢，得换！各位lsp对不住了！！
    voice "voice/心愛/cca_a1_1047.ogg"
    ai 心愛_下着_基本_驚き "欸……吓了我一跳！真是的！本来睡得挺好的来着！"

    # 莲 「心愛、起きろ。服着るぞ！　今日は月曜日だ！」
    lian "心爱，快起床，穿衣服！今天是星期一！"

    # 心爱 「へ！？　へ！？　あ！」
    # 这里的心爱上的也是HS的小头像呢，得换！各位lsp对不住了！！
    voice "voice/心愛/cca_a1_1048.ogg"
    ai 心愛_下着_基本_驚き "嗯！？嗯！？啊！"

    # nil 「俺達は昨日の夜、お互いの身体を何度か貪った後、翌朝の事も考えずに眠ってしまったようだ。」
    "昨天晚上，我们贪婪地吞噬了对方的身体好几次之后，似乎连第二天早上的事想都没想就睡着了"

    # 心爱 「ほいパンツとシャツとズボン！」
    # 这里的心爱终于可以放出来了，上面的就按照这里的来换吧
    show 心愛_下着_基本_驚き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1049.ogg"
    ai 心愛_下着_基本_驚き "嘿！胖次和衬衫还有裤子！"

    # nil 「早くも下着姿まで服を着ていた心愛が、タンスの中から俺のパンツを投げてくる。」
    "早就穿着内衣的心爱从衣柜里扔过来了我的衣服"

    # 莲 「ハイビスカス…またかよ…これだから女子は」
    lian "扶桑花…又来了……这就很女孩子味儿呢"

    # 心爱 「四の五の言ってないの！　さっさとそいつを隠しなさいな！」
    # 参考资料：https://gogen-yurai.jp/shinogonoiu/
    # 参考资料：https://www.weblio.jp/content/%E5%9B%9B%E3%81%AE%E4%BA%94%E3%81%AE%E8%A8%80%E3%82%8F%E3%81%AA%E3%81%84
    voice "voice/心愛/cca_a1_1050.ogg"
    ai 心愛_下着_基本_驚き "不要说这说那了！快把这家伙藏起来！（L:前半句原文「四の五の言ってないの！」四の五の言的说法起源于江户时代中期的骰子赌博游戏，也有来自四书五经的说法，意思是对某件事情抱怨，感兴趣的可以去自行Yahoo~）"

    # 莲 「そいつ呼ばわりかよ。昨夜は好き好き言ってたじゃねぇか」
    lian "你管它叫这家伙？昨天晚上不是还说了喜欢吗？"

    # 心爱 「二度と余計な事を喋らせるな」
    show 心愛_下着_基本_覚醒3 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1051.ogg"
    ai 心愛_下着_基本_覚醒3 "别让我和你再废话第二遍！"
    hide 心愛_下着_基本_驚き

    # 莲 「すんませんでした」
    lian "对不起"

    # nil 「俺が心愛から受け取ったトランクスをはくのに凡そ３秒。」
    "穿上我从心爱那里扔过来的胖次只要大约3秒"

    # nil 「その間に、心愛は制服姿に着替えていた。」
    "与此同时，心爱换上了制服"

    # 莲 「っていうかお前の制服がうちにあんだよ」
    lian "话说，我家为啥会有你的制服啊？"

    # 心爱穿上制服

    # 心爱 「こんな事もあろうかと、仕込んでおいたのだ！」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1052.ogg"
    ai 心愛_制服_基本_真顔 "因为我早就料到会发生这样或者那样的事情嘛！"
    hide 心愛_下着_基本_覚醒3

    # 莲 「計画的犯行かよ…」
    lian "你这是有预谋的犯罪啊……"

    # nil 「とりあえず、制服に着替えました。」
    "总之，换上了制服"

    # nil 「とりあえずこれで、昨夜の痕跡は消しました。あとは適当に言い訳を考えるだけです。」
    "总之，这样就消除了昨晚的痕迹，剩下的只是随便想个借口"

    # nil 「ただ、少しだけ腑に落ちませんでした。」
    "只是，我有一点想不明白"

    # nil 「隠し事をする事で、真冬を間接的に傷付けてしまう気がして…。」
    "我觉得像这样隐瞒事实，感觉会间接伤害了真冬……"

    # nil 「でも、そうしたら、心愛にも正直に、真冬との事を話さなければ…。」
    "但是，如果不这样的话，就必须对心爱说实话，告诉她我和真冬的事情…"

    # nil 「俺はまだ、少し決意をしきれていなかった。」
    "我还没有下定决心"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 自室a_朝 at love69_bg1620 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # nil 「30分経過。」
    "30分钟后"

    # 心爱 「来ないね真冬ちゃん」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1053.ogg"
    ai 心愛_制服_基本_泣き "没有来呢，真冬酱"

    # 莲 「おかしいな…あいつに限って寝坊する事はないとおもうんだが…」
    lian "好奇怪啊…我觉得只有她是不会睡过头的……"

    # 心爱 「うーん。部屋覗いてみようかな」
    voice "voice/心愛/cca_a1_1054.ogg"
    ai 心愛_制服_基本_泣き "嗯。去她的房间看看吧"

    # 莲 「俺がいくわ」
    lian "我去吧"

    # 心爱 「はーい。じゃぁ私、リビング行ってるね！」
    show 心愛_制服_基本_笑顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1055.ogg"
    ai 心愛_制服_基本_笑顔 "好——的。那我的话，就先去客厅啦！"
    hide 心愛_制服_基本_泣き

    # 场景切换：莲卧室->葛城家二楼走廊（朝）
    image bg 自宅二階廊下_昼 = "images/bg/自宅二階廊下_昼.png"
    scene 自宅二階廊下_昼 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「心愛と同時に部屋を出て、俺は真冬の部屋を、心愛は階段へと向かっていった。」
    "我和心爱同时离开了房间，我走向真冬的房间，心爱向楼梯走去"

    # 场景切换：葛城家二楼走廊（朝）->真冬卧室
    image bg 真冬部屋_朝 = "images/bg/真冬部屋_朝.png"
    scene 真冬部屋_朝 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「ガチャッ」
    "嘎吱嘎吱"

    # 莲 「おいおい真冬ちゃん、今日はお兄ちゃんが起こし…あれ、いねぇでやんの」
    lian "哦呀哦呀真冬酱，今天是欧尼酱来叫你起床哦~……咦，你没在啊？"

    # nil 「ドアを開けると、既に部屋はもぬけの殻で、夏風に揺れるカーテンが寂しく、宙を漂っていた。」
    "打开门一看，房间里已是空空如也，只有夏风中摇曳的窗帘寂寞地在空中飘浮"

    # 心爱 「『おーい蓮くーん！』」
    # 这里原作用了引号，但是不是电话或者引用的句子其实不需要的，所以就不加了
    ## 还是加上把，这里是心爱在一楼向二楼喊，尊重原作
    voice "voice/心愛/cca_a1_1056.ogg"
    ai 心愛_制服_基本_驚き "『喂——莲君！』"

    # nil 「階下から心愛の呼び声が聞こえる。」
    "楼下传来心爱的呼唤声"

    # nil 「俺は真冬の部屋のドアを開けっ放しにしたまで、急いで部屋から飛び出した。」
    "我连真冬房间的门都没顾上关，就急忙跑了出去"

    # 场景切换：真冬卧室->葛城家客厅
    image bg リビングa_朝 = "images/bg/リビングa_朝.png"
    scene リビングa_朝 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「俺がリビングに到着すると、メモ用紙を持って立ち尽くす心愛がいた。」
    "我一到客厅，就看到了拿着便条纸站着的心爱"

    # 莲 「どったの先生」
    lian "怎么啦，老师？（L:这里莲的说法是「どったの先生」，最开始真冬叫莲起床也是这么说的）"

    # 心爱 「ウサギちゃんは既に家を出てるみたいだよ」
    show 心愛_制服_基本_無表情 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1057.ogg"
    ai 心愛_制服_基本_無表情 "小兔子好像已经出门了呢"

    # 莲 「なんやて」
    lian "你在说什么啊"

    # 心爱 「ほら」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1058.ogg"
    ai 心愛_制服_基本_真顔 "你看嘛"
    hide 心愛_制服_基本_無表情

    # nil 「心愛が俺に、メモ用紙を手渡した。」
    "心爱把便签纸递给了我"

    # nil 「すると、俺が昨日真冬に書き置きしたメモ用紙に、文章が書き足されていた。」
    "于是，我发现昨天给在真冬留下的便签纸上面被加上了一句话"

    # nil 「『お土産のケーキとても美味しかったです。それと、お布団と携帯の充電もありがとうございました。ちょっと急用で先に出ます。」
    "『特产蛋糕很好吃。还有，谢谢你给我盖上被子还有给手机充电。有点急事我就先走了"

    # nil 「ごめんね。ご飯は良かったら食べて下さい。ＰＳ．玄関に心愛ちゃんの靴があったので、心愛ちゃんの分も作っておきました』」
    "对不起啦。如果可以的话回头我请吃饭。PS.门口有心爱酱的鞋子，所以也准备了心爱酱的份』"

    # nil 「テーブルの上には、二人分のところてんと生ハムサラダが盛りつけてあった。」
    "桌子上摆着两人份的凉粉和火腿沙拉"

    # nil 「だが、自分の分の食器を片付けた痕跡はなく…。」
    "但是，没有清理真冬自己那份餐具的痕迹……"

    # 莲 「あいつ…自分は飯食わず、俺たちの分作っていったのかよ…」
    lian "那家伙…自己没吃饭，只做了我们的份吗…"

    # 心爱 「ぶわあ…まふまふちゃん、なんて良い子なの…」
    show 心愛_制服_基本_ぶわー at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1059.ogg"
    ai 心愛_制服_基本_ぶわー "呜哇…嘛呼嘛呼酱，你真是个好孩子啊…"
    hide 心愛_制服_基本_真顔

    # 莲 「おいおい泣くな泣くな。涙の塩気がところてんに入っちゃうぞ」
    lian "喂喂，不要哭。眼泪的咸味进到沙拉里面的"

    # 心爱 「だってぇ…と、とりあえずお礼のリプライ飛ばしとくよ…」
    voice "voice/心愛/cca_a1_1060.ogg"
    ai 心愛_制服_基本_ぶわー "但是啊……总是先回复一句谢谢吧……"

    # 莲 「直接言えよ」
    lian "直接说出来就行"

    # nil 「席に座って、二人で手を合わせる。」
    "坐在座位上，两个人双手合十"

    # 心爱 「イタダキマス！」
    show 心愛_制服_基本_ペコちゃん at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1061.ogg"
    ai 心愛_制服_基本_ペコちゃん "我开动啦！"
    hide 心愛_制服_基本_ぶわー

    # 莲 「いただきます」
    lian "我开动了！"

    # 心爱 「もぐもぐ…もぐもぐ…うみゃい」
    show 心愛_制服_基本_もぐもぐ at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1062.ogg"
    ai 心愛_制服_基本_もぐもぐ "咕嘟咕嘟…咕嘟咕嘟…唔喵"
    hide 心愛_制服_基本_ペコちゃん

    # 莲 「…？　あ、あ…そうだな…美味しいな」
    lian "…？嗯…嗯……是啊…真好吃啊"

    # 心爱 「もぐもぐ」
    voice "voice/心愛/cca_a1_1063.ogg"
    ai 心愛_制服_基本_もぐもぐ "嗯嗯"

    # 莲 「（おかしいな…真冬にしては、塩気が強い…心境の変化か？）」
    lian "（好奇怪啊……就真冬的口味来说，咸味很重…是心境的变化吗？）"

    # scene09 场景1 【终于到了面对修罗场的时候了呢】 结束
    # scene09 场景2 【不知道如何开口而渐行渐远的三人】 开始

    # 场景切换：葛城家客厅->学校教室
    # BGM：sweet passion.ogg
    # 人物：心爱 莲 女学生A 花盆君

    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 教室_昼 at love69_bg1220 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    play music bgmfourteen fadeout 1.0 fadein 4.0

    # nil 「学校にて。」
    "在学校"

    # 心爱 「まっふまふちゃーん！」
    show 心愛_制服_基本_にっこり at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1064.ogg"
    ai 心愛_制服_基本_にっこり "嘛呼嘛呼酱~——！"

    # 女学生A 「心愛ちゃんおはよ。残念だけど真冬ちゃんまだ来てないよ」
    # 记得要去更新人物表(wsa->woman student A)，这里的女学生A的声音感觉是里昂CV配的捏
    # 原来demo版已经定义过了，也是wsa，233333
    voice "voice/その他/ot1_a1_0002.ogg"
    wsa "心爱酱早上好~虽然很遗憾但是真冬酱还没来呢"

    # 心爱 「えー！　今朝のお礼ついでに私の噛んだガムあげようかと思ったのに！」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1065.ogg"
    ai 心愛_制服_基本_泣き "欸——！我本来想今天早上来向你道谢的，顺便把我嚼过的口香糖给你的！"
    hide 心愛_制服_基本_にっこり

    # 女学生A 「嫌がらせじゃない…あれ、葛城くん、真冬ちゃんと一緒じゃないの？」
    voice "voice/その他/ot1_a1_0003.ogg"
    wsa "这不是骚扰嘛……啊嘞，葛城君，你今天不是和真冬酱一起的吗？"

    # 莲 「それがだなー真冬の奴、用事があるとかで先出たはずなんだが…」
    lian "整个嘛——真冬这家伙，应该是有事先走了……"

    # 女学生A 「なら、先生と一緒じゃないかな？」
    voice "voice/その他/ot1_a1_0004.ogg"
    wsa "那么，应该就是和老师在一起吧"

    # 心爱 「そだね。想瑠にゃん来るまで待ってみよう。車で来るまで」
    show 心愛_制服_基本_笑顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1066.ogg"
    ai 心愛_制服_基本_笑顔 "是啊。那就等想瑠喵过来吧，应该是开车过来的"
    hide 心愛_制服_基本_泣き

    # 莲 「うるせえ」
    lian "无路赛"

    # 女学生A 「笑えよ」
    voice "voice/その他/ot1_a1_0005.ogg"
    wsa "笑一个"

    # 莲 「はい」
    lian "好~"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 教室_昼 at love69_bg1220 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 定义花盆君在右的参数
    transform love69_huapen_right:
        zoom 0.89
        xalign 0.808
        yalign -18.0

    # 这个语句是针对花盆君设计的参数，能够调整花盆君在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.15
    $ sideimagesize.SideImageYalign = 1.21
    $ sideimagesize.SideImageZoom = 0.5

    # 花盆君 「…」
    show 花盆君_通常 at love69_huapen_right with dissolve
    voice "voice/アシュリー/ash_a1_0034.ogg"
    # 29-33 跳过
    pen 花盆君_通常 "......"

    # 莲 「……」
    lian "……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「……」
    show 心愛_制服_基本_泣き at love69_xinai_left with dissolve
    voice "voice/心愛/cca_a1_1067.ogg"
    ai 心愛_制服_基本_泣き "……"

    # 这个语句是针对花盆君设计的参数，能够调整花盆君在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.15
    $ sideimagesize.SideImageYalign = 1.21
    $ sideimagesize.SideImageZoom = 0.5

    # 花盆君 「…（ふりふり）」
    voice "voice/アシュリー/ash_a1_0035.ogg"
    pen 花盆君_通常 "......（摇摆摇摆）"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「想瑠にゃん来ないから自習だってさ」
    voice "voice/心愛/cca_a1_1068.ogg"
    ai 心愛_制服_基本_泣き "说是想瑠喵不来改成自习了"

    # 莲 「真冬も来なかったな」
    lian "真冬也没有来啊"

    # 心爱 「ね…はぁー…直接お礼言えなかったなー…」
    voice "voice/心愛/cca_a1_1069.ogg"
    ai 心愛_制服_基本_泣き "啊…哈啊——…没能直接道谢啊……"

    # 莲 「電話しとけば？」
    lian "打个电话吧"

    # 心爱 「そうするー」
    voice "voice/心愛/cca_a1_1070.ogg"
    ai 心愛_制服_基本_泣き "就这么办吧"

    # nil 「結局、その日一日、学園で真冬と担任の姿を見る事はなかった。」
    "在结果，那天一整天，都没有在学校看到过真冬和班主任的身影"

    # 场景切换：学校教室内->葛城家客厅
    # BGM：Slide the Way
    # 人物：莲 真冬
    play music bgmthirtysix fadeout 2.0 fadein 4.0
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=True, alpha=True, time_warp=None)
    scene リビングa_夜 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=True, alpha=True, time_warp=None)

    # nil 「その夜。」
    "是夜"

    # 莲 「ふむ…やはり牛乳は200ミリだな…」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%9F%E3%83%AA
    lian "嗯……果然牛奶是200milli（毫）啊……（L:原作如此，应该是200ml（毫升），但是莲只说了一半）"

    # nil 「俺は一人、リビングでミロと牛乳の絶妙な配分を調べながら、真冬の帰りを待つこと、午後11時。」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%8D%E3%82%B9%E3%83%AC%E3%83%BB%E3%83%9F%E3%83%AD
    "我独自坐在客厅里，试图找出Milo（L:一种由瑞士雀巢公司出品的奶类饮料，含有巧克力和麦芽成分，最早是1934年澳洲人托马斯研发）和牛奶的完美组合，等待真冬归来，现在是晚上11点"

    # nil 「何度か携帯をチェックするも、メールの返信も来ないし、ＳＮＳでも動いていない。」
    "我检查了好几次手机，没有回复短信，在SNS上也没有消息"

    # nil 「心愛から『まふまふちゃん電話でないー』とのメールが届いていた。」
    "从心爱那里收到了『真冬没有接电话呢——』的短信"

    # nil 「真冬の事だから、単に携帯を触ってないだけだろうが…。」
    "因为是真冬，所以可能只是碰巧没看手机而已…"

    # 莲 「…うむ、出来た、出来たぞ！！！」
    lian "……欸，找到啦、找到啦！！！"

    # nil 「ガチャンッ」
    "哐当一声"

    # nil 「ついに黄金比を見つけたその瞬間、自宅の玄関の扉が開いた。」
    "终于在找到黄金配比的那一瞬间，家里的大门打开了"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ただいまー…」
    show 真冬_制服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0790.ogg"
    dong 真冬_制服_基本_無表情 "我回来啦——……"

    # 莲 「お、おかえり真冬。良かったちょっと心配してたんだぞ。メールもかえさねぇし」
    lian "欢、欢迎回来真冬。太好了，我都有点担心了，发的短信也没回"

    # 真冬 「あ、あ、う、うん…ごめん、お兄ちゃん、ちょっと忙しくて…」
    voice "voice/真冬/maf_a1_0791.ogg"
    dong 真冬_制服_基本_無表情 "啊，啊，嗯、嗯……对不起，欧尼酱，我有点忙……"

    # 莲 「そんなに素直に謝られてもな…。疲れてるみたいだな…ほら、お兄ちゃんが完璧なミロを作ったから飲みなさい」
    lian "即使你那么坦率地道歉……你看起来好像很累啊…来，欧尼酱做了完美的Milo，快来喝吧"

    # 真冬 「うん…ありがと…」
    voice "voice/真冬/maf_a1_0792.ogg"
    dong 真冬_制服_基本_無表情 "嗯……谢谢……"

    # nil 「真冬は心底疲れているようで、目に生気がこもっておらず、弱々しく俺からミロの入ったグラスを受け取ると、」
    "真冬似乎真的很累，眼睛里毫无生气，虚弱地从我手中接过装着Milo的玻璃杯"

    # nil 「こくこくと喉を鳴らして飲み干した。」
    "咕咚咕咚地全部喝掉了"

    # 莲 「どうよ」
    lian "怎么样？"

    # 真冬 「うん…美味しいね…。ごめん、お兄ちゃん…私、疲れてるから…寝る…ね
    show 真冬_制服_基本_目閉じ at love69_center with dissolve
    voice "voice/真冬/maf_a1_0793.ogg"
    dong 真冬_制服_基本_目閉じ "嗯……很美味呢……对不起，欧尼酱……我，累了……去睡觉…了……"
    hide 真冬_制服_基本_無表情

    # 莲 「お、おう…」
    lian "哦，哦…"

    # nil 「真冬は淡々と靴を脱いで玄関をあがり、俺の横を通り過ぎていく。」
    "隆冬淡然地脱鞋走上玄关，从我身旁走过"

    # 莲 「あ、そうだ、心愛からだが…」
    lian "啊，对了，有心爱打来的……"

    # nil 「ピクッと真冬の身体が跳ねて、真冬は立ち止まった。」
    "真冬的身体突然跳了一下，停了下来"

    # 真冬 「…何？」
    show 真冬_制服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0794.ogg"
    dong 真冬_制服_基本_無表情 "……啥"
    hide 真冬_制服_基本_目閉じ

    # 莲 「今朝のご飯、ありがとう。凄く美味しかったよ。まふまふちゃん大好き…だとさ」
    # 这里反而没加引号，很奇怪捏，按照本作的惯例，加上引号
    lian "『今天早上的饭，谢谢你啦，味道非常好呢，我最喜欢嘛呼嘛呼酱了』这样的"

    # 真冬 「…そっか。じゃぁ『ありがとう。私も心愛ちゃん大好き。それと、電話出れなくてごめんね』って伝えといて」
    show 真冬_制服_基本_目閉じ at love69_center with dissolve
    voice "voice/真冬/maf_a1_0795.ogg"
    dong 真冬_制服_基本_目閉じ "…这样啊。那『谢谢。我也最喜欢心爱酱了。还有，没能接电话对不起』就这样告诉她吧"
    hide 真冬_制服_基本_無表情

    # 莲 「仲良いよなお前ら。ていうか直接言えよ」
    lian "你们关系这么好啊。直接和她这么说呗"

    # 真冬 「そうする…じゃぁ、お兄ちゃん、おやすみ」
    show 真冬_制服_基本_無表情 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0796.ogg"
    dong 真冬_制服_基本_無表情 "就这么办吧…那么，欧尼酱，晚安"
    hide 真冬_制服_基本_目閉じ

    # 莲 「あ…おやすみ。ゆっくり休めよ。しばらく起きてるから、何かして欲しい事とかあったら声かけてくれ」
    lian "啊…晚安，好好休息吧，我已还过一会睡，如果有什么需要我帮忙的事情的话就喊我一声"

    # 真冬 「…うん。ありがと」
    show 真冬_制服_基本_目閉じ at love69_center with dissolve
    voice "voice/真冬/maf_a1_0797.ogg"
    dong 真冬_制服_基本_目閉じ "…嗯，谢谢"
    hide 真冬_制服_基本_無表情

    # nil 「真冬はそれ以上何も言わず、無言で階段を上っていった。」
    "隆冬没再说什么，只是默默地走上楼梯"

    # 莲 「本当に疲れてんだな…そっとしておいてやるか…」
    lian "你真的很累啊…我就不打扰你了……"

    # 场景切换：葛城家客厅->学校教室
    # BGM：honky tonk saloon (pad)（bgm13）
    # 人物： 莲 心爱
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 教室_昼 at love69_bg1220 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    play music bgmthirteen fadeout 1.0 fadein 4.0

    # nil 「その日以来、真冬は毎朝、早く家を出て、毎晩遅く帰ってくる日々が続いた。」
    "从那天以来，真冬每天早上都早早出门，每天晚上很晚才回家"

    # nil 「それでも真冬は毎朝俺の朝食を律儀に作ってくれている。」
    "尽管如此，真冬还是每天早上都按时给我做早饭"

    # nil 「だが、少なくとも、俺と真冬のコミュニケーションの機会は確実に激減していた。」
    "但至少，我和真冬交流的机会确实锐减了"

    # nil 「毎朝の書き置きには毎回、「ごめんね」のワードが書き込まれている。」
    "每天早上的便签纸上都会写上『对不起』的字样"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はぁぅー…」
    show 心愛_制服_基本_泣き at love69_xinai_left with dissolve
    voice "voice/心愛/cca_a1_1071.ogg"
    ai 心愛_制服_基本_泣き "哈呜——…"

    # 莲 「今日も居ないのか」、真冬」<-原版如此，括号打多了
    lian "今天也不在吗？真冬"

    # 心爱 「まふまふちゃんに会いたいよー」
    voice "voice/心愛/cca_a1_1072.ogg"
    ai 心愛_制服_基本_泣き "嘛呼嘛呼酱我好想见你啊——"

    # 这个语句是针对花盆君设计的参数，能够调整花盆君在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.15
    $ sideimagesize.SideImageYalign = 1.21
    $ sideimagesize.SideImageZoom = 0.5

    # 花盆君 「…（ふるふる）」
    show 花盆君_通常 at love69_huapen_right with dissolve
    voice "voice/アシュリー/ash_a1_0036.ogg"
    pen 花盆君_通常 "......（颤抖颤抖）"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ねー、植木鉢くんも真冬ちゃんいなくて寂しいもんねー」
    voice "voice/心愛/cca_a1_1073.ogg"
    ai 心愛_制服_基本_泣き "害——花盆君看不到真冬酱也很寂寞啊"

    # 莲 「寂しいな…」
    lian "好寂寞啊…"

    # nil 「真冬が俺達の生活から居なくなった事で、心愛も急速に元気を失っていった。」
    "随着真冬从我们的生活中消失，心爱也迅速失去了活力"

    # 莲 「ほら、チョコ食うか」
    lian "来，要吃巧克力吗"

    # 心爱 「食べる…」
    voice "voice/心愛/cca_a1_1074.ogg"
    ai 心愛_制服_基本_泣き "吃…"

    # 莲 「早く真冬が落ち着くといな」
    lian "希望真冬快点安定下来"

    # 心爱 「うん…」
    voice "voice/心愛/cca_a1_1075.ogg"
    ai 心愛_制服_基本_泣き "嗯……"

    # 这个语句是针对花盆君设计的参数，能够调整花盆君在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.15
    $ sideimagesize.SideImageYalign = 1.21
    $ sideimagesize.SideImageZoom = 0.5

    # 花盆君 「…（じー）」
    voice "voice/アシュリー/ash_a1_0037.ogg"
    pen 花盆君_通常 "......（哈——）"

    # nil 「心愛は寂しげに、空席になってしまった隣の席を眺めた。」
    "心爱寂寞地看着旁边空出来的座位"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 教室_昼 at love69_bg1220 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はー！　ごめん！　蓮くん！　今日バイトあるの忘れてた！　一緒に帰れないや…」
    show 心愛_制服_基本_驚き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1076.ogg"
    ai 心愛_制服_基本_驚き "啊！对不起！莲君！我忘了今天还有打工！不能和你一起回去了……"

    # 莲 「バイト？　例のクマのぬいぐるみに入るやつか？」
    lian "打工？就是钻进那只熊玩偶里面吗？（L:就是前面提到的那个“康起来很没劲的熊玩偶”）"

    # 心爱 「いや、今日は軍艦にスプーンでいくらを盛りつけるバイトだよ」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1077.ogg"
    ai 心愛_制服_基本_真顔 "不，今天是在军舰上用勺子盛装三文鱼子的打工（L:这里说的是军舰寿司）"
    hide 心愛_制服_基本_驚き

    # 莲 「いくらの軍艦限定かよ。他の寿司も作ってやれよ、もしあれなら送っていこうか。ちょっと待ってくれば家からバイク引っ張り出してくるけど」
    # 原文是两句话，这里合并一句
    lian "只限定军舰啊，也做做其他的寿司啊，如果是那样的话我送你去吧，稍等一下，我这就把摩托车从家里整出来"

    # 心爱 「んーん。蓮くんに迷惑かけらんないから大丈夫！」
    show 心愛_制服_基本_笑顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1078.ogg"
    ai 心愛_制服_基本_笑顔 "不了。我不会给莲君添麻烦的，没事的！"
    hide 心愛_制服_基本_真顔

    # 莲 「迷惑とかじゃなくてだな…」
    lian "我不会觉得麻烦的……"

    # 心爱 「ちょっと一人で考え事もしたいから…ごめんね」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1079.ogg"
    ai 心愛_制服_基本_泣き "我想一个人想想事情……对不起"
    hide 心愛_制服_基本_笑顔

    # 莲 「いやいや、まぁ、真冬の事もあるしな…バイト頑張れよ」
    lian "没事没事，嘛，还有真冬的事情啊…那打工加油啊"

    # 心爱 「はーい。ありがと、蓮くん」
    show 心愛_制服_基本_にっこり at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1080.ogg"
    ai 心愛_制服_基本_にっこり "好——谢谢啦，莲君"
    hide 心愛_制服_基本_泣き
    hide 心愛_制服_基本_にっこり with dissolve

    # 莲 「おう」
    lian "嗯"

    # nil 「心愛もやはり、俺と同じように真冬の事で悩んでるのだろうか。」
    "心爱酱果然也是，和我一样在为真冬的事情烦恼吗"

    # nil 「できれば相談して欲しい所だが…。」
    "如果可以的话，我希望你能和我商量一下呢……"

    # 莲 「（それを言ったら俺も心愛に相談してねぇ…な…）」
    lian "（这么说的话我也没和你商量过…的吧…）"

    # nil 「それに、俺自身解決しなければ問題があるはずだ。」
    "而且，我自己不去解决的话肯定不行"

    # 场景切换：学校教室内->街道
    # BGM:I hear now [unreal_dm_-_stay_(for_this_moment)]
    # 人物： 莲

    play music bgmthirtyseven fadeout 1.0 fadein 4.0
    image bg 通学路d_夕 = "images/bg/自宅二階廊下_夜_消灯.png"
    scene 通学路d_夕 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # 莲 「（リオンも、今日は店を出してないのか…）」
    lian "（里昂今天也没有开店吗…）"

    # nil 「久しぶりに会いたいと思ってやってきたが、屋台は出てなかった。」
    "想着很久没见了所以过来了，但是摊子并没有摆出来呢"

    # 画面切换：街道->黄昏天空
    image bg 空_夕b = "images/bg/空_夕b.png"
    scene 空_夕b at love69_bg1440 with dissolve

    # 莲 「（孤独だ…）」
    lian "（孤独啊…）"

    # nil 「俺はバイクに乗りながら、宛もなくただ、ひたすら走り続けていた。」
    "我一个人骑着摩托车，没有目的地，只是一个劲地往前开"

    # nil 「考える事は、真冬の事、心愛の事。そして、これからの事。」
    "思考的事，是真冬的事，还有心爱的事。然后，接下来的事情"

    # nil 「俺の考えでは、真冬と心愛が機嫌の良いときに、勢いで話してしまおうという考えだったが、」
    "我的想法是，在真冬和心爱心情好的时候，趁这样的机会说出来"

    # nil 「それも今では可能性が薄くなってきた。」
    "但是现在这种可能性越来越小了"

    # nil 「単に時間が解決できる問題であればよいのだが…。」
    "如果只是时间能解决的问题就好了…"

    # 莲 「（くそっ…）」
    lian "（该死…）"

    # 场景切换：天空（街道）->海边
    image bg 通学路e_夕 = "images/bg/通学路e_夕.png"
    scene 通学路e_夕 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「思えば、孤独を感じる事なんて無かった。」
    "回顾过去，我从未感到孤独"

    # nil 「ずっと、真冬と心愛と一緒に居て。」
    "一直，都是和真冬和心爱在一起"

    # nil 「それが当たり前だと思っていた。」
    "我以为这是理所当然的"

    # nil 「喧嘩もしたけど、でも、翌日にはケロっと仲直りして。」
    "虽然也有吵架的时候，但是，第二天我们就和好了"

    # nil 「ただ、わからなかった。」
    "只是，我不知道"

    # nil 「真冬は夜に帰ってくるもの、毎日、凄く疲れた様子で、俺は深く聞く事を躊躇っていた。」
    "真冬现在是晚上才回来，每天看起来都很非常疲惫，我犹豫着要不要说这个事儿"

    # nil 「そんな中でも、真冬は毎日朝食を作ってくれる。」
    "在这样的情况下，真冬每天都给我做早饭"

    # nil 「だから、話せない事にイライラするにも、怒りは湧かなかった。」
    "所以，即使我对不能说话感到沮丧，我也不会生气"

    # nil 「真冬…一体どうしたんだ…」
    "真冬…你到底怎么了呢……"

    # nil 「俺は、何故かたどり着いてしまった海に向かってそう呟いた。」
    "我对着不知何故而抵达的大海喃喃自语"

    # 画面切换到街道心爱视角
    # 新BGM解锁

    play music bgmtwentysix fadeout 1.0 fadein 4.0
    image bg 通学路c_夕 = "images/bg/通学路c_夕.png"
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)
    scene 通学路c_夕  at love69_bg1440 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)

    # 心爱 「はぁーあー…なんとかしなくちゃ…」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1081.ogg"
    ai 心愛_制服_基本_泣き "哈啊——哈啊……必须得想办法了……"

    # nil 「私はバイトに向かう途中、ため息をついた。」
    "在去打工的路上，我叹了口气"

    # nil 「真冬ちゃんと接する時間が減って、真冬ちゃんに会えない事と目に見えて元気を失っていく蓮君の姿を見る事で、私のライフゲージは着実に削られていた。」
    "和真冬酱接触的时间减少了，看到了见不到真冬酱的事加上看到失去了精神的莲君的样子，我的生命量表被稳步削减"

    # nil 「それに、当然、キスやそれ以上の事もしなくなってしまったし、好きという言葉を伝える事も無くなってしまった。」
    "而且，当然，我们不再接吻，也不再说喜欢这个词了"

    # nil 「胸にぽっかり穴があいてしまったようで、苦しい。」
    "胸口好像突然裂开了一个洞，很痛苦"

    # nil 「そして、私は真冬ちゃんが蓮くんや私に会わない本当の理由に、薄々感づいていた。」
    "然后，我隐约感受到了真冬不见莲和我的真正理由"

    # 心爱 「恐らく…真冬ちゃんは…」
    voice "voice/心愛/cca_a1_1082.ogg"
    ai 心愛_制服_基本_泣き "恐怕……真冬酱…"

    # nil 「推測の域を出て居ないけど、多分、真冬ちゃんは蓮くんと身体を重ねている。」
    "虽然只是推测，不过，大概，真冬和莲君的身体已经重叠过了"

    # nil 「根拠は、この前蓮君と繋がった時に、布団から真冬ちゃんの香りを感じ取ったから。」
    "根据是，上次和莲君联系在一起的时候，从被子里感觉到了真冬酱的香味"

    # nil 「とはいっても、真冬ちゃんはこの間も添い寝から耳ペロをしてみたりと、頻繁にベッドには出入りしてるのかもしれないけど…。」
    "话虽如此，真冬酱最近也开始陪睡和耳pr，可能频繁出入于莲君的床上…"

    # nil 「ただ、私の直感が「そういうのではない」というのは今になってひしひしと感じている。」
    "只是，我的直觉「不是那样的」到了现在这种感觉非常强烈"

    # nil 「そして、何らかの原因で、私と蓮くんが愛し合っている事を知ってしまった。」
    "然后，因为某种原因，知道了我和莲君相爱的事情"

    # nil 「なので、気分を悪くした真冬ちゃんが、私達から距離を開けるのは当然の事だ。」
    "因此，心情不好的真冬，和我们拉开距离是理所当然的"

    # nil 「恐らく、知ったのはこの前蓮君の家に泊まったとき。」
    "恐怕，是我上次在莲君家过夜的时候知道的"

    # nil 「あの時、本来ならもっと良い選択肢があったはずだ…。」
    "那时候，本来应该有更好的选择…"

    # nil 「だけど、これで蓮君を責めるわけにはいかない。」
    "但我不能因此而责怪莲君"

    # nil 「彼と触れあった２回とも、私から誘っただけで、蓮くんは、その優しさで私を包み込んでくれただけ。」
    "和他接触的两次，都是我主动邀请的，莲君只是用他的温柔包容了我"

    # nil 「その優しさが心地よくて、幸せで。」
    "那份温柔让人心情舒畅，幸福"

    # nil 「大事な経過をすっ飛ばしてる事も忘れてしまいそうだった。」
    "差点忘了，我跳过了最重要的部分"

    # nil 「いや、忘れていたかったのかもしれない。」
    "不，也许只是想忘记而已"

    # nil 「そんな、私の惰性がこんな結果になってしまった。」
    "这样的，我的惰性导致了这样的结果"

    # 心爱 「だけど、後悔していても仕方がない…なんとかしなければ…手遅れになる前に…！」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1083.ogg"
    ai 心愛_制服_基本_真顔 "但是，后悔也不是办法……如果不想办法的话……在为时已晚之前…！"
    hide 心愛_制服_基本_泣き

    # nil 「私は拳をぐっと握りしめる。」
    "我握紧拳头"

    # nil 「あの日、かけてもらった言葉を思い出す。」
    "我想起了那天你对我说的话"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「『諦めなければ、必ず良い結果に辿り着けますよ』」
    ## 没有跳过
    voice "voice/霧葉/krh_a1_0207.ogg"
    dinerowner 店长_私服_目閉じ "『只要不放弃，也一定会有好结果的』"

    # 店长 「『人を好きになるって、素敵な事じゃないですか』」
    voice "voice/霧葉/krh_a1_0208.ogg"
    dinerowner 店长_私服_にっこり "『喜欢上一个人，不是很美妙吗?』"

    # nil 「胸に残ったその言葉が、崩れそうな私の心を、繋ぎ止めた。」
    "残留在心中的那句话，维系着快要崩溃的我的心"

    # 画面切换回海边莲君视角
    # BGM也切换回来

    play music bgmthirtyseven fadeout 1.0 fadein 4.0
    image bg 通学路e_夜 = "images/bg/通学路e_夜.png"
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)
    scene 通学路e_夜  at love69_bg1440 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)

    # nil 「すっかり夜になってしまった。」
    "天已经完全黑了"

    # 动画：CALL
    # 电话声
    # 可以复用scene01啦！

    play sound "voice/effect/14_携帯電話呼び出し音／lp.ogg"
    show screen callscr

    # nil 「ポケットの奥で、携帯が震える。」
    "在口袋里面，手机正在震动"

    # nil 「真冬だろうか。」
    "会是真冬吗"

    # nil 「画面を見ると「一条心愛」の文字が光っている。」
    "看向画面，「一条心爱」的文字闪烁着光芒"

    hide screen callscr
    play sound "voice/effect/18_携帯電話操作音1.ogg"

    # 接电话声
    # 参考 scene01 的实现即可

    # 莲 「心愛か。バイトは終わったのか？」
    lian "是心爱吗？打工结束了吗？"

    # 左下心爱手机小头像，具体实现参考 scene01 真冬电话小头像即可

    # 这个语句是针对电话里的心爱设计的参数，能够调整电话里的心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.04
    $ sideimagesize.SideImageYalign = 1.04
    $ sideimagesize.SideImageZoom = 0.6

    # 心爱 「『うん終わった。さっきはごめんね』」
    voice "voice/心愛/cca_a1_1084.ogg"
    ai 心愛_通話中 "『嗯，结束了。刚才对不起』"

    # 莲 「お、おう。気にするなよ。それで、どうしたんだ？」
    lian "哦，嗯，别在意。那么，怎么了？"

    # 心爱 「『うん。それを伝えたかっただけだよ』」
    voice "voice/心愛/cca_a1_1085.ogg"
    ai 心愛_通話中 "『没什么，我只是想告诉你而已』"

    # 莲 「そうか。今日はお疲れさん」
    lian "是吗？今天辛苦了"

    # 心爱 「『うん…あ、蓮くん蓮くん』」
    voice "voice/心愛/cca_a1_1086.ogg"
    ai 心愛_通話中 "『嗯…啊，莲君莲君』"

    # 莲 「…なんだい？」
    lian "……怎么了？"

    # 心爱 「『最近言えてなかったけど…大好きだよ』」
    voice "voice/心愛/cca_a1_1087.ogg"
    ai 心愛_通話中 "『虽然最近没有说…但是我最喜欢你了』"

    # 莲 「あ…ありがとう」
    lian "啊…谢谢"

    # 心爱 「『私も、蓮くんが元気だせるように頑張るから、辛いときは声…かけてね？』」
    voice "voice/心愛/cca_a1_1088.ogg"
    ai 心愛_通話中 "『我也会为了让莲君打起精神而努力的，痛苦的时候……叫我一声好吗？』"

    # 莲 「わかった。何かあったら頼らせてもらうよ」
    lian "我知道了，如果有什么需要，我会依靠你的"

    # 心爱 「『うん。じゃぁね』」
    voice "voice/心愛/cca_a1_1089.ogg"
    ai 心愛_通話中 "『嗯，再见』"

    play sound "voice/effect/電話／話し中.ogg"

    # nil 「ツーツーツー無機質な機械音だった。」
    "嘟——嘟——嘟——……只剩下无机质的机械音回响"

    # 莲 「（はぁ…）」
    lian "（哈啊…）"

    # nil 「俺は携帯電話をしまうと、海を眺めた。」
    "我收起手机，眺望大海。"

    # nil 「俺は反射的に心愛に「好き」と言い返せなかった事に気づいた。」
    "我反射性地发现了最近没有和心爱说「喜欢你」这样的事情"

    # scene09 场景2 【不知道如何开口而渐行渐远的三人】 结束
    # scene09 场景3 【逐渐意识到真相，努力化解隔阂的二人】 开始

    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 教室_昼 at love69_bg1220 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    play music bgmthirteen fadeout 1.0 fadein 4.0

    # nil 「時間が解決してくれると思っていたが…それはただの甘えだった。」
    "我以为时间能解决问题的……但那只是一厢情愿而已"

    # nil 「金曜日を迎えてしまった。これで、真冬がいない日々を一週間過ごしてしまったことになる。」
    "又到了周五，这样一来，我们已经度过了一个星期没有真冬的日子"

    # nil 「そして、今日は前期授業最終日。つまり、明日から夏休みだ。」
    "然后，今天是前期课程的最后一天。也就是说，明天开始就是暑假了"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「はい、つーことで、やっとこさ、貴様らが楽しみにしていた夏休みに入るわけだが…」
    ## 没有跳过
    show 想瑠_スーツ_見下し at love69_xiangliu_center with dissolve
    voice "voice/想瑠/sol_a1_0139.ogg"
    liu 想瑠_スーツ_見下し "是的，话说回来，终于要进入你们期待已久的暑假了……"

    # nil 「朝のＨＲ。相変わらず、真冬の席は空席のまだった。」
    "早上的HR，和最近一样，真冬的座位还是空着的"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あれ？　想瑠にゃん居るじゃん」
    voice "voice/心愛/cca_a1_1090.ogg"
    ai 心愛_制服_基本_驚き "啊咧？想瑠喵不是在家吗？"

    # 莲 「ほんとだ。流石に、終業式の日に居ないのはまずいと思ったんかね」
    lian "真的啊。果然，是不是觉得结课那天也不在实在是太牙白了吧"

    # 心爱 「まふまふちゃんの事聞いてみよう」
    voice "voice/心愛/cca_a1_1091.ogg"
    ai 心愛_制服_基本_微笑み "我去打听打听嘛呼嘛呼酱的事情吧"

    # 莲 「そうしましょう」
    lian "就这么办吧"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 教室_昼 at love69_bg1220 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「なぁ、アンタ、真冬の事知らないか？」
    lian "嘿，你知道真冬的事情吗？"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「え？　何、君ら喧嘩でもしたの？」
    show 想瑠_スーツ_見下し at love69_xiangliu_right with dissolve
    voice "voice/想瑠/sol_a1_0140.ogg"
    liu 想瑠_スーツ_見下し "欸？怎么了？你们吵架了吗？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あれ？　想瑠にゃんも知らないの？　まふまふちゃんの行方」
    show 心愛_制服_基本_驚き at love69_xinai_left with dissolve
    voice "voice/心愛/cca_a1_1092.ogg"
    ai 心愛_制服_基本_驚き "啊咧？想瑠喵也不知道吗？嘛呼嘛呼酱的去向"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「知らんと言ったら嘘になるけど…うーん、どうしよっかなー」
    voice "voice/想瑠/sol_a1_0141.ogg"
    liu 想瑠_スーツ_見下し "如果说不知道的话是骗人的……嗯，怎么办好呢？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「私は小手先の交渉が嫌いでね…」
    hide 心愛_制服_基本_驚き
    show 心愛_制服_基本_真顔:
        zoom 1.5
        xalign 0.13
        yalign -0.09
        linear 0.3 xalign 0.76
    voice "voice/心愛/cca_a1_1093.ogg"
    ai 心愛_制服_基本_真顔 "我不是一个喜欢小题大做的人……"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「い、痛いってば！　ぎぶ！　ぎぶだよ！　喋るから！」
    voice "voice/想瑠/sol_a1_0142.ogg"
    liu 想瑠_スーツ_見下し "嘿、好疼的啊！give！give up哒哟！我会说的啦！"

    # 莲 「心愛！　頸動脈だけ抑えるのやめろ！」
    lian "心爱！不要再掐着颈动脉了！"

    show 心愛_制服_基本_真顔:
        zoom 1.5
        xalign 0.76
        yalign -0.09
        linear 0.4 xalign 0.13

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ぜぇ…はぁ…君は武力以外での説得を覚えたまえ…。まぁでも、はっきり言って口止めされてるから、言えないよ」
    voice "voice/想瑠/sol_a1_0143.ogg"
    liu 想瑠_スーツ_見下し "哈啊……哈啊…你要学会除了武力以外的说服方法……不过嘛，因为被封口了，所以不能说（L:这里的后半句原版也是没有配音）"

    # 莲 「真冬に？」
    lian "被真冬？"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「うん。どうしてもっていうなら話すけど…。それは真冬ちゃんの気持ちを裏切る事になるよ」
    voice "voice/想瑠/sol_a1_0144.ogg"
    liu 想瑠_スーツ_見下し "嗯，如果你无论如何都要坚持的话我也可以告诉你……但是这等于是背叛了真冬酱的心情"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「真冬ちゃんが、想瑠にゃんを口止めしてまで、秘密にしたい事って…」
    show 心愛_制服_基本_泣き at love69_xinai_left with dissolve
    voice "voice/心愛/cca_a1_1094.ogg"
    ai 心愛_制服_基本_泣き "真冬酱，你让想瑠喵守口如瓶，想要保密的事情是……"
    hide 心愛_制服_基本_真顔

    # 莲 「なら、やはり真冬に直接問い詰めるしかないか…」
    lian "那么，还是只能找到真冬直接问她了吧…"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「うーん…しばらく待ってみればいんじゃないかな。何をそう焦ってるんだい？　別に、いなくなるわけじゃないんだからさ」
    voice "voice/想瑠/sol_a1_0145.ogg"
    liu 想瑠_スーツ_見下し "嗯——……也许稍微等一段时间不久行了吗？你为什么这么着急？又不是说不见了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「うん…。そうなんだけど…。なんだか、このま私達、仲直りしても…大切な物を失ってしまいそうな気がして…」
    voice "voice/心愛/cca_a1_1095.ogg"
    ai 心愛_制服_基本_泣き "嗯……虽然是这个理儿……但是总觉得，就算我们就这样和好了……也会失去重要的东西……"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ふーむ。まぁ、君らの問題に大人の私が関するのは本来良くないんだが…」
    voice "voice/想瑠/sol_a1_0146.ogg"
    liu 想瑠_スーツ_見下し "嗯——嘛，这个是你们的问题了，找我这个成年人解决本来就不大好……"

    # 想瑠 「とはいえ、君ら三人とも、私の大事な生徒だからな、是非とも仲良く幸せにして欲しい。という願いもある」
    voice "voice/想瑠/sol_a1_0147.ogg"
    liu 想瑠_スーツ_見下し "话虽如此，但你们三个都是我最重要的学生，我希望你们能和睦相处，幸福快乐"

    # 想瑠 「なので、一言だけ」
    voice "voice/想瑠/sol_a1_0148.ogg"
    liu 想瑠_スーツ_見下し "那么，我就只说一句"

    # 想瑠 「頑張れ！」
    voice "voice/想瑠/sol_a1_0149.ogg"
    liu 想瑠_スーツ_見下し "加油吧！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ほんとに一言だけかよー！」
    show 心愛_制服_基本_不機嫌 at love69_xinai_left with dissolve
    voice "voice/心愛/cca_a1_1096.ogg"
    ai 心愛_制服_基本_不機嫌 "真的只有一句话啊！"
    hide 心愛_制服_基本_泣き

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「ははははは！　じゃぁなお前ら！　私はこれからハワイ旅行の準備で忙しいんでね！」
    voice "voice/想瑠/sol_a1_0150.ogg"
    liu 想瑠_スーツ_見下し "哈哈哈哈哈！那么再见伙计们！我现在正忙着准备去夏威夷旅行呢！"

    # 莲 「んあ？　アンタもハワイいくの？」
    lian "嗯？你也要去夏威夷吗？"

    # 想瑠 「も？　なんだ、私がハワイいっちゃ悪いのか。ワイハーのゴイスーだぜ」
    # 参考资料：http://monjiro.net/dic/head/34/110525/10/0
    # 参考资料：https://ja.wikipedia.org/wiki/%E6%AD%BB%E8%AA%9E_(%E8%A8%80%E8%AA%9E)
    # 参考资料：https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q1068478850?__ysp=44K044Kk44K544O844GgIOS9lQ%3D%3D
    # 参考资料：https://ja.wikipedia.org/wiki/%E6%AF%9B%E3%81%AE%E7%8E%8B%E5%9B%BD#ゴイスー
    voice "voice/想瑠/sol_a1_0151.ogg"
    liu 想瑠_スーツ_見下し "什么？难道我不该去夏威夷吗？我可是怀哈（L:怀哈是夏威夷，怀哈（Waiha）是泰国苏梅岛的一种死语（就是因为没有人用所以消失的语言）对夏威夷的说法）的戈伊斯（L:音译，漫画鼻毛真拳中毛の王国里面的一个人物）"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「私達も行く予定なんだよー！　蓮君と真冬ちゃんの三人で！」
    show 心愛_制服_基本_笑顔 at love69_xinai_left with dissolve
    voice "voice/心愛/cca_a1_1097.ogg"
    ai 心愛_制服_基本_笑顔 "我们也计划去那里哦！加上莲和真冬酱三个人！"
    hide 心愛_制服_基本_不機嫌

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「向こうじゃ絶対会いたくねぇな…プライベートの私なんか絶対見せないからな…」
    voice "voice/想瑠/sol_a1_0152.ogg"
    liu 想瑠_スーツ_見下し "我绝对不想在那边和你们见面…我绝对不会让别人看到我的私生活…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「やだ！！　見る！！あ、でも…三人で行けるかな…」
    show 心愛_制服_基本_不機嫌 at love69_xinai_left with dissolve
    voice "voice/心愛/cca_a1_1098.ogg"
    ai 心愛_制服_基本_不機嫌 "亚哒！！就要看！！但是……真的能三个人一起去吗……"
    hide 心愛_制服_基本_笑顔

    # 莲 「大丈夫だろ。行けるさ」
    lian "没问题的。会去的"

    # 心爱 「そ、そだね…弱気になってちゃだめだね！」
    show 心愛_制服_基本_にっこり at love69_xinai_left with dissolve
    voice "voice/心愛/cca_a1_1099.ogg"
    ai 心愛_制服_基本_にっこり "是、是啊……可不能气馁啊！"
    hide 心愛_制服_基本_不機嫌

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 想瑠 「その意気だ。アディオス・ファッキン・アミーゴ」
    show 想瑠_スーツ_中指 at love69_xiangliu_right with dissolve
    voice "voice/想瑠/sol_a1_0153.ogg"
    liu 想瑠_スーツ_中指 "就是这种气势。Adiós・fxxking・amigo（又是西班牙语，Adiós=再见，amigo=友人(一般指没有血缘关系的友人)）"
    hide 想瑠_スーツ_見下し
    hide 想瑠_スーツ_中指 with dissolve

    # nil 「先生は、立てた中指を額に当て、ビシッと突きだしてから、教室から出て行った。」
    "老师把竖直的中指放在额头上，砰的一声伸了出来，然后从教室出去了"

    # nil 「俺と心愛は、お互い顔を合せてから、首をかしげた。」
    "我和心爱，面面相觑，歪着脑袋"

    # 莲 「帰るか…」
    lian "回去吗…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    hide 心愛_制服_基本_にっこり

    # 心爱 「そう…だね…真冬ちゃん、いないの寂しいね…」
    show 心愛_制服_基本_笑顔:
        zoom 1.5
        xalign 0.13
        yalign -0.09
        linear 0.3 xalign 0.53
    voice "voice/心愛/cca_a1_1100.ogg"
    ai 心愛_制服_基本_笑顔 "是…啊…真冬酱，你不在我很寂寞呢……"

    # 莲 「そう…だな…。心愛は今日もバイトか？」
    lian "是…啊…心爱今天也要打工吗？"

    # 心爱 「バイトはないんだけど、ちょっとやることがあるかなー」
    voice "voice/心愛/cca_a1_1101.ogg"
    ai 心愛_制服_基本_笑顔 "虽然没有打工，不过有点事情要做呢——"

    # 莲 「そうか…。俺もやろうとしてる事がある」
    lian "是吗……我也有一件事要做"

    # 心爱 「お互いがんばろ！」
    voice "voice/心愛/cca_a1_1102.ogg"
    ai 心愛_制服_基本_笑顔 "彼此加油! "

    # 莲 「あ。頑張ろう」
    lian "啊，加油吧！"

    # nil 「心愛は俺がしようとしてる事をわかっているのかもしれない。」
    "也许心爱知道我要做什么"

    # 场景切换：教室内->街道
    scene 通学路d_昼 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)
    stop music fadeout 4.0

    # nil 「校門で、心愛と別れて、普段の帰り道とは違う道を歩む。」
    "在校门口，和心爱告别，走上了与平时回家的路不同的路"

    # nil 「真冬を探そう。」
    "去寻找真冬吧"

    # nil 「何で今まで思い付かなかったのか。」
    "为什么到现在才想到呢"

    # nil 「念のため真冬に電話もかけるが、とることはなかった。」
    "为了慎重起见先给真冬打了电话，但是没有接"

    # nil 「ならば、まさに『力尽く』で真冬を見つけ出すしかない。」
    "那么，就只能『竭尽全力』来寻找真冬了"

    # nil 「担任が場所を知っているという事は、こから遠くにはいまい。少なくとも、この街にはいるはずだ。」
    "如果班主任知道地点，那么应该离这里不远，至少，应该还是在这个城市"

    # 莲 「…よし、行くか」
    lian "…好，出发吧"

    # nil 「俺は走り出し、真冬がいそうな場所を思い付く限り探す事にした。」
    "我跑起来，尽可能找到真冬可能在的地方"

    # 场景切换：街道->雾叶小店
    # 音效：摩托刹车
    play sound "voice/effect/15_ブレーキ2.ogg"
    scene 霧葉ちゃんのお店 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)
    play music bgmfifteen fadeout 2.0 fadein 2.0

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「真冬ちゃん…？　いやー知らないですねーこ一週間で見てませんよ」
    show 店长_私服_無表情 at love69_wuye_center with dissolve
    voice "voice/霧葉/krh_a1_0209.ogg"
    dinerowner 店长_私服_無表情 "真冬酱……？呀……不知道呢~已经一周没见着她了"

    # 莲 「げ、まじか。一番のヤマだと想ったんだが…」
    lian "额、真的吗？我还以为这里的可能性最大呢……"

    # 店长 「ふむー。そしてせっかく来て貰ってアレなんですが、ちょっと店を開けますね。買い物に行かなきゃなので…」&这里说是要开下店，但是结合语境应该是关下店或者让莲看店，结合下文应该是关下店，怀疑原作打错字了
    show 店长_私服_にっこり at love69_wuye_center with dissolve
    voice "voice/霧葉/krh_a1_0210.ogg"
    dinerowner 店长_私服_にっこり "嗯——你好不容易来一趟，虽然有点那个，但是我得先关下店，得去买东西呢……"
    hide 店长_私服_無表情

    # 莲 「あ、あ、いってらっしゃい」
    lian "啊、嗯，一路顺风"

    # 场景切换：雾叶小店->商店街
    # 音效：摩托刹车
    play sound "voice/effect/15_ブレーキ2.ogg"
    stop music fadeout 2.0
    image bg 商店街_昼 = "images/bg/商店街_昼.png"
    scene 商店街_昼 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # 莲 「こにも居ないか…」
    lian "这里也没有吗…"

    # 场景切换：雾叶小店->商店街
    # 音效：摩托刹车
    play sound "voice/effect/15_ブレーキ2.ogg"
    image bg ロータリー_昼 = "images/bg/ロータリー_昼.png"
    scene ロータリー_昼 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # 莲 「こも…」
    lian "这里也没…"

    # 场景切换：商店街->商店街桥
    image bg 歩道橋_昼 = "images/bg/歩道橋_昼.png"
    scene 歩道橋_昼 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # 莲 「あまりに宛がなさ過ぎるが…探すしかない…」
    lian "虽然有点太没目的了…但是也只能去找了…"

    # 场景切换：商店街桥->葛城家客厅
    # 音效：开门声（不带回音）
    play sound "voice/effect/13_ドア4～あける.ogg"
    scene リビングa_昼 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # 莲 「家にも居ない…か」
    lian "也不在家…吗？"

    # nil 「日が暮れてきた。」
    "天快黑了"

    # nil 「徒歩とバイクを駆使して、あらゆる所を探し回ったが、見つかりそうにない。」
    "我徒步和骑着摩托车到处寻找，但是似乎都没法找到"

    # nil 「家に居れば次第に帰ってくるだろうけど…そういう事じゃないんだよな…」
    "虽然呆在家里也能慢慢等到真冬回来……但是，不能这样的吧……"

    # 莲 「とにかく…手当たり次第に探すしかないか…」
    lian "总之……只能继续去找了吗……"

    # nil 「俺はもう一度家を出て、バイクのエンジンをかけた。」
    "我再一次出门，发动了摩托车的引擎"

    # 场景切换：葛城家客厅->校门口
    # 音效：摩托刹车
    play sound "voice/effect/15_ブレーキ2.ogg"
    image bg 校門_夕 = "images/bg/校門_夕.png"
    scene 校門_夕 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # 莲 「まさか…な…」
    lian "难道……"

    # nil 「そして、俺は何を思ったか学園へたどり着いた。学園には流石にバイクでは入れないので、近くに路駐すると、メットを脱いで、校門をくぐる。」
    "然后，我不知道想到了什么，终于来到了学校。但是毕竟学校是不能骑摩托车进去的，所以在附近停好摩托车，摘下头盔，穿过校门"

    # 场景切换：校门口->教室走廊（黄昏）
    image bg 学校廊下_夕 = "images/bg/学校廊下_夕.png"
    scene 学校廊下_夕 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「もう夏休みに突入してるので、校内には人の姿はほとんど無く、校庭には部活に勤しむ生徒達の姿もない。」
    "已经进入暑假了，所以校园里几乎没有人，也没有忙于社团活动的学生"

    # nil 「俺は階段を登り、不思議な力に吸い込まれるようにいつもの教室へと足を運んでいく。」
    "我登上楼梯，仿佛被一股不可思议的力量吸进去一般，来到了平时的教室"

    # nil 「この感覚はなんだろう。強いて言うならば「双子の直感」だろうか。」
    "这种感觉是什么呢？硬要说的话，应该是「双胞胎的直觉」吧"

    # nil 「カツカツカツと上履きが階段を上る音が、斜陽が差し込む踊り場を響き渡る。」
    "咔嗒咔嗒的室内鞋上楼梯的声音，回荡在夕阳西下的楼道里"

    # nil 「教室のドアがしまっている。普段なら開けっ放しになってるはずだが…。」
    "教室的门关着，但是平时应该是敞开着的…"

    # nil 「微かに、人の気配がする。誰だ。」
    "隐约，感觉到有人的气息，是谁？"

    # nil 「俺はその予感に淡い期待を抱きながら、教室の扉を開けた。」
    "我对这种预感抱着淡淡的期待，打开了教室的门"

    # 场景切换：教室走廊（黄昏）->教室（黄昏）
    image bg 教室_夕 = "images/bg/教室_夕.png"
    scene 教室_夕 at love69_bg1220 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「ガラッ。」
    "哗啦"

    # 莲 「…こんな所にいたのか」
    lian "…原来你在这里啊"

    # nil 「教室に足を踏み入れた俺の視界に入ってきたのは…」
    "踏入教室进入我的视野的是…"

    # 画面切换：教室（黄昏）->真冬
    image bg mcg_02_3 = "images/ev/mcg_02_3.png"
    scene mcg_02_3 with dissolve

    # nil 「教室の窓のサッシに寄りかり、風に髪を靡かせながら、無言で外を眺める真冬の姿だった。」
    "那是真冬的身影，靠在教室的窗框上，头发在风中飘扬，一言不发地向外眺望"

    # nil 「俺は、真冬の頬に流れる一筋の涙を、風に乗って空へと消えていく涙を、見逃しはしなかった。」&翻译稍微调整少翻俺は部分，更加通顺
    "真冬的脸颊上流下了一丝泪水，随风消失在了空中"

    # 莲 「泣いて…いるのか…真冬」
    lian "在哭…是吗……真冬"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「…あっ…おにいちゃ…ん？」
    voice "voice/真冬/maf_a1_0798.ogg"
    dong 真冬_制服_基本_泣き "…啊…欧尼…酱？"

    # nil 「今、俺の存在に気づいたのか、真冬は驚いた表情をこちらに向けた。」
    "也许是现在注意到我的存在了吧，真冬带着吃惊的表情转向了这边"

    # 莲 「心配かけやがって」
    lian "让你担心了"

    # 真冬 「何で…何で…お兄ちゃんがこに？」
    voice "voice/真冬/maf_a1_0799.ogg"
    dong 真冬_制服_基本_泣き "为什么…为什么…哥哥会在这里？"

    # 莲 「そりゃこっちの台詞だ。探したぞこの野郎」
    lian "那是我的台词。我找到你这个野孩子了"

    # nil 「俺は真冬に詰め寄る。自分でも驚く程に、感情の流れをせき止められなかった。」
    "我向真冬逼近。连我自己都感到惊讶，不能阻止感情的流动"

    # nil 「本当はただ、真冬が心配だっただけなのに…つい語気を強く迫ってしまう。」
    "其实，只是担心隆冬而已…但是不知不觉间语气就变得很强烈"

    # 莲 「今までどこをほっつき歩いていたんだよ。心愛も心配してたぞ、帰るぞ」
    lian "到现在为止你都在哪里闲逛呢。心爱也非常担心你，回家吧"

    # 真冬 「うん。もうちょっとこにいる」
    voice "voice/真冬/maf_a1_0800.ogg"
    dong 真冬_制服_基本_泣き "嗯。在稍微在这儿呆一会"

    # 莲 「なぁ、なんか辛い事でもあったのか？俺がもし、お前を悲しませてたなら―」
    lian "呐，是什么事情让你如此痛苦？如果是我让你伤心的话——"

    # 真冬 「うん。お兄ちゃんは私に何もしてないよ。お兄ちゃんは関係無い。私の問題」
    voice "voice/真冬/maf_a1_0801.ogg"
    dong 真冬_制服_基本_泣き "不是，欧尼酱什么都没有对我做，和欧尼酱没有关系，是我的问题"

    # 莲 「だったら、相談してくれよ。お前一人で悩むよりも俺が…」
    lian "那么，就和我商量一下吧，与其你一个人烦恼，和我……"

    # 真冬 「大丈夫。自分でなんとかするから」
    voice "voice/真冬/maf_a1_0802.ogg"
    dong 真冬_制服_基本_泣き "没关系，我会自己想办法搞定的"

    # 莲 「なぁ、教えてくれ。そんなに何を悩んでいる？俺や心愛に秘密にしておきたい程、何を悩んでいるんだ、真冬！」
    lian "呐，告诉我吧。你为什么这么烦恼？对我和心爱保密的烦恼，到底是什么呢，真冬！"

    # 真冬 「お兄ちゃんには関係ないって言ってるでしょ！！！」
    voice "voice/真冬/maf_a1_0803.ogg"
    dong 真冬_制服_基本_本気2 "我不是已经说了这不管你的事了吗！！！"

    # nil 「真冬は、はじけたように、語気を強め、険しい表情を俺に向けた。」
    "隆冬，像是爆发了一样，对我语气强硬，表情严肃"

    # nil 「だがそれは一瞬で、途端に後悔や悲しみや、複雑な表情を向けた。」
    "但是那只是一瞬间，她的脸上一下子就露出了后悔、悲伤和复杂的表情"

    # 真冬 「…ごめん…お兄ちゃん…本当にごめん…」
    voice "voice/真冬/maf_a1_0804.ogg"
    dong 真冬_制服_基本_泣き "…对不起…欧尼酱…真的对不起…"

    # 莲 「いや…俺も驚いただけだ…。強く迫りすぎたな…」
    lian "没……我也只是吓了一跳…是我太过逼迫了……"

    # 真冬 「うん。お兄ちゃんが怒るのも当たり前だよね…ごめんね…」
    voice "voice/真冬/maf_a1_0805.ogg"
    dong 真冬_制服_基本_泣き "不，欧尼酱生气也是理所当然的吧…对不起…"

    # 莲 「そんなに謝られても…。俺もさ、なんだ、無理にお前から聞き出したい程じゃないんだ…」
    lian "即使你那样道歉……我也是，那个，不会勉强让你说出来……"

    # 莲 「でも、お前が悩んでるなら…俺は力になりたいし、お前を悲しませてしまったなら、謝りたいし…」
    lian "但是，如果你烦恼的话…我想成为你的力量，如果让你悲伤的话，我想向你道歉……"

    # 真冬 「うん…。ありがとう…。でも本当に、お兄ちゃんは悪くないんだ…だから、不安にならないで…」
    voice "voice/真冬/maf_a1_0806.ogg"
    dong 真冬_制服_基本_泣き "嗯……谢谢……但是，真的不是欧尼酱你不好……所以，请不要担心……"

    # 莲 「そうか…。俺達に秘密にしてる理由は教えて貰えないか…？」
    lian "是吗…那可以告诉我向我们保密的原因吗…？"

    # 真冬 「それは…私が引き起こしてしまった問題だから…。いつまでも、二人に甘えてるわけにはいかない」
    voice "voice/真冬/maf_a1_0807.ogg"
    dong 真冬_制服_基本_泣き "那是…因为我引起的问题…我不能一直，都向你们两个人撒娇"

    # 真冬 「二人の…邪魔はしたくないから」
    voice "voice/真冬/maf_a1_0808.ogg"
    dong 真冬_制服_基本_泣き "我不想打扰……你们两个人"

    # 莲 「邪魔だと…？」
    lian "打扰吗……？"

    # 真冬 「……」
    voice "voice/真冬/maf_a1_0809.ogg"
    dong 真冬_制服_基本_泣き "……"

    # nil 「それ以来、真冬は黙ってまた窓の外へ視線を向けてしまった。」
    "那之后，真冬又默默地把视线投向了窗外"

    # 莲 「真冬」
    lian "真冬"

    # 真冬 「ねぇ、お兄ちゃん」
    voice "voice/真冬/maf_a1_0810.ogg"
    dong 真冬_制服_基本_無表情 "呐，欧尼酱"

    # 莲 「なんだ」
    lian "怎么了"

    # 真冬 「……」
    voice "voice/真冬/maf_a1_0811.ogg"
    dong 真冬_制服_基本_無表情 "……"

    # nil 「真冬はゆっくりとこちらを振り向いた。」
    "真冬慢慢地转过身来"

    # 真冬 「今まで、沢山優しくしてくれて、ありがとう」
    voice "voice/真冬/maf_a1_0812.ogg"
    dong 真冬_制服_基本_微笑み "至今为止，你一直对我这么温柔，谢谢你"

    # BGM:bgmfive（あの夏まで...）
    # Demo版结尾的音乐用的就是这里的
    play music bgmfive fadein 4.0

    # nil 「真冬は瞳に大粒の涙を湛えながら、優しく微笑んだ。」
    "真冬的眼睛里充满了大颗的眼泪，温柔地微笑着"

    # nil 「その微笑みは、先ほどの感情を露わにした表情よりも、もっと、人に見せないような、酷く悲しい笑顔だった。」
    "那个微笑，比起刚才流露出感情的表情，更像是不让人看到的极度悲伤的笑容"

    # nil 「全ての感情を封じ込んで、作った笑顔。」
    "将所有的感情封锁起来，强做出来的笑容"

    # 莲 「別れの挨拶でもないんだから…」
    lian "又不是告别的时候…"

    # 真冬 「そう…だね…あは。うん、でも…ちょっと、お別れかも…」
    voice "voice/真冬/maf_a1_0813.ogg"
    dong 真冬_制服_基本_微笑み "是的……啊…欸嘿嘿。嗯，但是……有点，可能要分别了……"

    # 莲 「お別れ…どこかいくのか？」
    lian "分别……你要去哪里？"

    # 真冬 「私…お兄ちゃんの優しさに包まれて、凄く幸せだった。でも、その幸せが当たり前になってしまって、周りの事、心愛ちゃんの事も、何もかも見えなくなってたよ…」
    voice "voice/真冬/maf_a1_0814.ogg"
    dong 真冬_制服_基本_微笑み "我……被哥哥的温柔包围着，非常幸福。但是，我把这种幸福当成理所当然事情了，周围的事情，心爱酱的事情，我什么都没有注意到……"

    # 真冬 「なのに、なのに、今でも、私は、あの幸せを求めてしまっている。だから、お兄ちゃんや心愛ちゃんと話したくなかった」
    voice "voice/真冬/maf_a1_0815.ogg"
    dong 真冬_制服_基本_微笑み "可是，可是，即使是现在，我还是想追求这种幸福。所以，我不想和欧尼酱和心爱酱说话了"

    # 真冬 「話してしまったら…また、耐え切れなくなってしまう。でも、そしたら…きっと、三人が一緒に居られなくなっちゃうから…」
    voice "voice/真冬/maf_a1_0816.ogg"
    dong 真冬_制服_基本_微笑み "如果说出来的话……那样，我又会忍不住的。但是，这样的话……三个人肯定就不能在一起了……"

    # 真冬 「だから…だから…」
    voice "voice/真冬/maf_a1_0817.ogg"
    dong 真冬_制服_基本_微笑み "所以…所以…"

    # 真冬 「前の私に戻れるまで…」
    voice "voice/真冬/maf_a1_0818.ogg"
    dong "直到我能变回以前的我为止…"

    # 真冬 「さようなら、お兄ちゃん」
    voice "voice/真冬/maf_a1_0819.ogg"
    dong "再见，哥哥"

    # 莲 「さようならなんて…言うなよ…なぁ」
    lian "再见什么的……别这样说……啊"

    # 真冬 「大丈夫。必ず、戻ってくるから…ね？」
    voice "voice/真冬/maf_a1_0820.ogg"
    dong "没关系，我一定会回来的…好吗？"

    # nil 「最後に真冬はにっこりと微笑んだ。」
    "最后真冬微微一笑"

    # nil 「俺はその笑顔を前に、何も言い返せなかった。」
    "在你的笑容面前，我什么都说不出口"

    # scene09 场景3 【逐渐意识到真相，努力化解隔阂的二人】 结束
    # scene09 场景4 【二人一起努力，让三个人一起幸福吧】 开始
    # 画面切换：教室（黄昏）->校门口（黄昏）
    scene 校門_夕 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「その後というと…よく覚えていない。」
    "那之后的事情……我记不太清了"

    # nil 「ただ、放心状態で真冬の居る教室を後にして…。」
    "只是，之后心不在焉地离开了真冬的教室"

    # nil 「なんとか校門をくぐって、学園の外にでた。」
    "穿过校门，来到了学校外面"

    # nil 「あれから真冬がどうなったかもわからない。」
    "也不知道后来真冬怎么样了"

    # 莲 「あんな顔…するなんて…」
    lian "竟然做出了…那样的表情…"

    # nil 「自分自身にがっかりだ。」
    "我对自己很失望"

    # nil 「大切な妹に、あんなに悲しそうな笑顔をさせてしまった。」
    "让我的宝贝妹妹，露出那么悲伤的笑容"

    # nil 「これではっきりした。」
    "现在我清楚了"

    # nil 「真冬は俺が心愛と結ばれている事を知って傷ついてしまった。」
    "真冬知道我和心爱结合在一起的事情之后很受伤"

    # 莲 「くそっ…くそっ…俺の…バカ野郎…！」
    lian "可恶…该死…我真是…混蛋…！"

    # nil 「俺の様子を見る考えが、まんまと裏目にでてしまった。」
    "和我想想的结果，恰恰相反了"

    # nil 「こんな事なら…早く思いを告げていれば…。」
    "如果当时能够……早点告诉你我的想法的话…"

    # nil 「ただ、後悔。」
    "只是，后悔"

    # nil 「そして、自分に問いかける。」
    "然后，向自己提问"

    # nil 「俺のやった事は間違っていたのか？」
    "我做的事情错了吗？"

    # nil 「二人を幸せにしたいという気持ちではあったのは確かだが…。」
    "确实是想让两个人幸福，但是…"

    # nil 「結果がこれでは…。」
    "结果却是这样……"

    # 莲 「さようなら…なんて…」
    lian "再见…什么的……"

    # nil 「俺はフラフラしながら、なんとか路駐していたバイクの所までたどり着いた。」
    "我摇摇晃晃的，好不容易才走到了停在路边的摩托车跟前"

    # nil 「すると、俺のバイクの横に、金髪の長い髪の少女が座り込んで、それを眺めていた。」
    "这时，一个金色长发的女孩坐在我的摩托车旁边，看着它"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「なぁマイコゥ。見て見ろよ…２０１３年モデルだぜ…」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    ## 没有跳过
    voice "voice/リオン/ron_a1_0986.ogg"
    lion リオン_基本_杖_微笑み "呐，迈克尔，你看那个……是2013年款的呢……（L:和本作发售同年）"

    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「俺はツインにしか興味ねぇな…」
    # 这里的MJ也少了小图标，回头加上
    ## 47-50 跳过
    voice "voice/その他/mjf_a1_0051.ogg"
    mj MJ_通常 "我只对双胞胎感兴趣..."

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「いなぁ…欲しいなぁ…またがりたいなぁ…ちょっとまたがってもいかなぁ」
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0987.ogg"
    lion リオン_基本_杖_悲しい "真不戳啊……好想要啊……好像坐上去啊……就稍微在上面坐一下"
    hide リオン_基本_杖_微笑み
    
    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「バイク以外にもまたがったらどうだ？」
    # 这里的MJ也少了小图标，回头加上
    voice "voice/その他/mjf_a1_0052.ogg"
    mj MJ_通常 "你为什么不骑摩托车以外的东西呢？"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「黙れマイケル。ちょ、ちょっとだけなら許されるかな…よ、よし！」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0988.ogg"
    lion リオン_基本_杖_微笑み "闭嘴，迈克尔。就稍微、稍微地在上面坐一下应该是可以的吧……好，上了！"
    hide リオン_基本_杖_悲しい

    # 莲 「リオン…」
    lian "里昂……"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「そ、その声は！　蓮くんじゃないかー！Hey！What's up！」
    show リオン_基本_杖_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0989.ogg"
    lion リオン_基本_杖_驚き "这这、这个声音！这不是莲君吗！Hey！What's up！"
    hide リオン_基本_杖_微笑み

    # 莲 「よう。俺のバイクに何か用か」
    lian "嗨，找我的摩托车是有什么事吗"

    # 里昂 「君のだったのかぁー！　いないな！　これ私本国で欲しかったんだよ！　結局手に入らなかったんだけどさ！」
    show リオン_基本_杖_ジト目 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0990.ogg"
    lion リオン_基本_杖_ジト目 "原来是你的啊！真不戳真不戳！这是我出国之前就想要的！结果还是没能入手呢！"
    hide リオン_基本_杖_驚き
    
    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「フルカウルのクオータースポーツか。意外と女々しい趣味してんだな」
    # 这里的MJ也少了小图标，回头加上
    # 参考资料：https://www.weblio.jp/content/%E3%82%AB%E3%82%A6%E3%83%AB
    # クオータース 四分之一
    # スポーツ sport->应该是指摩托车是赛、跑车类型的
    # 摩托车的防风罩
    voice "voice/その他/mjf_a1_0053.ogg"
    mj MJ_通常 "防风罩是四分之一长度的跑车啊，意外的是很有女人味啊"

    # 莲 「ようマイケル。い加減お前さんの存在にも慣れてきた所だ」
    lian "哟迈克尔，我已经习惯你的存在了"

    # MJ 「そいつは良かった。てめぇがツインに乗るようになったら、タンデムしてやってもいぜ」
    # 这里的MJ也少了小图标，回头加上
    voice "voice/その他/mjf_a1_0054.ogg"
    mj MJ_通常 "那太好了。等你骑双胞胎的时候，我也很乐意加入"

    # 莲 「悪いが俺はゲイのヤク中は例え帽子でも後ろには乗せないって事にしてるんでね」
    lian "不好意思，我不会把同性恋瘾君子放在后面的，即使是帽子"

    # MJ 「なんだとてめぇもう一度言ってみろ！　ゲイとヤク中は許す。だが帽子を差別するのは権利団体に訴えてやるからな！」
    # 这里的MJ也少了小图标，回头加上
    voice "voice/その他/mjf_a1_0055.ogg"
    mj MJ_通常 "再说一遍，你这个混蛋！说我是同性恋和瘾君子都可以原谅。但是如果你歧视我是帽子，我就向权利团体起诉你！"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「黙れマイケル。しかし…おや…なんか、表情が暗いね。嫌なことでもあった？　もしかして、フラれちゃった？」
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0991.ogg"
    lion リオン_基本_杖_悲しい "闭嘴吧，迈克尔。但是……咦，总觉得表情很阴沉呢。是不是有什么讨厌的事情？难道是被甩了？"
    hide リオン_基本_杖_ジト目

    # 莲 「まぁ…な…似たような事だ…」
    lian "嘛……是…差不多的事情吧……"

    # 里昂 「Crap…それは悪い事を聞いちゃったにゃー。愚痴りたいなら聞くよー？」
    voice "voice/リオン/ron_a1_0992.ogg"
    lion リオン_基本_杖_悲しい "Crap……我问了不好的事情喵，如果想抱怨的话我会听的哦？"

    # 莲 「アイスを売るのはいのか？」
    lian "你还有在卖冰淇淋吗？"

    # 里昂 「もういんだ。こで売るのは今日でおしまいだからねー。今日から夏休みなんだって？　だから私もお引っ越しですよ」
    voice "voice/リオン/ron_a1_0993.ogg"
    lion リオン_基本_杖_微笑み "已经结束了，今天就卖到这里了。听说今天开始放暑假了？所以我也要搬家了"

    # 莲 「それは…残念だな」
    lian "那…真遗憾啊"

    # 里昂 「暗い顔するなってばさー！　…って、暗い顔にもなるか…。ほらほら、せっかく最後の機会かもしれないんだからさ！　また私に話してごらんよ！」
    voice "voice/リオン/ron_a1_0994.ogg"
    lion リオン_基本_杖_微笑み "别愁眉苦脸的了！……这样，脸也会变得阴沉的吧……你看你看，这可能是最后一次机会了！再和我说说吧！"

    # nil 「元はといえば、あのアイスを食べさせなきゃこんな事は起こらなかったんじゃないか。」
    "说起来，如果当时她没有给我那个冰激凌，这一切都不会发生了"

    # nil 「そんなクソみてぇな発想が浮かぶが、必死で頭の中でかき消そうとする。」
    "虽然脑海中浮现出这样愚蠢的想法，但还是拼命在脑中抹掉"

    # nil 「それは違う。リオンは好意で渡してくれた物だ。そして、実際に恋は叶い、幸せにはなれたはずだ。」
    "不是这样的。里昂是你出于好意给我的。而实际上恋爱应该实现了，变得幸福了"

    # nil 「なのに…。」
    "但是……"

    # 里昂 「…何か、私に言いたい事があるみたいだね」
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0995.ogg"
    lion リオン_基本_杖_悲しい "……好像，你有什么话想对我说的样子呢"
    hide リオン_基本_杖_微笑み

    # 莲 「いや…俺の気のせいだ…」
    lian "不，是我的原因……"

    # nil 「まっすぐにリオンが俺の目を射貫く。」
    "里昂的视线看穿我的眼睛"

    # nil 「この目に貫かれるのは初めてではないが、毎回全身が凍り付くような感覚に襲われる。」
    "虽然不是第一次被这双眼睛所看穿，但每次都会有全身都冻住的感觉"

    # 里昂 「言ってくれていんだよ。もし、私があげたあのアイスのせいなら、私にも責任があるだろうからね」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0996.ogg"
    lion リオン_基本_杖_微笑み "你可以这么说。如果，是因为我给你的那个冰淇淋的话，我也有责任"
    hide リオン_基本_杖_悲しい

    # 莲 「違う！　そんな事は思ってない！」
    lian "不是的！我没有这么想！"

    # 里昂 「Bang！　Bingo！　図星みたいだね。いんだ、自分の感情を否定しなくてい、君の悪い癖だよ」
    show リオン_基本_杖_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0997.ogg"
    lion リオン_基本_杖_驚き "Bang！Bingo！看来我猜对了。没关系的，你不必否定自己的感情，这是你的坏习惯"
    hide リオン_基本_杖_微笑み

    # 莲 「確かに、事の始まりはアレが原因だったかもしれないが、リオンもあのアイスも悪くないだろ。悪いのは…俺だ…。俺の考えが甘かったばかりに…」
    lian "确实，事情的开始可能是因为那个，但是里昂和那个冰淇淋也不坏吧。错的是…我…我的想法太天真了…"

    # 里昂 「そうやって、自分を悪者にして、何が解決するかな？」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0998.ogg"
    lion リオン_基本_杖_微笑み "就这样，把自己当成坏人，能解决什么问题呢？"
    hide リオン_基本_杖_驚き

    # 里昂 「自己犠牲の精神は結構だがね。自分の心の声を、素直に吐き出すのも大事だよってね。サムライとニンジャの国の人には親しみのない理屈かい？」
    voice "voice/リオン/ron_a1_0999.ogg"
    lion リオン_基本_杖_微笑み "自我牺牲的精神固然很好，但是坦率地说出自己的心声也很重要。这是因为武士和忍者国度的人的习惯的原因吗？"

    # 莲 「だがそうしたら、俺はその経過で…アイスの事を否定してしまう事になる…。リオンにとっては、大切な物なんだろ？」
    lian "但是，这样的话，我就会在这个过程中…否定冰淇淋……对里昂来说，是很重要的东西吧？"

    # 里昂 「うん。とても大切だよ。だけど完璧じゃぁない。話してごらんよ。何が苦しい。何が辛い？」
    voice "voice/リオン/ron_a1_1000.ogg"
    lion リオン_基本_杖_微笑み "嗯。非常重要。但是不完美。说说看。有什么痛，有什么苦？"

    # 莲 「俺は…これからどうすればい…？」
    lian "我…接下来该怎么办…？"

    # 里昂 「聞こうか」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1001.ogg"
    lion リオン_基本_杖_にっこり "要听吗？"
    hide リオン_基本_杖_微笑み

    # 莲 「俺は改めて、リオンにアイスを心愛と真冬に食べさせた結果について語りはじめた。」
    lian "我重新开始向里昂讲述，给心爱和真冬吃了那个冰淇淋的结果"

    # 视角切换到真冬商店街桥上
    # BGM停
    stop music fadeout 2.0
    image bg 歩道橋_夕 = "images/bg/歩道橋_夕.png"
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)
    scene 歩道橋_夕 at love69_bg1440 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「…えぐ…くすん…」
    show 真冬_制服_基本_号泣 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0821.ogg"
    dong 真冬_制服_基本_号泣 "……呜……嗯呜……"

    # 真冬 「えぐ…お兄ちゃん…」
    voice "voice/真冬/maf_a1_0822.ogg"
    dong 真冬_制服_基本_号泣 "呜……欧尼酱……"

    # 真冬 「…心愛ちゃん…私…私…どうすれば…どうすればいの…」
    show 真冬_制服_基本_泣き at love69_center with dissolve
    voice "voice/真冬/maf_a1_0823.ogg"
    dong 真冬_制服_基本_泣き "……心爱酱……我…我…该怎么办……怎么办才好啊……"
    hide 真冬_制服_基本_号泣

    # 真冬 「う、うわあああああ…」
    show 真冬_制服_基本_号泣 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0824.ogg"
    dong 真冬_制服_基本_号泣 "哇、哇啊啊啊啊……"
    hide 真冬_制服_基本_泣き

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はあ……はあ……はあ……っ！」
    voice "voice/心愛/cca_a1_1103.ogg"
    ai 心愛_制服_基本_真顔 "哈啊……哈啊……哈啊……！"

    # 心爱 「やっと…見つけた…！　こんな所に…！」
    voice "voice/心愛/cca_a1_1104.ogg"
    ai 心愛_制服_基本_嬉しい "终于…找到了…！在这种地方…！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「…？」
    show 真冬_制服_基本_泣き at love69_center with dissolve
    voice "voice/真冬/maf_a1_0825.ogg"
    dong 真冬_制服_基本_泣き "…？"
    hide 真冬_制服_基本_号泣
    hide 真冬_制服_基本_泣き
    show 真冬_制服_基本_泣き:
        zoom 1.5
        xalign 0.5
        yalign -0.09
        linear 0.3 xalign 0.13

    show 心愛_制服_基本_嬉しい:
        zoom 1.5
        xalign 1.5618
        yalign -0.09
        linear 0.3 xalign 0.8918

    # nil 「キーッ！」
    "哒"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぜぇ…はぁ…見つけたよ…！　真冬ちゃん！」
    voice "voice/心愛/cca_a1_1105.ogg"
    ai 心愛_制服_基本_嬉しい "啊…哈……找到你了哦…！真冬酱！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「こ…こあちゃ…ん？」
    voice "voice/真冬/maf_a1_0826.ogg"
    dong 真冬_制服_基本_泣き "心…心爱…酱？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ちょっと…お話しようか。すごく大事なお話。聞いてくれる？」
    show 心愛_制服_基本_にっこり at love69_right with dissolve
    voice "voice/心愛/cca_a1_1106.ogg"
    ai 心愛_制服_基本_にっこり "稍微…来说说话吧。这是非常重要的事情，你可以听我说吗？"
    hide 心愛_制服_基本_嬉しい

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「え…え…い、いけ…ど…」
    voice "voice/真冬/maf_a1_0827.ogg"
    dong 真冬_制服_基本_泣き "欸…嗯…可、可以的…说…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「よし…！」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1107.ogg"
    ai 心愛_制服_基本_嬉しい "好的…！"
    hide 心愛_制服_基本_にっこり

    # 画面切换回莲校门口
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)
    scene 校門_夕 at love69_bg1440 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # nil 「俺は今までに起こった事を、全て話し終えた。」
    "我把至今为止发生的事情全部说完了"

    # 里昂 「なるほどね…そいつは厄介な事になったねぇ…」
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1002.ogg"
    lion リオン_基本_杖_悲しい "原来如此呢…那家伙成了麻烦事了…"

    # 莲 「もう…手遅れだろうか…」
    lian "已经…太晚了吧…"

    # 里昂 「いや、私はそうは思わないよ」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1003.ogg"
    lion リオン_基本_杖_にっこり "不，我不这么认为"
    hide リオン_基本_杖_悲しい

    # 莲 「そうか…？」
    lian "是吗…？"

    # 里昂 「手遅れもなにも…まだ何も終わっちゃいないもの。蓮くん、君の望みはなんだね」
    show リオン_基本_杖_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1004.ogg"
    lion リオン_基本_杖_ニタァ "一切都太迟了什么的……一切都还没有结束呢。莲君，你的愿望是什么呢？"
    hide リオン_基本_杖_にっこり

    # 莲 「それは…変わらない。二人に幸せになって欲しいんだ」
    lian "这是……不会改变的。我想让她们两个幸福"

    # 里昂 「正確には？」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1005.ogg"
    lion リオン_基本_杖_微笑み "确切地说是？"
    hide リオン_基本_杖_ニタァ

    # 莲 「…いや、俺の気持ちに嘘はないが…」
    lian "…不，我的心情是不会说谎的…"

    # 里昂 「嘘とは言っていないよ。ただ、大事な所が欠けている気がしてならないね」
    voice "voice/リオン/ron_a1_1006.ogg"
    lion リオン_基本_杖_微笑み "我不是在说你说谎。只是，我觉得你忘记了重要的地方"

    # 莲 「大事な所…」
    lian "重要的地方…"

    # nil 「俺は、考えた。」
    "我想一下"

    # nil 「俺の願いに何が欠けているというのか。」
    "我的愿望缺失了什么"

    # nil 「俺は、二人を幸せにしてあげたい。」
    "我，想让她们两个人幸福"

    # nil 「それだけが望みだったはずだ。」
    "这应该是唯一想要的"

    # nil 「俺は、二人を幸せに…」
    "我要让她们两个人幸福…"

    # 莲 「二人を…幸せに…俺が…あっ」
    lian "让两个人…幸福…我…啊"

    # 里昂 「気づいたようだね」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1007.ogg"
    lion リオン_基本_杖_にっこり "好像注意到了呢"
    hide リオン_基本_杖_微笑み

    # 莲 「俺が…二人を幸せにしたいんだ…」
    lian "我想…让她们两个人幸福…"

    # 里昂 「つまり、二人とどうなりたい？」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1008.ogg"
    lion リオン_基本_杖_微笑み "也就是说，你想和那两个人怎么样？"
    hide リオン_基本_杖_にっこり

    # 莲 「二人と…幸せになりたいんだ…三人で…恋人になりたい…」
    lian "想和两个人…变得幸福…三个人…想成为恋人…"

    # 里昂 「それは、二人に伝えた？」
    show リオン_基本_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1009.ogg"
    lion リオン_基本_杖_嬉しい "这句话，你告诉她们了吗？"
    hide リオン_基本_杖_微笑み

    # 莲 「いや…でも、今からじゃ…」
    lian "没有…但是，现在开始的话……"

    # 里昂 「さっきも言ったはず。まだ何も終わっちゃいないと。好きという気持ちを伝える事に早いも遅いもないさ」
    voice "voice/リオン/ron_a1_1010.ogg"
    lion リオン_基本_杖_嬉しい "我刚才也说过了，如果一切都还没有结束的话，向她们传达喜欢的心情永远是既不早也不晚的"

    # 里昂 「心が今だと告げているなら、今がその時だ」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1011.ogg"
    lion リオン_基本_杖_にっこり "如果你的心告诉你是现在的话，那现在就是时候"
    hide リオン_基本_杖_嬉しい

    # nil 「手遅れかもしれない。でも、それでも、俺は真冬と心愛に、本当の気持ちを伝えたかった。」
    "也许为时已晚。但是，尽管如此，我还是想把真正的心情传达给真冬和心爱"

    # nil 「二人を幸せにするんじゃない。三人で幸せになりたいんだ。」
    "不想两个人幸福，而是想让三个人一起幸福"

    # nil 「都合が良い考えかもしれない。けど、俺の望みに嘘はつけない。」
    "也许是个方便的想法。但是，我的愿望不会说谎"

    # 莲 「そうか…自分が抜けていたとは…な…」
    lian "是吗…没想到把自己漏掉了……"

    # 里昂 「君も、心愛ちゃんも、真冬ちゃんも、みんな不器用に優しいんだよね」
    show リオン_基本_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1012.ogg"
    lion リオン_基本_杖_嬉しい "你也好、心爱酱也好、真冬酱也好，大家都很笨拙而温柔呢"
    hide リオン_基本_杖_にっこり

    # 里昂 「お互いを思いやり、自分をないがしろにする優しさ同士がすれ違ったから、こんな事になってしまった。だから…今こそ、自分の気持ちをぶつける時だ。本当の望みを」
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1013.ogg"
    lion リオン_基本_杖_悲しい "互相体谅，忽视自己的温柔伙伴而擦肩而过，才会变成这样。所以……现在正是表达自己心情的时候，请说出真正的愿望"
    hide リオン_基本_杖_嬉しい

    # 莲 「あ…。だが、真冬と心愛がどこにいるかわからない。電話とかメールじゃなく、今すぐ直接伝えたいんだ」
    lian "啊……但是，我不知道真冬和心爱在哪里。我不想打电话或者发短信，而是想现在就当面直接告诉她们"

    # 里昂 「それは…コレが教えてくれるよ」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1014.ogg"
    lion リオン_基本_杖_にっこり "这个啊……这个东西会告诉你的"
    hide リオン_基本_杖_悲しい

    # nil 「そう言って、リオンはどこからともなくコーンに乗せられたアイスクリームを取り出した。」
    "这样说着，里昂不知道从哪里拿出了一个冰淇淋甜筒"

    # 里昂 「ラブポーション・シクスティナイン。恋を叶えてくれる魔法のアイスさ」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1015.ogg"
    lion リオン_基本_杖_微笑み "LOVEPOTION・SIXTYNINE。是能实现恋爱的魔法冰淇淋"
    hide リオン_基本_杖_にっこり

    # 对下面的操作进行说明
    ## 和 Python 一样，可以用 \n 来转义

    luckykeeper "关于接下来将要播放的嵌入式 STAFF 表的说明：\n
        接下来将要播放 STAFF 表，原作的 STAFF 表是由1496张加密的不透明的jpg图片组成，经过抠图处理，得到了1457张并不完美的带alpha通道的PNG图片，原作的这种播放方式并不适应Ren’Py引擎的设计"

    luckykeeper "所以为了正常播放 STAFF 表，这里程序会破例使用设备最大内存来对图形进行加载，预计会最大使用 7-8G 内存并导致程序运行缓慢甚至假死，为了完整的游戏体验，建议选择显示 STAFF 表"

    luckykeeper "如果你正在使用低性能设备，您可以选择不显示 STAFF 表来加快运行速度"

    luckykeeper "在显示 STAFF 表时，强烈建议您不要对程序大小进行调整，比如最大化，这可能会导致程序卡顿，如果程序假死，请耐心等待，加载完成后会自动恢复正常\n
        下面将对是否播放 STAFF 表进行选择"

    # By Luckykeeper @ 2022年1月7日
    # 过 STAFF 表，得好好想想怎么实现
    # bgm：heart beat full ver.，和 STAFF 表不同步，按音效播放方式处理即可
    # 这个 STAFF 好像不长，到Sprite Recording结束
    # 看了下，雀食是完整 STAFF 表
    # 原始是由1496张加密的jpg图片组成，通过抠图，得到1457张并不完美的带alpha通道的PNG图片
    # 思路
    # 用透明的 GIF （GIF 不能带 Alpha 通道但是似乎可以做成透明效果的）
    # 也可以试着用这里的方法重新处理康康效果
    # 参考资料：https://blog.csdn.net/u013580497/article/details/49385127/ 
    # 把处理好的单个 GIF 文件放在背景来放，类似之前的“CALL”动画
    # 做GIF的时候在结尾添加是项目组信息
    # 做的时候还需要处理一下这1457张图片，waifu2x到1920*1080大小
    # 如果实现效果实在太牙白了考虑不做
    # 考虑到素材的情况，到时候在左边的空白加个显示几秒的说明好了

    # 移植版的第一个选择肢诞生了！
    menu show_staff:
        "是否要播放嵌入式 STAFF 表"
        "播放 STAFF 表":
            $ show_staff = True
        "不播放 STAFF 表":
            $ show_staff = False
        
    if show_staff:
        show screen staff
        play sound bgmone
        # 考虑到 STAFF 表的加载时间过长，这里选择再重复播放一次
        queue sound bgmone
    else:
        play sound bgmone

    # 莲 「こ…これは…その…いや、発情するんじゃない…のか？」
    lian "这…这是…那个…不，不是会发情的吗…？"

    # 里昂 「いや。私がこのアイスに込めた魔法は『恋を叶える最善の”答え”を示してくれる』事。つまり、蓮君と繋がりたいって思う事は、彼女達の心が常に君を求めていたからだよ」
    show リオン_基本_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1016.ogg"
    lion リオン_基本_杖_嬉しい "不，我在这个冰淇淋里注入的魔法是『实现恋爱的最好答案』。也就是说，我想她们想和莲君结合在一起，是因为她们的心一直在追求着你"
    hide リオン_基本_杖_微笑み

    # 里昂 「身体を重ねる事。繋がる事は、最高の愛情表現だからね。それを彼女達が君に求めたのは…それだけ、君は愛されていたってことさ」
    voice "voice/リオン/ron_a1_1017.ogg"
    lion リオン_基本_杖_嬉しい "将身体重叠在一起，紧密联系起来，这是爱情的最高表现。她们向你如此寻求的原因是……你是被爱着的呢"

    # 莲 「…そうなのか…。じゃぁ、今、これを俺が食べれば…」
    lian "…是这样的吗…那么，如果现在我吃下这个的话……"

    # 里昂 「君が、恋を叶えるために、今すべきことを教えてくれる。さぁ、食べてごらん。最後の一つだよ」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1018.ogg"
    lion リオン_基本_杖_にっこり "你为了实现恋爱，告诉了我现在该做的事。来，吃下去吧，这是最后一件事了"
    hide リオン_基本_杖_嬉しい

    # 莲 「いのか？　そんなに大切なものを…」
    lian "可以吗？这么重要的东西……"

    # 里昂 「もし、君の恋がこれで叶うようなら。正式に商品として開発するまでさ。さぁ、一気に行ってくれたまえ」
    show リオン_基本_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1019.ogg"
    lion リオン_基本_杖_嬉しい "如果你的爱情能够通过这个实现的话，那就把它正式作为商品开发吧。那么，一口气去吧"
    hide リオン_基本_杖_にっこり

    # 莲 「ありがとうリオン。頂きます」
    lian "谢谢你，里昂。我要吃了"

    # nil 「俺は、リオンに頭を下げて、アイスを一気に平らげた。」
    "我向里昂低头，一口气吃完了冰淇淋"

    # nil 「それは、爽やかにとろけて、ひんやり甘い。最高に優しい味だった。」
    "它，清新融化，凉爽甜美，是最温柔的味道"

    # nil 「心の中に確かな優しさと、確固たる勇気が湧いてくる。」
    "心中涌出确实的温柔和坚定的勇气"

    # nil 「やましい感情なんて一切湧かず。ただ「今すぐこの想いを二人に伝えたい」という力強い感情がわき上がる。」
    "我不觉得有任何内疚的感情，只是「现在就想把这个想法传达给两个人」这样强有力的感情涌上心头"

    # 里昂 「どうだいブラザー。恋は叶えられそうかい？」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1020.ogg"
    lion リオン_基本_杖_微笑み "怎么样，Brother？爱情能实现吗？"
    hide リオン_基本_杖_嬉しい

    # 莲 「あ。大丈夫だ。行ける」
    lian "啊，可以的，那么我出发了"

    # 里昂 「よし！　い顔になったぞ！　それでこそ私の好きな蓮君だ…！おっと、紛らわしい事は言っちゃいけないね！」
    show リオン_基本_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1021.ogg"
    lion リオン_基本_杖_嬉しい "好！表情看起来不错！这才是我喜欢的莲君啊…！哎呀，不能说容易让人混淆的话啊！"
    hide リオン_基本_杖_微笑み

    # 莲 「なぁ、リオン。一つ教えてくれ」
    lian "呐，里昂，有件事想问你"

    # 里昂 「なんだい？」
    show リオン_基本_杖_驚き at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1022.ogg"
    lion リオン_基本_杖_驚き "是什么呢？"
    hide リオン_基本_杖_嬉しい

    # 莲 「どうしてこんなに、俺によくしてくれるんだ…？」
    lian "为什么对我这么好呢…？"

    # 里昂 「それは…」
    show リオン_基本_杖_悲しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1023.ogg"
    lion リオン_基本_杖_悲しい "那是……"
    hide リオン_基本_杖_驚き

    # nil 「リオンは一瞬黙った。」
    "里昂一瞬间沉默了"

    # nil 「やがてゆっくり口を開いた。」
    "然后慢慢地开了口"

    # 里昂 「夢を託したからだよ。君や、心愛ちゃん、真冬ちゃんの恋を叶えられたら…私の夢も叶うだろうって」
    show リオン_基本_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1024.ogg"
    lion リオン_基本_杖_嬉しい "因为我把梦想寄托在你的身上。如果我能实现你、心爱酱、真冬酱的爱情……那我的梦想也会实现"
    hide リオン_基本_杖_悲しい

    # 莲 「そうか…。なんてお礼を言ったらいか…わからないが…ありがとう。本当に」
    lian "是吗……我不知道该这么感谢你……但是……谢谢你……真的"

    # 里昂 「いやーいやー、お礼は事が全て解決してから言って欲しいかな！」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1025.ogg"
    lion リオン_基本_杖_にっこり "呀——呀——感谢的事情还是希望等事情全部解决后再说吧！"
    hide リオン_基本_杖_嬉しい

    # 莲 「でも、リオンは…もう、こには来ないんだろ…？」
    lian "但是，里昂…你已经不会再来这里了吧…？"

    # 里昂 「何年後になるかはわからないけど。もし、私が自分のお店を持てば、いつでも会えるじゃないか！　そしたら、３人で遊びに来てよ！　待ってるからさ！」
    show リオン_基本_杖_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1026.ogg"
    lion リオン_基本_杖_嬉しい "虽然不知道要过多长时间。如果我有了自己的店，我们就可以随时见面了！然后你们三个人就一起来玩吧！我等着你！（L:这里原作就缺少前面的配音）"
    hide リオン_基本_杖_にっこり

    # 莲 「わかった。じゃぁ、もし開くならこの街で開いてくれよ」
    lian "知道了。那么，如果要开店的话，就在这条街上开吧"

    # 里昂 「Of course！そのつもりだよ！さぁ！　アイスの効果が切れる前に行くんだ蓮君！　君の恋を叶えるために！」
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1027.ogg"
    lion リオン_基本_杖_微笑み "Of course！我就是这么想的！来吧！ 在冰激凌效果消失之前赶紧出发吧！为了实现你的爱情！"
    hide リオン_基本_杖_嬉しい

    # 莲 「おう。ちょっくら行ってくるぜ！」
    lian "好。那我稍微去一下！"

    # nil 「俺はメットをかぶって、バイクにまたがり、スタータースイッチを押した。」
    "我戴着头盔，骑着摩托车，按下了发动的开关"

    # nil 「行くべき場所は不思議とわかっている。アイスが教えてくれているのだろう。」
    "虽然很不可思议，但是冰淇淋会告诉我要去的目的地吧"

    # nil 「今ならきっと、魔法の存在を信じれる。」
    "现在的话，我相信膜法是一定存在的！"

    # 里昂 「あ、そうだ。蓮君。これだけは覚えていて欲しい」
    show リオン_基本_杖_無表情 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1028.ogg"
    lion リオン_基本_杖_無表情 "啊，对了。莲君，我希望你能记住这个"
    hide リオン_基本_杖_微笑み

    # 莲 「ん？」
    lian "嗯？"

    # 里昂 「魔法のアイスは『導いてくれる』だけ。恋を叶えるのは…君の、愛っす」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1029.ogg"
    lion リオン_基本_杖_にっこり "魔法冰淇淋只能『引导我』，能让爱情成真的…是你的爱（L:这里玩了个谐音梗233）"
    hide リオン_基本_杖_無表情

    # 莲 「あ～いっすね～…とでも言っておこうか」
    lian "啊~是这样的呢~…就按这么说的去做吧"

    # 里昂 「あは！Awesome！こういうの、日本後でいうと『ワザアリ』っていうんだっけ？」
    # 参考资料：https://ja.wikipedia.org/wiki/%E6%8A%80%E3%81%82%E3%82%8A
    show リオン_基本_杖_微笑み at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1030.ogg"
    lion リオン_基本_杖_微笑み "啊哈哈！Awesome！这样的话，在日本就叫做『技あり』吧？（L:技あり，Waza-Ari，半分，这是专门在日本武术“一分 - 半分”比赛（ippon wazari）中通常使用的给分制度，多用于柔道、 空手道、 柔术的最高得分）"
    hide リオン_基本_杖_にっこり

    # 莲 「ザブトンとかイッポンとかも言うぜ。さて、じゃぁこっちも一本とってくるとすっか」
    # 参考资料：https://ja.wikipedia.org/wiki/%E6%8A%80%E3%81%82%E3%82%8A
    lian "也叫イッポン或者Ippon（L:音「一本」，那么，现在我就去整一个来）"

    # 里昂 「！　ぐっとらっく！　素敵なニュースを待ってるぜ！」
    show リオン_基本_杖_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_1031.ogg"
    lion リオン_基本_杖_にっこり "Take it Easy！Good luck！我等你的好消息！"
    hide リオン_基本_杖_微笑み
    
    # 这个语句是针对MJ设计的参数，能够调整MJ在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.1
    $ sideimagesize.SideImageYalign = 0.78
    $ sideimagesize.SideImageZoom = 1.0

    # MJ 「慰めの台詞は用意しとかねぇからな」
    # 这里的MJ也少了小图标，回头加上
    voice "voice/その他/mjf_a1_0056.ogg"
    mj MJ_通常 "我不会给你准备安慰的台词哦"

    # 莲 「あ、任せろよ」
    lian "啊，交给我吧"

    # nil 「俺はリオンに手で合図を出して、クラッチを切ってギアを踏み込んでから、スロットルを一気に回した。」
    "我用手向里昂发出了信号，踩下离合器，挂上档，一口气转动油门"

    # 音效：摩托车疾驰
    # BG：Black
    stop sound fadeout 4.0
    play sound "voice/effect/02_発進走り去る／高速.ogg"
    scene black with dissolve

    # nil 「行くべき場所はわかっている。」
    "我知道该去哪里"

    # nil 「そして、自分がやるべき事も。」
    "还有，自己应该做的事情"

    # 场景切换：校门口（Black）->河（海）边公园栈道
    play sound "voice/effect/15_ブレーキ2.ogg"
    scene 公園_夕 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # nil 「俺は一瞬の迷いもなく、夕焼けに包まれる公園へとたどり着いた。」
    "我毫不犹豫地来到了被夕阳包围的公园"

    # nil 「公園の駐輪場にバイクを停めて、ゲートをくぐる。」
    "把摩托车停在公园的停车场，穿过大门"

    # nil 「すると、ベンチに並んで座る心愛と真冬の姿が見えた。」
    "于是，看到了并排坐在长椅上的心爱和真冬的身影"

    # nil 「心愛と真冬が一緒に居る事に、俺は驚かなかった。むしろ”知っていた”というべきか。」
    "对于心爱和真冬在一起这件事情，我并不感到惊讶。不如说是「知道」吧"

    # nil 「俺はまっすぐに二人に向かって叫んだ。」
    "我径直向他们喊道"

    # 莲 「心愛！　真冬！」
    lian "心爱！真冬！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「蓮…くん…？」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1108.ogg"
    ai 心愛_制服_基本_真顔 "莲…君…？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「お兄ちゃん…？」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0828.ogg"
    dong 真冬_制服_基本_無表情 "欧尼酱……？"

    # nil 「二人は揃って、俺の方に顔を向けた。」
    "两人都转过脸来看着我"

    # nil 「俺は二人が立ち上がるより先に、二人の元へと駆け寄る。」
    "我赶在他们站起来之前，先跑到他们身边"

    # nil 「二人とも、さっきまで泣いていたのか、同じように目元が赤く晴れていた。」
    "两个人直到刚才都还在哭，眼睛都同样红"

    # 真冬 「お兄ちゃん…私…」
    show 真冬_制服_基本_泣き at love69_left with dissolve
    voice "voice/真冬/maf_a1_0829.ogg"
    dong 真冬_制服_基本_泣き "欧尼酱…我…"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「え、えと…蓮くん…」
    show 心愛_制服_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1109.ogg"
    ai 心愛_制服_基本_泣き "那、那个…莲君…？"
    hide 心愛_制服_基本_真顔

    # 莲 「二人とも何も言うな。まずは、俺に言わせて欲しい」
    lian "你们两个先别着急说。首先，请让我来说"

    # 心爱 「は、はい」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1110.ogg"
    ai 心愛_制服_基本_真顔 "啊，好"
    hide 心愛_制服_基本_泣き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「う、うん」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0830.ogg"
    dong 真冬_制服_基本_無表情 "啊，嗯"
    hide 真冬_制服_基本_泣き

    # nil 「二人の言葉を遮って、俺は息を吸った。」
    "打断了两个人的话，我吸了一口气"

    # nil 「そして、ありったけの想いを込めて、目の前の二人に向けて叫んだ。」
    "然后，怀着所有的感情，朝着眼前的两个人喊道"

    # 莲 「心愛、真冬。好きだ。愛してる。俺と恋人になってくれ！」
    lian "真爱，真冬。我喜欢你们！我爱你们！和我成为恋人吧！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「蓮くん…っ！」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1111.ogg"
    ai 心愛_制服_基本_嬉しい "莲君……！"
    hide 心愛_制服_基本_真顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「おにいちゃん…っ！」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0831.ogg"
    dong 真冬_制服_基本_微笑み "欧尼酱……！"
    hide 真冬_制服_基本_無表情

    # nil 「その瞬間。二人の顔が笑顔で輝いた事がわかった。」
    "那个瞬间，我看到两个人的脸上都闪耀着笑容"

    # nil 「それと同時に、キラキラと宝石のように輝く涙が溢れだしていた。」
    "与此同时，闪闪发光的宝石般闪耀的泪水开始溢出"

    # nil 「そして…。」
    "然后…"

    # nil 「ガバッ！」
    "哒！"

    # 莲 「うおあっ！」
    lian "呜哇！"

    # nil 「二人同時に俺に抱きついた。」
    "两个人同时抱住了我"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「嬉しい。嬉しいよお…蓮君に、恋人になってくれって…蓮君から…言われちゃったよお…」
    show 心愛_制服_基本_号泣1 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1112.ogg"
    ai 心愛_制服_基本_号泣1 "我很高兴，太高兴了…莲君，要我成为你的恋人…莲君对我说……"
    hide 心愛_制服_基本_嬉しい

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「えへへへ…お兄ちゃん…私を…恋人にしてくれるなんて…幸せだよぉ…」
    show 真冬_制服_基本_号泣_1 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0832.ogg"
    dong 真冬_制服_基本_号泣_1 "欸嘿嘿……欧尼酱…竟然把我…当成恋人…真幸福啊…"
    hide 真冬_制服_基本_微笑み

    # 莲 「お、おい…その…なんだ…い、いのか？」
    lian "欸，喂……那…什么…可、可以吗？"

    # nil 「それよりも色々突っ込む事があるんじゃないか？　二人ともってどういうことだよ！　とかそういうの。」
    # 加了个括号表达更好
    "比起那个，不是还有很多要吐槽的事情吗？「这两个人怎么回事啊！」之类的。"

    # 真冬 「お兄ちゃん…えと…えと…その、さよならとか…言っちゃってごめんね…」
    show 真冬_制服_基本_泣き at love69_left with dissolve
    voice "voice/真冬/maf_a1_0833.ogg"
    dong 真冬_制服_基本_泣き "欧尼酱…那个…那个…就是，说再见之类的事情…对不起……"
    hide 真冬_制服_基本_号泣_1

    # 莲 「もう、さよならする気はなくなったか？」
    lian "已经不想说再见了吗？"

    # 真冬 「うんっ！　今ので完全になくなったよ！　大好き！　ずっと傍にいるからね、お兄ちゃん！」
    show 真冬_制服_基本_にっこり_1 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0834.ogg"
    dong 真冬_制服_基本_にっこり_1 "嗯！现在完全没有了！最喜欢了！我会一直在你身边的，欧尼酱！"
    hide 真冬_制服_基本_泣き

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はいはいはーい！　私も告白しまーす！」
    show 心愛_制服_基本_にっこり1 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1113.ogg"
    ai 心愛_制服_基本_にっこり1 "好好好！现在到我来告白啦！"
    hide 心愛_制服_基本_号泣1

    # nil 「心愛は頬を赤らめて、大粒の涙を流し続けたま、無邪気に笑った。」
    "心爱脸红了，继续流着大颗大颗的眼泪，天真地笑了"

    # 心爱 「私も！　蓮君と真冬ちゃん、二人と恋人になりたいです！　二人とも大好きです！」
    show 心愛_制服_基本_笑顔1 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1114.ogg"
    ai 心愛_制服_基本_笑顔1 "我也是！莲君和真冬酱，我想和你们两个成为恋人！我爱你们两个！"
    hide 心愛_制服_基本_にっこり1

    # 莲 「あ。恋人になろう、心愛」
    lian "啊，成为恋人吧，心爱"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「えー…こほん。この流れは…私も告白しなきゃいけない流れですよねー？」
    show 真冬_制服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0835.ogg"
    dong 真冬_制服_基本_目閉じ "欸——……嗯…这个流程是…我也必须要告白的流程吧？"
    hide 真冬_制服_基本_にっこり_1

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「にゃははー！　先手をとってやったぜマイハニー！」
    show 心愛_制服_基本_ニタァ at love69_right with dissolve
    voice "voice/心愛/cca_a1_1115.ogg"
    ai 心愛_制服_基本_ニタァ "呀啊哈哈！我先下手了！My honey！"
    hide 心愛_制服_基本_笑顔1

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「厄介な流れを作ったお兄ちゃんが悪い」
    show 真冬_制服_基本_ジト目 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0836.ogg"
    dong 真冬_制服_基本_ジト目 "是造成这样麻烦流程的欧尼酱不好"
    hide 真冬_制服_基本_目閉じ

    # 莲 「なんでや！　でも、俺も…真冬の気持ちを聞きたいな」
    lian "为什么啊！但是，我也想…听听真冬的心情"

    # 真冬 「っ…！　なんか、性格変わった？　そんなグイグイくる人だっけ…」
    show 真冬_制服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0837.ogg"
    dong 真冬_制服_基本_目閉じ "啊…！为什么感觉你性格变了？原来了这么顽固的人……"
    hide 真冬_制服_基本_ジト目

    # 莲 「お前ら二人に教えてもらったんだよ。攻めていかないと、欲しい物は手に入れられんってな」
    lian "是你们两个人教会我的。如果不去进攻的话，想要的东西就得不到了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「そそ！　恋愛は攻めたもん勝ちだよね！　さーさぁーまっふまふちゃーん。お気持ち、お聞かせ願えませんかねぇ…？」
    voice "voice/心愛/cca_a1_1116.ogg"
    ai 心愛_制服_基本_ニタァ "对对对！恋爱就是进攻才能得到胜利的呢！来~来~嘛呼嘛呼酱~你的感情，让我们也来听一听吧…？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「えー…こうされると言いにくいんですけどー…。…よし、じゃぁ、二人とも目を閉じて？」
    show 真冬_制服_基本_見下し4 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0838.ogg"
    dong 真冬_制服_基本_見下し4 "嗯……这样很难说出口呢……好吧，那，两个人都把眼睛闭上？"
    hide 真冬_制服_基本_ジト目

    # 莲 「逃げるなよ？」
    lian "不要逃跑啊？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「蓮君じゃないんだからそんなことしないよ」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1117.ogg"
    ai 心愛_制服_基本_真顔 "又不是莲君，不会那么做的啦"
    hide 心愛_制服_基本_ニタァ

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ざっつらいと」
    show 真冬_制服_基本_にっこり at love69_left with dissolve
    voice "voice/真冬/maf_a1_0839.ogg"
    dong 真冬_制服_基本_にっこり "That's right"
    hide 真冬_制服_基本_見下し4

    # 莲 「なんだお前ら。まぁいや、目、閉じるぞ心愛」
    lian "你们怎么回事？算了，闭上眼睛吧，心爱"

    scene black with dissolve

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あい」
    voice "voice/心愛/cca_a1_1118.ogg"
    ai 心愛_制服_基本_笑顔 "好~"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「…よし♪」
    voice "voice/真冬/maf_a1_0840.ogg"
    dong 真冬_制服_基本_にっこり_1 "……好♪~"

    # 真冬 「まずはお兄ちゃんに…ちゅっ♪」
    voice "voice/真冬/maf_a1_0841.ogg"
    dong 真冬_制服_基本_目閉じ_1 "先给欧尼酱…啾♪~"

    # nil 「真冬から、軽いキスを交わされる。」
    "真冬给了我一个轻吻"

    # 真冬 「次は、心愛ちゃんに…ちゅーっ♪」
    voice "voice/真冬/maf_a1_0842.ogg"
    dong 真冬_制服_基本_目閉じ_1 "下一个是，给心爱的…啾♪~"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ちゅーっ♪」
    voice "voice/心愛/cca_a1_1119.ogg"
    ai 心愛_制服_基本_にっこり1 "啾♪~"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「よし、目、開けていよ」
    voice "voice/真冬/maf_a1_0843.ogg"
    dong 真冬_制服_基本_目閉じ_1 "好，眼睛，可以睁开了"

    # 原作这里显示心爱了，应该是个Bug
    scene 公園_夕 with dissolve
    show 真冬_制服_基本_にっこり at love69_left with dissolve
    show 心愛_制服_基本_にっこり1 at love69_right with dissolve
    
    # nil 「俺が目を開けると、そこには真冬が、最高の笑顔を俺と心愛に向けていた。」
    "当我我睁开眼睛的时候，看到真冬站在那里，以最美的笑容对着我和心爱"

    # 真冬 「だーいすきだよ。お兄ちゃん。心愛ちゃん。私と、恋人になってくれますか？」
    show 真冬_制服_基本_にっこり_1 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0844.ogg"
    dong 真冬_制服_基本_にっこり_1"最喜欢你们了，欧尼酱，心爱酱。愿意和我成为恋人吗？"
    hide 真冬_制服_基本_にっこり

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「もっちろんだぜ！　らぶ！　らぶだよまふまふちゃん！」
    voice "voice/心愛/cca_a1_1120.ogg"
    ai 心愛_制服_基本_にっこり1 "当然的说啦！Love！Love哒哟嘛呼嘛呼酱！"

    # 莲 「キスが心愛より軽かったからどうしようかな」
    lian "但是对我的亲吻比心爱还轻，怎么办"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「貴様に交渉の余地を設けたつもりはないのだが？」
    show 真冬_制服_基本_見下し4 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0845.ogg"
    dong 真冬_制服_基本_見下し4 "我不想给你这家伙留下谈判的余地，不是吗？"
    hide 真冬_制服_基本_にっこり_1

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「立場をわきまえたまえ」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1121.ogg"
    ai 心愛_制服_基本_真顔 "请明确立场你这家伙"
    hide 心愛_制服_基本_にっこり1

    # 莲 「なんか突然酷くないか二人とも！」
    lian "你们两个怎么突然这么过分啊！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そうでもない。ね、心愛ちゃん？」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0846.ogg"
    dong 真冬_制服_基本_無表情 "也不是这样的啦，对吧，心爱酱？"
    hide 真冬_制服_基本_見下し4

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「そうだぞー！　まぁでも、しっかり告白してくれたし、ご褒美あげますか」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1122.ogg"
    ai 心愛_制服_基本_笑顔 "就是啊就是啊！嘛，不过，你已经好好告白了，要给你奖励吗？"
    hide 心愛_制服_基本_真顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「おっけ－。じゃぁ、心愛ちゃんそっちをお願いね」
    show 真冬_制服_基本_にっこり at love69_left with dissolve
    voice "voice/真冬/maf_a1_0847.ogg"
    dong 真冬_制服_基本_にっこり "OK——那，心爱酱，那就拜托你啦"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「がってん！　さ、もう一度おめとじましょうね～彼氏くん」
    hide 心愛_制服_基本_笑顔
    show 心愛_制服_基本_笑顔:
        zoom 1.5
        xalign 0.8918
        yalign -0.09
        linear 0.15 yalign -0.01
        linear 0.15 yalign -0.09
    voice "voice/心愛/cca_a1_1123.ogg"
    ai 心愛_制服_基本_笑顔 "好！那，再一次恭喜我们结为恋人吧~男朋友君"

    # 莲 「痛いのはおよしになって」
    lian "别弄疼我了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「いから」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1124.ogg"
    ai 心愛_制服_基本_真顔 "好——的——啦"
    hide 心愛_制服_基本_笑顔

    # nil 「心愛が俺の右目を手で覆って、真冬が俺の左目を手で覆った。」
    "心爱用手遮住了我的右眼，真冬用手捂住了我的左眼。"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 心爱&真冬 「『せーのっ』」
    # 需要去加人物表捏，这里头像是真冬的
    # voice "voice/心愛/cca_a1_1125.ogg"
    voice "voice/真冬/maf_a1_0848.ogg"
    ai_dong 真冬_制服_基本_にっこり "『3——2』"

    # 心爱&真冬 「『…ちゅーっ♪』」
    show 真冬_制服_基本_キス at love69_left with dissolve
    voice "voice/心愛/cca_a1_1126.ogg"
    # voice "voice/真冬/maf_a1_0849.ogg"
    ai_dong 真冬_制服_基本_キス "『……啾♪』"
    hide 真冬_制服_基本_にっこり

    # nil 「同時に、両サイドの頬に唇を触れさせられる。」
    "同时，嘴唇也接触到了两边的脸颊"

    # nil 「ぱっと両目の視界が開かれて、正面に立った二人が同時に口を開いた。」
    "突然睁开了双眼，站在正前方的两个人同时开口了"

    # 心爱&真冬 「『だーいすき！』」
    show 真冬_制服_基本_にっこり_1 at love69_left with dissolve
    # voice "voice/心愛/cca_a1_1127.ogg"
    voice "voice/真冬/maf_a1_0850.ogg"
    ai_dong 真冬_制服_基本_にっこり_1 "『最喜欢了！』"
    hide 真冬_制服_基本_キス

    # 莲 「お前ら…！」
    lian "你们…！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ひゃっ」
    show 心愛_制服_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1128.ogg"
    ai 心愛_制服_基本_驚き "呀！"
    hide 心愛_制服_基本_真顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「わっ」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0851.ogg"
    dong 真冬_制服_基本_無表情 "啊！"
    hide 真冬_制服_基本_にっこり_1

    # nil 「俺は堪えきれなくなって、二人を強く強く抱きしめた。」
    "我受不了了，紧紧地抱住了两个人"

    # nil 「俺達はさんざん遠回りしてしまったけど。」
    "虽然我们绕了很多圈子"

    # nil 「やっと望んだ形になる事ができた。」
    "终于成为了期望的形式"

    # nil 「この手に入れた幸せを絶対に離さないと誓った。」
    "我发誓永远不会放开我得到的幸福"

    # nil 「ありがとう…ラブポーション・シクスティナイン。」
    "谢谢……LOVEPOTION・SIXTYNINE"

    # 画面切换：莲心爱真冬->里昂
    scene black with dissolve
    scene 公園_夕 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    transform love69_lion_right:
        zoom 1.5
        yalign 0.07
        xalign 0.89

    # 里昂 「これにてハッピーエンド。日本語でいうところの大団円…って奴だね」
    show リオン_基本_杖_微笑み at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_1032.ogg"
    lion リオン_基本_杖_微笑み "这就是Happy End。用日语来说就是大团圆…吧"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「本当に、これが貴方の望んだ結果ですか？」
    show 店长_私服_不満 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0211.ogg"
    dinerowner 店长_私服_不満 "这真的是，你所希望的结果吗？"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「Who knows？　さぁね。でもこれで、私の夢は叶うよ。全ては計画通りに進んだわけだし…」
    show リオン_基本_杖_ニタァ at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_1033.ogg"
    lion リオン_基本_杖_ニタァ "Who knows？是啊。但是这样的话，我的梦想就实现了。全部都按照计划进行了……"
    hide リオン_基本_杖_微笑み

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「なら良かった。さて、ビジネスの話といきますか。リオン＝マクスウェルさん」
    show 店长_私服_目閉じ at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0212.ogg"
    dinerowner 店长_私服_目閉じ "那就好。那么，我们来谈生意吧。里昂·麦克斯韦小姐"
    hide 店长_私服_不満

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「お手柔らかに頼みますよ。霧葉さん」
    show リオン_基本_杖_微笑み at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_1034.ogg"
    lion リオン_基本_杖_微笑み "请手下留情。雾叶小姐"
    hide リオン_基本_杖_ニタァ

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「まずはうちの店で卸してみますので、需要と効果があるようなら…」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0213.ogg"
    dinerowner 店长_私服_微笑み "首先我们店试着批发康康，如果有需求和效果的话……"
    hide 店长_私服_目閉じ

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「店舗を一つお貸し頂けるという事で」
    voice "voice/リオン/ron_a1_1035.ogg"
    lion リオン_基本_杖_微笑み "如果可以借我一家店铺就好了呢"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「ですが。その効果の有無を確かめるためには、少し時間が必要です。ですので、その間までは貴方の身の振り方について、こちらの指示に従って頂ければと思います」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0214.ogg"
    dinerowner 店长_私服_無表情 "但是，为了确认效果的有无，需要一些时间。所以，在此期间，我们希望你能听从我们的指示"
    hide 店长_私服_微笑み

    # 店长 「つきましては、こちらの指示をご覧下さい」
    show 店长_私服_微笑み at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0215.ogg"
    dinerowner 店长_私服_微笑み "关于这点，请看这边的指示"
    hide 店长_私服_無表情

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「…これは…？！　まさか…そんなっ！」
    show リオン_基本_杖_驚き at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_1036.ogg"
    lion リオン_基本_杖_驚き "…这是…？！难道是…不可能！"
    hide リオン_基本_杖_微笑み

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「そのまさかです。こちらの条件を了承できない場合は、当方からの援助は無しということで」
    show 店长_私服_にっこり at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0216.ogg"
    dinerowner 店长_私服_にっこり "就是你想的这个“不可能”，如果不能同意我们的条件，我们就不提供援助了"
    hide 店长_私服_微笑み

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「いや…驚いただけで…でも、本当にいんですか？」
    voice "voice/リオン/ron_a1_1037.ogg"
    lion リオン_基本_杖_驚き "不，只是吃了一惊而已…但是，你真的确定吗？"

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「いかどうかを決めるのは私達ではなく、貴方です。指示に従うだけの設備等の手配はお任せ下さい」
    show 店长_私服_無表情 at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0217.ogg"
    dinerowner 店长_私服_無表情 "这不是由我们决定的，而是由你。我们会按照你的指示，做出必要的安排"
    hide 店长_私服_にっこり

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「…わかりました。是非、宜しくお願い致します」
    show リオン_基本_杖_にっこり at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_1038.ogg"
    lion リオン_基本_杖_にっこり "我知道了。请一定要多多关照"
    hide リオン_基本_杖_驚き

    # 这个语句是针对雾叶设计的参数，能够调整雾叶在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.07
    $ sideimagesize.SideImageYalign = -4.05
    $ sideimagesize.SideImageZoom = 1.0

    # 店长 「かしこまりました。では、計画は９月よりスタートしますので、その間、夏休みでも楽しんで下さい」
    show 店长_私服_にっこり at love69_wuye_left with dissolve
    voice "voice/霧葉/krh_a1_0218.ogg"
    dinerowner 店长_私服_にっこり "知道了。那么，计划将从9月份开始，在此期间，请尽情享受暑假吧"
    hide 店长_私服_無表情

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「なるほど…さぁ、これからどうなるかな…」
    show リオン_基本_杖_無表情 at love69_lion_right with dissolve
    voice "voice/リオン/ron_a1_1039.ogg"
    lion リオン_基本_杖_無表情 "原来如此……不知道接下来会发生什么呢……"
    hide リオン_基本_杖_にっこり

    # 画面切回莲心爱真冬
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 公園_夕 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「…さて」
    lian "…那么"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はい」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1129.ogg"
    ai 心愛_制服_基本_真顔 "嗯"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「わっ」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0852.ogg"
    dong 真冬_制服_基本_無表情 "嗯"

    # nil 「あれから、俺達は三人でベンチに並んで座りながら、風で揺れるブランコを眺めていた。」
    "在那以后，我们三个人并排坐在长椅上，望着在风中摇曳的秋千"

    # nil 「あらかた、この一週間で話せなかったことは話した。」
    "基本上，一起把这一周没能说的话都说完了"

    # nil 「心愛のバイトの事や、担任がハワイに行くことか。。」
    "关于心爱打工的事，还有班主任去夏威夷的事情"

    # 真冬 「へー…あの人達ハワイいくんだ…」
    voice "voice/真冬/maf_a1_0853.ogg"
    dong 真冬_制服_基本_無表情 "诶——……她们要去夏威夷啊……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「そういえば、真冬ちゃんって、店長さんと知り合いなんでしょ？」
    show 心愛_制服_基本_微笑み at love69_right with dissolve
    voice "voice/心愛/cca_a1_1130.ogg"
    ai 心愛_制服_基本_微笑み "说起来，你不是认识店长吗？"
    hide 心愛_制服_基本_真顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「霧葉さん？　想瑠にゃんの家に泊まったときに、想瑠にゃんの家にお姉さんと一緒に遊びに来てたよ。あと、想瑠にゃんのお姉さんにも会った」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0854.ogg"
    dong 真冬_制服_基本_微笑み "雾叶姐姐？在想瑠喵家里过夜的时候，她和姐姐一起也到想瑠喵家玩了。还有，也看到了想瑠喵的姐姐"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ほへー！　マジで！　いないなー！　え、何したの？　５人で。モノポリー？」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%A2%E3%83%8E%E3%83%9D%E3%83%AA%E3%83%BC
    hide 心愛_制服_基本_微笑み
    show 心愛_制服_基本_ポカーン:
        zoom 1.5
        xalign 0.8918
        yalign -0.09
        linear 0.15 yalign -0.01
        linear 0.15 yalign -0.09
    voice "voice/心愛/cca_a1_1131.ogg"
    ai 心愛_制服_基本_ポカーン "呜欸——！真的！真好啊真好啊！诶，干了什么？5个人，Monopoly？（L:Monopoly其实就是大富翁啦，台湾译作地产大亨，原名Monopoly意为“垄断”，因为最后只有一个胜利者，其余均以破产收场）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「んー秘密なんだけどな～…心愛ちゃんだけになら教えてあげてもいよ」
    show 真冬_制服_基本_まったり at love69_left with dissolve
    voice "voice/真冬/maf_a1_0855.ogg"
    dong 真冬_制服_基本_まったり "嗯~虽然是秘密啊~…但是如果只是心爱酱一个人的话，我可以告诉你哦"
    hide 真冬_制服_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「なになに！　聞かせて聞かせて！」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1132.ogg"
    ai 心愛_制服_基本_笑顔 "什么什么！快告诉我快告诉我！"
    hide 心愛_制服_基本_ポカーン

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「～～……（こしょこしょ）」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0856.ogg"
    dong 真冬_制服_基本_無表情 "～～……（悄悄话悄悄话）"
    hide 真冬_制服_基本_まったり

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「！！！！！」
    hide 心愛_制服_基本_笑顔
    show 心愛_制服_基本_ぐるぐる:
        zoom 1.5
        xalign 0.8918
        yalign -0.09
        linear 0.15 yalign -0.01
        linear 0.15 yalign -0.09
    voice "voice/心愛/cca_a1_1133.ogg"
    ai 心愛_制服_基本_ぐるぐる "！！！！！"

    # nil 「突然、ボンッ！　と音を立て心愛が真っ赤になった。」
    "突然，哈啊！发出这样的声音的心爱满脸通红"

    # 心爱 「しょ、しょんな事を…え…５人で…まさか…す…すげぇ…」
    show 心愛_制服_基本_ポカーン at love69_right with dissolve
    voice "voice/心愛/cca_a1_1134.ogg"
    ai 心愛_制服_基本_ポカーン "那、那种事琴…诶…5个人…真的吗……太厉害了…"
    hide 心愛_制服_基本_ぐるぐる

    # 莲 「な、なんだ気になるな」
    lian "到、到底是什么事啊"

    # 心爱 「いや…秘密っていうか、これは蓮君は聞かない方がい…女の子の神秘みたいなもんだから…うん…」
    voice "voice/心愛/cca_a1_1135.ogg"
    ai 心愛_制服_基本_ポカーン "没有没有……是秘密，莲君还是不要问的好…因为这是女孩子的秘密…嗯…"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そうね。隠し事っていうか、私達の未来のためにも、聞かない方が良いと思う」
    voice "voice/真冬/maf_a1_0857.ogg"
    dong 真冬_制服_基本_無表情 "是啊。应该说是有所隐瞒，为了我们的未来，我觉得还是不要问为好"

    # 莲 「…わかった。世の中知らない方が幸せな事もあるからな」
    lian "……我知道了。世上还是有些事情不知道才幸福"

    # 真冬 「うん。良い子良い子。心愛ちゃんも興味あるなら…来る？」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0858.ogg"
    dong 真冬_制服_基本_微笑み "嗯。好孩子好孩子。如果心爱酱也有兴趣的话…要来吗？"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「え…えー！？　ど、どどど、どーしよ！　どーしよう！　どどどどーしよう！」
    show 心愛_制服_基本_ぐるぐる at love69_right with dissolve
    voice "voice/心愛/cca_a1_1136.ogg"
    ai 心愛_制服_基本_ぐるぐる "诶……呜诶！？怎、怎怎怎、怎么办！怎么办！怎怎怎怎怎么办好啊！"
    hide 心愛_制服_基本_ポカーン

    # 莲 「めっちゃ興味津々だな」
    lian "真是太感兴趣了"

    # 心爱 「で、でも…私なんかが言って邪魔じゃないかな…そ、そういうの…したことないし…うん。でもぶっちゃけ興味ある…よ…うん…未知の世界だし…」
    show 心愛_制服_基本_ポカーン at love69_right with dissolve
    voice "voice/心愛/cca_a1_1137.ogg"
    ai 心愛_制服_基本_ポカーン "但、但是…我的话会不会很碍事呢……那，那样的事情……我也…没做过…不、不过直截了当地说我倒是感兴趣呢…嗯……又是个未知的世界呢……"
    hide 心愛_制服_基本_ぐるぐる

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「大丈夫大丈夫。想瑠にゃんのお姉さんと霧葉さんが滅茶苦茶上手いから。安心して身を任せれば大丈夫」
    show 真冬_制服_基本_ニタァ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0859.ogg"
    dong 真冬_制服_基本_ニタァ "没关系没关系。想瑠喵的姐姐和雾叶姐姐都非常会乱来。放心地交给她们就没问题了"
    hide 真冬_制服_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「わ、わかった…その時は、よろしくおねがいします…」
    show 心愛_制服_基本_ぐるぐる at love69_right with dissolve
    voice "voice/心愛/cca_a1_1138.ogg"
    ai 心愛_制服_基本_ぐるぐる "我、我知道了……到那时候，就拜托你们了……"
    hide 心愛_制服_基本_ポカーン

    # 莲 「……」
    lian "……"

    # nil 「もしかして、エロい話してるのか…？　と、とにかく、まだ、アイスの力が残っているのか、『知ろうとするな。死ぬぞ』という声が聞こえるので、耐える。」
    "难道是在说瑟琴的话题吗…？总之，不知是不是还残留着冰淇淋的力量？因为能听到『不要试图知道，你会死的』的声音，所以要忍住"

    # 莲 「よし、他に話してない事はあったかな…っと」
    lian "好吧，还有其他还没说的事情吗……"

    # 心爱 「あ！　はいはいはーい！　私、ぶっちゃけ気になってたことあるんだわさ！」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1139.ogg"
    ai 心愛_制服_基本_笑顔 "啊！这里这里这里！我，其实有件很在意的事情！"
    hide 心愛_制服_基本_ぐるぐる

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「あ、私も。多分、心愛ちゃんと一緒の疑問だと思う」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0860.ogg"
    dong 真冬_制服_基本_無表情 "啊，我也是。大概，是和心爱酱一样的疑问吧"
    hide 真冬_制服_基本_ニタァ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「よし、じゃぁせーので言おう！」
    show 心愛_制服_基本_にっこり1 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1140.ogg"
    ai 心愛_制服_基本_にっこり1 "好，那么我们一起来说吧！"
    hide 心愛_制服_基本_笑顔

    # 心爱 「せーのっ！」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1141.ogg"
    ai 心愛_制服_基本_笑顔 "3——2"
    hide 心愛_制服_基本_にっこり1

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 心爱&真冬 「『ラブポーション・シクスティナインって何？』」
    voice "voice/真冬/maf_a1_0861.ogg"
    # voice "voice/心愛/cca_a1_1142.ogg"
    ai_dong 真冬_制服_基本_無表情 "『LOVEPOTION・SIXTYNINE是什么？』"

    # 莲 「あー…」
    lian "啊——……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「さっきね、真冬ちゃんと話したんだけどね。私も真冬ちゃんも、蓮君と初めてエッチした日に、謎のアイスを食べてる事がわかったんだわさ」
    voice "voice/心愛/cca_a1_1143.ogg"
    ai 心愛_制服_基本_笑顔 "刚才啊，我和真冬酱聊过了。我和真冬酱都是在和莲君第一次H的那天，都是吃了谜一样的冰淇淋"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まぁ…私は勝手にアイスを食べちゃったんだけど…でも、お兄ちゃんがあのアイスを私に食べさせるために、家に置いておいたと仮定すると…」
    show 真冬_制服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0862.ogg"
    dong 真冬_制服_基本_目閉じ "嘛……我是不经意间吃下去那个冰淇淋的……不过，我是假设那个冰淇淋是欧尼酱给我买的，才放在家里的"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あのアイスに、何か…エッチな薬でも入っていたんではないか。という推論にたどり着いたわけです」
    voice "voice/心愛/cca_a1_1144.ogg"
    ai 心愛_制服_基本_笑顔 "那个冰淇淋里面，放了什么……让人发情的药物在里面，我们得到了这样的推论"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「結果的に、こうして三人で結ばれる事ができたし、お兄ちゃんと繋がれて幸せだったので、責めてるわけじゃないけど。事実確認はしておきたいというか」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0863.ogg"
    dong 真冬_制服_基本_微笑み "从结果上来看，我们三个人能这样结下姻缘，能和欧尼酱联系在一起很幸福呢，所以我们并不是在责备你，只是想确认一下事实"
    hide 真冬_制服_基本_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「そこんところ、ぶっちゃけどうなんでしょう！」
    show 心愛_制服_基本_にっこり at love69_right with dissolve
    voice "voice/心愛/cca_a1_1145.ogg"
    ai 心愛_制服_基本_にっこり "老实交代，那个和这个有什么关系！"
    hide 心愛_制服_基本_笑顔

    # 莲 「あーあー…それは、君たち、怒ったりしないかね？」
    lian "啊——啊…那，你们，不会生气的吧？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「やはり何かあるのね…」
    show 真冬_制服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0864.ogg"
    dong 真冬_制服_基本_目閉じ "果然是有什么呢…"
    hide 真冬_制服_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「怒ったりはしないよー！　凄く美味しかったし、今でも味を思い出せるもん！出来れば、また食べたいなって思ってるぐらいだからさ！」
    voice "voice/心愛/cca_a1_1146.ogg"
    ai 心愛_制服_基本_にっこり "我不会生气的！非常好吃，现在也能想起味道！如果可以的话，我还想再吃！"

    # 莲 「じゃぁ…正直に話すからな」
    lian "那么……我就实话实说了"

    # nil 「俺はリオンという少女との出会いと、あのアイスが「恋が叶う魔法のアイス」という触れ込みの『食べた人の恋を叶える手助けをしてくれるアイス』という事。」
    "我和一个叫里昂的少女相遇，那个冰淇淋宣传是「能实现恋爱的魔法冰淇淋」，是『能帮助吃了的人实现恋爱的冰淇淋』的事情"

    # nil 「そして、リオンの名誉のためにも決してエロい薬とかは入っておらず、発情効果があるのは『好きという気持ちが最高まで高まった結果』だという事を伝えた。」
    "并且，为了里昂的名誉，里面绝对没有加入让人发情的药物，导致发情效果的是『喜欢的心情高涨到顶点的结果』，把这样的事情告诉了她们"

    # nil 「心愛と真冬は、俺の話を聞きながら、驚いたり首をかしげたり、表情をころころ変えたが、終始怒ったりはせず、ちゃんと聞いてくれた。」
    "心爱和真冬听着我的话，时而惊讶，时而歪着头，时而变换着表情，但始终没有生气，只是认真地听着"

    # nil 「そして…。」
    "然后……"

    # 莲 「と、言う事らしい。真冬は覚えてないかな、一回だけそのアイスのCMを見てるぜ俺たち」
    lian "嘛，好像是这么说的。真冬没注意到嘛，我们当时在电视CM上还看到过一次这个冰激凌"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「あー…言われてみれば。一回お兄ちゃんと見た気がする。眉唾ものだと思ったけど、よもや本当に効果があるとは…」
    voice "voice/真冬/maf_a1_0865.ogg"
    dong 真冬_制服_基本_目閉じ "啊…这么说来，我记得我好像是和欧尼酱看到过一次。我觉得这是值得怀疑的东西，但没想到竟然真的有效果…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あうあうあー過ぎた事だけど…あれが自分のしたことだと思うと恥ずかしぃ…」
    show 心愛_制服_基本_ぐるぐる at love69_right with dissolve
    voice "voice/心愛/cca_a1_1147.ogg"
    ai 心愛_制服_基本_ぐるぐる "啊呜啊呜啊——虽然已经是过去的事情了…但是一想到那是自己做的事情就觉得太羞耻了…"
    hide 心愛_制服_基本_にっこり

    # 莲 「ちなみに、今さっき、俺もあのアイスを食べている」
    lian "顺便一提，刚才我也吃了那个冰淇淋"

    # 这回又变真冬&心爱了，而且没有对话框小头像了
    # 那这里就稍微修正一下吧，新增人物并把这里心爱酱的表情放在那里好了

    hide 心愛_制服_基本_ぐるぐる
    show 心愛_制服_基本_ぐるぐる:
        zoom 1.5
        xalign 0.8918
        yalign -0.09
        linear 0.15 yalign -0.01
        linear 0.15 yalign -0.09

    hide 真冬_制服_基本_目閉じ
    show 真冬_制服_基本_目閉じ:
        zoom 1.5
        xalign 0.13
        yalign -0.09
        linear 0.15 yalign -0.01
        linear 0.15 yalign -0.09

    # 真冬&心爱 「『っ！』」
    # voice "voice/心愛/cca_a1_1148.ogg"
    # voice "voice/真冬/maf_a1_0866.ogg"
    ## 跳过了，没有按顺序来，整个大概听了一边，感觉心爱的1691，1715，1216最像，真冬那边没有发现
    # 选1216
    # 太淦了，就不在心爱文件夹里面，离谱！
    # voice "voice/心愛/cca_a1_1216.ogg"
    voice "voice/その他/ex2_a1_0001.ogg"
    dong_ai 心愛_制服_基本_ぐるぐる "『啊！』"

    # nil 「その突如、真冬と心愛は一歩身を引いて、俺から距離を取った。」
    "突然，隆冬和心爱退后一步，远离了我"

    # 莲 「何で避けるんだよ！」
    lian "为什么要躲开啊！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そりゃ…発情してたらヤバいじゃん…」
    show 真冬_制服_基本_見下し at love69_left with dissolve
    voice "voice/真冬/maf_a1_0866.ogg"
    dong 真冬_制服_基本_見下し "那是……要是发情了就牙白了嘛…"
    hide 真冬_制服_基本_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「そうだよこお外だよ…やだよ外は…」
    voice "voice/心愛/cca_a1_1148.ogg"
    ai 心愛_制服_基本_ぐるぐる "就是啊……这是在外面啊，不要啊…外面啊……"

    # 莲 「お前ら人の話を聞いてたのか！？　別にエロい気分になる効果は含まれてないんだって！」
    lian "你们有在听我说话吗? 前面说了这里面并没有什么瑟琴的效果！"

    # 心爱 「でも私はなったよ？」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1149.ogg"
    ai 心愛_制服_基本_真顔 "但是我都变成这样了啊？"
    hide 心愛_制服_基本_ぐるぐる

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「私も。　なった原因が、好きって気持ちなら…エッチな気分になってもおかしくないよね？」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0867.ogg"
    dong 真冬_制服_基本_無表情 "我也是。变成这样的原因，如果是喜欢的心情的话…就算变成瑟琴的心情也不奇怪吧？"
    hide 真冬_制服_基本_見下し

    # 莲 「まぁ…そうなるな…」
    lian "嘛…就这样吧…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「それに…アレだよ、蓮くん。彼女としてはね…大好きな彼氏が自分を求めてエッチな気分になってくれたら、素直に嬉しいわけで…」
    show 心愛_制服_基本_微笑み at love69_right with dissolve
    voice "voice/心愛/cca_a1_1150.ogg"
    ai 心愛_制服_基本_微笑み "而且……就是那个，莲君。作为女朋友……如果最喜欢的男朋友追求自己而产生色情的心情的话，自然会很开心的……"
    hide 心愛_制服_基本_真顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うん…だから、極力拒否はしたくないっていうか…。でも、こじゃ落ち着いて出来ないし…ね？　せっかく恋人になったんだし、初めてはゆっくりまったりしたいよ？」
    show 真冬_制服_基本_目閉じ_1 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0868.ogg"
    dong 真冬_制服_基本_目閉じ_1 "嗯…所以，我是尽量不想拒绝的……但是，这里的话就没法冷静下来…对吧？好不容易成为恋人了，第一次还是想慢慢来的哟？"
    hide 真冬_制服_基本_無表情

    # 莲 「お、お前ら…」
    lian "你、你们……"

    # nil 「むくり」
    "呲啦"

    # 莲 「あ」
    lian "啊"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「鎮まれぇー！」
    show 心愛_制服_基本_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1151.ogg"
    ai 心愛_制服_基本_驚き "给我老实下来——！"
    hide 心愛_制服_基本_微笑み

    # nil 「ゲシゲシ」
    "喀哒喀哒"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「げっだうん！」
    show 真冬_制服_基本_見下し3 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0869.ogg"
    dong 真冬_制服_基本_見下し3 "Get down！"
    hide 真冬_制服_基本_目閉じ_1

    # nil 「ゲシゲシ」
    "咔哒咔哒"

    # 莲 「GYAAAAAAA！！さっきのしおらしい態度はどこへいきやがった！　思いっきり強硬に拒絶じゃねぇか！」
    lian "GYAAAAAAA！！刚才那温文尔雅的态度去哪里了！不是不想狠心拒绝的吗！"

    # nil 「沈みました（物理的に）」
    "被击沉了（物理上的）"

    # 莲 「い…痛い…使い物にならなくなっちゃう…」
    lian "呀……好痛……那里要变得没法用了……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぜぇ…はぁ…手こずらせやがって…」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1152.ogg"
    ai 心愛_制服_基本_真顔 "呜欸…哈啊…真是棘手的说…"
    hide 心愛_制服_基本_驚き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「しぶといったらありゃしない…」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0870.ogg"
    dong 真冬_制服_基本_無表情 "真是太不像话了…"
    hide 真冬_制服_基本_見下し3

    # 莲 「びええええ」
    lian "呜欸欸欸欸"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「もー、泣かないの」
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1153.ogg"
    ai 心愛_制服_基本_不機嫌 "真是的——不要哭了啊"
    hide 心愛_制服_基本_真顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「男が泣いちゃダメでしょー妹としてどうかと思うよ」
    show 真冬_制服_基本_ジト目 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0871.ogg"
    dong 真冬_制服_基本_ジト目 "男人不能哭吧，我作为妹妹都不知道该怎么办了"
    hide 真冬_制服_基本_無表情

    # 莲 「だってぇ…仕方ないじゃんか…生理現象なんだからさぁ…俺だって嬉しいんだよ…君らに優しくしてもらえるのはさ…」
    lian "可是……这不是没办法吗…因为是生理现象嘛…我也很开心啊…能被你们温柔对待…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「だから…もぉー恥ずかしいなぁ！　真冬ちゃん　パス！」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1154.ogg"
    ai 心愛_制服_基本_笑顔 "所以啊——……真是的~太害羞了！真冬酱Pass！"
    hide 心愛_制服_基本_不機嫌

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「しょうないなぁ。一つ貸しだよ心愛ちゃん」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0872.ogg"
    dong 真冬_制服_基本_無表情 "真是没办法呢，借你个人情吧，心爱酱"
    hide 真冬_制服_基本_ジト目

    # nil 「真冬と心愛はもう一度俺の隣に座ってくれる。」
    "真冬和心爱再一次坐在我的身边"

    # 真冬 「帰ったら…三人で、エッチ…しよ？」
    show 真冬_制服_基本_にっこり at love69_left with dissolve
    voice "voice/真冬/maf_a1_0873.ogg"
    dong 真冬_制服_基本_にっこり "回去之后……三个人，H……吧？"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ね。みんなで一緒に沢山チューとか…しよ？その時は…沢山気持ち良くしてあげるから…ね、真冬ちゃん」
    show 心愛_制服_基本_にっこり at love69_right with dissolve
    voice "voice/心愛/cca_a1_1155.ogg"
    ai 心愛_制服_基本_にっこり "呐。和大家一起啾很多次吧…怎么样？那个时候…我会让你心情变好的…呐，真冬酱"
    hide 心愛_制服_基本_笑顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うん。私達をお兄ちゃんの好きにして良いし、して欲しい事あったら…全部、してあげるよ」
    show 真冬_制服_基本_微笑み_1 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0874.ogg"
    dong 真冬_制服_基本_微笑み_1 "嗯，欧尼酱可以随心所欲地对待我们，如果你有想做的事……全部，都会帮你做的哦"
    hide 真冬_制服_基本_にっこり

    # 莲 「真冬…心愛…」
    lian "真冬……心爱……"

    # nil 「二人が愛おしくなって、肩を抱き寄せて頭を撫でる。」
    "两个人实在是太可爱了，我抱着她们的肩膀抚摸着她们的头"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    hide 心愛_制服_基本_にっこり
    show 心愛_制服_基本_にっこり1:
        zoom 1.5
        xalign 0.8918
        yalign -0.09
        linear 0.15 yalign -0.01
        linear 0.15 yalign -0.09

    # 心爱 「えへへ～♪　撫で撫で好き～」
    voice "voice/心愛/cca_a1_1156.ogg"
    ai 心愛_制服_基本_にっこり1 "欸嘿嘿嘿~♪摸摸最喜欢啦~"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うんっ好き。もっとして？　おにいちゃん」
    hide 真冬_制服_基本_微笑み_1
    show 真冬_制服_基本_にっこり_1:
        zoom 1.5
        xalign 0.13
        yalign -0.09
        linear 0.15 yalign -0.01
        linear 0.15 yalign -0.09
    voice "voice/真冬/maf_a1_0875.ogg"
    dong 真冬_制服_基本_にっこり_1 "嗯，喜欢，再摸一会儿？欧尼酱"

    # nil 「むくり」
    "呲啦"

    # 莲 「あ」
    lian "啊"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「バニィッシュ！」
    hide 心愛_制服_基本_にっこり1
    show 心愛_制服_基本_驚き:
        zoom 1.5
        xalign 0.8918
        yalign -0.09
        linear 0.15 yalign -0.01
        linear 0.15 yalign -0.09
    voice "voice/心愛/cca_a1_1157.ogg"
    ai 心愛_制服_基本_驚き "Punish！"

    # nil 「ベシイッ！」
    "啪叽！"

    # 莲 「ひぎい！」
    lian "呜欸！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ジャッジメント！」
    hide 真冬_制服_基本_にっこり_1
    show 真冬_制服_基本_見下し4:
        zoom 1.5
        xalign 0.13
        yalign -0.09
        linear 0.15 yalign -0.01
        linear 0.15 yalign -0.09
    voice "voice/真冬/maf_a1_0876.ogg"
    dong "Judgement！"

    # nil 「ドグシャァ！」
    "噗哈！"

    # 莲 「ホンゲェー！」
    lian "真是的！"

    # 莲 「くそう…お前ら…夜は覚えてろよ…」
    lian "可恶…你们…晚上给我等着啊…"

    # nil 「……」
    "……"

    # 莲 「やっと痛みが引きましたけど、息子は怖がって立ち上がろうとしません」
    lian "虽然疼痛终于止住了，但是儿子现在已经害怕得不敢再站起来了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「しばらくそうしてください」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1158.ogg"
    ai 心愛_制服_基本_真顔 "请暂时就这样"
    hide 心愛_制服_基本_驚き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「当然の報いです」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0877.ogg"
    dong 真冬_制服_基本_無表情 "这是罪有应得"
    hide 真冬_制服_基本_見下し4

    # 莲 「…はい。ていうか、なぁ、君ら二人は俺が来るまで何してたの？」
    lian "……是的。话说回来，你们俩在我来之前都做了什么？"

    # 真冬 「えー…それ言わなきゃだめ？」
    show 真冬_制服_基本_目閉じ_1 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0878.ogg"
    dong 真冬_制服_基本_目閉じ_1 "嗯……这个不说不行吗？"
    hide 真冬_制服_基本_無表情

    # 莲 「だめ」
    lian "不说不行"

    # 真冬 「じゃぁ、心愛ちゃんパス」
    show 真冬_制服_基本_ニタァ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0879.ogg"
    dong 真冬_制服_基本_ニタァ "那么，心爱酱Pass"
    hide 真冬_制服_基本_目閉じ_1

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぶえええ！　私かよぉ！」
    show 心愛_制服_基本_ぐるぐる at love69_right with dissolve
    voice "voice/心愛/cca_a1_1159.ogg"
    ai 心愛_制服_基本_ぐるぐる "呜欸欸欸！是我吗！"
    hide 心愛_制服_基本_真顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「これで貸し借り無し」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0880.ogg"
    dong 真冬_制服_基本_微笑み "这样就两不相欠了"
    hide 真冬_制服_基本_ニタァ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「断れない交渉しやがってぇ…。わかりました。じゃぁ、説明しますよー」
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1160.ogg"
    ai 心愛_制服_基本_不機嫌 "这是无法拒绝的交涉呢……我知道了。那么，我来说明一下吧——"
    hide 心愛_制服_基本_ぐるぐる

    # 莲 「頼むわ」
    lian "拜托了"

    # 画面切回商店街桥
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=True, alpha=True, time_warp=None)
    scene 歩道橋_夕 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=True, alpha=True, time_warp=None)

    # nil 「むかーしむかしの凡そ今から３０分くらい前。」
    "不久之前的刚才，距现在大概30分钟前"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「…えぐ…くすん…」
    show 真冬_制服_基本_号泣 at love69_center with dissolve
    voice "voice/真冬/maf_a1_0881.ogg"
    dong 真冬_制服_基本_号泣 "……呜……嗯呜……"

    # 真冬 「えぐ…お兄ちゃん…」
    voice "voice/真冬/maf_a1_0882.ogg"
    dong 真冬_制服_基本_号泣 "呜……欧尼酱……"

    # 真冬 「…心愛ちゃん…私…私…どうすれば…どうすればいの…」
    voice "voice/真冬/maf_a1_0883.ogg"
    dong 真冬_制服_基本_号泣 "……心爱酱……我…我…该怎么办……怎么办才好啊……"

    # 真冬 「う、うわあああああ…」
    voice "voice/真冬/maf_a1_0884.ogg"
    dong 真冬_制服_基本_号泣 "哇、哇啊啊啊啊……"

    # nil 「公園でベンチに座って一人、泣いている真冬ちゃんが居ました。」
    # L:惊了，这里不是商店街桥嘛，怎么也成公园的里面了，绝了！
    "在公园里一个人坐在长椅，不停哭泣着的真冬酱"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はあ……はあ……はあ……っ！」
    hide 真冬_制服_基本_号泣
    show 真冬_制服_基本_号泣:
        zoom 1.5
        xalign 0.5
        yalign -0.09
        linear 0.3 xalign 0.13

    show 心愛_制服_基本_真顔:
        zoom 1.5
        xalign 1.5618
        yalign -0.09
        linear 0.3 xalign 0.8918
    voice "voice/心愛/cca_a1_1161.ogg"
    ai 心愛_制服_基本_真顔 "哈啊……哈啊……哈啊……！"

    # 心爱 「やっと…見つけた…！　こんな所に…！」
    voice "voice/心愛/cca_a1_1162.ogg"
    ai 心愛_制服_基本_真顔 "终于…找到了…！在这种地方…！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「…？」
    show 真冬_制服_基本_泣き at love69_left with dissolve
    voice "voice/真冬/maf_a1_0885.ogg"
    dong 真冬_制服_基本_泣き "…？"
    hide 真冬_制服_基本_号泣

    # nil 「キーッ！」
    # 这里的动画似乎重放了呢，考虑下重新做一下，先在远处，再靠近
    hide 心愛_制服_基本_真顔
    show 心愛_制服_基本_嬉しい:
        zoom 1.5
        xalign 1.5618
        yalign -0.09
        linear 0.0 xalign 0.8918
        linear 0.15 xalign 0.5
    "哒"

    # nil 「私はその姿を見つけて、真冬ちゃんに一気に駆け寄ります。」
    "我看到了那个身影，一口气跑向了真冬"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぜぇ…はぁ…見つけたよ…！　真冬ちゃん！」
    show 心愛_制服_基本_真顔:
        zoom 1.5
        yalign -0.09
        xalign 0.5
    with dissolve
    voice "voice/心愛/cca_a1_1163.ogg"
    ai 心愛_制服_基本_真顔 "啊…哈……找到你了哦…！真冬酱！"
    hide 心愛_制服_基本_嬉しい

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「こ…こあちゃ…ん？」
    voice "voice/真冬/maf_a1_0886.ogg"
    dong 真冬_制服_基本_泣き "心…心爱…酱？"

    # nil 「真冬ちゃんは不思議そうな、そして申し訳なさそうな顔で私を見つめました。」
    "真冬带着不可思议和充满歉意的神情看着我"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ちょっと…お話しようか。すごく大事なお話。聞いてくれる？」
    voice "voice/心愛/cca_a1_1164.ogg"
    ai 心愛_制服_基本_真顔 "稍微…来说说话吧。这是非常重要的事情，你可以听我说吗？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「え…え…い、いけ…ど…」
    voice "voice/真冬/maf_a1_0887.ogg"
    dong 真冬_制服_基本_泣き "欸…嗯…可、可以的…说…"

    # nil 「私の提案を、真冬ちゃんは受け入れてくれました。」
    "真冬接受了我的提案"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「よし…！」
    show 心愛_制服_基本_嬉しい:
        zoom 1.5
        yalign -0.09
        xalign 0.5
    with dissolve
    voice "voice/心愛/cca_a1_1165.ogg"
    ai 心愛_制服_基本_嬉しい "好的…！"
    hide 心愛_制服_基本_真顔

    # nil 「私は、真冬ちゃんの隣に座ります。真冬ちゃんが、こちらに顔を向けるタイミングを逃がしませんでした。」
    "我坐在真冬的旁边，没有错过真冬酱把头转向我的时机"

    image bg ycg_1_1_1_1 = "images/ev/ycg_1_1_1_1.png"
    scene ycg_1_1_1_1 with dissolve

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「…んっ…ちゅっ！？」
    voice "voice/真冬/maf_a1_0888.ogg"
    dong 真冬_制服_基本_無表情 "……嗯……啾！？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ちゅー…っ！」
    voice "voice/心愛/cca_a1_1166.ogg"
    ai 心愛_制服_基本_キス "啾~……！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「んー！？　んぅー！！」
    voice "voice/真冬/maf_a1_0889.ogg"
    dong 真冬_制服_基本_キス "啊——！？嗯！！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「んぅー！　ちゅぅー！」
    voice "voice/心愛/cca_a1_1167.ogg"
    ai 心愛_制服_基本_キス "嗯——！嗯！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「んぅ…んぅう…ちゅぅ…」
    voice "voice/真冬/maf_a1_0890.ogg"
    dong 真冬_制服_基本_キス "嗯……嗯……啾……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    image bg ycg_1_1_1_2 = "images/ev/ycg_1_1_1_2.png"
    scene ycg_1_1_1_2 with dissolve

    # 心爱 「ちゅぅ…ん…ちゅりゅぅ…ちゅぅ…」
    voice "voice/心愛/cca_a1_1168.ogg"
    ai 心愛_制服_基本_キス "嗯……嗯……啾……啾……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「っ…！　んっ…ちゅぅ…はぁぅ…ちゅぅ…んっ…は、ぁっ…」
    voice "voice/真冬/maf_a1_0891.ogg"
    dong 真冬_制服_基本_キス "嗯……！啾……嗯……哈呜……哈呜……嗯……啾……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ん…ふ…ちゅ…れる…ちゅぷっ…」
    voice "voice/心愛/cca_a1_1169.ogg"
    ai 心愛_制服_基本_キス "嗯……嗯……啾……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「はあぅ…れる…ちゅっ…ちゅるっ…」
    voice "voice/真冬/maf_a1_0892.ogg"
    dong 真冬_制服_基本_キス "嗯……！啾……嗯……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ちゅぅ…ちゅりゅうっ。れるっ…」
    voice "voice/心愛/cca_a1_1170.ogg"
    ai 心愛_制服_基本_キス "啾……嗯……啾……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「はあぅ…れる…ちゅっ…ちゅるっ…」
    voice "voice/真冬/maf_a1_0893.ogg"
    dong 真冬_制服_基本_キス "嗯……！哈……嗯……啾……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「んっ、んーっ、ちゅうっ…ぷはぁっ…はぁ…はぁ…」
    voice "voice/心愛/cca_a1_1171.ogg"
    ai 心愛_制服_基本_キス "嗯…嗯！……嗯……啊哈…啊哈……啊哈……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ぷぁっ…はぁ…こあちゃ…ん…」
    voice "voice/真冬/maf_a1_0894.ogg"
    dong 真冬_制服_基本_キス "哈啊……哈啊……心爱…酱……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「真冬ちゃん…好き…ちゅっ」
    voice "voice/心愛/cca_a1_1172.ogg"
    ai 心愛_制服_基本_にっこり1 "真冬酱……喜欢……啾"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ん…すきぃ…ちゅっ…」
    voice "voice/真冬/maf_a1_0895.ogg"
    dong 真冬_制服_基本_キス "嗯……喜欢……啾……"

    # 画面切回公园河边
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 公園_夕 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    show 真冬_制服_基本_無表情 at love69_left with dissolve

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「おわかり頂けただろうか」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1173.ogg"
    ai 心愛_制服_基本_真顔 "事情就是这样您明白了吗？"

    # 莲 「だいたいわかった。もの凄くなんだ。パワープレイだな」
    lian "大体上知道了。非常厉害呢，这是力量游戏啊"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「途中から真冬ちゃんから舌絡めてきてくれたからね、頑張っちゃったよね」かり頂けただろうか」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1174.ogg"
    ai 心愛_制服_基本_嬉しい "因为从中途开始就被真冬酱用舌头缠着，所以非常努力了呢"
    hide 心愛_制服_基本_真顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「…ほんと、こういう時いつも強引だよね」
    voice "voice/真冬/maf_a1_0896.ogg"
    dong 真冬_制服_基本_無表情 "…真的，这种时候总是很强势呢"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「交渉事は苦手でね…」
    show 心愛_制服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1175.ogg"
    ai 心愛_制服_基本_真顔 "我不擅长交涉呢…"
    hide 心愛_制服_基本_嬉しい

    # 莲 「なんだ…じゃぁ俺が来るまでもなく二人は仲直りしてたんだな」
    lian "什么啊…原来在我来之前两个人就已经言归于好了啊"

    # 心爱 「私達はねー！　でも、蓮くんの気持ちはずっとわからないまだったから、モヤモヤはしてたよ！」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1176.ogg"
    ai 心愛_制服_基本_嬉しい "只是我们啊！因为，莲君的心情一直不清楚，所以有点不知所措呢！"
    hide 心愛_制服_基本_真顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ま、もしお兄ちゃんがいつまでも思いを伝えてくれなかったら、二人で付き合っちゃおうかって所までは来てた」
    # L:懂辽！莲你就是多余的那个！
    # W:莲就是应该打酱油的
    show 真冬_制服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0897.ogg"
    dong 真冬_制服_基本_目閉じ "嘛，如果欧尼酱一直不告诉我们你的想法，我们两个人就交往了"
    hide 真冬_制服_基本_無表情

    # 莲 「それは俺の人生が寂しくなるだけだからな…阻止できてよかった。お前ら二人以外と付き合うなんて今の俺じゃ考えられんからな…」
    lian "那只会让我的人生变得寂寞……能够阻止真是太好了，现在的我根本无法考虑和你们两人以外的人交往"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そんな事言っちゃって…もう…いかな…」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0898.ogg"
    dong 真冬_制服_基本_微笑み "说了那样的话…已经…不行了…"
    hide 真冬_制服_基本_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「むぅ…そうだね…私もこれ以上我慢できないかも」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1177.ogg"
    ai 心愛_制服_基本_笑顔 "嗯……是的啊…我可能也再忍不住了"
    hide 心愛_制服_基本_嬉しい

    # 莲 「へ？」
    lian "嗯？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「毎度毎度、言う事が直球すぎるんだよお兄ちゃんは…」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0899.ogg"
    dong 真冬_制服_基本_無表情 "每次每次，你说话都太直来直去了，欧尼酱……"
    hide 真冬_制服_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「そーだよ。もー…乙女心をわかってるよーでわかってないよーで！もう、知らないからね！」
    # ai "就是啊，真是的……也完全不管知不知道少女心！真是的，不是不知道嘛！"
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1178.ogg"
    ai 心愛_制服_基本_不機嫌 "就是啊，真是的……也完全不管少女心！我康你，是完全不懂哦！"
    hide 心愛_制服_基本_笑顔

    # 莲 「お、おいおい、怒らないでおくれよ」
    lian "呐，喂，不要生气哦嘛"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「違う。怒ってるんじゃなくて…」
    show 真冬_制服_基本_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0900.ogg"
    dong 真冬_制服_基本_目閉じ "不是，我不是生气"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「真冬ちゃん…」
    show 心愛_制服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1179.ogg"
    ai 心愛_制服_基本_嬉しい "真冬酱……"
    hide 心愛_制服_基本_不機嫌

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うんっ…」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0901.ogg"
    dong 真冬_制服_基本_微笑み "嗯……"
    hide 真冬_制服_基本_目閉じ

    # nil 「二人は頷いた後、ぎゅっと両腕にしがみついてきた。」
    "两个人点点头，紧紧抓住我的胳膊"

    # nil 「両腕に押しつけられた二人の胸から、高鳴った鼓動が伝わってくる。それだけじゃなく、二人とも気恥ずかしそうに、太もをすり合わせている。」
    "被双臂压住的两人的胸口，传来了激动的心跳。不仅如此，两个人都很害羞地互相摩擦着大腿"

    # nil 「彼女達がどんな気分になっているかは、想像に容易い。」
    "她们是什么心情，很容易想象"

    # nil 「そして俺も…。」
    "然后我也…"

    # 真冬 「家…かえろ…？　もう、ドキドキ収まらないよ…」
    voice "voice/真冬/maf_a1_0902.ogg"
    dong 真冬_制服_基本_微笑み "家……回去吧…？我的心，已经dokidoki地停不下来了呢……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「うん。好きって気持ちが抑えきれないよぉ…二人に…蓮君をちょうだい…？」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1180.ogg"
    ai 心愛_制服_基本_笑顔 "嗯，喜欢你们的心情我已经控制不住了…两个人……把莲君给……？"
    hide 心愛_制服_基本_嬉しい

    # 莲 「あ、あ…わかった。帰るか…二人とも歩けるか？」
    lian "啊，啊…知道了，我们回去吧…两个人这样都还能走吗？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「なんとか…でも、お兄ちゃんとくっついてなきゃやだ…」
    show 真冬_制服_基本_泣き at love69_left with dissolve
    voice "voice/真冬/maf_a1_0903.ogg"
    dong 真冬_制服_基本_泣き "总觉得……但是，不和欧尼酱黏在一起是不行的…"
    hide 真冬_制服_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「おうちまでずっと離さないでね…！」
    # 参考资料：https://www.weblio.jp/content/%E3%81%8A%E3%81%86%E3%81%A1
    # おうち お‐うち【▽御内／▽御▽家】 指代自己家的一种礼貌方式
    voice "voice/心愛/cca_a1_1181.ogg"
    ai 心愛_制服_基本_笑顔 "请永远不要离开我们的家哦……！"

    # 莲 「あ。離さないからな。愛してるよ、二人とも」
    lian "啊，我不会离开的。我爱你们，两个人都是"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 真冬&心爱 「『は、ぁうっ…ば、ばかぁっ…』」
    show 心愛_制服_基本_不機嫌 at love69_right with dissolve
    # voice "voice/真冬/maf_a1_0904.ogg"
    # voice "voice/心愛/cca_a1_1182.ogg"
    ### 音频实在没有找到，拿录屏的先放上去
    #### 不过发现了个非常好用的库，回头可以讲讲
    ##### https://github.com/charlesconnell/AudioCompare
    ## 这里不知道为啥，没有正常显示头像捏
    ### 是 image 写错了，注意简繁体
    # voice "voice/s9_4383（は、ぁうっ…ば、ばかぁっ…）.ogg"
    # 找到了，原作又在乱放文件了
    voice "voice/その他/ex2_a1_0002.ogg"
    dong_ai 心愛_制服_基本_不機嫌 "哈、啊啊啊……笨、笨蛋……"
    hide 心愛_制服_基本_笑顔

    # nil 「二人は同時に身体をビクっと跳ねさせた。俺の興奮もヒートアップしてきてしまう。」
    "两个人的身体同时一跳，我的兴奋感也高涨起来"

    # nil 「これは急いで帰ろう。」
    "这会儿就赶紧回去吧"

    # nil 「そして…二人と…三人で愛し合おう。」
    "然后…两个人…三个人一起相爱吧"

    # nil 「そう心に決めた。」
    "我这样下定了决心"

    # nil 「……」
    "……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ってバイクで来たんかーい！」
    voice "voice/心愛/cca_a1_1182.ogg"
    ai 心愛_制服_基本_不機嫌 "啊，你原来是骑摩托车来的啊！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「三人乗りは無理だよお兄ちゃん…」
    show 真冬_制服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0904.ogg"
    dong 真冬_制服_基本_無表情 "三个人一起坐是不可能的欧尼酱……"
    hide 真冬_制服_基本_泣き

    # 莲 「すんませんでした…」
    lian "对不起……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「鍵とメット貸して。心愛ちゃんは後ろ乗ってね」
    show 真冬_制服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0905.ogg"
    dong 真冬_制服_基本_微笑み "把钥匙和头盔给我，心爱酱就坐在后面吧"
    hide 真冬_制服_基本_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はーい！　まふまふちゃんの後ろ乗るのひさしぶりー！」
    show 心愛_制服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1183.ogg"
    ai 心愛_制服_基本_笑顔 "好——！好久没有坐在嘛呼嘛呼酱后面了"
    hide 心愛_制服_基本_不機嫌

    # 莲 「え、俺は！？」
    lian "欸、我呢！？"

    # 真冬&心爱 「『ダッシュ！』」
    # 坏了，这个也跳过了
    # voice "voice/真冬/maf_a1_0906.ogg"
    # voice "voice/心愛/cca_a1_1184.ogg"
    # voice "voice/dash.ogg"
    # 找到了，原作又在乱放文件了
    voice "voice/その他/ex2_a1_0003.ogg"
    dong_ai 心愛_制服_基本_笑顔 "dash！"

    # 莲 「まじすか！　っておい！　容赦なしかよ！」
    lian "真的吗！喂！一点面子都不给留的嘛！"

    # nil 「俺の叫び声をよそに、真冬は思いっきりフルスロットルで心愛を乗せて走り去っていってしまった。」
    "不顾我的喊叫声，真冬载着心爱走了，尽情地全速前进"

    # 莲 「…息子よ、もう少しの我慢だ。頑張れよ」
    lian "…儿子啊，再忍耐一下，加油"

    # nil 「俺はそう息子に言い聞かせて、クラウチングスタートで家路を急いだ。」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%AF%E3%83%A9%E3%82%A6%E3%83%81%E3%83%B3%E3%82%B0%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88
    "我这样告诉儿子，以crouch start（L:蹲踞式起跑，1896年雅典奥运会上美国田径运动员托玛斯·伯克创造的起跑方法，目前短跑比赛中普遍采用“蹲踞式”的起跑技术）赶回了家"

    # scene09 场景4 【二人一起努力，让三个人一起幸福吧】 结束

    # scene09 结束
    # 这个 scene09 的文本量可是有点大，差不多有一个 scene01 了都，有点哈人捏，终于做完啦！

    # 过场：心爱（常服）

    # 隐藏 quick_menu
    $ quick_menu = False

    play sound "voice/effect/moosehead honk (stinger).ogg"
    play music bgmtwentyfour fadein 4.0
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)
    scene アイキャッチ心愛 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)
 
    $ renpy.pause(1.5, hard=True)

    jump scene10
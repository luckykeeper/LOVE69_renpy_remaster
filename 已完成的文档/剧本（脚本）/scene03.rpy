# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene03 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：
# 版本 0.7 "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年3月27日

# 当前流程：编写脚本AIO Process

label scene03:
    # scene03 开始
    # 地点：街道
    # 人物：心爱 莲
    # BGM：bgm36

    # scene03 场景1 【和心爱的归家路】 开始
    # 实现渐变效果，需要增大阶数，默认的ramplen=8改到128效果比较好
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)

    image bg 通学路d_夜 = "images/bg/通学路d_夜.png"
    # 这里也是，调整到64比较好
    scene 通学路d_夜 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    $ quick_menu = True

    # 莲 「さて」
    lian "那么"

    # 心爱 「ふむ」
    show 心愛_大_制服_基本_真顔1 at love69_xinai_bg_center with dissolve
    # voice "voice/心愛/cca_a1_0295.ogg"
    # 295-313 跳过 听了一下，原作是把一二周目的音声放在一起了，跳过的部分是二周目的内容
    voice "voice/心愛/cca_a1_0314.ogg"
    ai 心愛_制服_基本_真顔1 "嗯姆"

    # nil 「公園でのイチャイチャの後、俺達は特にこれといった会話もなく、だらだらと徒歩で家路を進んでいた。」
    "在公园里打情骂俏之后，我们没有什么特别的交谈，而是懒懒散散地走向回家的路"

    # 莲 「で」
    lian "呐"

    # 心爱 「うむ」
    voice "voice/心愛/cca_a1_0315.ogg"
    ai 心愛_制服_基本_真顔1 "唔姆"

    # nil 「公園でのイチャイチャの後、俺達は特にこれといった会話もなく、だらだらと徒歩で家路を進んでいた。」
    "还是老样子，我和心爱牵着手，彼此都不想分开"

    # nil 「強いて述べるとしたら、指と指を絡めるような手の繋ぎ方になっている。」
    "如果硬要说的话，那就是手指交叉的那种连接方法"

    # 莲 「さっきのキャラメルアップルもういっこちょうだい」
    lian "请再给我一个刚才的奶糖苹果"

    # 心爱 「さっきので最後だよ」
    show 心愛_大_制服_基本_嬉しい at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0316.ogg"
    ai 心愛_制服_基本_嬉しい"刚才是最后一个辽"
    hide 心愛_大_制服_基本_真顔1

    # 莲 「無限に出てくるわけじゃないのか」
    lian "原来不是无穷无尽的吗"

    # 心爱 「蓮くんが食べちゃったから、もう出ないんだなー」
    show 心愛_大_制服_基本_泣き at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0317.ogg"
    ai 心愛_制服_基本_泣き "因为莲君吃了，所以已经出不来了哦"
    hide 心愛_大_制服_基本_嬉しい

    # 莲 「そうか」
    lian "是这样的嘛"

    # nil 「もしかして、食べたものを出しているのか…？　まぁい、どちらにせよ考えてもラチがあかん。」&协力请求
    "难道是悄悄地把吃的都拿出来了吗…？不管怎么想都想不通"

    # 心爱 「もぐもぐ」
    show 心愛_大_制服_基本_もぐもぐ at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0318.ogg"
    ai 心愛_制服_基本_もぐもぐ "咀嚼咀嚼"
    hide 心愛_大_制服_基本_泣き

    # 莲 「それなに？」
    lian "那是什么？"

    # 心爱 「火曜日」
    show 心愛_大_制服_基本_真顔 at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0319.ogg"
    ai 心愛_制服_基本_真顔 "星期二"
    hide 心愛_大_制服_基本_もぐもぐ

    # 莲 「そうか」
    lian "是吗？"

    # nil 「思えば心愛は、幼い頃からどこか不思議な奴だった。」
    "细细想来，心爱从小就让人觉得不可思议"

    # nil 「公園に行けば、エサも持ってないのにハトが群がるし、サツマイモを掘ってるはずなのに、土偶を発掘するし、スネアを叩いたのにハイハットが鳴るし。」
    # 参考资料：https://ja.wikipedia.org/wiki/土偶
    # 参考资料：https://ja.wikipedia.org/wiki/ドラムセット
    "去公园的时候，明明没有食物，鸽子却成群结队地聚集在边上，明明是在挖红薯，却发掘出来了土偶（L:是人形陶土制品，日本绳文时代的代表性遗物），明明是敲了小鼓，响的却是脚踏钹（L:这两样都是架子鼓上面的乐器）"

    # nil 「なんだか、俺達が居る世界から少しズレた所に存在しているような。」
    "总觉得，她好像存在于和我们所在的世界稍微有点偏差的地方"

    # 心爱 「んー？　欲しい－？　あげないよー？」
    show 心愛_大_制服_基本_ニタァ at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0320.ogg" # （L:这句原版是忘记放配音了2333）
    ai 心愛_制服_基本_ニタァ "嗯? 想要吗? 不给你哦?"
    hide 心愛_大_制服_基本_真顔

    # 莲 「おう、ゆっくり食えよ」
    lian "哦，那你慢慢吃吧"

    # 心爱 「もぐもぐ…ごくっ…もぐもぐ…うみゃい…」
    show 心愛_大_制服_基本_もぐもぐ at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0321.ogg"
    ai 心愛_制服_基本_もぐもぐ "唔姆唔姆…嗯…哈啊…唔姆唔姆…唔咩"
    hide 心愛_大_制服_基本_ニタァ

    # nil 「だが、物心ついてから心愛と時間を共にしている俺（と真冬）にとって、心愛は普通の女の子である事に変わりはない。」
    "但是，对于从懂事开始就和心爱在一起的我（和真冬）来说，心爱是普通的女孩子这件事是不会变的"

    # nil 「当然の認識だ。」
    "这是理所当然的事情"

    # 心爱 「ごくごく…ぷはー…」
    voice "voice/心愛/cca_a1_0322.ogg"
    ai 心愛_制服_基本_もぐもぐ "咕咕...噗哈~..."

    # 莲 「で」
    lian "呐"

    # 心爱 「うむ」
    show 心愛_大_制服_基本_真顔 at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0323.ogg"
    ai 心愛_制服_基本_真顔 "唔姆"
    hide 心愛_大_制服_基本_もぐもぐ

    # nil 「さて、そろそろ突っ込んだ方が良い頃合いか。」
    "那么，差不多该吐槽了吧"

    # 莲 「うち、来るの？」
    lian "我家，要来吗？"

    # 心爱 「へ？」
    show 心愛_大_制服_基本_驚き at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0324.ogg"
    ai 心愛_制服_基本_驚き "嗯？"
    hide 心愛_大_制服_基本_真顔

    # 莲 「お前の家通り過ぎたぞ」
    lian "我们已经走过你家了哦"

    # 心爱 「あ゛…あ゛ー…いやーこれがお恥ずかしゅうながらですね、この手を離すのが名残惜しかったと、いますか、はい」
    show 心愛_大_制服_基本_嬉しい at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0325.ogg"
    ai 心愛_制服_基本_嬉しい "啊、啊———— 呀、虽然很不好意思说出来这个，但是我舍不得放开你的手、是这样的"
    hide 心愛_大_制服_基本_驚き

    # 心爱 「えーこのー…おー…ね！　ほら！」
    show 心愛_大_制服_基本_にっこり1 at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0326.ogg"
    ai 心愛_制服_基本_にっこり1 "啊……这个……哦……呐! 你看呢!"
    hide 心愛_大_制服_基本_嬉しい


    # 莲 「や、来るのは構わんけど…流石に、真冬に見られたら末代までネタにされると思うんだが…」
    lian "emmm，来倒是没关系……不过，如果真冬看到的话，我想以后大概会成为话题……"

    # 心爱 「た、確かに！」
    show 心愛_大_制服_基本_泣き at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0327.ogg"
    ai 心愛_制服_基本_泣き "雀、雀食! "
    hide 心愛_大_制服_基本_にっこり1

    # 百叶窗效果，切回莲/真冬家门口
    # BGM 不变
    # 人物：莲 心爱 真冬

    image bg 自宅_夜_消灯 = "images/bg/自宅_夜_消灯.png"
    scene 自宅_夜_消灯 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「俺の自宅にたどり着くと、心愛からそっと繋いだ手を離した。」
    "到了我家门口，我放开了和心爱牵着的手"

    # 莲 「電気ついてねぇな」
    lian "灯没开啊"

    # 心爱 「寝てる？」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0328.ogg"
    ai 心愛_制服_基本_真顔 "睡着了?"

    # 莲 「もしくは自分の部屋でカーテン締め切って映画館ごっこしてる」
    # 参考资料：https://m-m2009.com/outi-eigakangokko/
    lian "或者是在自己的房间里拉上窗帘玩电影院游戏呢？（L:所谓“电影院游戏”，就是在家模拟电影院的感觉，通常会营造黑暗的氛围，制作电影票，准备爆米花。11区的一些家长喜欢和孩子玩这样的游戏）"

    # 心爱 「しかも５１型ホームシアターでな。７．１ｃｈサラウンドシステムだ」
    show 心愛_制服_基本_無表情 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0329.ogg"
    ai 心愛_制服_基本_無表情 "而且是51型家庭影院，7.1声道环绕声系统（L:这里的51型应该是指51寸，翻译君要馋哭了，我这儿连音响都没有，用的耳机还是从柜子里面翻出来的联想零几年的老式耳机，前天才自己修了一次）"
    hide 心愛_制服_基本_真顔

    # 莲 「人の台詞をとるなよ」
    lian "不要抢别人的台词啊喂"

    # 心爱 「はい鍵」
    show 心愛_制服_基本_微笑み at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0330.ogg"
    ai 心愛_制服_基本_微笑み "给，钥匙"
    hide 心愛_制服_基本_無表情

    # 莲 「はい」
    lian "嗯"

    # nil 「心愛から家の鍵を受け取って、ドアノブの鍵穴に差し込む。」
    "从心爱那里接过房子的钥匙，插进门把手下面的锁孔里"

    # nil 「ガチャッ」
    "喀嚓"

    # 心爱 「入って、どうぞ」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0331.ogg"
    ai 心愛_制服_基本_真顔 "来，请进~（L:游戏开场的欢迎声就是这句哦~做Demo版的时候可是让我一顿好找233）"
    hide 心愛_制服_基本_微笑み

    # 莲 「お邪魔しまーす」
    lian "打扰了"

    # scene03 场景1 【和心爱的归家路】 结束

    # scene03 场景2 【和心爱的晚饭时间】 开始

    image bg 玄関_夜_消灯 = "images/bg/玄関_夜_消灯.png"
    scene 玄関_夜_消灯 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # 心爱 「まふまふちゃーん、ただいまー」
    show 心愛_制服_基本_にっこり at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0332.ogg"
    ai 心愛_制服_基本_にっこり "嘛呼嘛呼酱，我回来啦~"

    # nil 「……」
    "……"

    # nil 「玄関の扉を開けて、中の電気を付ける。」
    "进入玄关的门，把灯打开"

    # 灯亮
    image bg 玄関_夜 = "images/bg/玄関_夜.png"
    scene 玄関_夜 at love69_bg1440

    # 修改一下原作的效果，让心爱连续出现
    show 心愛_制服_基本_にっこり at love69_xinai_center
    with Dissolve(0.2)

    # 莲 「いねぇのかな。靴がねぇや」
    lian "是没在吗？没看到鞋子呢"

    # 心爱 「まだ帰って来てないパターン？」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0333.ogg"
    ai 心愛_制服_基本_泣き "是还没回来的模式（MODE）吗？"
    hide 心愛_制服_基本_にっこり

    # 莲 「もしくはどっかでかけてるんかね」
    lian "也可能又到别的地方逛去了"

    # 莲 「真冬ー。おめぇの好きな心愛ちゃんを買ってきたぞ！しかも輸入物のな！」
    lian "真冬——!我给你买了你最喜欢的心爱酱!而且还是进口的"

    # 心爱 「いえ国産です！」
    show 心愛_制服_基本_驚き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0334.ogg"
    ai 心愛_制服_基本_驚き "不对，是国产的！"

    # nil 「やはり応答は返ってこない。爆音で映画を見てるなら、玄関まで漏れてくるだろうし、居ないと言う事で一つ。」
    "还是没有回应。如果是在看电影的话，电影里面的爆炸声在玄关应该就能听到，也就是说真冬不在捏"

    # 莲 「居ないようだな」
    lian "好像不在啊"

    # 心爱 「ほへー。じゃぁ、ご飯でも作って待ってあげよう」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0335.ogg"
    ai 心愛_制服_基本_嬉しい "咕嘿——那么，我去做饭，你去等着吧"
    hide 心愛_制服_基本_驚き

    # 莲 「そうしましょう」
    lian "就这么办吧"

    # 场景切换到客厅
    image bg リビングa_夜 = "images/bg/リビングa_夜.png"
    scene リビングa_夜 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「心愛と俺は靴を脱いで、リビングへとあがる。」
    "我和心爱脱掉鞋子，去了客厅"

    # nil 「リビングの様子は、朝俺が家を出てきた時と何も変わっちゃいなかった。」
    "客厅的样子和早上我从家里出来的时候并没有什么不同"

    # nil 「どうやら、帰って来てすらもいないようだ。」
    "显然，真冬没有回来"

    # nil 「適当に通学鞄を隅に投げ置いて、椅子に座る。」
    "随便地把书包扔在角落里，坐在椅子上"

    # nil 「テレビでもつけようと思ったが、手を伸ばしても届かない位置にあったのでやめた。」
    "本想把电视也打开，但因为现在处于伸手也够不到的位置，所以就放弃了"

    # 心爱 「よっしゃぁー！　そんじゃ、いっちょ晩ご飯作っちゃうよー！」
    show 心愛_制服_基本_ニタァ at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0336.ogg"
    ai 心愛_制服_基本_ニタァ "好耶！那就来做晚饭吧！"
    hide 心愛_制服_基本_嬉しい

    # 莲 「久しぶりだな、心愛ちゃんの手料理」
    lian "好久没恰过了，心爱酱亲手做的料理"

    # 心爱 「いつも、まふまふちゃんか、蓮くんが作っちゃうからね」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0337.ogg"
    ai 心愛_制服_基本_泣き "因为一直都是嘛呼嘛呼酱或者莲君做的呢"
    hide 心愛_制服_基本_ニタァ

    # 莲 「確かに」
    lian "雀食"

    # nil 「心愛が腕まくりをして、台所へ向かう。手際の良いことだ。」&可能翻的有问题，这里手際の良いことだ也可能是说心爱真聪明，不过结合语境感觉这里可能还是说莲君觉得自己干的真不戳
    "心爱卷起袖子，走向厨房。我干得漂亮啊！"

    # nil 「ん？　あいつ半袖なのにどうやって腕まくりしたの？…まぁいや。」
    "嗯？那家伙明明是穿着短袖的，是怎么挽起袖子的？…嘛，不管了"

    scene black
    scene リビングa_夜 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 心爱 「んしょ…んしょー…」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0338.ogg"
    ai 心愛_制服_基本_真顔 "嘿咻…嘿咻——…"
    hide 心愛_制服_基本_泣き

    # 莲 「手伝うか？」
    lian "需要帮忙吗？"

    # 心爱 「あ、うん。蓮くんは座っていよ！」
    show 心愛_制服_基本_笑顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0339.ogg"
    ai "嗯，不需要了，莲君坐着就好"
    hide 心愛_制服_基本_真顔

    # 莲 「そうか。手伝いが必要になったら言ってくれ」
    lian "这样啊。需要帮忙的话就和我说哦"

    # 心爱 「はーい。　んしょ…ん…しょ…」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0340.ogg"
    ai 心愛_制服_基本_真顔 "好——嘿咻…嘿咻…"
    hide 心愛_制服_基本_笑顔

    # 莲 「……」
    lian "……"

    # 心爱 「はーい。　んしょ…ん…しょ…」
    show 心愛_制服_基本_無表情 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0341.ogg"
    ai 心愛_制服_基本_無表情 "嘿咻…咕拗拗…嗯—咻…"
    hide 心愛_制服_基本_真顔

    # 莲 「手伝うか？」
    lian "需要帮忙吗？"

    # 心爱 「え、いよぉ。大丈夫！　蓮くんにご迷惑をおかけられませんて！」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0342.ogg"
    ai 心愛_制服_基本_嬉しい "啊，不需要的啦。没关系！我不会给莲君添麻烦的！"
    hide 心愛_制服_基本_無表情

    # 莲 「だって心愛ちゃん、貴方エプロンの後ろのヒモが結べなくてずっと格闘してるんですもの」
    lian "但是心爱酱，我看你围裙后面的绳子系不上，一直较着劲儿呢"

    # 心爱 「だぁもうエプロンなんていらねぇんだよっ！」
    show 心愛_制服_基本_不機嫌 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0343.ogg"
    ai 心愛_制服_基本_不機嫌 "啊真是的我已经不需要围裙了！"
    hide 心愛_制服_基本_嬉しい

    # 莲 「キレんなよ！　制服汚れちゃったら大変だろ！」
    lian "别生气啊！制服脏了可就不好了！"

    # 心爱 「そしたらクリーニングに出してやるまでだ」
    show 心愛_制服_基本_覚醒 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0344.ogg"
    ai 心愛_制服_基本_覚醒 "这样的话只需要送去洗衣店就好了"
    hide 心愛_制服_基本_不機嫌

    # 莲 「そりゃその通りだと思う」
    lian "好像是这个理儿"

    # 原地tp
    scene black
    scene リビングa_夜 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 心爱 「ウヒョオオオオオ！　ミキサーだァアアアア！」
    show 心愛_制服_基本_笑顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0345.ogg"
    ai 心愛_制服_基本_笑顔 "Whoo-hoo!——是搅拌机哒"
    hide 心愛_制服_基本_覚醒

    # nil 「ウイイイイイイイイイン」
    "嗡嗡嗡嗡嗡嗡嗡嗡嗡嗡嗡嗡"

    # 莲 「ほれ、バナもあるぞ」
    lian "看，还有香蕉呢"

    # 心爱 「ヤッタアアアアアアアアアアア！」
    voice "voice/心愛/cca_a1_0346.ogg"
    ai 心愛_制服_基本_笑顔 "好耶——！"

    # nil 「ウイイイイイイイイイン」
    "嗡嗡嗡嗡嗡嗡嗡嗡嗡嗡嗡嗡"

    # 心爱 「…バナが…細切れになったよ…」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0347.ogg"
    ai 心愛_制服_基本_泣き "…啊…香蕉它…碎掉了呢……"
    hide 心愛_制服_基本_笑顔

    # 莲 「牛乳とか入れないとダメだな」
    lian "不加点儿牛奶不行啊"

    # 心爱 「そうですね…」
    voice "voice/心愛/cca_a1_0348.ogg"
    ai 心愛_制服_基本_泣き "是呢…"

    # 原地tp
    scene black
    scene リビングa_夜 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 心爱 「それでは葛城隊長、冷蔵庫を開ける許可を下さい」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0349.ogg"
    ai 心愛_制服_基本_真顔 "那么葛城队长，请允许我打开冰箱"

    # 莲 「そんなん許可しなくても勝手に開ければいじゃないか」
    lian "不需要征得我的许可，直接打开就好啦"

    # 心爱 「いやーこの前テレビでやってたのですよ。フライパンに張り付いた餃子を剥がすには、濡れたタオルの上に置くと良いって」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0350.ogg"
    ai 心愛_制服_基本_嬉しい "呀——之前在电视上播过呢。要把贴在平底锅上的饺子剥下来，最好放在湿毛巾上呢"
    hide 心愛_制服_基本_真顔

    # 莲 「冷蔵庫関係ねぇ！」
    lian "这和冰箱没关系啊！"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene リビングa_夜 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 心爱 「隊長…事件発生です」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0351.ogg"
    ai 心愛_制服_基本_真顔 "队长... ... 出事了"

    # 莲 「なんだね心愛隊員」
    lian "什么事，心爱队员"

    # 心爱 「…冷蔵庫に…」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0352.ogg"
    ai 心愛_制服_基本_泣き "在冰箱里面……@#$!^&*@#!@#$!^&*@#!（L:原文：“冷蔵庫に”后面那句话没有字，应该是被吓到了开始胡言乱语了）"
    hide 心愛_制服_基本_真顔

    # 莲 「あれ？　もしかして、食材きらしてたとか？」
    lian "咦？莫非看到了讨厌的食材了？"

    # 心爱 「クマちゃんのぬいぐるみがァ！」
    show 心愛_制服_基本_驚き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0353.ogg"
    ai 心愛_制服_基本_驚き "是小熊的玩偶啊！"
    hide 心愛_制服_基本_泣き

    # 莲 「真冬の趣味だな」
    lian "这是真冬的爱好"

    # 心爱 「キンキンに冷えていらっしゃる…食べれるのかなこれ」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0354.ogg"
    ai 心愛_制服_基本_嬉しい "这东西被冻得硬邦邦的了... ... 能恰这个吗"
    hide 心愛_制服_基本_驚き

    # 莲 「やった事ねぇけど、多分ダメだと思うぜ」
    lian "我没试过，但是我觉得大概不行哦"

    # 心爱 「ちぇー」
    show 心愛_制服_基本_不機嫌 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0355.ogg"
    ai 心愛_制服_基本_不機嫌 "切——"
    hide 心愛_制服_基本_嬉しい

    # 原地tp
    # 音效：电话震动
    # pac:call
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene リビングa_夜 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    play sound "voice/effect/17_携帯電話着信バイブ音.ogg"
    show screen callscr

    # 心爱 「はあうっ！」
    show 心愛_制服_基本_驚き at love69_xinai_center
    show 心愛_制服_基本_驚き:
        zoom 1.5
        xalign 0.53
        yalign -0.09
        linear 0.15 yalign -0.01
        linear 0.15 yalign -0.09
    voice "voice/心愛/cca_a1_0356.ogg"
    ai 心愛_制服_基本_驚き "哈啊!"

    hide screen callscr

    # 莲 「突然どうした」
    lian "突然怎么了？"

    # nil 「台所に向かっていた心愛の身体が嬌声と共に大きく跳ねる。」
    "走向厨房的心爱的身体随着娇声大幅跳动"

    # 心爱 「いや…携帯のバイブがクリーンヒットしたの…」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0357.ogg"
    ai 心愛_制服_基本_泣き "没怎么...只是被手机振动准确命中了..."
    hide 心愛_制服_基本_驚き

    # 莲 「変な所に入れてるからだ」
    lian "所以你为啥把手机放在那种地方呢"

    # 心爱 「し、失敬な！　別にそんな所に入れたりしてないよ！」
    show 心愛_制服_基本_不機嫌 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0358.ogg"
    ai 心愛_制服_基本_不機嫌 "真、真没礼貌! 我才没有放在奇奇怪怪的地方呢"
    hide 心愛_制服_基本_泣き

    # 莲 「どこの話だと思ってるんだ」
    lian "你以为我是在说什么地方？"

    # 心爱 「そりゃ…なんでもない、なんでもない！」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0359.ogg"
    ai 心愛_制服_基本_泣き "那是…没什么，没什么！"
    hide 心愛_制服_基本_不機嫌

    # 音效：手机震动
    play sound "voice/effect/17_携帯電話着信バイブ音.ogg"

    # 心爱 「はぁうっ」
    hide 心愛_制服_基本_泣き
    show 心愛_制服_基本_驚き:
        zoom 1.5
        xalign 0.53
        yalign -0.09
        linear 0.15 yalign -0.01
        linear 0.15 yalign -0.09
    voice "voice/心愛/cca_a1_0360.ogg"
    ai 心愛_制服_基本_驚き "哈呜——"

    # 莲 「早く取れよ楽しんでないで」
    lian "赶紧拿出来吧，别玩得开心过头了"

    # 心爱 「たっ楽しんでないもん～！　う～！　もぉー…」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0361.ogg"
    ai 心愛_制服_基本_泣き "一、一点都不开心的啦……呜…真是的！"
    hide 心愛_制服_基本_驚き

    # 莲 「お前こういう事だけ、恥ずかしがり屋だよな」
    lian "你大概是唯一一个对这种事情感到害羞的人吧"

    # 心爱 「ひとつぐらい例外はあるもんなんですよ…」
    voice "voice/心愛/cca_a1_0362.ogg"
    ai 心愛_制服_基本_泣き "总有例外的嘛"

    # nil 「心愛は頬を赤く染めながら、そっとスカートの中から携帯電話を取りだした。」
    "心爱红着脸，悄悄地从裙子里拿出了手机"

    # nil 「マジで変な所にしまってんな。」
    "真的是放在奇奇怪怪的地方了呢"

    # nil 「ケーキのようにデコられたスマートフォンのタッチパネルを操作して、耳にあてた。」
    "她操作着装饰得像蛋糕一样的手机，贴在了耳朵上"

    # 心爱 「はいはーいもしもーし。どなたでございま…あ、まふまふちゃん！？なんでオイラの携帯に…え？　はいはい」
    show 心愛_制服_基本_笑顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0363.ogg"
    ai 心愛_制服_基本_笑顔 "喂——喂，听得到吗，请问是谁啊…啊，嘛呼嘛呼酱！？为什么要打我的手机…啊？好的好的"
    hide 心愛_制服_基本_泣き

    # 心爱 「ちょいちょい、葛城兄さん、お前さんの携帯はどこでやんすか」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0364.ogg"
    ai 心愛_制服_基本_嬉しい "戳、戳，葛城哥哥，你的手机放在了哪里呢？"
    hide 心愛_制服_基本_笑顔

    # 莲 「ん？　定位置なら…ズボンの右ポケットに…入って、ねぇな」
    lian "嗯? 如果是固定位置的话...放在裤子的右边口袋里...出来吧，嘿!"

    # 心爱 「見つからない？」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0365.ogg"
    ai 心愛_制服_基本_真顔 "找不到了吗？"
    hide 心愛_制服_基本_嬉しい

    # 莲 「いや…」
    lian "emmm…"

    # nil 「全身を叩いて場所を探す。すると、制服の上着のポケットに硬い感触がある。」
    "拍打着全身各个地方。突然，感觉制服上衣口袋里有种硬邦邦的感觉"

    # 莲 「んお。そうか、こんな所に…で、俺の携帯が何か…うお」
    lian "嗯。是在这里的嘛...然后，我的手机怎么了...哦"

    # nil 「携帯電話のスリープを解除して、モニターの電源をつける。」
    "解除手机的睡眠状态，打开屏幕的电源"

    # 莲 「着信が３２回入ってる。しかも全部真冬だ」
    lian "有32个来电，而且都是真冬"

    # 心爱 「…えー、まふまふちゃん。お兄ちゃんは、たった今着信を知ったそうです。やれやれですね。あ、代わる？　ほーい」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0366.ogg"
    ai 心愛_制服_基本_嬉しい " ......欸，嘛呼嘛呼酱。欧尼酱刚刚知道来电的事情了。真是的呢，要让他接电话吗? 好~的"
    hide 心愛_制服_基本_真顔

    # nil 「心愛がノールックで俺にスマートフォンを投げ渡す。俺の手の中にすっぽり収まったスマートフォンを耳に当てる。」
    "心爱不露声色地把手机扔给我，我准确地接住了，然后手机贴在耳朵上"

    # 这个语句是针对电话里的真冬设计的参数，能够调整电话里的真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.04
    $ sideimagesize.SideImageYalign = 1.04
    $ sideimagesize.SideImageZoom = 0.6

    # 真冬 「はろー、鈍感ブラザー」
    # voice "voice/真冬/maf_a1_0153.ogg" 依然不是按顺序来的
    # 153-175 跳过
    voice "voice/真冬/maf_a1_0176.ogg"
    dong 真冬_通話中 "『hello~钝感哥哥』"

    # 莲 「ちょっとした想定外だ。　で、３２回も俺に電話かけたあげく、心愛の感じる部分を刺激してまで電話したかった理由を聞こうか」
    lian "有点意料之外呢。那么，在给我打了32次电话之后，我想问下你为什么想打电话来刺激心爱的那个地方捏"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「か、感じてないぷー！」
    show 心愛_制服_基本_不機嫌 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0367.ogg"
    ai 心愛_制服_基本_不機嫌 "才、才没感觉到呢！"
    hide 心愛_制服_基本_嬉しい

    # 这个语句是针对电话里的真冬设计的参数，能够调整电话里的真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.04
    $ sideimagesize.SideImageYalign = 1.04
    $ sideimagesize.SideImageZoom = 0.6

    # 真冬 「今日、晩ご飯要らないよ、想瑠にゃんの家でご馳走になるから。という情報から、今夜お泊まりしますに更新されました」
    voice "voice/真冬/maf_a1_0177.ogg"
    dong 真冬_通話中 "『今天不需要做我的晚饭了，想瑠喵家今天晚上请客。有这样的消息，所以今天晚上要在那边留宿』"

    # 莲 「泊まる？　どこに？」
    lian "过夜? 住在哪里呢"

    # 真冬 「想瑠にゃんの家。なんか、あろうことか、想瑠にゃんモンスターエナジー飲んでハイになっちゃって、友達呼んでパーティ始まっちゃった感じで、帰れる空気じゃない」
    voice "voice/真冬/maf_a1_0178.ogg"
    dong 真冬_通話中 "『想瑠喵的家。怎么说呢，想瑠酱喝了怪物能量饮料就变high了，然后叫了朋友开始派对了，不是可以回去的气氛呢』"

    # nil 「声『今日こそてめぇをぶっ倒してやるからなァ霧葉ちゃんよぉ…いくぜオィ！』」
    # voice "voice/想瑠/sol_a1_0037.ogg"
    # 37-73 跳过
    voice "voice/想瑠/sol_a1_0074.ogg"
    "（电话里的声音）『今天一定要把你这家伙打倒啊，雾叶酱啊…上吧！』"

    # nil 「声『Don't get so cocky』」
    voice "voice/霧葉/krh_a1_0054.ogg"
    # 这里不需要跳过
    "（电话里的声音）『Don't get so cocky』（L:和我一起来学嘤语吧！cocky，自大的; 自以为是的; 过分自信的。所以这句可以翻为“别这么嚣张”）"

    # nil 「声『ぐわあー！　腕が曲がってはいけない方向に！』」
    voice "voice/想瑠/sol_a1_0075.ogg"
    "（电话里的声音）『呜哇！手臂朝着不能弯曲的方向！』"

    # nil 「声『ねえー私のパンツとブラジャー返してよー！』」
    # 14-26 跳过
    # 本作的孩子的声音（二周目）都是亚十礼的CV配的
    voice "voice/アシュリー/ash_a1_0027.ogg"
    "（电话里的声音）『呐，把我的胖次和胸罩还给我吧——！！』"

    # nil 「声『とったどー！』」
    # 01-03 跳过
    voice "voice/瑠那/lun_a1_0004.ogg"
    "（电话里的声音）『拿到啦！！！』"

    # nil 「声『ファーック！』」
    voice "voice/アシュリー/ash_a1_0028.ogg"
    "（电话里的声音）『花Q！！』"

    # 真冬 「ね」
    voice "voice/真冬/maf_a1_0179.ogg"
    dong 真冬_通話中 "『喏』"

    # 莲 「にぎやかなのはよくわかった。まぁ、なんだ。女子会をせいぜい楽しんでこいよ」
    lian "挺热闹的嘛。嘛，那个。尽情享受女子会吧~"

    # 真冬 「うん。今日は一緒にご飯いけなくてごめんねお兄ちゃん。あと、心愛ちゃんにも伝えといて」
    voice "voice/真冬/maf_a1_0180.ogg"
    dong 真冬_通話中 "『嗯，很抱歉今天不能和欧尼酱一起吃饭，还有，记得告诉心爱酱一声』"

    # nil 「声『さぁ！まふまふちゃんも！こっちきてお姉さん達と楽しい事しようじゃぁないか！』」
    voice "voice/瑠那/lun_a1_0005.ogg"
    "（电话里的声音）『来吧！嘛呼嘛呼酱也一起！来这边和姐姐们一起做开心的事吧！』"

    # nil 「声『つかまえましたよ、真冬ちゃん』」
    voice "voice/霧葉/krh_a1_0055.ogg"
    "（电话里的声音）『抓到你了哟，真冬酱』"

    # 真冬 「わっ、ちょっと、待っ…やっ…ぁっ…んっ―」
    voice "voice/真冬/maf_a1_0181.ogg"
    dong 真冬_通話中 "『哇，等、等一下... 呀... 呀... 呜啊...』"

    # 音效：电话挂断音
    play sound "voice/effect/電話／話し中.ogg"

    # nil 「プツッ」
    "滴……滴……滴……"

    # 莲 「……」
    lian "……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「…で？」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0368.ogg"
    ai 心愛_制服_基本_真顔 "……那么？"
    hide 心愛_制服_基本_不機嫌

    # 莲 「夜通しフィーバーするから泊まるって」
    lian "因为要彻夜狂欢所以要在那边过夜"

    # 心爱 「想瑠にゃんの家に？」
    voice "voice/心愛/cca_a1_0369.ogg"
    ai 心愛_制服_基本_真顔 "在想瑠喵家？"

    # 莲 「らしいよ」
    lian "好像是这样"

    # 心爱 「はえー…ってことは…まふまふちゃんの分、作っちゃったけど…」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0370.ogg"
    ai 心愛_制服_基本_泣き "哈啊……其实……我是做了嘛呼嘛呼酱的那份……"

    # 莲 「気にするなよ。俺が食うから」
    lian "别在意，我来消灭掉它"

    # 心爱 「あら、頼もしいですな！」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0371.ogg"
    ai 心愛_制服_基本_嬉しい "哎呀，真可靠啊！"
    hide 心愛_制服_基本_泣き

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene リビングa_夜 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 心爱 「じゃじゃーん！トマトとモッツァレラチーズのスパゲティにバジルとオリーブを添えてみまんた」
    # 参考资料：https://ja.wikipedia.org/wiki/モッツァレッラ
    # 参考资料：https://ja.wikipedia.org/wiki/バジル
    show 心愛_制服_基本_笑顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0372.ogg"
    ai 心愛_制服_基本_笑顔 "锵——锵！我试着在番茄和马苏里拉奶酪（L:是一种源自于意大利南部城市坎帕尼亚和那不勒斯的淡奶酪）的意大利面上加上了罗勒（L:是一类可用于烹调的香草，广东潮汕称为“金不换”、“鱼生菜”，皖北称为“香花子”，我国北方部分地区又称之为“兰香”）和橄榄"

    # 莲 「すげぇ我が家にある食材一個も使ってねぇ」
    lian "好厉害，我家的一个食材是一个都没用上"

    # nil 「でも、とても美味しかったです。普通に。」
    "但是，确实非常好吃呢"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=True, alpha=True, time_warp=None)
    scene リビングa_夜 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=True, alpha=True, time_warp=None)

    # nil 「夕食を終えて、心愛と二人でソファーに座りながらテレビでも眺める。梅昆布茶を啜りながら。」
    "吃完晚饭，我和心爱坐在沙发上看电视。喝着梅昆布茶"

    # nil 「お題目は「密着アクアリウム２４時」だ。」
    "节目的名字叫『在水族馆的24小时密切接触』"

    # 心爱 「でもいなー真冬ちゃん」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0373.ogg"
    ai 心愛_制服_基本_嬉しい "但是真好呢，真冬酱"

    # 莲 「どうした突然」
    lian "怎么啦？这么突然"

    # nil 「テレビ画面に映ったダイヤモンドネオンテトラを眺めながら、ぼそっと心愛がつぶやいた。」
    # 参考资料：https://ja.wikipedia.org/wiki/ネオンテトラ
    "看着电视画面上出现的霓虹脂鲤（L:中文俗名日光灯鱼、红绿灯鱼，为辐鳍鱼纲脂鲤目脂鲤科的其中一个种，是一种小型热带鱼），心爱自言自语道"

    # 心爱 「だって、今日、お泊まり会なんでしょ－？私もお泊まり会とかしてみたい！」
    show 心愛_制服_基本_笑顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0374.ogg"
    ai 心愛_制服_基本_笑顔 "因为，今天她那边不是开过夜会吗？我也想开个过夜会！"
    hide 心愛_制服_基本_嬉しい

    # 莲 「じゃぁ今日泊まってけばいじゃん」
    lian "那你今天就住下来吧"

    # 心爱 「ぶふっ」
    show 心愛_制服_基本_驚き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0375.ogg"
    ai 心愛_制服_基本_驚き "咕欸"
    hide 心愛_制服_基本_笑顔

    # 心爱 「ちょーっとー！　い、い、いきなりなーにを言い出すんだね！」
    show 心愛_制服_基本_不機嫌 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0376.ogg"
    ai 心愛_制服_基本_不機嫌 "等——下！你突、突、突然说什么啊！"
    hide 心愛_制服_基本_驚き

    # 莲 「ごめんごめん、ちょっと冗談が過ぎたわ」
    lian "对不起，我开玩笑开过头了"

    # 心爱 「むー…冗談キツいなぁ、もう…はぁ」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0377.ogg"
    ai 心愛_制服_基本_泣き "唔姆…不要随便开玩笑啊，已经…啊"
    hide 心愛_制服_基本_不機嫌

    # 莲 「ごめんって。ほら、それ飲み終わったら帰るか？」
    lian "对不起。那个，一会儿喝完那个就回去吧"

    # 心爱 「やだ」
    show 心愛_制服_基本_不機嫌 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0378.ogg"
    ai 心愛_制服_基本_不機嫌 "不要"
    hide 心愛_制服_基本_泣き

    # 莲 「む」
    lian "emmm"

    # nil 「心愛はうつむいたま、そっと細い声を漏らし、ぎゅっと俺の裾を掴んだ。」
    "心爱低着头，轻轻地发出了微弱的声音，紧紧地抓住了我的衣摆"

    # 心爱 「一応…確認だけど…さっきの、泊まっていけばいっていうのは…、マジで冗談？」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0379.ogg"
    ai 心愛_制服_基本_真顔 "姑且...确认一下...刚才你说要我留下来过夜...真的是开玩笑吗?"
    hide 心愛_制服_基本_不機嫌

    # 莲 「あー…嫌な思いをさせてたら謝るよ、ごめん」
    lian "啊……如果我让你不高兴了我会道歉的，对不起"

    # 心爱 「んーん。そうじゃなくて。あんまり鈍感だと怒るよ蓮くん」
    show 心愛_制服_基本_無表情 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0380.ogg"
    ai 心愛_制服_基本_無表情 "emm，不是那样的，如果你这么迟钝的话，我要生气了"
    hide 心愛_制服_基本_真顔

    # 莲 「…そうだな…」
    lian "…是这样啊…"

    # nil 「先ほどの発言は、正直な所を言うと、軽はずみな冗談ではあった。」
    "老实说，刚才的发言是一个轻率的玩笑"

    # nil 「だが、こで正直に述べてしまうのは、心愛を酷く傷付けてしまう。そんな事は俺でもわかる。」
    "但是，在这里说实话，会严重伤害心爱。这样的事情我也是知道的"

    # 莲 「心愛が、望むなら…泊まって行って貰っても…」
    lian "心爱，如果你愿意...你可以留下来住..."

    # 心爱 「……」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0381.ogg"
    ai 心愛_制服_基本_真顔 "……"
    hide 心愛_制服_基本_無表情

    # 莲 「その…ごめん、な？」
    lian "那个…对不起、嗯？"

    # 心爱 「…６５点」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0382.ogg"
    ai 心愛_制服_基本_泣き "…６５分"
    hide 心愛_制服_基本_真顔

    # 莲 「へ？」
    lian "欸？"

    # 心爱 「誘い文句としてはってこと！もー！　流れで考えてよさー！　さっきキスまでしてるのに、泊まって行けなんて冗談でも言われたら、そーいうこと意識しちゃうに決まってんじゃんかさー！」
    show 心愛_制服_基本_不機嫌 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0383.ogg"
    ai 心愛_制服_基本_不機嫌 "作为邀约的话当然是这个意思吧！真是的——！你换位思考下！刚才还亲过，现在就说让我住下之类的的话，肯定会有这样的想法吧！"
    hide 心愛_制服_基本_泣き

    # 莲 「ぁー」
    lian "啊——"

    # nil 「ボカボカボカボカボカボカ」
    "啪嗒啪嗒啪嗒啪嗒啪嗒啪嗒"

    # nil 「心愛が俺の両胸をポカポカと叩く。しがみついてくる心愛の頭を、俺はそっと撫でる。」
    "心爱啪嗒啪嗒地敲打着我的胸口，我轻轻地抚摸着紧紧抓住我的心爱的头"

    # 心爱 「ぜぇ…はぁ…ったく…さっきの不意打ちのキスのファインプレーはまぐれだったのかよ…」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0384.ogg"
    ai 心愛_制服_基本_泣き "切…啊…真是的…刚才那个出其不意精彩的吻的只是巧合啊…"
    hide 心愛_制服_基本_不機嫌

    # 莲 「すまん。どーしても、心愛はこういうの苦手な意識があってだな…」
    lian "对不起，不管怎么说，连心爱都不擅长这种事情..."

    # 心爱 「む、むー…！　じゃ、じゃぁ、私が今日の残りを平穏に過ごすために、一度しか言わないから！　す、す…好きな人に！　求められる事は！　普通に！　嬉しいから！　確かに恥ずかしいけども！」
    show 心愛_制服_基本_不機嫌 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0385.ogg"
    ai 心愛_制服_基本_不機嫌 "唔，嗯…！那么，为了我能平安度过今天剩下的日子，我只说一次！被喜、喜欢的人！要求的事是！普通的！开心！虽然确实很不好意思！"
    hide 心愛_制服_基本_泣き

    # 莲 「お、おう」
    lian "嗯、嗯"

    # 心爱 「つーことで！　後は判断に任せます！」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0386.ogg"
    ai 心愛_制服_基本_嬉しい "综上所述，接下来就交给你判断了！"
    hide 心愛_制服_基本_不機嫌

    # nil 「心愛がそっぽを向いたので、ほっぺを両手で持って、こちらを向かせる。」
    "心爱转过身来，双手捂着脸颊，面向这边"

    # 莲 「心愛、今日、泊まっていかないか？」
    lian "心爱，今天，你想留下来过夜吗？"

    # 心爱 「っ…！　…うん…っ…ちゅっ…」
    show 心愛_大_制服_基本_キス at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0387.ogg"
    ai 心愛_制服_基本_キス "哈啊...嗯... 啾..."
    hide 心愛_制服_基本_嬉しい

    # 心爱 「ちゅぅ…るっ…ちゅぷっ…んふぅ…れる…ぷはぁっ」
    voice "voice/心愛/cca_a1_0388.ogg"
    ai 心愛_制服_基本_キス "啾...嗯...嗯...哈啊..."

    # 心爱 「９５点…かなっ」
    show 心愛_大_制服_基本_嬉しい at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0389.ogg"
    ai 心愛_制服_基本_嬉しい"…９５分…吧"
    hide 心愛_大_制服_基本_キス

    # 莲 「まだ１００点には及ばずか」
    lian "还是没到１００分吗？"

    # 心爱 「１００点は…まだ、とっとく…はぁ…蓮くぅん…」
    show 心愛_大_制服_基本_キス at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0390.ogg"
    ai 心愛_制服_基本_キス "１００分……还没拿到…哈啊…莲君…"
    hide 心愛_制服_基本_嬉しい

    # nil 「心愛は、身体の力を抜いて、俺の胸元に倒れ込んできた。ゆっくりと頭を撫でると、心愛は安心したように、目を閉じた。」
    "心爱撤出了身体的力量，倒在了我的胸口。我慢慢地抚摸着头，心爱安心地闭上了眼睛"

    # nil 「心地の良い温かな空気が、俺達二人を包み込む。」
    "舒适温暖的空气包围着我们两个人"

    # 莲 「（大事な事をすっとばしてるような気がするが…今は…それでも…）」
    lian "（虽然觉得好像正在说重要的事情…但是…现在…即便如此…）"

    # scene03 场景2 【和心爱的晚饭时间】 结束

    # scene03 场景3 【心爱的心跳留宿】 开始
    play music bgmthirtyseven fadeout 2.0 fadein 2.0
    image bg 自室a_夜 = "images/bg/自室a_夜.png"
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 自室a_夜 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # nil 「さて、あれから何したっけな…。」
    "那么，那之后做了什么呢…"

    # nil 「だめだ、何も覚えてねぇ。」
    "哒咩，什么都不记得了"

    # 心爱 「ゴゴジュウイチジ ヲオシラセシマス」&&感觉好像涉及时间了，翻得可能有点问题
    # 参考资料：https://ja.wikipedia.org/wiki/次の犠牲者をオシラセシマス
    # 参考资料：https://web.archive.org/web/20121020172955/http://www.asgard-japan.com/booston/05tsugino/
    show 心愛_制服_基本_覚醒 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0391.ogg"
    ai 心愛_制服_基本_覚醒 "这是十一点的死亡通告（L:neta2011年PSP上的一款悬疑冒险游戏游戏『给下一个牺牲者的死亡通告（次の犠牲者をオシラセシマス）』的台词）"

    # 莲 「もうそんな時間か」
    lian "已经到时间了吗？"

    # nil 「俺たちは、とりあえずえーっと…。」
    "总之，我们先是，呃.."

    # nil 「部屋に来て、ベッドの上に二人並んで、座っていた。」
    "来到了我的房间，两个人并排坐在床上.."

    # nil 「心臓は早鐘のように鳴っているし、肩はガッチガチに強張っている。」
    "心脏砰砰直跳，肩膀也是硬邦邦的"

    # nil 「ついでに、あそこもガッチガチだぜ！」
    "顺便说下，那边那位也很紧张哦！"

    # nil 「…すいませんでした。」
    "…对不起"

    # 心爱 「ゴゴジュウイチジ、イップンヲオシラセシマス」
    voice "voice/心愛/cca_a1_0392.ogg"
    ai 心愛_制服_基本_覚醒 "这是十一点零一分的死亡通告"

    # 莲 「スヌーズしなくていよ」
    lian "不要打盹哦"

    # 心爱 「アイ」
    voice "voice/心愛/cca_a1_0393.ogg"
    ai 心愛_制服_基本_覚醒 "是"

    # nil 「とは言うと、心愛も見ての通りだ。」
    "话虽如此，但心爱也正如所见的那样"

    # nil 「あまりに緊張しすぎて機械化している。」
    "过于紧张而变成机器了"

    # nil 「先ほどまで、唇を重ねていたので、唇は月明かりに反射して艶めいているし、瞳もウルウルと輝いていた。」
    "到刚才为止，因为嘴唇重叠之后留下的液体，被月光反射而变得艳丽，眼睛也是闪闪发亮的"

    # nil 「お互い、この後自分達がどうなるかなんてのは、そりゃわかっている。」
    "我们彼此都知道后面会发生什么事情"

    # nil 「わかっているからこそ、このザマだ。」
    "正因为明白，所以才变成了这样"

    # 莲 「（なんとかしなければな…）」
    lian "（必须要想办法做点儿什么啊…）"

    # nil 「とはいえ、こであまり心愛を待たせてしまってもしかたない。」
    "话虽如此，让心爱在这里等太久也没有用"

    # nil 「カチカチと秒針が時を刻む音だけが部屋に響き渡る。」
    "只有秒针滴答滴答的滴答声在房间里回荡"

    # 莲 「…よし」
    lian "…好"

    # 心爱小幅跳动
    # 心爱 「はぅっ！？」
    hide 心愛_制服_基本_覚醒
    show 心愛_制服_基本_驚き:
        zoom 1.5
        xalign 0.53
        yalign -0.09
        linear 0.15 yalign -0.01
        linear 0.15 yalign -0.09
    voice "voice/心愛/cca_a1_0394.ogg"
    ai 心愛_制服_基本_驚き "哈呜？！"
    hide 心愛_制服_基本_覚醒

    # nil 「ビクゥッ！　と心愛が跳ねた。まだ何もしてないのに。」
    "明明还什么都没做呢，心爱就“哈呜！”一声跳了起来"

    # 莲 「…ぷっ」
    lian "…噗"

    # nil 「その仕草につい微笑みが零れた。」
    "看到如此反应我不由得微笑起来"

    # 心爱 「ナ、ナンデスカ」
    show 心愛_制服_基本_覚醒 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0395.ogg"
    ai 心愛_制服_基本_覚醒 "怎、怎么了呢？"
    hide 心愛_制服_基本_驚き

    # 莲 「いや、なんか、可愛いなと思ってな…」
    lian "不，总觉得，你很可爱啊…"

    # 心爱 「あ…あは…さっきは鈍感だとか言ってごめんね…本番近づくと、流石の私もガッチガチです…」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0396.ogg"
    ai 心愛_制服_基本_嬉しい "啊、啊哈哈哈，刚才说了你什么迟钝之类的话对不起…临近正式演出的时候，就连我也很紧张（ガッチガチ，僵硬的意思呢，也有那个地方硬起来的意思）呢…"
    hide 心愛_制服_基本_覚醒

    # 莲 「いや、ガッチガチなのは俺のほうだ」
    lian "不，我才是紧张（ガッチガチ）的那个"

    # 心爱 「二度同じネタを使うな」
    show 心愛_制服_基本_覚醒 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0397.ogg"
    ai 心愛_制服_基本_覚醒 "不要再用同一个段子了"
    hide 心愛_制服_基本_嬉しい

    # 莲 「何で知ってんだよ…」
    lian "你怎么知道的…"

    # 心爱 「だって…ガッチガチのご様子ですし…」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0398.ogg"
    ai 心愛_制服_基本_泣き "因为…你看起来很僵硬（ガッチガチ）呢……"
    hide 心愛_制服_基本_覚醒

    # 莲 「そんな所を見るな…といっても、これから見せるハメになるんだよな…」
    lian "别看那个地方啊……但是，现在开始要看了啊…"

    # 心爱 「は、はぃ…あぅ…え、えと…脱がせばいのかな…？」
    voice "voice/心愛/cca_a1_0399.ogg"
    ai 心愛_制服_基本_泣き "啊，嗯…啊…那个……要脱下来吗…？"

    # 莲 「ま、待たれい待たられい！　この流れで事に及んだら変な空気になっちゃうぞ！」
    lian "等、先等一下等一下，如果这样的话，气氛会变得非常奇怪的"

    # 心爱 「そーいうフリかと思いました！　と、というか！　こまで頑張らせちゃいましたし！　そろそろ…私も誠意を見せなきゃ…とは、はい、常々、考えておりまして」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0400.ogg"
    ai 心愛_制服_基本_嬉しい "我还以为你是装的呢！话说，你一直在努力着！差不多，我也在想，是时候...我也该表现出诚意了"
    hide 心愛_制服_基本_泣き

    # 莲 「いよ、もう」
    lian "啊，我已经忍不住了"

    # 心爱 「ふえ？　はわっ！」
    show 心愛_制服_基本_驚き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0401.ogg"
    ai 心愛_制服_基本_驚き "啊？哈啊！"
    hide 心愛_制服_基本_嬉しい

    # nil 「心愛がわたわたとしはじめたので、俺はそっと肩に触れて、ゆっくりとベッドに押し倒した。」
    "因为心爱现在软绵绵的，所以我轻轻地抚摸着肩膀，慢慢地把她推倒在床上"

    # nil 「最初は驚いたとはいえ、心愛は抵抗することなく、ぽふっと音を立て俺のベッドの上に収まった。」
    "虽然一开始很惊讶，但是心爱并没有抵抗，嗒的一声，躺在了我的床上"

    # 莲 「最後まで頑張らせてくれよ。ありがとう、心愛」
    lian "让我努力到了最后，谢谢，心爱"

    # nil 「ちゅっ」
    "啾"

    # nil 「心愛のおでこにキスを浴びせる。」
    "亲吻着心爱的额头"

    # 心爱放大

    # 心爱 「は、…ぁうっ…あ、甘えちゃう…よ？　ほんとに…こんな事されたら…」
    show 心愛_大_制服_基本_嬉しい at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0402.ogg"
    ai 心愛_制服_基本_嬉しい "哈，哈呜…哈…我要撒娇了…哦？真的…如果被这样做的话……"
    hide 心愛_制服_基本_驚き

    # 莲 「それが心愛の望みなら…俺はそれを叶えてあげたい」
    lian "如果那是心爱的愿望的话…我愿意实现它"

    # 心爱 「～～！　はぁっ…ぁぅ…も…ダメ…ドキドキがとまんない…。その言葉だけでどうにかなっちゃうよぉ…こんなに嬉しい事、あっていのかな…」
    voice "voice/心愛/cca_a1_0403.ogg"
    ai 心愛_制服_基本_嬉しい "啊——啊——哈…哈呜…哈…不行…心跳不已……光是这句话就没办法了啊……真的可以有这么开心的事吗…"

    # 莲 「おいおい、まだ始めてないだろ…大丈夫か？」
    lian "那个，还没开始呢，不要紧吧"

    # 心爱 「だ、大丈夫じゃない…ほんと私、このあとどうなるの…。蓮くんに、変な所見せちゃうかも…」
    voice "voice/心愛/cca_a1_0404.ogg"
    ai 心愛_制服_基本_嬉しい "才、才不是不要紧…说真的，我…这之后会变成什么样…也许会让莲君看到奇怪的地方……"

    # 莲 「いや、いつも変な所は見てるからそれについては問題ない」
    lian "不，我总是看到奇怪的地方，关于那个的话没有问题"

    # 心爱 「確かに」
    show 心愛_大_制服_基本_真顔 at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0405.ogg"
    ai 心愛_制服_基本_真顔 "确实呢"
    hide 心愛_大_制服_基本_嬉しい

    # 莲 「というか、もし、俺の知らない心愛がまだあるなら、もっと見て見たいし、やっぱ、お前のこと幸せにしてぇ。ということで…」
    lian "也就是说，如果还有我不知道的心爱的话，我想再多看看，果然，我还是想让你幸福"

    # 心爱 「」（原文没HOOK出来）
    voice "voice/心愛/cca_a1_0406.ogg"
    ai 心愛_制服_基本_真顔 "呀啊——！等下！stop！stop！stop！哈啊…哈啊……"

    # 莲 「むぐっ…」
    lian "呜啊…"

    # nil 「俺が心愛の唇を塞ごうとすると、両手で俺の口を押さえてきた。」
    "我正要堵住心爱的嘴唇时，她用双手捂住了我的嘴"

    # 心爱 「えと…えと…もう、言葉だけでイっちゃいそうだから…。その…せめて、イク前に…心の準備を…」
    show 心愛_大_制服_基本_キス at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0407.ogg"
    ai 心愛_制服_基本_キス "那个…那个…因为光是听到你的言语就已经不行了……那个…至少，在开始之前…让我做好心理准备……"
    hide 心愛_制服_基本_真顔

    # 莲 「もご、もご…」&不是很会翻
    lian "嗯"

    # nil 「お前可愛いな。と反射的に言おうとしたが、言葉を発せさせてくれない。」
    "真是可爱啊。虽然想反射性地想说出来，但是没有说出来"

    # # 为啥重了一个……，这里不是落了是多了
    # # 心爱 「えと…えと…もう、言葉だけでイっちゃいそうだから…。その…せめて、イク前に…心の準備を…」
    # voice "voice/心愛/cca_a1_0408.ogg"
    # ai "那个…那个…因为光是听到你的言语就已经不行了……那个…至少，在开始之前…让我做好心理准备……"

    # 心爱 「ごくりっ…よ、よし…」（原文没完整HOOK出来）
    show 心愛_大_制服_基本_嬉しい at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0408.ogg"
    ai 心愛_制服_基本_嬉しい "哈啊——！哈呜！哈！嗯！好、好的"
    hide 心愛_大_制服_基本_キス

    # 心爱 「じゃ、じゃぁ…え、えと、よ、よろしくおねがい…します…ぺこり」
    show 心愛_大_制服_基本_キス at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0409.ogg"
    ai 心愛_制服_基本_キス "那、那么……嗯，那个，请多关照……拜托了…"
    hide 心愛_大_制服_基本_嬉しい

    # 莲 「ふがふがふが（よろしくおねがいします）」
    lian "请多关叫（请多关照）"

    # nil 「俺は心愛に口を押さえられたま、ゆっくり頭を下げた。」
    "我被心爱捂住了嘴，慢慢地低下了头"

    # nil 「心愛がゆっくりと手を離し、俺の口を解放してくれた。」
    "心爱慢慢地放开了手，我的嘴唇解放了出来"

    # 莲 「愛してるよ、心愛…」
    lian "我爱你，心爱……"

    # 心爱 「私も…大好き…ちゅぅ…んっ…んっ…んぅうっ！」
    voice "voice/心愛/cca_a1_0410.ogg"
    ai 心愛_制服_基本_キス "我也最喜欢……嗯…嗯…嗯…嗯！"

    # nil 「ゆっくりと心愛と唇を合わせる。それと同時に、心愛の身体がビクビクと跳ねる。」
    "慢慢地和心爱亲吻着。与此同时，心爱的身体颤抖着跳了起来"

    # nil 「それでも俺は心愛の唇から唇を離さず、キスを続けた。」
    "尽管如此，我的嘴唇还是没有离开心爱的嘴唇，继续吻着她"

    # 心爱 「んっ、んぅっ…ぷは…ぁっ…はぁ…キスで…イっちゃった…」
    voice "voice/心愛/cca_a1_0411.ogg"
    ai 心愛_制服_基本_キス "嗯，嗯……呼……啊…啊…啊…接吻着……要出来了…"

    # nil 「心愛は、ぽーっと顔を惚けさせる。」
    "心爱的脸一下子变得恍惚起来"

    # 莲 「可愛いよ、心愛」
    lian "好可爱呀，心爱"

    # 心爱 「恥ずかしいとこ…見られちゃいました…ね…はぁぅ…」
    show 心愛_大_制服_基本_嬉しい at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0412.ogg"
    ai 心愛_制服_基本_嬉しい "羞耻的地方...被看到了呢...是这样...哈..."
    hide 心愛_大_制服_基本_キス

    # 莲 「もっと、見せてくれよ」
    lian "再多给我看看"

    # 心爱 「はぁい…うれしいよぉ…求めてもらえるの…すっごく幸せ…」
    voice "voice/心愛/cca_a1_0413.ogg"
    ai 心愛_制服_基本_嬉しい "哇…好高兴啊…能得到你的追求…非常幸福…"

    # 莲 「心愛が幸せそうにしてくれるからだよ」
    lian "心爱幸福的话我也会很幸福"

    # nil 「俺はそう言いながら、心愛に覆い被さって、体重を重ねる。」
    "我一边这样说着，一边覆盖住心爱，把体重叠加在一起"

    # nil 「ぐっと、心愛が俺の腕に手をまわしてくれる。」
    "突然，心爱伸手搂住我的胳膊"

    # 心爱 「ぎゅー…すきぃ…」
    show 心愛_大_制服_基本_キス at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0414.ogg"
    ai 心愛_制服_基本_キス "啾……喜欢"
    hide 心愛_大_制服_基本_嬉しい

    # 莲 「心愛の鼓動が聞こえる。すげぇドキドキしてるな…」
    lian "我能听到心爱的心跳声，你心跳得好快..."

    # 心爱 「蓮君もドキドキしてるね…こんなにも近くで、君を感じてる…」
    show 心愛_大_制服_基本_嬉しい at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0415.ogg"
    ai 心愛_制服_基本_嬉しい "莲君也是心跳不已呢…在这么近的地方，感受着你…"
    hide 心愛_大_制服_基本_キス

    # 心爱 「ねぇ、もっと近くに…」
    show 心愛_大_制服_基本_キス at love69_xinai_bg_center with dissolve
    voice "voice/心愛/cca_a1_0416.ogg"
    ai 心愛_制服_基本_キス "呐，再靠近一点…"
    hide 心愛_大_制服_基本_嬉しい

    # 切换到HS
    # BGM：开场音乐
    # 自带心爱娇喘声
    # 根据项目组安排，HS不翻译，请各位积极支持正版，自行购买正版欣赏
    # 这里放上宁宁举牌
    # 跳过
    # 统计一下跳过的心爱音声数量方便后续制作
    # 跳过（要删除）的心爱音声数量->太多了统计不出来了
    #

    luckykeeper "根据项目组安排，我们不会翻译 Hscene 里的内容，请各位积极支持正版，自行购买正版欣赏，还请各位谅解"

    # scene03 场景3 【心爱的心跳留宿】 结束
    # scene03 结束

    # 过场：心爱（常服）没有BGM （打算加一个？？）

    # 隐藏 quick_menu
    $ quick_menu = False

    play sound "voice/effect/moosehead honk (stinger).ogg"
    play music bgmtwentyeight fadeout 4.0 fadein 4.0 # 针对这里BGM的特点需要把 Scene04 的BGM提前到 Scene03 脚本的尾巴这里写，并增大 fadeout/in 的间隔
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)
    scene アイキャッチ心愛 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)

    $ renpy.pause(1.5, hard=True)
    $ renpy.end_replay()

    jump scene04

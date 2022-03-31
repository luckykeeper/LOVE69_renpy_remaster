# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene10 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：
# 版本 0.7 "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年3月31日

# 当前流程：编写脚本AIO Process

label scene10:
    # scene10 开始

    # scene10 场景1 【按捺不住激动心情飞回家的莲君】 开始

    # 地点：葛城家门口
    # 人物：お姉さん（小姐姐） 莲 心爱 真冬
    # BGM：

    # 显示 quick_menu
    $ quick_menu = True
    scene 自宅_夕 at love69_bg1440 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)

    # 莲 「すいません送ってもらっちゃって」
    lian "抱歉让你送我回来了"

    # お姉さん（小姐姐） 「いやいやー、旅は道連れ世は情けってやつでさー。まさかこの日本でヒッチハイクしてる人がいるとはおもわなんだ」
    # 记得去加人物表
    voice "voice/その他/ex4_a1_0001.ogg"
    xiaojiejie "哪里哪里~旅行就是同路人啊~没想到在日本也会有人搭便车呢"

    # 莲 「しっかし凄いですね。デロリアンなんて初めて乗りましたよ。しかも途中空飛んだし」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%87%E3%83%AD%E3%83%AA%E3%82%A2%E3%83%B3%E3%83%BB%E3%83%A2%E3%83%BC%E3%82%BF%E3%83%BC%E3%83%BB%E3%82%AB%E3%83%B3%E3%83%91%E3%83%8B%E3%83%BC
    lian "不过好厉害啊。我是第一次坐DeLorean（L:德罗宁汽车，1975-1982，成名于在世界各地广受欢迎的《回到未来系列》电影（前面有提到）。虽然在第一部电影上市前该公司已结业，但外观独特的DMC-12跑车被电影采用为道具。电影中德罗宁跑车被古怪的科学家埃米特·L·布朗博士改装成时间旅行机器，其形象成为普遍的公众回忆），而且中途还飞了起来"

    # お姉さん（小姐姐） 「人を乗せたの秘密だよー？　これ妹のだから！　二輪乗ってた頃の感覚で、渋滞は耐え切れなくてさー」&&协力请求
    voice "voice/その他/ex4_a1_0002.ogg"
    xiaojiejie "一起坐车是秘密哟~？这是我妹妹的！感觉就像是骑二轮车的时候一样呢，我受不了堵车"

    # 莲 「へいへい。そんじゃ、道中気をつけて」
    lian "嗯嗯。那，路上小心"

    # お姉さん（小姐姐） 「ほーい。じゃぁね、ばいばーい、心愛ちゃんと真冬ちゃんの彼氏さん！」
    # 合理怀疑：这个小姐姐是雾叶的姐姐亚十礼（ATRI）
    voice "voice/その他/ex4_a1_0003.ogg"
    xiaojiejie "好。那么，再见，心爱酱和真冬酱的男朋友！"

    # 莲 「な、何故それを！　まだ記者会見もしてない最新情報だぞ！」
    lian "呐，为什么会这样啊！这是还没有召开新闻发布会的最新情报啊！"

    # お姉さん（小姐姐） 「あでぃおーす・あみーご！」
    voice "voice/その他/ex4_a1_0004.ogg"
    xiaojiejie "Adiós・amigo（L:还是前面提到的西班牙语：再见，朋友）"

    # 莲 「あ、ちょっと、なぁ！」
    lian "啊，等一下，嘿！"

    # nil 「俺の質問には、排気音で答えて、お姉さんは走り去ってしまった。」
    "对于我的问题，小姐姐用排气筒的声音来回答，然后就离开了"

    # 莲 「（あの人…どっかで…）」
    lian "（那个人…在哪里…）"

    # nil 「雰囲気は違ったが、担任やリオンと似たような空気を感じる。しかし、何故知っていたのだろうか…もしかして、誰かが見ていたのか？」
    "虽然气氛有所不同，但是总感觉和班主任或者里昂很相似。但是，我为什么知道呢…难道，之前见过？"

    # nil 「ていうか、最近、二度ほど同じ別れの挨拶を貰っている気がする。」
    "话说回来，最近好像收到了两次同样的告别问候呢"

    # nil 「まぁともあれ、家にたどり着くまでに力尽きて倒れるなんて事は避けられたわけだ。」
    "不管怎样，终于是避免了在到家之前尽量筋疲力尽而倒下"

    # 莲 「さてさて。ウサギちゃん達は流石にご帰宅なさってる様子で」
    lian "好啊好啊，小兔子们看起来顺利地回到家了呢"

    # nil 「ガレージにはしっかり俺のバイクが収納されている。」
    "我的摩托车被好好地停放在了车库里面"

    # 莲 「ま、色々遠回りはしちまったが…これでやっと、彼氏彼女か」
    lian "嘛，虽然绕了很多弯路…现在终于是男朋友女朋友了"

    # nil 「真冬は？」
    "真冬捏？"

    # nil 「細かい事は関係ねぇ。」
    "细节就不要在意了"

    # nil 「さて、ちょっくら、帰宅ぶちかましてやるか。」
    "那么，稍微，来康康你们是不是都回家了吧"

    # nil 「ガチャッ…」
    "嘎吱……"

    # 莲 「んあ…鍵かってやがらぁ」
    lian "啊……我钥匙呢？"

    # nil 「ポケットの中をまさぐって、家の鍵を探す。」
    "在口袋里摸索，寻找房子的钥匙"

    # 莲 「ってあれか、バイクのキーと一緒になってんだわ」
    lian "原来是那样啊，和摩托车的钥匙放在一起了啊"

    # nil 「恐らくあの二人の事だ。この事は計算済みだろう。」
    "恐怕是那两个人，已经把这件事算计好了"

    # 莲 「なら、二人が期待する行動は…と」
    lian "那么，你们期待的行动是……"

    # nil 「俺はふっと息を吐いてから、」
    "我呼了一口气之后"

    # nil 「俺はインターホンのスイッチを強く押し込む。」
    "我用力按下对讲机的开关"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 音效：叮咚x1
    play sound "voice/effect/05_玄関チャイム.ogg"

    # 心爱 「『えっ、マジか！？　もう帰ってきたの！？　はやくない！？』」
    # 没有跳过
    voice "voice/心愛/cca_a1_1184.ogg"
    ai 心愛_yシャツ_パンツ有り_驚き "『咦，真的吗！？已经回来了！？这么快吗！？』"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「『あんのやろーズルしやがったな…』」
    # 没有跳过
    voice "voice/真冬/maf_a1_0906.ogg"
    dong 真冬_裸yシャツ_パンツ_本気 "『那家伙作弊了』"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「『次元転送装置か！』」
    voice "voice/心愛/cca_a1_1185.ogg"
    ai 心愛_yシャツ_パンツ有り_真顔 "『是用了次元传送装置吗！』"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「『そんなハイテクな物はこの世には存在してないと思う』」
    voice "voice/真冬/maf_a1_0907.ogg"
    dong 真冬_裸yシャツ_パンツ_目閉じ "『我觉得这个世界上不存在这种高科技的东西』"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「『この前ペニオクで売ってたよ』」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%9A%E3%83%8B%E3%83%BC%E3%82%AA%E3%83%BC%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3
    # 参考资料：https://www.docin.com/p-242798795.html
    voice "voice/心愛/cca_a1_1186.ogg"
    ai 心愛_yシャツ_パンツ有り_不機嫌 "『之前在penny auction上有卖的哦』（L:指“一分钱拍卖”始于德国的Swoopo，口号是“娱乐消费”，模式类似于京东拍拍的夺宝岛，上面所有商品起价统一0.15刀，每次加价为0.75刀，每多一名参与者价格上涨0.15刀，20秒没人新出价即成交）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「『あれやめといた方が良いよ。時間切れ直前で運営が釣り上げて、どうせ買えないから』」
    voice "voice/真冬/maf_a1_0908.ogg"
    dong 真冬_裸yシャツ_パンツ_無表情 "『那个还是算了吧。时间快到了运营就来钓鱼了，反正也买不起』（L:海鲜市场(闲鱼)·拍拍·转转等拍卖平台的卖家，常常会开小号，如果价格不满意就用小号加价，保证自己不亏）"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「『なんだとぅ！　芸能人のブログにだまされた！』」
    voice "voice/心愛/cca_a1_1187.ogg"
    ai 心愛_yシャツ_パンツ有り_驚き "『什么！我被艺人的博客欺骗了！』（L:日常夹带私货：不如来我的博客康康，保证没有骗人的东西(doge)，网址http://luckykeeper.site）"

    # nil 「ドアの向こう側でドッタンバッタンと音が聞こえる。慌ただしいな。」
    "在门的另一边听到咚的一声，真是仓促啊"

    # nil 「しばらく音を聞いて様子見と行こうか。」
    "先听一会儿声音，看看会发生什么"

    # 心爱 「『私が怖いのは饅頭だけなんだけど、あまりに饅頭が怖いんで口の中に入れたら次はお茶が怖くなってね』」
    # 参考资料：https://ja.wikipedia.org/wiki/%E9%A5%85%E9%A0%AD
    # 参考资料：https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q13175440813?__ysp=56eB44GM5oCW44GE44Gu44Gv6aWF6aCt44Gg44GR44Gq44KT44Gg44GR44Gp44CB44GC44G%2B44KK44Gr6aWF6aCt44GM5oCW44GE44KT44Gn5Y%2Bj44Gu5Lit44Gr5YWl44KM44Gf44KJ5qyh44Gv44GK6Iy244GM5oCW44GP44Gq44Gj44Gm44Gt
    # 这里的落语：https://ja.wikipedia.org/wiki/%E3%81%BE%E3%82%93%E3%81%98%E3%82%85%E3%81%86%E3%81%93%E3%82%8F%E3%81%84
    # 落语参考：http://www2.yamanashi-ken.ac.jp/~itoyo/essay/manjuukowai.htm
    voice "voice/心愛/cca_a1_1188.ogg"
    ai 心愛_yシャツ_パンツ有り_真顔 "『我唯一害怕的是馒头，放进嘴里的话，接下来就是害怕喝茶了』（L:这里馒头是指霓虹的馒头，与中国不同，是甜甜的小点心，吃了太甜的东西自然就想喝点热茶来中和一下，这是霓虹人的习惯，这里提到的害怕喝茶，是引用了古代落语まんじゅうこわい(馒头真可怕啊)的梗）（W:可以理解成类似豆沙包）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「『この前動物園のバイトでね、虎の中に入る仕事してたんだけど、ライオンと戦う羽目になったんだ。これはヤバいと思ったんだけど、ライオンの中も人入ってたんだよ』」
    voice "voice/真冬/maf_a1_0909.ogg"
    dong 真冬_裸yシャツ_パンツ_無表情 "『之前在动物园打工的时候，做过进入老虎玩偶里面的工作，结果变成了和狮子战斗的窘境。虽然觉得这很糟糕，但是其实狮子里面也是有人的』"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「『甥っ子がおあしをしらねぇってんで、おひな様の刀の鍔じゃねぇかと言いやがって。可愛いなと思ってちょいとくれてやったら、焼き芋買いにいきやがった』」
    # L：心爱你说人话好吗？我看不懂也听不懂
    # W：wtf，心爱在说梦话吧，大概，能把四句不相关的话合在一起，也是奇才了
    # L：作者太鉴了，这个落语是1733年的，很难不觉得霓虹人真的能顺利看懂本作嘛？
    # W：草，雀食如此
    # 参考资料：https://dictionary.goo.ne.jp/word/%E5%BE%A1%E8%B6%B3/ おあし
    # 参考资料：https://www.bilibili.com/video/BV1AW41147h4 おひな様の刀の鍔
    # 参考资料：https://ja.wikipedia.org/wiki/%E9%9B%9B%E9%8D%94 おひな様の刀の鍔
    # 参考资料：https://ja.wikipedia.org/wiki/%E9%9B%9B%E7%A5%AD%E3%82%8A おひな様
    # 落语参考：https://rakugonobutai.web.fc2.com/158hinatuba/hinatuba.html
    # 关于雏刀：■お雛様の鍔；イイ見立てですが、男の子が居ると、刀を引き抜いてチャンバラごっこを始めたりします。雛壇の上に、モグサと線香を置いておくこともあります。
    # それは男の子除けにお灸のセットを置いておくのです。
    # 五月の、男の子の節句では、大きな刀やカブトがありますので、男の子は大喜び。早々に壊しに掛かります。
    # 机翻：
    # 雏刃；虽然看起来不错，但是有男孩子在的话，会把刀拔出来开始乱糟糟的游戏。有时会在雏坛上放上木槿和线香。那是为了除掉男孩子而设置的灸套餐。
    # 五月的男孩节有大刀和大头菜，男孩非常高兴。会尽快着手破坏。
    # *雏祭是日本女孩子的节日
    voice "voice/心愛/cca_a1_1189.ogg"
    ai 心愛_yシャツ_パンツ有り_真顔 "『我的侄子说他不知道什么是钱，所以他问我这是不是雏祭的雏刀。我觉得它很可爱，所以我把它给了他，而他去买了一个烤红薯吃』（L:这里同样是引用了古代落语，出自三代目三遊亭的『雛鍔』，发布于1733年感兴趣可以去找找这个东西的落语，本作非常喜欢引落语相关的东西呢）"

    # 莲 「（世間話してんじゃねぇか！　つーか…妙に聞いた事あるエピソードだな…）」
    lian "（这不是在闲聊吗! 话说……我听到了什么奇怪的故事啊……）"

    # nil 「急かしてやろう。」
    "稍微催催她们吧"

    # 叮咚x1
    play sound "voice/effect/05_玄関チャイム.ogg"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「『はっ！　急がなきゃ！　こっちの準備は出来てる！？』」
    voice "voice/真冬/maf_a1_0910.ogg"
    dong 真冬_裸yシャツ_パンツ_無表情 "『啊！必须快点了！已经做好准备了吗！？』"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「『先輩！　このドラゴン柄のトランクスは！』」
    voice "voice/心愛/cca_a1_1190.ogg"
    ai 心愛_yシャツ_パンツ有り_真顔 "『前辈！这个龙纹的平角内裤是！』（L:前面有提到的莲君的胖次）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「『捨てといて』」
    voice "voice/真冬/maf_a1_0911.ogg"
    dong 真冬_裸yシャツ_パンツ_目閉じ "『扔了吧』"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「『らじゃ！』」
    voice "voice/心愛/cca_a1_1191.ogg"
    ai 心愛_yシャツ_パンツ有り_笑顔 "『收到！』"

    # 莲 「（おぃい！　気に入ってんだぞ！？）」
    lian "（喂喂喂！我很喜欢这条的啊！？）"

    # 叮咚x1
    play sound "voice/effect/05_玄関チャイム.ogg"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「『はいはいはーい！　ちょっと待ってくださいねー！』」
    voice "voice/心愛/cca_a1_1192.ogg"
    ai 心愛_yシャツ_パンツ有り_笑顔 "『来啦来啦来啦——！请稍微等一下哦！』"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「『玄関脇に盛った塩舐めていからー！』」
    # 参考资料：https://shinnikkei.lixil.co.jp/sumai/column/column_32.html
    voice "voice/真冬/maf_a1_0912.ogg"
    dong 真冬_裸yシャツ_パンツ_無表情 "『去舔舔玄关边上的盐吧——！』（L:中国的一个传说传到了日本，人们开始认为盐是一种邀请客人和带来好运的方式，即使在今天，在传统的餐馆、旅店等地人们在打扫过的门口两边放上一小堆盐，以带来好运）"

    # 久违的长篇豆知识时间！
    luckykeeper "这个传说起源于晋朝。皇帝有很多妻子，每天晚上他都会乘坐牛车到她们家去。皇帝会在牛车停靠的地方过夜，所以其中一位在她的门前放了一堆盐，这是牛喜欢的东西，这样牛车就会停在她家门口。果然，牛停下来舔盐，不愿意动。皇帝于是说：“今晚就在这里”，然后去了那个女人的房间，她在那里得到了皇帝的青睐）"

    # 莲 「俺は牛じゃねぇんだぞ！」
    lian "我又不是牛！"

    # nil 「と言いつ、塩をなめる。さすが、エチオピアの岩塩は美味い。」
    # 参考资料：http://www.kuangyeyuan.com/article/294
    "这么说着，舔了舔盐，不愧是埃塞俄比亚的岩盐，很好吃呢（L:埃塞本地市场的食盐消费量每年25万吨，主要依靠进口。埃塞的盐矿主要是地下岩盐,对之开采以传统手工为主,全国岩盐含量约为30亿吨）"

    # nil 「しかし、こんな物でこの俺が釣られると思ったのか…侮るなよ…。」
    "但是，你以为这样的东西能钓到我吗…别小看我啊…"

    # nil 「と思いながらも塩をなめる。さすが、エチオピアの岩塩は美味い。」
    "一边这么想着一边舔着盐，果然埃塞俄比亚的岩盐很好吃呢"

    # nil 「ドタドタドタドタ！　と家がきしむ音がして、ドアの向こう側に二人分の影が並ぶ。」
    "嘎哒嘎哒嘎哒嘎哒！家里传出吱吱嘎嘎的声音，门后站着两个人的影子"

    # 莲 「入ってもよろしくて？」
    lian "进来之后也请多多关照？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「『うぅー…やっぱり恥ずかしいってばこういうのはぁ～』」
    voice "voice/心愛/cca_a1_1193.ogg"
    ai 心愛_yシャツ_パンツ有り_不機嫌 "『嗯呜——……还是觉得不好意思，这种事情啊~』"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「『今更何を…言い出しっぺは心愛ちゃんじゃないですか』」
    voice "voice/真冬/maf_a1_0913.ogg"
    dong 真冬_裸yシャツ_パンツ_目閉じ "『事到如今还再说什么呢……提案的不是心爱酱吗？』"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「『だ、だがしかし！』」
    voice "voice/心愛/cca_a1_1194.ogg"
    ai 心愛_yシャツ_パンツ有り_真顔 "『然、然而但是啊！』"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「『まふ』」
    voice "voice/真冬/maf_a1_0914.ogg"
    dong 真冬_裸yシャツ_パンツ_まったり "『嘛呼』"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「『まふ』」
    voice "voice/心愛/cca_a1_1195.ogg"
    ai 心愛_yシャツ_パンツ有り_もぐもぐ "『嘛呼』"

    # 心爱 「『ありがとう、どうかしてたよ』」
    voice "voice/心愛/cca_a1_1196.ogg"
    ai 心愛_yシャツ_パンツ有り_笑顔 "『谢谢，刚才脑子一片空白呢』"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「『そんじゃ、お兄ちゃん。はいっていーよ』」
    voice "voice/真冬/maf_a1_0915.ogg"
    dong 真冬_裸yシャツ_パンツ_微笑み "『那就这样，欧尼酱，已经可以进来了』"

    # nil 「そして、少して、ガチャンと音がして家のドアが開いた。」
    "过了一会儿，房门咯噔一声打开了"

    # 音效：开门
    # 场景切换：葛城家门口->葛城家玄关
    # 人物：莲 心爱 真冬
    # BGM：不变
    play sound "voice/effect/07_ドア1～あける.ogg"
    scene 玄関_夕 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=64, reverse=True, alpha=True, time_warp=None)

    # 莲 「ただいまー」
    lian "我回来啦——"

    # 特效：纸吹雪，不好实现考虑直接做成视频
    # 音效：放炮

    # 通过下面的写法可以同时让多个图像 dissolve
    show 心愛_yシャツ_パンツ有り_笑顔 at love69_right
    show 真冬_裸yシャツ_パンツ_微笑み at love69_left
    with dissolve

    play sound "voice/effect/22_クラッカー.ogg"
    show screen papersnow

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 真冬&心爱 「『おかえりなさい！　彼氏くん！』」
    voice "voice/真冬/maf_a1_0916.ogg"
    dong_ai 心愛_yシャツ_パンツ有り_笑顔 "欢迎回来！男朋友！"

    # 莲 「お、おう…」
    lian "啊，嗯……"

    hide screen papersnow

    # nil 「扉をあけると…裸Ｙシャツ姿の真冬と心愛が笑顔で並んでいた。」
    # L:前面所有的裸Ｙシャツ全部统一翻译裸Ｙ衬衫好了，应该从字面意义上就能看懂
    "打开门…穿着裸Ｙ衬衫的真冬和心爱面带微笑站在一起"

    # nil 「手にはクラッカーが握られている。」
    "手里拿着饼干"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「えーと、ご飯にするー？」
    voice "voice/心愛/cca_a1_1198.ogg"
    ai 心愛_yシャツ_パンツ有り_笑顔 "那个，要吃饭吗？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「お風呂にするー？」
    voice "voice/真冬/maf_a1_0917.ogg"
    dong 真冬_裸yシャツ_パンツ_微笑み "去洗澡吗？"

    # 心爱&真冬 「『そーれーとーもー？』」
    voice "voice/真冬/maf_a1_0918.ogg"
    ai_dong 真冬_裸yシャツ_パンツ_微笑み "『还——是——说——要——？』"

    # 心爱&真冬 「『わたしたちにする？』」
    voice "voice/真冬/maf_a1_0919.ogg"
    ai_dong 真冬_裸yシャツ_パンツ_微笑み "『吃掉我们呢？』"

    # 莲 「飯だな」
    lian "吃饭吧"

    # 真冬 「リテイク！」
    # 参考资料：https://www.esp.ac.jp/epv/glossary/09_02.html
    show 真冬_裸yシャツ_基本_見下し3 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0920.ogg"
    dong 真冬_裸yシャツ_基本_見下し3 "Retake！（L:声优业界用语，指重新录制或重新拍摄）"
    hide 真冬_裸yシャツ_パンツ_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はいテイク２はいりまーす！」
    show 心愛_yシャツ_パンツ有り_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1201.ogg"
    ai 心愛_yシャツ_パンツ有り_真顔 "好，准备好Take 2（L:这里不是前面提到的喜剧二人组テイク２，是重来第二次的意思，常见于拍戏）"
    hide 心愛_yシャツ_パンツ有り_笑顔

    # 莲 「ええ…」
    lian "诶…"

    # 场景切换：葛城家玄关->葛城家门口
    # 时间切换到最开始
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 自宅_夕 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「すいません送ってもらっちゃって」
    lian "抱歉让你送我回来了"

    # お姉さん（小姐姐） 「いやいやー、旅は道連れ世は情けってやつでさー。まさかこの日本でヒッチハイクしてる人がいるとはおもわなんだ」
    voice "voice/その他/ex4_a1_0005.ogg"
    xiaojiejie "哪里哪里~旅行就是同路人啊~没想到在日本也会有人搭便车呢"

    # 莲 「ていうか無理にコからやりなおさんでも…。あんたも大変でしょう」
    lian "话说回来你应该不需要重新回来吧……你也太辛苦了"

    # お姉さん（小姐姐） 「そのためのこの車ですよ」
    voice "voice/その他/ex4_a1_0006.ogg"
    xiaojiejie "这辆车就是为了这个（L:前面有提到，德罗宁汽车用于《回到未来系列》电影拍摄）"

    # 莲 「やっぱタイムマシンになってるんや…。じゃぁ、また」
    lian "果然是时间机器啊。……那么，再见"

    # お姉さん（小姐姐） 「ばいばーい！」
    voice "voice/その他/ex4_a1_0007.ogg"
    xiaojiejie "Bye——Bye！"

    # 莲 「…あ、さっきの質問聞き忘れた」
    lian "啊，刚才忘记问之前的事儿了"

    # nil 「改めてドアの前に立つ。」
    "再次站在门前"

    # nil 「相変わらず鍵が閉まっている。まじでもう一度やらす気か。」
    "门还是锁着的。说真的你们想让我再干一次嘛"

    # 莲 「いぜ、今日はとことんお前らのお遊びに付き合ってやる」
    lian "来吧，今天我就陪你们玩个够"

    # nil 「俺はもう一度呼び鈴を押しこむ。」
    "我又按了一次门铃"

    # 叮咚x1
    play sound "voice/effect/05_玄関チャイム.ogg"

    # nil 「ガチャンと鍵があけられたので、ドアを開ける。」
    "门锁砰的一声转动，我打开了门"

    # 开门声
    # 场景切换：葛城家门口->葛城家玄关
    play sound "voice/effect/07_ドア1～あける.ogg"
    scene 玄関_夕 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=64, reverse=True, alpha=True, time_warp=None)

    # 莲 「ただいまー」
    lian "我回来啦——"

    # nil 「プツンッ」
    "噗哧"

    # 莲 「あ？」
    lian "啊？"

    # nil 「敷居をまたいだ瞬間、何か足下で糸を切った手応えを感じる。」
    "跨过门槛的一瞬间，感觉脚下有什么东西被绊断了线"

    # nil 「そして…」
    "然后…"

    # 莲 「うおあっ！！」
    lian "呜啊！！"

    # nil 「ヒュンッ！」
    "咻——！"

    # nil 「音を立て、名状しがたい冒涜的なプラスチック製の黄色い桶のような物が飛んできた。」
    "发出了这样的声音，飞过来了一个塑料制黄色大桶，里面装满了难以名状的亵渎性的液体"

    # nil 「…ケロリンか！」
    # 参考资料：https://www.kerorin.com/fanclub/yurai.html
    # 参考资料：https://www.kerorin.com/fanclub/about.html
    # 参考资料：https://page.om.qq.com/page/O5h_oebkzXUQgXo3lihkXytw0
    "……是ケロリン吗！（L:ケロリン(kerorin)是一款传统的解热头痛药，适用于头痛和生理疼痛，早年厂家在水盆里印上ケロリン字样宣传，经年累月，黄色红字的水盆已经成为了日本钱汤(就是澡堂子)的代名词）"

    # nil 「ギリギリのスウェーで身をかわして、体勢を立て直す。」
    "在千钧一发之际躲开，重新站好"

    # 莲 「っぶねーなー！　ホームアローンかよ！」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%9B%E3%83%BC%E3%83%A0%E3%83%BB%E3%82%A2%E3%83%AD%E3%83%BC%E3%83%B3
    lian "真是的啊！是在拍小鬼当家吗！（L:这个老经典了应该就不需要提了，不知道的话去康康，老有意思了）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「かわしたのでテイク３入りまーす」
    show 真冬_裸yシャツ_基本_見下し3 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0921.ogg"
    dong 真冬_裸yシャツ_基本_見下し3 "因为被躲开了，所以现在开始Take 3——！"

    # 莲 「もうやめてくれ！」
    lian "放过我吧！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「食らえ！」
    show 心愛_yシャツ_パンツ有り_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1202.ogg"
    ai 心愛_yシャツ_パンツ有り_笑顔 "给我恰！"

    # 莲 「ぐふっ」
    lian "嘎呜"

    # scene10 场景1 【按捺不住激动心情飞回家的莲君】 结束
    # scene10 场景2 【果然还是要先恰饭再洗澡，最后才是……】 开始
    # 场景切换：葛城家玄关->葛城家客厅
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=True, alpha=True, time_warp=None)
    scene リビングa_夜 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=True, alpha=True, time_warp=None)

    # nil 「結局ご飯になりました。」
    "结果还是先去吃了饭"

    # nil 「心愛がおなかすいたとゴネたので。」
    "因为心爱说肚子饿了呢"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「興が冷める事をしちゃだめだよお兄ちゃんこの野郎」
    show 真冬_裸yシャツ_基本_見下し3 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0922.ogg"
    dong 真冬_裸yシャツ_基本_見下し3 "别做让人扫兴的事哦，欧尼酱你这个混蛋"

    # 莲 「面目ない」
    # 参考资料：https://www.weblio.jp/content/%E9%9D%A2%E7%9B%AE%E3%81%AA%E3%81%84
    lian "没面子了呢"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「もぐもぐもぐもぐ。やっぱり福島の米はうめぇな！」
    # https://www.pref.fukushima.lg.jp/site/portal-zhc/ 惊了，这个语言选项有点多
    show 心愛_yシャツ_パンツ有り_もぐもぐ at love69_right with dissolve
    voice "voice/心愛/cca_a1_1203.ogg"
    ai 心愛_yシャツ_パンツ有り_もぐもぐ "咕呜咕呜咕呜咕呜。果然还是福岛的米好吃啊！（L:这里应该是指福岛县，核电站是2011年的事，本作是2013年的，根据农林水产省提供的统计数据(2009)，福岛县出产948亿日元的大米(日本第五)，福岛市第一产业占日本第一）"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ほら、気仙沼のマグロとカツオだよ」
    # 参考资料：https://ja.wikipedia.org/wiki/%E6%B0%97%E4%BB%99%E6%B2%BC%E5%B8%82
    show 真冬_裸yシャツ_パンツ_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0923.ogg"
    dong 真冬_裸yシャツ_パンツ_微笑み "来，是气仙沼的金枪鱼和鲣鱼（L:气仙沼市，位于日本宫城县东北端，以盛产鱼翅而闻名）"
    hide 真冬_裸yシャツ_基本_見下し3

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「わあい！」
    show 心愛_yシャツ_パンツ有り_きらきら at love69_right with dissolve
    voice "voice/心愛/cca_a1_1204.ogg"
    ai 心愛_yシャツ_パンツ有り_きらきら "哇咿！"
    hide 心愛_yシャツ_パンツ有り_もぐもぐ

    # 莲 「そういえば、心愛は東北出身だっけか」
    lian "这么说来，心爱好像是出身东北的人吧？"

    # 心爱 「生まれも育ちもみちのくでやんす！」
    # 参考资料：https://ja.wikipedia.org/wiki/%E6%9D%B1%E5%8C%97%E5%9C%B0%E6%96%B9
    show 心愛_yシャツ_パンツ有り_にっこり at love69_right with dissolve
    voice "voice/心愛/cca_a1_1205.ogg"
    ai 心愛_yシャツ_パンツ有り_にっこり "出生和成长都在东北地区！（L:东北地方是日本本州岛上的一个地区，因位于本州的东北部而得名，前面提到的福岛县、气仙沼市、宫城县都属于东北地区）"
    hide 心愛_yシャツ_パンツ有り_きらきら

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「育ちも…？　あれ？」
    show 真冬_裸yシャツ_パンツ_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0924.ogg"
    dong 真冬_裸yシャツ_パンツ_無表情 "成长也是…？啊咧？"
    hide 真冬_裸yシャツ_パンツ_微笑み

    # 心爱 「それ以上は禁忌に触れる事になるから聞かない方がい…」
    show 心愛_yシャツ_パンツ有り_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1206.ogg"
    ai 心愛_yシャツ_パンツ有り_真顔 "在此之上还有触及禁忌的事所以还是不要问比较好…"
    hide 心愛_yシャツ_パンツ有り_にっこり

    # 莲 「わかりました」
    lian "我知道了"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「もう一度言ってみろ」
    voice "voice/真冬/maf_a1_0925.ogg"
    dong 真冬_裸yシャツ_パンツ_無表情 "你再说一遍"

    # 莲 「わかりました」
    lian "我知道了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「よし」
    show 心愛_yシャツ_パンツ有り_無表情 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1207.ogg"
    ai 心愛_yシャツ_パンツ有り_無表情 "好"
    hide 心愛_yシャツ_パンツ有り_真顔

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene リビングa_夜 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「裸エプロンじゃないのか？」
    lian "这不是裸体围裙嘛？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「蓮くんそっちのが好きだったの？」
    show 心愛_yシャツ_パンツ有り_無表情 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1208.ogg"
    ai 心愛_yシャツ_パンツ有り_無表情 "莲君是喜欢那边的人吗？"

    # 莲 「いや…そういうわけでもないが」
    lian "不……也不是那么回事"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「それはお嫁さんがする事じゃないの？」
    show 真冬_裸yシャツ_パンツ_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0926.ogg"
    dong 真冬_裸yシャツ_パンツ_無表情 "那不是新娘该做的事吗？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「そだね。お嫁さんになったらしてあげるよ」
    show 心愛_yシャツ_パンツ有り_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1209.ogg"
    ai 心愛_yシャツ_パンツ有り_笑顔 "是啊，等嫁给你的时候就这样做吧"
    hide 心愛_yシャツ_パンツ有り_無表情

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うん。今は恋人だもんね。こーいう、恋人ならではの楽しみは、ゆっくり一つずつ消化していこ？」
    show 真冬_裸yシャツ_パンツ_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0927.ogg"
    dong 真冬_裸yシャツ_パンツ_微笑み "嗯。现在是恋人呢。这种，只有恋人才有的乐趣，慢慢地一个一个地消化吧？"
    hide 真冬_裸yシャツ_パンツ_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あー！」
    show 心愛_yシャツ_パンツ有り_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1210.ogg"
    ai 心愛_yシャツ_パンツ有り_驚き "啊——！"
    hide 心愛_yシャツ_パンツ有り_笑顔

    # 莲 「なんだ藪から棒に」
    # 参考资料：https://kotobank.jp/word/%E8%97%AA%E3%81%8B%E3%82%89%E6%A3%92-648950
    lian "什么啊，从灌木丛中伸出一根棍子（L:这个谚语是说言行、故事突兀，让人摸不到头脑，或者也可以说突然被别人吓着了，这个说法在前面Scene01的时候莲也这么说过）"

    # 心爱 「まふまふちゃん！　お嫁さんだけど！！　どっちがお嫁さんになればいの！？」
    show 心愛_yシャツ_パンツ有り_ぐるぐる at love69_right with dissolve
    voice "voice/心愛/cca_a1_1211.ogg"
    ai 心愛_yシャツ_パンツ有り_ぐるぐる "嘛呼嘛呼酱！要成为新娘的话！！谁成为新娘比较好呢！？"
    hide 心愛_yシャツ_パンツ有り_驚き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「心愛ちゃんでしょ？　籍は心愛ちゃんが入れて貰って、三人で一緒に住めばいんじゃない？」
    voice "voice/真冬/maf_a1_0928.ogg"
    dong 真冬_裸yシャツ_パンツ_微笑み "应该是心爱酱吧？让心爱酱入籍，然后三个人一起住在一起吧？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「すんなりいった！？　え、で、でも、それでいの？」
    show 心愛_yシャツ_パンツ有り_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1212.ogg"
    ai 心愛_yシャツ_パンツ有り_驚き "似乎很容易的样子啊！？啊、但、但是，这样好吗？"
    hide 心愛_yシャツ_パンツ有り_ぐるぐる

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「いもなにも。私は妹だから、結婚しなくても一緒に住んでもおかしくないもの」
    show 真冬_裸yシャツ_パンツ_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0929.ogg"
    dong 真冬_裸yシャツ_パンツ_無表情 "有什么不好的。我是他的一抹多，所以就算不结婚，住在一起也没什么奇怪的"
    hide 真冬_裸yシャツ_パンツ_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「結婚式はどうするのさー！」
    show 心愛_yシャツ_パンツ有り_ぐるぐる at love69_right with dissolve
    voice "voice/心愛/cca_a1_1213.ogg"
    ai 心愛_yシャツ_パンツ有り_ぐるぐる "那结婚典礼该怎么办啊！"
    hide 心愛_yシャツ_パンツ有り_驚き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「どうとでもなるんじゃないかな？」
    voice "voice/真冬/maf_a1_0930.ogg"
    dong 真冬_裸yシャツ_パンツ_無表情 "我想这其实并不重要？"

    # 莲 「はい先生」
    lian "欸，老师！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はい彼氏くん」
    show 心愛_yシャツ_パンツ有り_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1214.ogg"
    ai 心愛_yシャツ_パンツ有り_不機嫌 "嗯？男朋友"
    hide 心愛_yシャツ_パンツ有り_ぐるぐる

    # 莲 「結婚についてなんだが…」
    lian "关于结婚……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「無粋な事は聞かない事だよお兄ちゃん」
    show 真冬_裸yシャツ_パンツ_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0931.ogg"
    dong 真冬_裸yシャツ_パンツ_目閉じ "不要问无礼的问题哦欧尼酱"
    hide 真冬_裸yシャツ_パンツ_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「そだよー。私達はもう、ずっと一緒に居るって決めてるんだからさ」
    voice "voice/心愛/cca_a1_1215.ogg"
    ai 心愛_yシャツ_パンツ有り_不機嫌 "就是啊，我们已经决定要永远在一起了"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ね。喧嘩した時は、また仲直りしていこ？」
    show 真冬_裸yシャツ_パンツ_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0932.ogg"
    dong 真冬_裸yシャツ_パンツ_微笑み "呐，吵架的时候，也要和好吧？"
    hide 真冬_裸yシャツ_パンツ_目閉じ

    # 莲 「待て待てそういう事じゃない。夏休み、ハワイいくんだろ？　式場探そうぜ。その方が、色々めんどい事も避けれるだろ」
    lian "等等，不是这样的。暑假不是要去夏威夷吗? 我们去那边找婚礼场地吧，这样就可以避免很多麻烦呢"

    # 心爱&真冬 「『！！』」
    show 真冬_裸yシャツ_パンツ_無表情 at love69_left
    show 心愛_yシャツ_パンツ有り_驚き at love69_right
    with dissolve

    voice "voice/真冬/maf_a1_0933.ogg"
    ai_dong 真冬_裸yシャツ_パンツ_無表情 "『！！』"
    hide 真冬_裸yシャツ_パンツ_微笑み
    hide 心愛_yシャツ_パンツ有り_不機嫌

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「…お、お兄ちゃん」
    show 真冬_裸yシャツ_パンツ_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0934.ogg"
    dong 真冬_裸yシャツ_パンツ_目閉じ "……欧、欧尼酱"
    hide 真冬_裸yシャツ_パンツ_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「蓮君…にへ」
    show 心愛_yシャツ_パンツ有り_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1217.ogg"
    ai 心愛_yシャツ_パンツ有り_笑顔 "莲君…欸嘿嘿"
    hide 心愛_yシャツ_パンツ有り_驚き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ハワイで結婚式…かぁ…トロピカルジュース飲み放題…」
    show 真冬_裸yシャツ_パンツ_まったり at love69_left with dissolve
    voice "voice/真冬/maf_a1_0935.ogg"
    dong 真冬_裸yシャツ_パンツ_まったり "在夏威夷举行婚礼…啊…热带果汁无限畅饮……"
    hide 真冬_裸yシャツ_パンツ_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「パイナポウも食べ放題だ…」
    show 心愛_yシャツ_パンツ有り_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1218.ogg"
    ai 心愛_yシャツ_パンツ有り_真顔 "菠萝也可以随便吃…"
    hide 心愛_yシャツ_パンツ有り_笑顔

    # 莲 「どこに引っかってんだよ」
    lian "你俩这是跑哪儿去了？"

    # 画面切换：葛城家客厅（黄昏）
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=True, alpha=True, time_warp=None)
    scene リビングa_夕 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=True, alpha=True, time_warp=None)

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「はーい。じゃぁ、そういう事で。またね」
    show 真冬_裸yシャツ_パンツ_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0936.ogg"
    dong 真冬_裸yシャツ_パンツ_無表情 "好——那就这样吧。再见"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「何の電話してたの？」
    show 心愛_yシャツ_パンツ有り_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1219.ogg"
    ai 心愛_yシャツ_パンツ有り_笑顔 "你在打什么电话呢？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ん、お母さんとお父さんに、心愛ちゃんとお兄ちゃんと結婚するよ。って言ってきた」
    voice "voice/真冬/maf_a1_0937.ogg"
    dong 真冬_裸yシャツ_パンツ_無表情 "嗯，我跟妈妈和爸爸说，我要和心爱酱还有欧尼酱结婚了哦"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぶぇー！　そんな直球で聞いちゃって大丈夫なの！？」
    show 心愛_yシャツ_パンツ有り_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1220.ogg"
    ai 心愛_yシャツ_パンツ有り_驚き "呜欸——！这么直球的问题真的没关系嘛！？"

    # 莲 「で、何て言ってた？」
    lian "那，他们怎么说的？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「あいよー。式にはちゃんと心愛ちゃんの両親も呼ぶんだぞ…だってさ」
    show 真冬_裸yシャツ_パンツ_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0938.ogg"
    dong 真冬_裸yシャツ_パンツ_微笑み "好啊——婚礼上也要邀请心爱酱的父母呢……这样的"
    hide 真冬_裸yシャツ_パンツ_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「かっる！　ええ、蓮君はともかく、真冬ちゃんのパに、娘さんは貰います！　って言わなきゃ！」
    voice "voice/心愛/cca_a1_1221.ogg"
    ai 心愛_yシャツ_パンツ有り_驚き "好棒！欸~，莲君姑且不论，我得对真冬酱的爸爸说「你的女儿我要了」！"

    # 莲 「俺の事も気に掛けてくれよ！」
    lian "为什么我的事情就一笔带过了啊！"

    # 心爱 「あ、パとマの許可はとってるから大丈夫だよ」
    show 心愛_yシャツ_パンツ有り_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1222.ogg"
    ai 心愛_yシャツ_パンツ有り_不機嫌 "啊，我已经得到爸妈的许可了，所以不要紧的哟"
    hide 心愛_yシャツ_パンツ有り_驚き

    # 莲 「ご両親にご挨拶はさせてはくれんのか…」
    lian "不和我的父母打招呼吗……"

    # 心爱 「さっき電話したら『今更何言ってんだよ』って言われた」
    show 心愛_yシャツ_パンツ有り_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1223.ogg"
    ai 心愛_yシャツ_パンツ有り_真顔 "刚才打电话的时候，那边说『事到如今还说什么』"
    hide 心愛_yシャツ_パンツ有り_不機嫌

    # 莲 「そっすか…」
    lian "是吗…"

    # 画面切回晚上
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=True, alpha=True, time_warp=None)
    scene リビングa_夜 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=True, alpha=True, time_warp=None)

    # 莲 「ごちそうさまでした」
    lian "多谢款待"

    # 心爱 「ごちそーさまでした」
    show 心愛_yシャツ_パンツ有り_にっこり at love69_right with dissolve
    voice "voice/心愛/cca_a1_1224.ogg"
    ai 心愛_yシャツ_パンツ有り_にっこり "多谢款待"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「お粗末様でした」
    show 真冬_裸yシャツ_パンツ_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0939.ogg"
    dong 真冬_裸yシャツ_パンツ_目閉じ "粗茶淡饭不成敬意"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ありがとう東北地方！」
    show 心愛_yシャツ_パンツ有り_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1225.ogg"
    ai 心愛_yシャツ_パンツ有り_笑顔 "感谢东北地区！"
    hide 心愛_yシャツ_パンツ有り_にっこり

    # nil 「3人で共同で食器を片付ける。なんだか、三人の距離が今まで以上で最も近づいているような気がして嬉しくなる。」
    "3个人一起收拾餐具。总觉得三个人的距离比以往任何时候都更接近，很开心"

    # nil 「こんな生活が、これから続いていくのかと思うと…なんか、すげぇな。」
    "一想到这样的生活，今后还会持续下去…总觉得，真是太棒了啊"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「んー？　なーにボーっとしてるのさ！　もう、何も我慢しなくていんだからね？」
    show 心愛_yシャツ_パンツ有り_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1226.ogg"
    ai 心愛_yシャツ_パンツ有り_真顔 "嗯？你为什么在发呆呢！已经什么都不需要不忍耐了吧？"
    hide 心愛_yシャツ_パンツ有り_笑顔

    # 莲 「いや…この生活が、これから続くのかーと思うとな…しみじみとな」
    lian "没有没有……只是一想到今后的生活也会这样持续下去…我就感概万千"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「まーた考え事ですか。私達のお尻とかに見とれてくれてたほうが、恥ずい思いした甲斐があるんだけどなー」
    show 真冬_裸yシャツ_パンツ_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0940.ogg"
    dong 真冬_裸yシャツ_パンツ_無表情 "真的是这样的想法吗？要是被我们的屁股看得入迷的话，倒是觉得不好意思才有意义吧"
    hide 真冬_裸yシャツ_パンツ_目閉じ

    # 莲 「いやこれが、結構…来てるんですよ？」
    lian "不，这个、确实……要来吗？"

    # 真冬 「わっ」
    voice "voice/真冬/maf_a1_0941.ogg"
    dong 真冬_裸yシャツ_パンツ_無表情 "哇！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「きゃっ」
    show 心愛_yシャツ_パンツ有り_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1227.ogg"
    ai 心愛_yシャツ_パンツ有り_驚き "呀！"
    hide 心愛_yシャツ_パンツ有り_真顔

    # nil 「台所に並んで作業する、二人の間に入って肩を抱き寄せる。」
    "走到正在厨房干活的两个人中间，抱住她们的肩膀"

    # 莲 「キスしていか？」
    lian "可以吻你们吗？"

    # 心爱 「むー…」
    show 心愛_yシャツ_パンツ有り_無表情 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1228.ogg"
    ai 心愛_yシャツ_パンツ有り_無表情 "真是的——……"
    hide 心愛_yシャツ_パンツ有り_驚き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ん…」
    show 真冬_裸yシャツ_パンツ_目閉じ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0942.ogg"
    dong 真冬_裸yシャツ_パンツ_目閉じ "嗯……"
    hide 真冬_裸yシャツ_パンツ_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「やっぱだめ！」
    show 心愛_yシャツ_パンツ有り_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1229.ogg"
    ai 心愛_yシャツ_パンツ有り_笑顔 "还是不行！"
    hide 心愛_yシャツ_パンツ有り_無表情

    # 莲 「ぶへぇ！　何故だ！」
    lian "蛤！为啥啊！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「歯磨きしてから！」
    voice "voice/心愛/cca_a1_1230.ogg"
    ai 心愛_yシャツ_パンツ有り_笑顔 "刷完牙再说！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「じゃぁお先にお兄ちゃんとチューしちゃうね？　はい、お兄ちゃん。ちゅー」
    show 真冬_裸yシャツ_パンツ_キス at love69_left with dissolve
    voice "voice/真冬/maf_a1_0943.ogg"
    dong 真冬_裸yシャツ_パンツ_キス "那我就先来和欧尼酱亲一下吧？来，欧尼酱，啾——（L:这里真冬的CV也少说了一段捏）"
    hide 真冬_裸yシャツ_パンツ_目閉じ

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「させるかー！」
    show 心愛_yシャツ_パンツ有り_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1231.ogg"
    ai 心愛_yシャツ_パンツ有り_驚き "岂能让你得逞！"
    hide 心愛_yシャツ_パンツ有り_笑顔

    # 莲 「ぐわぁー！」
    lian "呜哇！"

    # 莲 「なんでコッチを突き飛ばすんや」
    lian "为什么你要把我推开啊！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ちゅー」
    show 心愛_yシャツ_パンツ有り_キス at love69_right with dissolve
    voice "voice/心愛/cca_a1_1232.ogg"
    ai 心愛_yシャツ_パンツ有り_キス "啾——"
    hide 心愛_yシャツ_パンツ有り_驚き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ちゅー」
    voice "voice/真冬/maf_a1_0944.ogg"
    dong 真冬_裸yシャツ_パンツ_キス "啾——（L:这里原作就莫得配音）"

    # 莲 「滅茶苦茶だろお前ら」
    lian "你们这都是搞啥呢？"

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene リビングa_夜 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「なんでこの家はチョコ味の歯磨き粉がないのよさ」
    show 心愛_yシャツ_パンツ有り_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1233.ogg"
    ai 心愛_yシャツ_パンツ有り_不機嫌 "为什么这个家没有巧克力味的牙膏呢？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「練りワサビならあるよ」
    show 真冬_裸yシャツ_パンツ_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0945.ogg"
    dong 真冬_裸yシャツ_パンツ_無表情 "芥末酱的话倒是有的"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「歯磨き粉ですらないじゃないかよぉ！」
    show 心愛_yシャツ_パンツ有り_驚き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1234.ogg"
    ai 心愛_yシャツ_パンツ有り_驚き "甚至连牙膏都没有啊！"
    hide 心愛_yシャツ_パンツ有り_不機嫌

    # 莲 「俺のだ」
    lian "那是我的"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「し、死ぬぞあんた…」
    show 心愛_yシャツ_パンツ有り_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1235.ogg"
    ai 心愛_yシャツ_パンツ有り_真顔 "你、你会死的……"
    hide 心愛_yシャツ_パンツ有り_驚き

    # 原地tp
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene リビングa_夜 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 心爱 「歯を磨きまんた」
    show 心愛_yシャツ_パンツ有り_にっこり at love69_right with dissolve
    voice "voice/心愛/cca_a1_1236.ogg"
    ai 心愛_yシャツ_パンツ有り_にっこり "我刷完牙了"

    # nil 「歯を磨きまんた。」
    "刷过了牙"

    # 莲 「さて…と、やり残したことはないか？」
    lian "那么啊…还有什么没做完的事情吗？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「お風呂ー！　と思ったけど…せっかくの裸Ｙシャツが…もったいないね…」
    show 心愛_yシャツ_パンツ有り_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1237.ogg"
    ai 心愛_yシャツ_パンツ有り_真顔 "去洗澡！本来是这么想的……难得的裸Ｙ衬衫……太可惜了……"
    hide 心愛_yシャツ_パンツ有り_にっこり

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「終わってから入ればいんじゃないの？　三人でさ」
    show 真冬_裸yシャツ_パンツ_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0946.ogg"
    dong 真冬_裸yシャツ_パンツ_無表情 "等结束之后再进去不好吗？三个人一起"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あ、その手があったか！」
    hide 心愛_yシャツ_パンツ有り_真顔
    show 心愛_yシャツ_パンツ有り_笑顔:
        zoom 1.5
        xalign 0.8918
        yalign -0.09
        linear 0.15 yalign 0.02
        linear 0.15 yalign -0.09
    voice "voice/心愛/cca_a1_1238.ogg"
    ai 心愛_yシャツ_パンツ有り_笑顔 "啊、原来还有这招！"

    # 莲 「三人で背中とか流し合えばいんじゃないのか？」
    # lian "三个人互相搓背不好嘛？"
    lian "三个人互相搓背不香嘛？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ついでにエッチもね？」
    show 真冬_裸yシャツ_パンツ_ニタァ at love69_left with dissolve
    voice "voice/真冬/maf_a1_0947.ogg"
    dong 真冬_裸yシャツ_パンツ_ニタァ "顺便一说H也是吧？"
    hide 真冬_裸yシャツ_パンツ_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「きゅぅ～…いきなり刺激的すぎます…お風呂はゆっくり入りましょう…」
    show 心愛_yシャツ_パンツ有り_ぐるぐる at love69_right with dissolve
    voice "voice/心愛/cca_a1_1239.ogg"
    ai 心愛_yシャツ_パンツ有り_ぐるぐる "Q~……！突然太刺激辽……等洗澡的时候慢慢仔细洗洗吧…"
    hide 心愛_yシャツ_パンツ有り_笑顔

    # 莲 「お前の価値観がわかんねぇよ」
    lian "我搞不懂你的价值观"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「だって…ぬるぬるプレイじゃん…」&&（L:有点没搞懂，应该是弄的到处都是得好好收拾吧，不然只能是咕噜咕噜玩水？好像说不大过去）
    show 心愛_yシャツ_パンツ有り_不機嫌 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1240.ogg"
    ai 心愛_yシャツ_パンツ有り_不機嫌 "因为…不是会弄得到处都是嘛…"
    hide 心愛_yシャツ_パンツ有り_ぐるぐる

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そこまでは考えてなかったかな…言われてみれば確かにそうだけど」
    show 真冬_裸yシャツ_パンツ_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0948.ogg"
    dong 真冬_裸yシャツ_パンツ_無表情 "没考虑到这一点呢…说起来确实是这样"
    hide 真冬_裸yシャツ_パンツ_ニタァ

    # nil 「結局、三人でお風呂に入る事にはなりましたが、その時どうなったかは…ご想像にお任せます。」
    "最后，三个人决定先一起洗澡，那个时候发生了什么样的事情呢？那就任凭你想象了"

    # 莲 「じゃぁ、行くか。部屋」
    lian "那么、去房间吧"

    # nil 「ぎゅっ」
    "嗒"

    # nil 「二人の手を握る。」
    "握住两个人的手"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はーい。…ごくり。緊張する…初めてじゃないのに…」
    voice "voice/心愛/cca_a1_1241.ogg"
    ai 心愛_yシャツ_パンツ有り_不機嫌 "好——有点紧张……明明不是第一次了……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ね…。今まで一番緊張するかも…。あはっ、すっごいテンパってる私」
    show 真冬_裸yシャツ_パンツ_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0949.ogg"
    dong 真冬_裸yシャツ_パンツ_微笑み "呐……可能是到现在为止最紧张的…欸嘿嘿，我的心情好紧张"
    hide 真冬_裸yシャツ_パンツ_無表情

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「上手にできるかな…」
    show 心愛_yシャツ_パンツ有り_ポカーン at love69_right with dissolve
    voice "voice/心愛/cca_a1_1242.ogg"
    ai 心愛_yシャツ_パンツ有り_ポカーン "能做得很好吗……"
    hide 心愛_yシャツ_パンツ有り_不機嫌

    # 莲 「心配ない。俺も緊張してる」
    lian "别担心，我也很紧张"

    # nil 「二人とも緊張して黙ってしまったが、俺が部屋へ向かうために手を引っ張ると、素直についてきてくれた。」
    "两个人都紧张得不说话了，但当我拉着她们的手走向房间时，她们还是老实地跟了过来"

    # nil 「部屋までの階段がやたらと長く感じる。心愛と真冬、二人いっぺんに結ばれる。」
    "通往房间的楼梯感觉特别长。心爱和真冬，两个人在一起"

    # nil 「自分が何をしようとしているか…今になって理解する。」
    "我现在才明白自己要做什么……"

    # nil 「俺も男だ、覚悟するしかない。」
    "我也是男人，只有做好觉悟"

    # 画面切换：葛城家客厅->葛城家二楼走廊
    scene 自宅二階廊下_夜 at love69_bg1440 with dissolve

    # nil 「そうこうしてるうちに、部屋の前にたどり着く。」
    "就这样，我们来到了房间前面"

    # 莲 「つきました」
    lian "到了呢"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「…はい」
    show 心愛_yシャツ_パンツ有り_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1243.ogg"
    ai 心愛_yシャツ_パンツ有り_真顔 "……是啊"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「なんか…いつもと違う風景に見える…ね…」
    show 真冬_裸yシャツ_パンツ_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0950.ogg"
    dong 真冬_裸yシャツ_パンツ_微笑み "总觉得…看起来和平时不一样…呢…"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「このドアを開けたら…もう後戻りはできない世界にいくのですね…私達は」
    show 心愛_yシャツ_パンツ有り_無表情 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1244.ogg"
    ai 心愛_yシャツ_パンツ有り_無表情 "一旦打开这扇门……就再也回不到原先的世界了……我们几个"
    hide 心愛_yシャツ_パンツ有り_真顔

    # 莲 「準備の程はよろしいですか？」
    lian "准备的怎么样了？"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「私は…うん、大丈夫…だと、思う。心愛ちゃんは？」
    show 真冬_裸yシャツ_パンツ_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_0951.ogg"
    dong 真冬_裸yシャツ_パンツ_無表情 "我觉得…嗯，没问题……吧。心爱酱呢？"
    hide 真冬_裸yシャツ_パンツ_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「だ、大丈夫だ、問題ない…」
    # L:来康这个：https://www.bilibili.com/video/BV1U7411Z7cP?p=1
    show 心愛_yシャツ_パンツ有り_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1245.ogg"
    ai 心愛_yシャツ_パンツ有り_真顔 "大、大丈夫萌大奶"
    hide 心愛_yシャツ_パンツ有り_無表情

    # 莲 「じゃぁ…」
    lian "那么…"

    # nil 「二人を抱き寄せて顎をあげさせる。」
    "把两个人搂在一起，抬起她们的下巴。"

    # nil 「こまで本当に長かった。だが、これで、二人に隠す事は何もない。」
    "真的是走了很的时间呢，不过，这样我们之间就没有什么隐瞒的事了"

    # 莲 「心愛からな」
    lian "心爱可以吗"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ん…ちゅぅ…」
    show 心愛_yシャツ_パンツ有り_キス at love69_right with dissolve
    voice "voice/心愛/cca_a1_1246.ogg"
    ai 心愛_yシャツ_パンツ有り_キス "嗯…啾……"
    hide 心愛_yシャツ_パンツ有り_真顔

    # 莲 「次は…真冬」
    lian "接下来是…真冬"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「はぁい…んっ…」
    show 真冬_裸yシャツ_パンツ_キス at love69_left with dissolve
    voice "voice/真冬/maf_a1_0952.ogg"
    dong 真冬_裸yシャツ_パンツ_キス "好……嗯…"
    hide 真冬_裸yシャツ_パンツ_無表情

    # 莲 「で、二人」
    lian "那么，两个人"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「まふゆちゃ…んっ…」
    voice "voice/心愛/cca_a1_1247.ogg"
    ai 心愛_yシャツ_パンツ有り_キス "真冬酱……嗯……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「こあちゃ…んっ…」
    voice "voice/真冬/maf_a1_0953.ogg"
    dong 真冬_裸yシャツ_パンツ_キス "心爱酱……嗯……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あとは…」
    show 心愛_yシャツ_パンツ有り_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1248.ogg"
    ai 心愛_yシャツ_パンツ有り_真顔 "还有……"
    hide 心愛_yシャツ_パンツ有り_キス

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「お兄ちゃん…」
    show 真冬_裸yシャツ_パンツ_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_0954.ogg"
    dong 真冬_裸yシャツ_パンツ_微笑み "欧尼酱……"
    hide 真冬_裸yシャツ_パンツ_キス

    # 心爱&真冬 「『…ちゅぅっ』」
    show 真冬_裸yシャツ_パンツ_キス at love69_left
    show 心愛_yシャツ_パンツ有り_キス at love69_right
    with dissolve
    voice "voice/真冬/maf_a1_0955.ogg"
    ai_dong 真冬_裸yシャツ_パンツ_キス  "『……啾』"

    # nil 「三人で唇を触れあわせる、初めてのキス。」
    "三个人的嘴唇互相碰触，这是三个人第一次接吻"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はぁー…」
    voice "voice/心愛/cca_a1_1250.ogg"
    ai 心愛_yシャツ_パンツ有り_キス "哈啊——……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「はぁ…はぁ…」
    voice "voice/真冬/maf_a1_0956.ogg"
    dong 真冬_裸yシャツ_パンツ_キス "哈…哈…"

    # nil 「二人は照れた様子で、頬を赤く染めた。」
    "两个人害羞得满脸通红"

    # 画面切换到莲卧室
    image bg 自室a_夜_消灯 = "/images/bg/自室a_夜_消灯.png"
    scene 自室a_夜_消灯 at love69_bg1440 with dissolve

    # nil 「ガチャッ…」
    "嘎吱……"

    # nil 「ガチャッ…」
    "静静地打开门，邀请她们进入房间。虽然没有开灯，但还是被月光照亮了"

    # nil 「正直言って何をするかはノープランだ。だが、こはノリと勢いで…なんとか乗り切って見せる！」
    "老实说，接下来怎么做我是没有计划的，不过，这里就用气势……挺过去吧！"

    # nil 「パタンッ」
    "啪嗒"

    # nil 「真冬がゆっくりと扉を閉めた。次にあの扉が開かれるときは、俺達の関係は変わっている。」
    "真冬慢慢地关上了门。下次这个门再打开的时候，我们的关系就已经改变了吧"

    # nil 「ごくり。息を呑む音が静かに部屋に木霊する。」
    "现在，屏住呼吸的声音静静地在房间里回响"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「はぁ…はぁ…」
    voice "voice/心愛/cca_a1_1251.ogg"
    ai 心愛_yシャツ_パンツ有り_キス "哈啊……哈啊……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「ん…ふぁ…はぁ…」
    voice "voice/真冬/maf_a1_0957.ogg"
    dong 真冬_裸yシャツ_パンツ_キス "嗯…啊…哈…"

    # nil 「二人とも未だに緊張したようすで、俺の事を潤んだ目付きで見つめてくる。」
    "两个人都还很紧张，用湿润的眼神看着我"

    # nil 「俺は、ベッド脇にたって、両手を広げた。」
    "我站在床边，张开双臂"

    # 莲 「おいで。真冬、心愛」
    lian "来吧，真冬，心爱"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 心爱&真冬 「『…うんっ…せーのっ（小声）』」
    show 心愛_yシャツ_パンツ有り_笑顔 at love69_right
    show 真冬_裸yシャツ_パンツ_微笑み at love69_left
    with dissolve
    voice "voice/真冬/maf_a1_0958.ogg"
    ai_dong 真冬_裸yシャツ_パンツ_微笑み "『……嗯…3——2（小声）』"
    hide 真冬_裸yシャツ_パンツ_キス

    # 莲 「えっ？」
    lian "欸？"

    # nil 「と俺が疑問を浮かべる前に、彼女達二人は俺の懐に潜り込んでいた。」
    "在我的疑问浮现出来之前，她们两个已经钻进了我的怀里"

    # nil 「広げた手よりも、もっと下に。」
    "比我张开的双臂要低"

    # nil 「これは…タックル！？」
    "这是……抢跑！？"

    # nil 「ボスッ」
    "扑嗵"

    # nil 「俺は反応しきれず、ベッドに押し倒された。」
    "我还没反应过来，就被推倒在了床上"

    # 心爱&真冬 「『Jackpot！』」
    voice "voice/真冬/maf_a1_0959.ogg"
    ai_dong 真冬_裸yシャツ_パンツ_微笑み "『Jackpot！（L:正中头奖！，一般形容彩票等需要碰运气的头奖）』"
    hide 心愛_yシャツ_パンツ有り_キス

    # 莲 「えー！」
    lian "欸——！"

    # nil 「真冬と心愛は俺の身体の上でハイタッチした。さっきまでの切なそうな表情はなんだったのか。」
    "真冬和心爱在我的身上击掌。刚才你们脸上的悲哀表情是怎么肥事儿啊！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「さてさて…それじゃぁ、いっちょ…おっぱじめるとしますか」
    # おっぱじめる “开始”的流行说法 参考：https://www.weblio.jp/content/%E3%81%8A%E3%81%A3%E3%81%B1%E3%81%98%E3%82%81%E3%82%8B
    voice "voice/真冬/maf_a1_0960.ogg"
    dong 真冬_裸yシャツ_パンツ_微笑み "好了好了……那么，我们就准备……开始吧……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「おいっす！　はいはーい、さぁ、御開帳だァ！」
    # L:开香槟咯！关键词：(C97)芹沢あ〇ひの夜の顔 (アイドルマスターシャイニーカラーズ) [中国翻訳] P10-P11
    voice "voice/心愛/cca_a1_1254.ogg"
    ai 心愛_yシャツ_パンツ有り_笑顔 "好耶！来来——那么，开张啦！（L:开香槟咯！(关键词：(C97)芹沢あ〇ひの夜の顔)(アイドルマスターシャイニーカラーズ) P10-P11）"

    # 心爱&真冬 HScene01 Skip~

    # Skip但是不完全Skip！后面的稍微翻一点点防止剧情断档（这里就不夹带私货了），然后接第二天早上，这里的背景接HS之前的莲房间

    # 心爱 1255-1396 Skip~
    # 真冬 961-1090 Skip~
    image bg nice_boat = "images/extra/luckykeeper/nice_boat.png"
    if persistent.hsceneG:
        scene nice_boat with dissolve
        pause 2.0

    else:
        pass

    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 自宅洗面所_夜 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「（やれやれ…二人がこんなにエロいとは…身体、持つかな俺…）」
    lian "（哎呀哎呀，两个人竟然这么好色……身体，撑得住吗我…）"

    # nil 「シャワーを浴びたら少しだけ正気を取り戻した。」
    "洗了个澡，稍微清醒了一点"

    # nil 「トランクスとＴシャツだけ着て、部屋へと戻る。」
    "只穿上平角胖次和T恤，回到了房间"

    image bg ycg_2_2_2_2 = "/images/ev/ycg_2_2_2_2.png"
    scene ycg_2_2_2_2 with dissolve

    # 心爱 「ちゅぅ…ちゅりゅっ…はぁう…もぉ…あっ、はぁあぁあんっ」
    voice "voice/心愛/cca_a1_1397.ogg"
    ai 心愛_下着_基本_キス "嗯呜…嗯呜…呜…呜…呜…哇…啊，啊啊啊啊啊"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「んちゅぅ…ぁっ、や、あっ、だ、めぇっ…んぁあっ！」
    voice "voice/真冬/maf_a1_1091.ogg"
    dong 真冬_下着_基本_キス "嗯…啾……啊，啊……不行……啊呜……"

    # 莲 「…お前らな…」
    lian "……你们……"

    image bg ycg_2_2_3_3 = "/images/ev/ycg_2_2_3_3.png"
    scene ycg_2_2_3_3 with dissolve

    # 真冬 「おにいちゃぁん…」
    voice "voice/真冬/maf_a1_1092.ogg"
    dong 真冬_下着_基本_キス "欧尼酱……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「れんくぅん…」
    voice "voice/心愛/cca_a1_1398.ogg"
    ai 心愛_下着_基本_キス "莲~君~……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 心爱&真冬 「『ちょーだい？』」
    voice "voice/真冬/maf_a1_1093.ogg"
    ai_dong 真冬_下着_基本_微笑み_1 "『等一下？』"

    # 莲 「徹夜だな…こりゃ」
    lian "开夜车了啊…这是……"

    # nil 「俺はため息をついてから、もう何度目かは忘れたが、二人に覆い被さった。」
    "我叹了一口气，已经不知道是第几次了，但还是被两个人覆盖了"

    # Black~
    # scene10 场景2 【果然还是要先恰饭再洗澡，最后才是……】 结束
    # scene10 场景3 【暑假的第一天当然要去约会啦】 开始

    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 心爱&真冬 「『あむっ』」
    voice "voice/真冬/maf_a1_1094.ogg"
    ai_dong 真冬_私服_基本_微笑み "『哈呜』"

    # 场景切到早上莲卧室
    play music bgmthirteen fadeout 2.0 fadein 4.0
    scene 自室a_朝 at love69_bg1620 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 莲 「おひょおう！」
    lian "哦yooooooooo！"

    # nil 「両耳に湿った柔らかい感触を感じて、俺は意識を覚醒させた。」
    "感觉到两耳湿润柔软的触感，我意识一下子清醒了过来"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「おっはよー彼氏くん！　昨夜は沢山幸せをありがとーございました！」
    show 心愛_私服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1401.ogg"
    ai 心愛_私服_基本_笑顔 "早上好，男朋友！谢谢你昨晚给我带来的幸福！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「はろーまいだーりん。うん、凄く楽しかったよ…」
    show 真冬_私服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1095.ogg"
    dong 真冬_私服_基本_微笑み "哈——喽~My Darling，嗯，非常开心呢"

    # 莲 「よ、よう…二人ともいやに元気だな…」
    lian "哟、哟……你们两个人康起来都很元气嘛……"

    # nil 「俺の視界がはっきりした時には、二人は着替えを済ませており、」
    "当我视野清晰的时候，两个人已经都换好衣服了"

    # nil 「体中に付着した体液なども綺麗に取り払われていた。」
    "附着在身上的体液之类的也已经被漂亮地清理干净了"

    # nil 「二人からはシャンプーとボディソープの香りが漂ってくる。」
    "飘来了两个人身上洗发水和沐浴露的香味"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「一足お先に、さっぱりしてきちゃいました！」
    voice "voice/心愛/cca_a1_1402.ogg"
    ai 心愛_私服_基本_笑顔 "先走一步啦，感觉清爽多了！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「うちのお風呂は三人じゃ狭いからね」
    show 真冬_私服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1096.ogg"
    dong 真冬_私服_基本_無表情 "我们家的浴室三个人用的话还是太挤了呢"
    hide 真冬_私服_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「まふまふちゃんのテクは凄かったです…」
    show 心愛_私服_基本_泣き at love69_right with dissolve
    voice "voice/心愛/cca_a1_1403.ogg"
    ai 心愛_私服_基本_泣き "嘛呼嘛呼酱的技术还真是厉害呢……"
    hide 心愛_私服_基本_笑顔

    # 莲 「そうか…そいつはよかった…」
    lian "是吗…那真是太好了呢…"

    # nil 「きっと二人でジャレあってたんだろう。朝からご苦労な事だ。」
    "一定是两个人在一起ghs了吧。从早上开始就辛苦了呢"

    # 心爱 「さぁさぁ、一日は短いんだから、ちゃっちゃと起きて下さいな！」
    show 心愛_私服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1404.ogg"
    ai 心愛_私服_基本_嬉しい "好啦好啦，一天的时间是很短暂的，请快点起来吧！"
    hide 心愛_私服_基本_泣き

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そうだよ。彼女待たせるなんて酷い彼氏だぞ」
    show 真冬_私服_基本_嬉しい at love69_left with dissolve
    voice "voice/真冬/maf_a1_1097.ogg"
    dong 真冬_私服_基本_嬉しい "就是啊，让女朋友一直等着可是不酷的男朋友哦"
    hide 真冬_私服_基本_無表情

    # 莲 「へいへい…。なんだ、今日はめでたい日かなんかなのか…？」
    lian "emmmm……什么啊，今天是由什么喜事儿还是什么大日子啊……？"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「そりゃー決まってるでしょー！　夏休み初日っすよー！」
    show 心愛_私服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1405.ogg"
    ai 心愛_私服_基本_笑顔 "那是当然的啦！今天是暑假的第一天！"
    hide 心愛_私服_基本_嬉しい

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「デートいこうよ、お兄ちゃん！」
    voice "voice/真冬/maf_a1_1098.ogg"
    dong 真冬_私服_基本_嬉しい "去约会吧，欧尼酱！"

    # 莲 「なーるほどな…おーけい、そういうことなら…よっこらせっと！」
    lian "原来如此——……阿嚏，既然如此……那就出发吧！"

    # nil 「俺は反動をつけて起き上がり、二人が用意してくれた衣服に着替える。」
    "我利用反作用力坐起来，换上两个人给我准备的衣服"

    # nil 「日は既にあがっており、確かに、デートには最適な快晴だ。」
    "太阳已经升起，的确，确实是最适合约会的晴天"

    # 莲 「うし、行くか」
    lian "那么。出发吧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「おー！　ってどこに？」
    voice "voice/心愛/cca_a1_1406.ogg"
    ai 心愛_私服_基本_笑顔 "哦——！那，去哪里？"

    # 莲 「そんなん行きながら適当に考えれば良いだろ」行くか」
    lian "一边走一边考虑就好啦"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「そうだね。心愛ちゃん行きたいところは？」
    show 真冬_私服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1099.ogg"
    dong 真冬_私服_基本_微笑み "是啊，心爱酱你想去哪里捏？"
    hide 真冬_私服_基本_嬉しい

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ＵＳＪのほら、魔法学校のアレ！」
    show 心愛_私服_基本_嬉しい at love69_right with dissolve
    voice "voice/心愛/cca_a1_1407.ogg"
    ai 心愛_私服_基本_嬉しい "ＵＳＪ的辣个，魔法学校的那个！（L:大版的环球影城，有霍格沃茨魔法学校，感兴趣的百度一下就有）"
    hide 心愛_私服_基本_笑顔

    # 莲 「それまだ出来てねぇんだな…あと日帰り距離で頼むわ」
    lian "那个还没做好呢（L:2013年的时候还没有完全建好）…还有，拜托你想个一日游能到达的距离"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「じゃぁ…できたてのカップルが行ったら別れるっていうジンクスの…」
    show 真冬_私服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1100.ogg"
    dong 真冬_私服_基本_無表情 "那……有说法刚组成的CP去了就要分手的……"
    hide 真冬_私服_基本_微笑み

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「でじにー！」
    # 参考资料：https://play-life.jp/articles/1416
    show 心愛_私服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1408.ogg"
    ai 心愛_私服_基本_笑顔 "Disney！（L:法务部发来律师函(doge)；霓虹人很喜欢传一些「CP去了就会分手的地方」，迪士尼和刚才提到的ＵＳＪ都有入选，原因是因为人太多了，等待时间太长，CP面面相觑，无话可说，压力会比较大，容易上头）"
    hide 心愛_私服_基本_嬉しい

    # 莲 「前置き余計だなおい！　そこならまぁ…良いか」
    lian "前面的话多余了！那里的话……可以吗"

    # 心爱 「ほんとはピューロランドが好きだけどな…」
    # 参考资料：https://loco.yahoo.co.jp/place/g-Ipt__3Bbi-I/?utm_source=dd_spot&sc_e=sydd_spt_slo_p_ttl&lsbe=1
    show 心愛_私服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1409.ogg"
    ai 心愛_私服_基本_真顔 "其实我很喜欢Puroland呢…（L:Sanrio Puroland，东京的三丽鸥彩虹乐园）"
    hide 心愛_私服_基本_笑顔

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「私はカップヌードルミュージアムかな…」
    # 参考资料：https://www.cupnoodles-museum.jp/zh-cn/
    # 参考资料：https://www.bilibili.com/video/BV1mg4y1i7m3 4：03
    voice "voice/真冬/maf_a1_1101.ogg"
    dong 真冬_私服_基本_無表情 "我的话是杯面博物馆吧…（L:在横滨和大版池田这个官方网站有中文可以去康康：https://www.cupnoodles-museum.jp/zh-cn/ ，这个纪念馆纪念了方便面的发明人、日清食品的创始人安藤百福）"

    # 莲 「舞浜いくぞ」
    # 参考资料：https://ja.wikipedia.org/wiki/%E8%88%9E%E6%B5%9C
    lian "去舞浜吧（L:是关东地方千叶县浦安市的地名，浦安市因市内的东京迪士尼乐园而知名，对的，东京迪士尼乐园不在东京在千叶）"

    # 心爱&真冬 「『はーい♪』」
    show 心愛_私服_基本_笑顔 at love69_right
    show 真冬_私服_基本_嬉しい at love69_left
    with dissolve
    voice "voice/真冬/maf_a1_1102.ogg"
    ai_dong 真冬_私服_基本_嬉しい "『好——♪』"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「じゃぁ、準備しておくから、シャワー浴びてきてね」
    show 真冬_私服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1103.ogg"
    dong 真冬_私服_基本_微笑み "那我先去准备好了，你去洗个澡吧"
    hide 真冬_私服_基本_嬉しい

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ヒゲも剃ってくるんだぞ！　ただし二枚刃までしか使えない」
    # 参考资料：https://ja.wikipedia.org/wiki/%E5%AE%89%E5%85%A8%E5%89%83%E5%88%80
    voice "voice/心愛/cca_a1_1411.ogg"
    ai 心愛_私服_基本_笑顔 "也把胡子全部剃掉吧！但是只能用双刃刀（L:1971年左右，吉列推出了双刃剃须刀，虽然说双刃刀属于安全剃刀，但是刀片锋利，误操作还是容易刮伤自己）"

    # 莲 「残念だが、俺は四枚刃を愛用しているんでな…おし、浴びてくるわ」
    # 参考资料：https://ja.wikipedia.org/wiki/%E5%AE%89%E5%85%A8%E5%89%83%E5%88%80
    lian "很遗憾，我喜欢用四刃刀呢…我去洗澡了（L:2008年吉列推出了四刃剃须刀）"

    # nil 「二人と同時に部屋を出て、心愛と真冬はリビングへ、俺は風呂場へ。」
    "我们同时走出房间，心爱和真冬去了客厅，我去了浴室"

    # BGM切换
    # 场景切换：莲卧室->葛城家浴室
    play music bgmfourteen fadeout 2.0 fadein 4.0
    scene 自宅洗面所_昼 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「『あ、お兄ちゃん、こに着替え置いとくね』」
    show 真冬_私服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1104.ogg"
    dong 真冬_私服_基本_微笑み "『啊，欧尼酱，我把换的衣服放在这里了昂』"

    # 莲 「おう、助かるわ」
    lian "啊，得救了"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「じー」
    show 心愛_私服_基本_きらきら at love69_right with dissolve
    voice "voice/心愛/cca_a1_1412.ogg"
    ai 心愛_私服_基本_きらきら "盯——"

    # 莲 「いやん」
    lian "别啊"

    # 场景切换：葛城家浴室->葛城家玄关
    image bg 玄関_朝 = "/images/bg/玄関_朝.png"
    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 玄関_朝 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ふあーすっごい良い天気！　ザ・バケイション！」
    show 心愛_私服_基本_笑顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1413.ogg"
    ai 心愛_私服_基本_笑顔 "哇啊——真是不错的天气啊！The vacation！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「んー…気持ちい…。ほらほら、空ばっかり見てると転ぶよ心愛ちゃん」
    show 真冬_私服_基本_微笑み at love69_left with dissolve
    voice "voice/真冬/maf_a1_1105.ogg"
    dong 真冬_私服_基本_微笑み "嗯——……感觉真好~……好啦好啦，老是看天空的话会摔倒的哦，心爱酱"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ぶえー！」
    hide 心愛_私服_基本_笑顔
    show 心愛_私服_基本_ぶわー:
        zoom 1.5
        xalign 0.8918
        yalign -0.09
        linear 0.15 yalign 0.02
        linear 0.15 yalign -0.09
    voice "voice/心愛/cca_a1_1414.ogg"
    ai 心愛_私服_基本_ぶわー "呜欸——！"

    # 莲 「いわんこっちゃない」
    lian "不是这么说了嘛"

    # 心爱 「ぽよーん」
    show 心愛_私服_基本_真顔 at love69_right with dissolve
    voice "voice/心愛/cca_a1_1415.ogg"
    ai 心愛_私服_基本_真顔 "扑通！"
    hide 心愛_私服_基本_ぶわー

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「跳ねた」
    show 真冬_私服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1106.ogg"
    dong 真冬_私服_基本_無表情 "跳起来了"
    hide 真冬_私服_基本_微笑み

    # 画面切换：湛蓝天空
    image bg 空 = "/images/bg/空.png"
    play music bgmtwentyeight fadeout 2.0 fadein 4.0
    scene 空 at love69_bg1440 with dissolve

    # nil 「三人で玄関をくぐり、透き通る青空を見上げた。」
    "三个人穿过玄关，仰望着清澈的蓝天。"

    # nil 「黄金色の太陽が、本格的な夏の訪れをつげている。」
    "金色的太阳宣告着真正夏天的到来"

    # nil 「心愛と真冬と恋人として過ごす日々の訪れを。」
    "和心爱还有真冬一起度过恋人的日子"

    # nil 「こんな日々がずっと続ていくだろう。根拠はないが、俺には自信がある。」
    "这样的日子一定会一直持续下去吧。虽然没有根据，但是我有自信"

    # nil 「風がそっと頬を撫でる。」
    "风轻轻拂过我的脸颊"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ねぇねぇ彼氏くん彼氏くん」
    voice "voice/心愛/cca_a1_1416.ogg"
    ai 心愛_私服_基本_笑顔 "呐呐男朋友君男朋友君"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「おにーちゃんおにーちゃん」
    voice "voice/真冬/maf_a1_1107.ogg"
    dong 真冬_私服_基本_嬉しい "欧尼酱欧尼酱"

    # 莲 「ん？」
    lian "嗯？"

    # 心爱&真冬 「『…ちゅっ♪　だいすき♪』」
    # 原作这里改回「」了，我们还是统一用『』吧，好康一些
    voice "voice/真冬/maf_a1_1108.ogg"
    ai_dong 真冬_私服_基本_微笑み "『…啾♪最喜欢♪』"

    # 进OP！
    $ renpy.movie_cutscene("video/Love69_OP.webm")

    scene 遊園地_商店街

    # nil 「遊園地にて」
    "在游乐园里"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 热狗 「ホットドッグいかがすかー！」
    # 记得去加人物表
    ## 没有跳过
    show 想瑠_hot_ニヤリ at love69_xiangliu_right with dissolve
    voice "voice/想瑠/sol_a1_0154.ogg"
    hotdog 想瑠_hot_ニヤリ "来份热狗怎么样——！"

    # 这个语句是针对花盆君设计的参数，能够调整花盆君在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.15
    $ sideimagesize.SideImageYalign = 1.21
    $ sideimagesize.SideImageZoom = 0.5

    # 定义花盆君在最右的参数
    transform love69_huapen_rightest:
        zoom 0.89
        xalign 1.07
        yalign -18.0

    # 花盆君 「植木鉢いかがですかー！」
    ## 没有跳过
    show 花盆君_通常:
        zoom 0.89
        xalign 1.07
        yalign -18.0
        linear 0.15 yalign -15.5
        linear 0.15 yalign -18.0
    with dissolve
    voice "voice/アシュリー/ash_a1_0038.ogg"
    pen 花盆君_通常 "来买盆植物怎么样——！"

    # 莲 「あ」
    lian "啊！"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「あ」
    show 心愛_私服_基本_笑顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_1418.ogg"
    ai 心愛_私服_基本_笑顔 "啊！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「あ」
    show 真冬_私服_基本_無表情 at love69_left with dissolve
    voice "voice/真冬/maf_a1_1109.ogg"
    dong 真冬_私服_基本_無表情 "啊"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 热狗 「あ」
    show 想瑠_hot_見下し at love69_xiangliu_right with dissolve
    voice "voice/想瑠/sol_a1_0155.ogg"
    hotdog 想瑠_hot_見下し "啊"
    hide 想瑠_hot_ニヤリ

    # 这个语句是针对花盆君设计的参数，能够调整花盆君在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.15
    $ sideimagesize.SideImageYalign = 1.21
    $ sideimagesize.SideImageZoom = 0.5

    # 花盆君 「あ」
    show 花盆君_通常:
        zoom 0.89
        xalign 1.07
        yalign -18.0
        linear 0.15 yalign -10.5
        linear 0.15 yalign -18.0
    voice "voice/アシュリー/ash_a1_0039.ogg"
    pen 花盆君_通常 "啊"

    # 莲 「……」
    lian "……"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「……」
    voice "voice/心愛/cca_a1_1419.ogg"
    ai 心愛_私服_基本_笑顔 "……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「……」
    voice "voice/真冬/maf_a1_1110.ogg"
    dong 真冬_私服_基本_無表情 "……"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 热狗 「……」
    voice "voice/想瑠/sol_a1_0156.ogg"
    hotdog 想瑠_hot_見下し "……"

    # 这个语句是针对花盆君设计的参数，能够调整花盆君在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.15
    $ sideimagesize.SideImageYalign = 1.21
    $ sideimagesize.SideImageZoom = 0.5

    # 花盆君 「……」
    voice "voice/アシュリー/ash_a1_0040.ogg"
    pen 花盆君_通常 "……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 三人 『お前喋れたのかよ！？』
    # 记得去加人物表
    show 想瑠_hot_驚き at love69_xiangliu_right with dissolve
    voice "voice/真冬/maf_a1_1111.ogg"
    lianaidong 真冬_私服_基本_無表情 "『你原来会说话啊！？』（L:蚌埠住了）"
    hide 想瑠_hot_見下し

    # 这个语句是针对花盆君设计的参数，能够调整花盆君在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.15
    $ sideimagesize.SideImageYalign = 1.21
    $ sideimagesize.SideImageZoom = 0.5

    # 花盆君 「…（ふりふり）」
    voice "voice/アシュリー/ash_a1_0041.ogg"
    pen 花盆君_通常 "......（摇晃摇晃）"

    # 莲 「何でアンタが突っ込むんだよ！」
    lian "你为什么在这个里面啊！"

    # 这个语句是针对想瑠喵设计的参数，能够调整想瑠喵在对话框里面的位置
    $ sideimagesize.SideImageXalign = -0.01
    $ sideimagesize.SideImageYalign = -1.65
    $ sideimagesize.SideImageZoom = 1.1

    # 热狗 「うるせえ！」
    show 想瑠_hot_見下し at love69_xiangliu_right with dissolve
    voice "voice/想瑠/sol_a1_0158.ogg"
    hotdog 想瑠_hot_見下し "无路赛！"
    hide 想瑠_hot_驚き

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「って、想瑠にゃんじゃん！」
    voice "voice/心愛/cca_a1_1421.ogg"
    ai 心愛_私服_基本_笑顔 "这，不是想瑠喵嘛！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「気づいてなかったの！？」
    voice "voice/真冬/maf_a1_1112.ogg"
    dong 真冬_私服_基本_無表情 "你没注意到吗！？"

    # scene10 场景3 【暑假的第一天当然要去约会啦】 结束

    # Scene10 结束！

    # 过场：心爱（常服）

    $ quick_menu = False

    play sound "voice/effect/moosehead honk (stinger).ogg"
    stop music fadeout 4.0
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)
    scene アイキャッチ心愛 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)

    $ renpy.pause(1.5, hard=True)
    $ renpy.end_replay()

    jump scene11

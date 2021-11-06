# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene02 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：WorldlineChanger（一处豆知识）
# 版本 0.1.0
# Blog：http://b.luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2021年11月6日

# 当前流程：整理生肉文本，翻译并润色

label scene02:
    # scene02 开始
    # 地点：雾叶店内
    # 人物： 雾叶（店长） 莲 心爱
    # BGM：雾叶店内的音乐（嘤语的）

    # scene02 场景1 【雾叶小店】 开始

    image bg 霧葉ちゃんのお店 = "images/bg/霧葉ちゃんのお店.png"
    scene 霧葉ちゃんのお店 with wiperight

    # nil 「案内された店内は、アメリカンダイナーの名に恥じない、クラシックでアメリカ風の装飾で、」
    "进入店内，映入眼帘的是经典的美式装饰，雀食和传单上宣传的美式餐厅的名号很匹配呢"

    # nil 「７アップやコーラと言ったネオンサインが壁中に飾られており、」
    # ７アップ 七喜
    # 参考资料：https://ja.wikipedia.org/wiki/セブンアップ_(飲料)
    "墙上挂满了霓虹灯（L:RGB！）七喜（７アップ）和可乐（L:７アップ，7.Up，七喜，是百事可乐的柠檬汽水品牌，1929年在密苏里州圣路易斯开始生产，叫7.Up最普遍的说法是7和u说明七喜包含7种调料并且进行过碳酸化）"

    # nil 「端には、ジュークボックスがネオン管をちらつかせながら、レコード特有の錆び付いた音色を奏でている。」
    "在唱片的边缘，点唱机摇晃着霓虹灯，奏出唱片特有的锈迹斑斑的音色"

    # nil 「天井には三機のシーリングファンがゆっくりとまわっていた。」
    "天花板上有三个吊扇在慢慢转动"

    # nil 「店主の趣味なのか、ベッカムのサインボールが飾られている。しかも野球ボールで。」
    "也许是店主的兴趣吧，店内装饰着贝克汉姆的签名球，而且还是棒球"

    # 这里的雾叶改叫店长了，应对方法：单独建立店长文件夹（这个等写脚本的阶段统一完成），代号dinerowner
    # 店长 「店主の趣味なのか、ベッカムのサインボールが飾られている。しかも野球ボールで。」
    dinerowner "咻——呦——咻——嗞咚！"

    # 莲 「あんた何やってんだよ」
    "你在干啥子嘞？"

    # 店长 「スペースシャトルの打ち上げです」
    dinerowner "这是航天飞机的发射"

    # 莲 「チュドーンはまずいだろチュドーンは…」
    # 参考资料：https://dic.pixiv.net/a/ちゅどーん
    lian "这声儿不大对啊"

    # 店长 「ヒューストンに…ヒューストーン！」
    # L的梗不知道请玩COD6或者康这个https://www.bilibili.com/video/av329767923/
    dinerowner "休斯顿…休斯顿！（L:休斯顿，请待命，我们可能有麻烦了(cod6)）"

    # 莲 「くっだらねぇなおい！」
    lian "淦哦！无聊死了！"

    #nil 「俺が色々用を済ませて、トイレの扉を開けると、」
    "我把各种事请都办完了，打开厕所的门"

    # nil 「店主の女性がルートビアのペットボトル（しかも中身が入っている）を持って、ロケット発射の真似事をしていた。」
    # 参考资料：https://ja.wikipedia.org/wiki/ルートビア
    "女店主拿着根汁汽水塑料瓶(而且里面装满了液体)在模仿火箭发射（L:根汁汽水/根汁啤酒，Root beer，起初命名为根汁茶（Root tea），禁酒令时期为了推销给煤矿工人，改称根汁啤酒，但实际上无添加酒精成分。是一种在北美洲流行的含糖汽水饮料）"

    # 店长 「あ、中身入ってる…」
    dinerowner "啊，里面原来有东西的嘛…"

    # 莲 「気づいてなかったのかよ！」
    lian "绝了，你没注意到吗！"

    # 店长 「まぁ…いか…いただきまーす」
    dinerowner "嘛…怎么样都好了…我开动了"

    # nil 「当然の事ながら、ペットボトルから大量の泡が吹き出した。」
    "理所当然地，从塑料瓶里面喷出了大量的泡沫"

    # 店长 「わっ」
    dinerowner "哇！"

    # 莲 「当たり前だろ！　少しは悩みたまえ！」
    lian "当然会这样的吧！倒是稍微思考一下啊喂！"

    # 店长 「やれやれ…最近の炭酸ジュースは不親切設計ですね…」
    dinerowner "哎呀呀…最近的碳酸果汁设计得相当不亲切啊…"

    # 莲 「あんた天然なのかそれとも炭酸飲むの初めてなのか、どっちだ？」
    lian "啊这，你是天然呆，还是第一次喝碳酸饮料啊？"

    # 店长 「いやぁ久しぶりにこっちの世界に戻ってきたんで、うっかりしてましたよ」
    dinerowner "哎呀，好久没回这个世界了，我一不小心就忘了"

    # 莲 「まるで異世界にいたかのような口ぶりだな…もしくは、危ない薬でもやってたのか？向こうでは一部合法らしいしな」
    lian "你的口气好像在异世界一样……或者说，你磕了什么危险的药吗？似乎在某些地方好像有一部分是合法的"

    # 店长 「似たようなものです。あそうそう、お姫様はぐっすり寝てますよ」
    dinerowner "差不多。对了，公主睡得很香哦"

    # nil 「店主の女性が手を差しのばして、窓際のテーブル席へと案内すると、クッションを枕代わりに、心愛がソファーに寝かせられていた。」
    "女店主伸出手，把她领到窗边的桌子上，把靠垫当做枕头，让她躺在桌子旁的沙发座椅上面"

    # 心爱 「すーっ…すーっ…むにゃ…すぅ…じゅるっ…ふがしたべる…すーっ」
    ai "嗯…呜…呜嗯…呼…呼喵…泚溜…还挺好次的嘛…嗯…"

    # nil 「思いっきり腹を殴られた割に、心地よさそうに寝息を立ている。」
    "虽然被暴打了一顿，但是现在却是很舒服地呼呼大睡呢"

    # nil 「心なしか、先ほどよりも顔色がい。血行が良くなったのか？」
    "也许是心理作用吧，感觉现在的脸色比刚才更苍白了，血液循环还好吗？"

    # 莲 「世話になりました」
    lian "承蒙关照了"

    # 店长 「いえいえ、事の顛末を見ていないので詳細はわかりかねますが、受け入れたら受け入れたで彼女は後で後悔するだろうけど、如実に拒絶したら彼女を傷付けてしまう。だから、こは他人の手を借りよう…そんな所でしょうか」#中间加几句以使句子在中文下更好理解
    dinerowner "没有没有，我不知道事情的来龙去脉，详细情况也还不太清楚呢。（所以事情实际上是什么情况呢？）是那种如果接受告白的话，她以后可能后悔，但是如果拒绝的话又会伤害到她，所以，只好借别人的手了。是这种情况吗？"

    # 莲 「人の心理の詳細まで寸分違わず把握、お見事です」
    lian "连我的心理细节都看透了，真是厉害呢"

    # 店长 「額に書いてありましたんでね」
    dinerowner "都写在额头上了呢"

    # 莲 「顔じゃないかなそれ。額だと、肉とかしか書かれてないと思う」
    lian "不应该是脸吗，额头上除了肉可是啥也没有哦"

    # 店长 「お姫様の額にでも書きますか？」
    dinerowner "那要在公主的额头上写一下吗？"

    # 莲 「チョコレートソースで書いたら喜ぶとは思う」
    lian "我觉得如果你用巧克力酱写的话她会很开心的"

    # 店长 「チョコで…肉って…ぷっ…チョコを…ちょこっと…ぷっ」
    dinerowner "巧克力…肉…噗…巧克力…稍微…噗（L：这里是谐音梗）"

    # 莲 「ツボに入ったのかよ。しかも後半全然関係無いじゃねぇか」
    lian "你这是被点到笑穴了吗？这和后半部分完全没有关系哦"

    # nil 「自分で思い付いたダジャレで自爆した店主を尻目に、夢心地の心愛に近寄る。」
    "把被自己想到的冷笑话逗笑的店主扔在后面，接近沉浸在梦乡里的心爱"

    # 店长 「起こすつったら、やっぱ王子様のキスですか？」
    dinerowner "要叫醒公主的话，果然应该是王子殿下的吻吧？"

    # 莲 「そんな事した日にゃ、俺が恥ずかしくて寝たきりになっちまう」
    lian "如果做了这种事的话，我会害羞到卧床不起的"

    # 店长 「でも、女の子はそういうの、結構期待してると思いますよー？」
    dinerowner "但是，我觉得女孩子都很期待这样的事情哦？"

    # 莲 「あんたもそういうのが趣味が？」
    lian "你是不是也喜欢这样呢？"

    # 店长 「いえ、私は女の子にしてあげる方です」
    dinerowner "不，我只会给女孩子做这样的事情"

    # 莲 「そういう趣味か。似合いそうだ」
    lian "原来是这样的性趣吗？好像挺适合你的"

    # 店长 「これはどうも。…ん…これはこれは…？」
    dinerowner "理解万岁！嗯…这个是…？"

    # 心爱 「むにゃ…みねすとろーねもたべる…すぅ…」
    ai "嗯姆…那种地方…是不可以摸的啊"

    # nil 「店主の女性が何か異変に気づいたのか、一度店の奥に戻り、何かを持って戻ってきた。」
    "女店主似乎发现了什么异常，从店里面拿着什么东西出来了"

    # 店长 「鼻提灯…いけますかね？」
    dinerowner "鼻灯笼... 可以吗?（L:还记得上一幕心爱给真冬做的鼻灯笼吗？这波啊，这波是以其人之道，还其人之身！危险动作不要模仿哦）"

    # 莲 「それ吸えるポリバルーンだろ！？女子の間で流行ってんのか！？そこのお姫様も、今日うちの妹にやってたよ…」
    lian "是那种可以吸的塑料气球吧（L:一定不能吸哦！）？这个在女生之间很流行吗？那里的公主今天也给我妹妹做了一个呢…"

    # 店长 「このケミカルな香りが…またハイにさせてくれるんですよね…」
    dinerowner "这种化学香味...又要让我嗨起来了捏..."

    # 莲 「それについては同意するが…まぁ、止めはしないよ」
    lian "雀食...我不会阻止你的，冲鸭!"

    # 店长 「じゃぁ、お言葉に甘えまして…’！……Let's show down！」
    dinerowner "那我就不客气了!…Let's show down!"

    # 心爱 「ふがっ」
    ai "呜哇！（L:你可能会觉得对话框心爱的小头像有点怪，不知道从哪儿来的奶糖苹果，但是原作就是这样的捏...）"

    # 店长 「あっ」
    dinerowner "啊..."

    # 莲 「…なんでストローごと鼻の穴に突っ込むんだよ…。しかも今日このツッコミ２回目だよ…」
    lian "为什么连吸管都要把插到鼻孔里面…而且这是我今天第二次吐槽这个了…"

    # 原地tp

    # nil 「心愛が目覚めたのはその発言から凡そ５分後だった。」
    "心爱在5分钟后才苏醒过来（L:所以说这么搞很⑧靠谱嘛）"

    # 原地tp

    # 心爱 「ふぁ…よく寝た…はっ！　こ、こはどこ！　わたしは誰！」
    ai "呼啊…睡得好苏福…啊！这、这是哪！我是谁！（我要做什么？！L:人生三问还差一句呢）"

    # 店长 「こは第三惑星ジェネシス、君はEDFの惑星探査員で地質学者の『エレナ・ユン・グラード』だ」
    # 第三惑星ジェネシス 参考资料：https://ja.wikipedia.org/wiki/猿の惑星:_創世記
    # EDFの惑星 参考资料：https://ja.wikipedia.org/wiki/宇宙戦艦ヤマト
    # 『エレナ・ユン・グラード』 不知道是什么梗？
    dinerowner "这是创世纪第三行星，你是EDF行星探查员，地质学家的『艾莉娜・尤恩・格拉德』（L:这乱洗脑可不好呀，想到了『少女理论及其周边』里面的恶搞FD『从兄妹理论及其周边』）"

    luckykeeper "又到豆知识时间啦!创世纪第三行星（第三惑星ジェネシス）是猩球崛起（猿の惑星: 創世記）的梗，EDF行星探查员（EDFの惑星探査員）应该是『宇宙战舰大和号』里地球防卫军的梗，人名实在没看出来是哪里的"

    # 心爱 「そうか…私はEDFの惑星探査員で地質学者の『エレナ・ユン・グラード』…！」
    ai "是吗…我是EDF行星探查员，地质学家的『艾莉娜・尤恩・格拉德』…！"

    # 莲 「洗脳するのはおやめなすって。この子そういうの信じちゃうから」
    lian "别给她洗脑了，她会相信的"

    # 心爱 「くっ…私が眠ってから何年経ったというのだ…。他の探検隊のメンバーは一体…私は…何かされたのか…だめだ、何も思い出せん…」
    ai "啊...我已经沉睡了几年了...其他探险队的成员...我...是不是被人做了什么...不行，我什么都想不起来了...（L:小仓朝阳既视感233）"

    # 莲 「ね」
    lian "啊这"

    # 店长 「…面白いですね…」
    dinerowner "真是很有趣呢"

    # 莲 「はいはい心愛ちゃん、ご気分はいかがですか？先ほどは随分お楽しみのようでしたね」
    lian "好啦好啦，心爱，你现在感觉怎么样? 刚才你似乎玩得很开心呢"

    # 心爱 「…へ？　ぶえぇえ！あ、あの、あの、れ、れんく…ん…えとえと…」
    ai "啊？欸？！…呃？！那、那个，莲君，那个……"

    # nil 「先ほどのを思い出したのか、急に赤面しだして目線を泳がせた。」
    "也许是想起了刚才的事，她突然脸红了，视线飘忽不定"

    # 莲 「覚えてはいらっしゃるようだな…」
    lian "好像还记得呢…"

    # 心爱 「は…ぃ…あぅ…ちょっと本気で…恥ずかし…ぅ…はー…どーして私あんな事しちゃったんだろ」
    ai "哈……啊……刚刚有点认真…真是不好意思……哈…我怎么做了那种事呢？"

    # 莲 「心愛って、あいう事って結構消極的っつーか…苦手なん？」
    lian "心爱，你好像对那种事请很消极的来着…是不擅长吗？"

    # 心爱 「えっ！？　その辺ほじくり返すトークなの！？ど、どうしよう！　心の準備若干できてないよ！？」
    ai "啊! ? 这是在挖苦我吗? 怎、怎、怎、怎么办? 我还没有做好心理准备呢! ?"

    # 莲 「忘れた方がいなら忘れとくぞ。カウントもしないでおく」
    lian "如果你想让我忘记的话，我会忘掉这件事的。我不会计较的"

    # 心爱 「そ、それも寂しい気がするけど…！　とりあえず一旦置いといて貰えると助かります。というか…いやまぁ、私はぶっちゃけ全部覚えてるんだけど…冷静だね蓮くん…」
    ai "嗯，虽然这我觉得这样会很寂寞……！总之先把这事儿放一边的话就帮了我大忙了。或者说... 不，坦白说，我记得刚才所有的事情…真冷静呢莲君…"

    # 莲 「自分がどうすべきかわかっていたからな。あのアイスを食べさせたのは俺だし、粗相はせんよ」&感觉翻的有点问题
    lian "因为我知道自己该做什么。让你吃那个冰淇淋的人是我，所以我会妥善处理的"

    # 心爱 「あ、でも！　あのアイスは本当に美味しかったよ！また食べたいにゃー！どこで売ってるの？」
    ai "啊，但是！那个冰淇淋真的是很好吃呢！还想吃喵！在哪里卖呢？（L；这里原作的配音就少了一句，但是配的字是有“在哪里卖呢？”这句）"

    # 莲 「あーそれはな…」
    lian "啊，那是…"

    # nil 「とりあえず、心愛に、あのアイスを手に入れた経緯を説明した。」
    "总之，我向心爱解释了我是如何得到那个冰淇淋的"

    # nil 「『恋が叶う魔法のアイス』という売り文句はひとまず秘密にしたまで。」
    "『实现恋爱的魔法冰淇淋』这个卖点就暂且保密吧"

    # 心爱 「ほへー…じゃぁ、まだお店では買えないんだねー。ほんとすっごく美味しかった…！　一口で食べたのはもったいなかったなー」
    ai "啊这…那还不能在店里买到呢。真的非常好吃呢…！当时一口吃了下去真是可惜啊"

    # 莲 「そうだな…。今度からは優しくおねだりする事だな…」
    lian "是这样的……所以，下次再想恰的时候啊，你要温柔地乞求哦"

    # nil 「そういえば…「一気に食べさせるな」なんて忠告を受けてたような気がするが…。」
    "这么说来…我觉得好像听到过『别一口气恰完』这样的忠告来着…"

    # nil 「心愛の反応を見る限り、味は良かったらしい。」
    "从心爱的反应来看，味道雀食似乎很不错的亚子呢"

    # nil 「そして些か過剰ではあるが、『恋が叶う』という機能も取りそろえている。」
    "虽然效果有点太过剩了，但是确实是具备了『实现恋爱』的功能"

    # nil 「もう少し機能を調整すれば存外、悪い商品ではないのだろう。」
    "如果再稍微调整一下效果的话，就不会是不好的商品了吧"

    # nil 「尤も、今のまでは悪用されるのではないかとすら不安も覚えるが。」
    "不过，从现在这样的效果来看的话，我不禁担心这个东西会被滥用呢"

    # nil 「同時に、俺以外が心愛に食べさせていたら…と考えると、少しゾッとする。」
    "同时，一想到如果除了我之外还有其他人用这个给心爱恰... 我就有点毛骨悚然"

    # nil 「まだ少し紅潮はしているが、落ち着きを取り戻したであろう心愛を眺める。」
    "看向心爱，虽然她还有点脸红，但是已经平静下来了"

    # 心爱 「む…あ、あの…そんなに見つめられると、さっきの事思い出しちゃうよ…ね？」
    ai "嗯…那、那个……被那样盯着看的话，刚才的事会想起来吧…？"

    # 莲 「お、おう、すまん…」
    lian "啊、啊这，对不起…"

    # nil 「いつもの、抜けているようで飄々とした態度（一部トチ狂っている）ではなく、年頃の女の子らしい態度で、照れる心愛。」
    "现在的心爱不再是平常那种似乎有些飘忽不定的态度(甚至有时候可以说是有点疯狂的) ，而是像这个年龄段的女孩子那样，害羞的心爱"

    # nil 「それが妙に新鮮で、気恥ずかしくなる。」
    "这让我感到有点奇妙的新鲜和尴尬"

    # nil 「実際の所、心愛があの時どう思っていたかを知りたくなってきたが…。少し時間をおくとしよう。」
    "事实上，我现在也开始想知道心爱当时是怎么想的...稍微花点时间留意一下吧"

    # 店长 「はいお待たせ致しました。ストロベリーショートパンケーキですよっと」
    dinerowner "来，让您久等了，这是草莓蛋糕"

    # 心爱 「わーい☆　おいしそー！」
    ai "哇咿☆~，好好吃啊！"

    # 莲 「え？　頼んじゃいないけど…」
    lian "啊嘞？我记得我没点过来着？"

    # 店长 「お二人とも姉さんにチラシ渡されて来たクチでしょう？　サービスですよ」
    dinerowner "你们两位都是被姐姐的传单吸引的吧？是免费的哦"

    # 莲 「姉さ…ん？」
    lian "姐姐…嗯？"

    # nil 「確かにチラシを渡されたが、この人の姉にではなく、植木鉢くんに渡されたのだが…。」
    "确实是收到了传单，但是不是从这个人的姐姐那里，而是从花盆君那儿…"

    # nil 「概ね、この人の姉から貰ったチラシを、俺達に渡したという所だろうか。」&感觉翻的不对
    "大概是她姐姐把传单交给花盆君了吧"

    # 店长 「あー…口が滑りましたね。今の発言は忘れて下さい」
    dinerowner "啊…嘴飘了，请忘记刚才的发言"

    # 心爱 「あっ！　てんちょーさん！　先ほどはどうもありがとうございました！お陰様で目が覚めた上に、なんだか身体が軽いです！」
    ai "啊! 店长桑! 刚才真是太感谢您了! 托您的福我醒过来了，而且感觉身体轻飘飘的!"

    # 店长 「どういたしまして。血行をよくするツボを突いたので、そのせいでしょうね」
    dinerowner "不用客气。是因为刺中了促进血液循环的穴位吧?大概是这个原因吧"

    # 莲 「ただのボディブローじゃなかったのか…」
    lian "原来不是单纯的身体打击吗"

    # 心爱 「蓮君には見えてなかったか…実はあの時私は１６発殴られている」
    ai "莲君没看到吗... ... 其实当时我挨了十六拳"

    # 莲 「お前には見えてたのかよ。すげぇ動体視力だな」
    # 参考资料：https://ja.wikipedia.org/wiki/視力#静止視力・動体視力
    lian "原来你看见了吗？真是厉害的动态视力啊（L:动态视力（動体視力）指不移开视线，持续识别移动物体的能力）"

    # nil 「その気になれば避けれてたんじゃないのか…？まぁいや。」
    "那当时如果心爱想避开的话，是不是就可以避开了呢... ？算了算了，不管了"

    # nil 「俺達の座るテーブルに置かれたそのパンケーキは、標準よりも大きめのサイズで、」
    # パンケーキ 英文：pancake，中文是煎饼的意思，这里结合上下文应该翻成“蛋糕胚”，后面根据情况翻成“蛋糕”
    "放在我们桌子上的那个蛋糕胚的尺寸比标准的大"

    # nil 「三段重ねになっており、パンケーキ同士の間には生クリームとカットされた苺が挟まれている。」
    "三层重叠，蛋糕里面之间夹着鲜奶油和切好的草莓"

    # nil 「しかもその上から苺のソースがたっぷりとかけられて、普通に美味しそうだ。」
    "而且上面撒了很多草莓酱，看起来很好吃呢"

    # 店长 「少し大きめに作りましたので、お二人で仲良く分けて食べてくださいな」
    dinerowner "稍微做大了一点，两个人好好分着吃吧"

    # 莲 「でもそうしたら、あんた商売あがったりなんじゃないか？俺がなんか頼むよ」
    lian "这样的话，你这生意要亏本的吧? 我来帮忙做点什么吧"

    # 店长 「気にしなくて大丈夫ですよ。もし、そのパンケーキ食べて足りなかったらその時に何かご注文下さいな」
    dinerowner "不用在意。如果恰了那个蛋糕之后还没恰饱的话，请在那个时候再点东西"

    # 心爱 「ぷはーっ！　ごちそうさまでしたー！おいしかったですにゃー！」
    ai "哇！谢谢您的款待！很好吃喵！"

    # 莲 「…すまん、一口も食べる前に無くなった」
    lian "不好意思，我还没吃一口就没了"

    # 店长 「これは予想外でした…」
    dinerowner "这真是意料之外的情况呢…"

    # 心爱 「あ゛…もしかして、全部食べちゃまずかったパターン…？　ぶえごめんよう、甘い物を見るとつい…自分を抑えきれず…」
    ai "啊~难道是一口吃完就会觉得不好吃那种类型…？呜欸…对不起啦，一看到甜食就忍不住自己……"

    # 莲 「まぁ確かにお前は自分を抑えきれない女だからな」
    lian "嘛，你确实是无法抑制自己的人啊"

    # 心爱 「ぶえ…」
    ai "呜欸…"

    # 店长 「あは、良いですよ、もう一個サービスしちゃいます。今度はしっかり、蓮君に食べさせてあげるんですよ、心愛ちゃん」
    dinerowner "啊哈哈，没事的，我再给你们做一个。这次一定要好好地给莲吃哦，心爱酱"

    # 心爱 「あい！　頑張って耐えます！」
    ai "啊！我会努力忍耐的！"

    # 莲 「なんか、すんません。良くしてもらってるみたいで」
    lian "总觉得不好意思。你对我们太好了"

    # 店长 「いえいえ。お似合いな二人って、見ていて楽しいのですよ」
    dinerowner "哪里哪里。只是因为你们两个人很般配，所以看着很开心罢了"

    # 心爱 「そ、そうかな…！？　私達ってお似合い…かな？」
    ai "是、是这样吗…！？我们看起来很般配吗？"

    # 莲 「俺に聞かれても答えにくいな…心愛はどう思う？」
    lian "即使问我也很难回答呢……心爱觉得怎么样呢？"

    # 心爱 「に…似合ってたら嬉しいかも…！」
    ai "如果是这样的话，我也许会很开心呢…！"

    # 莲 「じゃぁその線でいこうか」
    lian "那我们就走这条线吧（L:这就进心爱线了？！）"

    # 心爱 「うん！」
    ai "嗯！"

    # 店长 「くすっ。じゃ、少々お待ちくださいね」
    dinerowner "哈哈。那就请稍等一下"

    # nil 「店主の女性は微笑んで、厨房へと入っていった。」
    "女店主微笑着走进了厨房"

    # nil 「新しいパンケーキができあがるまでの間、俺達に特に会話は無かったが、終始心愛はニコニコしっぱなしであった。」
    "在新的蛋糕做好之前，我们没有什么特别的对话，但是心爱始终保持着微笑"

    # 原地tp

    # 心爱 「ぬお！　蓮くんにあ～んってしてあげたいのに…！　手が…手が勝手に私の口にパンケーキを運ぶ…！　くっ…！」
    ai "啊——！我本来想“啊”地喂给莲君——的…！手…手它擅作主张地把蛋糕送到自己的嘴里去了…！啊…！"

    # 莲 「自分で食うわ」
    lian "我自己喂自己吃"

    # 心爱 「ひぎい」
    ai "呜呜"

    # 店长 「私がやりましょうか？」
    dinerowner "我来吧"

    # 心爱 「させぬ！」
    ai "不会让你的得逞的！"

    # 店长 「いや、あ～んされる側を」
    dinerowner "不，是被喂的那方"

    # 心爱 「それなら大丈夫」
    ai "那就没事儿了"

    # 莲 「俺に食わせろ！」
    lian "喂我吃吧！"

    # 原地tp

    # 心爱 「ぷはー！大変美味しゅう御座いました！ぺこり」
    ai "噗哈! 非常好吃! 多谢款待!"

    # 莲 「ごちそうさま。美味しかった」
    lian "多谢款待。很好吃"

    # 店长 「ご満足頂けたなら何より。是非お友達にも紹介してあげてくださいね」
    dinerowner "能让你们满意的话就太好了，请一定要向朋友介绍一下"

    # 心爱 「今度はまふまふちゃんも連れてきたいね！」
    ai "下次想把嘛呼嘛呼酱也带来呢！"

    # 莲 「あ、あいつも好きなはずだぜ、こういう雰囲気のお店。一時あいつヴィレヴァンでネオンサイン本気で欲しがって、止めるのにコーラをおごってやった記憶がある」
    # 参考资料：https://baijiahao.baidu.com/s?id=1613270635119941843&wfr=spider&for=pc
    # 参考资料2：https://en.wikipedia.org/wiki/Village_Vanguard_(Japanese_bookstore)
    # 参考资料3：https://en.wikipedia.org/wiki/Village_Vanguard
    # 根据语境，这里指的应当是Village Vanguard书店，俱乐部应该不卖灯，而且俱乐部在米国不在11区
    lian "啊，那家伙应该也喜欢这种气氛的店。我记得有一段时间那家伙在 Village Vanguard (L：是11区一家不务正业的书店)想买要霓虹灯，为了阻止她我请她喝了可乐"

    # 店长 「近くにヴィレヴァンに卸してるネオン屋さんありますよ。クッションと一緒に売ってる」
    # “ヴィレヴァン”应该是书店的简称
    dinerowner "那家店附近有批发给它家的霓虹灯店哦，和靠垫一起卖的"

    # 莲 「それは是非俺の妹には教えないでやってくれ、バイト代を全部ネオンにつぎ込みかねん」
    lian "这事千万别告诉我妹妹，她会把打工的钱都花在霓虹灯上的"

    # 心爱 「でもさー、まふまふちゃんは想瑠にゃん達と何やってんの？」
    ai "说起来啊，嘛呼嘛呼酱和想瑠喵她们在干什么呢？"

    # 莲 「温泉掘るためのボーリング調査つってた」
    lian "为了挖掘温泉而进行的钻探调查"

    # 心爱 「ぐっ…い、いきたい…じゅるり…趣味なんだよ…穴を弄るのが…凄く趣味なんだ…」
    ai "嗯…嗯，我也想去啊…嗯…我的兴趣是…玩弄小洞…是我的兴趣……（L:心爱你好涩啊）"

    # 店长 「穴があったら弄りたいお年頃ですもんね」
    dinerowner "正是有了洞就想玩的年纪呢"

    # 莲 「セクハラ…？　まぁいや。この後どうする？心愛は予定とかあんの？」
    lian "性骚扰... ? 算了，接下来怎么办? 心爱有什么计划吗"

    # 心爱 「へ？　特に無いよ。あるとしたらネットで木こりの画像を集めて、顔をブラピに差し替えて遊ぶぐらいかな。結構評判がいのだよこれが」
    # 参考资料：https://ja.wikipedia.org/wiki/ブラッド・ピット
    ai "啊？没什么特别的。有的话，就在网上收集伐木工的画像，然后把脸换成布拉德·皮特，这个很受欢迎呢（L：布拉德·皮特（11区爱称ブラピ），美国男演员及电影制片人，获得过多个奥斯卡奖项）"

    # 莲 「その予定はキャンセルできないか？」
    lian "那个计划能取消吗？"

    # 心爱 「ほ？　何？何かお手伝いが必要だったりする事があるの？鉱石の採掘？」
    ai "哦？什么什么？有什么需要帮忙的吗？开采矿石？"

    # 莲 「お前は穴を弄るのがそんなに好きか。もし俺がレアメタルを必要になったらその時は頼る」
    lian "你那么喜欢玩洞洞吗？如果以后我需要稀有金属的话，那就拜托你了"

    # 心爱 「まっかせてー！　で、今回は採掘じゃなくて…？」
    ai "交给我啦！那么，这次不是开采…？"

    # 莲 「まぁ、なんだ、さっきアイスを一本ゆっくり食べさせてあげられなかったんで、埋め合わせを…あー…」
    lian "嘛，刚才没能让你好好品尝冰淇淋，想补偿你一下来着……"

    # 心爱 「お？　お？あれは私が原因だから気にしなくていのに！」
    ai "哦？哦？！那是我的原因，所以别在意"

    # 店长 「くすくす」
    dinerowner "哈哈"

    # 莲 「えい回りくどい表現は苦手だ！言い直す。せっかくの良い天気だし、今からどこか出かけないか？　二人で」
    lian "我不擅长拐弯抹角的说话！实际上，难得的好天气，现在去哪里玩玩吧？两个人一起"

    # 心爱 「ぶえ！　それって要はデートって事ですかぁ！？いんですかぁ！？　そんな事してぇ…。さっきの事否が応でも意識しちゃいますよ私ィ～！」
    ai "哇欸！那就是约会吗！？是吗！？做了那样的事…刚才的事情我会变得更在意了哦！"

    # 莲 「それについても整理すべきだと思ってるしな…とりあえずどっかいこうぜ。行きたいところとかない？」
    lian "关于那个事情我也觉得应该整理一下……总之先去哪里吧。有想去的地方吗？"

    # 心爱 「じゃぁ私、ラウワン行きたい」
    # 参考资料：https://ja.wikipedia.org/wiki/ラウンドワン
    ai "那我想去朗玩（ラウワン）（L:ラウワン是一个保龄球娱乐公司，总部在大阪府大阪市中央区，国内现在也有两家，分别在广州和深圳）"

    # 莲 「ボウリング場かよ。こだわりすぎだろ、ボーリングっていう文字列に」
    lian "保龄球馆啊。你太执着了吧，对保龄球这个词"

    # 心爱 「もしくはハワイ。出雲大社とソープファクトリーに行きたい」
    # 参考资料：https://ja.wikipedia.org/wiki/出雲大社
    # 参考资料：https://www.nakutemo-hawaii.com/northshore-soap-factory/
    ai "或者是夏威夷。我想去出云大社和肥皂工厂（L:出云大社是位于日本岛根县出云市大社町的神社，以“结良缘”闻名，这里是供奉结缘之神大国主命；肥皂工厂指夏威夷的北岸肥皂厂（North Shore Soap Factory））"

    # 莲 「それは夏休みな」
    lian "那是暑假的事情吧"

    # 心爱 「はーい…え？連れてってくれるのかよ！ワイハーやでワイハー！」&不是很确定
    ai "嗯…诶？能带我去吗！夏威夷！威夷！"

    # 莲 「真冬が来るつったらいんじゃないか？」&也不是很确定
    lian "记得你不是说真冬也要去吗？"

    # 心爱 「わーい♪　じゃぁ新しい水着買っとくー♪」
    ai "哇♪那就买新泳衣吧♪"

    # 店长 「そんなあっさり決める人初めて見ましたよ。私も一つ、みんなに旅行でも提案してみたくなりました」
    dinerowner "第一次看到这么爽快地决定的人。我也想给大家提一个旅行的建议呢"

    # nil 「と、言う事で、本日の予定は心愛ちゃんとのデートに決まりまんた。」
    "于是，今天就决定和心爱酱约会啦"

    # 心爱 「えへ…ねぇ、蓮くん。手、繋いでもい？」
    ai "嘿嘿嘿……呐，莲君，我可以牵你的手吗？"

    # 莲 「ん？　おう。何年ぶりだろうな…」
    lian "嗯？啊，已经几年没牵了吧…"

    # 心爱 「１２年と三ヶ月と六日ぶりかな」
    ai "十二年零三个月零六天了吧"

    # 莲 「なんで覚えてるんだよ」
    lian "你为什么还记得呢？"

    # 心爱 「蓮くんにしてもらった事なら何でも覚えているよ！」
    ai "只要是莲君的事情我都会记得的！"

    # 莲 「じゃぁ試しに、3年前の今日、俺はお前に何をした？」
    lian "那么，来试试康，3年前的今天，我对你做了什么？"

    # 心爱 「自転車で轢いた」
    ai "骑自行车撞了我"

    # 莲 「ごめん」
    lian "对不起"

    # nil 「と、いうことで、心愛ちゃんとのデートの一部始終をダイジェストでお送りいたします。」
    "所以，下面是我和心爱约会的整个过程的摘要"

    # scene02 场景1 【雾叶小店】 结束
    # ------------------------------
    # scene02 场景2 【和心爱的约会】 开始

    # 场景切换
    # 地点：保龄球馆
    # 人物：莲君 心爱
    # BGM：比较活跃

    # nil 「ボウリング場にて。」
    "在保龄球场"

    # 心爱从右侧一点点向左挪一点点
    # L:“淦，回头又得写ATL语句了”

    # 心爱 「ふん…ふぬ！」
    ai "咕呜... 咕奴奴奴奴!"

    # 莲 「おいおい無理するなよ、何で15ポンドのボールを選ぶんだ」
    lian "喂喂，不要勉强啊，为什么要选15磅的球啊喂？（L:15磅大概是6803克的亚子~）"

    # 心爱从右侧一点点又向左挪了一点点，到接近中间的位置
    # L:“淦，ATL语句了疯狂加增ing...”

    # 心爱 「重い方が！　威力も高いじゃないですか！　とおもって！」
    ai "重点的那个！威力自然也高一些吧！我是怎么觉得的!"

    # 莲 「自分の体重の１０％っていうセオリーがあってな」
    lian "理论上用自己体重10%的球会比较好哦~"

    # 心爱从向左上移动了一点，到中间的位置
    # L:“啊啊啊我不要写ATL啊”

    # 心爱 「なるほど。じゃぁおいらは10ポンドあたりがちょうどいってことだね」
    ai "原来如此。那这么说来，以我的体重用10磅（4535克左右）的就刚刚好呢!"

    # 莲 「ちなみにそれ、自分の体重をこっそり発表してるようなもんだけどな」
    lian "话说啊，你这样好像悄悄地发表了自己的体重哦~（L:帮大家算了一下，心爱酱大概是91斤呢）"

    # 心爱 「ぐ…」
    ai "唔…"

    # 场景切换
    # 朗玩（保龄球场）->购物中心
    # 人物：心爱 莲

    # nil 「ショッピングセンターにて。」
    "在购物中心"

    # 心爱 「ほらほらほら！　蓮くんこっちこっち！こがロッキーマウンテンチョコレートファクトリーだよ！キャラメルアップルの原産地！」
    ai "快看快看快看! 莲君这边这边！这个是来自洛基山巧克力工厂的！奶糖苹果的原产地！"

    # 莲 「このやる気の無いクマのぬいぐるみはなんだ」
    lian "这个康起来很没劲的熊玩偶是个啥？"

    # 心爱 「私以前、この中の人のバイトやったことあるよ」
    ai "我啊，以前在这个玩偶里面做过兼职哦~"

    # 莲 「椅子にだらーって座ってるだけ？」
    lian "一定是懒洋洋地坐在椅子上的那种吧"

    # 心爱 「そそ。で、たまに子供が油断しておなかとか触ってくるから、そしたら立ち上がる」
    ai "对对，有时候我就突然站起来，吓唬那些摸我肚子的小孩"

    # 莲 「泣くぞ子供」
    lian "孩子要哭了啊"

    # 熊（クマ） 「！！！」
    bear "！！！"

    # 心爱 「ぶえ立ち上がったよお」
    ai "呜欸——突然站起来了啊！"

    # 莲 「知ってやったんじゃねぇのかよ」
    lian "你不是知道的吗？"

    # 场景切换
    # 购物中心->冰淇淋店
    # 人物：心爱 莲
    # BGM不变

    # nil 「アイスクリーム屋にて」
    "在冰淇淋店"

    # 莲 「ほら、お前の大好きなコールドストーンだぞ」
    # コール:call
    # 参考视频：https://www.bilibili.com/video/av711502425/
    lian "你看，是你最喜欢的冷石冰淇淋（L:就是在冷石板上炒出来的冰淇淋，简单来说，就是“炒冰淇淋”）"

    # 心爱 「へ？　マジで奢ってくれるの？」
    ai "欸？你真的要请客吗？"

    # 莲 「こで良いなら」
    lian "如果可以的话"

    # 心爱 「わーい♪　あ、ねぇねぇ、奢ってくれるついでに、もう一個わがま聞いて貰ってもい？」
    ai "哇~咿~♪ 哦! 呐呐，请客的事情谢谢啦，能不能顺便再问个任性的问题呢?"

    # 莲 「なんなりとどうぞお嬢様」
    lian "大小姐，您请"

    # 心爱 「このお店ね、店員さんに歌を頼むと、歌ってくれるサービスがあるんだ」
    ai "这家店呢，只要拜托店员唱歌，就会有唱歌的服务哦"

    # 莲 「あ、あるな。誕生日とか祝ってくれるやつな」
    lian "啊，对。就是庆祝生日的那种对吧"

    # 心爱 「で、せっかくなので、蓮くんにも一緒に歌って欲しいなーなんて思っちゃったり」
    ai "呐，难得有机会，我就想让莲君跟我一起唱一次"

    # 莲 「まじかよ。何を歌えばいんだ」
    lian "真的吗？唱什么好呢？"

    # 心爱 「蛍の光」
    # 参考资料：https://ja.wikipedia.org/wiki/蛍の光
    # 原版：https://www.bilibili.com/video/BV1Ds411471s/
    ai "萤之光（L:这是改编自苏格兰民谣《友谊地久天长》的日本歌曲，作词者是稻垣千颖，歌名《萤之光》，语出中国成语“囊萤映雪”，在游戏目录下的“这是个啥文件夹？”我们给大家准备了歌曲的链接）"

    # 莲 「閉店ムードになるからダメだ」
    lian "因为有打烊的气氛所以不行"

    # 心爱 「じゃぁサッカー入場の時に流れるあれ」
    # 参考资料：https://zh.wikipedia.org/wiki/国际足联公平竞赛曲
    ai "那足球队入场的时候会放的那个（L:指FIFA ANTHEM（国际足联公平竞赛曲），挺好听的，近年（指18年后）被逐渐换为Living Football）"

    # 莲 「サッカーの試合みたいになっちゃうぞ」
    lian "肯定会变得像足球比赛一样哦"

    # 心爱 「パーンパーパーンパーンパーンパーパーン♪」
    ai "梆~梆梆梆~梆~梆~梆梆~梆♪（L:这个就是FIFA ANTHEM的旋律啦♪~）"

    # 场景切换
    # 冰淇淋店->寿司店
    # 人物：心爱 莲
    # BGM不变

    # nil 「寿司屋にて」
    "在寿司店"

    # 心爱 「大将、ぎょく！」
    # 参考资料：https://dictionary.goo.ne.jp/word/玉_%28ぎょく%29/
    ai "老板，寿司煎蛋！"

    # 莲 「専門的な頼み方をするんだな…」
    lian "你这要求挺专业的嘛"

    # 心爱 「ちなみに、醤油は紫と言います」
    # 参考资料：https://www.chuokai-yamagata.or.jp/s-miso/qa/soy/34.html
    ai "顺带一提，酱油叫“紫”（L:原因有三种说法，可到https://www.chuokai-yamagata.or.jp/s-miso/qa/soy/34.html查阅）"

    # 场景切换
    # 寿司店->游戏中心
    # 人物：心爱 莲
    # BGM不变

    # nil 「ゲームセンターにて」
    "在游戏厅"

    # 心爱 「ほらほら！　蓮くん蓮くん！　ポーズポーズ！」
    ai "呐、呐，莲君莲君！pose、pose！"

    # 莲 「プリクラなんてほぼ初めてだからわかんねぇぞ！？どうすりゃいんだよ！」
    lian "呀呀呀呀，我这是第一次拍大头贴，所以不知道该怎么办啊？！"

    # 心爱 「そんなの簡単だよ！白目向いて、舌を出して、両手でピース！」
    ai "那很简单啊！翻个白眼，伸出舌头，双手peace！"

    # 击打声、白光切入

    # 心爱 「完っ璧」
    ai "完美"

    # 莲 「…アヘ顔ダブルピースじゃねぇか！」
    lian "…这不是阿黑颜嘛！"

    # 心爱 「大事にするね。蓮くんとの初プリ」
    ai "我会好好珍惜的。和莲君的第一次约会"

    # 莲 「なおさら不服だ、撮り直しを要求する」
    lian "我不满意，要求重拍"

    # 心爱左移

    # 心爱 「やだぷー！」
    ai "才不要呢——"

    # 莲 「てめぇ写真持ってどこいきやがるつもりだ！」
    lian "你打算拿着照片去哪儿啊！"

    # 心爱左移接近屏幕左边缘！

    # 心爱 「ハンズ」
    ai "HANDS（L:指东急手创馆（TOKYU HANDS INC.）是日本一专门售卖家与DIY用品的连锁居家生活百货公司，是东急集团成员公司之一，于1976年创办）"

    # 场景切换
    # 游戏中心->HANDS
    # 人物：心爱 莲
    # BGM不变

    # nil 「ハンズにて」
    "在HANDS"

    # 莲 「ぜぇ…はぁ…やっと捕まえたぞ…」
    lian "哈啊... 哈啊... 终于抓到你了"

    # 心爱 「まさか画材売り場まで追いかけてくるとは…」
    ai "没想到会追到画材卖场…"

    # 莲 「俺の恥ずかしい写真は没収だ」
    lian "我的羞耻照片必须没收"

    # 心爱 「やーだー！　まふまふちゃんと賭けをしてたんだもんー！『君のお兄ちゃんのアヘ顔ダブピ写真を撮ったら一日私の妹になってくれるかい？』って！」
    ai "呀哒! 我和嘛呼嘛呼酱打赌了————‘如果我给你哥哥拍张阿黑颜的照片，你就做我一天妹妹’"

    # 莲 「やめろ！　真冬はわたさん！」
    lian "住手！真冬是我的！"

    # 心爱 「ならば、ピカリンジャンケンで勝負だ！」
    # 参考资料：https://www.nicovideo.jp/watch/sm17102569 （大雾！）
    ai "那么，就以皮卡林猜拳来决胜负吧！（L:皮卡林猜拳是スマイルプリキュア!里面キュアピース的经典动作）"

    # 莲 「上等！」
    lian "来吧！"

    # 心爱 「ゆくぞ！ピカピカピカリン…ジャンケン」
    ai "冲鸭! 皮卡皮卡皮卡林... 石头、剪刀"

    # 心爱 「ポン！」
    ai "布！"

    # 心爱 「かちまんた」
    ai "赢了！"

    # 莲 「畜生！　サ○エさんには負けたことないのに！」
    lian "淦哦! 我之前从来没输过的！（L:莲你和别人打什么游戏赢过吗？？）"

    # nil 「すまない真冬、一日心愛の妹になってきてくれ。」
    "对不起，真冬，请你做一天心爱的妹妹吧"

    # 视角切回真冬
    # BGM 停
    # 场景：教室
    # 人物：真冬 想瑠喵

    # 真冬 「へっくし…お兄ちゃん達が私の噂してる…」
    dong "啊嚏……欧尼酱他们在说我的事情呢…"

    # 想瑠 「ピンポイントだな…」
    liu "真是精确（的第六感）啊... ..."

    # 真冬 「まふ」
    dong "嘛呼"

    # 视角切回心爱组
    # BGM 恢复之前的
    # 场景：购物街
    # 人物：心爱 莲

    # 心爱 「スーパーカミオカンデにて」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%82%B9%E3%83%BC%E3%83%91%E3%83%BC%E3%82%AB%E3%83%9F%E3%82%AA%E3%82%AB%E3%83%B3%E3%83%87
    ai "去看超级神冈探测器吧（L:是日本东京大学在岐阜县飞驒市神冈町的神冈矿山一个深达1000米的废弃砷矿中建造的大型中微子探测器。其目标是探测质子衰变以及被设计来寻找太阳、地球大气的中微子，并观测银河系内超新星爆发）"

    # 莲 「いかねぇよ！」
    lian "不行！"

    # 心爱 「貴様は見たくはないのか…本物のチェレンコフ光を…」
    # 参考资料：https://ja.wikipedia.org/wiki/%E3%83%81%E3%82%A7%E3%83%AC%E3%83%B3%E3%82%B3%E3%83%95%E6%94%BE%E5%B0%84
    ai "你不想看吗... 真正的切连科夫辐射... "

    # 翻译君的豆知识时间！
    luckykeeper "切连科夫辐射是介质中运动的电荷速度超过该介质中光速时发出的一种以短波长为主的电磁辐射，其特征是蓝色辉光。这种辐射是1934年由苏联物理学家帕维尔·阿列克谢耶维奇·切连科夫发现的，因此以他的名字命名。1937年另两名苏联物理学家伊利亚·弗兰克和伊戈尔·塔姆成功地解释了切连科夫辐射的成因，三人因此共同获得1958年的诺贝尔物理学奖"

    # 莲 「夏休みな」
    lian "暑假吧"

    # 心爱 「つれてってくれるのかーい！」
    ai "能带我去吗？"

    # 莲 「いよ」&不大会翻呢
    # 参考资料：https://dictionary.goo.ne.jp/word/%E3%81%84%E3%82%88/
    # 参考资料：https://dictionary.goo.ne.jp/word/%E5%BC%A5_%28%E3%81%84%E3%82%84%29/#jn-15196
    # 中文参考资料：http://wenda.tianya.cn/question/0040c2ae69072d88?sort=t
    lian "就这样吧"

    # 场景切换
    # 购物街->るなちー的店
    # 人物：心爱 莲
    # BGM变 有点怪的 像RPG游戏里面的那种

    # nil 「街の片隅にある変なお店にて。・るなちーのお店」
    # 参考资料：https://seesaawiki.jp/theunusualskyblock/d/%CD%D1%B8%EC%B2%F2%C0%E2#content_1_9_27
    # 参考资料：https://seesaawiki.jp/theunusualskyblock/d/%c6%c3%bc%ec%a5%e2%a5%f3%a5%b9%a5%bf%a1%bc#
    # 整合包参考资料：https://skyblock.jp
    "在街道角落里的奇怪的店・るなちー的店"

    # 是W的豆知识时间哟~
    luckykeeper "这回是WorldlineChanger的豆知识时间哦！るなちー是the unusual skyblock的mc整合包里面的狂气之瞳的爱称，攻击带有多种debuff，不是很好对付"

    # 翻译君的豆知识时间哒~
    # 参考资料：https://twitter.com/lunachi_bot
    luckykeeper "接着是L的豆知识时间，最开始我和W都是向这mc的方向想的，不过问了10多个人都不知道，于是换了个思路到twitter搜了一下，发现本作的前作月宮瑠那的宣传账号用的是这个名字るなちー_bot（@Lunachi_bot）从时间上面考虑，我个人认为这一说更加合理。所以，你作作者到底是从哪儿搞来的阴间梗啊？！"

    # 心爱 「むー……むー……むー……」
    ai "嗯↓——嗯↑——唔姆——"

    # 莲 「何をそんな真剣に悩んでいるんだ」
    lian "你那么认真地烦恼，是有什么事情呢？"

    # 心爱 「もうすぐ二歳になる従兄弟がいるんだけどね。この『雪崩式ブレーンバスター』と『マルセイユルーレット』のどっちをあげたら喜ぶかなって」
    # 参考资料：https://ja.wikipedia.org/wiki/ブレーンバスター
    # 参考资料：https://ja.wikipedia.org/wiki/マルセイユ・ルーレット
    ai "我有一个快两岁的表弟。我要给他『Brainbuster』（L:职业摔跤技法，WWE禁止）和『马赛回旋』（L:Marseille roulette，是一种足球比赛中进攻队员摆脱对方防守的带球过人技巧）中的哪一个才好呢"

    # 莲 「もうちょっと微笑ましいモノにしなさい。そもそも売り物じゃないだろそれは…」
    lian "笑话多来点多来点，这本来就不是卖的东西嘛"

    # 心爱 「悩んだ結果、『バスターエンドラン』にしまんた」
    ai "烦恼的结果是，『Brainbuster』就是它了！"

    # 莲 「好きにしてくれ」
    lian "随你便吧"

    # 场景切换
    # るなちー的店->购物街
    # 人物：心爱 莲
    # BGM变 不是原先那个，换新的嘤文歌辽

    # nil 「街角にて」
    "在街角"

    # 心爱 「にへ…蓮くんに『中東の笛』をおごってもらいました。これで理不尽なオフサイド判定も意のまです」
    # 参考资料：https://ja.wikipedia.org/wiki/中東の笛
    ai "嘿嘿... ... 莲君请我吃了『中东之哨』（L:是一种比赛日程和裁判被认为对阿拉伯国家有利的赛事，主要是在国际体育赛事中）。这样一来，不合理的越位判罚也就顺理成章了"

    # 音效：中東の笛

    # 莲 「そこまで喜んでくれるのは嬉しいんだが、前を見て歩いておくれよ。転ぶぞ」
    lian "你这么高兴我也很高兴呢，但你还是看着前面的路吧，会跌倒的哦"

    # 心爱 「ぶえー！」
    ai "呜欸——！"

    # 画面震动

    # nil 「ビターン！」
    "啪嗒！"

    # 莲 「ほら、いわんこっちゃない」
    lian "你看，我没说错吧"

    # 心爱 「ジジ……ジジジ……」
    ai "叽叽……叽叽叽……"

    # 音效（是音效，不会循环播放的！！！）：加速的『スターチス』結月そら / 原創曲:cittan*

    # 心爱 「……」
    ai "……"

    # 莲 「……」
    lian "……（L:蚌埠住了？）"

    # 心爱 「……」
    ai "……"

    # 莲 「…チューニングがズレたのか」
    lian "…是调频错了吗？"

    # 心爱 「ありがとう、なおりまんた」
    ai "谢谢，治好了"

    # 莲 「おう。あと、何でお前の周り飛んでるの？」
    lian "喔。还有，周围为什么都在绕着你飞呢？"

    # 心爱 「私自身がアクセスポイントになっているからね」
    ai "因为我自身就是Access Point哦（L:Access Point，AP，不懂的话可以简单理解成无线路由器）"

    # 莲 「なるほど」
    lian "原来如此"

    # 原地tp

    # 心爱 「リニアモーターカーは名古屋、品川間を凡そ40分で行き来できます」
    ai "磁悬浮列车在名古屋、品川之间大约需要行驶40分钟"

    # 莲 「あれ、なんでお前色々雑になってるの？」
    lian "呀呀，为什么你的思维突然变得跳跃起来了呢？"

    # 心爱 「ほえ…？　ごしごし…はうあ！化粧乱れてるやんけ！ちょっくら直してきます！」
    ai "呜欸…？擦擦…哈呜啊！你的妆好乱啊！我来帮你改一下！"

    # 原地tp

    # 心爱 「ただいま」
    ai "我回来了"

    # 莲 「おかえり」
    lian "欢迎回来~"

    # 原地tp

    # 心爱 「蓮くん蓮くん」
    ai "莲君莲君"

    # 莲 「ん？」
    lian "嗯？"

    # 心爱 「にぎにぎ」
    ai "牵手牵手"

    # 莲 「おう」
    lian "嗯"

    # 心爱 「ぎゅー」
    ai "抱~"

    # 莲 「おう」
    lian "嗯"

    # 心爱 「ぺろぺろ」
    ai "我舔我舔"

    # 莲 「おう」
    lian "嗯"

    # 心爱 「がぶ」
    ai "嘎呜"

    # 莲 「おう」
    lian "嗯"

    # 心爱 「じー…」
    ai "盯——"

    # 莲 「なんだ、突っ込んでくれ的な目だな」
    lian "怎么啦，你这眼神真刺眼啊"

    # 心爱 「（こくこく）」
    ai "（哼哼）"

    # 莲 「カーネルおじさんの乳首を責めるのはやめてやれ。ほんのり赤くなってるじゃねぇか」
    # 参考资料：https://ja.wikipedia.org/wiki/カーネル・サンダース
    lian "不要责怪哈兰德·桑德斯叔叔（L:他是肯德基的创始人，肯德基商品的外包装的肖像画就是他的）的乳头了，不是有点发红吗（L:桑德斯在1980年6月被检测出白血病，这里“有点发红”应该是指该病症状）"

    # 心爱 「ビスケット食べたい」
    ai "饼干想恰了"

    # 场景切换
    # 购物街->岸边公园
    # 人物：心爱 莲
    # BGM变 Harmony（鸿蒙也叫这个呢）
    # 心爱 「よかぜーにさらーわれたなみだー！　ゆきーのけーっしょおーにかーわるー！」
    # 参考资料：https://www.youtube.com/watch?v=BCE0R7P-z44&list=PLAuLqe9EqzhvHO6TN5nfJ2jVTxVFJhxlJ&index=41  1分16秒
    ai "夜风中被夺走的泪水，化作雪的结晶（这句是『スターチス』里面1分16秒开始的歌词，作曲人是cittan*，本作的曲也是他作的）"

    # 心爱 「そのきーみーのよーこーがおだけはー！　なによーりもー！　まもりーたいからー！」
    ai "看着那样的你的侧脸，是我比任何都最想保护的（这首歌也被用作本作的前作里面的曲子）"

    # 心爱 「いてつーいーてしーまうせーつなーもー！　とかーしーだすーたいようのよ・お・にー！」
    ai "连冻结的眼泪都能在刹那间溶解，成为想那样的太阳"

    # 心爱 「つよーさーをもーとーめーてー！　きみだーけのぼくになるーと」
    ai "追求着力量，渴望成为只属于——"

    # 莲 「ちーかうー」
    lian "你的我"

    # 心爱 「フィニッシュをとられたぁあああああ！」
    ai "结尾被抢去了啊——"

    # 莲 「ふはは」
    lian "啊哈哈"

    # 心爱 「しかし、素敵な歌詞だよね。私も君だけの僕になるとか言われたい」
    ai "但是，这是一首很棒的歌词呢。我也想被说成是只属于你的我"

    # 莲 「君だけの俺になってやろうか？」
    lian "我要成为只属于你的我吗？"

    # 心爱 「へ？」
    ai "嗯？"

    # 莲 「なーんつってーな」
    lian "怎么了？"

    # 心爱 「むぅ…さっきの事思い出しちゃうじゃんかー！」
    ai "呜…刚才的事不是想起来了吗！（L:说的是心爱恰了冰淇淋时候的事情哦）"

    # 莲 「そういうフリかと思ったけど…」
    lian "我以为你是装成那样的…"

    # 心爱 「ちょっと…意識してたかも？」
    ai "可能有点……意识到了呢？"

    # nil 「そろそろ頃合いか…。」
    "差不多是时候了吧…"

    # nil 「ビルの隙間から顔を覗かせる太陽が、世界をオレンジ色に染める。」
    "从大楼的缝隙中露出脸的太阳，将世界染成了橙色"

    # nil 「隣を歩く制服姿の心愛の頬も、心なしか温かい朱色に染まっているように見える。」
    "穿着制服走在身旁的心爱的脸颊，似乎也被一种温暖的朱红色染红了"

    # nil 「小さな公園のベンチに並んで腰掛ける。心愛の手には、スカートの中より取り出したキャラメルアップルが握られている。」
    "并排坐在小公园的长凳上。心爱的手上握着从裙子里面取出来的奶糖苹果"

    # 莲 「さっきの事について、ちょっと話そうか」
    lian "关于刚才的事，我们来谈谈吧"

    # 心爱 「あはーまじかぁ…う、うん…大丈夫。心の準備…する…」
    ai "啊，真的吗…嗯、嗯…没关系，我会做好心理准备的……"

    # 莲 「別に、忘れてもいが…」
    lian "没什么，把它忘了吧…"

    # 心爱 「あ、うんうん！　蓮くんがしたいならそう…しても、私は構わないよ！何も無かった！　綺麗さっぱり！」
    ai "啊，嗯嗯! 如果莲君这么想的话... ... 我也没关系的! 刚才什么都没有发生! 忘得一干二净!"

    # nil 「そっと、心愛が握る手に力を込める。心愛は目を泳がせる。」
    "轻轻地，心爱使劲握紧手。眼神不断游动着"

    # 莲 「お前の癖だよな。不本意な打算を選ぶ時、手を握って目線をそらすの」
    lian "这是你的习惯吧。在遇到不愿意的选择的时候，就握着手移开视线"

    # 心爱 「はうっ」
    ai "哈呜！"

    # 莲 「しかも、今日一日手を繋いでデートしちまってんだよな…。これを忘れるっつーのも、少し寂しいとは思わないか？」
    lian "而且，今天一整天都是牵着手约会的吧…忘记这个，不觉得有点寂寞吗？"

    # 心爱 「確かにそうだけどさー…うーん、ねぇ、正直、どう思った？」
    ai "确实是这样，但是……嗯，说实话，你是怎么想的？"

    # 莲 「何が？」
    lian "关于什么？"

    # 心爱 「私に…その…強引に…き…きす…」
    ai "我……那个…强行…k…kiss……"

    # 莲 「正直、驚いたね」
    lian "老实说，我吓了一跳"

    # 心爱 「あう」
    ai "哈呜"

    # 莲 「俺の中で、心愛はその辺苦手っつーか、ただの幼馴染み的な感じで俺に接してるだけだと思ってたしな」
    lian "在我心中，心爱只是不擅长这个，或者只是以一种青梅竹马的方式对待我"

    # 心爱 「に、苦手ってわけじゃないんだよ！？　単に、経験がないだけでやり方とかわかんないし…その…私は…ただの幼馴染みだから…」
    ai "我并不是不擅长啊！？只是因为没有经验所以不知道怎么做…那个…我…只是个青梅竹马而已…"

    # 莲 「でもよ、実の妹に俺は今朝、耳を舐められたんだが」
    lian "但是，我今天早上被亲妹妹舔了耳朵"

    # 心爱 「それは、真冬ちゃんと蓮君が特別親しいからで…」
    ai "那是因为真冬和莲君特别亲近……"

    # 莲 「確かに俺と真冬は、特別親しいな。だが、それは真冬に限った話ではない」
    lian "确实，我和真冬是特别亲近的。但是，这并不局限于真冬"

    # 莲 「俺は…お前とも特別親しいと思っているんだが…それは勘違いか？」
    lian "我... ... 我认为我和你特别亲近... ... 这是误会吗"

    # 心爱 「勘違いではないとおもう！　実際、蓮くんと真冬ちゃんの事は大好きだし、私も家族同然だと思ってる！」
    ai "我想你没有误会！实际上我很喜欢莲和真冬，我觉得我们像家人一样！"

    # 莲 「だろ？　だったら、別に俺がお前にキスをされたとて、驚いたとはいえ、関係で不思議に感じる事は想わない」
    lian "对吧？那么我认为被你亲吻并不奇怪，尽管我对这种关系感到惊讶"

    # 莲 「もっとも。これは俺の価値観であって、一般常識と照らし合わせたら違ってくるが…」
    lian "当然。这是我的价值观，和一般常识对照的话可能会不同……"

    # 心爱 「ていうか、私に常識という概念は似合わないよね」
    ai "话说，常识这个概念不适合我吧"

    # 莲 「自覚はあったのか」
    lian "你原来是有自觉的吗？"

    # 心爱 「でも、こんな私を受け入れてくれている二人には、本当に感謝してるんだよ」
    ai "但是，对于接受这样的我的两个人，真的非常感谢"

    # 莲 「受け入れるもなにも…物心ついた頃からお前がいたからな…。俺たちにとって普通の事だ」
    lian "接受也好什么也好…从懂事的时候开始就有你在……这对我们来说是很普通的事情"

    # 心爱 「じゃぁ…その…うーん…でも…」
    ai "那么…那个……嗯…但是…"

    # 莲 「今日一日手を繋いでいろんな所言って、お前のわがまにも付き合ったんだ。最後までわがまに付き合うつもりでいるよ、俺は」
    lian "今天一整天都牵着你的手，去了很多地方，陪着你任性。我会一直陪你到最后的"

    # 心爱 「私にキスされて、嫌じゃなかった…？」
    ai "被我吻了，你不讨厌吗…？"

    # 莲 「なるわけないだろ。普通に嬉しかったぞ」
    lian "怎么可能呢，我只是普通的高兴而已"

    # 心爱 「優しいよね、本当に。だからこそ、余計に不安になるよ。本心なのか、優しさなのか…って」
    ai "真的很温柔呢。正因为如此，我才更加不安。你到底是真心，还是出于温柔……"

    # 莲 「俺自身の趣味とでも言っておこうか。お前のワガマに付き合う事がな」&微调翻译以符合中文语境
    lian "我可以说出我自己的想法吗？我要和你任性的交往"

    # 心爱 「じゃあ…もう少し、わがましてもい？」
    ai "那么... 我可以再自私一点吗? "

    # 莲 「少しじゃなくてもどうぞ」
    lian "就算不是一点也请"

    # 心爱 「チューして…い？」
    ai "亲我吗？"

    # 莲 「むしろ、俺でいのか？」
    lian "不如说，我可以吗？"

    # 心爱 「良くなければ、こんな事聞かない」
    ai "不好的话，就不会问这种事哦"

    # 莲 「なら…」
    lian "那么…"

    # 心爱 「ん…っ！？」
    ai "嗯……？！"

    # 莲 「なら…」
    lian "那么…"

    # nil 「そっと心愛の唇に自分の唇を重ねる。」
    "轻轻地将自己的嘴唇重叠在心爱的嘴唇上"

    # nil 突然の事に心愛は驚いて、肩をこわばらせる。空いた手で、心愛の肩を撫でると、徐々にリラックスしていくのがわかる。
    "突如其来的一吻让心爱吃了一惊，肩膀僵硬起来。用双手抚摸心爱的肩膀，她的肩膀慢慢放松"

    # 心爱 「ん…ちゅぅ…ぷはぁ…ふ…ふいうち…」
    ai "嗯…呜…哈哈…嗯…突然间……"

    # 莲 「不意打ちは不意打ちでかえさんとだろ？」
    lian "不突然的话怎么能叫出其不意呢？"

    # 心爱 「ば、ばかー！　そんな事されたら…そんな事されたらー！一回で満足できなくなっちゃうじゃんかー！」
    ai "啊，笨蛋！如果被那样做的话……被那样做的话！一次就不能满足了吧！"

    # 莲 「言ったはずだ。最後まで付き合うと」
    lian "我说过的吧，要陪你到最后"

    # 心爱 「んむっ…んぅっ…」
    ai "呼嗯……嗯……"

    # nil 「間髪入れずに唇を奪う」
    "马上夺走她的嘴唇"

    # 心爱 「んふ…ちゅぅ…んっ」
    ai "嗯……嗯…"

    # nil 「心愛はゆっくりと目を閉じて、俺が預けた体重を受け止めた。」
    "心爱慢慢闭上眼睛，承受着我托付给她的体重"

    # 心爱 「ちゅぅ…っ…はぁ…はぁ…はぅ…」
    ai "嗯呜……哈…哈…哈……"

    # 莲 「色々言いたいことはあるだろうがな。とりあえず、お互いが幸せならそれでいんじゃないか？」
    lian "我知道你有很多话要说，总之，如果我们彼此都幸福，那不是很好吗"

    # nil 「ぎゅっ」
    "被紧紧地抓住了"

    # 莲 「ん？」
    lian "嗯？"

    # 心爱 「……」
    ai "……"

    # nil 「立ち上がった俺の制服の裾を、心愛はぎゅっと掴んで、その手に握られていたキャラメルアップルを俺に差し出した。」
    "心爱紧紧地抓住了我制服的下摆，把手中握着的奶糖苹果递给了我"

    # 心爱 「…ありがとう、蓮くん…♪」
    ai "谢谢你，莲君…♪"

    # 莲 「どういたしまして。好きだよ、心愛」
    lian "不客气。我喜欢你，心爱"

    # 心爱 「えへ、私も…大好き♪　ちゅー」
    ai "嘿嘿，我也是... 最喜欢你了♪啾——"

    # nil 「初めて食うキャラメルリンゴの味は、何故か思ったより甘酸っぱかった。」
    "第一次品尝奶糖苹果的味道，不知为何比想象的要更加酸甜"

    # nil 「……」
    "……"

    # 心爱 「じー…」
    ai "盯——"

    # 莲 「なんだよその目は。くれたんじゃないのか」
    lian "你的眼睛怎么了? （这个奶糖苹果）不是给我的吗"

    # 心爱 「いや、わかっちゃいるんだけどね…わかっちゃいるんだけど…欲望が…！」
    ai "不，我知道…我知道的…但是我的欲望…！"

    # 心爱 「んむぅっ…んっ…んっ…」
    ai "嗯姆...... 嗯...... 嗯......"

    # 莲 「これでご満足頂けたかな？」
    lian "这样您就满意了吧？"

    # 心爱 「ぷはぁ…ぜぇ…はぁ…次やったら舌入れるからな…」&稍微调整一下吧
    ai "噗哈…哈啊……哈啊…下次再做的话把整个苹果放进去吧……"

    # 莲 「試してみるか？」
    lian "要来试试吗？"

    # 心爱 「っ…！　は、はずぃよー…」
    ai "啊...! 怎、怎么可能嘛..."

    # 莲 「よしよし」
    lian "好啦好啦"

    # 心爱 「はう」
    ai "哈呜~"

    # nil 「……」
    "……"

    # scene02 场景2 【和心爱的约会】 结束！

    # scene02 翻译完成！

    # 过场：心爱

    # scene02 结束，跳转到scene03
    jump scene03

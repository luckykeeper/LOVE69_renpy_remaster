# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene20 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：
# 版本 NightBuild "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年6月24日

# 当前流程：All Done!

label scene20:
    # scene20 开始
    # 可变标题
    # Scene 序号
    $ sceneNo =  " scene20"
    # 存档名称和 Scene 大标题
    $ sceneName = " 里昂线 考验后的幸福"
    # 小场景的名称
    $ partName = " 【心跳不已的第一次】"
    $ changeTitleName()
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)

    # scene20 场景1 【心跳不已的第一次】 开始
    $ quick_menu = True

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # 里昂 「はぁ…んぅ…」
    voice "voice/リオン/ron_a1_0467.ogg"
    lion リオン_私服_基本_微笑み "啊……嗯……"

    # nil 「完全に、スイッチの切り替わってしまったリオンは、顔を真っ赤にしたま、くてっと俺の身体に身を預けている。」
    # "完全切换了开关的里昂满脸变得通红，一直把身体靠在我的怀里"
    "完全打开了开关的里昂满脸变得通红，一直把身体靠在我的怀里"

    # nil 「ラブホテルなんざ初めて入ったが、入り口のなんとなく雰囲気よさげな部屋のボタンを押す。」
    "虽然是第一次进入情人旅馆，但总觉得入口的气氛很好，按下了预订房间的按钮"

    # nil 「機械から吐き出された鍵を掴み、そのま、リオンの手を引いてエレベーターに乗り込んだ。」
    "抓住从机器里吐出的钥匙，然后拉着里昂的手上了电梯"

    # nil 「カシャーン。　ゆっくりとエレベーターのドアが閉まる。」
    "咔嚓，电梯门慢慢关上"

    # nil 「ぎゅっ」
    "啾"

    # nil 「直後、リオンがすがるように抱きついて来た。」
    "紧接着，里昂紧紧抱住了我"

    # 里昂 「きす…きすぅ…ちゅぅ…んぅ…」
    voice "voice/リオン/ron_a1_0468.ogg"
    lion リオン_私服_基本_微笑み_1 "Kiss……Kiss……嗯……啾……嗯……"

    # 里昂 「んぅ…ちゅぅ…はぁう…ちゅぅ…」
    voice "voice/リオン/ron_a1_0469.ogg"
    lion リオン_私服_基本_キス_1 "嗯……啾……哈……啾……嗯……"

    # nil 「エレベーターの壁に押しつけられるようにして、リオンに唇を塞がれる。」
    "压在电梯的墙壁上，堵住里昂的嘴唇"

    # 里昂 「は…はぁ…んぅ…ちゅぅ…」
    voice "voice/リオン/ron_a1_0470.ogg"
    lion リオン_私服_基本_キス_1 "哈……哈啊……嗯……啾……"

    # nil 「抱き合いながら、お互いの背中をなで回す。その間も、口と口はついばむように触れあわさせる。」
    "互相拥抱着，抚摸着彼此的后背。在这期间，嘴对嘴地互相啄食"

    # nil 「まだ、俺はリオンをリードしなければならない。という一心で、理性を保てはいるが、」
    "现在，我必须来主导，这样的想法使我还保持着理性"

    # nil 「このまではいつその理性を溶かされるかすらわからない。」
    "在这之上甚至不知道什么时候那份理性会被溶解"

    # 里昂 「んぅ、ちゅぅ…んふ…ちゅぅ…はぁ…はぁ…」
    voice "voice/リオン/ron_a1_0471.ogg"
    lion リオン_私服_基本_嬉しい_1 "嗯、啾……嗯……啾……哈啊……哈啊……"

    # nil 「エレベーターが止まり、ゆっくりとドアが開く。」
    "电梯停了下来，门慢慢打开"

    # 里昂 「ん…」
    voice "voice/リオン/ron_a1_0472.ogg"
    lion リオン_私服_基本_微笑み_1 "嗯……"

    # nil 「リオンは俺の指先を掴んで、もう片方の手の指先を唇に運んだ。」
    "里昂抓住我的指尖，把那只手的指尖放到嘴唇上"

    # nil 「鉄製の厚い扉の前にたどり着く。鍵の番号と同じ番号が描かれたパネルが光を放っている。」
    "来到厚厚的铁门前，和钥匙号码一样的面板闪着光"

    # nil 「俺は、鍵を差し込んで、サムターンを回して鍵を開ける。」
    "我把钥匙插进去，转动开锁"

    # 场景切换到房间
    image bg ホテル = "images/bg/ホテル.png"
    scene ホテル at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「ドアを開けて、リオンを招き入れる。」
    "打开门，带里昂进来"

    # nil 「が、そこで今度は俺から不意打ちでキス。」
    "这次是我突然袭击的吻"

    # 里昂 「んぅ…ぁう…ちゅぅ、んぅ…」
    show リオン_私服_基本_キス_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0473.ogg"
    lion リオン_私服_基本_キス_1 "嗯……啊……啾……嗯……"

    # 里昂 「は、んぅ…ちゅ、んぅ、ちゅっ…」
    show リオン_私服_基本_嬉しい_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0474.ogg"
    lion リオン_私服_基本_嬉しい_1 "哈……嗯……嗯……啾"
    hide リオン_私服_基本_キス_1

    # nil 「エレベーターの時と同じように、鉄の扉を背にして、抱き合いながらキス。」
    "就像在电梯时一样，背对着铁门，互相拥抱着亲吻"

    # nil 「キスをしながら、ドアノブを掴み、ゆっくりと部屋のドアを閉じる。」
    "一边接吻，一边抓住门把手，慢慢地关上房间的门"

    # nil 「ガチャリとオートロックが施錠され、この空間が密室となった。」
    "咔嚓一声，自动锁被锁上了，这个空间成为了密室"

    # 里昂 「ぷは…ぁ…えへ…」
    show リオン_私服_基本_にっこり_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0475.ogg"
    lion リオン_私服_基本_にっこり_1 "呼…啊…嘿嘿…"
    hide リオン_私服_基本_嬉しい_1

    # nil 「ぎゅーっとリオンが一度しがみついてから、そっと身体から離れる。」
    # "紧紧地抱住里昂，然后轻轻地离开身体"
    "紧紧地抱了一下里昂，然后轻轻地离开她的怀抱"

    # nil 「靴を脱いで、部屋にあがって、エアコンの設定温度を25度に下げた。」
    "脱掉鞋子，走进房间，把空调温度调到25摄氏度"

    # 莲 「うお…なんか雰囲気あるな…」
    lian "嗯……看起来很有气氛啊…"

    # 里昂 「そうだね…私こんな本格的な間接照明初めて見たよ…」
    show リオン_私服_基本_微笑み_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0476.ogg"
    # lion リオン_私服_基本_微笑み_1 "是啊…我第一次看到这种真正的间接照明…（L:间接照明很多人应该都知道，不知道的请问度娘）"
    if persistent.luckykeeperSay == "shutup":
        lion リオン_私服_基本_微笑み_1 "是啊…我第一次看到这种真正的间接照明…"
    else:
        lion リオン_私服_基本_微笑み_1 "是啊…我第一次看到这种真正的间接照明…（L:间接照明很多人应该都知道，不知道的请问度娘）"

    hide リオン_私服_基本_にっこり_1

    # nil 「手を繋ぎながら、天井にはお星様のようなラメのちりばめられた部屋の中を見渡す。」
    "手牵着手，环顾着天花板着镶满了金银般星星的房间"

    # nil 「ダブルベッドが部屋の中央に配置されていて、明らかに俺の部屋のものよりフカフカだ。」
    "双人床被布置在房间的中央，显然比我房间的那个还要柔软"

    # 里昂 「よいしょ…おじゃましまーす」
    show リオン_私服_基本_嬉しい at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0477.ogg"
    lion リオン_私服_基本_嬉しい "嘿咻……打扰了"
    hide リオン_私服_基本_微笑み_1

    # nil 「リオンも靴を脱いで、ちょこんと部屋に上がった。」
    "里昂也脱了鞋，一溜烟地进了房间"

    # nil 「さっきより、少しは落ち着いた様子のリオンは、興味津々で部屋の中を見渡している。」
    "比刚才稍微平静了一点的里昂，兴致勃勃地环视着房间"

    # 莲 「向こうにはこういうホテルはないのか？」
    lian "那边没有这样的旅馆吗？"

    # 里昂 「それが無いのだよー。大体は、格安のモーテルでシミのついた布団で、忘れたくなるような夜を過ごすんだよ」
    show リオン_私服_基本_悲しい2 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0478.ogg"
    lion リオン_私服_基本_悲しい2 "没有啊。一般来说，我都会在便宜的汽车旅馆里，用沾有污点的被子，度过让人想忘却的夜晚"
    hide リオン_私服_基本_嬉しい

    # 莲 「…経験あるのか？」
    lian "…有经验吗？"

    # 里昂 「さぁーどうでしょう！…にへ、なーいよ♪　男の人とチューするのも、これがはじめてだよ」
    show リオン_私服_基本_ニタァ at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0479.ogg"
    lion リオン_私服_基本_ニタァ "那么，怎么样呢！…欸嘿嘿，没有哦♪跟男人亲吻也是，这是第一次哦"
    hide リオン_私服_基本_悲しい2

    # 莲 「そうか、ならよかった」
    lian "是吗，那就好"

    # 里昂 「嫉妬しちゃった…？　んー？」
    voice "voice/リオン/ron_a1_0480.ogg"
    lion リオン_私服_基本_ニタァ "嫉妒了…？嗯？"

    # 莲 「ちょっとな」
    lian "有点"

    # nil 「リオンは悪戯っぽく、微笑んで、部屋の奥へと進んでいった。」
    "里昂调皮地微笑着，向房间深处走去"

    # nil 「ちょっとお値段は高かったが、その分居心地は良さそうだ。」
    "虽然价格有点贵，但是感觉还是很舒服的"

    # 里昂 「窓あるよ？　カーテンあける？」
    show リオン_私服_基本_にっこり at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0481.ogg"
    lion リオン_私服_基本_にっこり "有窗户吗？要拉开窗帘嘛？"
    hide リオン_私服_基本_ニタァ

    # 莲 「恥ずかしいよ！」
    lian "太害羞了！"

    # 里昂 「七階だし夜だからいじゃんかよー。夜景みたいなー」
    show リオン_私服_基本_ジト目 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0482.ogg"
    lion リオン_私服_基本_ジト目 "这是在七楼，现在又是晚上，有什么不好的嘛，想看看夜景嘛"
    hide リオン_私服_基本_にっこり

    # nil 「そう言いながら、リオンは部屋のカーテンを開いた。」
    "这样说着，里昂打开了房间的窗帘"

    # 里昂 「わー…！」
    show リオン_私服_基本_驚き_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0483.ogg"
    lion リオン_私服_基本_驚き_1 "哇——…！"
    hide リオン_私服_基本_ジト目

    # nil 「確かに夜景は綺麗だった。リオンが夜景に見とれているうちに、俺はこっそりバスルームのお湯を張るスイッチを押す。」
    # "确夜景确实很美，趁着里昂被夜景迷住的时候，我悄悄地按下了浴室热水的开关（L:我没看到夜景捏，这是原作懒得画差分，绝对不是我忘换背景了哦~）"
    if persistent.luckykeeperSay == "shutup":
        # "确夜景确实很美，趁着里昂被夜景迷住的时候，我悄悄地按下了浴室热水的开关（L:我没看到夜景捏，这是原作懒得画差分，绝对不是我忘换背景了哦~）"
        "确实是很美的夜景，趁着里昂被夜景迷住的时候，我悄悄地按下了浴室热水的开关"
    else:
        "确实是很美的夜景，趁着里昂被夜景迷住的时候，我悄悄地按下了浴室热水的开关（L:我没看到夜景捏，这是原作懒得画差分，绝对不是我忘换背景了哦~）"

    # 里昂 「あれ？　蓮くん？」
    voice "voice/リオン/ron_a1_0484.ogg"
    lion リオン_私服_基本_驚き_1 "啊咧？莲君？"

    # 莲 「風呂入れてる。あと５分もすりゃ入れるようになるぞ」
    lian "去洗澡吧，再过５分钟就可以去洗了"

    # 里昂 「むー…えいっ」
    show リオン_私服_基本_ジト目 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0485.ogg"
    lion リオン_私服_基本_ジト目 "嗯——嘿"
    hide リオン_私服_基本_驚き_1

    # 莲 「うおっ」
    lian "喔哦"

    # nil 「ぼふっ」
    "嗒"

    # nil 「リオンが飛びついてきて、俺をベッドへと押し倒す。」
    "里昂扑上来，把我推倒在床上"

    # 莲 「押し倒されました」
    lian "被推倒了"

    # 里昂 「ね…ちゅーしてい…？」
    show リオン_私服_基本_嬉しい_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0486.ogg"
    lion リオン_私服_基本_嬉しい_1 "呐……来啾——好吗？"
    hide リオン_私服_基本_ジト目

    # 莲 「ん…」
    lian "嗯…"

    # 里昂 「…んぅ…ちゅぅ…」
    show リオン_私服_基本_にっこり_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0487.ogg"
    lion リオン_私服_基本_にっこり_1 "……嗯……啾……"
    hide リオン_私服_基本_嬉しい_1

    # nil 「ベッドの上で、リオンと重なり合いながら、キス。」
    # "在床上，与里昂重叠、接吻"
    "在床上，与里昂身体交织、接吻"

    # 里昂 「ん、ちゅぅ…ちゅっ…ん…舌だして…」
    show リオン_私服_基本_嬉しい_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0488.ogg"
    lion リオン_私服_基本_嬉しい_1 "嗯，呜……嗯…舌头伸出来……"
    hide リオン_私服_基本_にっこり_1

    # 里昂 「ちゅ、ん、んぅ…ちゅぅ…れる…ちゅぷっ…」
    show リオン_私服_基本_微笑み_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0489.ogg"
    lion リオン_私服_基本_微笑み_1 "啾、嗯、嗯……啾……嗯……啾……"
    hide リオン_私服_基本_嬉しい_1

    # 里昂 「ぷは…んぅ…ちゅぅ、んっ…ちゅ…」
    show リオン_私服_基本_にっこり_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0490.ogg"
    lion リオン_私服_基本_にっこり_1 "呼…嗯…嗯……嗯…啾……"
    hide リオン_私服_基本_微笑み_1

    # nil 「リオンの指示通りに、舌を口から出すと、それをリオンは、自らの舌で絡め取ってくる。」
    "按照里昂的指示，从嘴里伸出舌头，里昂用舌头把我的舌头缠住"

    # 里昂 「ちゅぅ…んぅ、…れる…ちゅぅ…んっ…はぁ…はぁ…」
    show リオン_私服_基本_嬉しい_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0491.ogg"
    lion リオン_私服_基本_嬉しい_1 "呜…嗯……嗯……呜…嗯…哈…"
    hide リオン_私服_基本_にっこり_1

    # 莲 「今度はリオンな…」
    lian "这次到里昂了…"

    # 里昂 「はぃ…あ…ぅ…んぅんっ、はぅ…んっ」.
    show リオン_私服_基本_微笑み_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0492.ogg"
    lion リオン_私服_基本_微笑み_1 "哈…啊…嗯…嗯，哈…嗯"
    hide リオン_私服_基本_嬉しい_1

    # 里昂 「ゃ、ぁぅ…ンっ…ん…ん、ひぅ…んっ」
    show リオン_私服_基本_悲しい2_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0493.ogg"
    lion リオン_私服_基本_悲しい2_1 "呀，啊…嗯…嗯，嗯…嗯"
    hide リオン_私服_基本_微笑み_1

    # nil 「リオンが舌を出してくれたので、その舌を、リオンが俺にしたように、ゆっくりと舌で愛撫する。」
    "里昂伸出舌头，我用舌头慢慢地爱抚她的舌头，就像里昂对我那样"

    # nil 「重力に従って、リオンの唾液が俺の口の中に流れ込んでくる。」
    "随着重力，里昂的唾液流入我的口中"

    # 里昂 「ぁ、んっ…ちゅ、れる…ん、んぅう」
    voice "voice/リオン/ron_a1_0494.ogg"
    lion リオン_私服_基本_悲しい2_1 "啊，嗯…啾，嗯…嗯，嗯"

    # 里昂 「ちゅぅ、れるぅ…ん、れりゅぅ…ちゅぅ…」
    show リオン_私服_基本_キス_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0495.ogg"
    lion リオン_私服_基本_キス_1 "呜嗯、啾…嗯、嗯……啾……"
    hide リオン_私服_基本_悲しい2_1

    # nil 「最後は、二人で舌を出し合って、お互いに絡め合わせさせていく。両腕は抱き合ったま、特に動かす事はなかったが、」
    "最后，两个人互相伸出舌头，让彼此相伸互缠绕，抱在一起，没有什么特别的动作"

    # nil 「キスだけでなんだかイってしまいそうだ。先ほどの観覧車での、リオンの絶頂も頷ける。」
    "只是接吻就觉得很棒了，那么在刚才的摩天轮上，里昂的绝顶也是可以理解的"

    # 里昂 「ちゅ…んぅ…ぷは…はぁ…はぁ…もう…しちゃう…？」
    show リオン_私服_基本_嬉しい_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0496.ogg"
    lion リオン_私服_基本_嬉しい_1 "啾…嗯……呜…哈…哈…已经可以…做了…？"
    hide リオン_私服_基本_キス_1

    # 莲 「する…？」
    lian "做吧…？"

    # 里昂 「ん…蓮くんのすきなように…」
    show リオン_私服_基本_微笑み_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0497.ogg"
    lion リオン_私服_基本_微笑み_1 "嗯…就像莲君喜欢的那样…"
    hide リオン_私服_基本_嬉しい_1

    # nil 「こつんと額を重ね合って、」
    # "额头与额头重合"
    "额头与额头相贴"

    # 里昂 「んっ、ちゅっ…んっ…ちゅっ、ちゅっ…ちゅぅ…」
    show リオン_私服_基本_キス_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0498.ogg"
    lion リオン_私服_基本_キス_1 "嗯，啾……嗯…啾、啾……"
    hide リオン_私服_基本_微笑み_1

    # nil 「時間を稼ぐように、ついばむキス。」
    # "这是等待时机，啄食的吻"
    "这是抓住时机，啄食般的吻"

    # nil 「俺が、劣情にかられて、リオンの腰を後ろから抱き寄せると、ギシッとベッドがきしむ。」
    # "我赌气地从后面抱住里昂的腰，床吱吱作响"
    "我赌气地从后面抱住了里昂的腰，床随着我的动作吱吱作响"

    # 里昂 「ん、ちゅぅ…おっきくなってる…ん…うれし…」
    show リオン_私服_基本_嬉しい_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0499.ogg"
    lion リオン_私服_基本_嬉しい_1 "嗯，啾……变大了…很高兴…"
    hide リオン_私服_基本_キス_1

    # nil 「押しつけられた俺の下腹部のソレに、リオンは小さく微笑んだ。俺も正直耐えられそうにない。」
    # "我小腹的那个东西压在里昂身上，她微微一笑，老实说，我已经无法忍耐了"
    "我小腹下的那个东西压在里昂身上，她微微一笑。老实说，我已经无法忍耐了"

    # nil 「ラブホテルに入ったら、エッチの前にシャワーを浴びるのがセオリーなのはわかっていたのだが…。」
    # "进入情人旅馆后，虽然知道在H前先洗澡是一般理论，但是…"
    "进入情人旅馆后，虽然知道在H前先洗澡是一般流程，但是…"

    # 莲 「リオン…もう、しちゃってもいか…？」
    lian "里昂…已经，可以做了吗…？"

    # 里昂 「ん…♪　じゃあ…えっち…しちゃお…？」
    show リオン_私服_基本_にっこり_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0500.ogg"
    lion リオン_私服_基本_にっこり_1 "嗯♪……那么……来H吧……？"
    hide リオン_私服_基本_嬉しい_1

    # nil 「俺の問いかけに、リオンは快諾してくれる。嬉しくなって、リオンの頭を撫でながらリオンの唇を塞ぐ。」
    "对于我的提问，里昂爽快地答应了。很开心，抚摸着里昂的头，堵住了里昂的嘴唇"

    # 里昂 「んぅ…ちゅぅ…んぅ…ちゅっ…んっ…」
    show リオン_私服_基本_キス_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0501.ogg"
    lion リオン_私服_基本_キス_1 "嗯……嗯……啊…嗯……嗯……"
    hide リオン_私服_基本_にっこり_1

    # 里昂 「きゃっ…」
    show リオン_私服_基本_驚き_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0502.ogg"
    lion リオン_私服_基本_驚き_1 "呀……"
    hide リオン_私服_基本_キス_1

    # nil 「リオンの頭を抱えたま、ころんとロールして、俺が上になる。」
    "抱着里昂的头，滚来滚去，我在上面"

    # nil 「結構ベッドの端ギリギリだ。」
    "这个床还挺结实的嘛"

    # 莲 「うお、あぶね…」
    lian "哦，危险啊…"

    # 里昂 「もぉ…私がしてあげてもいのに…」
    show リオン_私服_基本_ジト目_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0503.ogg"
    lion リオン_私服_基本_ジト目_1 "真是的…明明我帮你做也可以的……"
    hide リオン_私服_基本_驚き_1

    # 莲 蓮「いや、俺も、リオンを可愛がりたい」
    lian "不，我也想疼爱里昂"

    # 里昂 「は、ぁぅ…そ、そういう、どストレートなの…嬉しい…んっ…」
    show リオン_私服_基本_嬉しい_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0504.ogg"
    lion リオン_私服_基本_嬉しい_1 "哈，啊…怎、怎么这么直接…好开心……嗯……"
    hide リオン_私服_基本_ジト目_1

    # 莲 「いか？」
    lian "可以吗？"

    # 里昂 「ぅん…じゃぁ…甘えてもいーい…？」
    show リオン_私服_基本_悲しい2_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0505.ogg"
    lion リオン_私服_基本_悲しい2_1 "嗯…那么…我可以撒娇吗…？"
    hide リオン_私服_基本_嬉しい_1

    # 莲 「あ、めいっぱい気持ち良くなってくれよ…」
    lian "啊，一起变得舒服起来吧"

    # 里昂 「あ、は、ぁぅんっ…！」
    show リオン_私服_基本_嬉しい_1 at love69_lion_center with dissolve
    voice "voice/リオン/ron_a1_0506.ogg"
    lion リオン_私服_基本_嬉しい_1 "啊，哈、哈啊……！"
    hide リオン_私服_基本_悲しい2_1

    # nil 「俺は、リオンの首筋にキスをする。それが試合開始のゴングだった。」
    # "我亲吻了里昂的脖子。那是比赛开始的信号"
    "我亲吻了里昂的脖颈。那是比赛开始的信号"

    # 结尾的信息不翻可能会导致剧情断档，先确认一下需不需要翻，如果需要的话就转比基尼里昂来翻，如果不需要就直接全部Skip~

    # 里昂 HScene1 Skip~
    # ron 507-738
    image httpdog = "images/extra/luckykeeper/httpdog.png"
    if persistent.hsceneG:
        $ quick_menu = False # 隐藏 quick_menu
        window hide
        scene httpdog with dissolve
        pause 3.0

    else:
        pass

    # scene20 场景1 【心跳不已的第一次】 结束

    # 离全部翻译完成只剩 2 个 Scene ！

    # 过场：里昂（常服）

    # Scene20 结束！
    # 隐藏 quick_menu
    $ quick_menu = False

    play sound "voice/effect/moosehead honk (stinger).ogg"
    # hide screen quick_menu
    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)
    scene アイキャッチリオン with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=False, alpha=True, time_warp=None)

    $ renpy.pause(1.5, hard=True)
    $ renpy.end_replay()

    jump scene21

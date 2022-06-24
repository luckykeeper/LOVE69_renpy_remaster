# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene14 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：
# 版本 NightBuild "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年6月24日

# 当前流程：All Done!

label scene14:
    # scene14 开始

    # scene14 场景1 【热情似火的夏威夷】 开始

    # 地点：夏威夷酒店
    # 人物：心爱 真冬 莲
    # BGM：无
    # 可变标题
    # Scene 序号
    $ sceneNo =  " scene14"
    # 存档名称和 Scene 大标题
    $ sceneName = " 真冬&心爱线 三人心跳时刻"
    # 小场景的名称
    $ partName = "【热情似火的夏威夷】"
    $ changeTitleName()

    scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)

    # 显示 quick_menu
    $ quick_menu = True

    # nil 「ホテルにチェックイン完了。」
    "酒店入住完毕"

    # 莲 「さて、では、まずはお部屋の内装についてご紹介を―」
    lian "然后，那么，首先介绍一下房间的内部装修吧"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「どうりゃあ！！！！」
    # 没有跳过
    voice "voice/心愛/cca_a1_1762.ogg"
    ai 心愛_水着_基本_ニタァ "怎么样！！！！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「だっしゃぁあ！！！」
    voice "voice/真冬/maf_a1_1416.ogg"
    dong 真冬_水着_基本_ニタァ "哒呷！！！"

    # 莲 「やっぱりかあ！！！！」
    lian "果然会这样啊！！！！"

    # nil 「可愛い彼女二人による鮮やかな連携プレーにより、フカフカ新素材のベッドに張り倒されました。」
    # "由于两位可爱的女朋友的精彩合作，被扑倒在松软舒适的新材料床上了"
    "由于两位可爱女朋友的精彩合作，被扑倒在松软舒适的新材料床上了"

    # nil 「もう少し大切に扱えよなぁ！フィアンセをよぉ！」
    "稍微好好珍惜对待一下啊！我的未婚妻们啊！"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「心愛ちゃん、脚抑えて。私頭いくから」
    voice "voice/真冬/maf_a1_1417.ogg"
    dong 真冬_水着_基本_ニタァ "心爱酱，把脚压住，我去脑袋那边"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「おっけー！　ほいでは、彼氏くん、失礼しますよ」
    voice "voice/心愛/cca_a1_1763.ogg"
    ai 心愛_水着_基本_ニタァ "OK——！那么，男朋友，稍微失礼一下啦"

    # 莲 「なんだ、今日はいやに積極的じゃないか…」
    lian "什么嘛，今天不是很积极吗…"

    # nil 「リオンから貰ったアイスの効果もあるだろうが、やはりこの常夏の島のバカンスで舞い上がっているのだろう。」
    "虽然也有从里昂那里得到的冰淇淋的效果，但还是在这个常夏的岛上度假的时候兴奋起来了吧"

    # nil 「だから、今夜は俺も精々楽しませて貰うとしようか！」
    "所以，今晚我也尽情享受吧！"

    # nil 「ということで…。」
    "因此…"

    # 心爱&真冬 HScene 03 Skip~
    # cca 1764-1850
    # maf 1416-1495
    image bg 寧々 = "images/extra/luckykeeper/寧々.png"
    if persistent.hsceneG:
        $ quick_menu = False # 隐藏 quick_menu
        window hide
        scene 寧々 with dissolve
        pause 3.0

    else:
        pass

    # scene14 场景1 【热情似火的夏威夷】 结束

    # Scene14 结束！

    # 过场： 心爱&真冬（常服）
    ## 稍微改改
    image bg アイキャッチ心愛＆真冬水着 = "images/bg/アイキャッチ心愛＆真冬水着.png"

    $ quick_menu = False

    play sound "voice/effect/moosehead honk (stinger).ogg"
    # scene black with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)
    scene アイキャッチ心愛＆真冬水着 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)

    $ renpy.pause(1.5, hard=True)
    $ renpy.end_replay()

    jump scene15

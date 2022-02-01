# --------------------------------
# LOVE69_Renpy_Remaster_Project
# 人物名称定义（人物表）
# Author:Luckykeeper
# 版本 0.4 "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 开始日期 2021年8月28日
# 修订日期 2022年2月2日

# 定义老婆和其他人的名字
# 基本定义如下，取中文拼音最后一字的全拼
# | 角色 | 脚本中的代号 | 备注 |
# 一条心爱 ai
# 葛城真冬 dong
# 葛城莲 lian
# 里昂·麦克斯韦 lion //使用英文名，因为是英国人
# 月宫想瑠 liu
# 月宫瑠那 na
# 雾叶（和亚十礼的姓有待商榷，有想法的老哥快来） ye
# 花盆君（植木鉢） pen
# 亚十礼（发音ATRI,雾叶的姐姐）atri //暂定译名从近月2来，缩写atri因为高性能~
# 迈克尔（帽子） mj //帽子就不要名字了（有名字，缩写mj，但是这里为了做区分就叫它帽子）|改，有的地方叫帽子，所以认识之前还是叫hat好了
# 旁白君 bai
# テしビ TV 最早在 sence01 葛城家客厅出现，不大确定是啥，应该是电视里面传来的声音，暂时管电视里面没立绘（包括后面的）的都叫TV好辽
# 翻译君（我自己） Luckykeeper
# ？？？ unknown404 给不知道是谁的时候用 //根据实际开发情况决定弃用，在全部替换完成后注释define
# nil 没人说话的旁白，不在脚本中定义名称
# wsa 女学生A （Woman Student A）


###########尝试定义可变名称，失败，测试带对话框头像的不能使用这种方式，名称可变，但是小头像无法显示
###########解决方案：新建一个人物，每个有？？？的都需要一个，立绘也要单独建文件夹
###########原因是可变名称只能指定名称一个属性，其它属性即使设置了也无效，而小头像是用tag去找图片的，不指定image属性就不能用tag找图片
###########如果没有显示小头像的需求可参照下面的参考代码

# init python in character:
#     ai = "？？？"
#
# $ import store.character as character
# define ai = Character("character.ai]",color="#ffc9be",image="心愛")
# $ character.ai = "心爱"
###########

# 一条心爱 ai //和原版相比，移植版打算在人物名上加入颜色，心爱的颜色是场景切换的CG里从刘海儿中间上最长的那根毛上面取的

define ai = Character("心爱",color="#ffc9be",image="心愛")

# 定义心爱的立绘
# 显示在画面中的

# 常服_普通系列
image side 心愛 心愛_制服_基本_にっこり = "images/face/心愛/心愛_制服_基本_にっこり.png" # 闭眼，微笑
image side 心愛 心愛_制服_基本_にっこり1 = "images/face/心愛/心愛_制服_基本_にっこり1.png" # 闭眼，微笑，脸红
image side 心愛 心愛_制服_基本_ジト目 = "images/face/心愛/心愛_制服_基本_ジト目.png" # 睁眼，嘴三角，眉平缓向中下
image side 心愛 心愛_制服_基本_不機嫌 = "images/face/心愛/心愛_制服_基本_不機嫌.png" # 睁眼，嘴-(
image side 心愛 心愛_制服_基本_不機嫌1 = "images/face/心愛/心愛_制服_基本_不機嫌1.png" # 睁眼，嘴-(，脸红
image side 心愛 心愛_制服_基本_もぐもぐ = "images/face/心愛/心愛_制服_基本_もぐもぐ.png" # 闭眼，嘴-(，两个粉椭圆
image side 心愛 心愛_制服_基本_ニタァ = "images/face/心愛/心愛_制服_基本_ニタァ.png" # 睁眼，嘴开口，“w”，是有点小坏的笑呢，两个粉椭圆
image side 心愛 心愛_制服_基本_笑顔 = "images/face/心愛/心愛_制服_基本_笑顔.png" # 睁眼，嘴o
image side 心愛 心愛_制服_基本_笑顔1 = "images/face/心愛/心愛_制服_基本_笑顔1.png" # 睁眼，嘴o，脸红
image side 心愛 心愛_制服_基本_泣き= "images/face/心愛/心愛_制服_基本_泣き.png" # 睁眼，含泪珠
image side 心愛 心愛_制服_基本_驚き = "images/face/心愛/心愛_制服_基本_驚き.png" # 睁眼，惊讶
image side 心愛 心愛_制服_基本_真顔 = "images/face/心愛/心愛_制服_基本_真顔.png" # 睁眼，嘴闭
image side 心愛 心愛_制服_基本_真顔1 = "images/face/心愛/心愛_制服_基本_真顔1.png" # 睁眼，嘴闭，脸红
image side 心愛 心愛_制服_基本_無表情 = "images/face/心愛/心愛_制服_基本_無表情.png" # 字面意思，睁眼，嘴·
image side 心愛 心愛_制服_基本_きらきら = "images/face/心愛/心愛_制服_基本_きらきら.png" # 睁眼，嘴⚪三角，眼睛有小星星，这属于是馋哭了
image side 心愛 心愛_制服_基本_ぶわー = "images/face/心愛/心愛_制服_基本_ぶわー.png" # 闭眼，很有标志性的哭
image side 心愛 心愛_制服_基本_キス = "images/face/心愛/心愛_制服_基本_キス.png" # 闭眼，脸红，kiss准备
image side 心愛 心愛_制服_基本_ぐるぐる = "images/face/心愛/心愛_制服_基本_ぐるぐる.png" # （被打）晕了
image side 心愛 心愛_制服_基本_嬉しい = "images/face/心愛/心愛_制服_基本_嬉しい.png" # 康起来很喜感的笑
image side 心愛 心愛_制服_基本_嬉しい1 = "images/face/心愛/心愛_制服_基本_嬉しい1.png" # 康起来很喜感的笑，脸红
image side 心愛 心愛_制服_基本_微笑み = "images/face/心愛/心愛_制服_基本_微笑み.png" # 睁眼，微笑
image side 心愛 心愛_制服_基本_微笑み1 = "images/face/心愛/心愛_制服_基本_微笑み1.png" # 睁眼，微笑，脸红
image side 心愛 心愛_制服_基本_ぐるぐる = "images/face/心愛/心愛_制服_基本_ぐるぐる.png" # 眼睛咕哩咕噜转圈圈
image side 心愛 心愛_制服_基本_覚醒02 = "images/face/心愛/心愛_制服_基本_覚醒02.png" # 心爱觉醒，眼睛变成蛇的样子，眼睛微眯
image side 心愛 心愛_制服_基本_まふまふ = "images/face/心愛/心愛_制服_基本_まふまふ.png" # 基于笑顔，闭眼，两个粉椭圆

# 常服_奶糖苹果系列
image side 心愛 心愛_制服_おやつ_にっこり = "images/face/心愛/心愛_制服_おやつ_にっこり.png" # 闭眼，微笑，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_ジト目 = "images/face/心愛/心愛_制服_おやつ_ジト目.png" # 睁眼，嘴三角，眉平缓向中下，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_ジト目1 = "images/face/心愛/心愛_制服_おやつ_ジト目1.png" # 睁眼，嘴三角，眉平缓向中下，脸红，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_不機嫌 = "images/face/心愛/心愛_制服_おやつ_不機嫌.png" # 睁眼，嘴-(，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_不機嫌1 = "images/face/心愛/心愛_制服_おやつ_不機嫌1.png" # 睁眼，嘴-(，脸红，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_もぐもぐ = "images/face/心愛/心愛_制服_おやつ_もぐもぐ.png" # 睁眼，嘴-(，两个粉椭圆，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_笑顔 = "images/face/心愛/心愛_制服_おやつ_笑顔.png" # 睁眼，嘴o，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_笑顔1 = "images/face/心愛/心愛_制服_おやつ_笑顔1.png" # 睁眼，嘴o，脸红，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_泣き= "images/face/心愛/心愛_制服_おやつ_泣き.png" # 睁眼，含泪珠，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_泣き1= "images/face/心愛/心愛_制服_おやつ_泣き1.png" # 睁眼，含泪珠，脸红，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_驚き = "images/face/心愛/心愛_制服_おやつ_驚き.png" # 睁眼，惊讶，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_真顔 = "images/face/心愛/心愛_制服_おやつ_真顔.png" # 睁眼，嘴闭，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_真顔1 = "images/face/心愛/心愛_制服_おやつ_真顔1.png" # 睁眼，嘴闭，脸红，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_無表情 = "images/face/心愛/心愛_制服_おやつ_無表情.png" # 字面意思，睁眼，嘴·，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_無表情1 = "images/face/心愛/心愛_制服_おやつ_無表情1.png" # 字面意思，睁眼，嘴·，脸红，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_ぶわー = "images/face/心愛/心愛_制服_おやつ_ぶわー.png" # 闭眼，很有标志性的哭，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_嬉しい = "images/face/心愛/心愛_制服_おやつ_嬉しい.png" # 康起来很喜感的笑，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_嬉しい1 = "images/face/心愛/心愛_制服_おやつ_嬉しい1.png" # 康起来很喜感的笑，脸红，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_微笑み = "images/face/心愛/心愛_制服_おやつ_微笑み.png" # 睁眼，微笑，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_微笑み1 = "images/face/心愛/心愛_制服_おやつ_微笑み1.png" # 睁眼，微笑，脸红，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_ジト目1 = "images/face/心愛/心愛_制服_おやつ_ジト目1.png" # 睁眼，嘴三角，眉平缓向中下，拿着奶糖苹果
image side 心愛 心愛_制服_おやつ_キス = "images/face/心愛/心愛_制服_おやつ_キス.png" # 闭眼，脸红，kiss准备，拿着奶糖苹果

# 大_常服_奶糖苹果系列
image side 心愛 心愛_大_制服_おやつ_キス = "images/face/心愛/心愛_大_制服_おやつ_キス.png" # 大，闭眼，脸红，kiss准备，拿着奶糖苹果
image side 心愛 心愛_大_制服_おやつ_不機嫌1 = "images/face/心愛/心愛_大_制服_おやつ_不機嫌1.png" # 大，睁眼，嘴-(，脸红，拿着奶糖苹果

# 大_常服_普通系列
image side 心愛 心愛_大_制服_基本_キス = "images/face/心愛/心愛_大_制服_おやつ_キス.png" # 大，闭眼，脸红，kiss准备
image side 心愛 心愛_大_制服_基本_にっこり1 = "images/face/心愛/心愛_大_制服_基本_にっこり1.png" # 大，闭眼，微笑
image side 心愛 心愛_大_制服_基本_きらきら = "images/face/心愛/心愛_大_制服_基本_きらきら.png" # 睁眼，嘴⚪三角，眼睛有小星星，这属于是馋哭了
image side 心愛 心愛_大_制服_基本_真顔 = "images/face/心愛/心愛_大_制服_基本_真顔.png" # 大，睁眼，嘴闭
image side 心愛 心愛_大_制服_基本_真顔1 = "images/face/心愛/心愛_大_制服_基本_真顔1.png" # 大，睁眼，嘴闭，脸红
image side 心愛 心愛_大_制服_基本_嬉しい = "images/face/心愛/心愛_大_制服_基本_嬉しい.png" # 大，康起来很喜感的笑
image side 心愛 心愛_大_制服_基本_泣き= "images/face/心愛/心愛_大_制服_基本_泣き.png" # 大，睁眼，含泪珠
image side 心愛 心愛_大_制服_基本_もぐもぐ = "images/face/心愛/心愛_大_制服_基本_もぐもぐ.png" # 大，闭眼，嘴-(，两个粉椭圆
image side 心愛 心愛_大_制服_基本_ニタァ = "images/face/心愛/心愛_大_制服_基本_ニタァ.png" # 大，睁眼，嘴开口，“w”，是有点小坏的笑呢，两个粉椭圆
image side 心愛 心愛_大_制服_基本_驚き = "images/face/心愛/心愛_大_制服_基本_驚き.png" # 大，睁眼，惊讶

# 其它
image side 心愛 心愛_トランザム = "images/face/心愛/心愛_トランザム.png" # 全身变红，心爱真·觉醒！
image side 心愛 心愛_ラフ = "images/face/心愛/心愛_ラフ.png" # 粗线条描绘的心爱酱
image side 心愛 心愛_制服_基本_覚醒 = "images/face/心愛/心愛_制服_基本_覚醒.png" # 基于无表情，眼睛深红

# 下面定义不知道是谁的时候的心爱
# 知不道的人物使用发色称呼
# 如：心爱——>粉
# 文件应当取自 face 文件夹，但是stand有现成更清晰的，且参数已经调试完毕，所以用stand，stand没有的再进行特殊处理，为了和后面的waifu2x区分
# 工程目录写为 face
define fen = Character("？？？",color="#ffc9be",image="粉")
image side 粉 粉_制服_基本_にっこり = "images/face/粉/粉_制服_基本_にっこり.png" # 闭眼，微笑
image side 粉 粉_制服_基本_ジト目 = "images/face/粉/粉_制服_基本_ジト目.png" # 睁眼，嘴三角，眉平缓向中下
image side 粉 粉_制服_基本_不機嫌 = "images/face/粉/粉_制服_基本_不機嫌.png" # 睁眼，嘴-(
image side 粉 粉_制服_基本_もぐもぐ = "images/face/粉/粉_制服_基本_もぐもぐ.png" # 睁眼，嘴-(，两个粉椭圆
image side 粉 粉_制服_基本_笑顔 = "images/face/粉/粉_制服_基本_笑顔.png" # 睁眼，嘴o
image side 粉 粉_制服_基本_泣き= "images/face/粉/粉_制服_基本_泣き.png" # 睁眼，和真冬的表情很像呢
image side 粉 粉_制服_基本_驚き= "images/face/粉/粉_制服_基本_驚き.png" # 睁眼，惊讶

###############################################角色分割线###############################################

# 葛城真冬 dong //和原版相比，移植版打算在人物名上加入颜色，真冬的颜色是场景切换的CG里从领带上面取的
define dong = Character('真冬',color="#4da8c0",image="真冬")
# 定义真冬的立绘
# 显示在画面中的

# 定义显示在对话框中的小人物头像
# 文件应当取自 face 文件夹，但是stand有现成更清晰的，且参数已经调试完毕，所以用stand，stand没有的再进行特殊处理，为了和后面的waifu2x区分
# 工程目录写为 face
image side 真冬 真冬_制服_基本_無表情 = "images/face/真冬/真冬_制服_基本_無表情.png" # 字面意思，睁眼，嘴·
image side 真冬 真冬_制服_基本_むーっ = "images/face/真冬/真冬_制服_基本_むーっ.png" # 闭眼，撅嘴，眉毛y=-x（斜下45度）
image side 真冬 真冬_制服_基本_ジト目 = "images/face/真冬/真冬_制服_基本_ジト目.png" # 睁眼，嘴三角，眉上凸
image side 真冬 真冬_制服_基本_本気2 = "images/face/真冬/真冬_制服_基本_本気2.png" # 眼睁大，眉毛y=-x，嘴o
image side 真冬 真冬_制服_基本_微笑み = "images/face/真冬/真冬_制服_基本_微笑み.png" # 字面意思
image side 真冬 真冬_制服_基本_微笑み2 = "images/face/真冬/真冬_制服_基本_微笑み2.png" # 字面意思，嘴型近“o”
image side 真冬 真冬_制服_基本_目閉じ = "images/face/真冬/真冬_制服_基本_目閉じ.png" # 闭眼，嘴·
image side 真冬 真冬_制服_基本_目閉じ_1 = "images/face/真冬/真冬_制服_基本_目閉じ_1.png"
image side 真冬 真冬_制服_基本_泣き = "images/face/真冬/真冬_制服_基本_泣き.png" # 睁眼，含泪珠
image side 真冬 真冬_制服_基本_泣き_1 = "images/face/真冬/真冬_制服_基本_泣き_1.png"
image side 真冬 真冬_制服_基本_見下し = "images/face/真冬/真冬_制服_基本_見下し.png" # 闭眼，眉毛y=-x，嘴o
image side 真冬 真冬_制服_基本_見下し2 = "images/face/真冬/真冬_制服_基本_見下し2.png"
image side 真冬 真冬_制服_基本_にっこり = "images/face/真冬/真冬_制服_基本_にっこり.png" # 闭眼，微笑
image side 真冬 真冬_制服_基本_にっこり_1 = "images/face/真冬/真冬_制服_基本_にっこり_1.png"
image side 真冬 真冬_制服_基本_まったり = "images/face/真冬/真冬_制服_基本_まったり.png" # 闭眼，嘴“w”，嘛呼嘛呼
image side 真冬 真冬_制服_基本_おやつ1 = "images/face/真冬/真冬_制服_基本_おやつ1.png" # 闭眼，嘴“w”，拿着奶糖苹果
image side 真冬 真冬_制服_基本_おやつ2 = "images/face/真冬/真冬_制服_基本_おやつ2.png" # 闭眼，嘴开口，“w”，是有点小坏的笑呢，拿着奶糖苹果
image side 真冬 真冬_制服_基本_おやつ3 = "images/face/真冬/真冬_制服_基本_おやつ3.png" # 闭眼，嘴开口，椭圆，是有点小萌的笑呢，拿着奶糖苹果
image side 真冬 真冬_制服_基本_ニタァ = "images/face/真冬/真冬_制服_基本_ニタァ.png" # 睁眼，嘴开口，“w”，是有点小坏的笑呢
# https://github.com/luckykeeper/LOVE69_renpy_remaster/issues/2 04
image side 真冬 真冬_制服_基本_居眠り = "images/face/真冬/真冬_制服_基本_居眠り.png" # 闭眼，嘴开口，半圆，碎着辽~

# 裸y衬衫系列
image side 真冬 真冬_裸yシャツ_パンツ_無表情 = "images/face/真冬/真冬_裸yシャツ_パンツ_無表情.png" # 字面意思，睁眼，嘴·
image side 真冬 真冬_裸yシャツ_パンツ_まったり = "images/face/真冬/真冬_裸yシャツ_パンツ_まったり.png" # 闭眼，嘴“w”，嘛呼嘛呼
image side 真冬 真冬_裸yシャツ_パンツ_目閉じ = "images/face/真冬/真冬_裸yシャツ_パンツ_目閉じ.png" # 闭眼，嘴·
image side 真冬 真冬_裸yシャツ_パンツ_微笑み = "images/face/真冬/真冬_裸yシャツ_パンツ_微笑み.png" # 字面意思
image side 真冬 真冬_裸yシャツ_パンツ_居眠り = "images/face/真冬/真冬_裸yシャツ_パンツ_居眠り.png" # 闭眼，嘴开口，半圆，碎着辽~
image side 真冬 真冬_裸yシャツ_パンツ_ジト目 = "images/face/真冬/真冬_裸yシャツ_パンツ_ジト目.png" # 睁眼，嘴三角，眉上凸
image side 真冬 真冬_裸yシャツ_パンツ_微笑み2 = "images/face/真冬/真冬_裸yシャツ_パンツ_微笑み2.png" # 字面意思，嘴型近“o”
image side 真冬 真冬_裸yシャツ_パンツ_見下し = "images/face/真冬/真冬_裸yシャツ_パンツ_見下し.png" # 闭眼，眉毛y=-x，嘴o

# 其它
image side 真冬 真冬_通話中 = "images/face/真冬/真冬_通話中.png" # 装在携带里面的真冬


# 葛城莲 lian //主人公，工具人就不要加颜色了吧，不加颜色的统一强制指定白色（#ffffff）
define lian = Character('莲',color="#ffffff")

# 里昂·麦克斯韦 lion //和原版相比，移植版打算在人物名上加入颜色，里昂的颜色是摘掉帽子之后在头顶上取的
define lion = Character('里昂',color="#fff7bb",image="リオン")

# 定义里昂的立绘
# 显示在画面中的

image side リオン リオン_帽子無し_杖_微笑み = "images/face/リオン/リオン_帽子無し_杖_微笑み.png" # 睁眼，没帽子，拿杖，微笑
image side リオン リオン_基本_杖_微笑み = "images/face/リオン/リオン_基本_杖_微笑み.png" # 睁眼，有帽子，拿杖，微笑
image side リオン リオン_帽子無し_杖なし_微笑み = "images/face/リオン/リオン_帽子無し_杖なし_微笑み.png" # 睁眼，没帽子，没杖，微笑
image side リオン リオン_基本_杖_にっこり = "images/face/リオン/リオン_基本_杖_にっこり.png" # 闭眼，有帽子，拿杖，微笑
image side リオン リオン_基本_杖_嬉しい = "images/face/リオン/リオン_基本_杖_嬉しい.png" # 闭眼，有帽子，拿杖，喜
image side リオン リオン_帽子無し_杖_ジト目 = "images/face/リオン/リオン_帽子無し_杖_ジト目.png" # 睁眼，没帽子，拿杖，皱眉，嘴倒三角
image side リオン リオン_基本_杖_ジト目 = "images/face/リオン/リオン_基本_杖_ジト目.png" # 睁眼，有帽子，拿杖，皱眉，嘴倒三角
image side リオン リオン_帽子無し_杖_ニタァ = "images/face/リオン/リオン_帽子無し_杖_ニタァ.png" # 睁眼，没帽子，拿杖，皱眉，嘴半圆，是有点小坏的笑呢
image side リオン リオン_基本_杖_ニタァ = "images/face/リオン/リオン_基本_杖_ニタァ.png" # 睁眼，有帽子，拿杖，皱眉，嘴半圆，是有点小坏的笑呢
image side リオン リオン_帽子無し_杖_驚き = "images/face/リオン/リオン_帽子無し_杖_ニタァ.png" # 睁眼，没帽子，拿杖，惊讶
image side リオン リオン_基本_杖_驚き = "images/face/リオン/リオン_基本_杖_驚き.png" # 睁眼，有帽子，拿杖，惊讶
image side リオン リオン_帽子無し_杖_悲しい = "images/face/リオン/リオン_帽子無し_杖_悲しい.png" # 睁眼，没帽子，拿杖，悲，嘴小开口
image side リオン リオン_基本_杖_悲しい = "images/face/リオン/リオン_基本_杖_悲しい.png" # 睁眼，有帽子，拿杖，悲，嘴小开口
image side リオン リオン_基本_杖_悲しい2 = "images/face/リオン/リオン_基本_杖_悲しい2.png" # 睁眼，有帽子，拿杖，悲，嘴一条缝
image side リオン リオン_基本_杖_無表情 = "images/face/リオン/リオン_基本_杖_無表情.png" # 睁眼，有帽子，拿杖，莫得感情
image side リオン リオン_基本_杖_見下し = "images/face/リオン/リオン_基本_杖_見下し.png" # 睁眼，有帽子，拿杖，嘴三角圆
image side リオン リオン_基本_杖_ぶわー = "images/face/リオン/リオン_基本_杖_ぶわー.png" # 睁眼，有帽子，拿杖，是和心爱一样标志性的哭呢

# 下面定义不知道是谁的时候的里昂
# 知不道的人物使用发色称呼
# 如：里昂——>黄
# 文件应当取自 face 文件夹，但是stand有现成更清晰的，且参数已经调试完毕，所以用stand，stand没有的再进行特殊处理，为了和后面的waifu2x区分
# 工程目录写为 face
define ang = Character('少女',color="#fff7bb",image="黄")
image side 黄 黄_帽子無し_杖_微笑み = "images/face/黄/黄_帽子無し_杖_微笑み.png" # 睁眼，没帽子，拿杖，微笑
image side 黄 黄_基本_杖_微笑み = "images/face/黄/黄_基本_杖_微笑み.png" # 睁眼，有帽子，拿杖，微笑
image side 黄 黄_帽子無し_杖なし_微笑み = "images/face/黄/黄_帽子無し_杖なし_微笑み.png" # 睁眼，没帽子，没杖，微笑
image side 黄 黄_基本_杖_にっこり = "images/face/黄/黄_基本_杖_にっこり.png" # 闭眼，有帽子，拿杖，微笑
image side 黄 黄_帽子無し_杖_ジト目 = "images/face/黄/黄_帽子無し_杖_ジト目.png" # 睁眼，没帽子，拿杖，皱眉，嘴倒三角
image side 黄 黄_基本_杖_ジト目 = "images/face/黄/黄_基本_杖_ジト目.png" # 睁眼，有帽子，拿杖，皱眉，嘴倒三角
image side 黄 黄_帽子無し_杖_ニタァ = "images/face/黄/黄_帽子無し_杖_ニタァ.png" # 睁眼，没帽子，拿杖，皱眉，嘴半圆，是有点小坏的笑呢
image side 黄 黄_基本_杖_ニタァ = "images/face/黄/黄_基本_杖_ニタァ.png" # 睁眼，有帽子，拿杖，皱眉，嘴半圆，是有点小坏的笑呢
image side 黄 黄_帽子無し_杖_驚き = "images/face/黄/黄_帽子無し_杖_ニタァ.png" # 睁眼，没帽子，拿杖，惊讶
image side 黄 黄_基本_杖_驚き = "images/face/黄/黄_基本_杖_驚き.png" # 睁眼，有帽子，拿杖，惊讶
image side 黄 黄_帽子無し_杖_悲しい = "images/face/黄/黄_帽子無し_杖_悲しい.png" # 睁眼，没帽子，拿杖，悲，嘴小开口
image side 黄 黄_基本_杖_無表情 = "images/face/黄/黄_基本_杖_無表情.png" # 睁眼，有帽子，拿杖，莫得感情
image side 黄 黄_基本_杖_見下し = "images/face/黄/黄_基本_杖_見下し.png" # 睁眼，有帽子，拿杖，嘴三角圆
image side 黄 黄_基本_杖_ぶわー = "images/face/黄/黄_基本_杖_ぶわー.png" # 睁眼，有帽子，拿杖，是和心爱一样标志性的哭呢

# 月宫想瑠 liu //和原版相比，移植版打算在人物名上加入颜色，想瑠喵的颜色是SISTARS里面的CG里面取的
define liu = Character('想瑠',color="#a4808c",image="想瑠")

# 定义显示在对话框中的小人物头像
# 文件应当取自 face 文件夹，但是stand有现成更清晰的，且参数已经调试完毕，所以用stand，stand没有的再进行特殊处理，为了和后面的waifu2x区分
# 工程目录写为 face
image side 想瑠 想瑠_スーツ_ニヤリ = "images/face/想瑠/想瑠_スーツ_ニヤリ.png" # 睁眼，嘴“w”，手撑头，两个粉椭圆
image side 想瑠 想瑠_スーツ_見下し = "images/face/想瑠/想瑠_スーツ_見下し.png" # 睁眼，嘴椭圆小开口，手撑头
image side 想瑠 想瑠_スーツ_真顔 = "images/face/想瑠/想瑠_スーツ_真顔.png" # 睁眼，嘴点点，手撑头
image side 想瑠 想瑠_スーツ_真顔2 = "images/face/想瑠/想瑠_スーツ_真顔2.png" # 睁眼，嘴-，手撑头
image side 想瑠 想瑠_スーツ_目閉じ = "images/face/想瑠/想瑠_スーツ_目閉じ.png" # 闭眼，嘴点点，手撑头
image side 想瑠 想瑠_スーツ_本気 = "images/face/想瑠/想瑠_スーツ_本気.png" # 睁眼，嘴-，眉毛斜向下，手撑头，认真起来了捏
image side 想瑠 想瑠_スーツ_悲しみ = "images/face/想瑠/想瑠_スーツ_悲しみ.png" # 睁眼，嘴点点，悲伤，康起来穷嗖嗖的感觉233
image side 想瑠 想瑠_スーツ_にっこり = "images/face/想瑠/想瑠_スーツ_にっこり.png" # 闭眼，微笑（乖巧）
image side 想瑠 想瑠_スーツ_ほほえみ = "images/face/想瑠/想瑠_スーツ_ほほえみ.png" # 睁眼，微笑（乖巧）
image side 想瑠 想瑠_スーツ_ぶわ = "images/face/想瑠/想瑠_スーツ_ぶわ.png" # 是和心爱一样标志性的哭

# 月宫瑠那 na //和原版相比，移植版打算在人物名上加入颜色，瑠那的颜色是SISTARS里面的CG里面取的
define na = Character('瑠那',color="#a4808c",image="瑠那")

# 雾叶 ye //和原版相比，移植版打算在人物名上加入颜色，雾叶的颜色是从皮带上十字的中央取的
define ye = Character('雾叶',color="#414141",image="霧葉")

# 雾叶在本作更多的时候叫店长
# 好久没写了差点忘记了，还排了半天Bug
# 定义人物头像的时候必须写tag
# image side 店长 店长_私服_本気 = "images/face/店长/店长_私服_本気.png"
# 店长 店长_私服_本気 前面的店长是tag，不可省略
# 后面的 店长_私服_本気 是调用的图片
define dinerowner = Character('店长',color="#414141",image="店长")
image side 店长 店长_私服_目閉じ = "images/face/店长/店长_私服_目閉じ.png" # 闭眼，嘴微张，手撑头
image side 店长 店长_私服_目閉じ_1 = "images/face/店长/店长_私服_目閉じ_1.png" # 闭眼，嘴微张，手撑头
image side 店长 店长_私服_微笑み = "images/face/店长/店长_私服_微笑み.png" # 睁眼，微笑，闭嘴，手撑头
image side 店长 店长_私服_微笑み_1 = "images/face/店长/店长_私服_微笑み_1.png" # 睁眼，微笑，闭嘴，手撑头，脸红
image side 店长 店长_私服_本気 = "images/face/店长/店长_私服_本気.png" # 睁眼，嘴o，手撑头
image side 店长 店长_私服_ニヤリ = "images/face/店长/店长_私服_ニヤリ.png" # 睁眼，手撑头，是有点小坏的笑呢
image side 店长 店长_私服_ニヤリ_1 = "images/face/店长/店长_私服_ニヤリ_1.png" # 睁眼，手撑头，是有点小坏的笑呢，脸红
image side 店长 店长_私服_無表情 = "images/face/店长/店长_私服_無表情.png" # 睁眼，手撑头，闭嘴，莫得感情
image side 店长 店长_私服_ジト目 = "images/face/店长/店长_私服_ジト目.png" # 睁眼，手撑头，嘴椭圆，一脸正经


# 下面定义不知道是谁的时候的雾叶
# 知不道的人物使用发色称呼
# 如：雾叶——>黑
define hei = Character("？？？",color="#414141",image="黑")
image side 黑 黑_私服_無表情 = "images/face/黑/黑_私服_無表情.png" # 睁眼，挠头，闭嘴，莫得感情
image side 黑 黑_私服_ニヤリ = "images/face/黑/黑_私服_ニヤリ.png" # 睁眼，挠头，是有点小坏的笑呢
image side 黑 黑_私服_不満 = "images/face/黑/黑_私服_ニヤリ.png" # 和无表情很像但是皱眉
image side 黑 黑_私服_目閉じ = "images/face/黑/黑_私服_目閉じ.png" # 和无表情很像但是皱眉

# 花盆君 pen //和原版相比，移植版打算在人物名上加入颜色，花盆君的颜色当然是健康的绿色啦~
define pen = Character('花盆君',color="#659839",image="花盆君")
image side 花盆君 花盆君_通常 = "images/face/花盆君/花盆君_通常.png" # 花盆君

# 亚十礼 atri //和原版相比，移植版打算在人物名上加入颜色，亚十礼的颜色也是从头发上取哒~
define atri = Character('亚十礼',color="#fcfafc",image="アシュリー")

# 迈克尔 mj //和原版相比，移植版打算在人物名上加入颜色，帽子就要它本来的颜色就好啦~
define hat = Character('帽子',color="#67435e",image="帽子")
define mj = Character('MJ',color="#67435e",image="MJ")

image side 帽子 帽子_通常 = "images/face/帽子/帽子_通常.png" # 帽子？？？
image side MJ MJ_通常 = "images/face/MJ/MJ_通常.png" # MJ

# 旁白君 bai 不加颜色的统一强制指定白色（#ffffff）
define bai = Character('旁白君',color="#ffffff")

# テしビ tv 不加颜色的统一强制指定白色（#ffffff）
define tv = Character('TV',color="#ffffff")

# 翻译君（我自己） Luckykeeper 用于写长段注释，图标从QQ头像来（要圆的）//译者君的颜色是从个人博客的favion图案里面来哒，和心爱的颜色很像哦~
define luckykeeper = Character('Luckykeeper',color="#ffc0cb")

# ？？？ ??? 给不知道是谁的时候用 不加颜色的统一强制指定白色（#ffffff）
define unknown404 = Character('？？？',color="#ffffff",image="unknown404")

# wsa 女学生A （Woman Student A） 不加颜色的统一强制指定白色（#ffffff）
define wsa = Character('女学生A',color="#ffffff")

# bear 熊 （Woman Student A） 不加颜色的统一强制指定白色（#ffffff）
define bear = Character('熊',color="#ffffff")

# 人物名称定义结束
# ---------------------------------------------

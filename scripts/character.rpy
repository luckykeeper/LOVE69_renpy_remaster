# --------------------------------
# LOVE69_Renpy_Remaster_Project
# 人物名称定义（人物表）
# Author:Luckykeeper
# 版本 1.0 "LuckyCocoa"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 开始日期 2021年8月28日
# 修订日期 2022年4月27日

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
image side 心愛 心愛_制服_基本_もぐもぐ = "images/face/心愛/心愛_制服_基本_もぐもぐ.png" # 闭眼，嘴-(，两个粉椭圆，嘛呼嘛呼
image side 心愛 心愛_制服_基本_ニタァ = "images/face/心愛/心愛_制服_基本_ニタァ.png" # 睁眼，嘴开口，“w”，是有点小坏的笑呢，两个粉椭圆
image side 心愛 心愛_制服_基本_笑顔 = "images/face/心愛/心愛_制服_基本_笑顔.png" # 睁眼，嘴o
image side 心愛 心愛_制服_基本_笑顔1 = "images/face/心愛/心愛_制服_基本_笑顔1.png" # 睁眼，嘴o，脸红
image side 心愛 心愛_制服_基本_泣き= "images/face/心愛/心愛_制服_基本_泣き.png" # 睁眼，含泪珠
image side 心愛 心愛_制服_基本_号泣1= "images/face/心愛/心愛_制服_基本_号泣1.png" # 闭眼，嚎啕大哭，含泪珠，脸红
image side 心愛 心愛_制服_基本_驚き = "images/face/心愛/心愛_制服_基本_驚き.png" # 睁眼，惊讶
image side 心愛 心愛_制服_基本_真顔 = "images/face/心愛/心愛_制服_基本_真顔.png" # 睁眼，嘴闭
image side 心愛 心愛_制服_基本_真顔1 = "images/face/心愛/心愛_制服_基本_真顔1.png" # 睁眼，嘴闭，脸红
image side 心愛 心愛_制服_基本_無表情 = "images/face/心愛/心愛_制服_基本_無表情.png" # 字面意思，睁眼，嘴·
image side 心愛 心愛_制服_基本_きらきら = "images/face/心愛/心愛_制服_基本_きらきら.png" # 睁眼，嘴⚪三角，眼睛有小星星，这属于是馋哭了
image side 心愛 心愛_制服_基本_ぶわー = "images/face/心愛/心愛_制服_基本_ぶわー.png" # 闭眼，很有标志性的哭
image side 心愛 心愛_制服_基本_キス = "images/face/心愛/心愛_制服_基本_キス.png" # 闭眼，脸红，kiss准备
# image side 心愛 心愛_制服_基本_ぐるぐる = "images/face/心愛/心愛_制服_基本_ぐるぐる.png" # （被打）晕了
image side 心愛 心愛_制服_基本_嬉しい = "images/face/心愛/心愛_制服_基本_嬉しい.png" # 康起来很喜感的笑
image side 心愛 心愛_制服_基本_嬉しい1 = "images/face/心愛/心愛_制服_基本_嬉しい1.png" # 康起来很喜感的笑，脸红
image side 心愛 心愛_制服_基本_微笑み = "images/face/心愛/心愛_制服_基本_微笑み.png" # 睁眼，微笑
image side 心愛 心愛_制服_基本_微笑み1 = "images/face/心愛/心愛_制服_基本_微笑み1.png" # 睁眼，微笑，脸红
image side 心愛 心愛_制服_基本_ぐるぐる = "images/face/心愛/心愛_制服_基本_ぐるぐる.png" # 眼睛咕哩咕噜转圈圈
image side 心愛 心愛_制服_基本_覚醒02 = "images/face/心愛/心愛_制服_基本_覚醒02.png" # 心爱觉醒，眼睛变成蛇的样子，眼睛微眯
image side 心愛 心愛_制服_基本_まふまふ = "images/face/心愛/心愛_制服_基本_まふまふ.png" # 基于笑顔，闭眼，两个粉椭圆
image side 心愛 心愛_制服_基本_ポカーン = "images/face/心愛/心愛_制服_基本_ポカーン.png" # 心爱翻白眼了

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
image side 心愛 心愛_大_制服_基本_笑顔 = "images/face/心愛/心愛_大_制服_基本_笑顔.png" # 大，睁眼，嘴o

# 水着系列
image side 心愛 心愛_水着_基本_無表情 = "images/face/心愛/心愛_水着_基本_無表情.png" # 字面意思，睁眼，嘴·
image side 心愛 心愛_水着_基本_ポカーン = "images/face/心愛/心愛_水着_基本_ポカーン.png" # 心爱翻白眼了
image side 心愛 心愛_水着_基本_にっこり = "images/face/心愛/心愛_水着_基本_にっこり.png" # 闭眼，微笑
image side 心愛 心愛_水着_基本_笑顔 = "images/face/心愛/心愛_水着_基本_笑顔.png" # 睁眼，嘴o
image side 心愛 心愛_水着_基本_不機嫌 = "images/face/心愛/心愛_水着_基本_不機嫌.png" # 睁眼，嘴-(
image side 心愛 心愛_水着_基本_嬉しい = "images/face/心愛/心愛_水着_基本_嬉しい.png" # 康起来很喜感的笑
image side 心愛 心愛_水着_基本_泣き= "images/face/心愛/心愛_水着_基本_泣き.png" # 睁眼，含泪珠
image side 心愛 心愛_水着_基本_真顔 = "images/face/心愛/心愛_水着_基本_真顔.png" # 睁眼，嘴闭
image side 心愛 心愛_水着_基本_キス = "images/face/心愛/心愛_水着_基本_キス.png" # 闭眼，脸红，kiss准备
image side 心愛 心愛_水着_基本_驚き = "images/face/心愛/心愛_水着_基本_驚き.png" # 睁眼，惊讶
image side 心愛 心愛_水着_基本_ぶわー = "images/face/心愛/心愛_水着_基本_ぶわー.png" # 闭眼，很有标志性的哭
image side 心愛 心愛_水着_基本_ぐるぐる = "images/face/心愛/心愛_水着_基本_ぐるぐる.png" # 眼睛咕哩咕噜转圈圈
image side 心愛 心愛_水着_基本_もぐもぐ = "images/face/心愛/心愛_水着_基本_もぐもぐ.png" # 闭眼，嘴-(，两个粉椭圆，嘛呼嘛呼
image side 心愛 心愛_水着_基本_きらきら = "images/face/心愛/心愛_水着_基本_きらきら.png" # 睁眼，嘴⚪三角，眼睛有小星星，这属于是馋哭了
image side 心愛 心愛_水着_基本_号泣 = "images/face/心愛/心愛_水着_基本_号泣.png" # 闭眼，嚎啕大哭，含泪珠，脸红
image side 心愛 心愛_水着_基本_微笑み = "images/face/心愛/心愛_水着_基本_微笑み.png" # 睁眼，微笑
image side 心愛 心愛_水着_基本_まふまふ = "images/face/心愛/心愛_水着_基本_まふまふ.png" # 基于笑顔，闭眼，两个粉椭圆
image side 心愛 心愛_水着_基本_ニタァ = "images/face/心愛/心愛_水着_基本_ニタァ.png" # 睁眼，嘴开口，“w”，是有点小坏的笑呢，两个粉椭圆

# 水着_奶糖苹果系列
image side 心愛 心愛_水着_おやつ_もぐもぐ = "images/face/心愛/心愛_水着_おやつ_もぐもぐ.png" # 闭眼，嘴-(，两个粉椭圆，嘛呼嘛呼
image side 心愛 心愛_水着_おやつ_笑顔 = "images/face/心愛/心愛_水着_おやつ_笑顔.png" # 睁眼，嘴o，拿着奶糖苹果

# 下着（内衣）系列
image side 心愛 心愛_下着_基本_ポカーン = "images/face/心愛/心愛_下着_基本_ポカーン.png" # 心爱翻白眼了
image side 心愛 心愛_下着_基本_まふまふ = "images/face/心愛/心愛_下着_基本_まふまふ.png" # 基于笑顔，闭眼，两个粉椭圆
image side 心愛 心愛_下着_基本_驚き = "images/face/心愛/心愛_下着_基本_驚き.png" # 睁眼，惊讶
image side 心愛 心愛_下着_基本_キス = "images/face/心愛/心愛_下着_基本_キス.png" # 闭眼，脸红，kiss准备

# 裸y衬衫系列
image side 心愛 心愛_yシャツ_パンツ有り_驚き = "images/face/心愛/心愛_yシャツ_パンツ有り_驚き.png" # 睁眼，惊讶
image side 心愛 心愛_yシャツ_パンツ有り_真顔 = "images/face/心愛/心愛_yシャツ_パンツ有り_真顔.png" # 睁眼，嘴闭
image side 心愛 心愛_yシャツ_パンツ有り_不機嫌 = "images/face/心愛/心愛_yシャツ_パンツ有り_不機嫌.png" #心愛_下着_基本_驚き
image side 心愛 心愛_yシャツ_パンツ有り_笑顔 = "images/face/心愛/心愛_yシャツ_パンツ有り_笑顔.png" # 睁眼，嘴o
image side 心愛 心愛_yシャツ_パンツ有り_まふまふ = "images/face/心愛/心愛_yシャツ_パンツ有り_まふまふ.png" # 基于笑顔，闭眼，两个粉椭圆
image side 心愛 心愛_yシャツ_パンツ有り_もぐもぐ = "images/face/心愛/心愛_yシャツ_パンツ有り_もぐもぐ.png" # 闭眼，嘴-(，两个粉椭圆
image side 心愛 心愛_yシャツ_パンツ有り_きらきら = "images/face/心愛/心愛_yシャツ_パンツ有り_きらきら.png" # 睁眼，嘴⚪三角，眼睛有小星星，这属于是馋哭了
image side 心愛 心愛_yシャツ_パンツ有り_にっこり = "images/face/心愛/心愛_yシャツ_パンツ有り_にっこり.png" # 闭眼，微笑
image side 心愛 心愛_yシャツ_パンツ有り_無表情 = "images/face/心愛/心愛_yシャツ_パンツ有り_無表情.png" # 字面意思，睁眼，嘴·
image side 心愛 心愛_yシャツ_パンツ有り_ぐるぐる = "images/face/心愛/心愛_yシャツ_パンツ有り_ぐるぐる.png" # 眼睛咕哩咕噜转圈圈
image side 心愛 心愛_yシャツ_パンツ有り_キス = "images/face/心愛/心愛_yシャツ_パンツ有り_キス.png" # 闭眼，脸红，kiss准备
image side 心愛 心愛_yシャツ_パンツ有り_ポカーン = "images/face/心愛/心愛_yシャツ_パンツ有り_ポカーン.png" # 心爱翻白眼了

# 私服系列
image side 心愛 心愛_私服_基本_笑顔 = "images/face/心愛/心愛_私服_基本_笑顔.png" # 睁眼，嘴o
image side 心愛 心愛_私服_基本_泣き= "images/face/心愛/心愛_私服_基本_泣き.png" # 睁眼，含泪珠
image side 心愛 心愛_私服_基本_嬉しい = "images/face/心愛/心愛_私服_基本_嬉しい.png" # 康起来很喜感的笑
image side 心愛 心愛_私服_基本_真顔 = "images/face/心愛/心愛_私服_基本_真顔.png" # 睁眼，嘴闭
image side 心愛 心愛_私服_基本_きらきら = "images/face/心愛/心愛_私服_基本_きらきら.png" # 睁眼，嘴⚪三角，眼睛有小星星，这属于是馋哭了
image side 心愛 心愛_私服_基本_ぶわー = "images/face/心愛/心愛_私服_基本_ぶわー.png" # 闭眼，很有标志性的哭
image side 心愛 心愛_私服_基本_にっこり = "images/face/心愛/心愛_私服_基本_にっこり.png" # 闭眼，微笑
image side 心愛 心愛_私服_基本_無表情 = "images/face/心愛/心愛_私服_基本_無表情.png" # 字面意思，睁眼，嘴·
image side 心愛 心愛_私服_基本_ポカーン = "images/face/心愛/心愛_私服_基本_ポカーン.png" # 心爱翻白眼了
image side 心愛 心愛_私服_基本_微笑み = "images/face/心愛/心愛_私服_基本_微笑み.png" # 睁眼，微笑
image side 心愛 心愛_私服_基本_もぐもぐ = "images/face/心愛/心愛_私服_基本_もぐもぐ.png" # 闭眼，嘴-(，两个粉椭圆
image side 心愛 心愛_私服_基本_ニタァ = "images/face/心愛/心愛_私服_基本_ニタァ.png" # 睁眼，嘴开口，“w”，是有点小坏的笑呢，两个粉椭圆
image side 心愛 心愛_私服_基本_驚き = "images/face/心愛/心愛_私服_基本_驚き.png" # 睁眼，惊讶
image side 心愛 心愛_私服_基本_キス = "images/face/心愛/心愛_私服_基本_キス.png" # 闭眼，脸红，kiss准备
image side 心愛 心愛_私服_基本_ぐるぐる = "images/face/心愛/心愛_私服_基本_ぐるぐる.png" # 眼睛咕哩咕噜转圈圈
image side 心愛 心愛_私服_基本_号泣1 = "images/face/心愛/心愛_私服_基本_号泣1.png"
image side 心愛 心愛_私服_基本_不機嫌 = "images/face/心愛/心愛_私服_基本_不機嫌.png" # 睁眼，嘴-(

# 其它
image side 心愛 心愛_トランザム = "images/face/心愛/心愛_トランザム.png" # 全身变红，心爱真·觉醒！
image side 心愛 心愛_ラフ = "images/face/心愛/心愛_ラフ.png" # 粗线条描绘的心爱酱
image side 心愛 心愛_制服_基本_覚醒 = "images/face/心愛/心愛_制服_基本_覚醒.png" # 基于无表情，眼睛深红
image side 心愛 心愛_制服_基本_覚醒01 = "images/face/心愛/心愛_制服_基本_覚醒01.png" # 基于真顔，眼睛深红
image side 心愛 心愛_下着_基本_覚醒3 = "images/face/心愛/心愛_下着_基本_覚醒3.png" # 基于真顔，眼睛深红，需要注意和别的很像，睫毛是"-""
image side 心愛 心愛_制服_基本_ペコちゃん = "images/face/心愛/心愛_制服_基本_ペコちゃん.png" # 心爱奇奇怪怪的表情，有点像小丑的感觉
image side 心愛 心愛_制服_基本_ゴルゴ = "images/face/心愛/心愛_制服_基本_ゴルゴ.png" # 心爱奇奇怪怪的表情，暴漫风
image side 心愛 心愛_水着_基本_ゴルゴ = "images/face/心愛/心愛_水着_基本_ゴルゴ.png" # 心爱奇奇怪怪的表情，暴漫风
image side 心愛 心愛_水着_基本_覚醒 = "images/face/心愛/心愛_水着_基本_覚醒.png" # 基于无表情，眼睛深红
image side 心愛 心愛_水着_基本_ペコちゃん = "images/face/心愛/心愛_水着_基本_ペコちゃん.png" # 心爱奇奇怪怪的表情，有点像小丑的感觉
image side 心愛 心愛_私服_基本_覚醒03 = "images/face/心愛/心愛_私服_基本_覚醒03.png" # 基于真顔，眼睛深红，需要注意和别的很像，睫毛是"-""
image side 心愛 心愛_私服_基本_覚醒04 = "images/face/心愛/心愛_私服_基本_覚醒04.png" # 基于真顔，眼睛深红，需要注意和别的很像，睫毛是"-""

# 特殊
image side 心愛 心愛_通話中 = "images/face/心愛/心愛_通話中.png" # 装在携带里面的真冬

# 没有表情，所以不指定 image
define lian_ai = Character("莲&心爱",color="#ffc9be",image="心愛")

# 真冬&心爱 心爱和真冬共同出现，因为头像是真冬的所以用真冬的颜色
##　只需要指定　image="心爱"　，不需要单独指定表情了
define dong_ai =  Character('真冬&心爱',color="#ffc9be",image="心愛")

# 心爱A
define aia =  Character('心爱A',color="#ffc9be",image="心愛A")
image side 心愛A 心愛A_水着_基本_笑顔 = "images/face/心愛A/心愛A_水着_基本_笑顔.png" # 睁眼，嘴o
image 心愛A_水着_基本_笑顔 = "images/face/心愛A/心愛A_水着_基本_笑顔.png" # 睁眼，嘴o

# 心爱B
define aib =  Character('心爱B',color="#ffc9be",image="心愛B")
image side 心愛B 心愛B_水着_基本_笑顔 = "images/face/心愛B/心愛B_水着_基本_笑顔.png" # 睁眼，嘴o
image 心愛B_水着_基本_笑顔 = "images/face/心愛B/心愛B_水着_基本_笑顔.png" # 睁眼，嘴o

# 心爱AB
define aiab =  Character('心爱AB',color="#ffc9be",image="心愛AB")
image side 心愛AB 心愛AB_水着_基本_笑顔 = "images/face/心愛AB/心愛AB_水着_基本_笑顔.png" # 睁眼，嘴o
image 心愛AB_水着_基本_笑顔 = "images/face/心愛AB/心愛AB_水着_基本_笑顔.png" # 睁眼，嘴o

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

# 常服_普通系列
image side 真冬 真冬_制服_基本_無表情 = "images/face/真冬/真冬_制服_基本_無表情.png" # 字面意思，睁眼，嘴·
image side 真冬 真冬_制服_基本_むーっ = "images/face/真冬/真冬_制服_基本_むーっ.png" # 闭眼，撅嘴，眉毛y=-x（斜下45度）
image side 真冬 真冬_制服_基本_ジト目 = "images/face/真冬/真冬_制服_基本_ジト目.png" # 睁眼，嘴三角，眉上凸
image side 真冬 真冬_制服_基本_本気2 = "images/face/真冬/真冬_制服_基本_本気2.png" # 眼睁大，眉毛y=-x，嘴o
image side 真冬 真冬_制服_基本_微笑み = "images/face/真冬/真冬_制服_基本_微笑み.png" # 字面意思
image side 真冬 真冬_制服_基本_微笑み_1 = "images/face/真冬/真冬_制服_基本_微笑み_1.png" # 字面意思，脸红
image side 真冬 真冬_制服_基本_微笑み2 = "images/face/真冬/真冬_制服_基本_微笑み2.png" # 字面意思，嘴型近“o”
image side 真冬 真冬_制服_基本_目閉じ = "images/face/真冬/真冬_制服_基本_目閉じ.png" # 闭眼，嘴·
image side 真冬 真冬_制服_基本_目閉じ_1 = "images/face/真冬/真冬_制服_基本_目閉じ_1.png"
image side 真冬 真冬_制服_基本_泣き = "images/face/真冬/真冬_制服_基本_泣き.png" # 睁眼，含泪珠
image side 真冬 真冬_制服_基本_泣き_1 = "images/face/真冬/真冬_制服_基本_泣き_1.png"
image side 真冬 真冬_制服_基本_見下し = "images/face/真冬/真冬_制服_基本_見下し.png" # 闭眼，眉毛y=-x，嘴o
image side 真冬 真冬_制服_基本_見下し2 = "images/face/真冬/真冬_制服_基本_見下し2.png"
image side 真冬 真冬_制服_基本_見下し3 = "images/face/真冬/真冬_制服_基本_見下し3.png" # 眼睁大，眉毛y=-x，嘴-，非常生气
image side 真冬 真冬_制服_基本_見下し4 = "images/face/真冬/真冬_制服_基本_見下し4.png" # 眼睁大，眉毛略微向下，嘴-，不高兴
image side 真冬 真冬_制服_基本_にっこり = "images/face/真冬/真冬_制服_基本_にっこり.png" # 闭眼，微笑
image side 真冬 真冬_制服_基本_にっこり_1 = "images/face/真冬/真冬_制服_基本_にっこり_1.png"
image side 真冬 真冬_制服_基本_まったり = "images/face/真冬/真冬_制服_基本_まったり.png" # 闭眼，嘴“w”，嘛呼嘛呼
image side 真冬 真冬_制服_基本_おやつ1 = "images/face/真冬/真冬_制服_基本_おやつ1.png" # 闭眼，嘴“w”，拿着奶糖苹果
image side 真冬 真冬_制服_基本_おやつ2 = "images/face/真冬/真冬_制服_基本_おやつ2.png" # 闭眼，嘴开口，“w”，是有点小坏的笑呢，拿着奶糖苹果
image side 真冬 真冬_制服_基本_おやつ3 = "images/face/真冬/真冬_制服_基本_おやつ3.png" # 闭眼，嘴开口，椭圆，是有点小萌的笑呢，拿着奶糖苹果
image side 真冬 真冬_制服_基本_ニタァ = "images/face/真冬/真冬_制服_基本_ニタァ.png" # 睁眼，嘴开口，“w”，是有点小坏的笑呢
# https://github.com/luckykeeper/LOVE69_renpy_remaster/issues/2 04
image side 真冬 真冬_制服_基本_居眠り = "images/face/真冬/真冬_制服_基本_居眠り.png" # 闭眼，嘴开口，半圆，碎着辽~
image side 真冬 真冬_制服_基本_キス = "images/face/真冬/真冬_制服_基本_キス.png" # kiss准备
image side 真冬 真冬_制服_基本_号泣 = "images/face/真冬/真冬_制服_基本_号泣.png" # 闭眼，嘴开口，圆，嚎啕大哭
image side 真冬 真冬_制服_基本_号泣_1 = "images/face/真冬/真冬_制服_基本_号泣_1.png" # 闭眼，嘴开口，圆，嚎啕大哭，脸红
image side 真冬 真冬_制服_基本_本気2 = "images/face/真冬/真冬_制服_基本_本気2.png" # 眼睁大，嘴开口，圆，发火
image side 真冬 真冬_制服_基本_嬉しい = "images/face/真冬/真冬_制服_基本_嬉しい.png" # # 康起来很喜感的笑

# 裸y衬衫系列
image side 真冬 真冬_裸yシャツ_基本_無表情 = "images/face/真冬/真冬_裸yシャツ_基本_無表情.png" # 字面意思，睁眼，嘴·
image side 真冬 真冬_裸yシャツ_基本_まったり = "images/face/真冬/真冬_裸yシャツ_基本_まったり.png" # 闭眼，嘴“w”，嘛呼嘛呼
image side 真冬 真冬_裸yシャツ_基本_目閉じ = "images/face/真冬/真冬_裸yシャツ_基本_目閉じ.png" # 闭眼，嘴·
image side 真冬 真冬_裸yシャツ_基本_微笑み = "images/face/真冬/真冬_裸yシャツ_基本_微笑み.png" # 字面意思
image side 真冬 真冬_裸yシャツ_基本_居眠り = "images/face/真冬/真冬_裸yシャツ_基本_居眠り.png" # 闭眼，嘴开口，半圆，碎着辽~
image side 真冬 真冬_裸yシャツ_基本_ジト目 = "images/face/真冬/真冬_裸yシャツ_基本_ジト目.png" # 睁眼，嘴三角，眉上凸
image side 真冬 真冬_裸yシャツ_基本_微笑み2 = "images/face/真冬/真冬_裸yシャツ_基本_微笑み2.png" # 字面意思，嘴型近“o”
image side 真冬 真冬_裸yシャツ_基本_見下し = "images/face/真冬/真冬_裸yシャツ_基本_見下し.png" # 闭眼，眉毛y=-x，嘴o
image side 真冬 真冬_裸yシャツ_基本_むーっ = "images/face/真冬/真冬_裸yシャツ_基本_むーっ.png" # 闭眼，撅嘴，眉毛y=-x（斜下45度）
image side 真冬 真冬_裸yシャツ_基本_見下し3 = "images/face/真冬/真冬_裸yシャツ_基本_見下し3.png" # 睁眼，生气，嘴-，眉毛y=-x（斜下45度）
image side 真冬 真冬_裸yシャツ_基本_泣き = "images/face/真冬/真冬_裸yシャツ_基本_泣き.png" # 睁眼，含泪珠
image side 真冬 真冬_裸yシャツ_基本_本気 = "images/face/真冬/真冬_裸yシャツ_基本_本気.png" # 眼睁大，眉毛y=-x,嘴闭
image side 真冬 真冬_裸yシャツ_基本_キス = "images/face/真冬/真冬_裸yシャツ_基本_キス.png" # kiss准备
image side 真冬 真冬_裸yシャツ_基本_ニタァ = "images/face/真冬/真冬_裸yシャツ_基本_ニタァ.png" # 睁眼，嘴开口，“w”，是有点小坏的笑呢

# 大_常服
image side 真冬 真冬_大_制服_基本_キス = "images/face/真冬/真冬_大_制服_基本_キス.png" # 大，kiss准备
image side 真冬 真冬_大_制服_基本_微笑み = "images/face/真冬/真冬_大_制服_基本_微笑み.png" # 大，字面意思

# 私服系列
image side 真冬 真冬_私服_基本_まったり = "images/face/真冬/真冬_私服_基本_まったり.png" # 闭眼，嘴“w”，嘛呼嘛呼
image side 真冬 真冬_私服_基本_無表情 = "images/face/真冬/真冬_私服_基本_無表情.png" # 字面意思，睁眼，嘴·
image side 真冬 真冬_私服_基本_微笑み = "images/face/真冬/真冬_私服_基本_微笑み.png" # 字面意思
image side 真冬 真冬_私服_基本_目閉じ = "images/face/真冬/真冬_私服_基本_目閉じ.png" # 闭眼，嘴·
image side 真冬 真冬_私服_基本_ジト目 = "images/face/真冬/真冬_私服_基本_ジト目.png" # 睁眼，嘴三角，眉上凸
image side 真冬 真冬_私服_基本_キス = "images/face/真冬/真冬_私服_基本_キス.png" # kiss准备
image side 真冬 真冬_私服_基本_嬉しい = "images/face/真冬/真冬_私服_基本_嬉しい.png" # # 康起来很喜感的笑
image side 真冬 真冬_私服_基本_ニタァ = "images/face/真冬/真冬_私服_基本_ニタァ.png" # 睁眼，嘴开口，“w”，是有点小坏的笑呢
image side 真冬 真冬_私服_基本_にっこり_1 = "images/face/真冬/真冬_私服_基本_にっこり_1.png"
image side 真冬 真冬_私服_基本_居眠り = "images/face/真冬/真冬_私服_基本_居眠り.png" # 闭眼，嘴开口，半圆，碎着辽~
image side 真冬 真冬_私服_基本_にっこり = "images/face/真冬/真冬_私服_基本_にっこり.png"
image side 真冬 真冬_私服_基本_微笑み2_1 = "images/face/真冬/真冬_私服_基本_微笑み2_1.png"
image side 真冬 真冬_私服_基本_ジト目3_1 = "images/face/真冬/真冬_私服_基本_ジト目3_1.png"
image side 真冬 真冬_私服_基本_本気2 = "images/face/真冬/真冬_私服_基本_本気2.png"

# 大_私服
image side 真冬 真冬_大_私服_基本_キス = "images/face/真冬/真冬_大_私服_基本_キス.png" # 大，kiss准备
image side 真冬 真冬_大_私服_基本_ジト目 = "images/face/真冬/真冬_大_私服_基本_ジト目.png" # 大，睁眼，嘴三角，眉上凸
image side 真冬 真冬_大_私服_基本_微笑み = "images/face/真冬/真冬_大_私服_基本_微笑み.png" # 大，字面意思
image side 真冬 真冬_大_私服_基本_目閉じ = "images/face/真冬/真冬_大_私服_基本_目閉じ.png" # 闭眼，嘴·

# 下着（内衣）系列
image side 真冬 真冬_下着_基本_キス = "images/face/真冬/真冬_下着_基本_キス.png" # 闭眼，脸红，kiss准备
image side 真冬 真冬_下着_基本_微笑み = "images/face/真冬/真冬_下着_基本_微笑み.png" # 字面意思
image side 真冬 真冬_下着_基本_微笑み_1 = "images/face/真冬/真冬_下着_基本_微笑み_1.png" # 字面意思，脸红

# 水着系列
image side 真冬 真冬_水着_基本_まったり = "images/face/真冬/真冬_水着_基本_まったり.png" # 闭眼，嘴“w”，嘛呼嘛呼
image side 真冬 真冬_水着_基本_微笑み = "images/face/真冬/真冬_水着_基本_微笑み.png" # 字面意思
image side 真冬 真冬_水着_基本_無表情 = "images/face/真冬/真冬_水着_基本_無表情.png" # 字面意思，睁眼，嘴·
image side 真冬 真冬_水着_基本_目閉じ = "images/face/真冬/真冬_水着_基本_目閉じ.png" # 闭眼，嘴·
image side 真冬 真冬_水着_基本_ジト目 = "images/face/真冬/真冬_水着_基本_ジト目.png" # 睁眼，嘴三角，眉上凸
image side 真冬 真冬_水着_基本_キス = "images/face/真冬/真冬_水着_基本_キス.png" # kiss准备
image side 真冬 真冬_水着_基本_泣き = "images/face/真冬/真冬_水着_基本_泣き.png" # 睁眼，含泪珠
image side 真冬 真冬_水着_基本_号泣 = "images/face/真冬/真冬_水着_基本_号泣.png" # 闭眼，嘴开口，圆，嚎啕大哭
image side 真冬 真冬_水着_基本_嬉しい = "images/face/真冬/真冬_水着_基本_嬉しい.png" # # 康起来很喜感的笑
image side 真冬 真冬_水着_基本_本気 = "images/face/真冬/真冬_水着_基本_本気.png" # 眼睁大，眉毛y=-x,嘴闭
image side 真冬 真冬_水着_基本_にっこり = "images/face/真冬/真冬_水着_基本_にっこり.png" # 闭眼，微笑
image side 真冬 真冬_水着_基本_ニタァ = "images/face/真冬/真冬_水着_基本_ニタァ.png" # 睁眼，嘴开口，“w”，是有点小坏的笑呢

# 水着_奶糖苹果系列
image side 真冬 真冬_水着_基本_おやつ = "images/face/真冬/真冬_水着_基本_おやつ.png" # 拿着奶糖苹果，嘛呼嘛呼

# 其它
image side 真冬 真冬_通話中 = "images/face/真冬/真冬_通話中.png" # 装在携带里面的真冬
image side 真冬 真冬_制服_中指_見下し_1 = "images/face/真冬/真冬_制服_中指_見下し_1.png"

# 心爱&真冬 心爱和真冬共同出现，以为头像是真冬的所以用真冬的颜色
##　只需要指定　image="真冬"　，不需要单独指定表情了
define ai_dong =  Character('心爱&真冬',color="#4da8c0",image="真冬")

# 三人 （（莲）心爱真冬想瑠）
define lianaidong =  Character('三人',color="#4da8c0",image="真冬")

# 莲・真冬
define lian_dong =  Character('莲・真冬',color="#4da8c0",image="真冬")

# みんな（大伙）
define aio_dong = Character('大伙',color="#4da8c0",image="真冬")

# 葛城莲 lian //主人公，工具人就不要加颜色了吧，不加颜色的统一强制指定白色（#ffffff）
define lian = Character('莲',color="#ffffff")

# 里昂·麦克斯韦 lion //和原版相比，移植版打算在人物名上加入颜色，里昂的颜色是摘掉帽子之后在头顶上取的
define lion = Character('里昂',color="#fff7bb",image="リオン")

# 定义里昂的立绘
# 显示在画面中的

# 常服_帽子_杖系列
image side リオン リオン_基本_杖_微笑み = "images/face/リオン/リオン_基本_杖_微笑み.png" # 睁眼，有帽子，拿杖，微笑
image side リオン リオン_基本_杖_微笑み_1 = "images/face/リオン/リオン_基本_杖_微笑み_1.png" # 睁眼，有帽子，拿杖，微笑
image side リオン リオン_基本_杖_にっこり = "images/face/リオン/リオン_基本_杖_にっこり.png" # 闭眼，有帽子，拿杖，微笑
image side リオン リオン_基本_杖_にっこり_1 = "images/face/リオン/リオン_基本_杖_にっこり_1.png" # 闭眼，有帽子，拿杖，微笑
image side リオン リオン_基本_杖_嬉しい = "images/face/リオン/リオン_基本_杖_嬉しい.png" # 闭眼，有帽子，拿杖，喜
image side リオン リオン_基本_杖_ジト目 = "images/face/リオン/リオン_基本_杖_ジト目.png" # 睁眼，有帽子，拿杖，皱眉，嘴倒三角
image side リオン リオン_基本_杖_ジト目_1 = "images/face/リオン/リオン_基本_杖_ジト目_1.png" # 睁眼，有帽子，拿杖，皱眉，嘴倒三角
image side リオン リオン_基本_杖_ニタァ = "images/face/リオン/リオン_基本_杖_ニタァ.png" # 睁眼，有帽子，拿杖，皱眉，嘴半圆，是有点小坏的笑呢
image side リオン リオン_基本_杖_驚き = "images/face/リオン/リオン_基本_杖_驚き.png" # 睁眼，有帽子，拿杖，惊讶
image side リオン リオン_基本_杖_驚き_1 = "images/face/リオン/リオン_基本_杖_驚き_1.png" # 睁眼，有帽子，拿杖，惊讶
image side リオン リオン_基本_杖_悲しい = "images/face/リオン/リオン_基本_杖_悲しい.png" # 睁眼，有帽子，拿杖，悲，嘴小开口
image side リオン リオン_基本_杖_悲しい2 = "images/face/リオン/リオン_基本_杖_悲しい2.png" # 睁眼，有帽子，拿杖，悲，嘴一条缝
image side リオン リオン_基本_杖_無表情 = "images/face/リオン/リオン_基本_杖_無表情.png" # 睁眼，有帽子，拿杖，莫得感情
image side リオン リオン_基本_杖_無表情_1 = "images/face/リオン/リオン_基本_杖_無表情_1.png" # 睁眼，有帽子，拿杖，莫得感情
image side リオン リオン_基本_杖_見下し = "images/face/リオン/リオン_基本_杖_見下し.png" # 睁眼，有帽子，拿杖，嘴三角圆
image side リオン リオン_基本_杖_ぶわー = "images/face/リオン/リオン_基本_杖_ぶわー.png" # 睁眼，有帽子，拿杖，是和心爱一样标志性的哭呢
image side リオン リオン_基本_杖_キス = "images/face/リオン/リオン_基本_杖_キス.png" # 睁眼，有帽子，拿杖，kiss

# 常服_帽子_杖_大系列
image side リオン リオン_大_基本_杖_キス = "images/face/リオン/リオン_大_基本_杖_キス.png" # 睁眼，有帽子，拿杖，kiss

# 常服_没帽子_杖系列
image side リオン リオン_帽子無し_杖_にっこり = "images/face/リオン/リオン_帽子無し_杖_にっこり.png" # 闭眼，拿杖，微笑
image side リオン リオン_帽子無し_杖_微笑み = "images/face/リオン/リオン_帽子無し_杖_微笑み.png" # 睁眼，没帽子，拿杖，微笑
image side リオン リオン_帽子無し_杖_ジト目 = "images/face/リオン/リオン_帽子無し_杖_ジト目.png" # 睁眼，没帽子，拿杖，皱眉，嘴倒三角
image side リオン リオン_帽子無し_杖_ニタァ = "images/face/リオン/リオン_帽子無し_杖_ニタァ.png" # 睁眼，没帽子，拿杖，皱眉，嘴半圆，是有点小坏的笑呢
image side リオン リオン_帽子無し_杖_驚き = "images/face/リオン/リオン_帽子無し_杖_ニタァ.png" # 睁眼，没帽子，拿杖，惊讶
image side リオン リオン_帽子無し_杖_悲しい = "images/face/リオン/リオン_帽子無し_杖_悲しい.png" # 睁眼，没帽子，拿杖，悲，嘴小开口
image side リオン リオン_帽子無し_杖_無表情_1 = "images/face/リオン/リオン_帽子無し_杖_無表情_1.png" # 睁眼，拿杖，莫得感情
image side リオン リオン_帽子無し_杖_悲しい2 = "images/face/リオン/リオン_帽子無し_杖_悲しい2.png" # 睁眼，拿杖，悲，嘴一条缝
image side リオン リオン_帽子無し_杖_ぶわー = "images/face/リオン/リオン_帽子無し_杖_ぶわー.png" # 睁眼，拿杖，是和心爱一样标志性的哭呢
image side リオン リオン_帽子無し_杖_嬉しい = "images/face/リオン/リオン_帽子無し_杖_嬉しい.png" # 闭眼，有帽子，拿杖，喜
image side リオン リオン_帽子無し_杖_にっこり_1 = "images/face/リオン/リオン_帽子無し_杖_にっこり_1.png" # 闭眼，有帽子，拿杖，微笑

# 常服_没帽子_没杖系列
image side リオン リオン_帽子無し_杖なし_微笑み = "images/face/リオン/リオン_帽子無し_杖なし_微笑み.png" # 睁眼，没帽子，没杖，微笑
image side リオン リオン_帽子無し_杖なし_微笑み_1 = "images/face/リオン/リオン_帽子無し_杖なし_微笑み_1.png" # 睁眼，有帽子，拿杖，微笑
image side リオン リオン_帽子無し_杖なし_驚き = "images/face/リオン/リオン_帽子無し_杖なし_驚き.png" # 睁眼，没帽子，拿杖，惊讶
image side リオン リオン_帽子無し_杖なし_無表情_1 = "images/face/リオン/リオン_帽子無し_杖なし_無表情_1.png" # 睁眼，拿杖，莫得感情
image side リオン リオン_帽子無し_杖なし_ジト目 = "images/face/リオン/リオン_帽子無し_杖なし_ジト目.png" # 睁眼，没帽子，拿杖，皱眉，嘴倒三角
image side リオン リオン_帽子無し_杖なし_見下し = "images/face/リオン/リオン_帽子無し_杖なし_見下し.png" # 睁眼，有帽子，拿杖，嘴三角圆
image side リオン リオン_帽子無し_杖なし_悲しい2 = "images/face/リオン/リオン_帽子無し_杖なし_悲しい2.png" # 睁眼，拿杖，悲，嘴一条缝
image side リオン リオン_帽子無し_杖なし_悲しい2_1 = "images/face/リオン/リオン_帽子無し_杖なし_悲しい2_1.png" # 睁眼，拿杖，悲，嘴一条缝
image side リオン リオン_帽子無し_杖なし_嬉しい = "images/face/リオン/リオン_帽子無し_杖なし_嬉しい.png" # 闭眼，有帽子，拿杖，喜
image side リオン リオン_帽子無し_杖なし_嬉しい_1 = "images/face/リオン/リオン_帽子無し_杖なし_嬉しい_1.png" # 闭眼，有帽子，拿杖，喜
image side リオン リオン_帽子無し_杖なし_驚き_1 = "images/face/リオン/リオン_帽子無し_杖なし_驚き_1.png" # 睁眼，惊讶
image side リオン リオン_帽子無し_杖なし_ニタァ = "images/face/リオン/リオン_帽子無し_杖なし_ニタァ.png" # 睁眼，没帽子，拿杖，皱眉，嘴半圆，是有点小坏的笑呢
image side リオン リオン_帽子無し_杖なし_キス = "images/face/リオン/リオン_帽子無し_杖なし_キス.png" # 睁眼，有帽子，拿杖，kiss
image side リオン リオン_帽子無し_杖なし_にっこり_1 = "images/face/リオン/リオン_帽子無し_杖なし_にっこり_1.png" # 闭眼，微笑

# 常服_帽子_没杖系列
image side リオン リオン_基本_杖なし_無表情 = "images/face/リオン/リオン_基本_杖なし_無表情.png" # 睁眼，有帽子，拿杖，莫得感情
image side リオン リオン_基本_杖なし_微笑み = "images/face/リオン/リオン_基本_杖なし_微笑み.png" # 睁眼，没帽子，没杖，微笑
image side リオン リオン_基本_杖なし_ニタァ = "images/face/リオン/リオン_基本_杖なし_ニタァ.png" # 睁眼，没帽子，拿杖，皱眉，嘴半圆，是有点小坏的笑呢
image side リオン リオン_基本_杖なし_キス = "images/face/リオン/リオン_基本_杖なし_キス.png" # 睁眼，有帽子，拿杖，kiss
image side リオン リオン_基本_杖なし_嬉しい = "images/face/リオン/リオン_基本_杖なし_嬉しい.png" # 闭眼，有帽子，拿杖，喜
image side リオン リオン_基本_杖なし_驚き = "images/face/リオン/リオン_基本_杖なし_驚き.png" # 睁眼，没帽子，拿杖，惊讶
# image side リオン リオン_基本_杖なし_にっこり = "images/face/リオン/リオン_基本_杖なし_にっこり.png" # 闭眼，拿杖，微笑
image side リオン リオン_基本_杖なし_微笑み_1 = "images/face/リオン/リオン_基本_杖なし_微笑み_1.png" # 睁眼，有帽子，拿杖，微笑
image side リオン リオン_基本_杖なし_にっこり_1 = "images/face/リオン/リオン_基本_杖なし_にっこり_1.png" # 闭眼，拿杖，微笑
image side リオン リオン_基本_杖なし_にっこり = "images/face/リオン/リオン_基本_杖なし_にっこり.png" # 闭眼，拿杖，微笑
image side リオン リオン_基本_杖なし_無表情_1 = "images/face/リオン/リオン_基本_杖なし_無表情_1.png" # 睁眼，有帽子，拿杖，莫得感情
image side リオン リオン_基本_杖なし_悲しい2_1 = "images/face/リオン/リオン_基本_杖なし_悲しい2_1.png" # 睁眼，悲，嘴小开口
image side リオン リオン_基本_杖なし_ジト目 = "images/face/リオン/リオン_基本_杖なし_ジト目.png" # 睁眼，没帽子，拿杖，皱眉，嘴倒三角
image side リオン リオン_基本_杖なし_見下し = "images/face/リオン/リオン_基本_杖なし_見下し.png" # 睁眼，有帽子，拿杖，嘴三角圆

# 私服系列
image side リオン リオン_私服_基本_ジト目 = "images/face/リオン/リオン_私服_基本_ジト目.png" # 睁眼，皱眉，嘴倒三角
image side リオン リオン_私服_基本_にっこり = "images/face/リオン/リオン_私服_基本_にっこり.png" # 闭眼，微笑
image side リオン リオン_私服_基本_にっこり_1 = "images/face/リオン/リオン_私服_基本_にっこり_1.png" # 闭眼，微笑
image side リオン リオン_私服_基本_嬉しい = "images/face/リオン/リオン_私服_基本_嬉しい.png" # 闭眼，喜
image side リオン リオン_私服_基本_嬉しい_1 = "images/face/リオン/リオン_私服_基本_嬉しい_1.png" # 闭眼，喜
image side リオン リオン_私服_基本_驚き = "images/face/リオン/リオン_私服_基本_驚き.png" # 睁眼，惊讶
image side リオン リオン_私服_基本_驚き_1 = "images/face/リオン/リオン_私服_基本_驚き_1.png" # 睁眼，惊讶
image side リオン リオン_私服_基本_ニタァ = "images/face/リオン/リオン_私服_基本_ニタァ.png" # 睁眼，皱眉，嘴半圆，是有点小坏的笑呢
image side リオン リオン_私服_基本_ニタァ_1 = "images/face/リオン/リオン_私服_基本_ニタァ_1.png" # 睁眼，皱眉，嘴半圆，是有点小坏的笑呢
image side リオン リオン_私服_基本_微笑み = "images/face/リオン/リオン_私服_基本_微笑み.png" # 睁眼，微笑
image side リオン リオン_私服_基本_微笑み_1 = "images/face/リオン/リオン_私服_基本_微笑み_1.png" # 睁眼，有帽子，拿杖，微笑
image side リオン リオン_私服_基本_悲しい = "images/face/リオン/リオン_私服_基本_悲しい.png" # 睁眼，悲，嘴小开口
image side リオン リオン_私服_基本_悲しい2 = "images/face/リオン/リオン_私服_基本_悲しい2.png" # 睁眼，悲，嘴小开口
image side リオン リオン_私服_基本_悲しい2_1 = "images/face/リオン/リオン_私服_基本_悲しい2_1.png" # 睁眼，悲，嘴小开口
image side リオン リオン_私服_基本_無表情 = "images/face/リオン/リオン_私服_基本_無表情.png" # 睁眼，有帽子，拿杖，莫得感情
image side リオン リオン_私服_基本_無表情_1 = "images/face/リオン/リオン_私服_基本_無表情_1.png" # 睁眼，莫得感情
image side リオン リオン_私服_基本_ジト目_1 = "images/face/リオン/リオン_私服_基本_ジト目_1.png" # 睁眼，没拿杖，皱眉，嘴倒三角
image side リオン リオン_私服_基本_ぶわー = "images/face/リオン/リオン_私服_基本_ぶわー.png" # 睁眼，是和心爱一样标志性的哭呢
image side リオン リオン_私服_基本_見下し = "images/face/リオン/リオン_私服_基本_見下し.png" # 睁眼，有帽子，拿杖，嘴三角圆
image side リオン リオン_私服_基本_キス = "images/face/リオン/リオン_私服_基本_キス.png" # 睁眼，有帽子，拿杖，kiss
image side リオン リオン_私服_基本_キス_1 = "images/face/リオン/リオン_私服_基本_キス_1.png" # 睁眼，有帽子，拿杖，kiss

# 下着（内衣）系列
image side リオン リオン_下着_基本_悲しい2_1 = "images/face/リオン/リオン_下着_基本_悲しい2_1.png" # 睁眼，有帽子，拿杖，悲，嘴一条缝

# 特殊
image side リオン リオン_通話中 = "images/face/リオン/リオン_通話中.png" # 装在携带里面的里昂
image side リオン リオン_大_基本_杖なし_キス = "images/face/リオン/リオン_大_基本_杖なし_キス.png" # 睁眼，有帽子，kiss

# アイス屋（冰淇淋店）（里昂）
define icecreamroom = Character('冰淇淋店',color="#fff7bb",image="リオン")

# 莲&里昂
define lian_lion = Character('莲&里昂',color="#fff7bb",image="リオン")

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
image side 想瑠 想瑠_スーツ_中指 = "images/face/想瑠/想瑠_スーツ_中指.png" # 中指
image side 想瑠 想瑠_スーツ_驚き = "images/face/想瑠/想瑠_スーツ_驚き.png" # 睁眼，震惊
image side 想瑠 想瑠_スーツ_照れ = "images/face/想瑠/想瑠_スーツ_照れ.png" # 睁眼，微笑，脸红

# 想瑠 in hotdog?!
define hotdog = Character('热狗',color="#a4808c",image="想瑠")
image side 想瑠 想瑠_hot_ニヤリ = "images/face/想瑠/想瑠_hot_ニヤリ.png" # 睁眼，嘴“w”，手撑头，两个粉椭圆
image side 想瑠 想瑠_hot_見下し = "images/face/想瑠/想瑠_hot_見下し.png" # 睁眼，嘴椭圆小开口，手撑头
image side 想瑠 想瑠_hot_驚き = "images/face/想瑠/想瑠_hot_驚き.png" # 睁眼，震惊
image side 想瑠 想瑠_hot_ぶわ = "images/face/想瑠/想瑠_hot_ぶわ.png" # 是和心爱一样标志性的哭

image side 想瑠 想瑠_風呂_ぐるぐる = "images/face/想瑠/想瑠_風呂_ぐるぐる.png" # 马赛克想瑠

# 月宫瑠那 na //和原版相比，移植版打算在人物名上加入颜色，瑠那的颜色是从头发中间取的（之前取错了233）
define na = Character('瑠那',color="#ffedb5",image="瑠那")
image side 瑠那 瑠那_私服_にっこり = "images/face/瑠那/瑠那_私服_にっこり.png" # 闭眼，微笑
image side 瑠那 瑠那_私服_きらきら = "images/face/瑠那/瑠那_私服_きらきら.png" # 睁眼，嘴⚪三角，眼睛有小星星
image side 瑠那 瑠那_私服_真顔 = "images/face/瑠那/瑠那_私服_真顔.png" # 睁眼，嘴闭
image side 瑠那 瑠那_私服_微笑 = "images/face/瑠那/瑠那_私服_微笑.png" # 睁眼，微笑
# 瑠那_私服_微笑み 小头像不能识别，改为上面这样
image side 瑠那 瑠那_私服_はう = "images/face/瑠那/瑠那_私服_はう.png" # 闭眼，眼睛多条黑线
image side 瑠那 瑠那_私服_驚き = "images/face/瑠那/瑠那_私服_驚き.png" # 睁眼，嘴⚪，惊Σ(っ °Д °;)っ
image side 瑠那 瑠那_私服_笑顔 = "images/face/瑠那/瑠那_私服_笑顔.png"
image side 瑠那 瑠那_私服_悲しみ = "images/face/瑠那/瑠那_私服_悲しみ.png"

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
image side 店长 店长_私服_にっこり = "images/face/店长/店长_私服_にっこり.png" # 闭眼，微笑，手撑头
image side 店长 店长_私服_にっこり_1 = "images/face/店长/店长_私服_にっこり_1.png" # 闭眼，微笑，手撑头
image side 店长 店长_私服_本気 = "images/face/店长/店长_私服_本気.png" # 睁眼，嘴o，手撑头
image side 店长 店长_私服_本気_1 = "images/face/店长/店长_私服_本気_1.png" # 睁眼，嘴o，手撑头
image side 店长 店长_私服_ニヤリ = "images/face/店长/店长_私服_ニヤリ.png" # 睁眼，手撑头，是有点小坏的笑呢
image side 店长 店长_私服_ニヤリ_1 = "images/face/店长/店长_私服_ニヤリ_1.png" # 睁眼，手撑头，是有点小坏的笑呢，脸红
image side 店长 店长_私服_無表情 = "images/face/店长/店长_私服_無表情.png" # 睁眼，手撑头，闭嘴，莫得感情
image side 店长 店长_私服_ジト目 = "images/face/店长/店长_私服_ジト目.png" # 睁眼，手撑头，嘴椭圆，一脸正经
image side 店长 店长_私服_不満_1 = "images/face/店长/店长_私服_不満_1.png" # 睁眼，手撑头，闭嘴，不高兴，脸红
image side 店长 店长_私服_不満 = "images/face/店长/店长_私服_不満.png" # 睁眼，手撑头，闭嘴，不高兴
image side 店长 店长_私服_見下し = "images/face/店长/店长_私服_見下し.png" # 睁眼，有点小坏的笑但是又不小坏

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
image side アシュリー アシュリー_私服_にっこり = "images/face/アシュリー/アシュリー_私服_にっこり.png" # 闭眼，笑，嘴张大
image side アシュリー アシュリー_私服_無表情 = "images/face/アシュリー/アシュリー_私服_無表情.png" # 字面意思，睁眼，嘴-
image side アシュリー アシュリー_私服_驚き = "images/face/アシュリー/アシュリー_私服_驚き.png" # 睁眼，震惊
image side アシュリー アシュリー_私服_微笑み = "images/face/アシュリー/アシュリー_私服_微笑み.png" # 睁眼，微笑，嘴张大
image side アシュリー アシュリー_私服_困り = "images/face/アシュリー/アシュリー_私服_困り.png" # 泪珠打转
image side アシュリー アシュリー_私服_幸せ = "images/face/アシュリー/アシュリー_私服_幸せ.png" # 类似ニヤリ

# 迈克尔 mj //和原版相比，移植版打算在人物名上加入颜色，帽子就要它本来的颜色就好啦~
define hat = Character('帽子',color="#67435e",image="帽子")
define mj = Character('MJ',color="#67435e",image="MJ")

image side 帽子 帽子_通常 = "images/face/帽子/帽子_通常.png" # 帽子？？？
image side MJ MJ_通常 = "images/face/MJ/MJ_通常.png" # MJ

# 旁白君 bai 不加颜色的统一强制指定白色（#ffffff）
define bai = Character('旁白君',color="#ffffff")

# テしビ tv 不加颜色的统一强制指定白色（#ffffff）
define tv = Character('TV',color="#ffffff",image="リオン")

# 翻译君（我自己） Luckykeeper 用于写长段注释，图标从QQ头像来（要圆的）//译者君的颜色是从个人博客的favion图案里面来哒，和心爱的颜色很像哦~
define luckykeeper = Character('Luckykeeper',color="#ffc0cb")

# ？？？ ??? 给不知道是谁的时候用 不加颜色的统一强制指定白色（#ffffff）
define unknown404 = Character('？？？',color="#ffffff",image="unknown404")

# wsa 女学生A （Woman Student A） 不加颜色的统一强制指定白色（#ffffff）
define wsa = Character('女学生A',color="#ffffff")

# wsa 女学生B （Woman Student B） 不加颜色的统一强制指定白色（#ffffff）
define wsb = Character('女学生B',color="#ffffff")

# bear 熊 （Woman Student A） 不加颜色的统一强制指定白色（#ffffff）
define bear = Character('熊',color="#ffffff")

# 莲&店长
define lian_and_dinerowner = Character('莲&店长',color="#414141",image="店长")

# 小姐姐
define xiaojiejie = Character('小姐姐',color="#ffffff")

# 老外A
define foreignera = Character('老外A',color="#ffffff")

# 老外B
define foreignerb = Character('老外B',color="#ffffff")

# 老外C
define foreignerc = Character('老外C',color="#ffffff")

# 老外D
define foreignerd = Character('老外D',color="#ffffff")

# DJ
define dj = Character('DJ',color="#ffffff")

# 旁白
define aside = Character('旁白',color="#ffffff")

# 二周目限定人物!
# 子供Ａ（孩子A）
define childa = Character('孩子A',color="#ffffff")

# 子供Ｂ（孩子B）
define childb = Character('孩子B',color="#ffffff")

# 子供Ｃ（孩子C）
define childc = Character('孩子C',color="#ffffff",image="アシュリー")

# 子供Ｄ（孩子D）
define childd = Character('孩子D',color="#ffffff")

# 子供Ｅ（孩子E）
define childe = Character('孩子E',color="#ffffff")

# 仔猫達（小猫们）
define nekos = Character('小猫们',color="#ffffff")

# 仔猫（小猫）
define neko = Character('小猫',color="#ffffff")

# 母親Ａ（母亲A）
define mothera = Character('母亲A',color="#ffffff")

# 母親Ｂ（母亲B）
define motherb = Character('母亲B',color="#ffffff")

#  母親Ｃ（母亲C）
define motherc = Character('母亲C',color="#ffffff")

#  母亲Ｄ（孩子D）
define motherd = Character('母亲D',color="#ffffff")

#  母亲Ｅ（孩子D）
define mothere = Character('母亲E',color="#ffffff")

# 人物名称定义结束
# ---------------------------------------------

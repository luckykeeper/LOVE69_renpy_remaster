# --------------------------------
# 人物名称定义
# Author:Luckykeeper
# 版本 0.0.4
# Blog：http://b.luckykeeper.site
# 开始日期 2021年8月28日
# 修订日期 2021年9月5日

# 定义老婆和其他人的名字
# 基本定义如下，取中文拼音最后一字的全拼
# | 角色 | 脚本中的代号 | 备注 |
# 一条心爱 ai
# 葛城真冬 dong
# 葛城莲 lian
# 麦克斯韦·里昂 lion //使用英文名，因为是英国人
# 月宫想瑠 liu
# 月宫瑠那 na
# 雾叶（和亚十礼的姓有待商榷，有想法的老哥快来） ye
# 花盆君（植木鉢） pen
# 亚十礼（发音ATRI,雾叶的姊妹）atri //暂定译名从近月2来，缩写atri因为高性能~
# 迈克尔（帽子） mj //帽子就不要名字了（有名字，缩写mj，但是这里为了做区分就叫它帽子）|改，有的地方叫帽子，所以认识之前还是叫hat好了
# 旁白君 bai
# テしビ TV 最早在 sence01 葛城家客厅出现，不大确定是啥，应该是电视里面传来的声音，暂时管电视里面没立绘（包括后面的）的都叫TV好辽
# 翻译君（我自己） Luckykeeper
# ？？？ unknown404 给不知道是谁的时候用
# nil 没人说话的旁白，不在脚本中定义名称
# wsa 女学生A （Woman Student A）

# 一条心爱 ai //和原版相比，移植版打算在人物名上加入颜色，心爱的颜色是场景切换的CG里从刘海儿中间上最长的那根毛上面取的
define ai = Character('心爱',color="#ffc9be",image="心愛")

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

image side 真冬 真冬_制服_基本_目閉じ = "images/face/真冬/真冬_制服_基本_目閉じ.png" # 闭眼微笑
image side 真冬 真冬_制服_基本_目閉じ_1 = "images/face/真冬/真冬_制服_基本_目閉じ_1.png"
image side 真冬 真冬_制服_基本_泣き = "images/face/真冬/真冬_制服_基本_泣き.png" # 睁眼，含泪珠
image side 真冬 真冬_制服_基本_泣き_1 = "images/face/真冬/真冬_制服_基本_泣き_1.png"
image side 真冬 真冬_制服_基本_見下し = "images/face/真冬/真冬_制服_基本_見下し.png" # 闭眼，眉毛y=-x，嘴o
image side 真冬 真冬_制服_基本_見下し2 = "images/face/真冬/真冬_制服_基本_見下し2.png"
image side 真冬 真冬_制服_基本_にっこり = "images/face/真冬/真冬_制服_基本_にっこり.png" # 闭眼，微笑
image side 真冬 真冬_制服_基本_にっこり_1 = "images/face/真冬/真冬_制服_基本_にっこり_1.png"
image side 真冬 真冬_制服_基本_まったり = "images/face/真冬/真冬_制服_基本_まったり.png" # 闭眼，嘴“w”
image side 真冬 真冬_制服_基本_ニタァ = "images/face/真冬/真冬_制服_基本_ニタァ.png" # 睁眼，嘴开口，“w”，是有点小坏的笑呢



# 葛城莲 lian //主人公，工具人就不要加颜色了吧，不加颜色的统一强制指定白色（#ffffff）
define lian = Character('莲',color="#ffffff")

# 麦克斯韦·里昂 lion //和原版相比，移植版打算在人物名上加入颜色，里昂的颜色是摘掉帽子之后在头顶上取的
define lion = Character('里昂',color="#fff7bb",image="リオン")

# 月宫想瑠 liu //和原版相比，移植版打算在人物名上加入颜色，想瑠喵的颜色是SISTARS里面的CG里面取的
define liu = Character('想瑠',color="#a4808c",image="想瑠")

# 月宫瑠那 na //和原版相比，移植版打算在人物名上加入颜色，瑠那的颜色是SISTARS里面的CG里面取的
define na = Character('瑠那',color="#a4808c",image="瑠那")

# 雾叶 ye //和原版相比，移植版打算在人物名上加入颜色，雾叶的颜色是从皮带上十字的中央取的
define ye = Character('雾叶',color="#414141",image="霧葉")

# 花盆君 pen //和原版相比，移植版打算在人物名上加入颜色，花盆君的颜色当然是健康的绿色啦~
define pen = Character('花盆君',color="#659839",image="アシュリー_植木鉢")

# 亚十礼 atri //和原版相比，移植版打算在人物名上加入颜色，亚十礼的颜色也是从头发上取哒~
define atri = Character('亚十礼',color="#fcfafc",image="アシュリー")

# 迈克尔 mj //和原版相比，移植版打算在人物名上加入颜色，帽子就要它本来的颜色就好啦~
define hat = Character('帽子',color="#67435e",image="mj")
define mj = Character('迈克尔',color="#67435e",image="mj")

# 旁白君 bai 不加颜色的统一强制指定白色（#ffffff）
define bai = Character('旁白君',color="#ffffff")

# テしビ tv 不加颜色的统一强制指定白色（#ffffff）
define tv = Character('TV',color="#ffffff")

# 翻译君（我自己） Luckykeeper 用于写长段注释，图标从QQ头像来（要圆的）//译者君的颜色是从个人博客的favion图案里面来哒，和心爱的颜色很像哦~
define luckykeeper = Character('Luckykeeper',color="#ffc0cb")

# ？？？ ??? 给不知道是谁的时候用 不加颜色的统一强制指定白色（#ffffff）
define unknown404 = Character('？？？',color="#ffffff")

# wsa 女学生A （Woman Student A） 不加颜色的统一强制指定白色（#ffffff）
define wsa = Character('女学生A',color="#ffffff")

# 人物名称定义结束
# ---------------------------------------------

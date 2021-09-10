# LOVE69_renpy_remaster

| 项目状况             | LOVE69 Ren’py Remaster Project                               |
| -------------------- | ------------------------------------------------------------ |
| 状态                 | 进行中（Demo版开发中）\|\| 准备返校 & 在火车上 ｜今天就能恢复更新 |
| star数               | ![star](https://img.shields.io/github/stars/luckykeeper/LOVE69_renpy_remaster) |
| fork数               | ![fork](https://img.shields.io/github/forks/luckykeeper/LOVE69_renpy_remaster) |
| issues数             | ![issues](https://img.shields.io/github/issues/luckykeeper/LOVE69_renpy_remaster) |
| 项目组成员           | 1人（[Luckykeeper](https://github.com/luckykeeper)）         |
| Contributors<br/>2人 | [WorldlineChanger](https://github.com/WorldlineChanger)（两处文本润色）；<br/>[Santa-Weaves](https://github.com/Santa-Weaves)（OP歌词润色）； |
| 项目地址             | https://github.com/luckykeeper/LOVE69_renpy_remaster         |
| 项目组官网           | https://love69renpyremasterproject.github.io                 |
| 项目组官网构建状态   | ![status](https://app.travis-ci.com/love69renpyremasterproject/love69renpyremasterproject.github.io.svg?branch=main&status=passed) |

使用ren'py重制LOVEPOTION SIXTYNINE，并加以汉化和全平台适配

<img src="images/项目组logo_smallsize.png" alt="项目组logo"  />

## 🎉开坑宣告🎉

推了好多年的Gal，也想自己做出一些贡献呢，最近正好推完了LOVEPOTION SIXTYNINE，文本难度不是很高，基本上都看懂了，又简单看了一下ren’py，似乎不是很难，所以打算开个坑，整个个人汉化，当然，~~如果能有其它组来做那是大欢迎啦，但是感觉这么冷门的电波系作品应该没有哪个组来做汉化，所以我就这么打算开坑啦~~（2021.09.08_注：希望各位大大还是不要来抢坑了，我现在非常有信心做完的说![huaji](https://cdn.jsdelivr.net/gh/luckykeeper/LuckyBlog_RS@main/face/huaji.aqdzo604ncs.png))

### 实机开发运行界面

LOVE69使用的引擎是 YU-RIS ，因为~~脚本解密不能~~（我太菜了），所以决定使用 ren’py 进行移植，通过三天左右的不懈努力（翻译scene01（差三个小场景）+做GUI（对话框+主页面+logo）+跨平台+听音频+学习使用 ren’py +~~被迫上课~~+……），终于把小小的demo跑了起来！小Demo运行界面如下，可供参考。在sence01完成后会开发给大家下载体验（找Bug），因为拿不到脚本，人物表情，音效，背景图片等等一切设定全部只能通过~~逆向工程~~照着原作人力比对文件完成，所以进度可能略缓慢（不过在不断推进啦），请各位看官耐心等待~

Demo版实机开发界面_主菜单

<img src="images/Demo版实机开发界面_主菜单.PNG" alt="Demo版实机开发界面_主菜单.PNG" style="zoom:20%;" />

原对话框实现

<img src="images/原对话框实现.PNG" alt="原对话框实现.PNG" style="zoom:20%;" />

实机演示_Demo版对话框实现

<img src="images/实机演示_Demo版对话框实现.PNG" alt="实机演示_Demo版对话框实现.PNG" style="zoom:20%;" />

原带CG的主页面

<img src="images/原带CG的主页面.PNG" alt="原带CG的主页面.PNG" style="zoom:20%;" />

实机演示_Demo版带CG的主页面（waifu2x 720p->1080p）

<img src="images/实机演示_Demo版带CG的主页面.PNG" alt="实机演示_Demo版带CG的主页面.PNG" style="zoom:20%;" />

**跨平台测试**

测试平台：中兴Axon 30 Ultra 5G / Android 11 / MyOS 11.0.22MR_A2022P

初步确认可运行于新旧安卓手机、X86安卓设备、模拟器及Chrome Book

除上述平台外，预计还将会有 iOS 版（不过没开发者账户，估计⑧能有），Linux版和MacOS版，甚至WEB版！

安卓Demo实机运行页面_安装

<img src="images/安卓Demo实机运行页面_安装.jpg" alt="安卓Demo安卓Demo实机运行页面_安装.jpg" style="zoom:10%;" />

安卓Demo实机运行页面_项目组logo

<img src="images/安卓Demo实机运行页面_项目组logo.jpg" alt="安卓Demo实机运行页面_项目组logo.jpg" style="zoom:20%;" />

安卓Demo实机运行页面_主菜单

<img src="images/安卓Demo实机运行页面_主菜单.jpg" alt="安卓Demo实机运行页面_主菜单.jpg" style="zoom:20%;" />

安卓Demo实机运行页面_对话框实现

<img src="images/安卓Demo实机运行页面_对话框实现.jpg" alt="安卓Demo实机运行页面_对话框实现.jpg" style="zoom:20%;" />

安卓Demo实机运行页面_带CG的主页面

<img src="images/安卓Demo实机运行页面_带CG的主页面.jpg" alt="安卓Demo实机运行页面_带CG的主页面.jpg" style="zoom:20%;" />

Demo版实机测试_GIF图

可以简短的看下做完大概是什么样子，另外视频里面的“开裂”并不是waifu2x的锅，下面演示中用到的真冬的介绍动画是由解包出来的146张不带alpha通道的jpg文件导到AE做的视频，作品原动画文件是由146张不带alpha通道的jpg文件加上另外几个不能正常打开的jpg文件（推测这几个文件是记录了alpha通道的信息），下面给出一个参考文件供各位大佬分析，如果您有办法能解决这个问题，欢迎加入项目组一起来搞事情![huaji](https://cdn.jsdelivr.net/gh/luckykeeper/LuckyBlog_RS@main/face/huaji.aqdzo604ncs.png)

参考文件 链接：https://pan.baidu.com/s/1lOxy0fX3wEf6dyQNHydhDQ 提取码：qxqm

<img src="images/Demo版实机测试_GIF图.gif" alt="Demo版实机测试_GIF图.gif" style="zoom:20%;" />

## 👏成员👏

组长：[Luckykeeper](https://github.com/luckykeeper)

程序：[Luckykeeper](https://github.com/luckykeeper)

翻译：[Luckykeeper](https://github.com/luckykeeper)

美工：[Luckykeeper](https://github.com/luckykeeper)

校对：[Luckykeeper](https://github.com/luckykeeper)

测试/润色：[Luckykeeper](https://github.com/luckykeeper)

项目组网站构建、维护：[Luckykeeper](https://github.com/luckykeeper)

## 🎂目标🎂

- [ ] 使用ren’py重置本作品，实现跨平台

- [ ] 使用waifu2x将材质高清化（720p->1080p，部分素材2K）

- [ ] 让更多人有机会接触本作，爱上本作

- [ ] 汉化成果最终全部开源，给其它想参与汉化的同好提供一个思路

## ✨目前状态✨

请参考本项目[projects页面](https://github.com/luckykeeper/LOVE69_renpy_remaster/projects/1)

## 😁翻译原则😊

- 采用机翻+润色的方式进行，因为我是个日语渣，翻译初稿来自百度翻译+彩云小译的结果，润色通过听译+Yahoo参考等方式进行

- 主要采用意译的方式，因为本来就是电波系作品，很多地方并不好直译

- 不会翻的地方使用 // 标出，希望老哥们帮帮忙（等上传scene01就能看到了，现在还在做…）

- 第一次做翻译，也是第一次用ren'py，活整的不好还请带伙见谅

## 🐱‍🏍想要参与？🐱‍👓

需要的工作如下：

日语翻译&纠错：在某个 scene 完成后，提交PR或在本页[“issues”栏目下](https://github.com/luckykeeper/LOVE69_renpy_remaster/issues)留言（推荐`issues`）

Yu-ris的ybn文件解包：请将联系方式发送至 luckykeeper@luckykeeper.site （某些情况可能收不到邮件，如未及时回复请电脑访问我的[个人博客](http://b.luckykeeper.site)，在主页头像下方寻找我的联系方式）

ren’py的GUI制作：我还没开始学，而且想复刻本作目前的样式……所以如果会做的话请将联系方式发送至 luckykeeper@luckykeeper.site 

CG、BGM等素材的解包工作已全部完成，无需帮助

测试、校对：可以先把联系方式发送到 luckykeeper@luckykeeper.site ，完成后将会联系

动画的alpha通道分析（本作的动画是由一堆jpg构成的，在文件夹内有4个不能显示图像的jpg文件，00000000-3.jpg），希望有人来分析一下提取出alpha通道。若这个问题不能解决，移植时可能会放弃部分特效或不得不从其它地方提取部分特效进行替代，具体情况请参见上方演示画面的gif图（2021.09.08_注：这个问题不着急了，今天已经把ed的1457张jpg扣出来了，拿不到 alpha 通道，我就en扣！）

### 找不到文件？

- 人物表、剧本（脚本）在上面显示代码的地方里面的[“已完成的文档”](https://github.com/luckykeeper/LOVE69_renpy_remaster/tree/main/%E5%B7%B2%E5%AE%8C%E6%88%90%E7%9A%84%E6%96%87%E6%A1%A3)目录下，点开文件夹， `.rpy` 格式的就是啦，不需要下载任何程序，在网页上就能浏览，剧本（脚本）文件中使用的是这些角色名字的缩写（当然原人物也已标出）
- 人物表文件夹只有一个文件 `character.rpy` 是人物的译名和人物在（剧本）脚本中的定义
- 剧本（脚本）文件夹下包含多个文件， `script.rpy` 是主程序脚本，也就是程序（游戏）的入口，而 `scene01（01这样的数字会根据场景（scene）更改）.rpy` 这样的文件包含了真正的脚本（剧本），也就是原文、翻译、BGM、人物、图片、表情……等等东西都是在这里定义的，**想做翻译纠错主要是看这些文件**，需要协助翻译或修改的地方在原文后已经用  `//` 标出

## 🚦使用说明🚦

1. 本项目的任何代码，请勿用于商业化，如果您使用了本项目的任何代码和脚本进行二次创作则必须对其开源，且必须在开源页面标注使用了本项目并标注本项目的 GitHub 地址
2. 使用项目中[“已完成的文档”](https://github.com/luckykeeper/LOVE69_renpy_remaster/tree/main/%E5%B7%B2%E5%AE%8C%E6%88%90%E7%9A%84%E6%96%87%E6%A1%A3)目录下的任何内容进行二次开发必须先在`issues`内申请，申请时请说明你是谁、以及使用该项目的哪些内容，加上使用内容的目的，得到授权方可按照条件使用（条件参考但并不限于“使用说明”内容）
3. 使用[“已完成的文档”](https://github.com/luckykeeper/LOVE69_renpy_remaster/tree/main/%E5%B7%B2%E5%AE%8C%E6%88%90%E7%9A%84%E6%96%87%E6%A1%A3)目录下的任何内容须标明本项目的url和本人的名字（Luckykeeper）
4. 若程序使用了[“已完成的文档”](https://github.com/luckykeeper/LOVE69_renpy_remaster/tree/main/%E5%B7%B2%E5%AE%8C%E6%88%90%E7%9A%84%E6%96%87%E6%A1%A3)目录下的任何内容，则禁止擅自在一切视频网站（如：B站）上进行游戏的录播和直播
5. 请务必遵守您所在国家/地区的相关法律法规
6. 支持开源精神，鼓励用爱发电，欢迎大家参考本项目为自己喜欢的ADV/AVG进行汉化移植，如果该项目帮助了你，希望你在发布程序的时候提及一下这个项目的url和我
7. 如果该项目帮助了你，请帮我点亮一下页面上方的 `star` 这是对我最好的鼓励
8. 本项目不接受任何形式的捐赠，~~本页面是唯一指定的联系方式~~（L:项目组网站肝完了，链接在上面的表格里面，去那边也可以，那边评论不需要GitHub账号，没有GitHub账号的阔以去那边），想找我就发issues，看到会及时回复，没有其它任何联系方式

## 😥其它事项😅

- 项目可能因为学业原因无限期推迟（学业繁忙+是只鸽子😅）~~【所以有其他人想来汉化那是大欢迎，也欢迎使用本项目已经汉化好的文本和提取出的日语文本~~，不过如果用的话请加上我的名字（Luckykeeper）】{就不要着急催着填坑了哈}【2021.09.08_注：做不完的可能性不大，目前还是非常顺利的，我非常有信心能把坑填完，烦请各位大大就不要抢坑了哈】
- 项目相关文件解压密码为本页面网址（即 https://github.com/luckykeeper/LOVE69_renpy_remaster ）下载链接暂时取消
- 出于各种原因，本次汉化移植并不会对“gkd”的内容（即 Hscene ）进行汉化和移植![doge](https://cdn.jsdelivr.net/gh/luckykeeper/LuckyBlog_RS@main/face/doge.7cjy2wsn5n40.png)
- 本页面最后修改时间 2021年9月11日

## Stargazers over time 

[![Stargazers over time](https://starchart.cc/luckykeeper/LOVE69_renpy_remaster.svg)](https://starchart.cc/luckykeeper/LOVE69_renpy_remaster) 

最近一次夜间自动构建状态（dev分支）：[![dev 分支夜间测试&构建](https://github.com/luckykeeper/LOVE69_renpy_remaster/actions/workflows/build-love69.yml/badge.svg?event=schedule)](https://github.com/luckykeeper/LOVE69_renpy_remaster/actions/workflows/build-love69.yml)

欢迎来到 dev 分支，任何的新PR请提交至此分支

注意：请不要改动 `options.rpy` 中的 Build 时间 （即“（Build 20220428）”）程序会根据当前构建时间自动替换

## ChangeLog

> 基于：正式版 1.0 （Build 20220428）

### 2022-05-01

- 创建 dev 分支
- 编写&完善夜间自动构建&测试脚本

### 2022-05-03

- 加入吐槽模式的开关（脚本对应内容暂时还没做，等我调整一下）

### 2022-05-07

> 修复了 [#19](https://github.com/luckykeeper/LOVE69_renpy_remaster/issues/19) 的问题

- 修复了在STAFF表播放过程中返回菜单会把 STAFF 的 BGM 带回主菜单的问题
- 修复了在播放 staff 表时读档回到选项前再次选择播放 staff 表，会导致 staff 表卡在某一帧不动的问题

### 2022-05-09

- 更新 Scene06 脚本，添加一处梗的解释（真冬哼的一句歌，德沃夏克-自新大陆交响曲），感谢B站[@**Karma_0xCC**](https://space.bilibili.com/12020130)


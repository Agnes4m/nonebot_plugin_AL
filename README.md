<div align="center">

<img src="https://raw.githubusercontent.com/Agnes4m/nonebot_plugin_l4d2_server/main/image/logo.png" width="180" height="180"  alt="AgnesDigitalLogo">
                <br>
<p><img src="https://s2.loli.net/2022/06/16/xsVUGRrkbn1ljTD.png" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot_plugin_al 0.3.0

__✨Nonebot & 碧蓝航线攻略✨__

<a href="https://github.com/Agnes4m/nonebot_plugin_AL/stargazers">
<img alt="GitHub stars" src="https://img.shields.io/github/stars/Agnes4m/nonebot_plugin_AL" alt="stars">
</a>

<a href="https://github.com/Agnes4m/nonebot_plugin_AL/issues">
<img alt="GitHub issues" src="https://img.shields.io/github/issues/Agnes4m/nonebot_plugin_AL" alt="issues">
</a>

<a href="https://jq.qq.com/?_wv=1027&k=HdjoCcAe">
        <img src="https://img.shields.io/badge/QQ%E7%BE%A4-399365126-orange?style=flat-square" alt="QQ Chat Group">
</a>

<a href="https://pypi.python.org/pypi/nonebot_plugin_AL">
        <img src="https://img.shields.io/pypi/v/nonebot_plugin_AL.svg" alt="pypi">

</a>

<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">
    <img src="https://img.shields.io/badge/nonebot-2.0.0-red.svg" alt="NoneBot">

</div>

## 功能

1、b站wiki井号榜一图流

2、舰船装备图鉴

3、(70%完成)移植大部分[blhx](https://github.com/Gaylone/blhx_wiki)（原hoshino改项目）的大部分功能


## 安装

以下命令选其一即可

```sh
nb plugin install nonebot_plugin_al
```
```sh
pip install nonebot_plugin_al
```
```sh
git clone https://github.com/Agnes4m/nonebot_plugin_AL.git
```

## 资源包

本项的图片资源基本都来源于本地，具体在项目的images文件夹里，大小在3.5G左右，项目在[api](https://github.com/AzurAPI/azurapi-js-setup) 打包下载，将下载来的项目里的images文件夹放入bot目录下`data/al/ship_html`里面，也就是说路径为`data/al/ship_html/images/`这点十分重要，blhx_wiki功能90%依赖这个资源包，请自行留意它的更新

<!-- 除了图片文件，还有一些其它的，比如原作者仓库的 一些(划掉) 好多东西 -->

百度云盘：链接：https://pan.baidu.com/s/1ppLW3rkygLovXIG_Y58Qrg?pwd=57uk 
提取码：57uk

## 指令

### 【总】碧蓝帮助 | 碧蓝指令

- 1、碧蓝+['强度榜','装备榜','金部件榜','萌新榜','兵器榜','专武榜',
        '兑换榜','研发榜','改造榜','跨队榜','pt榜','氪金榜','打捞主线榜','打捞作战榜']
- 2、碧蓝角色【角色名称】
- 3、碧蓝装备【装备名称】

### 【blhx_wiki】（强制检查空格）

0.帮助信息

命令示范：blhx 帮助

1.根据船名查舰船信息

命令示范： blhx 长门

2.根据船名和皮肤名查询皮肤立绘

命令示范：blhx 圣路易斯 Luxury_Handle

命令示范：blhx 长门 御狐的辉振袖

命令示范：blhx 长门 原皮

命令示范：blhx 长门 婚纱

3.随机返回游戏加载页面的插画

命令示范：blhx 过场

4.返回bwiki的PVE强度榜信息

命令示范：blhx 强度榜

7.强制更新(目前已使用代理更新api数据为离线模式所用，如果出问题及时issue)

命令示范：blhx 强制更新

8.获取最新活动信息(有问题及时issue)

命令示范：blhx 最新活动

9.为舰船取昵称(以后你就可以用昵称查询了)

命令示范：blhx备注 光辉 太太

以后就可以用 blhx 太太 婚纱 这种昵称取代正式名称查询

10.删除舰船昵称

命令示范：blhx移除备注 光辉 太太

11.舰船昵称快捷查询

命令示范：blhx皮肤 光辉 0

12.建造模拟

命令示范：blhx大建 轻型/重型/特型

## 🙈 其他

- 本项目仅供学习使用，请勿用于商业用途
- 喜欢该项目可以Star或者提供PR，你的支持就是我持续维护的动力
- [爱发电](https://afdian.net/a/agnes_digital)
- [MIT License](https://github.com/Agnes4m/nonebot_plugin_AL/blob/main/LICENSE) ©[@Agnes4m](https://github.com/Agnes4m)

## 感谢

- [AzurAPI](https://github.com/AzurAPI/azurapi-js-setup)持续更新的碧蓝航线数据库
- [blhx_wiki](https://github.com/Gaylone/blhx_wiki) - hoshino碧蓝航线项目（已停止维护）

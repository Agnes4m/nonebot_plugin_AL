import aiohttp

from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.matcher import Matcher
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import (
    Message,
    MessageSegment
)
from .bili import jinghao,get_data

__version__ = "0.0.1"
__plugin_meta__ = PluginMetadata(
    name="碧蓝航线攻略",
    description='碧蓝航线井号榜等等攻略',
    usage='碧蓝航线攻略',
    extra={
        "version": __version__,
        "author": "Agnes4m <Z735803792@163.com>",
    },
)

al_command = on_command('al',aliases={'碧蓝'},priority=30,block=True)
tag_ser = on_command('alhelp',aliases={'碧蓝指令','碧蓝帮助'},priority=30,block=True)
tags = ['强度榜','装备榜','金部件榜','萌新榜','兵器榜','专武榜',
        '兑换榜','研发榜','改造榜','跨队榜','pt榜','氪金榜','打捞主线榜','打捞作战榜']

@tag_ser.handle()
async def _(matcher:Matcher):
    msg = '碧蓝帮助指令\n'
    data:str = ''
    for one in tags:
        data += f'{one} | '
    msg += data
    await matcher.finish(msg)

@al_command.handle()
async def _(matcher:Matcher,args:Message = CommandArg()):
    word = args.extract_plain_text()
    if word in tags:
        await matcher.finish(MessageSegment.image(await get_data(await jinghao(word))))
    else:
        await matcher.finish()
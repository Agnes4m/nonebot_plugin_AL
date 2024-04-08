import asyncio
from bs4 import BeautifulSoup
from pathlib import Path
import time

from nonebot.log import logger
from nonebot_plugin_htmlrender import (
    html_to_pic,
)


from .api import get_data

rank_mapping = {
    "强度榜": "认知觉醒主线推荐榜.jpg",
    "装备榜": "装备一图榜.jpg",
    "金部件榜": "金部件推荐榜.jpg",
    "萌新榜": "萌新入坑舰船推荐榜.png",
    "兵器榜": "兵装推荐榜.jpg",
    "专武榜": "专武推荐榜.png",
    "兑换榜": "兑换装备推荐榜.png",
    "研发榜": "装备研发推荐榜.png",
    "改造榜": "改造舰船推荐榜.png",
    "跨队榜": "跨队舰船推荐榜.png",
    "pt榜": "新晋指挥官pt兑换榜.png",
    "氪金榜": "氪金榜主榜.png",
    "打捞主线榜": "井号打捞表主线地图.png",
    "打捞作战榜": "井号打捞表作战档案.png",
}

async def jinghao(tag):
    data = await get_data('https://wiki.biligame.com/blhx/井号碧蓝榜合集')
    soup = BeautifulSoup(data, 'html.parser')
    if tag:
        img_tag = soup.find('img', alt=rank_mapping.get(tag))
    else:
        return None
    img_src = img_tag.get('src')
    print(img_src)
    return img_src
    



async def get_ship_msg(name:str):
    "获取单个船的页面html"
    start_time = time.time()
    Path("data/al/ship").mkdir(parents=True, exist_ok=True)
    ship_path = Path(f"data/al/ship/{name}.html")
    # if not ship_path.exists():
    msg:BeautifulSoup = await get_data(url=f"https://wiki.biligame.com/blhx/{name}",mode="html")
    msg_str = str(await ship_html_select(await soup_del_gif(msg)))
    with open(ship_path,mode="w" ,encoding="utf-8")as f:
        f.write(msg_str)
    # else:
    #     with open(ship_path,mode="r" ,encoding="utf-8")as f:
    #         msg_str = f.read()
    msg_img:bytes = await html_to_pic(msg_str)
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.success(f"绘图成功，耗时: {elapsed_time} 秒")
    return msg_img

async def ship_html_select(soup:BeautifulSoup):
    # 修改为图片html
    html_str = soup.prettify()
    start_index = html_str.index('<!DOCTYPE html>')
    css_msg = html_str[:start_index]
    base_msg = soup.select_one("div[class='row']").prettify()
    wp_msg = soup.find("div",class_="panel panel-shiptable").prettify()
    fina_soup = css_msg + base_msg + wp_msg
    return fina_soup


async def soup_del_gif(soup: BeautifulSoup):
    # 删除gif图
    gif_images = soup.select('img[src$=".gif"]')

    for img in gif_images:
        img.extract()
        
    return soup
    
if __name__== '__main__':
    asyncio.run(get_ship_msg("新泽西"))
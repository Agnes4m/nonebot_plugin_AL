import asyncio
from bs4 import BeautifulSoup
from pathlib import Path
import time
        
        
from nonebot_plugin_htmlrender import (
    html_to_pic,
)
from .api import get_data



async def jinghao(tag):
    data = await get_data('https://wiki.biligame.com/blhx/井号碧蓝榜合集')
    soup = BeautifulSoup(data, 'html.parser')
    if tag == '强度榜':
        img_tag = soup.find('img', alt="认知觉醒主线推荐榜.jpg")
    elif tag == '装备榜':
        img_tag = soup.find('img', alt="装备一图榜.jpg")
    elif tag == '金部件榜':
        img_tag = soup.find('img', alt="金部件推荐榜.jpg")
    elif tag == '萌新榜':
        img_tag = soup.find('img', alt="萌新入坑舰船推荐榜.png")
    elif tag == '兵器榜':
        img_tag = soup.find('img', alt="兵装推荐榜.jpg")
    elif tag == '专武榜':
        img_tag = soup.find('img', alt="专武推荐榜.png")
    elif tag == '兑换榜':
        img_tag = soup.find('img', alt="兑换装备推荐榜.png")
    elif tag == '研发榜':
        img_tag = soup.find('img', alt="装备研发推荐榜.png")
    elif tag == '改造榜':
        img_tag = soup.find('img', alt="改造舰船推荐榜.png")
    elif tag == '跨队榜':
        img_tag = soup.find('img', alt="跨队舰船推荐榜.png")
    elif tag == 'pt榜':
        img_tag = soup.find('img', alt="新晋指挥官pt兑换榜.png")
    elif tag == '氪金榜':
        img_tag = soup.find('img', alt="氪金榜主榜.png")
    elif tag == '打捞主线榜':
        img_tag = soup.find('img', alt="井号打捞表主线地图.png")
    elif tag == '打捞作战榜':
        img_tag = soup.find('img', alt="井号打捞表作战档案.png")
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
    msg_str = str(await ship_html_select(await ship_html_remove( await soup_del_gif(msg))))
    with open(ship_path,mode="w" ,encoding="utf-8")as f:
        f.write(msg_str)
    # else:
    #     with open(ship_path,mode="r" ,encoding="utf-8")as f:
    #         msg_str = f.read()
    msg_img:bytes = await html_to_pic(msg_str)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"耗时: {elapsed_time} 秒")
    return msg_img

async def ship_html_select(soup:BeautifulSoup):
    # 修改为图片html
    unwanted_elements = [
        "div.wiki-header.navbar.navbar-default.navbar-static-top.container",
        "div#siteNotice.mw-body-content",
        "div.mw-indicators",
        "div#headBox",
        "div.wiki-componment-rank",
        "div#copyField",
        "div.qchar-container",
        "panel panel-shiptable",
        "div.footer-public.visible-md-block.visible-lg-block"
    ]
    for selector in unwanted_elements:
        elements = soup.select(selector)
        for element in elements:
            element.extract()
    return soup

async def ship_html_remove(soup: BeautifulSoup):
    start_tag = soup.find("div", class_="thumb tright")
    end_tag = soup.find("div", class_="mw-references-wrap")
    if start_tag and end_tag:
        current_tag = start_tag
        while current_tag and current_tag != end_tag:
            next_tag = current_tag.find_next()
            current_tag.decompose()
            current_tag = next_tag
    return soup

async def soup_del_gif(soup: BeautifulSoup):
    # 删除gif图
    gif_images = soup.select('img[src$=".gif"]')

    for img in gif_images:
        img.extract()
        
    return soup
    
if __name__== '__main__':
    asyncio.run(get_ship_msg("新泽西"))
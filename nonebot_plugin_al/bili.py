import asyncio
from bs4 import BeautifulSoup
from pathlib import Path
            
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
    Path("data/al/ship").mkdir(parents=True, exist_ok=True)
    ship_path = Path(f"data/al/ship/{name}.html")
    if not ship_path.exists():
        msg:bytes = await get_data(url=f"https://wiki.biligame.com/blhx/{name}")
        msg_str = msg.decode('utf-8')
        with open(ship_path,mode="w" ,encoding="utf-8")as f:
            f.write(msg_str)
    else:
        with open(ship_path,mode="r" ,encoding="utf-8")as f:
            msg_str = f.read()
    msg_img = await html_to_pic(msg_str)

    return msg_img
# css = httpx.get("https://wiki.biligame.com/blhx/%E6%96%B0%E6%B3%BD%E8%A5%BF",headers=headers).content

    
if __name__== '__main__':
    asyncio.run(get_ship_msg("新泽西"))
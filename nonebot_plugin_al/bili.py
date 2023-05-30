import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def get_data(url:str):
    """获取网页内容"""
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, timeout=600) as response:
            if response.status == 200:
                return await response.read()
            else:
                return None
            
# async def data_to_bs4(data:bytes):
#     soup = BeautifulSoup(data, 'html.parser')
#     return soup
    

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
    
if __name__== '__main__':
    asyncio.run(jinghao())
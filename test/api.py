import aiohttp
import asyncio
import httpx
from bs4 import BeautifulSoup

async def get_data(url:str ,mode = None):
    """获取网页内容"""
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, timeout=600) as response:
            if response.status == 200:
                if mode == "html":
                    html = await response.text()  # 获取网页源代码
                    soup = BeautifulSoup(html, 'html.parser')  # 创建BeautifulSoup对象
                    return soup
                else:
                    return await response.read()
            else:
                return None
MAIN_URL = "https://ghproxy.com/https://raw.githubusercontent.com/AzurAPI"    ##https://raw.fastgit.org可以根据需要配置不同代理，结合网络情况自行修改
SHIP_LIST = f"{MAIN_URL}/azurapi-js-setup/master/ships.json"
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
}
msg = httpx.get(url=SHIP_LIST,headers=headers).json()
# print(msg)
print(type(msg))
# from azurlane import AzurAPI
# import os
# import json
# import certifi
# import ssl
# import httpx
# ssl_context = ssl.create_default_context(cafile=certifi.where())
import aiohttp
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

# os.environ['REQUESTS_CA_BUNDLE'] = './cacert.pem'
# api = AzurAPI()
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37'
# }
# url="https://raw.githubusercontent.com/AzurAPI/azurapi-js-setup/master/ships.json"
# msg = httpx.get(url=url,headers=headers)
# msg = msg.json()
# with open("msg.json",mode='w',encoding="utf-8")as f:
#     json.dump(msg,f,ensure_ascii=False)
# msg = api.getAllShipsByChineseName()
# print(msg)
# api.updater.update()

import httpx

async def get_ship_msg(name:str):
    "获取单个船的页面html"
    msg:bytes = await get_data(url=f"https://wiki.biligame.com/blhx/{name}")
    msg_str = msg.decode('utf-8')
    return msg_str
# css = httpx.get("https://wiki.biligame.com/blhx/%E6%96%B0%E6%B3%BD%E8%A5%BF",headers=headers).content
# with open("text.html",mode="w",encoding="utf-8")as f:
#     f.write(msg)
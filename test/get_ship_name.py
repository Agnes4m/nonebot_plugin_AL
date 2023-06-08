import httpx
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
    }

def get_one_msg(ship_msg:BeautifulSoup):
    name_span = ship_msg.find("span", class_="jntj-4")
    names = name_span.decode_contents()
    names = names[names.find(">") + 1:names.rfind("<")]
    print(names)
    names = names.split('<br/>')
    return {names[0]:names}

# data_msg = httpx.get(url="https://wiki.biligame.com/blhx/%E8%88%B0%E8%88%B9%E5%9B%BE%E9%89%B4",
#                      headers=headers).text
data_msg = httpx.get(url="https://wiki.biligame.com/blhx/%E8%A3%85%E5%A4%87%E5%9B%BE%E9%89%B4",
                     headers=headers).text
soup = BeautifulSoup(data_msg, 'html.parser')
ship_msg = soup.select("#CardSelectTr div.jntj-1.divsort")
data_json = {}
for one in ship_msg:
    data_json.update(get_one_msg(one))
with open ("ship.json",mode="w",encoding="utf-8")as f:
    json.dump(data_json,f,ensure_ascii=False)
    

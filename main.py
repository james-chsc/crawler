import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = "https://water.taiwanstat.com/"
rsp = requests.get(url)

# 抓取回傳的狀態碼，200表示成功，不是表示有錯誤發生
if rsp.status_code != 200:
  print(f'抓取網頁發生錯誤，代碼：{rsp.status_code}')
  quit() # 結束程式

# 顯示取回的網頁原始檔
# print(rsp.text)

# 也可以用 html5lib，不過要先安裝 pip install html5lib
soup = BeautifulSoup(rsp.text, 'html.parser')

# prettify()用來把 html 程式變漂亮
# print(soup.prettify())

wb = Workbook()
ws = wb.active
ws.append(['水庫', '最大存水量'])
reservoirs = soup.select('div.reservoir')  # 'div.class'  'div.#id'

for rsv in reservoirs:
  name = rsv.select('div.name>h3')[0].text
  volumn = rsv.select('div.volumn>h5')[0].text
  ws.append([name, volumn])
  
wb.save('水庫資訊.xlsx')
wb.close
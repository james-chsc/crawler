from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome('./chromedriver')   # 指向 chromedriver 的位置
driver.get('https://example.oxxostudio.tw/python/selenium/demo.html')  # 打開瀏覽器，開啟網頁

a = driver.find_element(By.ID, 'a')                # 取得 id 為 a 的網頁元素 ( 按鈕 A )
# a = driver.find_element(By.CSS_SELECTOR, '#a')
b = driver.find_element(By.CLASS_NAME, 'btn')      # 取得 class 為 btn 的網頁元素 ( 按鈕 B )
# b = driver.find_element(By.CSS_SELECTOR, '.btn')
c = driver.find_element(By.CSS_SELECTOR, '.test')  # 取得 class 為 test 的網頁元素 ( 按鈕 C )
d = driver.find_element(By.NAME, 'dog')            # 取得屬性 name 為 dog 的網頁元素 ( 按鈕 D )
# d = driver.find_element(By.CSS_SELECTOR, '[name="dog"]')
h1 = driver.find_element(By.TAG_NAME, 'h1')        # 取得 tag h1 的網頁元素
# h1 = driver.find_element(By.CSS_SELECTOR, 'h1')

sleep(5)

a.click_and_hold()
sleep(5)
a.release()

sleep(10)

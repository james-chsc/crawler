from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome('./chromedriver_mac_arm64')       # 指向 chromedriver 的位置
driver.get('http://www.chsc.tw')                           # 打開瀏覽器，開啟網頁

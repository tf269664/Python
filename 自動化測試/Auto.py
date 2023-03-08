from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'})
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

'''使用Chrome App到國泰世華銀行官網(https://www.cathaybk.com.tw/cathaybk/)並將畫面截圖。'''

driver.get('https://www.cathaybk.com.tw/cathaybk/')

#待頁面加載完成後截圖
wait.until(EC.presence_of_element_located(('class name', 'cubre-o-indexKv__action')))
driver.save_screenshot("Question1.png")

'''點選左上角選單，進入 個人金融 > 產品介紹 > 信用卡列表，需計算有幾個項目並將畫面截圖。'''

wait.until(EC.presence_of_element_located(('class name','cubre-o-header__burger'))).click()
driver.find_element('xpath', '/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div').click()
card = driver.find_element('xpath', '/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div')
card.click()

#取得信用卡列表下方項目數量並截圖
card_list = driver.find_element('xpath', '/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]')
card_list_item = card_list.find_elements('xpath', 'a')
print('項目數量:', len(card_list_item))
time.sleep(2)
driver.save_screenshot("Question2.png")

'''個人金融 > 產品介紹 > 信用卡 > 卡片介紹 > 計算頁面上所有(停發)信用卡數量並截圖'''

card_list.find_element('xpath', 'a[1]').click()
wait.until(EC.presence_of_element_located(('xpath','/html/body/div[1]/main/article/div/div/div/div[1]/div/div')))

#取得停發信用卡數量並截圖
disabled_card = driver.find_element('xpath', '/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]')
disabled_card.find_element('xpath', 'span[2]').click()
disabled_card_item = disabled_card.find_elements('xpath', 'span')
print('停發信用卡數量:', len(disabled_card_item))

i = 1
while i <= len(disabled_card_item):
    disabled_card.find_element('xpath', 'span['+str(i)+']').click()
    time.sleep(1)
    driver.save_screenshot("Question3-"+str(i)+".png")
    i += 1

driver.quit()

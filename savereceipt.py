
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os

# Google Chrome Driverの設定
chopt=webdriver.ChromeOptions()
appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local",
            "account":""
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}

prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(appState)}
chopt.add_experimental_option('prefs', prefs)
chopt.add_argument('--kiosk-printing')

driver = webdriver.Chrome("./driver/chromedriver", options=chopt)
order_history = "https://www.amazon.co.jp/gp/css/order-history?ref_=nav_orders_first"

userID = "ユーザーID"
userPass = "パスワード"

#GoogleChromeを開く
driver.get(order_history)

#ID入力
mailElement = driver.find_element_by_id('ap_email')
mailElement.send_keys(userID)

nextButton = driver.find_element_by_id('continue')
nextButton.click()

#パスワード入力
passElement = driver.find_element_by_id('ap_password')
passElement.send_keys(userPass)

loginButton = driver.find_element_by_id('signInSubmit')
loginButton.click()

#二段階認証選択画面
#radioElement = driver.find_element_by_xpath("//input[@value='email']").click()

#continueButton = driver.find_element_by_id('continue')
#continueButton.click()

#認証番号入力フォーム
#authNumber = input("確認番号を入力してください")

#authField = driver.find_element_by_name('code')
#authField.send_keys(authNumber)

#continueButton = driver.find_element_by_xpath("//input[@aria-labelledby='a-autoid-0-announce']")
#continueButton.click()

#注文履歴画面
orderData = driver.find_elements_by_xpath("//span[@class='hide-if-js']")

print(len(orderData))
print(orderData)

for i, order in enumerate(orderData):

    reseatHref = order.find_element_by_xpath("a[@class='a-link-normal']")
    reseatLink = reseatHref.get_attribute("href")

    print(reseatLink)

    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(reseatLink)

    driver.execute_script('return window.print()')

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

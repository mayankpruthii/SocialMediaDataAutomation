from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import time
from datetime import date
import json

def MediumStatsScraper():
    with open('./Cred.json') as f:
        data = json.load(f) 

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome('./chromedriver.exe')
    # driver.maximize_window()  

    driver.get('https://medium.com/nyaaya/stats/overview')

    # time.sleep(2)

    google_signin_button = driver.find_elements_by_class_name('button-label')[0]

    # google_signin_button = driver.find_element_by_xpath('//*[@id="_obv.shell._surface_1590917072241"]/div/div[3]/div/section/div[1]/div/button[1]')
    google_signin_button.click()

    time.sleep(1)

    loginName = driver.find_element_by_name('identifier')
    loginName.send_keys(data['Medium']['emailID'])
    nextButton = driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
    nextButton.click()

    time.sleep(2)

    passwordEnter = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    passwordEnter.send_keys(data['Medium']['password'])
    nextButton2 = driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
    nextButton2.click()

    time.sleep(10)

    data = {}

    # minutes_read = driver.find_element_by_tag_name('h2')
    minutes_read = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div[1]/div[1]/h2').text

    # minutes_read = driver.find_element_by_class_name('js-readingTimeStatsText').text
    print(minutes_read)
    views = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div[2]/div[1]/h2').text
    visitors = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div[3]/div[1]/h2').text


    data['Date'] = str(date.today())
    data['Minutes Read'] = minutes_read
    data['Views'] = views
    data['Visitors'] = visitors

    return data

if __name__ == '__main__':
    myData = MediumStatsScraper()
    print(myData)

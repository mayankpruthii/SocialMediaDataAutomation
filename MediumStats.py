from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import time
from datetime import date
import json

jsonData = []


class MyMediumStats:
    
    def __init__(self):
        self.data = {}

    def MediumStatsScraper(self):
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

        # minutes_read = driver.find_element_by_tag_name('h2')
        minutes_read = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div[1]/div[1]/h2').text

        # minutes_read = driver.find_element_by_class_name('js-readingTimeStatsText').text
        # print(minutes_read)
        views = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div[2]/div[1]/h2').text
        visitors = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div[3]/div[1]/h2').text


        self.data['Date'] = str(date.today())
        self.data['Minutes Read'] = minutes_read
        self.data['Views'] = views
        self.data['Visitors'] = visitors

        
        driver.get('https://medium.com/nyaaya/stats/stories?format=json')

        jsonData = driver.find_element_by_xpath("/html/body/pre").text

        self.data['jsonData'] = jsonData

    def MediumOverviewStats(self):
        # my_data = MediumStatsScraper()
        response = {key: self.data[key] for key in self.data.keys() & {'Date', 'Minutes Read', 'Views', 'Visitors'}}
        return response

    def MediumPostsStats(self):
        response = {key: self.data[key] for key in self.data.keys() & {'jsonData'}}
        response = response['jsonData']
        response = response[16:]
        jsonResponse = json.loads(response)
        my_data = jsonResponse['payload']['value']
        myList = []
        for post in my_data:
            myDict = {'Title':'', 'Publish Month':'', 'Views':'', 'Reads':'', 'Read Ratio':'', 'Reading time':'', 'Fans':'' }
            myDict['Title'] = post['title']
            myDict['Publish Month'] = post['firstPublishedAtBucket']
            myDict['Fans'] = post['upvotes']
            myDict['Views'] = post['views']
            myDict['Reads'] = post['reads']
            myDict['Reading time'] = post['readingTime']
            read_ratio = (post['reads']/post['views']) * 100
            myDict['Read Ratio'] = int(read_ratio)
            myList.append(myDict)

        return myList

if __name__ == '__main__':
    myData = MyMediumStats()
    myData.MediumStatsScraper()
    myData.MediumPostsStats()
    
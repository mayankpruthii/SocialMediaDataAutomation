from selenium import webdriver
import time
from datetime import date
import tweepy
from selenium.webdriver.chrome.options import Options
import json

def TwitterDataFetch():

    with open('./Cred.json') as f:
        data = json.load(f) 
    
    # First Scraping is done to get some values
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome('./chromedriver.exe')

    driver.get('https://analytics.twitter.com/user/NyaayaIN/home')

    loginName = driver.find_element_by_name('session[username_or_email]')
    loginName.send_keys(data['Twitter'][0]['Scrape']['loginUsername'])
    password = driver.find_element_by_name('session[password]')
    password.send_keys(data['Twitter'][0]['Scrape']['password'])
    loginButton = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div/span/span')
    loginButton.click()

    time.sleep(2)

    tweetsNavigation = driver.find_element_by_xpath('//*[@id="SharedNavBarContainer"]/div/div/ul[1]/li[2]/a')
    tweetsNavigation.click()
    calenderButton = driver.find_element_by_xpath('//*[@id="daterange-button"]')
    calenderButton.click()
    calender7days = driver.find_element_by_xpath('/html/body/div[4]/div[4]/ul/li[1]')
    calender7days.click()

    time.sleep(2)
    
    engagement_rate = driver.find_element_by_xpath('//*[@id="engagements-time-series-container"]/div/div[1]/div[2]').text
    link_clicks = driver.find_element_by_xpath('//*[@id="clicks-time-series-container"]/div/div[1]/div[2]').text
    retweets = driver.find_element_by_xpath('//*[@id="retweets-time-series-container"]/div/div[1]/div[2]').text
    likes = driver.find_element_by_xpath('//*[@id="favs-time-series-container"]/div/div[1]/div[2]').text
    replies = driver.find_element_by_xpath('//*[@id="replies-time-series-container"]/div/div[1]/div[2]').text
    impressions = driver.find_element_by_xpath('//*[@id="tweet-impression-header"]/h3/strong[1]').text[::-1]
    
    driver.quit()

    impressions = impressions[13:]
    impressions = impressions[::-1]


    consumer_key = data['Twitter'][1]['Authentication']['consumerKey']
    consumer_secret = data['Twitter'][1]['Authentication']['consumerSecret']
    key = data['Twitter'][1]['Authentication']['accessKey']
    secret = data['Twitter'][1]['Authentication']['accessSecret']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)
    api = tweepy.API(auth)
    followers = api.me().followers_count
    posts = api.me().statuses_count

    myDict = {}

    myDict['Date'] = str(date.today())
    myDict['Impressions'] = float(impressions)
    myDict['Engagement Rate'] = float(engagement_rate[0:3])
    myDict['Link Clicks'] = int(link_clicks)
    myDict['Retweets'] = int(retweets)
    myDict['Likes'] = int(likes)
    myDict['Replies'] = int(replies)
    myDict['Posts'] = posts
    myDict['Followers'] = followers
    
    return myDict


import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# this function is not needed anymore
def InstagramScraping():
    with open('./Cred.json') as f:
        data = json.load(f)

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome('./chromedriver.exe')

    driver.get('https://www.tanke.fr/en/instagram-engagement-rate-calculator-2/')
    time.sleep(2)

    instaId = driver.find_element_by_name('pseudo')
    instaId.send_keys('nyaayaorg')
    analyseButton = driver.find_element_by_xpath('//*[@id="pseudoform"]/p[2]/input')
    analyseButton.click()
    time.sleep(5)
    engagementRate = driver.find_element_by_id('engrate').text
    return engagementRate


def InstagramInsights():
    with open('./Cred.json') as f:
        data = json.load(f) 

    user_access_token_i = data['Instagram']['UserAccessToken']
    metric1_i = 'impressions'
    metric2_i = 'reach'
    metric3_i = 'followers_count'
    user_id_i = data['Instagram']['UserID']
    user_access_token = data['Facebook'][2]['UserAccessToken']

    url_i1 = 'https://graph.facebook.com/v6.0/'+user_id_i+'/insights?metric='+metric1_i+','+metric2_i+'&period=week&access_token='+user_access_token_i
    url_i2 = 'https://graph.facebook.com/v6.0/'+user_id_i+'?fields='+metric3_i+'&access_token='+user_access_token_i
    url_i3 = 'https://graph.facebook.com/v6.0/'+user_id_i+'?fields=business_discovery.username(nyaayaorg){media_count}&access_token='+user_access_token

    response_i1 = requests.get(url_i1)
    response_i2 = requests.get(url_i2)
    response_i3 = requests.get(url_i3)

    # print(response_i1)
    # print(response_i2)
    # print(response_i3)

    jsonResponse_i1 = response_i1.json()
    jsonResponse_i2 = response_i2.json()
    jsonResponse_i3 = response_i3.json()
    print(jsonResponse_i1)
    print(jsonResponse_i2)
    print(jsonResponse_i3)

    myDict_i = {}

    myData_i = jsonResponse_i1['data']

    for obj in myData_i:
        if obj['name'] == 'impressions':
            myDict_i['Impressions'] = obj['values'][0]['value']
        elif obj['name'] == 'reach':
            myDict_i['Reach'] = obj['values'][0]['value']
            myDict_i['Date'] = obj['values'][1]['end_time'][0:10]

    myDict_i['Total Followers'] = jsonResponse_i2['followers_count']
    myDict_i['Total Posts'] = jsonResponse_i3['business_discovery']['media_count']
    # engagementRate = InstagramScraping()
    # myDict_i['Engagement Rate'] = engagementRate
    url_i4 = 'https://graph.facebook.com/v10.0/'+user_id_i+'/media?access_token='+user_access_token_i
    response_i4 = requests.get(url_i4)
    # print(response_i4)
    jsonResponse_i4 = response_i4.json()
    print(jsonResponse_i4)
    instagram_posts_ids = jsonResponse_i4['data']
    i = 0
    engagement_sum = 0
    for id in instagram_posts_ids:
        if(i < 5):
            i += 1
            continue
        insta_id = id['id']
        insta_media_url = "https://graph.facebook.com/v10.0/"+str(insta_id)+"/insights?metric=engagement&access_token="+user_access_token_i
        insta_media_response = requests.get(insta_media_url)
        jsonResponse_insta_media = insta_media_response.json()
        # print(jsonResponse_insta_media)
        engagement_sum += jsonResponse_insta_media['data'][0]['values'][0]['value']
        i += 1
    # return myDict_i
    total_engagement = engagement_sum / 200
    print(total_engagement)
    myDict_i['Engagement Rate'] = total_engagement
    # print("MyInstaData")
    # print(myDict_i)
    return myDict_i

if __name__=="__main__":
    InstagramInsights()
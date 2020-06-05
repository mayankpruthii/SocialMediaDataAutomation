import requests
import json

# Fetching English Facebook Page Data

def FacebookInsightsEnglishSite():   
  
    with open('./Cred.json') as f:
        data = json.load(f) 
  
    english_page_access_token = data['Facebook'][0]['English']['pageToken']
    metric1 = 'page_fans'
    metric2 = 'page_engaged_users'
    metric3 = 'page_impressions_organic_unique'
    metric4 = 'page_impressions_paid_unique'
    english_page_id = data['Facebook'][0]['English']['pageId']

    url_english = "https://graph.facebook.com/v6.0/"+english_page_id+"/insights?metric="+metric1+','+metric2+','+metric3+','+metric4+'&access_token='+english_page_access_token
    url_english1 = "https://graph.facebook.com/v6.0/"+english_page_id+"?fields=id,name,fan_count&access_token="+english_page_access_token
    url_english2 = "https://graph.facebook.com/v6.0/"+english_page_id+"?fields=published_posts.limit(1).summary(total_count).since(1)&access_token="+english_page_access_token

    response = requests.get(url_english)
    response1 = requests.get(url_english1)
    response2 = requests.get(url_english2)
    # print(response)
    # print(response1)
    # print(response2)
    
    jsonResponse = response.json()
    jsonResponse1 = response1.json()
    jsonResponse2 = response2.json()

    myData = jsonResponse['data']

    myDict = {}

    for obj in myData:
        if obj['period'] == 'week':
            
            if obj['name'] == 'page_impressions_organic_unique':
                myDict['Organic Reach'] = obj['values'][1]['value']
            
            elif obj['name'] == 'page_impressions_paid_unique':
                myDict['Paid Reach'] = obj['values'][1]['value']
            
            elif obj['name'] == 'page_engaged_users':
                myDict['Users Engaged'] = obj['values'][1]['value']
                
        myDict['Date'] = obj['values'][1]['end_time'][0:10]
        
    myDict['Total Likes'] = jsonResponse1['fan_count']
    myDict['Total Posts'] = jsonResponse2['published_posts']['summary']['total_count']

    return myDict


# Fetching Hindi Facebook page data

def FacebookInsightsHindiSite():

    with open('./Cred.json') as f:
        data = json.load(f) 

    hindi_page_access_token = data['Facebook'][1]['Hindi']['pageToken']
    metric1 = 'page_fans'
    metric2 = 'page_engaged_users'
    metric3 = 'page_impressions_organic_unique'
    metric4 = 'page_impressions_paid_unique'
    hindi_page_id = data['Facebook'][1]['Hindi']['pageId']

    url_h = "https://graph.facebook.com/v6.0/"+hindi_page_id+"/insights?metric="+metric1+','+metric2+','+metric3+','+metric4+'&access_token='+hindi_page_access_token
    url_h1 = "https://graph.facebook.com/v6.0/"+hindi_page_id+"?fields=id,name,fan_count&access_token="+hindi_page_access_token
    url_h2 = "https://graph.facebook.com/v6.0/"+hindi_page_id+"?fields=published_posts.limit(1).summary(total_count).since(1)&access_token="+hindi_page_access_token

    response_h = requests.get(url_h)
    response_h1 = requests.get(url_h1)
    response_h2 = requests.get(url_h2)

    print(response_h)
    print(response_h1)
    print(response_h2)

    jsonResponse_h = response_h.json()
    jsonResponse_h1 = response_h1.json()
    jsonResponse_h2 = response_h2.json()

    myData_h = jsonResponse_h['data']

    myDict_h = {}

    for obj in myData_h:
        if obj['period'] == 'week':
            
            if obj['name'] == 'page_impressions_organic_unique':
                myDict_h['Organic Reach'] = obj['values'][1]['value']
            
            elif obj['name'] == 'page_impressions_paid_unique':
                myDict_h['Paid Reach'] = obj['values'][1]['value']
            
            elif obj['name'] == 'page_engaged_users':
                myDict_h['Users Engaged'] = obj['values'][1]['value']
                
        myDict_h['Date'] = obj['values'][1]['end_time'][0:10]
        
    myDict_h['Total Likes'] = jsonResponse_h1['fan_count']
    myDict_h['Total Posts'] = jsonResponse_h2['published_posts']['summary']['total_count']

    return myDict_h
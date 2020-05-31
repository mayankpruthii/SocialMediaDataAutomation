import requests
import json

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

    print(response_i1)
    print(response_i2)
    print(response_i3)

    jsonResponse_i1 = response_i1.json()
    jsonResponse_i2 = response_i2.json()
    jsonResponse_i3 = response_i3.json()
    print(jsonResponse_i2)

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

    return myDict_i
import requests
import json
from datetime import date, datetime, timedelta

def FacebookIndividualPostInsights(pageObject, facebookStr):
    with open('./Cred.json') as f:
        data = json.load(f) 
    
    if(facebookStr == "english"):
        page_access_token = data['Facebook'][0]['English']['pageToken']
        page_id = data['Facebook'][0]['English']['pageId']
    elif(facebookStr == "hindi"):
        page_access_token = data['Facebook'][1]['Hindi']['pageToken']
        page_id = data['Facebook'][1]['Hindi']['pageId']
    else:
        print("not epic")
        return

    url = "https://graph.facebook.com/"+page_id+"/feed?access_token="+page_access_token
    todayDate = date.today();
    response = requests.get(url)
    jsonResponse = response.json()
    allPosts = jsonResponse["data"]
    counter = 0
    # print(len(allPosts))
    result = []
    for post in allPosts:
        created_at = post["created_time"][0:10]
        dateObj = datetime.strptime(created_at, '%Y-%m-%d').date()
        if(date.today()-timedelta(days=14) > dateObj):
            break
        myDict = {}   
        post_page_Id = post["id"]
        pageFeedItemUrl = "https://graph.facebook.com/v6.0/"+post_page_Id 
        
        # Title and Shares
        postTitleUrl = pageFeedItemUrl+"?fields=message,shares&access_token="+page_access_token
        postTitle = requests.get(postTitleUrl)
        postTitleResAndShares = postTitle.json()
        postTitleRes = postTitleResAndShares["message"][0:30] + "..."
        myDict["Id"] = post_page_Id
        myDict["Link"] = "https://facebook.com/" + post_page_Id
        myDict["Title"] = postTitleRes
        # print(postTitleRes)
        postShares = 0

        try:
            if(postTitleResAndShares["shares"]):
                postShares = postTitleResAndShares["shares"]["count"]
        except:
            None

        # Comments Likes
        commentsOnPost = pageFeedItemUrl + "/comments"+"?summary=true&access_token="+page_access_token
        commentRes = requests.get(commentsOnPost)
        jsonComment = commentRes.json()["summary"]["total_count"]
        likesOnPost = pageFeedItemUrl + "/likes?summary=true&access_token="+page_access_token
        likesRes = requests.get(likesOnPost)
        jsonLikes = likesRes.json()["summary"]["total_count"]
        myDict["Likes"] = jsonLikes
        myDict["Comments"] = jsonComment
        myDict["Shares"] = postShares
        
        # Reach
        reachUrl = pageFeedItemUrl + "/insights?fields=limit(100)&metric=post_impressions_organic,post_impressions_paid,post_clicks,post_engaged_users&access_token=" +page_access_token
        reachRes = requests.get(reachUrl)
        jsonReach = reachRes.json()["data"]
        print(jsonReach)
        organicReach = jsonReach[0]["values"][0]["value"]
        myDict["Organic Reach"] = organicReach

        inorganicReach = jsonReach[1]["values"][0]["value"]
        myDict["Paid Reach"] = inorganicReach
        
        totalReach = int(organicReach) + int(inorganicReach)
        myDict["Total Reach"] = totalReach
        
        postClicks = int(jsonReach[2]["values"][0]["value"])
        myDict["Post Clicks"] = postClicks
        
        fbClickThroughRate = postClicks * 100 / totalReach
        myDict["Click Through Rate"] = fbClickThroughRate

        totalEngagement = int(jsonReach[3]["values"][0]["value"])
        myDict["Total Engagement"] = totalEngagement

        followerCount = pageObject["Follower Count"]
        myDict["Followers"] = followerCount

        engagementRate = totalEngagement / followerCount * 100
        myDict["Engagement Rate"] = engagementRate
        
        result.append(myDict)
        
        counter += 1
        print("counter", counter)

    print("All done!")
    return result

# Fetching English Facebook Page Data

def FacebookInsightsSite(lang):   
  
    with open('./Cred.json') as f:
        data = json.load(f) 
  
    if(lang=="Hindi"):
        page_access_token = data['Facebook'][1]['Hindi']['pageToken']
        page_id = data['Facebook'][1]['Hindi']['pageId']
    else:
        page_access_token = data['Facebook'][0]['English']['pageToken']
        page_id = data['Facebook'][0]['English']['pageId']

    metric1 = 'page_fans'
    metric2 = 'page_engaged_users'
    metric3 = 'page_impressions_organic_unique'
    metric4 = 'page_impressions_paid_unique'

    url = "https://graph.facebook.com/v6.0/"+page_id+"/insights?metric="+metric1+','+metric2+','+metric3+','+metric4+'&access_token='+page_access_token
    url1 = "https://graph.facebook.com/v6.0/"+page_id+"?fields=id,name,fan_count,followers_count&access_token="+page_access_token
    weekBeforeDate = date.today()-timedelta(days=7)
    url2 = "https://graph.facebook.com/v6.0/"+page_id+"?fields=published_posts.limit(100).summary(total_count).since("+ str(weekBeforeDate) +")&access_token="+page_access_token
    response = requests.get(url)
    response1 = requests.get(url1)
    response2 = requests.get(url2)

    print(response)
    print(response1)
    print(response2)
    
    jsonResponse = response.json()
    jsonResponse1 = response1.json()
    jsonResponse2 = response2.json()

    print(jsonResponse)
    print(jsonResponse1)
    print(jsonResponse2)

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
    myDict['Follower Count'] = jsonResponse1['followers_count']
    myDict['Total Posts'] = jsonResponse2['published_posts']['summary']['total_count']

    return myDict

if __name__=="__main__":
    resultArray = FacebookIndividualPostInsights({"Follower Count": 1000}, "hindi")
    for arrItem in resultArray:
        print(arrItem)
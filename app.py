import gspread
import gspread.models
from oauth2client.service_account import ServiceAccountCredentials
import json
from dictsheet import DictSheet

from TwitterDataFetch import TwitterDataFetch
# from FacebookDataFetch import FacebookInsightsEnglishSite
from FacebookDataFetch import FacebookInsightsSite
# from FacebookDataFetch import FacebookIndividualPostInsights
from InstagramDataFetch import InstagramInsights, InstagramPostInsights

# from MediumStats import MyMediumStats

with open('./Cred.json') as f:
        data = json.load(f)

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets' ,'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('myGoogleAPI.json', scope)

gc = gspread.authorize(credentials)

my_spreadsheet = gc.open(data['Gspread']['SpreadsheetName'])

###########################################################

# Twitter Data Automation
twitter_data = TwitterDataFetch()
print(twitter_data)
twitterWks = my_spreadsheet.worksheet('Twitter')
dict_TwitterWks = DictSheet(wks = twitterWks)
dict_TwitterWks.append(twitter_data)

print('Twitter Scraping Done!')

# Facebook English Data Automation
facebook_data_english = FacebookInsightsSite(lang="English")
print(facebook_data_english)
FacebookWks = my_spreadsheet.worksheet('Facebook')
dict_FacebookWks = DictSheet(wks = FacebookWks)
dict_FacebookWks.append(facebook_data_english)

###########################################################

# Facebook Hindi Data Automation
facebook_data_hindi = FacebookInsightsSite(lang="Hindi")
print(facebook_data_hindi)
FacebookHindiWks = my_spreadsheet.worksheet('FacebookHindi')
dict_FacebookWks = DictSheet(wks = FacebookHindiWks)
dict_FacebookWks.append(facebook_data_hindi)

print("Facebook Done!")

###########################################################

# Individual Facebook English Content
# facebookEnglishDataArray = FacebookIndividualPostInsights(facebook_data_english, "english")
# print("Individual Post done")
# FacebookEnglishPostsWks = my_spreadsheet.worksheet("FacebookEnglishPosts")
# dict_FacebookPostsWks = DictSheet(wks = FacebookEnglishPostsWks)
# for item in facebookEnglishDataArray:
#         dict_FacebookPostsWks.append(item)

###########################################################

# Individual Facebook Hindi Content
# facebookHindiDataArray = FacebookIndividualPostInsights(facebook_data_hindi, "hindi")
# print("Individual Post done")
# FacebookHindiPostsWks = my_spreadsheet.worksheet("FacebookHindiPosts")
# dict_FacebookHindiPostsWks = DictSheet(wks = FacebookHindiPostsWks)
# for item in facebookHindiDataArray:
#         dict_FacebookHindiPostsWks.append(item)

###########################################################

# Instagram Data Automation
instagram_data = InstagramInsights()
InstagramWks = my_spreadsheet.worksheet('Instagram')
dict_InstagramWks = DictSheet(wks = InstagramWks)
dict_InstagramWks.append(instagram_data)

###########################################################

# Instagram Individual Post Automation
# instagram_posts_data = InstagramPostInsights()
# InstagramPostsWks = my_spreadsheet.worksheet('InstagramPosts')
# dict_InstagramPostsWks = DictSheet(wks = InstagramPostsWks)
# for item in instagram_posts_data:
#         print(item)
#         dict_InstagramPostsWks.append(item)

print('All Done!')

import gspread
import gspread.models
from oauth2client.service_account import ServiceAccountCredentials
import json
from dictsheet import DictSheet

from TwitterDataFetch import TwitterDataFetch
from FacebookDataFetch import FacebookInsightsEnglishSite
from FacebookDataFetch import FacebookInsightsHindiSite
from InstagramDataFetch import InstagramInsights
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
facebook_data_english = FacebookInsightsEnglishSite()
print(facebook_data_english)
FacebookWks = my_spreadsheet.worksheet('Facebook')
dict_FacebookWks = DictSheet(wks = FacebookWks)
dict_FacebookWks.append(facebook_data_english)

###########################################################

# Facebook Hindi Data Automation
facebook_data_hindi = FacebookInsightsHindiSite()
print(facebook_data_hindi)
FacebookHindiWks = my_spreadsheet.worksheet('FacebookHindi')
dict_FacebookWks = DictSheet(wks = FacebookHindiWks)
dict_FacebookWks.append(facebook_data_hindi)

###########################################################

# Instagram Data Automation
instagram_data = InstagramInsights()
print(instagram_data)
InstagramWks = my_spreadsheet.worksheet('Instagram')
dict_InstagramWks = DictSheet(wks = InstagramWks)
dict_InstagramWks.append(instagram_data)

print('Done!')

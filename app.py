import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
from dictsheet import DictSheet

from TwitterDataFetch import TwitterDataFetch
from FacebookDataFetch import FacebookInsightsEnglishSite
from FacebookDataFetch import FacebookInsightsHindiSite
from InstagramDataFetch import InstagramInsights
from MediumStats import MediumStatsScraper

with open('./Cred.json') as f:
        data = json.load(f)

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets' ,'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('myGoogleAPI.json', scope)

gc = gspread.authorize(credentials)

my_spreadsheet = gc.open(data['Gspread']['SpreadsheetName'])

twitter_data = TwitterDataFetch()
print(twitter_data)
twitterWks = my_spreadsheet.worksheet('Twitter')
dict_TwitterWks = DictSheet(wks = twitterWks)
dict_TwitterWks.append(twitter_data)

print('Twitter Scraping Done!')

medium_data = MediumStatsScraper()
print(medium_data)
mediumWks = my_spreadsheet.worksheet('Medium')
dict_mediumWks = DictSheet(wks = mediumWks)
dict_mediumWks.append(medium_data)

print('Medium Scraping Done!')

facebook_data_english = FacebookInsightsEnglishSite()
print(facebook_data_english)
FacebookWks = my_spreadsheet.worksheet('Facebook')
dict_FacebookWks = DictSheet(wks = FacebookWks)
dict_FacebookWks.append(facebook_data_english)

facebook_data_hindi = FacebookInsightsHindiSite()
print(facebook_data_hindi)
FacebookHindiWks = my_spreadsheet.worksheet('FacebookHindi')
dict_FacebookWks = DictSheet(wks = FacebookHindiWks)
dict_FacebookWks.append(facebook_data_hindi)

instagram_data = InstagramInsights()
print(instagram_data)
InstagramWks = my_spreadsheet.worksheet('Instagram')
dict_InstagramWks = DictSheet(wks = InstagramWks)
dict_InstagramWks.append(instagram_data)

print('Done!')
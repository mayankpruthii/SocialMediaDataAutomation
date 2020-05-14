from TwitterDataFetch import TwitterDataFetch
from FacebookDataFetch import FacebookInsightsEnglishSite
from FacebookDataFetch import FacebookInsightsHindiSite

twitter_data = TwitterDataFetch()
print(twitter_data)

facebook_data_english = FacebookInsightsEnglishSite()
print(facebook_data_english)

facebook_data_hindi = FacebookInsightsHindiSite()
print(facebook_data_hindi)
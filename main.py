import gspread
from twitter import *

gc = gspread.service_account('credentials.json')
token = 'xxxxxXXXXXXXXyyyyyyyyyyYYYYYYYYYYYYYYY'
token_secret = 'CcccccccccccccDDDDddddddiuefoiwhgqkebfgqeugfowqhgv.kwEBVg'
consumer_key = 'skjhrfgowughwbvgoqwhfpq;jf'
consumer_secret = 'sjuhgfoqbegvkwiuO;TYGUqopefb.wkUHGFPQIFR'

t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))
    
    # Get your "home" timeline
t.statuses.home_timeline()

# Open a sheet from a spreadsheet in one go
wks = gc.open("Twitter-Bot").sheet1

# Update a range of cells using the top left corner address
next_tweet  = wks.acell('A2').value

#post tweet through twitter API
t.statuses.update(
    status= next_tweet)


# delete row on success   
wks.delete_rows(2)


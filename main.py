import gspread
from twitter import *

gc = gspread.service_account('credentials.json')
token = '1481574931645472770-piSZzU4GzyNiwI3cknFKh4jjOngiwt'
token_secret = 'y1s3U1FdqipD2MphFfmy5ZkHs6nyw7KsBYekyZLqhrXLq'
consumer_key = 'jIwmZbk3cXKyKXWLJQ54Db3km'
consumer_secret = 'f5gh6QzVvugMoMQDMSXCBHBCwz9N3qoWlkCFD7ruUeBh8TRxjC'

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


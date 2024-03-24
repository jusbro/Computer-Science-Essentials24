#NASA API APOD With Date Selection

#In this activity, you will add a feature to request a date from the user.
#that date will be sent to APOD, and APOD will send back the photo from that date
#This should work for any date from today all the way back to June 16, 1995
#PLEASE KNOW: This program will crash if one of the few videos they uploaded is requested...It will only work for photos

#IMPORTS
import requests
from PIL import Image
from io import BytesIO

def fetch_apod(base_url, api_key, date_to_search):
    #concatenate a url with the base_url, your api key, and the extra parameters for the desired date
    #This is the format your url request should be:
    #https://api.nasa.gov/planetary/apod?api_key=YOUR_API_KEY&date=YYYY-MM-DD
    url = 
    print(url)
    response = requests.get(url)
    data = response.json()
    return data

#base_url is the beginning of the url that we will go to for our APOD
base_url = "https://api.nasa.gov/planetary/apod?api_key="
#below, paste your NASA API Key.
api_key = "YOUR KEY HERE"
date_to_search = #Finish this code
apod_data = fetch_apod(#finish this code)

#if the response we get back has a 'url'...
if 'url' in apod_data:
    print("Title:", apod_data['title'])
    print("Date:", apod_data['date'])
    print("Explanation:", apod_data['explanation'])
    print("HD URL:", apod_data.get('hdurl', "Not available"))
    print("URL:", apod_data['url'])

    # Open and display the image
    response = requests.get(apod_data['url'])
    image = Image.open(BytesIO(response.content))
    image.show()
#otherwise, if it did not have a url...
else:
    print("Error:", apod_data.get('msg', 'Unknown error'))


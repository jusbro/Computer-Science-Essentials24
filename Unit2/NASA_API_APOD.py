#This program will introduce you to APIs (APPLICATION PROGRAMMING INTERFACE)

#In this program, you will obtain a NASA API Key for yourself, finish coding below to make an APOD request, then display that image on your screen

#Part 1: Obtain a NASA API. 
#Use the link below to go to NASA's API creation page. Use your school email to create an API
#DO NOT LOOSE THIS API KEY!!!!!!!!!
#It is recommended that you make a .txt file in your VS code that allows you to copy your personal code in the event you loose yours\

#https://api.nasa.gov/
#HINT: Ctrl + mouse click that comment to open the link

#CODE BEGINS BELOW

#NASA API APOD Practice

#IMPORTS

#requests is a library we will use to make HTTP requests
import requests
#PIL stands for "Photo Imaging Library". We will use it to display our image
from PIL import Image
#io means Input/Output. BytesIO allows us to store information and recall it. It is like an advanced variable.
from io import BytesIO

#fetch_apod function makes the request through the internet to get our APOD data
def fetch_apod(base_url, api_key):
    #concatenate a url with the base_url and your api key.
    url = base_url+api_key
    #store the url response as a variable called "response" using the requests library
    response = requests.get(url)
    #The data we get back is a "JSON" file, a very common method of sending data. We need to "translate it" so we can do something with it.
    data = response.json()
    #send the data to the main loop
    return data

#base_url is the beginning of the url that we will go to for our APOD
base_url = "https://api.nasa.gov/planetary/apod?api_key="
#below, paste your NASA API Key.
api_key = "YOUR KEY GOES IN THESE QUOTES"
apod_data = fetch_apod(base_url,api_key)

#if the response we get back has a 'url', then we probably got a legit response...If not, go to the 'else' below cause somethin dun messed up good
if 'url' in apod_data:
    #Thanks to our data being a JSON, it is easy to sort through and find key words
    #First, find the 'title' in the data and print the data that comes after it
    print("Title:", apod_data['title'])
    #Then, look for date and... well  you probably know the rest...
    print("Date:", apod_data['date'])
    print("Explanation:", apod_data['explanation'])
    print("HD URL:", apod_data.get('hdurl', "Not available"))
    print("URL:", apod_data['url'])

    # Open and display the image
    response = requests.get(apod_data['url'])
    image = Image.open(BytesIO(response.content))
    image.show()
else:
    print("Error:", apod_data.get('msg', 'Unknown error'))

#DID IT WORK? If so, try viewing the raw data using Chrome!
#Copy and paste the base_url (not the ""!) and copy and paste your API key after it, press enter, and see what the raw data looks like.
#Aren't you glad you could make a program to sort through that data for you?

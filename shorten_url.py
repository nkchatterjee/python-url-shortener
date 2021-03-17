import os
from dotenv import load_dotenv
from pyshorteners import Shortener 

load_dotenv()
ACCESS_TOKEN = os.environ.get("MY_ACCESS_TOKEN")

answer = input("Do you want to shorten or expand your URL? ") 

# Shorten long URL
if answer.lower() == 'shorten':
  long_url = input("Enter the URL you wish to shorten: ")
  url_shortener = Shortener(api_key = ACCESS_TOKEN) 
  print("Short URL is {}".format(url_shortener.bitly.short(long_url)))

# Expand short URL
elif answer.lower() == 'expand':
  short_url = input("Enter the short URL you wish to expand: ")
  url_expander = Shortener(api_key = ACCESS_TOKEN)
  print("Long URL is {}".format(url_expander.bitly.expand(short_url)))

else: 
  print("Please run the program again and specify if you'd like to shorten or expand your URL")
from scraper_api import ScraperAPIClient
from bs4 import BeautifulSoup as b4
import tkinter as tk
client = ScraperAPIClient('499f6c0c23ea1af3fddf96587890d93d')

srch = input("Enter your sentence or text: ")

srch = srch.split(" ")
srch = "+".join(srch)
result = client.get(url = 'https://www.google.com/search?q=%s&oq=%s&aqs=edge..69i57j0i13j0i13i30l5.16351j0j1&sourceid=chrome&ie=UTF-8' %(srch, srch)).text
soup = b4(result, 'html.parser')
soup = soup.find_all("a", class_ ="gL9Hy")
try:
    soup = soup[0]
    soup = soup.get_text()
    print(soup)
except: print("We could not find any problem for fixing in your text ! :) (if it's not true and you belife that your text have problem , try that word in sentence)")

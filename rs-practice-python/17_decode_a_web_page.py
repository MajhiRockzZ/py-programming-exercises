"""
---------------------------------------------------------
Exercise 17 :
---------------------------------------------------------
Use the BeautifulSoup and requests Python packages to
print out a list of all the article titles on the New
York Times homepage[].
---------------------------------------------------------
Concepts :
---------------------------------------------------------
    1. Libraries
    2. requests
    3. BeautifulSoup
---------------------------------------------------------
 """
from bs4 import BeautifulSoup
import requests
url = "http://github.com"
r = requests.get(url)
r_html = r.text
print(r_html)
soup = BeautifulSoup(r_html)
title = soup.find("span", "articletitle").string
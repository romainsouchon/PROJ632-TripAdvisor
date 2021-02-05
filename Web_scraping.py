# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:03:40 2021

@author: Romain
"""

import requests
from bs4 import BeautifulSoup
import re

URL = 'https://www.tripadvisor.fr/Restaurant_Review-g8309764-d968592-Reviews-Brasserie_le_Z-Chambery_Savoie_Auvergne_Rhone_Alpes.html'
res = re.split('Reviews',URL)
res[0] += 'Reviews'

req = requests.get(URL)
soup = BeautifulSoup(req.text, "lxml")

soup.title
# <title>BRASSERIE LE Z, Chambéry - Menu, Prix, Restaurant Avis &amp; Réservations - Tripadvisor</title>
 
soup.title.name
# 'title'
 
soup.title.string
# 'BRASSERIE LE Z, Chambéry - Menu, Prix, Restaurant Avis & Réservations - Tripadvisor'

users = soup.find_all('div', {'class' : 'info_text pointer_cursor'})

review = soup.find_all('p', {'class' : 'partial_entry'})

notes = soup.find_all('span', {'class' : 'ui_bubble_rating'})

date = soup.find_all('span', {'class' : 'ratingDate'})

#notes des avis clean
review_notes = []
for note in notes[5:15]:
    review_notes.append(str(note)[37:39])

for i in range(0, len(review_notes)):
    review_notes[i] = int(review_notes[i])//10
    
for i in range(0, len(users)-1):
    print (users[i].string)
    print (review_notes[i],'/ 5')
    print (review[i].string,'\n\n')

    
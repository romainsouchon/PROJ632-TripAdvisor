# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:03:40 2021

@author: Romain
"""

import requests
from bs4 import BeautifulSoup


req = requests.get('https://www.tripadvisor.fr/Restaurant_Review-g8309764-d968592-Reviews-Brasserie_le_Z-Chambery_Savoie_Auvergne_Rhone_Alpes.html')
soup = BeautifulSoup(req.text, "lxml")

soup.title
# <title>BRASSERIE LE Z, Chambéry - Menu, Prix, Restaurant Avis &amp; Réservations - Tripadvisor</title>
 
soup.title.name
# 'title'
 
soup.title.string
# 'BRASSERIE LE Z, Chambéry - Menu, Prix, Restaurant Avis & Réservations - Tripadvisor'

users = soup.find_all('div', {'class' : 'info_text pointer_cursor'})

review = soup.find_all('p', {'class' : 'partial_entry'})

note = soup.find_all('span', {'class' : 'ui_bubble_rating'})


for i in range(0, len(users)-1):
    print (users[i].string)
    print (review[i].string,'\n\n')
    

"""review = soup.find_all('p', {'class' : 'partial_entry'})
for i in range(0, len(review)-1):
    print ('review', i+1,'\n', review[i].string)"""
    
print(len(review))
print(len(users))
print(len(note))
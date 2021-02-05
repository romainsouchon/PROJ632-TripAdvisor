# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:03:40 2021

@author: Romain
"""

import requests
from bs4 import BeautifulSoup
import re

URL = 'https://www.tripadvisor.fr/Restaurant_Review-g8309764-d968592-Reviews-or30-Brasserie_le_Z-Chambery_Savoie_Auvergne_Rhone_Alpes.html'
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

#commentaire par user
com_entier = soup.find_all('div', {'class' : 'ui_column is-9'})
liste_com =[]
for k in range(len(com_entier)):
    com_entier_str=str(com_entier[k])
    indice_debut = com_entier_str.find('<p class="partial_entry">') + 25
    indice_fin1 = com_entier_str.find('</p></div></div><div class="prw_rup prw_reviews_stay_date_hsx" data-prwidget-init="" data-prwidget-name="reviews_stay_date_hsx">')
    indice_fin2 = com_entier_str.find('</p></div></div><div class="prw_rup prw_reviews_inline_photos_hsx" data-prwidget-init="" data-prwidget-name="reviews_inline_photos_hsx">')
    indice_fin3 = com_entier_str.find('''<span class="taLnk ulBlueLinks" onclick="widgetEvCall('handlers.clickExpand',event,this);">Plus</span>''')
    if indice_fin3 != -1:
        indice_fin = indice_fin3
    else:
        indice_fin=max(indice_fin1,indice_fin2)
    com = com_entier_str[indice_debut:indice_fin]
    liste_com.append(com)

#notes des avis clean
review_notes = []
for note in notes[5:15]:
    review_notes.append(str(note)[37:39])

for i in range(0, len(review_notes)):
    review_notes[i] = int(review_notes[i])/10
    
    
commentaires = []   #ajout de la liste commentaires
for i in range(0,len(users)):                 #un Dico = un avis
    avis = {"pseudo" : users[i].string,         #Avec le pseudo
            "note" : review_notes[i],           #La note sur 5
            "commentaire" : liste_com[i],       #Le com
            "date" : date[i].string}            #La date

    
    commentaires.append(avis)
    
for i in commentaires:
    print(i, "\n\n")
    
    
print(commentaires[2].get("pseudo"))

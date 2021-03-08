# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:51:04 2021

@author: cleme
"""
import requests
from bs4 import BeautifulSoup

        
URL = 'https://www.tripadvisor.fr/Restaurant_Review-g8309764-d968592-Reviews-or490-Brasserie_le_Z-Chambery_Savoie_Auvergne_Rhone_Alpes.html'


page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

#users
users = soup.find_all('div', {'class' : 'info_text pointer_cursor'})


#review
review = soup.find_all('p', {'class' : 'partial_entry'})


#note
notes = soup.find_all('span', {'class' : 'ui_bubble_rating'})

#notes des avis clean
review_notes = []
for note in notes[5:15]:
    review_notes.append(str(note)[37:39])

#date
date = soup.find_all('span', {'class' : 'ratingDate'})

#end_page : la dernière page
#dans ce programme elle est inutile 
end_page = soup.find_all('a' , {'class' : 'pageNum last'})

num_end_page = []
for page in end_page:
    num_end_page.append(str(page)[60:62])
print(num_end_page)

    
    

#il manque le tri des avis patron/utilisateurs


for i in range(0, len(users)):
            print (users[i].string, '\n')
            #print ('note :',review_notes[i], '\n')
            #print (review[i].string, '\n\n')
            



        
      




 
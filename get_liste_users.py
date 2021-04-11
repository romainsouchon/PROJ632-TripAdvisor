# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:51:04 2021

@author: cleme
"""
import requests
from bs4 import BeautifulSoup
import re

liste_users = []

def first_search(soup):
#    print('-----------------------------------------')
#    print('on est à la page :', int(soup.find('a', {'class' : re.compile('current')}).string))
    
    
    #users
    users = soup.find_all('div', {'class' : 'info_text pointer_cursor'})
        
    for i in range(0, len(users)):
        #all_users.append(users[i].string)
        #print (users[i].string)
        liste_users.append(users[i].string)
        
    

        
        
        
#Brasserie le Z   
URL = 'https://www.tripadvisor.fr/Restaurant_Review-g8309764-d968592-Reviews-Brasserie_le_Z-Chambery_Savoie_Auvergne_Rhone_Alpes.html'

#Resto Leo Paul
#URL = 'https://www.tripadvisor.fr/Restaurant_Review-g187259-d20059901-Reviews-Restaurant_Leo_Paul-Aix_les_Bains_Savoie_Auvergne_Rhone_Alpes.html'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

nbre_de_pages = int(soup.find('a' , {'class' : 'pageNum last'}).string)



first_search(soup)

def all_search():      
    for i in range(10,(nbre_de_pages)*10,10):
        #Brasserie le Z
        URL_reviews = 'https://www.tripadvisor.fr/Restaurant_Review-g8309764-d968592-Reviews-or' + str(i) + '-Brasserie_le_Z-Chambery_Savoie_Auvergne_Rhone_Alpes.html'
        #Resto Leo Paul
        # URL_reviews = 'https://www.tripadvisor.fr/Restaurant_Review-g187259-d20059901-Reviews-or' + str(i) + '-Restaurant_Leo_Paul-Aix_les_Bains_Savoie_Auvergne_Rhone_Alpes.html'
        

    
        page = requests.get(URL_reviews)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        first_search(soup)
        
    return liste_users
 
print(all_search())
        
    







        
      




 
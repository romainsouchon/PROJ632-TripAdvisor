# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 08:53:13 2021

@author: cleme
"""

import requests
from bs4 import BeautifulSoup
import re
#from get_liste_users import first_search, all_search


#URL = 'https://www.tripadvisor.fr/Restaurant_Review-g8309764-d968592-Reviews-Brasserie_le_Z-Chambery_Savoie_Auvergne_Rhone_Alpes.html'
URL = 'https://www.tripadvisor.fr/Restaurant_Review-g187259-d20059901-Reviews-Restaurant_Leo_Paul-Aix_les_Bains_Savoie_Auvergne_Rhone_Alpes.html'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

nbre_de_pages = int(soup.find('a' , {'class' : 'pageNum last'}).string)






#==============================================================================
review = soup.find_all('p', {'class' : 'partial_entry'})

notes = soup.find_all('span', {'class' : 'ui_bubble_rating'})

date = soup.find_all('span', {'class' : 'ratingDate'})



liste_pseudo = []
    
def get_reviews(soup): 
    #print('-----------------------------------------')
    print('on est à la page :', int(soup.find('a', {'class' : re.compile('current')}).string))
 
    #users
    users = soup.find_all('div', {'class' : 'info_text pointer_cursor'})
    
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
        
    '''
    #notes des avis clean
    review_notes = []
    for note in notes[5:15]:
        review_notes.append(str(note)[37:39])
    
    for i in range(0, len(review_notes)):
        review_notes[i] = int(review_notes[i])/10
     '''   
    
    commentaires = []   #ajout de la liste commentaires
    for i in range(0,len(users)):                 #un Dico = un avis
        avis = {"pseudo" : users[i].string,         #Avec le pseudo
                "note" : review_notes[i],           #La note sur 5
                "commentaire" : liste_com[i],       #Le com
                "date" : date[i].string}            #La date
    
        commentaires.append(avis)
     
    
    
 
    for i in commentaires:
        
        liste_pseudo.append(i['pseudo'])
        print (i, '\n')
        
    
        
        
        
  
  


def get_users():   #cette méthode retourne tous les users des autres pages   
    for i in range(10,(nbre_de_pages)*10,10):
        #Brasserie le Z
        #URL_reviews = 'https://www.tripadvisor.fr/Restaurant_Review-g8309764-d968592-Reviews-or' + str(i) + '-Brasserie_le_Z-Chambery_Savoie_Auvergne_Rhone_Alpes.html'
        URL_reviews = 'https://www.tripadvisor.fr/Restaurant_Review-g187259-d20059901-Reviews-or' + str(i) + '-Restaurant_Leo_Paul-Aix_les_Bains_Savoie_Auvergne_Rhone_Alpes.html'
        page = requests.get(URL_reviews)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        get_reviews(soup)
    
    
#PRINT
      
print(get_reviews(soup))    
a = get_users()
#==============================================================================




















# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 08:29:28 2021

@author: cleme
"""


from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time


#liste_users = all_search()  
liste_users = ['sophiefM9916QJ', 'Dranrebgnal', 'mumu73100', '639minap', 'Nini74100', 'alex p', 'AdrienMi', 'Venture114902', 'caramelmoux73', 'expro73', 'françoise G', 'Mamzelltopi', 'bruno m', 'foodamour69', '318luciler', 'philippemW2539LQ', 'mikado_6', '530fran_oisc', 'gisele-gnv', 'opep2016', 'Memeduquercy', 'RBXY', 'vellea2020', 'gillesd397', 'Lovesavoie', 'jfq2015', 'jfdietlin', 'papinouin', '28silvainb', 'J2661OHjuliac', 'Patrice C', 'tommy2Savoie']

#URL = 'https://www.tripadvisor.fr/Restaurant_Review-g187259-d20059901-Reviews-Restaurant_Leo_Paul-Aix_les_Bains_Savoie_Auvergne_Rhone_Alpes.html'
URL = 'https://www.tripadvisor.fr/Restaurant_Review-g8309764-d968592-Reviews-Brasserie_le_Z-Chambery_Savoie_Auvergne_Rhone_Alpes.html'


page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

  
    


#    print(profil)
def get_uid():
    '''
    recupère l'UID de chaque utilisateur
    '''
    content_uid = soup.find_all("div", {'class' : 'member_info'})
    content_uid_str = str(soup.find_all("div", {'class' : 'member_info'}))
#    print(content_uid[0])
    uid = []
    for part in content_uid:
        
        str_part = str(part)
        
        content = str_part[880:962]
        uid.append(content)
    UID = []   
    for element in uid:
        for car in range(len(element)):
            if element[car] == 'U' and element[car+1] == 'I' and element[car+2] == 'D':
                index = element.index(element[car])
                UID.append(element[index:index + 50])
    
    return UID



def get_url_user(URL,uid):
    '''
    ouvre le navigateur à l'url du restaurant et ouvre la page d'un utilisateur
    pour un uid donné
    '''
    driver = webdriver.Chrome('C:/Users/cleme/OneDrive/Documents/POLYTECH/S6/PROJ632/chromedriver.exe')
    driver.get(URL)
    time.sleep(0.5)
    
    driver.find_element_by_id("_evidon-accept-button").click()
    time.sleep(2)
    #click du widget de l'utilisateur
    all_user_url = []
    
    driver.find_element_by_id(uid).click()
   
    time.sleep(2)
    driver.find_element_by_tag_name('h3').click()
    #ok on ouvre la page de l'utilisateur
    time.sleep(2)    
    current_url = driver.current_url
    all_user_url.append(current_url)
    driver.close()
            
    return current_url



#for uid in get_uid():
#    print(get_url_user(URL,uid))


liste = ['https://www.tripadvisor.fr/Profile/VictorineH9',
         'https://www.tripadvisor.fr/Profile/maurices986',
         'https://www.tripadvisor.fr/Profile/sylvianneb2017',
         'https://www.tripadvisor.fr/Profile/laurentlZ6447SK',
         'https://www.tripadvisor.fr/Profile/207estellel',
         'https://www.tripadvisor.fr/Profile/20Cent91',
         'https://www.tripadvisor.fr/Profile/296davidm',
         'https://www.tripadvisor.fr/Profile/Eyna69',
         'https://www.tripadvisor.fr/Profile/emct800',
         'https://www.tripadvisor.fr/Profile/charlinep122']




    
def extraction_nb_contrib(liste_URL_profils):
    '''Fonction qui prend en argument une liste d'URL de page de profil
    et qui retourne une liste de chaines de caractères indiquant le nombre
    de contribution de chaque pseudo'''
    '''Nécessite l'importation de BeautifulSoup et requests'''
    liste_contributions = []
    for k in range(len(liste_URL_profils)):    
        URL1 = liste_URL_profils[k]
        req = requests.get(URL1) 
        soup = BeautifulSoup(req.content, "html.parser")
        haut_profil = soup.find_all('a', {'class' : '_1q4H5LOk'})
        nb_contributions = str(haut_profil[0])[21:str(haut_profil[0]).find('</a>')]
        pseudo = liste_URL_profils[k][liste_URL_profils[k].find('Profile/')+8:]
        liste_contributions.append("Nombre de contributions de : " + pseudo +" est : " + nb_contributions)
    return liste_contributions


for ext in extraction_nb_contrib(liste):
    print(ext)


# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 08:29:28 2021

@author: cleme
"""

from get_liste_users import all_search
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#liste_users = all_search()  
liste_users = ['sophiefM9916QJ', 'Dranrebgnal', 'mumu73100', '639minap', 'Nini74100', 'alex p', 'AdrienMi', 'Venture114902', 'caramelmoux73', 'expro73', 'françoise G', 'Mamzelltopi', 'bruno m', 'foodamour69', '318luciler', 'philippemW2539LQ', 'mikado_6', '530fran_oisc', 'gisele-gnv', 'opep2016', 'Memeduquercy', 'RBXY', 'vellea2020', 'gillesd397', 'Lovesavoie', 'jfq2015', 'jfdietlin', 'papinouin', '28silvainb', 'J2661OHjuliac', 'Patrice C', 'tommy2Savoie']

URL = 'https://www.tripadvisor.fr/Restaurant_Review-g187259-d20059901-Reviews-Restaurant_Leo_Paul-Aix_les_Bains_Savoie_Auvergne_Rhone_Alpes.html'

#URL = 'https://www.tripadvisor.fr/Profile/'


page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

#profil = soup.find_all('div', {'class' : 'memberOverlayRedesign g10n'})
driver = webdriver.Chrome('C:/Users/cleme/OneDrive/Documents/POLYTECH/S6/PROJ632/chromedriver.exe')
driver.get(URL)
driver.send_keys(Keys.F12)
action = driver.ActionChains(driver)
action.key_down(Keys.F12)

### APPUI SUR F12 pour naviguer et recup les chaine de caractère 

    
    
    

#    print(profil)


def open_browser(URL):
    '''
    ouvre le navigateur à l'url du restaurant
    '''
    driver = webdriver.Chrome('C:/Users/cleme/OneDrive/Documents/POLYTECH/S6/PROJ632/chromedriver.exe')
    driver.get(URL)
    time.sleep(2)
    
    driver.find_element_by_id("_evidon-accept-button").click()
    time.sleep(2)
    #id du widget
    driver.find_element_by_id("UID_CD4024906819CF99E97A82711431183A-SRC_779720233").click()
    
    
    time.sleep(2)
    driver.find_element_by_link_text("").click()
    time.sleep(2)
    current_url = driver.current_url
    return current_url
'''
for us in liste_users:
    print(open_browser(URL,us))   
'''



#open_browser(URL)



    
    
def extraction_nb_contrib(liste_URL_profils):
    liste_contributions = []
    for k in range(len(liste_URL_profils)):
        URL1=liste_URL_profils[k]
        req = requests.get(URL1)
        soup = BeautifulSoup(req.text, "lxml")
        haut_profil = soup.find_all('a', {'class' : '_1q4H5LOk'})
        nb_contributions = str(haut_profil[0])[21:str(haut_profil[0]).find('</a>')]
        pseudo=liste_URL_profils[k][liste_URL_profils[k].find('Profile/')+8:]
        liste_contributions.append("Nombre de contributions de : " + pseudo +" est : " + nb_contributions)
    return liste_contributions




# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 08:29:28 2021

@author: cleme
"""


from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv
import re
#liste_users = all_search()  

#URL = 'https://www.tripadvisor.fr/Restaurant_Review-g187259-d20059901-Reviews-Restaurant_Leo_Paul-Aix_les_Bains_Savoie_Auvergne_Rhone_Alpes.html'
URL = 'https://www.tripadvisor.fr/Restaurant_Review-g8309764-d968592-Reviews-Brasserie_le_Z-Chambery_Savoie_Auvergne_Rhone_Alpes.html'


# page = requests.get(URL)
# soup = BeautifulSoup(page.content, "html.parser")


 


def get_uid(url):
    '''
    recupère l'UID de chaque utilisateur
    '''
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    

    content_uid = soup.find_all("div", {'class' : 'member_info'})
    content_uid_str = str(soup.find_all("div", {'class' : 'member_info'}))
    uid = []
    for part in content_uid:
        
        str_part = str(part)
        
        content = str_part[880:1000]
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

    chrome_path = 'C:/Users/cleme/OneDrive/Documents/POLYTECH/S6/PROJ632/chromedriver.exe'
   
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    
    
    driver = webdriver.Chrome(chrome_path)
    driver.get(URL)
    time.sleep(0.5)
    
    driver.find_element_by_id("_evidon-accept-button").click()
    time.sleep(2)
    #click du widget de l'utilisateur
    all_user_url = []
    
    # driver.find_element_by_id(uid).click()
    driver.find_element_by_id(uid).click()
    time.sleep(2)
    driver.find_element_by_tag_name('h3').click()
    #ok on ouvre la page de l'utilisateur
    time.sleep(2) 
    current_url = driver.current_url   
    all_user_url.append(current_url)
    driver.close()
            
    return current_url


liste_uid = []
with open('liste_url_users.csv', 'r', newline = '') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0])
        liste_uid.append(row[0])

def write_csv():
    '''
    Ecrit dans un csv chaque adresse url des profils des utilisateurs
    '''
    URL = 'https://www.tripadvisor.fr/Restaurant_Review-g8309764-d968592-Reviews-Brasserie_le_Z-Chambery_Savoie_Auvergne_Rhone_Alpes.html'

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")


    nbre_de_pages = int(soup.find('a' , {'class' : 'pageNum last'}).string)

    liste_urls = []
    for i in range(0,(nbre_de_pages)*10,10):
        print('-----------------------------------------')
        print('on est à la page :', int(soup.find('a', {'class' : re.compile('current')}).string))

        pages = 'https://www.tripadvisor.fr/Restaurant_Review-g8309764-d968592-Reviews-or' + str(i) + '-Brasserie_le_Z-Chambery_Savoie_Auvergne_Rhone_Alpes.html'
        page = requests.get(pages)
        soup = BeautifulSoup(page.content, 'html.parser')

        
        for uid in get_uid(pages):
            print(uid, pages)
            liste_urls.append(get_url_user(pages,uid))


    with open('liste_url_users.csv', 'w', newline ='') as file:
        writer = csv.writer(file, delimiter = ';')
        # for row in dictio.keys():
       
        for row in liste_urls:
            writer.writerow([row])

    return 'done'

print(write_csv())




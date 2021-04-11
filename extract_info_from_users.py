import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

import csv

liste_urls = []
with open('liste_url_users.csv', 'r', newline = '') as f:
    reader = csv.reader(f)

    for row in reader:
        liste_urls.append(row[0])



def extraction_nb_contrib(liste_URL_profils):
    '''Fonction qui prend en argument une liste d'URL de page de profil
    et qui retourne une liste de chaines de caractères indiquant le nombre
    de contribution de chaque pseudo'''
    '''Nécessite l'importation de BeautifulSoup et requests'''
    
    cpt = 0
    liste_infos = []
    for k in range(len(liste_URL_profils)): 
        ville_origine=""
        date_creation=""
        cpt += 1 
          
        URL1 = liste_URL_profils[k]
        req = requests.get(URL1) 
        soup = BeautifulSoup(req.content, "html.parser")
        haut_profil = soup.find_all('a', {'class' : '_1q4H5LOk'})
        # nb_contributions = str(haut_profil[0])[21:str(haut_profil[0]).find('</a>')]
        for c in str(haut_profil[0]):
            if c == '>':
                nb_contributions = str(haut_profil[0])[str(haut_profil[0]).index(c)+1:str(haut_profil[0]).find('</a>')]
        pseudo = liste_URL_profils[k][liste_URL_profils[k].find('Profile/')+8:]
        ###
        ville = soup.find_all('span',{'class': '_2VknwlEe _3J15flPT default'})
        ville_origine = str(ville)[str(ville).find('></span>')+8:str(ville)[str(ville).find('></span>')+8:].find('</span>')+str(ville).find('></span>')+8]
        date = soup.find_all('span',{'class': '_1CdMKu4t'})
        date_creation = str(date)[str(date).find('></span>')+8:str(date)[str(date).find('></span>')+8:].find('</span>')+str(date).find('></span>')+8]
        profil = [pseudo, nb_contributions, ville_origine, date_creation]
        liste_infos.append(profil)
        print(profil, cpt)

    return liste_infos


liste_infos_perso = extraction_nb_contrib(liste_urls)
        

with open('infos_from_users.csv', 'w', newline ='', encoding = 'utf8') as file:
    writer = csv.writer(file, delimiter = ';')
    writer.writerow(['Nom', 'Nombre de contribution', '''Ville d'origine''', 'date de création'])
    for row in liste_infos_perso:
        
        writer.writerow(row)
  










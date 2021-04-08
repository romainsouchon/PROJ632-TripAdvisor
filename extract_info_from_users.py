import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

import csv
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
    liste_pseudo = []
    liste_contributions = []
    for k in range(len(liste_URL_profils)):    
        URL1 = liste_URL_profils[k]
        req = requests.get(URL1) 
        soup = BeautifulSoup(req.content, "html.parser")
        haut_profil = soup.find_all('a', {'class' : '_1q4H5LOk'})
        nb_contributions = str(haut_profil[0])[21:str(haut_profil[0]).find('</a>')]
        pseudo = liste_URL_profils[k][liste_URL_profils[k].find('Profile/')+8:]
        liste_pseudo.append(pseudo)
        liste_contributions.append(nb_contributions)
    return liste_pseudo, liste_contributions
    
pseudo_liste = extraction_nb_contrib(liste)[0] 
contrib_liste = extraction_nb_contrib(liste)[1]
total = []

for i in range(len(pseudo_liste)):
    total.append([pseudo_liste[i],contrib_liste[i]])
print(total)

dictio = [['yes', 'no'],['jjj', 'kkk']] 



with open('infos_from_users.csv', 'w', newline ='') as file:
    writer = csv.writer(file, delimiter = ';')
    # for row in dictio.keys():
    writer.writerow(['Nom', 'Nombre de contribution'])
    for row in total:
        writer.writerow(row)
  





    # for row in range(len(liste1)):
    #     col1 = csv.writer(file, delimiter = '\t')
    #     col1.writerows([liste1[row]])
    #     col2 = csv.writer(file, delimiter = '\t')
    #     col2.writerows([liste2[row]])
            




            







    
    






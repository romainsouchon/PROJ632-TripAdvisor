# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:43:56 2021

@author: Romain
"""

import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher
import csv
'''
this program returns all the reviews that a user made
'''


URL = 'https://www.tripadvisor.fr/Profile/207estellel'


def prend_entre(chaine, debut, fin):
    pos1 = chaine.find(debut)
    pos2 = chaine.find(fin)
    rep = chaine[pos1 + len(debut): pos2]
    return rep


def if_not_parent(soup, type, classorid, nom):
    res = []
    for so in soup:
        if so.find_parent(type, {classorid, nom}) == None:
            res.append(so)
    return res


def get_date_com(lien):
    url = "https://www.tripadvisor.fr/" + lien
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    date = soup.find('span', {'class': 'ratingDate'})

    return date


def get_full_com(lien):
    url = "https://www.tripadvisor.fr/" + lien
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find('p', {'class': 'partial_entry'})


def tri_com(com):
    pos1 = com.find('<span class="fullText">')
    if pos1 != -1:
        pos2 = com.find("""</span>""")
        rep = com[pos1 + len('<span class="fullText">'): pos2]

    else:
        rep = com

    rep2 = rep.replace("<br/>", "\n")
    return rep2


def get_avis_user(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    notes_liste = []
    commentaire_liste = []
    date_liste = []

    pseudo = soup.find_all('span', {'class': '_2wpJPTNc _345JQp5A'})
    allnote = soup.find_all('span', {'class': 'ui_bubble_rating'})
    note = if_not_parent(allnote, 'div', 'class', 'rZtp3RDr _1RuUIMSG')
    date = soup.find_all('span', {'class': '_1_xw04A-'})

    dico = {"pseudo": prend_entre(str(pseudo[0]), '">', '</span>'), "note": notes_liste,
            "commentaire": commentaire_liste, "date": date_liste}

    for i in range(0, len(note)):
        dico["note"].append(int(prend_entre(str(note[i]), "rating bubble_", '"><')))
        dico["commentaire"].append(tri_com(prend_entre(str(get_full_com(date[i].a["href"])), '">', '</p>')))
        dico["date"].append(prend_entre(str(get_date_com(date[i].a["href"])), 'title="', '">'))
    return dico

def get_member_date(URL):
    a = get_avis_user(URL)  
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    member_date = str(soup.find('span', {'class' : '_1CdMKu4t'}))
    return member_date[71:-7]

def get_date_review(URL):
    a = get_avis_user(URL)
    date_review = a['date'][0]
    return date_review

def print_infos(URL):
    a = get_avis_user(URL)       
    for i in range(0, len(a["note"])):
        print("pseudo = ", a["pseudo"])
        print("note = ", a["note"][i])
        print("commentaire = ", a["commentaire"][i])
        print("date = ", a["date"][i])
    return '\n'


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def check_date(URL):
    a = get_avis_user(URL)

    member_date = get_member_date(URL)[14:]

    date_review = a['date'][0]

    return similar(date_review,member_date)



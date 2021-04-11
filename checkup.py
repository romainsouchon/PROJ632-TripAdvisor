import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from get_all_user_advice import *
import csv
from difflib import SequenceMatcher



def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def suspect_csv(liste):
	with open('suspect_users.csv','w', newline ='' ) as f:
		writer = csv.writer(f, delimiter = ';')
		writer.writerow(['Username', 'Membre depuis', 'Commentaire posté le','raison'])
		for row in liste:
			writer.writerow(row)



'''
test au niveau des dates de création de compte : on test si l'utilisateur a posté son commentaire 
au même moment qu'il a créer son compte => suspect 
'''
liste_users_suspect = []

with open('infos_from_users.csv','r', newline ='' ) as file:
	reader = csv.reader(file, delimiter = ';')
	for row in reader:
		if row[-1][-4:] == '2020' and row[2] == '1':

			# print('utilisateur :', row[1])
			# print(get_member_date(row[0]))
			# print('commentaire posté:', get_date_review(row[0]))
			simil = check_date(row[0])
			if simil > 0.70:
			# 	print('''l'utilisateur ''', row[1], ''' est suspect ''', '\n')
				suspect = [row[1],get_member_date(row[0]),get_date_review(row[0]),'commentaire posté au moment de la création du compte']
				liste_users_suspect.append(suspect)
				suspect_csv(liste_users_suspect)



	
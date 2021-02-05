import requests
from bs4 import BeautifulSoup

URL1 = 'https://www.tripadvisor.fr/Restaurant_Review-g8309764-d968592-Reviews-Brasserie_le_Z-Chambery_Savoie_Auvergne_Rhone_Alpes.html'
URL2 = 'https://www.tripadvisor.fr/Restaurant_Review-g8309764-d968592-Reviews-or10-Brasserie_le_Z-Chambery_Savoie_Auvergne_Rhone_Alpes.html'

URL = URL1   #MODIFIER ICI

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

#Utilisateurs
users = soup.find_all('div',{'class' : 'info_text pointer_cursor'})

#Notes
notes = soup.find_all('span', {'class' : 'ui_bubble_rating'})

#Ajustement notes
review_notes = []
for note in notes[5:15]:
    review_notes.append(str(note)[37:39])

#Commentaires            
com_entier = soup.find_all('div', {'class' : 'ui_column is-9'})
liste_com =[]
for k in range(len(com_entier)):
    com_entier_str=str(com_entier[k])
    indice_debut = com_entier_str.find('<p class="partial_entry">') + 25
    indice_fin1 = com_entier_str.find('</p></div></div><div class="prw_rup prw_reviews_stay_date_hsx" data-prwidget-init="" data-prwidget-name="reviews_stay_date_hsx">')
    indice_fin2 = com_entier_str.find('</p></div></div><div class="prw_rup prw_reviews_inline_photos_hsx" data-prwidget-init="" data-prwidget-name="reviews_inline_photos_hsx">')
    indice_fin=max(indice_fin1,indice_fin2)
    com = com_entier_str[indice_debut:indice_fin]
    liste_com.append(com)

#Dates
date = soup.find_all('span', {'class' : 'ratingDate'})
daterep = soup.find_all('span', {'class' : 'responseDate'})

#Info_user
info_users = soup.find_all('div', {'class' : 'member_info'})
'''print(info_users[0])'''


'''print('Tailles avant changements')
print('users :', len(users))
print('note :', len(note))
print('review :', len(review))
print('date :', len(date))

print('Tailles après changements')
print('users :', len(users))
print('note :', len(note))
print('review :', len(review))
print('date :', len(date), '\n')'''

for i in range(0, len(users)):
    print (users[i].string, '\n')
    print ('note :',review_notes[i], '\n')
    print (liste_com[i], '\n')
    print (date[i].string, '\n\n')



import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

URL1 = 'https://www.tripadvisor.fr/Restaurant_Review-g8309764-d968592-Reviews-Brasserie_le_Z-Chambery_Savoie_Auvergne_Rhone_Alpes.html'
URL2 = 'https://www.tripadvisor.fr/Restaurant_Review-g8309764-d968592-Reviews-or10-Brasserie_le_Z-Chambery_Savoie_Auvergne_Rhone_Alpes.html'

URL = URL1   #MODIFIER ICI

page = requests.get(URL)
uClient = uReq(URL)
page_html = uClient.read()
uClient.close()


soup = BeautifulSoup(page.content, 'html.parser')
users = soup.find_all('div',{'class' : 'info_text pointer_cursor'})
note = soup.find_all('span',{'class' : 'ui_bubble_rating'})
review = soup.find_all('p',{'class' : 'partial_entry'})
date = soup.find_all('span', {'class' : 'ratingDate'})
#print(date)
print('Tailles avant changements')
print('users :', len(users))
print('note :', len(note))
print('review :', len(review))
print('date :', len(date))

note = note[5:15]
print('Tailles après changements')
print('users :', len(users))
print('note :', len(note))
print('review :', len(review))
print('date :', len(date), '\n')

for i in range(0, len(users)-1):
    print (users[i].string, '\n')
    print (note[i], '\n')
    print (review[i].string, '\n\n')



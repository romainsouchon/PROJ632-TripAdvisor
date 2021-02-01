import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

URL = 'https://www.tripadvisor.fr/Restaurant_Review-g8309764-d968592-Reviews-Brasserie_le_Z-Chambery_Savoie_Auvergne_Rhone_Alpes.html'
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
print(len(users))
print(len(note))
print(len(review))
print(len(date))

for i in range(0, len(users)-1):
    print (users[i].string, '\n')
    print (review[i].string, '\n')
    print (note[i+5].class, '\n\n')


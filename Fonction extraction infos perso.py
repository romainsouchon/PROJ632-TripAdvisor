# -*- coding: utf-8 -*-

def extraction_infos_perso(URL_profil):
    ''' Fonction qui prend en argument l'URL d'un profil et qui retourne
    le ville d'origine de l'utilisateur (si elle existe) et la date de
    création de son profil'''
    ''' Nécessite l'importation de BeautifulSoup et requests'''
    ville_origine=""
    date_creation=""
    URL = URL_profil
    req = requests.get(URL)
    soup = BeautifulSoup(req.text, "lxml")
    ville = soup.find_all('span',{'class': '_2VknwlEe _3J15flPT default'})
    ville_origine = str(ville)[str(ville).find('></span>')+8:str(ville)[str(ville).find('></span>')+8:].find('</span>')+str(ville).find('></span>')+8]
    date = soup.find_all('span',{'class': '_1CdMKu4t'})
    date_creation = str(date)[str(date).find('></span>')+8:str(date)[str(date).find('></span>')+8:].find('</span>')+str(date).find('></span>')+8]
    return [ville_origine, date_creation]
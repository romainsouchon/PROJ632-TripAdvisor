def extraction_nb_contrib(liste_URL_profils):
    '''Fonction qui prend en argument une liste d'URL de page de profil
    et qui retourne une liste de listes indiquant le nombre
    de contributions pour chaque pseudo'''
    '''Nécessite l'importation de BeautifulSoup et requests'''
    liste_contributions = []
    for k in range(len(liste_URL_profils)):    
        URL1=liste_URL_profils[k]
        req = requests.get(URL1)
        soup = BeautifulSoup(req.text, "lxml")
        haut_profil = soup.find_all('a', {'class' : '_1q4H5LOk'})
        nb_contributions = str(haut_profil[0])[21:str(haut_profil[0]).find('</a>')]
        pseudo=liste_URL_profils[k][liste_URL_profils[k].find('Profile/')+8:]
        liste_contributions.append([pseudo, nb_contributions])
    return liste_contributions
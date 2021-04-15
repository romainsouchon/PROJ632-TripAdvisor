# PROJ632 TripAdvisor
## Goal 
A TripAdvisor project that prevent fake reviews for a restaurant.  
  
we took the restaurant : "BRASSERIE LE Z", 12 avenue des Ducs de Savoie, 73000 Chambéry France  
here is their TripAdvisor page : [Brasserie le Z](https://www.tripadvisor.fr/Restaurant_Review-g8309764-d968592-Reviews-Brasserie_le_Z-Chambery_Savoie_Auvergne_Rhone_Alpes.html)
## Milestones for the project
1- Get all the information we need on a user (note, date, comment,...)  
2- sort username from one page  
3- get all the username from all pages  
4- for one user, sort his information from his own account (his posts, his comments, ...)  
5- csv creation in order to have an access to url users   
6- compare with specifical information in order to know if it's a possible fake.

 -----------------------------------------
Results are situated in the "csv file".  
you can check the suspect_users.csv check who are the suspicious users concerning the date issues :  
for example a person who created his account and posted a comment the same time => it can be suspicious.
If you want to check some information of users from "Brasserie le Z", check the "infos_from_users.csv".

## How it works  
* First in order to get all some information on user from their comment, launch the "get_information all pages.py".    
* Then if you want more information but from one user, this is with "get_user_advice.py". In order to launch the "extract_info_from_users.py", we have to get all the users's url. * So "get_liste_urls_user.py" return a csv with all the urls.  
* Then "checkup.py" is able (but it remains increases) to analyse some criterias and write in "suspect_users.csv" all the users with a reason why they are suspect.

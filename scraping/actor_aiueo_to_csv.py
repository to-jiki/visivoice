import time
import requests
from bs4 import BeautifulSoup
import csv

top_char_b =["a","i","u","e","o"]
top_char_s =["", "k","s","t","n","h","m","y","r","w"]
top_char = []
csv_list = [["声優", "url"]]
url_names = []
for shiin in top_char_s:
    for boin in top_char_b:    
        if((shiin == "y" and (boin == "i" or boin == "e")) or ((shiin =="w") and boin != "a" )):
            continue
        top_char.append(shiin + boin)
        
for link in  top_char:
    url_names.append("https://sakuhindb.com/anime/alph_info/j/people_voice_" +link+".html")


for urlName in url_names:
    url = requests.get(urlName)
    soup = BeautifulSoup(url.content, "html.parser")
    
    all_man = soup.find_all(attrs = {"class":["man","female","no_sex"]})
    for actor in all_man:
        tag = actor.parent['href']
        name = actor.contents[0]
        csv_list.append([name, "https://sakuhindb.com/" + tag])
    
file = open("../data/aiueo_actor.csv","w")
writecsv = csv.writer(file, lineterminator='\n')

writecsv.writerows(csv_list)
file.close()
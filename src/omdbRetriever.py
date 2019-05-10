import pandas as pd
import numpy as np
import urllib

df_data = pd.read_csv("docs/raw.csv")
df_titles = df_data['Movie']
df_year = df_data['Released']
wrong_names = []
df_omdb = []
assert len(df_titles) == len(df_year)

'''for title,year in zip(df_titles,df_year):
    data = pd.read_json("http://www.omdbapi.com/?t=" + title + "&y=" + str(year) + "&plot=short&r=json&apikey=4465fefc")
    print(data)'''

for i in range(175, len(df_titles)):
    
    print(i, df_titles[i])
    link = "http://www.omdbapi.com/?t=" + str(df_titles[i]) + "&y="  + "&plot=short&r=json&apikey=4465fefc"

    # Parse movie titles to those in iMDB
    link = link.replace('Star Wars Ep. I: The Phantom Menace', 'Star Wars: Episode I - The Phantom Menace')
    link = link.replace('Star Wars Ep. II: Attack of the Clones', 'Star Wars: Episode II - Attack of the Clones')
    link = link.replace('Star Wars Ep. III: Revenge of the Sith', 'Star Wars: Episode III - Revenge of the Sith')
    link = link.replace('Star Wars Ep. IV: A New Hope', 'Star Wars: Episode IV - A New Hope')
    link = link.replace('Star Wars Ep. V: The Empire Strikes Back', 'Star Wars: Episode V - The Empire Strikes Back')
    link = link.replace('Star Wars Ep. VI: Return of the Jedi', 'Star Wars: Episode VI - Return of the Jedi')
    link = link.replace('Star Wars Ep. VII: The Force Awakens', 'Star Wars: Episode VII - The Force Awakens')
    link = link.replace('Star Wars Ep. VIII: The Last Jedi', 'Star Wars: The Last Jedi')
    link = link.replace('Harry Potter and the Deathly Hallows: Part II', 'Harry Potter and the Deathly Hallows: Part 2')
    link = link.replace('Harry Potter and the Deathly Hallows: Part I', 'Harry Potter and the Deathly Hallows: Part 1')
    link = link.replace('Fast and Furious 6', 'Fast & Furious 6')
    link = link.replace('Mission: Impossible 2', 'Mission: Impossible II')
    link = link.replace('X-Men 2', 'X2: X-Men United')
    link = link.replace('Doctor Seuss\' The Lorax', 'The Lorax')
    link = link.replace('Men in Black 2', 'Men in Black II')
    link = link.replace('Spider-Man: Into The Spider-Verse 3D', 'Spider-Man: Into The Spider-Verse')
    link = link.replace('Fantastic Four: Rise of the Silver Surfer', 'Fantastic 4: Rise of the Silver Surfer')
    link = link.replace('The Divergent Series: Insurgent', 'Insurgent')
    link = link.replace('Mamma Mia: Here We Go Again!', 'Mamma Mia! Here We Go Again')
    link = link.replace('I Now Pronounce You Chuck and Larry', 'I Now Pronounce You Chuck & Larry')
    link = link.replace('Lemony Snicket\'s A Series of Unfortunate Events', 'A Series of Unfortunate Events')
    link = link.replace('The Hangover 3', 'The Hangover Part III')
    link = link.replace('Crocodile Dundee 2', 'Crocodile Dundee II')
    link = link.replace('The Conjuring 2: The Enfield Poltergeist', 'The Conjuring 2')
    link = link.replace('Jackass Presents: Bad Grandpa', 'Bad Grandpa')
    link = link.replace('Cowboys and Aliens', 'Cowboys & Aliens')
    link = link.replace('Gnomeo and Juliet', 'Gnomeo & Juliet')
    link = link.replace('John Wick: Chapter Two', 'John Wick: Chapter 2')
    link = link.replace('Prince of Persia: Sands of Time', 'Prince of Persia: The Sands of Time')
    link = link.replace('Disney Planes', 'Planes')
    link = link.replace('Spy Kids 2: The Island of Lost Dreams', 'Spy Kids 2: Island of Lost Dreams')
    link = link.replace('SpongeBob SquarePants: The Movie', 'The SpongeBob SquarePants Movie')
    link = link.replace('Rocky 2', 'Rocky II')
    link = link.replace('AVP: Alien Vs. Predator', 'AVP: Alien Vs Predator')
    link = link.replace('Artificial Intelligence: AI', 'A.I. Artificial Intelligence')
    link = link.replace('La marche de l\'empereur', 'March of the Penguins')
    link = link.replace('Garfield: The Movie', 'Garfield')
    
    link = link.replace(' ', '%20')
    print(link)

    try:
        df_omdb.append(pd.read_json(link))
    except urllib.error.HTTPError as e: 
        ResponseData = ''
        #df_omdb.append({})
        wrong_names.append(str(df_titles[i]))
    except UnicodeEncodeError as e_2:
        wrong_names.append(str(df_titles[i]))
    # print(df_omdb)
print (wrong_names)
print (len(wrong_names))

#test = "http://www.omdbapi.com/?t=" + df_titles[1] + "&y=" + str(df_year[1]) + "&type=movie&r=json&ratings=true" + "&apikey=4465fefc"
#"http://www.omdbapi.com/?t=Avatar&y=&plot=short&r=json&apikey=4465fefc"
#test2 = pd.read_json(test)
#print(test)
#print(test2)
#print(df_year)
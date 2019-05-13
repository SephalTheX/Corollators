import pandas as pd
import numpy as np
import urllib

df_data = pd.read_csv("../data/raw.csv")
df_titles = df_data['Movie']

lst_imdb_ratings = []
lst_imdb_votes = []
lst_rotten_tomatoes = []
lst_metacritic = []
lst_released = []
lst_genre = []
invalid_ascii = []
invalid_link = []

for i in range(len(df_titles)):
    
    print(i, df_titles[i])
    link = "http://www.omdbapi.com/?t=" + str(df_titles[i]) + "&rottentomatoes=true&metacritic=true&apikey=a968f1d9"

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
    link = link.replace('Pirates of the Caribbean: The Curse of the Blac…', 'Pirates of the Caribbean: The Curse of the Black Pearl')
    link = link.replace('The Chronicles of Narnia: The Lion, the Witch a…', 'The Chronicles of Narnia: The Lion, the Witch and the Wardrobe')
    link = link.replace('The Chronicles of Narnia: The Voyage of the Daw…', 'The Chronicles of Narnia: The Voyage of the Dawn Treader')
    link = link.replace('The Naked Gun 2½: The Smell of Fear', 'The Naked Gun 2')
    link = link.replace('Teenage Mutant Ninja Turtles II: The Secret of …', 'Teenage Mutant Ninja Turtles II: The Secret of the Ooze')
    link = link.replace('Barnyard: The Original Party Animals', 'Barnyard')

    link = link.replace(' ', '%20')
    print(link)

    try:
        movie_data = pd.read_json(link)
        # IMDb
        print("IMDb rating:", movie_data.loc[0, 'imdbRating'])
        print("IMDb vote count:", movie_data.loc[0, 'imdbVotes'])
        lst_imdb_ratings.append(movie_data.loc[0, 'imdbRating'])
        lst_imdb_votes.append(movie_data.loc[0, 'imdbVotes'])
        lst_released.append(movie_data.loc[0, 'Released'])
        lst_genre.append(movie_data.loc[0, 'Genre'])
        # Rotten Tomatoes (str)
        if any(d['Source'] == 'Rotten Tomatoes' for d in movie_data['Ratings']):
            for d in movie_data['Ratings']:
                if d['Source'] == 'Rotten Tomatoes':
                    rTomatoes_rating = d['Value']
                    break
            print("Rotten Tomatoes: ", rTomatoes_rating)
            lst_rotten_tomatoes.append(rTomatoes_rating)
        else:
            print("Rotten Tomatoes: ", None)
            lst_rotten_tomatoes.append(None)
        # Metacritic (str)
        if any(d['Source'] == 'Metacritic' for d in movie_data['Ratings']):
            for d in movie_data['Ratings']:
                if d['Source'] == 'Metacritic':
                    metacritic_rating = d['Value']
                    break
            print("Metacritic: ", metacritic_rating)
            lst_metacritic.append(metacritic_rating)
        else:
            print("Metacritic: ", None)
            lst_metacritic.append(None)
    except urllib.error.HTTPError as e: 
        ResponseData = ''
        invalid_link.append(str(df_titles[i]))
    except UnicodeEncodeError as e_2:
        invalid_ascii.append(str(df_titles[i]))

assert not invalid_ascii
assert not invalid_link

assert len(lst_imdb_ratings) == len(lst_imdb_votes)
assert len(lst_imdb_votes) == len(lst_metacritic)
assert len(lst_metacritic) == len(lst_rotten_tomatoes)
assert len(lst_rotten_tomatoes) == len(df_titles)
assert len(lst_released) == len(df_titles)
assert len(lst_genre) == len(df_titles)

df_data['IMDb Ratings'] = lst_imdb_ratings # int
df_data['IMDB Votes'] = lst_imdb_votes # int
df_data['Metacritic'] = lst_metacritic # string
df_data['Rotten Tomatoes'] = lst_rotten_tomatoes # string
df_data['Released Month'] = lst_released 
df_data['Genre'] = lst_genre

# Uncomment to generate new one
df_data.to_csv('../data/omdb_joined.csv')
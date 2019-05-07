import pandas as pd
import numpy as np
import urllib

df_data = pd.read_csv("docs/raw.csv")
df_titles = df_data['Movie']
df_year = df_data['Released']
df_omdb = []
assert len(df_titles) == len(df_year)

'''for title,year in zip(df_titles,df_year):
    data = pd.read_json("http://www.omdbapi.com/?t=" + title + "&y=" + str(year) + "&plot=short&r=json&apikey=4465fefc")
    print(data)'''

for i in range(len(df_titles)):
    
    print(i, df_titles[i])
    link = "http://www.omdbapi.com/?t=" + df_titles[i] + "&y=" + str(df_titles[i]) + "&plot=short&r=json&apikey=4465fefc"
    print(link)
    try:
        df_omdb.append(pd.read_json(link))
    except urllib.error.HTTPError as e: 
        ResponseData = ''
        df_omdb.append({})
    print(df_omdb)

#test = "http://www.omdbapi.com/?t=" + df_titles[1] + "&y=" + str(df_year[1]) + "&type=movie&r=json&ratings=true" + "&apikey=4465fefc"
#"http://www.omdbapi.com/?t=Avatar&y=&plot=short&r=json&apikey=4465fefc"
#test2 = pd.read_json(test)
#print(test)
#print(test2)
#print(df_year)
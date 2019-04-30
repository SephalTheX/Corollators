import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup
#import urllib.request

ctx = []
row = []
links = ["https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time", "https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time/101", "https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time/201", "https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time/301", "https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time/401", "https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time/501", "https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time/601", "https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time/701", "https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time/801", "https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time/901", "https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time/1001"]
#links = ["https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time", "https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time/101"]
for i in links:
	res = requests.get(i)
	soup = BeautifulSoup(res.content, 'lxml')
	for j in soup.find_all('table'):
		ctx.append(pd.read_html(str(j)))
df = pd.DataFrame.from_records(ctx[0][0])
for i in np.arange(1, len(ctx),1):
	df1 = pd.DataFrame.from_records(ctx[i][0])
	df = df.append(df1,ignore_index = True)

df.to_csv("raw.csv")
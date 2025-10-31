import requests
from bs4 import BeautifulSoup

response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data=response.text

#creating soup
soup=BeautifulSoup(data,"html.parser")

movie_title=soup.select(selector='h3.title')


for movie in movie_title[::-1]:   #reversing the list order so movie names start from 1)
    with open("movies.txt","a") as file:
        file.write(f"{movie.getText()}\n")




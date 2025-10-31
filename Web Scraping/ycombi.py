#SCRAPING DATA FROM A LIVE WEBSITE
from bs4 import BeautifulSoup
import requests

# response=requests.get("https://news.ycombinator.com/news")

# print(response)   #returns 200 means the get requests was successful - get fetches the entire source from the url provided.
# content=response.text  #Returns the full source code from the url.

#Creating a file to feed the html code data from the website
# with open("ycombinator.html","w") as file:
#     file.write(content)
with open("ycombinator.html","r") as file:
    data=file.read()


#getting hold of the title and max points of it.

soup=BeautifulSoup(data,"html.parser")

#get hold of the news titles , by inspecting we saw have class titleline and a tag
tag=soup.select(selector='span.titleline a ')
org_link_to_rem=soup.select(selector='span.sitebit.comhead a')
article_title=[item for item in tag if item not in org_link_to_rem]
article_points=soup.select('span.score')
article_texts=[]
article_links=[]
article_upvote=[]

for title in article_title:
    article_texts.append(title.getText())
    article_links.append(title.get('href'))
    
for title in article_points:
    upvote=title.getText()
    vote=upvote.strip('points')
    article_upvote.append(int(vote))


#TO GET HOLD OF THE NEWS OF THE DAY WITH MAX. UPVOTES.
index_values=article_upvote.index(max(article_upvote)) # for votes in article_upvote:
                                #     if vote>index_values
                                #     index_values+=vote
    

def get_highlight_news():
    news_title=article_texts[index_values]
    news_link=article_links[index_values]
    
    print(f"HERE IS YOUR HIGHLIGHT TECH NEWS TODAY :\n{news_title}.READ MORE:👉👉{news_link}")
    
get_highlight_news()
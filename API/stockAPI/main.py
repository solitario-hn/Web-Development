import requests
import requests
from twilio.rest import Client
from newsapi import NewsApiClient
import os 
from dotenv import load_dotenv
load_dotenv()
NEWS_API= os.getenv("NEWS_API")
COMPANY_NAME = "Tesla Inc"
NEWS_URL="https://newsapi.org/v2/everything"
ACCOUNT_SDH=os.getenv("ACCOUNT_SDH")
AUTH_TOKEN=os.getenv("AUTH_TOKEN")
print(NEWS_API,"HOHCO")

NEWS_PARAMS={
    "q":COMPANY_NAME,
    "from":"2025-10-22",
    "to":"2025-10-21",
    "sortBy":"relevancy",
    "apikey":NEWS_API,
    "pageSize":10,
    'language':"en",
}

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_URL="https://www.alphavantage.co/query"
STOCK_API="SSBS5SBRBGNO30UT"
STOCK_PARAM={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "outputsize":"compact",
    "datatype":"json",
    "apikey":STOCK_API
}



# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock=requests.get(url=STOCK_URL,params=STOCK_PARAM)
stock.raise_for_status()
stock_data=stock.json()['Time Series (Daily)']
data=[value for (key,value) in stock_data.items()]


yesterday_closing=float(data[0]["4. close"])        #21 dec 
day_before_yesterday_closing=float(data[1]["4. close"])    #20 dec
diff=day_before_yesterday_closing-yesterday_closing
per=None
indicator=None
if diff>0:
    indicator='🔼'
elif diff<0:
    indicator='🔽'
    

# print(type(today_closing))    checking the type to ensure we can calculate percentage
def percentage(yes,day_before):
    diff=abs(day_before-yes)          #gives out the absolute difference removing any negative sign
    per=diff/day_before*100
    return per


def get_news():
    news_response=requests.get(url=NEWS_URL,params=NEWS_PARAMS)
    news_response.raise_for_status()
    news_data=news_response.json()['articles']
    top_articles=[item for item in news_data[0:3]]

    for article in top_articles:
        twilio_client=Client(ACCOUNT_SDH,AUTH_TOKEN)
        message = twilio_client.messages\
        .create(
            body=f"{STOCK},{COMPANY_NAME} {per} {indicator}\n\nHEADLINE:{article['title']}\n\n{article['description']}\n\n{article['content']} ",
            from_="+12762849782",to="+91 8743002178")  

   
if percentage(yesterday_closing,day_before_yesterday_closing)>5:
    get_news()
    


#Sample text message
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


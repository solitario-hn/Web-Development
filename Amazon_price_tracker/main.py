import requests
import smtplib
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

#What is a Header?

#When making a request to Amazon or any website, your browser will send some additional data along with the request. Typically this will be information regarding what browser you are using, what computer you have, and what your preferred language is. This information is included in the headers. By using the headers, Amazon's server can respond with the right website for your region and your language.
header={"Accept-Language":"en-US,en;q=0.9",
        "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"}
URL='https://www.amazon.in/iPhone-16-128-GB-Control/dp/B0DGJHBX5Y/ref=sr_1_1?crid=2F3D7DLB6BSBV&dib=eyJ2IjoiMSJ9.F11mcIhGiZDuohQOIomDgVr34v_2AF23NFPJVUIDAOUCyGubOm7aRjms1KpE9AtfjGPMbGlcZtf0QMZru7wIUmH3AoV9DcqBxgDVxWILnTJkObab40L5vhgP83pT5ICBVkgzrdb4nM_Qv4qbXxK6m80MdctIjdGJogI38BcAwJSGbUgq5orhOkzF7IoKPtkCgnLzX10D-K45mcMapFB6t1feAEtoDt_6g-1Sq5G5sYQ.B5Mv2H8HiKB7XeYFEYKeKb8oYY5wNdHqPMNu8wO72sg&dib_tag=se&keywords=i%2Bphone&qid=1761925435&sprefix=i%2Bphone%2Caps%2C204&sr=8-1&th=1'
load_dotenv()
my_email=os.getenv('MY_ADDRESS')
receiver_email=os.getenv("EMAIL_ADDRESS")
passwrd=os.getenv('EMAIL_PASSWORD')
response=requests.get(url=URL,headers=header)
response.raise_for_status()

data=response.text
rice=BeautifulSoup(data,"html.parser")
product_title=rice.find(class_='a-size-large product-title-word-break').getText()

price=rice.find(class_='a-price aok-align-center reinventPricePriceToPayMargin priceToPay').getText()    #
# print(type(price))
price_amt=float(price.replace(" ₹","").replace(",",""))

BUY_PRICE=100000

if price_amt<BUY_PRICE:
    message=f"Subject:Amazon Price Alert!\n\n{product_title} is on sale for {price_amt}\nLINK BELOW:👇👇{URL}"
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        try:
            connection.login(user=my_email,password=passwrd)
            connection.sendmail(from_addr=my_email,to_addrs=receiver_email,msg=message.encode("utf-8"))
            connection.close()
        except:
            print("An issue occured. Kindly connect to your email provider.")
    




   
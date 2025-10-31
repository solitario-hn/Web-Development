from dotenv import load_dotenv
import os 
import requests
from twilio.rest import Client
path=os.path.dirname(os.path.abspath(__file__))
load_dotenv(f"{path}/rain.env")            #load dotenv file

ENDPOINT="https://api.openweathermap.org/data/2.5/forecast"
API=os.getenv("API_KEY")
LAT=os.getenv("LATITUDE")
LONG=os.getenv("LONGITUDE")
ACCOUNT_SID=os.getenv("ACCOUNT_SDH")
AUTH=os.getenv("AUTH_TOKEN")

parameters={
    "lat":LAT,
    "lon":LONG,
    "appid":API,
    "cnt":4,
}

response=requests.get(url=ENDPOINT,params=parameters)
response.raise_for_status()
weather_data=response.json()

will_rain=False
for wea in weather_data["list"]:
    condition_code= wea["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True
        
if will_rain==True: 
    twilio_client=Client(ACCOUNT_SID,AUTH)
    message = twilio_client.messages\
    .create(
        body="IT MIGHT RAIN TODAY! BRING AN UMBRELLA SWEETIE!⛱☔ ",
        from_="+12762849782",to="+91 89685765654")  
    print(message.status)


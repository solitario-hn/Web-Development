import requests
from datetime import datetime 
import smtplib , time
MY_LANG=77.0348901960073
MY_LAT=28.629755993743597
MY_EMAIL="xtraa56789aa@gmail.com"
response=requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)   'it will print out a response class object with status code 200=process successfull"
def is_overhead():
    response.raise_for_status()                 #this attribute in response class raise exception for the returned responnse code .
    data=response.json()     #this stores all the json data into data var.
    longitude=float(data["iss_position"]["longitude"])
    latitude=float(data["iss_position"]["latitude"])
    iss_position=(longitude,latitude)

    if MY_LANG-5<=longitude<=MY_LANG+5 and MY_LAT-5<=latitude<=MY_LANG+5:
        return True
    
    



#USING SUNRISE SUNSET API TO GET THE INFO OF SUNRISE IN OUR LOCATION
#THIS API DOCUMENTATION STATES THAT IT NEEDS 'LAT' AND 'LANG' TWO PARAMETERS TO GET A RESPONSE. (KEEP THE SPELLING SAME AS IN DOCUMNETATION)


#creating a paramter dictionary to export the parameters with the request.

def is_night():
    paramters={
        "lat":MY_LAT,
        "lng":MY_LANG,
        "formatted":0                       #to return the time in 24hrs clock format
    }

    response2=requests.get(url="https://api.sunrise-sunset.org/json",params=paramters)
    response2.raise_for_status()   #incase theres a status error
    data2=response2.json()
    sunrise=int(data2["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data2["results"]["sunset"].split("T")[1].split(":")[0])   #we can use split function like this

    time_now=datetime.now().hour
     #returns the hour of the time
    if time_now<=sunrise or time_now>=sunset:
        return True
    

while True:      #the true loop will keep on looping till the iss position is just far away from you.
    if is_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com",587) as connection: #Without specifying 587, Python defaults to port 25, which Gmail either doesn't support for client submissions or heavily restricts, causing your connection delays.
            connection.starttls()   #TLS= TRANSPORT LAYER SECURITY is way of securing our connection to our email server. this would encyrpt our messages and provide security to us.
    #now since connection has been setup and secured let's login using username and password
            connection.login(user=MY_EMAIL,password="jztc faps afor jpzl")
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up In the Sky ISS IS ABOVE YOU!!\n\nHEY!LOOK THE SKIES ARE SHINIER TODAY ARE YOU?"
            )
    

#IF THE ISS TIME IS CLOSE (+5 -5 long lat to location) TO MY LOCATION TIME AND IT'S DARK THEN SEND ME A EMAIL.



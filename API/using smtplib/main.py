# from fastapi import FastAPI

# app=FastAPI()            #server

# @app.get("/")
# def read_root():
#     return {"message":"AC COOLER GREAT BRO!"}

# @app.post("/item")
# def fucn(user:str):
#     return {"username":user}

# import smtplib

# my_email="xtraa56789aa@gmail.com"

# with smtplib.SMTP("smtp.gmail.com",587) as connection: #Without specifying 587, Python defaults to port 25, which Gmail either doesn't support for client submissions or heavily restricts, causing your connection delays.
#     connection.starttls()   #TLS= TRANSPORT LAYER SECURITY is way of securing our connection to our email server. this would encyrpt our messages and provide security to us.
#     #now since connection has been setup and secured let's login using username and password

#     connection.login(user=my_email,password="jztc faps afor jpzl")

#     #after logging in to your own account , use sendmail method to send mail to other gmail acc
#     try:
#         connection.sendmail(from_addr=my_email,to_addrs="edaigiacaiolafe@gmail.com",msg="Subject:Hey!Connection Done.\n\nGOODNIGHT")  #using \n\n moves it to the body of the message
#         connection.close()
#     except:
#         print("an issue.")
#     else:
#         print("Email sent.")


#using datetime module

# import datetime as dt
# now=dt.datetime.now()        #tapping into datetime class from datetime module , and then it's now method
# year=now.year
# month=now.month
# day_of_the_week=now.weekday()   #returns 0==monday  and sunday==6




   
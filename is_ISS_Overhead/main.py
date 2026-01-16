# import requests
# from datetime import datetime
#
# MY_LAT= 51.507351 # you get this coordinate from lat/long website
# MY_LONG = -0.127758 #in this case we are using Angela's location in London
#
# parameters = {
#
#     "lat" : MY_LAT,  #these are both required parameters
#     "Lng" : MY_LONG,  #these are both required parameters
#     "formatted" : 0,
# }
#
#
#
#
#
#
# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters) #need to specify parameters in this get method
# response.raise_for_status() #this piece of code will give you an error if you do not provide the required API Parameters
# data = response.json() #formats sunset/sunrise data as JSON dictionary
#
# sunrise = data["results"]["sunrise"].split("T")[1] .split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1] .split(":")[0]
#
# #sunrise.split("T")[1] .split(":")[0] this code is giving us a list of what was before and after T in the sunrise/sunset dictionary and split it further with :
# #1 aobve gets hold of second list and what to split in second list which is :
#
# #now we need to get the current date and time
# time_now = datetime.now()
#
# """the format of date time is not the same format as our sunrise/sunset data
# thus we have to put in an optional parameter that gets the data formatted as
# the datetime data we then get that data and split it using the letter T --> giving
# us a list of what was before and after T"""

#2nd part of project
#If the ISS is close to my current position
#Then send me email to tell me to look uo
#Bonus: run the code every 60 seconds

import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"
MY_LAT = 40 # Your latitude
MY_LONG = 10 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json") #request ISS API
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"]) #getting ISS positions
    iss_longitude = float(data["iss_position"]["longitude"]) #getting ISS position

    #Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters) #parameters needed for location of sunrise and senset, thus your location
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour #turns this datetime.now() into an integer

    if time_now >= sunset or time_now <= sunrise: #lets us know if it is dark
        return True

while True: #sends email if the ISS is close and its at night so you can see it, this checks happens every 60 seconds
    time.sleep(60) #checks every 60 seconds
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )




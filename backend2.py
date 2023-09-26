import requests

# make a request to the API
apiKey = "c7b76719fbe4781adb2aa67ac72c1123"
def zipcodegrab(grabbedzip):
    grabbedzip = zipcodegrab(input("ZIP?"))

zip_code = input("What is your ZIP code?")
# store the requested data in a response variable
def runresponse():
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid={apiKey}&units=imperial")
    print(response.status_code)

    # store JSON data in a dictionary variable
    zip_data = response.json()
    print(zip_data)
    return zip_data


def displayzip(zip_data):
    # display the user's latitude and longitude
    print("You are currently in:", ["name"])
    lati = zip_data["lat"]
    longi = zip_data["lon"]

    lati = str(lati)
    longi = str(longi)

    print(f"Your latitude is: {lati} and your longitude is {longi} \n \n \n")
def secondcall():
    # transpose latitude and longitude into the caller URL
    secondcallURL = f"https://api.openweathermap.org/data/2.5/weather?lat={lati}&lon={longi}&appid=c7b76719fbe4781adb2aa67ac72c1123&units=imperial"

    # make second request to API
    secondresponse = requests.get(secondcallURL)


    weather = secondresponse.json()
    weathermain = weather["main"]
    for key, value in weather["main"].items():
        print(f"{key}:  {value}")

    temp = "temp"
    feels_like="feels_like"
    humidity = "humidity"

    # print the weather

    return weathermain
def weatherprint(weathermain):
    print(weathermain)
    print("TEST")
    if temp in weathermain:
        print(f"It's currently {weathermain[temp]} degrees F.")
    if feels_like in weathermain:
        print(f"It currently feels like {weathermain[feels_like]} degrees F.")
    if humidity in weathermain:
        print(f"The humidity index is {weathermain[humidity]} percent.")

    weatherprint()


zip_data = runresponse()

displayzip(zip_data)

weatherprint(displayzip)
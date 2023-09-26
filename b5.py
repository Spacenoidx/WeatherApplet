# import modules
import requests

# define API key
apiKey = "c7b76719fbe4781adb2aa67ac72c1123"

# ask for ZIP code
def askzip():
    zip_code = input("What is your ZIP code? ")
    return zip_code

# make a request to the API

def runresponse():
    zip_code = askzip()

    response = requests.get(
        f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid={apiKey}&units=imperial"
                            )
    print(f"Success! Status code {response.status_code}!")

    # store JSON data in a dictionary variable

    zip_data = response.json()
    return zip_data


# store the requested ZIP data in a response variable (func)

zip_data = runresponse()
coordinates = [zip_data["lat"], zip_data["lon"]]
name = zip_data['name']
lat = zip_data["lat"]
lon = zip_data["lon"]

#display latitude and longitude
def displaycoord():
    print(f"You are in: {name}")

    print(f"Your coordinates are: {lat} , {lon}")

# transpose latutude and longitude into the caller URL
displaycoord()
def secondcall():
    # transpose latitude and longitude into the caller URL
    secondcallURL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=c7b76719fbe4781adb2aa67ac72c1123&units=imperial"

    # make second request to API
    secondresponse = requests.get(secondcallURL)

    weather = secondresponse.json()
    weathermain = weather["main"]

    return weathermain

weathermain = secondcall()
print(weathermain)
def dictsearch(weathermain):
    if "temp" in weathermain:
        temp = weathermain["temp"]
        print(f"The current temperature is: {temp} degrees F.")

    if "feels_like" in weathermain:
        feels_like = weathermain["feels_like"]
        print(f"It currently feels like: {feels_like} degrees F.")

    if "temp_min" in weathermain:
        temp_min = weathermain["temp_min"]
        print(f"Today's low is: {temp_min} degrees F.")

    if "temp_max" in weathermain:
        temp_max = weathermain["temp_max"]
        print(f"Today's high is: {temp_max} degrees F.")

    if "humidity" in weathermain:
        humidity = weathermain["humidity"]
        print(f"The present humidity is: {humidity} percent.")



dictsearch(weathermain)
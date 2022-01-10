import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter Your City Name: ")

if city == "":
    print("City Name is Empty")
    exit()

API_KEY = "51f0963710a433139c3764db6f7f429c"

URL = BASE_URL + "q=" + city + "&appid=" + API_KEY

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    print("Weather: ", data["weather"][0]["description"])
    print("Temperature: {0:02f}℃".format(data["main"]["temp"] - 273.15))
    print("Feels Like: {0:.2f}℃".format(data["main"]["feels_like"] - 273.15))
    print("Humidity: ", data["main"]["humidity"])
    print("Wind Speed: ", data["wind"]["speed"])
else:
    print("Error: ", response.status_code)

#This class pulls data from openweathermap.org

#it gets current weather for a specific city
#and then calculates wet bulb temperature and wet bulb global temperature
#for that city

#that data is used to build a tweet
import requests
import json

class GetWeather():
    
    def __init__(self, cities) -> None:
        self.cities = cities

        #get API key
        file = open("../config.json")
        fileJson = json.load(file)
        self.key = fileJson["WEATHER_KEY"]


    def fetchCityWeather(self, city):
        #set lat and long
        lat = self.cities[city][0]
        lon = self.cities[city][1]

        #request weather data
        cityWeather = requests.get("https://api.openweathermap.org/data/2.5/weather?units=metric&lat={}&lon={}&appid={}".format(lat, lon, self.key))
        cityData = cityWeather.json()

    def calcWBT(self) -> float:
        pass

    def calcWBGT(self) -> float:
        pass

    def needsTweet(self) -> bool:
        pass

    


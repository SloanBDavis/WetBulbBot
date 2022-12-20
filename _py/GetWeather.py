#This class pulls data from openweathermap.org

#it gets current weather for a specific city
#and then calculates wet bulb temperature and wet bulb global temperature
#for that city

#that data is used to build a tweet
import requests
import json
import math

class GetWeather():
    
    def __init__(self, cities) -> None:
        self.cities = cities

        #get API key
        file = open("../config.json")
        fileJson = json.load(file)
        self.key = fileJson["WEATHER_KEY"]


    def calcWBT(self, temp, relHumidity) -> None:
        #formula is Tw = T * arctan[0.151977 * (rh% + 8.313659)^(1/2)] + arctan(T + rh%) - arctan(rh% - 1.676331) + 0.00391838 *(rh%)^(3/2) * arctan(0.023101 * rh%) - 4.686035
        #                    1                                           2                 3                                                  4
        arctan1 = math.atan( 0.151977 * ( (relHumidity + 8.313659) ** (1/2) ) )
        arctan2 = math.atan(temp + relHumidity)
        arctan3 = math.atan(relHumidity - 1.676331)
        arctan4 = math.atan(0.023101 * relHumidity)

        self.wbt = temp * arctan1 + arctan2 - arctan3 + ( 0.00391838 *(relHumidity) ** (3/2) ) * arctan4 - 4.686035

    def fetchCityWeather(self, city):
        #set lat and long
        lat = self.cities[city][0]
        lon = self.cities[city][1]

        #request weather data
        cityWeather = requests.get("https://api.openweathermap.org/data/2.5/weather?units=metric&lat={}&lon={}&appid={}".format(lat, lon, self.key))
        cityData = cityWeather.json()
        self.calcWBT(cityData["main"]["temp"], cityData["main"]["humidity"])

    def needsTweet(self) -> bool:
        if(self.wbt >= 26):
            return True
        return False

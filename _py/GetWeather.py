#This class pulls data from openweathermap.org

#it gets current weather for a specific city
#and then calculates wet bulb temperature and wet bulb global temperature
#for that city

#that data is used to build a tweet

from tokenize import Double


class GetWeather():
    
    def __init__(self) -> None:
        pass

    def fetchCityWeather(self, city):
        pass

    def calcWBT(self) -> float:
        pass

    def calcWBGT() -> float:
        pass

    def needsTweet(self) -> bool:
        pass
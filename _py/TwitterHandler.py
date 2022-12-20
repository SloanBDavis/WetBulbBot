#Purpose of this script is to authorize the twitter bot account 
#and secure a access token and refresh token

import requests
import json
#for oauth2
from requests_oauthlib import OAuth2Session
#to parse url queries
from urllib.parse import urlparse
from urllib.parse import parse_qs


class TwitterHandler():
    def __init__(self) -> None:
        #load file and init 
        file = open("../config.json")
        self.data = json.load(file)
        file.close()
        self.accessToken = {}
        self.refreshToken = ""

        #setup needed network variables
        self.client_ID = self.data["CLIENT_ID"]
        self.client_Secret = self.data["CLIENT_SECRET"]
        self.redirectURI = "https://www.sloandavis.com"
        self.scope = ["tweet.read","tweet.write","users.read", "offline.access"]
        self.codeVerifier = self.data["CODE_VERIFIER"]
        self.basicAuth = self.data["BASIC_AUTH"]
        self.codeChallenge = self.data["CODE_CHALLENGE"]

        #create oauth instance
        self.oauth = OAuth2Session(client_id=self.client_ID, redirect_uri=self.redirectURI, scope=self.scope)

    def getAuthURL(self) -> str:
        """Generates a url to navigate to authorize bot account. Returns auth code"""
       
        #generate a url to get auth code from
        authURL = self.oauth.authorization_url("https://twitter.com/i/oauth2/authorize", code_challenge=self.codeChallenge, code_challenge_method="s256", state="state")
        return authURL
    #end getAuthURL
    

    def authorize(self, redirectURL) -> None:
        """saves Auth code and refresh token"""
        
        #parse auth code from the url that oauth gives after login
        parseUrl = urlparse(redirectURL)
        authCode = parse_qs(parseUrl.query)["code"][0]

        #build access token request
        parameters = {"grant_type": "authorization_code", "client_id": self.client_ID, "redirect_uri": r"{}".format(self.redirectURI), "code_verifier": r"{}".format(self.codeVerifier), "code": authCode}
        headerContent = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization": "Basic {}".format(self.basicAuth)}

        #request access token
        getTokenR = requests.post(
            "https://api.twitter.com/2/oauth2/token",
            headers=headerContent,
            params=parameters
        )
        #response from twitter token api
        jsonResponse = getTokenR.json()

        #read config data
        with open("../config.json", "r") as file:
            fileData = json.load(file)

        #update config file contents
        fileData["ACCESS_TOKEN"] = jsonResponse["access_token"]
        fileData["REFRESH_TOKEN"] = jsonResponse["refresh_token"]

        #update classs date instance
        self.data = fileData
       
        #update config file
        with open("../config.json", "w") as file:
            json.dump(fileData, file)
    #end authorize
        

    def refresh(self) -> None:
        """Uses refresh token to get new authorization code"""
        header = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "Basic {}".format(self.data["BASIC_AUTH"])}
        queries = {"refresh_token" : self.data["REFRESH_TOKEN"], "grant_type" : "refresh_token"}

        refreshRequest = requests.post("https://api.twitter.com/2/oauth2/token", headers=header, params=queries)
        jsonResponse = refreshRequest.json()


        #read config data
        with open("../config.json", "r") as file:
            fileData = json.load(file)

        #update config file contents
        fileData["ACCESS_TOKEN"] = jsonResponse["access_token"]
        fileData["REFRESH_TOKEN"] = jsonResponse["refresh_token"]

        #update class data instance
        self.data = fileData
       
        #update config file
        with open("../config.json", "w") as file:
            json.dump(fileData, file)
    #end refresh

    def buildTweet(self, city) -> str:
        #if wbt is potentially deadly
        if(self.wbt >= 35):
            text = "If you live in #{}, strongly consider going inside. The weather (WBT) outside is dangerous at {:.2f}C".format(city, self.wbt)
            return text
        #if wbt is high
        text = "If you live in #{}, please stay cool and consider going inside. The heat (WBT) outside is potentially dangerous at {:.2f}C".format(city, self.wbt)
        return text

    def sendTweet(self, twtText: str) -> None:

        #build data for request
        body = {"text" : twtText}
        header = {"Authorization" : "Bearer {}".format(self.data["ACCESS_TOKEN"])}
        
        #send tweet request
        tweetRequest = requests.post(
            "https://api.twitter.com/2/tweets", 
            headers=header, 
            json=body
        )
    #end sendTweet

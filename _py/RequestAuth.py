#Purpose of this script is to authorize the twitter bot account 
#and secure a access token and refresh token

import requests
import json
#for oauth2
from oauthlib.oauth2 import WebApplicationClient
from requests_oauthlib import OAuth2Session
#to parse url queries
from urllib.parse import urlparse
from urllib.parse import parse_qs


class RequestAuth():
    def __init__(self) -> None:
        #load file and init 
        self.file = open("../config.json")
        self.data = json.load(self.file)
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
    
    def authorize(self, redirectURL) -> str:
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
        
    def refresh(self, refreshToken):
        """Uses refresh token to get new authorization code"""
        pass


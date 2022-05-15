#script runner
import time
import RequestAuth

def initialize():
    auth = RequestAuth.RequestAuth()
    url = auth.getAuthURL()
    print(url)

    redirectURL = input("Redirect URL: ")

    auth.authorize(redirectURL)

    pass

if __name__ == "__main__":
    initialize()
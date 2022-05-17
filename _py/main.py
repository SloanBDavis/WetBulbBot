#script runner
from msvcrt import getwch
import time
import RequestAuth
import GetWeather

cities = {
    "Coatzacoalcos" : [18.1345, -94.4590],
    "Macapa" : [0.0405, -51.0561],
    "Santo Antonio" : [-6.310940, -35.479580],
    "Sapele" : [5.8751, 5.6931],
    "Hulhumale" : [4.2106, 73.5388],
    "Patna" : [25.5941, 85.1376],
    "Bhubaneshwar" : [20.2961, 85.8245],
    "Cuttack" : [20.4625, 85.8245],
    "Satkhira" : [22.3155, 89.1115],
    "Khulna" : [22.8456, 89.5403],
    "Sittwe" : [20.1528, 92.8677],
    "Guwahati" : [26.1445, 91.7362],
    "Haora" : [22.5958, 88.2636],
    "Kolkata" : [22.5726, 88.3639],
    "Gaya" : [24.7914, 85.0002],
    "Mawlamvine" : [16.4543, 97.6440],
    "Sylhet" : [24.8949, 91.8687],
    "Jessore" : [23.1778, 89.1801],
    "Durgapur" : [23.5204, 87.3119],
    "Barisal" : [22.7010,90.3535],
    "Comilla" : [23.4607, 91.1809],
    "Varanasi" : [25.3176, 82.9739],
    "Saidpur" : [25.7830, 82.9739],
    "Hpa-an" : [16.8759, 97.6440],
    "Rangpur" : [25.7439, 89.2752]
}

def initialize():
    auth = RequestAuth.RequestAuth()
    url = auth.getAuthURL()
    print(url)

    redirectURL = input("Redirect URL: ")

    auth.authorize(redirectURL)

if __name__ == "__main__":
    initialize()
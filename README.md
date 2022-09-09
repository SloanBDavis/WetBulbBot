# WetBulbBot   

*Visit the docs folder for a project log*

This project is a Twitter bot that updates followers on dangerous weather, called wet bulb conditions, in certain cities around the globe. It will tweet that the weather conditions in a city are potentially dangerous if wet bulb temperature reaches above [26C](https://research.noaa.gov/article/ArtMID/587/ArticleID/2621/Dangerous-humid-heat-extremes-occurring-decades-before-expected). If WBT is above 35C it will tweet that the temperature is dangerous. At 35C, being outside for long periods of time is [potentially deadly](https://research.noaa.gov/article/ArtMID/587/ArticleID/2621/Dangerous-humid-heat-extremes-occurring-decades-before-expected)

### What are Wet Bult Conditions

"The Wet Bulb temperature is the temperature of adiabatic saturation. This is the temperature indicated by a moistened thermometer bulb exposed to the air flow." [Source](https://www.weather.gov/source/zhu/ZHU_Training_Page/definitions/dry_wet_bulb_definition/dry_wet_bulb.html)

### Technologies Used
- Twitter Authentication uses OAuth2
- Utilizes Twitter API v2
- Weather Data is collected via [openweathermap.org](https://openweathermap.org/)
- The program is written entirely in python 3.10.4
- Used Modules
    1. requests 2.27.1
    2. requests-oauthlib 1.3.1
    3. json
    4. math
    5. urllib.parse

### Current Cities Supported

**To request to add a city or correct a current one, dm [@heat_humidity](https://twitter.com/heat_humidity)**

City name : [latitude, longitude]
- Coatzacoalcos : [18.1345, -94.4590]
- Macapa [0.0405, -51.0561],
- Santo Antonio : [-6.310940, -35.479580]
- Sapele : [5.8751, 5.6931]
- Hulhumale : [4.2106, 73.5388]
- Patna : [25.5941, 85.1376]
- Bhubaneshwar : [20.2961, 85.8245]
- Cuttack : [20.4625, 85.8245]
- Satkhira : [22.3155, 89.1115]
- Khulna : [22.8456, 89.5403]
- Sittwe : [20.1528, 92.8677]
- Guwahati : [26.1445, 91.7362]
- Haora : [22.5958, 88.2636]
- Kolkata : [22.5726, 88.3639]
- Gaya : [24.7914, 85.0002]
- Mawlamvine : [16.4543, 97.6440]
- Sylhet : [24.8949, 91.8687]
- Jessore : [23.1778, 89.1801]
- Durgapur : [23.5204, 87.3119]
- Barisal : [22.7010, 90.3535]
- Comilla : [23.4607, 91.1809]
- Varanasi : [25.3176, 82.9739]
- Saidpur : [25.7830, 82.9739]
- Hpa-an : [16.8759, 97.6440]
- Rangpur : [25.7439, 89.2752]
- Kuwait City : [29.3759, 47.9774]
- Dammam : [26.4207, 50.0888]
- Manama : [26.2235, 50.5876]


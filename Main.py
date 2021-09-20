from tuya_iot import TuyaOpenAPI
from requests import get
import random

ipAddress = get('https://api.ipify.org').text

accessId = ''
accessKey = ''

ENDPOINT = "https://openapi.tuyaus.com"

userName = ''
passWord = ''

FINGERBOT_DEVICE_ID = ''
LIGHTSTRIP_DEVICE_ID = ''

DARK_BLUE = {'h': 246, 's': 100, 'v': 100}
LIGHT_BLUE = {'h': 193, 's': 56, 'v': 100}
WHITE = {'h': 1, 's': 1, 'v': 100}
ORANGE = {'h': 23, 's': 90, 'v': 100}
YELLOW = {'h': 62, 's': 81, 'v': 100}
RED = {'h': 1, 's': 100, 'v': 100}

openapi = TuyaOpenAPI(ENDPOINT, accessId, accessKey)
openapi.login(userName, passWord)


def get_weather():
	location_url = f'/v1.0/iot-03/locations/ip?ip={PUBLIC_IP}'
	location = openapi.get(location_url)['result']
	lat, lon = location['latitude'], location['longitude']

	weather_url = f"/v2.0/iot-03/weather/current?lat={lat}&lon={lon}"
	weather = openapi.get(weather_url)['result']['current_weather']['temp']
	return weather
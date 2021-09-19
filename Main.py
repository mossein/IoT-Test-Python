from tuya_iot import TuyaOpenAPI
from requests import get
import random

ipAddress = get('https://api.ipify.org').text

accessId = ''
accessKey = ''

# For more info: https://developer.tuya.com/en/docs/iot/api-request?id=Ka4a8uuo1j4t4
ENDPOINT = "https://openapi.tuyaus.com"

userName = ''
passWord = ''
#data.nba.net/prod/v1/today.json
#gives you links you want
#json - javascript object notation

#pip insall requests

from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/toda.json"

data = get(BASE_URL + ALL_JSON).json()
#print(response) will give a gabage value to the terminal

printer.pprint(data)